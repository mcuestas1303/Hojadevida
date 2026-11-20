#!/usr/bin/env python3
"""Postproduccion gratis con ffmpeg: todo lo que se edita no se paga en creditos.

Uso:
    postpro.py info        <video>
    postpro.py recortar    <entrada> <salida> [--desde S] [--hasta S]
    postpro.py vertical    <entrada> <salida> [--modo desenfoque|recorte] [--ancho 1080 --alto 1920]
    postpro.py velocidad   <entrada> <salida> --factor F [--suave]      (0.5 = camara lenta, 2 = doble)
    postpro.py fotograma   <entrada> <imagen.png> [--ultimo | --en S]   (keyframe para encadenar tomas)
    postpro.py color       <entrada> <salida> [--estilo calido|frio|noche|vivo|suave] [--lut archivo.cube]
    postpro.py subtitulos  <entrada> <subs.srt> <salida> [--tamano 64]
    postpro.py unir        <clip1> <clip2> ... -o <salida> [--transicion corte|fundido] [--dur 0.4]
                           [--ancho 1080 --alto 1920 --fps 30]
    postpro.py mezclar     <video> <salida> [--voz archivo] [--musica archivo] [--efectos archivo@seg ...]
                           [--musica-db -18] [--sin-original]
    postpro.py normalizar  <entrada> <salida> [--lufs -14]
    postpro.py zoom        <imagen> <salida> [--dur 4] [--hacia dentro|fuera] [--ancho 1080 --alto 1920]
"""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ESTILOS = {
    "calido": "colorbalance=rs=0.06:gs=0.01:bs=-0.06:rm=0.05:bm=-0.05,eq=saturation=1.08",
    "frio": "colorbalance=rs=-0.05:bs=0.07:rm=-0.04:bm=0.05,eq=saturation=0.92",
    "noche": "colorbalance=rs=-0.08:bs=0.12,eq=brightness=-0.06:contrast=1.08:saturation=0.8",
    "vivo": "eq=saturation=1.25:contrast=1.06",
    "suave": "eq=saturation=0.9:contrast=0.95:brightness=0.02",
}
CODEC_V = ["-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", "-movflags", "+faststart"]
CODEC_A = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000"]


def ffmpeg(args):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"ffmpeg fallo:\n{r.stderr.strip()}")


def sondear(ruta):
    r = subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(ruta)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"ffprobe no pudo leer {ruta}:\n{r.stderr.strip()}")
    return json.loads(r.stdout)


def duracion(ruta):
    return float(sondear(ruta)["format"].get("duration", 0))


def tiene_audio(ruta):
    return any(s["codec_type"] == "audio" for s in sondear(ruta)["streams"])


def lienzo(ancho, alto, fps=None):
    f = (f"scale={ancho}:{alto}:force_original_aspect_ratio=decrease,"
         f"pad={ancho}:{alto}:(ow-iw)/2:(oh-ih)/2,setsar=1")
    return f + (f",fps={fps}" if fps else "")


def cmd_info(a):
    d = sondear(a.video)
    v = next((s for s in d["streams"] if s["codec_type"] == "video"), None)
    au = next((s for s in d["streams"] if s["codec_type"] == "audio"), None)
    print(f"Archivo:   {a.video}")
    print(f"Duracion:  {float(d['format'].get('duration', 0)):.2f} s")
    if v:
        num, den = (v.get("avg_frame_rate") or "0/1").split("/")
        fps = float(num) / float(den) if float(den) else 0
        ancho, alto = v["width"], v["height"]
        print(f"Video:     {ancho}x{alto} · {fps:.2f} fps · {v['codec_name']} · aspecto {ancho / alto:.3f}"
              f" ({'vertical' if alto > ancho else 'horizontal' if ancho > alto else 'cuadrado'})")
    print(f"Audio:     {au['codec_name'] + ' · ' + au.get('sample_rate', '?') + ' Hz' if au else 'sin audio'}")


def cmd_recortar(a):
    args = []
    if a.desde:
        args += ["-ss", str(a.desde)]
    args += ["-i", a.entrada]
    if a.hasta:
        args += ["-t", str(a.hasta - (a.desde or 0))]
    ffmpeg([*args, *CODEC_V, *CODEC_A, a.salida])
    print(f"Recortado -> {a.salida}")


