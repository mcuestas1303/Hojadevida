#!/usr/bin/env python3
"""Portada del short 3 de Tin & Tan (1080x1920): es el fotograma 0 del video, tal cual.

Uso (desde la carpeta del proyecto):
    python3 codigo/miniatura.py [salida.png]          # por defecto 06_final/portada_short03.png

Regla del dueño (ENTREGA_YOUTUBE.md, «Portada de los Shorts»): el primer segundo del video ES la portada. Aquí: «Back In /
11 Days?» entre y = 400 y 700, la silla de director vacía en el centro (y 720-1100), las caras de Tan y Tin dentro de
la zona útil (x 60-960, y 380-1440) mirando la silla, y el lápiz bumerán en el pasillo, sin tocar texto, silla ni
caras (FIRMA_LAPIZ_BUMERAN.md, §3 y §11). Este archivo no dibuja nada propio: guarda el fotograma 0 y mide las cajas.
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render as R  # noqa: E402

UTIL = (60, 380, 960, 1440)          # zona útil de la portada de un Short
PAPEL = np.array([0xF3, 0xE9, 0xD2])


def _caja(m):
    ys, xs = np.where(m)
    return int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())


def _cerca(a, hexa, tol=40):
    c = np.array([int(hexa[i:i + 2], 16) for i in (1, 3, 5)])
    return np.abs(a - c).sum(axis=2) < tol


def medidas(img):
    """Cajas (x0, y0, x1, y1) del texto, de la silla, del lápiz y de las dos caras, medidas sobre los píxeles."""
    a = np.asarray(img, dtype=np.int16)
    P = R.PALETA
    tinta = _cerca(a, P["tinta"], 60)
    marron = _cerca(a, P["marron"])
    mostaza = _cerca(a, P["mostaza"])
    texto = (tinta | mostaza).copy()
    texto[715:] = False                                   # por encima de la silla solo hay texto
    silla = (tinta | marron).copy()
    silla[:715] = False
    silla[1105:] = False
    silla[:, :300] = False
    silla[:, 780:] = False
    lapiz = mostaza.copy()
    lapiz[:1105] = False
    lapiz[1400:] = False
    lapiz[:, :330] = False
    lapiz[:, 750:] = False
    izq = np.zeros(a.shape[:2], bool)
    izq[1105:1500, :540] = True
    der = np.zeros(a.shape[:2], bool)
    der[1105:1500, 720:] = True
    tan = (_cerca(a, P["verde_azulado"]) | _cerca(a, P["verde_azulado_osc"])) & izq      # cabeza y rodete
    tin = (_cerca(a, P["naranja"]) | (marron & der)) & der                                # cabeza y gorra
    return {"texto": _caja(texto), "silla": _caja(silla), "lápiz": _caja(lapiz), "cara de Tan": _caja(tan),
            "cara de Tin": _caja(tin)}


def dentro(c, zona):
    return zona[0] <= c[0] and zona[1] <= c[1] and c[2] <= zona[2] and c[3] <= zona[3]


def separacion(a, b):
    dx = max(b[0] - a[2], a[0] - b[2], 0)
    dy = max(b[1] - a[3], a[1] - b[3], 0)
    return (dx ** 2 + dy ** 2) ** 0.5


def portada(salida):
    img = R.fotograma(0)
    m = medidas(img)
    assert dentro(m["texto"], (UTIL[0], 400, UTIL[2], 700)), f"texto fuera de la franja y 400-700: {m['texto']}"
    assert R.TAM_PORTADA >= 120, "letra de menos de 120 px"
    assert dentro(m["silla"], (UTIL[0], 715, UTIL[2], 1105)), f"silla fuera de la franja y 720-1100: {m['silla']}"
    for quien in ("cara de Tan", "cara de Tin", "lápiz"):
        assert dentro(m[quien], UTIL), f"{quien} fuera de la zona útil: {m[quien]}"
    sep = {k: separacion(m["lápiz"], m[k]) for k in ("texto", "silla", "cara de Tan", "cara de Tin")}
    assert sep["texto"] >= 30 and sep["silla"] >= 30 and sep["cara de Tan"] > 0 and sep["cara de Tin"] > 0, sep
    salida.parent.mkdir(parents=True, exist_ok=True)
    img.save(salida, optimize=True)
    print(f"Portada (fotograma 0) -> {salida} ({img.size[0]}x{img.size[1]}, {salida.stat().st_size / 1024:.0f} KB)")
    print(f"  letra de {R.TAM_PORTADA:.0f} px, dos renglones, 4 palabras")
    for k, c in m.items():
        print(f"  {k}: x {c[0]}-{c[2]}, y {c[1]}-{c[3]}")
    print("  separación del lápiz (px, entre cajas): " + ", ".join(f"{k} {v:.0f}" for k, v in sep.items()))
    print(f"  ancho del lápiz: {m['lápiz'][2] - m['lápiz'][0] + 1} px ({100 * (m['lápiz'][2] - m['lápiz'][0] + 1) / 1080:.0f} % del ancho)")


if __name__ == "__main__":
    portada(Path(sys.argv[1]) if len(sys.argv) > 1 else R.PROY / "06_final" / "portada_short03.png")
