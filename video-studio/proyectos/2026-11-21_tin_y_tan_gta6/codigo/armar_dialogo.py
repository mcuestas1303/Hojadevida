#!/usr/bin/env python3
"""Arma 05_audio/dialogo_110.mp3: el diálogo del short 2 de Tin & Tan («How Many Days Did We Wait for GTA 6?»).

Método del canal (canales/nostalgia-tin-y-tan/voces.md, el mismo del short 1): cada voz normalizada a -14 LUFS, cada
línea recortada por sus pausas medidas, acelerada un 10 % sin cambiar el tono (atempo=1.10) y separada de la siguiente
por 0,23 s de silencio. Novedad de este short: las pausas internas largas (tras «So,» y «Wow,» en Tan, y las de Tin que
pasan de 0,35 s) se acortan a 0,15 s (medidos ya al 110 %); cada tramo lleva un fundido de 8 ms para que no haga clic.
Escribe también 05_audio/linea_de_tiempo_voz.md con los tiempos medidos. Gratis: solo ffmpeg y numpy.

Los tramos se midieron con `silencedetect=noise=-35dB:d=0.12` (2026-11-21). NADIE HA ESCUCHADO las voces: el texto de
cada tramo es el probable según el orden del guion y la duración; hay que comprobarlo al oído antes de publicar.
"""
import json
import re
import subprocess
import tempfile
import wave
from pathlib import Path

import numpy as np

AUDIO = Path(__file__).resolve().parent.parent / "05_audio"
SR = 48000
SILENCIO = 0.23          # entre líneas
PAUSA_INTERNA = 0.15     # pausa interna acortada (en el diálogo final, ya al 110 %)
TEMPO = 1.10
MARGEN = 0.03
FUNDIDO = 0.008
TAN, TIN = "voz_tan_zelda.wav", "voz_tin_kevin.wav"

# (quién, texto exacto del guion, archivo, tramos [(desde, hasta, texto probable del tramo)]) — tiempos del archivo
# original. Dos tramos en una línea = pausa interna larga que se acorta a PAUSA_INTERNA. Las pausas internas cortas
# (0,16 a 0,24 s) no se tocan y quedan dentro de su tramo.
LINEAS = [
    ("Tan", "Remember buying G T A five at midnight?", TAN, [(0.481, 2.532, "Remember buying G T A five at midnight?")]),
    ("Tan", "So, how many days did we wait for G T A six?", TAN,
     [(3.497, 4.077, "So,"), (4.880, 7.332, "how many days did we wait for G T A six?")]),
    ("Tin", "G T A five came out September seventeenth, twenty thirteen.", TIN,
     [(0.396, 4.145, "G T A five came out September seventeenth, twenty thirteen.")]),
    ("Tin", "Thirteen years times three sixty-five: four thousand, seven hundred forty-five days.", TIN,
     [(4.839, 6.947, "Thirteen years times three sixty-five:"), (7.421, 10.107, "four thousand, seven hundred forty-five days.")]),
    ("Tin", "Add three leap days: four thousand, seven hundred forty-eight.", TIN,
     [(10.555, 11.924, "Add three leap days:"), (12.318, 14.754, "four thousand, seven hundred forty-eight.")]),
    ("Tin", "Plus sixty-three days: September seventeenth to November nineteenth.", TIN,
     [(16.264, 19.915, "Plus sixty-three days: September seventeenth to November nineteenth.")]),
    ("Tin", "Four thousand, eight hundred eleven days.", TIN,
     [(20.531, 21.292, "Four thousand,"), (21.724, 23.113, "eight hundred eleven days.")]),
    ("Tan", "Wow, that long?", TAN, [(8.244, 8.760, "Wow,"), (9.446, 10.340, "that long?")]),
    ("Tin", "A baby born that day is a teenager now.", TIN, [(23.628, 25.600, "A baby born that day is a teenager now.")]),
]
TRAMOS_ESPERADOS = {TAN: 5, TIN: 9}      # los de 05_audio/voces_generadas.md


def ff(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args], check=True)


def leer(ruta):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(ruta), "-ar", str(SR), "-ac", "1",
                        "-f", "f32le", "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32).astype(np.float64)