def cmd_vertical(a):
    w, h = a.ancho, a.alto
    if a.modo == "recorte":
        filtro = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1"
    else:
        filtro = (f"split[f][p];[f]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},gblur=sigma=40,"
                  f"eq=brightness=-0.08[fondo];[p]scale={w}:{h}:force_original_aspect_ratio=decrease[frente];"
                  f"[fondo][frente]overlay=(W-w)/2:(H-h)/2,setsar=1")
    ffmpeg(["-i", a.entrada, "-filter_complex", filtro, *CODEC_V, *CODEC_A, a.salida])
    print(f"{w}x{h} ({a.modo}) -> {a.salida}")


def atempo(factor):
    pasos, f = [], factor
    while f < 0.5:
        pasos.append("atempo=0.5")
        f /= 0.5
    while f > 2.0:
        pasos.append("atempo=2.0")
        f /= 2.0
    pasos.append(f"atempo={f:.4f}")
    return ",".join(pasos)


def cmd_velocidad(a):
    if a.factor <= 0:
        sys.exit("--factor tiene que ser mayor que 0")
    v = f"setpts=PTS/{a.factor}"
    if a.suave and a.factor < 1:
        v += ",minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1"
    args = ["-i", a.entrada, "-filter:v", v]
    args += ["-filter:a", atempo(a.factor), *CODEC_A] if tiene_audio(a.entrada) else ["-an"]
    ffmpeg([*args, *CODEC_V, a.salida])
    print(f"Velocidad x{a.factor} -> {a.salida}")


def cmd_fotograma(a):
    if a.ultimo:
        ffmpeg(["-sseof", "-0.1", "-i", a.entrada, "-update", "1", "-frames:v", "1", a.imagen])
    else:
        ffmpeg(["-ss", str(a.en or 0), "-i", a.entrada, "-frames:v", "1", a.imagen])
    print(f"Fotograma -> {a.imagen}")


def cmd_color(a):
    if a.lut:
        filtro = f"lut3d={a.lut}"
    else:
        filtro = ESTILOS[a.estilo]
    args = ["-i", a.entrada, "-vf", filtro, *CODEC_V]
    args += ["-c:a", "copy"] if tiene_audio(a.entrada) else []
    ffmpeg([*args, a.salida])
    print(f"Color ({a.lut or a.estilo}) -> {a.salida}")


def cmd_subtitulos(a):
    d = sondear(a.entrada)
    v = next(s for s in d["streams"] if s["codec_type"] == "video")
    vertical = v["height"] > v["width"]
    # Zona segura 9:16: el texto queda en el tercio central-bajo, lejos de los botones de la app.
    # libass escala los .srt a una altura virtual de 288: tamano y margen se pasan a esa escala.
    margen = round((0.28 if vertical else 0.08) * 288)
    tamano = max(8, round(a.tamano * 288 / v["height"]))
    estilo = (f"FontName=DejaVu Sans,Fontsize={tamano},"
              f"Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=3,Shadow=0,"
              f"Alignment=2,MarginV={margen},MarginL=40,MarginR=60")
    with tempfile.TemporaryDirectory() as tmp:
        srt = Path(tmp) / "subs.srt"
        shutil.copy(a.srt, srt)
        args = ["-i", a.entrada, "-vf", f"subtitles={srt}:force_style='{estilo}'", *CODEC_V]
        args += ["-c:a", "copy"] if tiene_audio(a.entrada) else []
        ffmpeg([*args, a.salida])
    print(f"Subtitulos -> {a.salida}")


