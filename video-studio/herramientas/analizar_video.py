#!/usr/bin/env python3
"""Desarma un video de referencia en piezas que un agente puede "ver":
metadatos, cortes de escena, fotogramas, hojas de contacto y audio.

Uso:
    python3 analizar_video.py <video> <carpeta_salida> [--cada SEG] [--umbral 0.30]

Solo necesita ffmpeg/ffprobe. No gasta creditos de ningun generador.
"""
import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from pathlib import Path

COLS, FILAS = 5, 4  # fotogramas por hoja de contacto


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def metadatos(video):
    r = run(["ffprobe", "-v", "error", "-print_format", "json",
             "-show_format", "-show_streams", str(video)])
    if r.returncode != 0:
        sys.exit(f"ffprobe no pudo leer {video}:\n{r.stderr}")
    data = json.loads(r.stdout)
    v = next((s for s in data["streams"] if s["codec_type"] == "video"), None)
    if v is None:
        sys.exit("El archivo no tiene pista de video.")
    a = next((s for s in data["streams"] if s["codec_type"] == "audio"), None)
    num, den = (int(x) for x in v["r_frame_rate"].split("/"))
    ancho, alto = v["width"], v["height"]
    g = math.gcd(ancho, alto)
    return {
        "archivo": Path(video).name,
        "duracion_s": round(float(data["format"]["duration"]), 2),
        "ancho": ancho,
        "alto": alto,
        "aspecto": f"{ancho // g}:{alto // g}",
        "orientacion": "vertical" if alto > ancho else "horizontal" if ancho > alto else "cuadrado",
        "fps": round(num / den, 2) if den else None,
        "codec_video": v["codec_name"],
        "tiene_audio": a is not None,
        "codec_audio": a["codec_name"] if a else None,
    }


def cortes(video, umbral):
    """Tiempos (s) donde cambia la escena."""
    r = run(["ffmpeg", "-hide_banner", "-i", str(video), "-an",
             "-vf", f"select='gt(scene,{umbral})',showinfo", "-f", "null", "-"])
    return [round(float(t), 2) for t in re.findall(r"pts_time:([0-9.]+)", r.stderr)]


def silencios(video):
    r = run(["ffmpeg", "-hide_banner", "-i", str(video), "-vn",
             "-af", "silencedetect=noise=-35dB:d=0.4", "-f", "null", "-"])
    ini = re.findall(r"silence_start: ([0-9.]+)", r.stderr)
    fin = re.findall(r"silence_end: ([0-9.]+)", r.stderr)
    return [{"inicio": round(float(i), 2), "fin": round(float(f), 2)} for i, f in zip(ini, fin)]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video")
    p.add_argument("salida")
    p.add_argument("--cada", type=float, default=None,
                   help="segundos entre fotogramas (por defecto: se ajusta a ~40 fotogramas)")
    p.add_argument("--umbral", type=float, default=0.30,
                   help="sensibilidad de deteccion de cortes, 0-1 (menor = mas cortes)")
    args = p.parse_args()

    video, out = Path(args.video), Path(args.salida)
    if not video.is_file():
        sys.exit(f"No existe el video: {video}")
    frames = out / "frames"
    if frames.exists():
        shutil.rmtree(frames)
    frames.mkdir(parents=True)
    for viejo in out.glob("hoja_*.jpg"):
        viejo.unlink()

    meta = metadatos(video)
    dur = meta["duracion_s"]
    cada = args.cada or max(0.5, round(dur / 40, 2))

    # Fotogramas a intervalo fijo (ancho 480: suficiente para ver, barato de leer)
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(video),
         "-vf", f"fps=1/{cada},scale=480:-2", "-q:v", "4", str(frames / "f_%04d.jpg")])
    lista = sorted(frames.glob("f_*.jpg"))
    indice = []
    for i, f in enumerate(lista):
        t = round(i * cada + cada / 2, 2)  # el filtro fps toma el centro del intervalo
        nuevo = frames / f"t_{t:07.2f}s.jpg"
        f.rename(nuevo)
        indice.append({"t": t, "archivo": f"frames/{nuevo.name}"})

    # Hojas de contacto: un vistazo barato a todo el video
    por_hoja = COLS * FILAS
    hojas = []
    for n in range(math.ceil(len(indice) / por_hoja)):
        hoja = out / f"hoja_{n + 1:02d}.jpg"
        desde = n * por_hoja
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(video),
             "-vf", (f"fps=1/{cada},select='gte(n,{desde})',scale=320:-2,"
                     f"tile={COLS}x{FILAS}:padding=6:margin=6:color=white"),
             "-frames:v", "1", "-q:v", "4", str(hoja)])
        if hoja.exists():
            hojas.append({"archivo": hoja.name,
                          "desde_s": indice[desde]["t"],
                          "hasta_s": indice[min(desde + por_hoja, len(indice)) - 1]["t"],
                          "orden": f"izquierda a derecha, arriba a abajo, un cuadro cada {cada}s"})

    # Un fotograma nitido justo despues de cada corte
    lista_cortes = cortes(video, args.umbral)
    dir_cortes = out / "cortes"
    if dir_cortes.exists():
        shutil.rmtree(dir_cortes)
    dir_cortes.mkdir()
    tomas, limites = [], [0.0] + lista_cortes + [dur]
    for i in range(len(limites) - 1):
        ini, fin = limites[i], limites[i + 1]
        if fin - ini < 0.05:
            continue
        img = dir_cortes / f"toma_{len(tomas) + 1:02d}_{ini:07.2f}s.jpg"
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", str(min(ini + 0.15, max(fin - 0.05, 0))),
             "-i", str(video), "-frames:v", "1", "-vf", "scale=640:-2", "-q:v", "3", str(img)])
        tomas.append({"toma": len(tomas) + 1, "inicio_s": ini, "fin_s": round(fin, 2),
                      "duracion_s": round(fin - ini, 2),
                      "fotograma": f"cortes/{img.name}" if img.exists() else None})

    audio = None
    if meta["tiene_audio"]:
        wav = out / "audio.wav"
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(video),
             "-vn", "-ac", "1", "-ar", "16000", str(wav)])
        audio = {"archivo": wav.name, "silencios": silencios(video),
                 "transcripcion": None}
        if shutil.which("whisper"):
            run(["whisper", str(wav), "--output_dir", str(out), "--output_format", "txt"])
            txt = out / "audio.txt"
            if txt.exists():
                audio["transcripcion"] = txt.name

    resumen = {
        "video": meta,
        "ritmo": {
            "numero_de_tomas": len(tomas),
            "duracion_media_toma_s": round(dur / max(len(tomas), 1), 2),
        },
        "tomas": tomas,
        "fotogramas_cada_s": cada,
        "fotogramas": indice,
        "hojas_de_contacto": hojas,
        "audio": audio,
    }
    (out / "analisis.json").write_text(json.dumps(resumen, indent=2, ensure_ascii=False) + "\n")

    print(f"{meta['archivo']}: {dur}s, {meta['ancho']}x{meta['alto']} ({meta['aspecto']}, "
          f"{meta['orientacion']}), {meta['fps']} fps, audio: {'si' if meta['tiene_audio'] else 'no'}")
    print(f"{len(tomas)} tomas detectadas, {len(indice)} fotogramas, {len(hojas)} hoja(s) de contacto")
    print(f"Empieza por: {out / 'hoja_01.jpg'}  y  {out / 'analisis.json'}")


if __name__ == "__main__":
    main()
