#!/usr/bin/env python3
"""Portada del short 2 de Tin & Tan (1080x1920): es el fotograma 0 del video, tal cual.

Uso (desde la carpeta del proyecto):
    python3 codigo/miniatura.py [salida.png]          # por defecto 06_final/portada_short02.png
    python3 codigo/miniatura.py --alternativa [png]   # el «4,811 days» en tomate (06_final/portada_short02_alternativa.png)

Regla del dueño (ENTREGA_YOUTUBE.md, «Portada de los Shorts»; manual/12, control 4.5): el primer segundo del video ES
la portada. Por eso el «GTA 5?» de las tomas 1 y 13 ya va en el video al 12 % del alto y entre y = 400 y 700, dentro de
la zona útil (x 60-960, y 380-1440), y este archivo no dibuja nada propio: guarda el fotograma 0 y comprueba la caja
del texto. No adelanta la respuesta. La alternativa (fotograma de 23,0 s) sí la adelanta: solo para probar aparte.
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render as R  # noqa: E402

TEXTO_PORTADA = (R.T("GTA "), R.K("5"), R.T("?"))     # el mismo de la fila 1 de la tabla de textos (2 palabras)


def caja_del_texto(img):
    """Caja de lo que no es papel por encima del mando (y < 760): el texto de la portada."""
    a = np.asarray(img, dtype=np.int16)[:760]
    m = np.abs(a - np.array([0xF3, 0xE9, 0xD2])).sum(axis=2) > 90
    ys, xs = np.where(m)
    return int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())


def portada(salida):
    assert R.TEXTOS[0][4] == TEXTO_PORTADA
    img = R.fotograma(0)
    x0, y0, x1, y1 = caja_del_texto(img)
    assert 60 <= x0 and x1 <= 960 and 400 <= y0 and y1 <= 700, f"texto fuera de la franja de portada: {x0, y0, x1, y1}"
    salida.parent.mkdir(parents=True, exist_ok=True)
    img.save(salida, optimize=True)
    print(f"Portada (fotograma 0) -> {salida} ({img.size[0]}x{img.size[1]}, {salida.stat().st_size / 1024:.0f} KB; "
          f"texto de x = {x0} a {x1}, y = {y0} a {y1})")


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
