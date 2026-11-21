#!/usr/bin/env python3
"""Comprobaciones a resolución completa sobre el video ya codificado (gratis): cortes en la rejilla,
tramos sin cambio y bucle. Uso: python3 codigo/comprobar_video.py [video]"""
import subprocess
import sys
from pathlib import Path

import numpy as np

PROY = Path(__file__).resolve().parent.parent
video = sys.argv[1] if len(sys.argv) > 1 else str(PROY / "06_final" / "tin_y_tan_short01_v1.mp4")
W, H = 540, 960
r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", video, "-vf", f"scale={W}:{H},format=gray",
                    "-f", "rawvideo", "-"], capture_output=True)
fr = np.frombuffer(r.stdout, dtype=np.uint8).reshape(-1, H, W).astype(np.float32)
d = np.abs(fr[1:] - fr[:-1]).mean(axis=(1, 2))          # d[i]: cambio entre el fotograma i y el i+1
print(f"fotogramas: {len(fr)}")
esperados = [0.5, 1.0, 3.5, 5.0, 6.5, 9.5, 12.0, 14.5, 17.0, 18.5, 20.5, 23.5, 25.5, 27.0, 28.0]
print("cortes (cambio medio 0-255 en el fotograma del corte; mediana de sus 10 vecinos):")
for t in esperados:
    f = int(round(t * 30))
    vec = np.median(np.concatenate([d[max(0, f - 7):f - 3], d[f + 2:f + 6]]))
    print(f"  {t:5.1f} s  fotograma {f:3d}  cambio {d[f - 1]:6.2f}  vecinos {vec:5.2f}")
otros = [int(i) + 1 for i in np.argsort(d)[::-1][:25] if d[i] > 4 and all(abs((i + 1) - round(t * 30)) > 2 for t in esperados)]
print("cambios grandes fuera de la rejilla (movimiento dentro de la toma, no cortes; fotogramas):", sorted(otros) or "ninguno")
quietos, ini = [], None
for i, v in enumerate(d):
    if v < 0.01:
        ini = i if ini is None else ini
    else:
        if ini is not None and i - ini >= 15:
            quietos.append((ini / 30, i / 30))
        ini = None
print("tramos de 0,5 s o más sin ningún cambio:", [f"{a:.2f}-{b:.2f}" for a, b in quietos] or "ninguno")
print(f"cambio mínimo por fotograma en todo el video: {d.min():.4f}")
print(f"bucle: diferencia media entre el último fotograma (899) y el 0: {np.abs(fr[-1] - fr[0]).mean():.3f} (0-255)")
vacios = [i for i in range(len(fr)) if fr[i].std() < 3]
print("fotogramas vacíos (imagen plana):", vacios or "ninguno")