def cmd_unir(a):
    clips = a.clips
    if len(clips) < 2:
        sys.exit("unir necesita al menos 2 clips")
    con_audio = all(tiene_audio(c) for c in clips)
    entradas = sum((["-i", c] for c in clips), [])
    norm = [f"[{i}:v]{lienzo(a.ancho, a.alto, a.fps)},format=yuv420p[v{i}]" for i in range(len(clips))]
    if con_audio:
        norm += [f"[{i}:a]aformat=sample_rates=48000:channel_layouts=stereo[a{i}]" for i in range(len(clips))]
    if a.transicion == "corte":
        pares = "".join(f"[v{i}]" + (f"[a{i}]" if con_audio else "") for i in range(len(clips)))
        grafo = norm + [f"{pares}concat=n={len(clips)}:v=1:a={1 if con_audio else 0}[v]" + ("[a]" if con_audio else "")]
    else:
        grafo, prev_v, prev_a, t = list(norm), "v0", "a0", 0.0
        for i in range(1, len(clips)):
            t += duracion(clips[i - 1]) - a.dur
            grafo.append(f"[{prev_v}][v{i}]xfade=transition=fade:duration={a.dur}:offset={t:.3f}[x{i}]")
            prev_v = f"x{i}"
            if con_audio:
                grafo.append(f"[{prev_a}][a{i}]acrossfade=d={a.dur}[y{i}]")
                prev_a = f"y{i}"
        grafo.append(f"[{prev_v}]null[v]")
        if con_audio:
            grafo.append(f"[{prev_a}]anull[a]")
    mapas = ["-map", "[v]"] + (["-map", "[a]", *CODEC_A] if con_audio else [])
    ffmpeg([*entradas, "-filter_complex", ";".join(grafo), *mapas, *CODEC_V, a.salida])
    print(f"{len(clips)} clips ({a.transicion}) -> {a.salida}" + ("" if con_audio else "  (sin audio)"))


def cmd_mezclar(a):
    entradas, capas, n = ["-i", a.video], [], 1
    original = tiene_audio(a.video) and not a.sin_original
    if original:
        capas.append(("original", "[0:a]volume=0dB"))
    voz = None
    if a.voz:
        entradas += ["-i", a.voz]
        voz = n
        n += 1
    musica = None
    if a.musica:
        entradas += ["-i", a.musica]
        musica = n
        n += 1
    efectos = []
    for e in a.efectos or []:
        ruta, _, seg = e.partition("@")
        entradas += ["-i", ruta]
        efectos.append((n, float(seg or 0)))
        n += 1
    if not (voz or musica or efectos or original):
        sys.exit("Nada que mezclar: pasa --voz, --musica o --efectos")
    grafo, etiquetas = [], []
    fmt = "aformat=sample_rates=48000:channel_layouts=stereo"
    if original:
        grafo.append(f"[0:a]{fmt}[orig]")
        etiquetas.append("[orig]")
    if voz is not None:
        grafo.append(f"[{voz}:a]{fmt},asplit=2[voz][vozsc]")
        etiquetas.append("[voz]")
    if musica is not None:
        grafo.append(f"[{musica}:a]{fmt},volume={a.musica_db}dB[mus0]")
        if voz is not None:
            # La musica se agacha sola cuando habla la voz.
            grafo.append("[mus0][vozsc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[mus]")
        else:
            grafo.append("[mus0]anull[mus]")
        etiquetas.append("[mus]")
    elif voz is not None:
        grafo.append("[vozsc]anullsink")
    for i, (idx, seg) in enumerate(efectos):
        ms = int(seg * 1000)
        grafo.append(f"[{idx}:a]{fmt},adelay={ms}|{ms}[sfx{i}]")
        etiquetas.append(f"[sfx{i}]")
    grafo.append(f"{''.join(etiquetas)}amix=inputs={len(etiquetas)}:duration=first:normalize=0,"
                 f"loudnorm=I=-14:TP=-1:LRA=11[a]" if original else
                 f"{''.join(etiquetas)}amix=inputs={len(etiquetas)}:duration=longest:normalize=0,"
                 f"loudnorm=I=-14:TP=-1:LRA=11[a]")
    ffmpeg([*entradas, "-filter_complex", ";".join(grafo), "-map", "0:v", "-map", "[a]",
            "-c:v", "copy", *CODEC_A, "-shortest", a.salida])
    print(f"Mezcla ({len(etiquetas)} capas, -14 LUFS) -> {a.salida}")


def cmd_normalizar(a):
    if not tiene_audio(a.entrada):
        sys.exit("El video no tiene audio.")
    ffmpeg(["-i", a.entrada, "-af", f"loudnorm=I={a.lufs}:TP=-1:LRA=11", "-c:v", "copy", *CODEC_A, a.salida])
    print(f"Audio a {a.lufs} LUFS -> {a.salida}")


