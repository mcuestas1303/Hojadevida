#!/usr/bin/env python3
"""Crea una serie nueva a partir de la plantilla.

Uso:
    python3 nueva_serie.py <nombre> [--copiar-reglas-de <serie existente>]

Crea series/<nombre>/ con serie.md, entorno.md, temario.md y referencias/.
Con --copiar-reglas-de, parte de la biblia de una serie que ya funciona (por
ejemplo granja) en lugar de la plantilla vacia: quedan sus reglas de ritmo,
idiomas y revision, y hay que cambiar elenco, lugar, estructura y frases.
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

ESTUDIO = Path(__file__).resolve().parent.parent


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("nombre")
    p.add_argument("--copiar-reglas-de")
    a = p.parse_args()
    if not re.fullmatch(r"[a-z0-9_]+", a.nombre):
        sys.exit("El nombre va en minúsculas, sin espacios ni acentos.")
    destino = ESTUDIO / "series" / a.nombre
    if destino.exists():
        sys.exit(f"Ya existe: {destino}")
    shutil.copytree(ESTUDIO / "plantillas" / "serie", destino)
    (destino / "referencias").mkdir()
    (destino / "referencias" / ".gitkeep").touch()
    if a.copiar_reglas_de:
        origen = ESTUDIO / "series" / a.copiar_reglas_de / "serie.md"
        if not origen.is_file():
            shutil.rmtree(destino)
            sys.exit(f"No existe la serie de origen: {a.copiar_reglas_de}")
        aviso = (f"> COPIADA de la serie `{a.copiar_reglas_de}` el día de su creación. Revisar y cambiar: elenco permitido,\n"
                 "> quiénes salen, la pareja, estructura, frases fijas, estilo y publicación. Borrar este aviso al terminar.\n\n")
        (destino / "serie.md").write_text(aviso + origen.read_text())
    print(f"Serie creada: {destino.relative_to(ESTUDIO)}")
    print("Sigue el MANUAL.md, fase 2.")


if __name__ == "__main__":
    main()