def guardar(ruta, x):
    y = np.clip(np.round(x * 32767.0), -32768, 32767).astype("<i2")
    with wave.open(str(ruta), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(y.tobytes())


def tramos_medidos(ruta, umbral=-35, minimo=0.25):
    """Tramos con voz según silencedetect (pausas de `minimo` s o más), para comprobar la cuenta de tramos."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(ruta), "-af",
                        f"silencedetect=noise={umbral}dB:d={minimo}", "-f", "null", "-"], capture_output=True, text=True)
    ini = [float(v) for v in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    fin = [float(v) for v in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    dur = float(re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr).group(3))
    bordes = [0.0]
    for a, b in zip(ini, fin + [dur] * (len(ini) - len(fin))):
        bordes += [a, b]
    bordes.append(dur)
    return [(a, b) for a, b in zip(bordes[::2], bordes[1::2]) if b - a > 0.05]


def trozo(x, desde, hasta):
    a, b = int(max(0, desde - MARGEN) * SR), min(len(x), int((hasta + MARGEN) * SR))
    y = x[a:b].copy()
    n = int(FUNDIDO * SR)
    y[:n] *= np.linspace(0, 1, n)
    y[-n:] *= np.linspace(1, 0, n)
    return y


def main():
    avisos = []
    for nombre, esperados in TRAMOS_ESPERADOS.items():
        n = len(tramos_medidos(AUDIO / nombre))
        usados = sum(len(l[3]) for l in LINEAS if l[2] == nombre)
        estado = "coincide" if n == esperados == usados else "NO COINCIDE"
        print(f"  {nombre}: {n} tramos medidos, {esperados} esperados, {usados} usados: {estado}")
        if estado != "coincide":
            avisos.append(f"{nombre}: {n} tramos medidos frente a {esperados} esperados y {usados} usados")
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        normal = {}
        for nombre in (TAN, TIN):
            ruta = tmp / f"norm_{nombre}"
            ff("-i", str(AUDIO / nombre), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", str(SR), "-ac", "1", str(ruta))
            normal[nombre] = leer(ruta)
        partes, filas, t = [], [], 0.0
        for i, (quien, texto, archivo, tramos) in enumerate(LINEAS, 1):
            x = normal[archivo]
            piezas, cortes = [], []
            for j, (desde, hasta, _) in enumerate(tramos):
                if j:
                    # la pausa interna se mide en el diálogo final: aquí va 1,10 veces más larga, menos los márgenes
                    piezas.append(np.zeros(int(max(0.0, PAUSA_INTERNA * TEMPO - 2 * MARGEN) * SR)))
                    cortes.append(sum(len(p) for p in piezas) / SR / TEMPO)     # dónde empieza el tramo 2 (al 110 %)
                piezas.append(trozo(x, desde, hasta))
            cruda, pieza = tmp / f"cruda_{i}.wav", tmp / f"linea_{i}.wav"
            guardar(cruda, np.concatenate(piezas))
            ff("-i", str(cruda), "-af", f"atempo={TEMPO}", "-ar", str(SR), str(pieza))
            d = len(leer(pieza)) / SR
            filas.append((i, quien, t, t + d, d, texto, archivo, tramos, [t + c for c in cortes]))
            partes.append(leer(pieza))
            t += d
            if i < len(LINEAS):
                partes.append(np.zeros(int(SILENCIO * SR)))
                t += SILENCIO
        junta = tmp / "junta.wav"
        todo = np.concatenate(partes)
        # La grabación de Tin termina con la voz todavía sonando (-27 dB, sin cola; medido con revisar_voz.py el
        # 2026-11-23). Fundido de salida de 200 ms (eran 120; lo pidió el diseñador de sonido: se parece más a la caída
        # natural de «now») para que no acabe de golpe. No mueve ningún tiempo. Es edición, no regeneración.
        n = int(0.20 * SR)
        todo[-n:] = todo[-n:] * (np.cos(np.linspace(0, np.pi / 2, n)) ** 2).reshape((-1,) + todo.shape[1:])
        guardar(junta, todo)
        ff("-i", str(junta), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "44100", "-b:a", "192k",
           str(AUDIO / "dialogo_110.mp3"))
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json",
                        str(AUDIO / "dialogo_110.mp3")], capture_output=True, text=True, check=True)
    total = float(json.loads(r.stdout)["format"]["duration"])
    md = ["# Línea de tiempo de la voz (110 %)", "",
          "Diálogo `dialogo_110.mp3`, armado con `codigo/armar_dialogo.py` a partir de `voz_tan_zelda.wav` y",
          f"`voz_tin_kevin.wav` (una generación cada una). Duración del archivo: {total:.2f} s; la última línea termina en "
          f"{filas[-1][3]:.2f} s. En el video la voz empieza en el fotograma 0 (sin retraso): estos tiempos son los del video.",
          "",
          f"Cada línea al 110 % (`atempo={TEMPO}`, sin cambiar el tono), {SILENCIO:.2f} s entre líneas; las pausas internas",
          f"largas (tras «So,» y «Wow,», y las de Tin de más de 0,35 s) se acortaron a {PAUSA_INTERNA:.2f} s.",
          "",
          "**Cortes hechos por las pausas medidas (`silencedetect` a −35 dB), sin escuchar.** El texto de cada tramo es el",
          "probable por orden y duración: hay que comprobarlo al oído antes de publicar.", "",
          "| Línea | Quién | Empieza (s) | Termina (s) | Dura (s) | Texto | Segundo tramo empieza (s) | De dónde sale |",
          "|---|---|---|---|---|---|---|---|"]
    for i, quien, a, b, d, texto, archivo, tramos, cortes in filas:
        origen = "; ".join(f"{x:.2f} a {y:.2f} s («{tx}»)" for x, y, tx in tramos)
        md.append(f"| {i} | {quien} | {a:.2f} | {b:.2f} | {d:.2f} | {texto} | "
                  f"{(f'{cortes[0]:.2f}' if cortes else '—')} | `{archivo}`: {origen} |")
    md += ["", "## Dudas de los cortes (sin escucha)", ""]
    md += [f"- {a}" for a in avisos] or ["- El número de tramos medidos coincide con el esperado en las dos voces (Tan 5, Tin 9)."]
    md += ["- Línea 7 («Four thousand, / eight hundred eleven days.»): el tramo de 20,53 a 21,29 s se supone «Four thousand,» "
           "por su duración (0,76 s); no está confirmado al oído.",
           "- Línea 9: el archivo de Tin termina en 25,60 s sin silencio de cola medible; se toma hasta el final. Si la última "
           "sílaba («now») quedó cortada por el generador, solo se nota al oído.",
           "- Líneas 3, 4 y 5 conservan dentro una pausa corta (0,16 a 0,24 s en el original) que no se tocó.",
           "- «G T A» letra por letra y la pronunciación de las cifras no se pueden comprobar con medidas."]
    (AUDIO / "linea_de_tiempo_voz.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"dialogo_110.mp3: {total:.2f} s; la voz termina en {filas[-1][3]:.2f} s")
    for f in filas:
        print(f"  {f[0]} {f[1]} {f[2]:.2f}-{f[3]:.2f}", [round(c, 2) for c in f[8]])


if __name__ == "__main__":
    main()
