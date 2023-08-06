#!/usr/bin/python

import subprocess
import sys
from dataclasses import dataclass, field
from os.path import expanduser
from pathlib import Path
from re import finditer, fullmatch
from shutil import rmtree
from tempfile import NamedTemporaryFile
from typing import List
from urllib.request import urlopen
from zipfile import ZipFile

from .manager import ExtensionManager
from .schema import AvailableExtension, InstalledExtension
from .store import GnomeExtensionStore


@dataclass
class FilesystemExtensionManager(ExtensionManager):
    """
    Handle extensions with basic filesystem operations
    """

    store: GnomeExtensionStore
    user_folder: Path = field(
        default=Path(expanduser("~/.local/share/gnome-shell/extensions"))
    )
    system_folders: List[Path] = field(
        default_factory=lambda: [
            Path("/usr/share/gnome-shell/extensions"),
            Path("/usr/local/share/gnome-shell/extensions"),
        ]
    )

    def get_current_shell_version(self) -> str:
        stdout = subprocess.check_output(
            ["gnome-shell", "--version"],
            text=True,
        )
        matcher = fullmatch(r"GNOME Shell (?P<version>[0-9.]+)", stdout.strip())
        assert matcher is not None, "Cannot retrieve Gnome Shell version"
        return matcher.group("version")

    def list_installed_extensions(self) -> List[InstalledExtension]:
        out = {}
        for folder in filter(Path.is_dir, self.system_folders + [self.user_folder]):
            for subfolder in sorted(folder.iterdir()):
                metadata_file = subfolder / "metadata.json"
                if metadata_file.is_file():
                    ext = InstalledExtension(subfolder)
                    out[ext.uuid] = ext
        return list(out.values())

    def install_extension(self, ext: AvailableExtension) -> bool:
        assert (
            ext.download_url is not None
        ), f"Cannot find recommended version for {ext.uuid}"
        self.disable_uuids([ext.uuid])
        target_dir = self.user_folder / ext.uuid
        if target_dir.exists():
            rmtree(target_dir)
        target_dir.mkdir(parents=True)
        try:
            with NamedTemporaryFile() as tmp:
                with urlopen(f"{self.store.url}{ext.download_url}") as stream:
                    tmp.write(stream.read())
                tmp.seek(0)
                with ZipFile(tmp.name) as zipfile:
                    for member in zipfile.namelist():
                        zipfile.extract(member, path=target_dir)
            self.enable_uuids([ext.uuid])
        except BaseException:  # pylint: disable=broad-except
            rmtree(str(target_dir))
            return False
        return True

    def uninstall_extension(self, ext: InstalledExtension):
        assert not ext.read_only, f"Cannot uninstall a system extension {ext.uuid}"
        self.disable_uuids([ext.uuid])
        rmtree(ext.folder)

    def edit_extension(self, ext: InstalledExtension):
        raise NotImplementedError()

    def list_enabled_uuids(self) -> List[str]:
        stdout = subprocess.check_output(
            ["gsettings", "get", "org.gnome.shell", "enabled-extensions"],
            text=True,
        )
        uuids = [m.group("uuid") for m in finditer(r"'(?P<uuid>[^']+)'", stdout)]
        return uuids

    def set_enabled_uuids(self, uuids: List[str]):
        uuids_text = ",".join((f"'{uuid}'" for uuid in uuids))
        subprocess.check_call(
            [
                "gsettings",
                "set",
                "org.gnome.shell",
                "enabled-extensions",
                f"[{uuids_text}]",
            ]
        )
        self.restart_gnome_shell()

    def restart_gnome_shell(self) -> bool:
        proc = subprocess.run(
            [
                "dbus-send",
                "--session",
                "--type=method_call",
                "--dest=org.gnome.Shell",
                "/org/gnome/Shell",
                "org.gnome.Shell.Eval",
                'string:"global.reexec_self();"',
            ],
            check=False,
        )
        if proc.returncode != 0:
            print(
                "Could not restart Gnome Shell, you have to restart it manually",
                file=sys.stderr,
            )
        return proc.returncode == 0
