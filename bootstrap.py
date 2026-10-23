#!/usr/bin/env python3
"""Instala ajustes portables sin sobreescribir identidades ni secretos."""

import argparse
import datetime
import os
from pathlib import Path
import shlex
import shutil
import sys


ROOT = Path(__file__).resolve().parent
MARKER = "# entorno-gabriel"


def backup(path):
    if path.exists():
        stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        destination = path.with_name(path.name + ".backup-" + stamp)
        index = 1
        while destination.exists():
            destination = path.with_name(path.name + ".backup-" + stamp + "-" + str(index))
            index += 1
        shutil.copy2(str(path), str(destination))
        print("Copia de seguridad:", destination)


def write_if_changed(path, content, apply):
    original = path.read_text(encoding="utf-8") if path.exists() else None
    if original == content:
        print("Sin cambios:", path)
        return
    print(("Actualizar: " if original is not None else "Crear: ") + str(path))
    if apply:
        path.parent.mkdir(parents=True, exist_ok=True)
        backup(path)
        path.write_text(content, encoding="utf-8")


def append_once(path, line, apply):
    original = path.read_text(encoding="utf-8") if path.exists() else ""
    if line in original:
        print("Ya configurado:", path)
        return
    suffix = "" if not original or original.endswith("\n") else "\n"
    write_if_changed(path, original + suffix + line + "\n", apply)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="aplicar los cambios")
    args = parser.parse_args()
    home = Path.home()
    destination = home / ".config" / "entorno-gabriel"
    for name in ("gitconfig.shared", "shell.sh", "Microsoft.PowerShell_profile.ps1"):
        write_if_changed(destination / name,
                         (ROOT / "config" / name).read_text(encoding="utf-8"),
                         args.apply)

    if os.name == "nt":
        profile = home / "Documents" / "PowerShell" / "Microsoft.PowerShell_profile.ps1"
        script_path = str(destination / "Microsoft.PowerShell_profile.ps1").replace("'", "''")
        source = ". '" + script_path + "' " + MARKER
        append_once(profile, source, args.apply)
    else:
        source = ". " + shlex.quote(str(destination / "shell.sh")) + " " + MARKER
        profiles = [p for p in (home / ".bash_profile", home / ".bashrc", home / ".zshrc") if p.exists()]
        if not profiles:
            profiles = [home / ".bashrc"]
        for profile in profiles:
            append_once(profile, source, args.apply)

    gitconfig = home / ".gitconfig"
    include_line = "\tpath = " + str(destination / "gitconfig.shared")
    existing = gitconfig.read_text(encoding="utf-8") if gitconfig.exists() else ""
    if include_line in existing:
        print("Git ya configurado:", gitconfig)
    else:
        addition = "\n[include]\n" + include_line + "\n"
        write_if_changed(gitconfig, existing.rstrip("\n") + addition, args.apply)

    print("Configuración aplicada." if args.apply else "Vista previa. Usa --apply para aplicar.")
    if shutil.which("git") is None:
        print("Aviso: instala Git antes de usar los alias.", file=sys.stderr)


if __name__ == "__main__":
    main()
