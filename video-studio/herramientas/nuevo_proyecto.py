#!/usr/bin/env python3
"""Crea la carpeta de un video nuevo a partir de la plantilla.

Uso:
    python3 nuevo_proyecto.py <nombre> [video_de_referencia]

Si se pasa un video de referencia, lo copia a 01_referencia/ y lo analiza.
"""
import datetime
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

ESTUDIO = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    limpio = unicodedata.normalize("NFKD", sys.argv[1]).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "_", limpio.lower()).strip("_")
    if not slug:
        sys.exit("El nombre no tiene letras ni números.")
    destino = ESTUDIO / "proyectos" / f"{datetime.date.today():%Y-%m-%d}_{slug}"
    if destino.exists():
        sys.exit(f"Ya existe: {destino}")
    shutil.copytree(ESTUDIO / "plantillas" / "proyecto", destino)
    print(f"Proyecto creado: {destino}")
    if len(sys.argv) == 3:
        ref = Path(sys.argv[2])
        if not ref.is_file():
            sys.exit(f"No existe el video de referencia: {ref}")
        copia = destino / "01_referencia" / f"referencia{ref.suffix.lower()}"
        shutil.copy2(ref, copia)
        subprocess.run([sys.executable, str(Path(__file__).with_name("analizar_video.py")),
                        str(copia), str(destino / "01_referencia" / "analisis")], check=True)


if __name__ == "__main__":
    main()
