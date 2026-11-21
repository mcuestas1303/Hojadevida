#!/usr/bin/env python3
"""Control de texto del estudio (bloqueante): ortografía, nombres propios, puntuación y cifras.

Regla del dueño (2026-11-21): «un error ortográfico puede matar el video […] no son cosas que tengan flexibilidad».
Ningún texto sale del estudio (pantalla, subtítulos, miniatura, banner, título, descripción, etiquetas, perfil) sin
pasar por aquí con 0 errores. Lo corre el supervisor de continuidad; entrega.py lo corre solo sobre la ficha y los
subtítulos.

Uso:
  python3 video-studio/herramientas/revisar_texto.py <archivo_o_carpeta>... [--idioma en|es|pt|en,es]

Qué lee:
  .srt  → el texto de los subtítulos
  .json → titulo, descripcion y etiquetas (ficha.json)
  .txt  → todo el texto
  .py   → el texto que se dibuja en pantalla: literales de T("…"), K("…"), titulo(lz, "…"), texto(…, "…")
Si no se da --idioma, se toma «idioma» de la ficha.json que haya; si no hay, se pide.

Qué revisa (cada hallazgo es ERROR salvo que diga AVISO):
  - nombres propios en minúscula: Tin, Tan, Tiky, Lumi, Spike y los nombres de canal (también en hashtags)
  - ortografía con Hunspell (diccionarios de LibreOffice: en, es, pt-BR) más video-studio/glosario.txt
  - espacios dobles, espacio antes de signo, palabra repetida («the the»), comillas, paréntesis y ¿? ¡! sin cerrar
  - oraciones de título y descripción que empiezan en minúscula
  - separador decimal del idioma: «4,76» en inglés es error; «4.76» en español es aviso
  - números con decimales o fracciones sin «≈» delante: se aproximan (regla del dueño, 2026-11-21); en citas
    textuales de una fuente, solo aviso
Sale con código 1 si hay errores. Si falta el corrector ortográfico, también: la ortografía no queda comprobada.
"""
import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
GLOSARIO = RAIZ / "glosario.txt"

# Nombres propios que siempre van con mayúscula inicial. Los que también son palabras comunes en un idioma
# («tan» en español, «tin» y «tan» en inglés) solo son error en minúscula cuando van en pareja («tin & tan»);
# sueltos quedan como AVISO para que una persona los lea.
NOMBRES = ["Tin", "Tan", "Tiky", "Lumi", "Spike"]
COMUNES = {"es": {"tan"}, "en": {"tin", "tan"}, "pt": {"tan"}}
PAREJA = re.compile(r"\b(tin|tan)(\s*&\s*|\s+(?:y|and|e)\s+)(tin|tan)\b", re.IGNORECASE)
HASHTAG_PAREJA = re.compile(r"#(tin|tan)(and|y|e)?(tin|tan)\b", re.IGNORECASE)

