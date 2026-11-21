#!/usr/bin/env python3
"""Arma 05_audio/dialogo_110_v2.mp3: el diálogo del short con las líneas 4, 5, 6 y 8 de Tin en pulgadas y pies
y el remate «For one side.» (cambio aprobado por el dueño el 2026-11-21, `video-studio/cambios/2026-11-21_tin_y_tan_remate_y_unidades.md`).

Mismo método que el v1 (canales/nostalgia-tin-y-tan/voces.md): cada voz normalizada a -14 LUFS, cada línea recortada
por sus pausas, acelerada un 10 % sin cambiar el tono (atempo=1.10) y separada de la siguiente por 0,23 s de silencio.
Escribe también 05_audio/linea_de_tiempo_voz_v2.md con los tiempos medidos. Gratis: solo ffmpeg.
"""
import json
import subprocess
import tempfile
from pathlib import Path

AUDIO = Path(__file__).resolve().parent.parent / "05_audio"
SILENCIO = 0.23
TEMPO = 1.10
MARGEN = 0.03

# (quién, texto, archivo, desde, hasta) — tiempos en el archivo original, antes de acelerar.
LINEAS = [
    ("Tan", "Remember rewinding a cassette with a pencil?", "voz_tan_zelda.wav", 0.43, 3.05),
    ("Tan", "So, how many turns does it really take?", "voz_tan_zelda.wav", 4.21, 7.35),
    ("Tin", "A C ninety tape plays forty-five minutes per side.", "voz_tin_kevin.wav", 0.23, 2.92),
    ("Tin", "At one and seven-eighths inches a second, that's about four hundred twenty feet of tape.",
     "voz_tin_kevin_v2_pulgadas.wav", 0.0, 4.41),
    ("Tin", "One pencil turn winds about four and a third inches.", "voz_tin_kevin_v2_pulgadas.wav", 4.78, 7.59),
    ("Tin", "Four hundred twenty feet, divided by four and a third inches...", "voz_tin_kevin_v2_pulgadas.wav",
     8.39, 11.49),
    ("Tan", "About eleven hundred seventy turns!", "voz_tan_zelda.wav", 8.46, 11.75),
    # En la toma nueva el modelo dejó 11,6 s de silencio puro (-90 dB) después de los puntos suspensivos: se salta.
    ("Tin", "At two turns a second, almost ten minutes. For one side.", "voz_tin_kevin_v2_pulgadas.wav", 23.09, 27.38),
]


def ff(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args], check=True)


def duracion(ruta):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(ruta)],
                       capture_output=True, text=True, check=True)
    return float(json.loads(r.stdout)["format"]["duration"])


def main():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        normal = {}
        for nombre in sorted({l[2] for l in LINEAS}):
            normal[nombre] = tmp / f"norm_{nombre}"
            ff("-i", str(AUDIO / nombre), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-ac", "1",
               str(normal[nombre]))
        partes, filas, t = [], [], 0.0
        silencio = tmp / "silencio.wav"
        ff("-f", "lavfi", "-i", f"anullsrc=r=48000:cl=mono", "-t", str(SILENCIO), str(silencio))
        for i, (quien, texto, archivo, desde, hasta) in enumerate(LINEAS, 1):
            pieza = tmp / f"linea_{i}.wav"
            ff("-ss", f"{max(0, desde - MARGEN):.3f}", "-to", f"{hasta + MARGEN:.3f}", "-i", str(normal[archivo]),
               "-af", f"atempo={TEMPO}", str(pieza))
            d = duracion(pieza)
            filas.append((i, quien, t, t + d, d, texto, archivo, desde, hasta))
            partes.append(pieza)
            t += d
            if i < len(LINEAS):
                partes.append(silencio)
                t += SILENCIO
        lista = tmp / "lista.txt"
        lista.write_text("".join(f"file '{p}'\n" for p in partes))
        ff("-f", "concat", "-safe", "0", "-i", str(lista), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
           "-ar", "44100", "-b:a", "192k", str(AUDIO / "dialogo_110_v2.mp3"))
    total = duracion(AUDIO / "dialogo_110_v2.mp3")
    md = ["# Línea de tiempo de la voz, v2 (110 %)", "",
          "Diálogo `dialogo_110_v2.mp3`, armado con `codigo/armar_dialogo_v2.py`. Cambian las líneas 4, 5, 6 y 8 (pulgadas y",
          "pies, remate «For one side.»); el resto sale de las mismas grabaciones que el v1. "
          f"Duración: {total:.1f} s. Los tiempos son dentro del diálogo; en el video se desplazan lo que dure el gancho.",
          "", "Cortes hechos por las pausas medidas, sin escuchar: comprobar al oído antes de publicar.", "",
          "| Línea | Quién | Empieza (s) | Termina (s) | Dura (s) | Texto | De dónde sale |",
          "|---|---|---|---|---|---|---|"]
    for i, quien, a, b, d, texto, archivo, desde, hasta in filas:
        md.append(f"| {i} | {quien} | {a:.2f} | {b:.2f} | {d:.2f} | {texto} | `{archivo}` de {desde:.2f} a {hasta:.2f} s |")
    (AUDIO / "linea_de_tiempo_voz_v2.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"dialogo_110_v2.mp3: {total:.2f} s")


if __name__ == "__main__":
    main()
