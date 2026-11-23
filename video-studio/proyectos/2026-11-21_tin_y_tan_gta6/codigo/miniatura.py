#!/usr/bin/env python3
"""Portada del short 2 de Tin & Tan (1080x1920): es el fotograma 0 del video, tal cual.

Uso (desde la carpeta del proyecto):
    python3 codigo/miniatura.py [salida.png]          # por defecto 06_final/portada_short02.png
    python3 codigo/miniatura.py --alternativa [png]   # el «4,811 days» en tomate (06_final/portada_short02_alternativa.png)

Regla del dueño (ENTREGA_YOUTUBE.md, «Portada de los Shorts»; manual/12, control 4.5): el primer segundo del video ES
la portada. Por eso las tomas 1 y 13 del video ya son la portada: «GTA 5?» al 12 % del alto entre y = 400 y 700, el
mando en el centro (y 720-1100) y las caras de Tan y Tin dentro de la zona útil (x 60-960, y 380-1440), mirando el
mando. Este archivo no dibuja nada propio: guarda el fotograma 0 y mide las cajas del texto, el mando y las caras. No adelanta la respuesta. La alternativa (fotograma de 23,0 s) sí la adelanta: solo para probar aparte.
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render as R  # noqa: E402

TEXTO_PORTADA = (R.T("GTA "), R.K("5"), R.T("?"))     # el mismo de la fila 1 de la tabla de textos (2 palabras)


UTIL = (60, 380, 960, 1440)          # zona útil de la portada de un Short
PAPEL = np.array([0xF3, 0xE9, 0xD2])


def _caja(m):
    ys, xs = np.where(m)
    return int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())


def _cerca(a, hexa, tol=40):
    c = np.array([int(hexa[i:i + 2], 16) for i in (1, 3, 5)])
    return np.abs(a - c).sum(axis=2) < tol


def medidas(img):
    """Cajas (x0, y0, x1, y1) del texto, del mando y de las dos caras en la portada, medidas sobre los píxeles."""
    a = np.asarray(img, dtype=np.int16)
    no_papel = np.abs(a - PAPEL).sum(axis=2) > 90
    texto = no_papel.copy()
    texto[715:] = False                                   # por encima del mando solo hay texto
    banda = np.zeros_like(no_papel)
    banda[715:1105] = True                                # la franja del objeto
    mando = no_papel & banda
    izq = np.zeros_like(no_papel)
    izq[1105:1500, :540] = True
    der = np.zeros_like(no_papel)
    der[1105:1500, 540:] = True
    P = R.PALETA
    tan = (_cerca(a, P["verde_azulado"]) | _cerca(a, P["verde_azulado_osc"])) & izq      # cabeza y rodete
    tin = (_cerca(a, P["naranja"]) | _cerca(a, P["marron"]) | _cerca(a, P["marron_claro"])) & der   # cabeza y gorra
    return {"texto": _caja(texto), "mando": _caja(mando), "cara de Tan": _caja(tan), "cara de Tin": _caja(tin)}


def dentro(c, zona, margen=0):
    return zona[0] - margen <= c[0] and zona[1] - margen <= c[1] and c[2] <= zona[2] + margen and c[3] <= zona[3] + margen


def portada(salida):
    assert R.TEXTOS[0][4] == TEXTO_PORTADA
    img = R.fotograma(0)
    m = medidas(img)
    tam = R.ajustar(TEXTO_PORTADA, R.TEXTOS[0][2])
    assert dentro(m["texto"], (UTIL[0], 400, UTIL[2], 700)), f"texto fuera de la franja y 400-700: {m['texto']}"
    assert tam >= 120 and len("GTA 5?".split()) <= 4, "letra de menos de 120 px o más de 4 palabras"
    assert dentro(m["mando"], (UTIL[0], 720, UTIL[2], 1100)), f"mando fuera de la franja y 720-1100: {m['mando']}"
    for quien in ("cara de Tan", "cara de Tin"):
        assert dentro(m[quien], UTIL), f"{quien} fuera de la zona útil: {m[quien]}"
    salida.parent.mkdir(parents=True, exist_ok=True)
    img.save(salida, optimize=True)
    print(f"Portada (fotograma 0) -> {salida} ({img.size[0]}x{img.size[1]}, {salida.stat().st_size / 1024:.0f} KB)")
    print(f"  letra de {tam:.0f} px")
    for k, c in m.items():
        print(f"  {k}: x {c[0]}-{c[2]}, y {c[1]}-{c[3]}")


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
