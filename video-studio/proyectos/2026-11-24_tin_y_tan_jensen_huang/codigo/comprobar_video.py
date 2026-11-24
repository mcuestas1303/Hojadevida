#!/usr/bin/env python3
"""Comprobaciones a resolución completa sobre el video ya codificado (gratis): formato, cortes en la rejilla,
tramos sin cambio, bucle, fotogramas vacíos, zona segura del texto, banda de subtítulos y sonoridad del archivo.
Uso: python3 codigo/comprobar_video.py [video]   (adaptado del short 2)"""
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tiempos as tm  # noqa: E402

PROY = Path(__file__).resolve().parent.parent
video = sys.argv[1] if len(sys.argv) > 1 else str(PROY / "06_final" / "tin_y_tan_short03_v1.mp4")
FPS, N_ESPERADO = 30, tm.N
esperados = tm.CORTES[1:-1]

r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                    "stream=codec_name,pix_fmt,width,height,r_frame_rate,nb_frames,sample_rate:format=duration,size",
                    "-of", "json", video], capture_output=True, text=True, check=True)
info = json.loads(r.stdout)
v = next(s for s in info["streams"] if s["codec_name"] == "h264")
a = next(s for s in info["streams"] if s["codec_name"] != "h264")
print(f"formato: {v['codec_name']} {v['width']}x{v['height']} {v['pix_fmt']} {v['r_frame_rate']} fps, {v['nb_frames']} fotogramas; "
      f"audio {a['codec_name']} {a['sample_rate']} Hz; duración {float(info['format']['duration']):.3f} s; "
      f"{int(info['format']['size']) / 1e6:.2f} MB")
ok_formato = (v["width"], v["height"], v["pix_fmt"], v["r_frame_rate"], int(v["nb_frames"]), a["codec_name"]) == \
    (1080, 1920, "yuv420p", "30/1", N_ESPERADO, "aac")
print(f"formato pedido (1080x1920, 30 fps, H.264, yuv420p, AAC, {N_ESPERADO} fotogramas):", "sí" if ok_formato else "NO")

W, H = 540, 960
r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", video, "-vf", f"scale={W}:{H},format=gray",
                    "-f", "rawvideo", "-"], capture_output=True)
fr = np.frombuffer(r.stdout, dtype=np.uint8).reshape(-1, H, W).astype(np.float32)
d = np.abs(fr[1:] - fr[:-1]).mean(axis=(1, 2))          # d[i]: cambio entre el fotograma i y el i+1
print(f"fotogramas leídos: {len(fr)}")
print("cortes (cambio medio 0-255 en el fotograma del corte; mediana de sus vecinos):")
for t in esperados:
    f = int(round(t * FPS))
    vec = np.median(np.concatenate([d[max(0, f - 7):f - 3], d[f + 2:f + 6]]))
    print(f"  {t:5.1f} s  fotograma {f:3d}  cambio {d[f - 1]:6.2f}  vecinos {vec:5.2f}  {'corte' if d[f - 1] > 4 * max(vec, 0.3) else 'REVISAR'}")
otros = [int(i) + 1 for i in np.argsort(d)[::-1][:25] if d[i] > 4 and all(abs((i + 1) - round(t * FPS)) > 2 for t in esperados)]
print("cambios grandes fuera de la rejilla (movimiento dentro de la toma, no cortes; fotogramas):", sorted(otros) or "ninguno")
quietos, ini = [], None
for i, x in enumerate(d):
    if x < 0.01:
        ini = i if ini is None else ini
    else:
        if ini is not None and i - ini >= 15:
            quietos.append((ini / FPS, i / FPS))
        ini = None
print("tramos de 0,5 s o más sin ningún cambio:", [f"{a:.2f}-{b:.2f}" for a, b in quietos] or "ninguno")
print(f"cambio mínimo por fotograma en todo el video: {d.min():.4f}")
print(f"bucle: diferencia media entre el último fotograma ({len(fr) - 1}) y el 0: {np.abs(fr[-1] - fr[0]).mean():.3f} (0-255); "
      f"cambio medio entre fotogramas vecinos del plano de cierre: {np.median(d[-25:]):.3f}")
vacios = [i for i in range(len(fr)) if fr[i].std() < 3]
print("fotogramas vacíos (imagen plana):", vacios or "ninguno")
cortes = tm.CORTES
print("mitad de abajo del cuadro (desviación de gris; < 3 = vacía):",
      ", ".join(f"T{i + 1} {fr[int((cortes[i] + cortes[i + 1]) / 2 * FPS)][H // 2:].std():.0f}" for i in range(14)))
# Zona segura: fuera de x 100-980 e y 250-1670 no debe haber tinta de texto (a media resolución: x 50-490, y 125-835).
oscuro = fr < 90
fuera_arriba = [i for i in range(len(fr)) if oscuro[i][:125].any()]
fuera_lados = [i for i in range(len(fr)) if oscuro[i][:480, :50].any() or oscuro[i][:480, 490:].any()]
print("fotogramas con tinta por encima de y = 250:", fuera_arriba or "ninguno")
print("fotogramas con tinta fuera de x 100-980 en la mitad de arriba (texto y gráficos):", fuera_lados or "ninguno")
# Banda de subtítulos: en la portada (primer y último segundo) no hay panel ni texto en y 905-1085 salvo la silla.
blanco = [i for i in range(len(fr)) if fr[i].mean() > 250]
print("fotogramas casi blancos a pantalla completa (media > 250):", blanco or "ninguno", f"(máxima media: {fr.mean(axis=(1, 2)).max():.0f})")

r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", video, "-af", "ebur128=peak=true", "-f", "null", "-"],
                   capture_output=True, text=True)
res = r.stderr[r.stderr.rfind("Summary:"):]
lufs = float(re.search(r"I:\s+(-?[\d.]+) LUFS", res).group(1))
pico = float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", res).group(1))
print(f"audio del archivo (AAC): {lufs:.1f} LUFS integrados, pico real {pico:.1f} dBTP "
      f"({'dentro' if abs(lufs + 14) <= 1 and pico <= -1 else 'FUERA'} de -14 ±1 LUFS y -1 dBTP)")
r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", video, "-af", "silencedetect=noise=-50dB:d=0.3", "-f", "null", "-"],
                   capture_output=True, text=True)
print("silencios totales de 0,3 s o más (a -50 dB):", re.findall(r"silence_start: [\d.]+", r.stderr) or "ninguno")
print(f"pico (llegada de 4,382): {tm.LLEGA:.2f} s = {100 * tm.LLEGA / tm.DUR:.1f} % de {tm.DUR} s; la voz entra en "
      f"{tm.VOZ_ENTRA:.3f} s y termina en {tm.E(11):.2f} s ({tm.DUR - tm.E(11):.2f} s sin voz hasta el empalme)")
