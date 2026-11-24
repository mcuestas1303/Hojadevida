#!/usr/bin/env python3
"""Arma 05_audio/dialogo_110.wav: el diálogo del short 3 de Tin & Tan («Jensen Huang Is Back as Nvidia CEO After 11 Days»).

Método del canal (canales/nostalgia-tin-y-tan/voces.md, el mismo de los shorts 1 y 2): cada voz normalizada a -14 LUFS,
cada línea recortada por sus pausas medidas, acelerada un 10 % sin cambiar el tono (atempo=1.10) y separada de la
siguiente por 0,23 s de silencio; las pausas internas largas se acortan (0,15 s; 0,25 s entre las dos frases de la
línea 11) y la de «Apple:» se deja en 0,45 s a propósito (silencio antes del número: prompt, sección 7). Cada tramo
lleva un fundido de 8 ms. La coletilla «That's all, folks.» de cada archivo se descarta.
Escribe 05_audio/dialogo_110.wav, 05_audio/linea_de_tiempo.json (lo leen render.py y audio.py) y
05_audio/linea_de_tiempo_voz.md. Gratis: solo ffmpeg y numpy. Las voces NO se regeneran.

Los tramos se midieron con `silencedetect=noise=-35dB:d=0.12` (2026-11-24) y su texto se comprobó con
`herramientas/revisar_voz.py --tramos --voz-sola` (07_revision/vuelta_01/voz_tan.md y voz_tin.md).
En el video la voz entra en el fotograma 14 (0,467 s): lo pide la firma del lápiz bumerán (FIRMA_LAPIZ_BUMERAN.md, §7).
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
FPS = 30
VOZ_ENTRA = 14 / FPS     # la voz de Tan entra en el fotograma 14 (firma del lápiz bumerán)
SILENCIO = 0.23          # entre líneas
PAUSA_INTERNA = 0.15     # pausa interna acortada (en el diálogo final, ya al 110 %)
TEMPO = 1.10
MARGEN = 0.03
FUNDIDO = 0.008
TAN, TIN = "voz_tan_zelda.wav", "voz_tin_kevin.wav"

# (quién, texto exacto del guion, archivo, tramos [(desde, hasta, texto oído en el tramo, pausa antes en s o None)])
# Tiempos del archivo original. Dos tramos en una línea = pausa interna que se fija al valor dado (en el diálogo final).
LINEAS = [
    ("Tan", "Was Jensen Huang's comeback in eleven days fast?", TAN,
     [(0.467, 3.676, "Was Jensen Huang's comeback in eleven days fast?", None)]),
    ("Tin", "He resigned from Nvidia on November twelfth after a scandal.", TIN,
     [(0.265, 1.472, "He resigned from Nvidia", None), (1.977, 3.696, "on November twelfth after a scandal.", PAUSA_INTERNA)]),
    ("Tin", "On the seventeenth the board said it would not bring him back.", TIN,
     [(4.069, 6.545, "On the seventeenth the board said it would not bring him back.", None)]),
    ("Tin", "Six days later it reinstated him as C E O.", TIN,
     [(6.864, 9.448, "Six days later it reinstated him as C E O.", None)]),
    ("Tin", "Before that: more than thirty-three years in charge.", TIN,
     [(9.735, 12.139, "Before that: more than thirty-three years in charge.", None)]),
    ("Tan", "Fast compared to who?", TAN, [(4.764, 6.518, "Fast compared to who?", None)]),
    ("Tin", "Sam Altman at OpenAI: five days.", TIN,
     [(12.524, 14.133, "Sam Altman at OpenAI:", None), (14.355, 15.112, "five days.", 0.20)]),
    ("Tin", "Steve Jobs at Apple: four thousand, three hundred eighty-two days.", TIN,
     [(15.644, 16.919, "Steve Jobs at Apple:", None),
      (17.061, 19.069, "four thousand, three hundred eighty-two days.", 0.45)]),
    ("Tan", "That is twelve years?", TAN, [(7.756, 8.370, "That is", None), (9.041, 10.146, "twelve years?", PAUSA_INTERNA)]),
    ("Tin", "Faster than Jobs. Slower than Altman.", TIN,
     [(19.426, 20.474, "Faster than Jobs.", None), (20.727, 21.609, "Slower than Altman.", 0.20)]),
    ("Tan", "Who else came back? Subscribe for the next count.", TAN,
     [(11.048, 12.205, "Who else came back?", None), (13.063, 14.960, "Subscribe for the next count.", 0.25)]),
]
# El último tramo de Tin («Slower than Altman.») va pegado a la coletilla: entre «Altman» y «That's all» solo hay
# 0,15 s (21,609 a 21,758). Se corta ahí con margen de 0,03 s y un fundido de salida de 60 ms.
FUNDIDO_FINAL = {9: 0.06, 10: 0.10}        # índice de línea (desde 0) -> fundido de salida más largo del último tramo


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


def trozo(x, desde, hasta, fundido_fin=FUNDIDO):
    a, b = int(max(0, desde - MARGEN) * SR), min(len(x), int((hasta + MARGEN) * SR))
    y = x[a:b].copy()
    n = int(FUNDIDO * SR)
    y[:n] *= np.linspace(0, 1, n)
    n = int(fundido_fin * SR)
    y[-n:] *= np.linspace(1, 0, n)
    return y


def main():
    for nombre in (TAN, TIN):
        if not (AUDIO / nombre).exists():
            raise SystemExit(f"Falta {AUDIO / nombre}: la voz la deja el dueño (una generación por personaje).")
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        normal = {}
        for nombre in (TAN, TIN):
            ruta = tmp / f"norm_{nombre}"
            ff("-i", str(AUDIO / nombre), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", str(SR), "-ac", "1", str(ruta))
            normal[nombre] = leer(ruta)
        partes, filas, t = [], [], 0.0
        for i, (quien, texto, archivo, tramos) in enumerate(LINEAS):
            x = normal[archivo]
            piezas, cortes = [], []
            for j, (desde, hasta, _, pausa) in enumerate(tramos):
                if j:
                    # la pausa interna se mide en el diálogo final: aquí va 1,10 veces más larga, menos los márgenes
                    piezas.append(np.zeros(int(max(0.0, pausa * TEMPO - 2 * MARGEN) * SR)))
                    cortes.append((sum(len(p) for p in piezas) + MARGEN * SR) / SR / TEMPO)   # inicio del tramo (110 %)
                ultimo = j == len(tramos) - 1
                piezas.append(trozo(x, desde, hasta, FUNDIDO_FINAL.get(i, FUNDIDO) if ultimo else FUNDIDO))
            cruda, pieza = tmp / f"cruda_{i}.wav", tmp / f"linea_{i}.wav"
            guardar(cruda, np.concatenate(piezas))
            ff("-i", str(cruda), "-af", f"atempo={TEMPO}", "-ar", str(SR), str(pieza))
            y = leer(pieza)
            d = len(y) / SR
            filas.append({"linea": i + 1, "quien": quien, "texto": texto, "archivo": archivo,
                          "empieza": round(VOZ_ENTRA + t, 3), "termina": round(VOZ_ENTRA + t + d, 3), "dura": round(d, 3),
                          "tramos": [round(VOZ_ENTRA + t, 3)] + [round(VOZ_ENTRA + t + c, 3) for c in cortes],
                          "origen": [(a, b, tx) for a, b, tx, _ in tramos]})
            partes.append(y)
            t += d
            if i < len(LINEAS) - 1:
                partes.append(np.zeros(int(SILENCIO * SR)))
                t += SILENCIO
        junta = tmp / "junta.wav"
        guardar(junta, np.concatenate(partes))
        ff("-i", str(junta), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", str(SR), "-ac", "1",
           str(AUDIO / "dialogo_110.wav"))
    total = len(leer(AUDIO / "dialogo_110.wav")) / SR
    datos = {"voz_entra": round(VOZ_ENTRA, 4), "fps": FPS, "tempo": TEMPO, "silencio_entre_lineas": SILENCIO,
             "duracion_dialogo": round(total, 3), "lineas": filas}
    (AUDIO / "linea_de_tiempo.json").write_text(json.dumps(datos, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    md = ["# Línea de tiempo de la voz (110 %)", "",
          "Diálogo `dialogo_110.wav`, armado con `codigo/armar_dialogo.py` a partir de `voz_tan_zelda.wav` y",
          f"`voz_tin_kevin.wav` (una generación cada una; no se regeneran). Duración del diálogo: {total:.2f} s.",
          f"**En el video la voz entra en el fotograma 14 ({VOZ_ENTRA:.3f} s)**, como pide la firma del lápiz bumerán",
          "(`canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`, sección 7): los tiempos de la tabla son los del video.",
          "",
          f"Cada línea al 110 % (`atempo={TEMPO}`, sin cambiar el tono), {SILENCIO:.2f} s entre líneas. Pausas internas",
          f"fijadas en edición: {PAUSA_INTERNA:.2f} s (líneas 2 y 9), 0,20 s (líneas 7 y 10), 0,25 s (línea 11, entre la",
          "pregunta y la invitación) y **0,45 s tras «Apple:»** (línea 8; en el original eran 0,14 s: se alargó con silencio",
          "para el silencio antes del número). La coletilla «That's all, folks.» de los dos archivos no se usa.",
          "",
          "Cortes hechos por las pausas medidas (`silencedetect` a −35 dB) y comprobados con `revisar_voz.py --tramos`",
          "(Whisper small.en): el texto de cada tramo es el reconocido. **Ninguna persona ha escuchado el audio.**", "",
          "| Línea | Quién | Empieza (s) | Termina (s) | Dura (s) | Texto | Segundo tramo empieza (s) | De dónde sale |",
          "|---|---|---|---|---|---|---|---|"]
    for f in filas:
        origen = "; ".join(f"{a:.2f} a {b:.2f} s («{tx}»)" for a, b, tx in f["origen"])
        seg = f"{f['tramos'][1]:.2f}" if len(f["tramos"]) > 1 else "—"
        md.append(f"| {f['linea']} | {f['quien']} | {f['empieza']:.2f} | {f['termina']:.2f} | {f['dura']:.2f} | {f['texto']} | "
                  f"{seg} | `{f['archivo']}`: {origen} |")
    md += ["", "## Dudas de los cortes", "",
           "- Línea 10: «Slower than Altman.» está pegada a la coletilla en el archivo de Tin (0,15 s entre «Altman» y",
           "  «That's all»). Se cortó en 21,61 s (+0,03 s de margen) con un fundido de salida de 60 ms. Con `revisar_voz.py`",
           "  se oye «Altman» entero y nada de la coletilla; la cola de la «n» solo la puede juzgar una persona.",
           "- El archivo de Tan termina con la coletilla cortada por el generador («folks» con la voz aún sonando): no",
           "  afecta, la coletilla no se usa. «Subscribe for the next count.» tiene 0,82 s de silencio detrás; se tomó",
           "  0,12 s más allá del umbral de −35 dB (hasta 14,96 s) con fundido de 100 ms para no cortar la cola de «count».",
           "- Líneas 5 y 6 conservan dentro una pausa corta del original (0,13 s tras «Before that:» y 0,22 s en «Fast",
           "  compared / to who?») que no se tocó.",
           "- La pronunciación de «Nvidia», «Huang», «OpenAI» y «C E O» no se puede juzgar con medidas: el reconocedor las",
           "  transcribe bien («Nvidia», «Huang's», «OpenAI», «CEO»), y eso solo dice que se entienden."]
    (AUDIO / "linea_de_tiempo_voz.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"dialogo_110.wav: {total:.2f} s; en el video la voz va de {filas[0]['empieza']:.2f} a {filas[-1]['termina']:.2f} s")
    for f in filas:
        print(f"  {f['linea']:2d} {f['quien']} {f['empieza']:.2f}-{f['termina']:.2f}", f["tramos"][1:])


if __name__ == "__main__":
    main()
