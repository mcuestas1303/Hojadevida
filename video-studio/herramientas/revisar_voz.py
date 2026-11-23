#!/usr/bin/env python3
"""Control de voz del estudio: transcribe un audio y lo compara con el guion, palabra por palabra.

Regla del dueño (2026-11-23): «busca [herramientas] para que puedas auditar el tema de voz y audio». Claude no oye;
esto es su oído. Usa Whisper (modelo small.en) con sherpa-onnx, sin conexión y sin costo.

Instalación (una vez por contenedor): bash video-studio/herramientas/instalar_oido.sh

Uso:
  python3 video-studio/herramientas/revisar_voz.py <audio o video> --guion "texto esperado" [--guion-archivo f.txt]
      [--tramos] [--voz-sola]  [--salida informe.md]

Sin --guion solo transcribe. Con --tramos transcribe además cada tramo entre silencios (≥ 0,25 s a −35 dB), con
sus tiempos: sirve para ver qué palabra cae en qué segundo y si el final quedó cortado.
Compara sin mayúsculas ni puntuación y con los números escritos igual («4,811» = «four thousand eight hundred
eleven»). Sale con código 1 si falta, sobra o cambia alguna palabra.

Límites, para no engañarse: reconoce palabras, no juzga naturalidad, acento ni si la música tapa la voz; un modelo
de reconocimiento puede «arreglar» una palabra mal dicha. Lo que marque como distinto se revisa; lo que dé por bueno
sigue necesitando una escucha humana antes de publicar.
"""
import argparse
import difflib
import re
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import numpy as np

MODELO = Path(__file__).resolve().parent / "modelos_voz" / "sherpa-onnx-whisper-small.en"
UNIDADES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen " \
           "seventeen eighteen nineteen".split()
DECENAS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
ORDINALES = {"first": "one", "second": "two", "third": "three", "fifth": "five", "eighth": "eight", "ninth": "nine",
             "twelfth": "twelve"}


def en_palabras(n):
    if n < 20:
        return UNIDADES[n]
    if n < 100:
        return DECENAS[n // 10] + ("" if n % 10 == 0 else " " + UNIDADES[n % 10])
    if n < 1000:
        return UNIDADES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + en_palabras(n % 100))
    return en_palabras(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + en_palabras(n % 1000))


def normalizar(texto):
    t = texto.lower().replace("-", " ")
    t = re.sub(r"(\d),(\d{3})", r"\1\2", t)

    def anio(m):                                   # 2013 → twenty thirteen (como se dice un año)
        n = int(m.group(0))
        if 1100 <= n <= 2099 and n % 100 and not 2000 <= n <= 2009:
            return en_palabras(n // 100) + " " + en_palabras(n % 100)
        return en_palabras(n)

    t = re.sub(r"\b(\d+)(st|nd|rd|th)\b", lambda m: en_palabras(int(m.group(1))) + "th", t)
    t = re.sub(r"\b\d{4}\b", anio, t)
    t = re.sub(r"\b\d+\b", lambda m: en_palabras(int(m.group(0))), t)
    t = re.sub(r"[^a-z' ]+", " ", t)
    palabras = []
    for w in t.split():
        w = ORDINALES.get(w, w)
        w = re.sub(r"(ie)?th$", lambda m: "y" if m.group(1) else "", w) if re.fullmatch(
            r"(four|six|seven|ten|eleven|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|"
            r"twentie|thirtie|fortie|fiftie|sixtie|seventie|eightie|ninetie)th", w) else w
        palabras.append(w)
    t = " ".join(palabras)
    t = re.sub(r"\bthree sixty five\b", "three hundred sixty five", t)     # «three sixty-five» = 365
    t = re.sub(r"\bhundred and\b", "hundred", t)
    t = re.sub(r"\bg t a\b", "gta", t)
    t = re.sub(r"\bx\b", "times", t)                                    # el reconocedor escribe «13 years x 365»
    return t.split()


def a_wav(origen, destino):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(origen), "-vn", "-ac", "1", "-ar", "16000",
                    "-c:a", "pcm_s16le", str(destino)], check=True)


