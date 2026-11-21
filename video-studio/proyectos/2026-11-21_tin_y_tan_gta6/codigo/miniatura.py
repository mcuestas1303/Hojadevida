#!/usr/bin/env python3
"""Portada del short 2 de Tin & Tan (1080x1920), dibujada con el mismo código del video.

Uso (desde la carpeta del proyecto):
    python3 codigo/miniatura.py [salida.png]          # por defecto 06_final/portada_short02.png
    python3 codigo/miniatura.py --alternativa [png]   # el «4,811 days» en tomate (06_final/portada_short02_alternativa.png)

Sección 8 del prompt: la portada es el fotograma 0 (el mando con «GTA 5?»). Aquí es el mismo dibujo del fotograma 0
(mando en ángulo 0 con su estela), con el texto más grande y más abajo: en el video el «GTA 5?» va en y = 15 % (288 px)
y la zona útil de la portada de un Short es x 60-960, y 380-1440 (manual/12, control 4.5; ENTREGA_YOUTUBE.md).
No adelanta la respuesta. La alternativa es el fotograma de 23,0 s tal cual, para probar en otra publicación.
"""
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render as R  # noqa: E402
import palitos  # noqa: E402

W, H = 1080, 1920
UTIL = (60, 380, 960, 1440)


def portada(salida):
    lz = palitos.Lienzo(W, H)
    R.mando_grande(lz, 0.0)                      # centro en 54 %: de y = 800 a 1273
    img = lz.resultado()
    segs = (R.T("GTA "), R.K("5"), R.T("?"))     # mismas palabras que el fotograma 0; «GTA» es sigla, va en mayúsculas
    tam = 230
    tx, margen, linea = R.imagen_texto(segs, tam)
    k = 1 / palitos.SS
    chico = tx.resize((int(tx.width * k), int(tx.height * k)), Image.LANCZOS)
    x, y = 108 - int(margen * k), 430
    caja = chico.getbbox()
    assert UTIL[0] <= x + caja[0] and x + caja[2] <= UTIL[2] and UTIL[1] <= y + caja[1] and y + caja[3] <= 780, \
        "el texto de la portada sale de la zona útil o toca el mando"
    img.paste(chico, (x, y), chico)
    salida.parent.mkdir(parents=True, exist_ok=True)
    img.save(salida, optimize=True)
    print(f"Portada -> {salida} ({img.size[0]}x{img.size[1]}, {salida.stat().st_size / 1024:.0f} KB; "
          f"texto de x = {x + caja[0]} a {x + caja[2]}, y = {y + caja[1]} a {y + caja[3]})")


def alternativa(salida):
    img = R.fotograma(int(23.0 * R.FPS))
    salida.parent.mkdir(parents=True, exist_ok=True)
    img.save(salida, optimize=True)
    print(f"Portada alternativa (fotograma de 23,0 s) -> {salida}")


def main():
    args = sys.argv[1:]
    if args and args[0] == "--alternativa":
        return alternativa(Path(args[1]) if len(args) > 1 else R.PROY / "06_final" / "portada_short02_alternativa.png")
    portada(Path(args[0]) if args else R.PROY / "06_final" / "portada_short02.png")


if __name__ == "__main__":
    main()
