#!/usr/bin/env python3
"""Da de alta un personaje nuevo a partir de la plantilla.

Uso:
    python3 nuevo_personaje.py <id> "<Nombre>" "<rol en una frase>" [--publico "<publico>"]

Crea personajes/<id>/ con su ficha, la carpeta de referencias y las carpetas de
prompts (intro, capitulos, shorts, otros), y lo anota en personajes/REGISTRO.md.
El personaje no se puede usar en un prompt hasta completar la ficha, incluida
la seccion "Definición para generar", y guardar al menos una imagen aprobada.
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

ESTUDIO = Path(__file__).resolve().parent.parent
PERSONAJES = ESTUDIO / "personajes"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("id")
    p.add_argument("nombre")
    p.add_argument("rol")
    p.add_argument("--publico", default="por definir")
    a = p.parse_args()
    if not re.fullmatch(r"[a-z0-9_]+", a.id):
        sys.exit("El id va en minúsculas, sin espacios ni acentos (letras, números y guion bajo).")
    destino = PERSONAJES / a.id
    if destino.exists():
        sys.exit(f"Ya existe: {destino}")
    shutil.copytree(PERSONAJES / "_plantilla", destino)
    for carpeta in ("intro", "capitulos", "shorts", "otros"):
        (destino / "prompts" / carpeta).mkdir(parents=True)
        (destino / "prompts" / carpeta / ".gitkeep").touch()
    ficha = destino / "ficha.md"
    t = ficha.read_text()
    t = t.replace("# Ficha de personaje", f"# {a.nombre}", 1)
    t = t.replace("- **ID:** `@id_del_personaje`", f"- **ID:** `@{a.id}`", 1)
    t = t.replace("- **Nombre:**", f"- **Nombre:** {a.nombre}", 1)
    t = t.replace("- **Rol / arquetipo:**", f"- **Rol / arquetipo:** {a.rol}", 1)
    ficha.write_text(t)
    registro = PERSONAJES / "REGISTRO.md"
    lineas = registro.read_text().splitlines()
    ultima = max(i for i, l in enumerate(lineas) if l.startswith("| `@"))
    lineas.insert(ultima + 1, f"| `@{a.id}` | {a.nombre} | {a.rol} | {a.publico} | `{a.id}/ficha.md` |")
    registro.write_text("\n".join(lineas) + "\n")
    print(f"Personaje creado: {destino.relative_to(ESTUDIO)}")
    print("Falta: completar la ficha (bloque de identidad y «Definición para generar») y guardar la imagen aprobada en referencias/.")
    print("Sigue el MANUAL.md, fase 1.")


if __name__ == "__main__":
    main()