def leer(wav):
    with wave.open(str(wav)) as f:
        datos = np.frombuffer(f.readframes(f.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
        return datos, f.getframerate()


def reconocedor():
    try:
        import sherpa_onnx
    except ImportError:
        sys.exit("Falta el oído: bash video-studio/herramientas/instalar_oido.sh")
    if not MODELO.exists():
        sys.exit("Falta el modelo de voz: bash video-studio/herramientas/instalar_oido.sh")
    return sherpa_onnx.OfflineRecognizer.from_whisper(
        encoder=str(MODELO / "small.en-encoder.int8.onnx"), decoder=str(MODELO / "small.en-decoder.int8.onnx"),
        tokens=str(MODELO / "small.en-tokens.txt"), num_threads=4, language="en", task="transcribe")


def transcribir(rec, datos, sr):
    relleno = np.zeros(int(0.4 * sr), dtype=np.float32)
    s = rec.create_stream()
    s.accept_waveform(sr, np.concatenate([relleno, datos, relleno]))
    rec.decode_stream(s)
    return s.result.text.strip()


def tramos(datos, sr, umbral_db=-35.0, pausa=0.25):
    ventana = int(0.02 * sr)
    n = len(datos) // ventana
    rms = np.sqrt(np.mean(datos[:n * ventana].reshape(n, ventana) ** 2, axis=1) + 1e-12)
    voz = 20 * np.log10(rms) > umbral_db
    out, ini, silencio = [], None, 0
    for i, v in enumerate(voz):
        if v:
            if ini is None:
                ini = i
            silencio = 0
        elif ini is not None:
            silencio += 1
            if silencio * 0.02 >= pausa:
                out.append((ini * 0.02, (i - silencio + 1) * 0.02))
                ini, silencio = None, 0
    if ini is not None:
        out.append((ini * 0.02, n * 0.02))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("audio")
    ap.add_argument("--guion")
    ap.add_argument("--guion-archivo")
    ap.add_argument("--tramos", action="store_true")
    ap.add_argument("--voz-sola", action="store_true",
                    help="el archivo es solo voz (sin música ni efectos): avisa si termina con la voz sonando")
    ap.add_argument("--salida")
    a = ap.parse_args()
    guion = a.guion or (Path(a.guion_archivo).read_text(encoding="utf8") if a.guion_archivo else None)

    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "a.wav"
        a_wav(a.audio, wav)
        datos, sr = leer(wav)
    rec = reconocedor()
    dur = len(datos) / sr
    L = [f"# Control de voz · {Path(a.audio).name}", "", f"Duración: {dur:.2f} s. Reconocedor: Whisper small.en "
         "(sherpa-onnx), sin conexión.", ""]

    # El reconocedor se queda corto con pasadas largas (comprobado: deja de escribir a mitad de 9 s con pausas).
    # Se transcribe por bloques de unos 6 s, cortados en el punto más silencioso cercano (sirve también con música).
    ts = tramos(datos, sr)
    paso = int(0.02 * sr)
    energia = np.array([np.mean(datos[i:i + paso * 10] ** 2) for i in range(0, max(1, len(datos) - paso * 10), paso)])
    bloques, ini = [], 0.0
    while dur - ini > 8.0:
        i0, i1 = int((ini + 4.5) / 0.02), int((ini + 7.5) / 0.02)
        corte = (i0 + int(np.argmin(energia[i0:i1])) + 5) * 0.02
        bloques.append((ini, corte))
        ini = corte
    bloques.append((ini, dur))
    oido = " ".join(transcribir(rec, datos[int(b0 * sr):int(b1 * sr)], sr) for b0, b1 in bloques).strip()
    L += ["## Lo que se oye", "", f"> {oido}", ""]

    estado = 0
    if guion:
        g, o = normalizar(guion), normalizar(oido)
        dif = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, g, o).get_opcodes():
            if op == "replace":
                dif.append(f"- CAMBIA: guion «{' '.join(g[i1:i2])}» → se oye «{' '.join(o[j1:j2])}»")
            elif op == "delete":
                dif.append(f"- FALTA: «{' '.join(g[i1:i2])}»")
            elif op == "insert":
                dif.append(f"- SOBRA: «{' '.join(o[j1:j2])}»")
        L += ["## Contra el guion", "", f"> {guion.strip()}", ""]
        if dif:
            estado = 1
            L += [f"**NO COINCIDE: {len(dif)} diferencia(s)** ({len(g)} palabras en el guion, {len(o)} oídas)", ""] + dif
        else:
            L += [f"**COINCIDE: {len(g)} palabras, 0 diferencias.**"]
        L.append("")

    if a.tramos:
        L += ["## Tramos entre silencios", "", "| De (s) | A (s) | Dura | Se oye |", "|---|---|---|---|"]
        for t0, t1 in ts:
            txt = transcribir(rec, datos[int(max(0, t0 - 0.05) * sr):int(min(dur, t1 + 0.05) * sr)], sr)
            L.append(f"| {t0:.2f} | {t1:.2f} | {t1 - t0:.2f} | {txt} |")
        cola = dur - ts[-1][1] if ts else dur
        nivel_final = 20 * np.log10(np.sqrt(np.mean(datos[-int(0.05 * sr):] ** 2)) + 1e-9)
        L += ["", f"Silencio al final: {cola:.2f} s. Nivel de los últimos 50 ms: {nivel_final:.0f} dB"
              + (" — **el audio termina con voz sonando: posible final cortado**" if a.voz_sola and nivel_final > -40
                 else "") + ".", ""]
        if not a.voz_sola and nivel_final > -40:
            # En una mezcla ese nivel puede ser la música o un efecto, no la voz: el aviso solo vale sobre la voz sola.
            L += ["(El audio no termina en silencio. Si este archivo es solo voz, repite con `--voz-sola` para saber si "
                  "el final está cortado; en una mezcla con música o efectos no se puede saber desde aquí.)", ""]

    L += ["Límite: esto reconoce palabras; no juzga naturalidad, acento ni mezcla. Falta la escucha de una persona "
          "antes de publicar.", ""]
    texto = "\n".join(L)
    if a.salida:
        Path(a.salida).write_text(texto, encoding="utf8")
    print(texto)
    sys.exit(estado)


if __name__ == "__main__":
    main()