def cmd_zoom(a):
    fps, cuadros = 30, int(a.dur * 30)
    z = (f"min(1+0.15*on/{cuadros},1.15)" if a.hacia == "dentro" else f"max(1.15-0.15*on/{cuadros},1)")
    filtro = (f"scale={a.ancho * 2}:{a.alto * 2}:force_original_aspect_ratio=increase,crop={a.ancho * 2}:{a.alto * 2},"
              f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={cuadros}:s={a.ancho}x{a.alto}:fps={fps}")
    ffmpeg(["-loop", "1", "-i", a.imagen, "-vf", filtro, "-t", str(a.dur), *CODEC_V, a.salida])
    print(f"Zoom {a.hacia} {a.dur}s -> {a.salida}")


def main():
    if shutil.which("ffmpeg") is None:
        sys.exit("Falta ffmpeg.")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="orden", required=True)

    s = sub.add_parser("info"); s.add_argument("video"); s.set_defaults(f=cmd_info)
    s = sub.add_parser("recortar"); s.add_argument("entrada"); s.add_argument("salida")
    s.add_argument("--desde", type=float); s.add_argument("--hasta", type=float); s.set_defaults(f=cmd_recortar)
    s = sub.add_parser("vertical"); s.add_argument("entrada"); s.add_argument("salida")
    s.add_argument("--modo", choices=["desenfoque", "recorte"], default="desenfoque")
    s.add_argument("--ancho", type=int, default=1080); s.add_argument("--alto", type=int, default=1920)
    s.set_defaults(f=cmd_vertical)
    s = sub.add_parser("velocidad"); s.add_argument("entrada"); s.add_argument("salida")
    s.add_argument("--factor", type=float, required=True); s.add_argument("--suave", action="store_true")
    s.set_defaults(f=cmd_velocidad)
    s = sub.add_parser("fotograma"); s.add_argument("entrada"); s.add_argument("imagen")
    g = s.add_mutually_exclusive_group(); g.add_argument("--ultimo", action="store_true")
    g.add_argument("--en", type=float); s.set_defaults(f=cmd_fotograma)
    s = sub.add_parser("color"); s.add_argument("entrada"); s.add_argument("salida")
    s.add_argument("--estilo", choices=sorted(ESTILOS), default="calido"); s.add_argument("--lut")
    s.set_defaults(f=cmd_color)
    s = sub.add_parser("subtitulos"); s.add_argument("entrada"); s.add_argument("srt"); s.add_argument("salida")
    s.add_argument("--tamano", type=int, default=64); s.set_defaults(f=cmd_subtitulos)
    s = sub.add_parser("unir"); s.add_argument("clips", nargs="+"); s.add_argument("-o", "--salida", required=True)
    s.add_argument("--transicion", choices=["corte", "fundido"], default="corte")
    s.add_argument("--dur", type=float, default=0.4)
    s.add_argument("--ancho", type=int, default=1080); s.add_argument("--alto", type=int, default=1920)
    s.add_argument("--fps", type=int, default=30); s.set_defaults(f=cmd_unir)
    s = sub.add_parser("mezclar"); s.add_argument("video"); s.add_argument("salida")
    s.add_argument("--voz"); s.add_argument("--musica"); s.add_argument("--efectos", nargs="*")
    s.add_argument("--musica-db", type=float, default=-18); s.add_argument("--sin-original", action="store_true")
    s.set_defaults(f=cmd_mezclar)
    s = sub.add_parser("normalizar"); s.add_argument("entrada"); s.add_argument("salida")
    s.add_argument("--lufs", type=float, default=-14); s.set_defaults(f=cmd_normalizar)
    s = sub.add_parser("zoom"); s.add_argument("imagen"); s.add_argument("salida")
    s.add_argument("--dur", type=float, default=4); s.add_argument("--hacia", choices=["dentro", "fuera"], default="dentro")
    s.add_argument("--ancho", type=int, default=1080); s.add_argument("--alto", type=int, default=1920)
    s.set_defaults(f=cmd_zoom)

    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