# enlaces, código entre comillas invertidas y rutas de archivo no se revisan (las unidades «cm/s» y las
# fracciones «7/8» sí)
URL = re.compile(r"https?://[^\s)»”\"]+|www\.[^\s)»”\"]+|`[^`]*`|[\w.-]+(?:/[\w.-]+)+\.\w{1,4}\b|[\w.-]+(?:/[\w.-]+){2,}")
PALABRA = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:['’][A-Za-zÀ-ÖØ-öø-ÿ]+)*")
LITERAL_PY = re.compile(r"""\b(?:T|K|titulo|texto|etiqueta)\((?:[^()"']*?,\s*)?(["'])(.+?)\1""")


def leer(ruta):
    """Devuelve [(origen, texto, es_oracion)] de un archivo. es_oracion: el texto debe empezar en mayúscula."""
    s = ruta.suffix.lower()
    if s == ".srt":
        lineas = [ln for ln in ruta.read_text(encoding="utf-8").splitlines()
                  if ln.strip() and not ln.strip().isdigit() and "-->" not in ln]
        return [(f"{ruta.name}:{i + 1}", ln, False) for i, ln in enumerate(lineas)]
    if s == ".json":
        d = json.loads(ruta.read_text(encoding="utf-8"))
        out = []
        if d.get("titulo"):
            out.append((f"{ruta.name}:titulo", d["titulo"], True))
        for i, parrafo in enumerate(str(d.get("descripcion", "")).split("\n")):
            if parrafo.strip():
                out.append((f"{ruta.name}:descripcion línea {i + 1}", parrafo, True))
        for e in d.get("etiquetas", []) or []:
            out.append((f"{ruta.name}:etiqueta", str(e), False))
        return out
    if s == ".py":
        out = []
        for n, ln in enumerate(ruta.read_text(encoding="utf-8").splitlines(), 1):
            for m in LITERAL_PY.finditer(ln):
                out.append((f"{ruta.name}:{n} (en pantalla)", m.group(2), False))
        return out
    return [(f"{ruta.name}:{n}", ln, False) for n, ln in enumerate(ruta.read_text(encoding="utf-8").splitlines(), 1)
            if ln.strip()]


DICCIONARIOS = Path(__file__).resolve().parent / "diccionarios"   # los instala instalar_corrector.sh
ARCHIVO_DIC = {"en": "en", "es": "es", "pt": "pt"}                   # pt = portugués de Brasil


class Corrector:
    """Hunspell (motor spylls, diccionarios de LibreOffice vía wooorm/dictionaries): acepta plurales, conjugaciones
    y mayúsculas de inicio de oración. Varios idiomas: una palabra vale si la acepta cualquiera."""

    def __init__(self, idiomas):
        from spylls.hunspell import Dictionary
        self.dics = []
        for i in idiomas:
            base = DICCIONARIOS / ARCHIVO_DIC.get(i, i) / "index"
            if not base.with_suffix(".dic").exists():
                raise FileNotFoundError(base)
            self.dics.append(Dictionary.from_files(str(base)))

    def __contains__(self, palabra):
        return any(d.lookup(palabra) for d in self.dics)

    def correction(self, palabra):
        for d in self.dics:
            for s in d.suggest(palabra):
                return s
        return None


def corrector(idiomas):
    try:
        return Corrector(idiomas)
    except (ImportError, FileNotFoundError):
        return None


def glosario():
    if not GLOSARIO.exists():
        return set()
    return {ln.strip().lower() for ln in GLOSARIO.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.startswith("#")}


def revisar_textos(textos, idiomas):
    """textos: [(origen, texto, es_oracion)]. Devuelve (errores, avisos)."""
    errores, avisos = [], []
    sc = corrector(idiomas)
    permitidas = glosario()
    if sc is None:
        errores.append("ortografía SIN COMPROBAR: falta el corrector (Hunspell). Se instala con "
                       "bash video-studio/herramientas/instalar_corrector.sh; mientras tanto el supervisor lee cada palabra y lo deja escrito en 07_revision/")
    for origen, texto, es_oracion in textos:
        limpio = URL.sub("§", texto)

        # nombres propios
        for m in PAREJA.finditer(limpio):
            for parte in (m.group(1), m.group(3)):
                if not parte[0].isupper():
                    errores.append(f"{origen}: «{m.group(0)}» → los nombres van con mayúscula: «Tin», «Tan»")
                    break
        for m in HASHTAG_PAREJA.finditer(limpio):
            if not (m.group(1)[0].isupper() and m.group(3)[0].isupper()):
                errores.append(f"{origen}: «{m.group(0)}» → hashtag con mayúsculas: «#TinAndTan» / «#TinYTan»")
        sin_parejas = HASHTAG_PAREJA.sub(" ", PAREJA.sub(" ", limpio))
        for nombre in NOMBRES:
            for m in re.finditer(rf"(?<![\w#]){nombre.lower()}(?!\w)", sin_parejas):
                if any(nombre.lower() in COMUNES.get(i, set()) for i in idiomas):
                    avisos.append(f"{origen}: «{m.group(0)}» en minúscula: si es el personaje, va «{nombre}»")
                else:
                    errores.append(f"{origen}: «{m.group(0)}» → «{nombre}» (nombre propio)")

        # puntuación y espacios
        if "  " in limpio.strip():
            errores.append(f"{origen}: espacio doble")
        if re.search(r"\s[,.;:!?](?!\w)", limpio) and not any(i == "fr" for i in idiomas):
            errores.append(f"{origen}: espacio antes de un signo de puntuación")
        for m in re.finditer(r"\b(\w+)\s+\1\b", limpio, re.IGNORECASE):
            if not m.group(1).isdigit():
                errores.append(f"{origen}: palabra repetida «{m.group(0)}»")
        for a, b in (("(", ")"), ("«", "»"), ("“", "”")):
            if limpio.count(a) != limpio.count(b):
                errores.append(f"{origen}: «{a}» y «{b}» no cierran")
        if limpio.count('"') % 2:
            errores.append(f'{origen}: comillas " sin cerrar')
        if idiomas == ["es"]:
            for a, b in (("¿", "?"), ("¡", "!")):
                if limpio.count(a) != limpio.count(b):
                    errores.append(f"{origen}: «{a}» y «{b}» no van en pareja (español)")
        if es_oracion:
            for m in re.finditer(r"(?:^|[.!?]\s+)([a-záéíóúñ])", limpio.strip()):
                errores.append(f"{origen}: oración que empieza en minúscula («{m.group(1)}…»)")

        # cifras
        if idiomas == ["en"] and re.search(r"\d,\d{1,2}(?!\d)", limpio):
            errores.append(f"{origen}: coma decimal en inglés (se escribe con punto: 4.76)")
        if idiomas == ["es"] and re.search(r"(?<![\d.])\d+\.\d{1,2}(?![\d.])", limpio):
            avisos.append(f"{origen}: punto decimal en español (se escribe con coma: 4,76), revisar")

        # números con decimales o fracciones: se aproximan y llevan «≈» (regla del dueño, 2026-11-21).
        # En una cita textual de una fuente («…» o "…") el número no se toca: queda como AVISO.
        citas = re.findall(r'"[^"]*"|«[^»]*»|“[^”]*”', limpio)
        for m in re.finditer(r"(?<![\d.,/])(\d+(?:[.,]\d+)?\s?[½⅓⅔¼¾⅕⅛⅜⅝⅞]|\d+/\d+(?![\d/])|\d+[.,]\d{1,2}(?!\d)|\d+[.,]\d{4,}|[½⅓⅔¼¾⅛⅜⅝⅞])", limpio):
            num = m.group(0)
            if re.fullmatch(r"\d{1,3}[.,]\d{3}", num):
                continue                       # separador de miles (1,170 / 1.170), no es decimal
            antes = limpio[max(0, m.start() - 3):m.start()]
            if "≈" in antes or "~" in antes:
                continue
            if any(num in c for c in citas):
                avisos.append(f"{origen}: «{num}» dentro de una cita textual: se deja como en la fuente")
            else:
                errores.append(f"{origen}: «{num}» tiene decimales o fracción → se aproxima y lleva «≈» "
                               f"(p. ej. «≈ 422 ft», «≈ 4.8 cm/s»); en la voz: «about», «unos», «cerca de»")

        # ortografía
        if sc is not None:
            for m in PALABRA.finditer(re.sub(r"#\w+", " ", limpio)):
                p = m.group(0).replace("’", "'")
                bajo = p.lower()
                if len(p) < 2 or bajo in permitidas or (p[0].isupper() and p in NOMBRES):
                    continue
                if p in sc or bajo in sc:
                    continue
                if "'" in bajo and all(x in sc or x in permitidas for x in bajo.split("'")):
                    continue
                sug = sc.correction(bajo)
                errores.append(f"{origen}: «{p}» no está en el diccionario"
                               + (f" (¿«{sug}»?)" if sug and sug != bajo else "")
                               + " — si es correcta, se agrega a video-studio/glosario.txt con su porqué")
    return errores, avisos


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("rutas", nargs="+", type=Path)
    ap.add_argument("--idioma", help="en, es, pt o varios separados por coma (textos mezclados)")
    a = ap.parse_args()

    archivos = []
    for r in a.rutas:
        if r.is_dir():
            archivos += sorted(p for p in r.rglob("*") if p.suffix.lower() in (".srt", ".json", ".txt", ".py"))
        elif r.exists():
            archivos.append(r)
        else:
            sys.exit(f"No existe: {r}")
    idiomas = a.idioma.split(",") if a.idioma else None
    if not idiomas:
        for f in archivos:
            if f.name == "ficha.json":
                idiomas = [json.loads(f.read_text(encoding="utf-8")).get("idioma", "")]
        if not idiomas or not idiomas[0]:
            sys.exit("Falta --idioma (en, es, pt).")

    textos = []
    for f in archivos:
        textos += leer(f)
    errores, avisos = revisar_textos(textos, idiomas)
    print(f"Control de texto · {len(textos)} textos · idioma {','.join(idiomas)}")
    for x in avisos:
        print(f"  AVISO  {x}")
    for x in errores:
        print(f"  ERROR  {x}")
    if errores:
        sys.exit(f"\nNO PASA: {len(errores)} error(es). Ningún texto con errores sale del estudio.")
    print("\nPASA: 0 errores." + (" Leer los avisos uno por uno." if avisos else ""))


if __name__ == "__main__":
    main()
