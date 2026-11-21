#!/usr/bin/env python3
"""Revisa una carpeta de entrega para el publicador de YouTube antes de subirla a Drive.

Uso:
    entrega.py <carpeta>                 # revisa ficha.json y archivos
    entrega.py --plantilla <carpeta>     # crea la carpeta con una ficha.json para llenar

Controles (los mismos que aplica el publicador, más la miniatura): campos obligatorios, título de 100 caracteres o
menos y sin < ni >, descripción de 5.000 bytes o menos, etiquetas de 500 caracteres o menos en total, canal e idioma
válidos, objetivos medibles con plazo, archivos presentes, miniatura menor de 2 MB de 1280x720 (horizontal) o
1080x1920 (Short, regla 29), y el control de texto de revisar_texto.py.
Protocolo completo: video-studio/ENTREGA_YOUTUBE.md. No sube nada.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

CAMPOS = ["codigo", "canal", "titulo", "descripcion", "etiquetas", "idioma", "categoria_id",
          "contenido_sintetico_realista", "para_ninos", "objetivos", "archivos", "notas"]

PLANTILLA = {
    "codigo": "",
    "canal": "en",
    "titulo": "",
    "descripcion": "",
    "etiquetas": [],
    "idioma": "en",
    "categoria_id": "22",
    "contenido_sintetico_realista": None,
    "para_ninos": None,
    "objetivos": [{"metrica": "vistas", "meta": 0, "plazo_dias": 28}],
    "fecha_sugerida": "",
    "archivos": {"video": "video.mp4", "miniatura": "miniatura.png", "subtitulos": "subtitulos.srt"},
    "color": {"neutros": [], "acento": "", "por_que": "", "objetivo": "", "medido": ""},
    "notas": "",
}


def medida_video(ruta):
    """(ancho, alto) del video con ffprobe, o None si no se puede medir."""
    import subprocess
    if not ruta.is_file():
        return None
    try:
        r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                            "stream=width,height", "-of", "csv=p=0:s=x", str(ruta)],
                           capture_output=True, text=True, timeout=30)
        w, h = r.stdout.strip().split("x")[:2]
        return int(w), int(h)
    except (OSError, ValueError, subprocess.SubprocessError):
        return None


def revisar(carpeta):
    errores, avisos = [], []
    ficha_ruta = carpeta / "ficha.json"
    if not ficha_ruta.is_file():
        return [f"falta {ficha_ruta}"], avisos
    try:
        f = json.loads(ficha_ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"ficha.json no es JSON válido: {e}"], avisos

    for c in CAMPOS:
        if c not in f or f[c] in ("", None, [], {}):
            errores.append(f"falta el campo «{c}» (o está vacío)")

    if f.get("codigo") and carpeta.name != f["codigo"]:
        avisos.append(f"la carpeta se llama «{carpeta.name}» y el código es «{f['codigo']}»: deben coincidir")
    t = f.get("titulo") or ""
    if len(t) > 100:
        errores.append(f"el título tiene {len(t)} caracteres (máximo 100)")
    d = f.get("descripcion") or ""
    if len(d.encode("utf-8")) > 5000:
        errores.append(f"la descripción tiene {len(d.encode('utf-8'))} bytes (máximo 5.000)")
    for campo, texto in (("titulo", t), ("descripcion", d)):
        if re.search(r"[<>]", texto):
            errores.append(f"«{campo}» tiene los signos < o >")
    etiquetas = f.get("etiquetas") or []
    if not isinstance(etiquetas, list):
        errores.append("«etiquetas» tiene que ser una lista")
    elif sum(len(e) for e in etiquetas) > 500:
        errores.append(f"las etiquetas suman {sum(len(e) for e in etiquetas)} caracteres (máximo 500)")
    for campo in ("canal", "idioma"):
        if f.get(campo) not in ("en", "es"):
            errores.append(f"«{campo}» tiene que ser \"en\" o \"es\"")
    for campo in ("contenido_sintetico_realista", "para_ninos"):
        if not isinstance(f.get(campo), bool):
            errores.append(f"«{campo}» tiene que ser true o false (lo decide una persona)")
    for i, o in enumerate(f.get("objetivos") or []):
        if not (isinstance(o, dict) and o.get("metrica") and isinstance(o.get("meta"), (int, float))
                and o.get("meta") > 0 and isinstance(o.get("plazo_dias"), int) and o["plazo_dias"] > 0):
            errores.append(f"el objetivo {i + 1} no es medible con plazo (metrica, meta > 0, plazo_dias > 0)")
    if f.get("fecha_sugerida"):
        try:
            fecha = datetime.fromisoformat(f["fecha_sugerida"])
            if fecha.tzinfo is None:
                errores.append("«fecha_sugerida» no tiene zona horaria (p. ej. -06:00)")
        except ValueError:
            errores.append("«fecha_sugerida» no está en formato ISO")

    archivos = f.get("archivos") or {}
    for clave in ("video", "miniatura"):
        if not archivos.get(clave):
            errores.append(f"«archivos» no dice cuál es el {clave}")
        elif not (carpeta / archivos[clave]).is_file():
            errores.append(f"falta el archivo {archivos[clave]}")
    sub = archivos.get("subtitulos")
    if sub and not (carpeta / sub).is_file():
        avisos.append(f"«archivos» nombra {sub} pero no está (los subtítulos son opcionales: quita la línea o agrega el archivo)")
    mini = carpeta / archivos.get("miniatura", "")
    if archivos.get("miniatura") and mini.is_file():
        if mini.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            errores.append("la miniatura tiene que ser PNG o JPG")
        if mini.stat().st_size >= 2 * 1024 * 1024:
            errores.append(f"la miniatura pesa {mini.stat().st_size / 1048576:.1f} MB (menos de 2 MB)")
        # Short (video vertical) → miniatura vertical 1080x1920 (regla 29, 2026-11-21); horizontal → 1280x720
        short = medida_video(carpeta / archivos.get("video", "")) or None
        short = (short[1] > short[0]) if short else "-S-" in str(f.get("codigo", ""))
        esperada = (1080, 1920) if short else (1280, 720)
        try:
            from PIL import Image
            with Image.open(mini) as im:
                if im.size != esperada:
                    errores.append(f"la miniatura mide {im.size[0]}x{im.size[1]} (tiene que ser "
                                   f"{esperada[0]}x{esperada[1]}{', vertical: es un Short' if short else ''})")
        except ImportError:
            avisos.append("sin Pillow no pude medir la miniatura")
        if short:
            avisos.append("Short: la portada va también en los primeros 0,5 a 1 s del video (regla 29); el "
                          "supervisor la revisa con la hoja de contactos")

    # decisión de color (regla del dueño, 2026-11-21; manual/13_color_con_intencion.md)
    color = f.get("color")
    if not isinstance(color, dict):
        errores.append("falta «color»: neutros, acento, por_que, objetivo y medido (manual/13_color_con_intencion.md)")
    else:
        for c in ("neutros", "acento", "por_que", "objetivo", "medido"):
            if not color.get(c):
                errores.append(f"«color» no dice «{c}»")
        if color.get("neutros") and len(color["neutros"]) != 2:
            errores.append("«color.neutros» lleva 2 colores (regla 2 neutros + 1 acento)")

    # control de texto bloqueante (regla del dueño, 2026-11-21): ortografía, nombres, puntuación, cifras
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import revisar_texto as RT
    textos = RT.leer(ficha_ruta)
    if sub and (carpeta / sub).is_file():
        textos += RT.leer(carpeta / sub)
    e_txt, a_txt = RT.revisar_textos(textos, [f.get("idioma") or "en"])
    errores += [f"texto: {x}" for x in e_txt]
    avisos += [f"texto: {x}" for x in a_txt]
    return errores, avisos


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--plantilla":
        c = Path(sys.argv[2])
        c.mkdir(parents=True, exist_ok=True)
        ficha = dict(PLANTILLA, codigo=c.name)
        (c / "ficha.json").write_text(json.dumps(ficha, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Plantilla -> {c / 'ficha.json'}")
        return
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    errores, avisos = revisar(Path(sys.argv[1]))
    for a in avisos:
        print(f"  AVISO  {a}")
    for e in errores:
        print(f"  ERROR  {e}")
    if errores:
        sys.exit(f"\nNO entregues todavía: {len(errores)} error(es).")
    print("Lista para entregar (todavía no se subió nada).")


if __name__ == "__main__":
    main()
