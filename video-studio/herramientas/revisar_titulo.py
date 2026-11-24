#!/usr/bin/env python3
"""Filtro de títulos del estudio (bloqueante en lo que es dato; aviso en lo que es opinión).

Versión 1.1 (2026-11-24) · parámetros flexibles de Tin & Tan
  Regla del dueño (2026-11-24): «Cambia esas limitantes y define nuevos parámetros; podría ser que los parámetros
  sean flexibles». Ley: video-studio/canales/nostalgia-tin-y-tan/PARAMETROS.md (sección 5: la lista de palabras
  prohibidas por opinión queda sin efecto; solo bloquea lo engañoso, lo difamatorio y la línea editorial).
  Qué cambió respecto de la 1.0:
  - Canal `tin-y-tan`: pasan de ERROR a AVISO las reglas que eran opinión del equipo y no dato de la plataforma:
    longitud fuera de 25–60 (se sigue recomendando 30–50), menos de 3 palabras, cierre en punto/dos puntos/guion,
    puntos suspensivos, cantidad de «!», «?», «:» y paréntesis, frase de búsqueda ausente, repetida, que no empieza
    al inicio o que termina después del carácter 40, Title Case imperfecto, repeticiones de palabras, la
    cifra-respuesta en el título, el título «casi igual» (no idéntico) a uno usado, una sola palabra en mayúsculas
    que no está en la lista de siglas, y las palabras «sensacionalistas» (shocking, insane, secret, viral,
    trending, free, subscribe…). Cada aviso dice su porqué.
  - Siguen como ERROR en `tin-y-tan`: más de 100 caracteres (límite de YouTube), espacios y saltos raros, signos
    repetidos («!!», «??»: YouTube lo llama «loud»), caracteres no permitidos, título en MAYÚSCULAS (salvo siglas),
    nombres propios mal escritos, título idéntico a uno ya usado, marca ajena sin descargo en la descripción,
    términos de la línea editorial, promesas engañosas evidentes (leaked, leak, official, exclusive, not clickbait,
    guaranteed, 100%) y el formato de las cifras (decimal con «≈», separador de miles: regla del dueño, manual 12).
  - Canal `tiky-lumi`: NO cambia nada. Ese perfil no se flexibiliza: manda `infantil/guia_1_a_3.md`.
  - Opción nueva `--estricto`: devuelve el comportamiento de la 1.0 en `tin-y-tan`.
  - Las palabras de una marca autorizada con `--marca` pueden ir en mayúsculas (son su grafía, p. ej. «NVIDIA»).
  - El bloque JSON trae `"filtro": {"version": "1.1", "modo": "flexible" | "estricto" | "infantil", …}`.
Versión 1.0 (2026-11-21): primera versión; todo bloqueaba.

Regla del dueño (2026-11-21): estudiar qué títulos penetran el algoritmo y el SEO según el público, volverlo
instrucción y filtro, y dejarlo en la ficha. El estudio, las fuentes y el porqué de cada umbral están en
video-studio/comercial/titulos.md (sección 6); este script mide lo que una máquina puede medir. Lo que revisa una
persona (que el video cumpla lo que el título promete, que no engañe, línea editorial) no lo sustituye.

Uso:
  python3 video-studio/herramientas/revisar_titulo.py "Título" --canal tin-y-tan|tiky-lumi --idioma en|es|pt-BR \
      --formato short|largo --frase "frase de búsqueda" [--marca "GTA 6"]... [--respuesta 4811]... \
      [--descripcion archivo.txt] [--proyecto nombre] [--registrar] [--estricto]

--marca       marca de terceros que la ficha autoriza a nombrar (solo tin-y-tan).
--respuesta   cifra que es la respuesta del video. En tiky-lumi y con --estricto no puede ir en el título; en
              tin-y-tan da aviso: se decide por video y se mide (PARAMETROS.md, sección 3).
--estricto    aplica a tin-y-tan las reglas de la versión 1.0 (todo bloquea).
--descripcion texto de la descripción; si hay marcas, debe traer el descargo de no afiliación.
--registrar   con 0 errores, anota el título en video-studio/comercial/titulos_usados.json.
Sale con código 1 si hay errores. Imprime al final el bloque «filtro» listo para pegar en la ficha.
"""
import argparse
import datetime
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

VERSION = "1.1"
RAIZ = Path(__file__).resolve().parents[1]
REGISTRO = RAIZ / "comercial" / "titulos_usados.json"

PERFILES = {
    ("tin-y-tan", "short"): dict(min=25, max=60, rec=(30, 50), frase_antes=40, excl=1),
    ("tin-y-tan", "largo"): dict(min=25, max=60, rec=(30, 50), frase_antes=40, excl=1),
    ("tiky-lumi", "largo"): dict(min=20, max=60, rec=(35, 50), frase_antes=45, excl=0),
    ("tiky-lumi", "short"): dict(min=15, max=50, rec=(25, 40), frase_antes=40, excl=0),
}
SIGLAS = {"GTA", "VHS", "CD", "TV", "DVD", "AI", "USA", "UK", "NES", "PS5", "CEO", "GPU", "RTX", "PC", "CPU", "RAM"}
MENORES_EN = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet", "at", "by", "in", "of", "on", "to",
              "up", "as", "vs", "with", "from"}
PERMITIDOS = set(". , : ? ! ' ’ ( ) & ≈ – - \" “ ” ¿ ¡".split()) | {" "}
PROPIOS = ["Tiky", "Lumi", "Tin & Tan", "Tin and Tan", "Tin y Tan", "Tin e Tan"]
MARCAS_INFANTILES = ["cocomelon", "peppa", "bluey", "pocoyo", "baby shark", "ms rachel", "miss rachel", "disney",
                     "mickey", "galinha pintadinha", "mundo bita"]
PUBLICO = {"toddler", "toddlers", "baby", "babies", "kids", "bebé", "bebés", "niños", "crianças", "bebê", "bebês"}
DESCARGO = {"en": "not affiliated with", "es": "sin afiliación con", "pt-BR": "sem afiliação com"}

LIMITE_YOUTUBE = 100  # titulos.md, Y1: «Video titles have a character limit of 100 characters»
# Lo que sigue bloqueando en tin-y-tan flexible: línea editorial del dueño y promesas engañosas evidentes.
DURAS = {
    "en": {"gender", "woke", "leaked", "leak", "official", "exclusive", "not clickbait", "guaranteed", "100%"},
    "es": {"género", "ideología", "oficial", "garantizado", "100 %"},
    "pt-BR": {"gênero", "ideologia", "oficial", "garantido", "100%"},
}

PROHIBIDAS = {
    "en": """you won't believe|you wont believe|won't believe|shocking|shocked|insane|mind-blowing|mind blowing|
gone wrong|must watch|must see|don't miss|dont miss|wait for it|watch till the end|watch until the end|secret|secrets|
exposed|leaked|leak|official|exclusive|free|giveaway|subscribe|like and|click|viral|trending|best ever|number one|
100%|guaranteed|not clickbait|gender|woke""",
    "en+tiky-lumi": """cure|therapy|treatment|disorder|autism|autistic|adhd|delay|delayed|doctor|medical|genius|
smarter|smart baby|iq|brain boost|brain development|will talk|will speak|talk faster|speak faster|learn fast|
learn faster|in minutes|in days|scientifically|proven|surprise|challenge|prank|scary""",
    "es": """tu bebé hablará|hablará|habla más rápido|hablar más rápido|aprende rápido|aprenderá|garantizado|cura|
terapia|tratamiento|trastorno|autismo|autista|tdah|retraso|médico|genio|más inteligente|coeficiente|
cociente intelectual|desarrollo cerebral|científicamente|comprobado|sorpresa|reto|broma|susto|no te lo pierdas|
increíble|impactante|no vas a creer|no creerás|secreto|final inesperado|gratis|suscríbete|dale like|viral|tendencia|
oficial|el mejor|número 1|100 %|género|ideología""",
    "pt-BR": """seu bebê vai falar|vai falar|fala mais rápido|falar mais rápido|aprende rápido|garantido|cura|terapia|
tratamento|transtorno|autismo|autista|tdah|atraso|médico|gênio|mais inteligente|qi|desenvolvimento cerebral|
cientificamente|comprovado|surpresa|desafio|pegadinha|susto|não perca|incrível|chocante|você não vai acreditar|
segredo|final inesperado|grátis|inscreva-se|curta|viral|tendência|oficial|o melhor|número 1|100%|gênero|ideologia""",
}


def lista(clave):
    return [p.strip() for p in PROHIBIDAS.get(clave, "").replace("\n", "").split("|") if p.strip()]


def llano(texto):
    """minúsculas, sin tildes ni puntuación, espacios simples"""
    t = unicodedata.normalize("NFD", texto.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return re.sub(r" +", " ", t).strip()


def palabras(titulo):
    return re.findall(r"[^\W\d_]+(?:['’][^\W\d_]+)?", titulo)


def revisar(titulo, canal, idioma, formato, frase, marcas=(), respuestas=(), descripcion=None, proyecto=None,
            estricto=False):
    errores, avisos = [], []
    E, A = errores.append, avisos.append
    flexible = canal == "tin-y-tan" and not estricto

    def F(mensaje, porque):
        """Regla que era opinión: aviso con su porqué en tin-y-tan flexible; error en infantil y en --estricto."""
        if flexible:
            A(f"{mensaje} · aviso, no bloqueo: {porque}")
        else:
            E(mensaje)
    p = PERFILES[(canal, formato)]
    titulo_nfc = unicodedata.normalize("NFC", titulo)
    n = len(titulo_nfc)

    # M1 longitud
    if n > LIMITE_YOUTUBE:
        E(f"M1 longitud {n}: YouTube no admite más de {LIMITE_YOUTUBE} caracteres")
    elif not p["min"] <= n <= p["max"]:
        F(f"M1 longitud {n}: fuera de {p['min']} a {p['max']} caracteres (recomendado: {p['rec'][0]} a "
          f"{p['rec'][1]})", "el rango es del equipo; el límite de YouTube es 100. En el feed de Shorts se ven "
          "unos 40 caracteres (terceros, sin verificar)")
    elif not p["rec"][0] <= n <= p["rec"][1]:
        A(f"M1 longitud {n}: lo recomendado es de {p['rec'][0]} a {p['rec'][1]}")
    if len(palabras(titulo_nfc)) < 3:
        F("M1 menos de 3 palabras", "el mínimo era opinión; comprueba que el título diga qué cumple el video")

    # M2 espacios y cierres
    if titulo_nfc != titulo_nfc.strip() or "  " in titulo_nfc or re.search(r"[\t\n\r]", titulo_nfc):
        E("M2 espacios al inicio, al final, dobles, tabulación o salto de línea")
    if re.search(r"(\.|:|-|–)$", titulo_nfc.strip()):
        F("M2 termina en punto, dos puntos o guion", "es estilo del canal, no regla de YouTube")
    if re.search(r"[!?¿¡]{2,}", titulo_nfc):
        E("M2 signos repetidos («!!», «??», «?!»): YouTube lo cataloga como «loud» (titulos.md, Y6)")
    if "..." in titulo_nfc or "…" in titulo_nfc:
        F("M2 puntos suspensivos", "es gesto de suspenso; solo si el video cumple lo que el título deja abierto")

    # M3 caracteres
    raros = sorted({c for c in titulo_nfc if not (c.isalnum() or c in PERMITIDOS)})
    if raros:
        E("M3 caracteres no permitidos: " + " ".join(raros))
    for signo, maximo in (("!", p["excl"]), ("?", 1), (":", 1), ("(", 1)):
        if titulo_nfc.count(signo) > maximo:
            F(f"M3 más de {maximo} «{signo}»", "el tope era estilo del canal")

    # M4 frase de búsqueda
    tl, fl = llano(titulo_nfc), llano(frase)
    if not fl:
        E("M4 falta la frase de búsqueda")
    elif tl.count(fl) != 1:
        F(f"M4 la frase «{frase}» debe aparecer completa una sola vez (aparece {tl.count(fl)})",
          "YouTube pide «lo importante al inicio» (Y2) pero no exige la frase literal; revisa que el título use "
          "las palabras que la gente busca")
    else:
        # posición en el título original, palabra a palabra
        toks = [(m.group(0), m.start(), m.end()) for m in re.finditer(r"[^\W_]+", titulo_nfc)]
        ll = [llano(t[0]) for t in toks]
        fw = fl.split()
        for i in range(len(ll) - len(fw) + 1):
            if ll[i:i + len(fw)] == fw:
                ini, fin = toks[i][1] + 1, toks[i + len(fw) - 1][2]
                if fin > p["frase_antes"]:
                    F(f"M4 la frase termina en el carácter {fin}; debe terminar antes del {p['frase_antes']}",
                      "el corte de ≈ 40 caracteres del feed es de terceros, sin dato oficial")
                if ini > 4 and fl != tl:
                    A(f"M4 la frase empieza en el carácter {ini}; mejor al inicio (1 a 4)")
                break

    # M5 mayúsculas sostenidas
    letras = [c for c in titulo_nfc if c.isalpha()]
    permitidas = SIGLAS if canal == "tin-y-tan" else set()
    if flexible:  # la grafía de una marca autorizada no es «gritar»
        permitidas = permitidas | {w for marca in marcas for w in palabras(marca) if w.isupper()}
    gritadas = [w for w in palabras(titulo_nfc) if len(w) >= 2 and w.isupper() and w not in permitidas]
    if flexible and len(gritadas) == 1:
        A(f"M5 «{gritadas[0]}» va toda en mayúsculas y no está en la lista de siglas · aviso, no bloqueo: si es "
          "una sigla o una marca, autorízala con --marca; YouTube pide limitar las MAYÚSCULAS, no prohíbe una sigla")
    else:
        for w in gritadas:
            E(f"M5 «{w}» va toda en mayúsculas")
    if letras and sum(c.isupper() for c in letras) / len(letras) > 0.45:
        E("M5 más del 45 % de las letras en mayúscula")

    # M6 mayúsculas del idioma
    ws = palabras(titulo_nfc)
    propios_sueltos = {w for nombre in PROPIOS + list(marcas) for w in palabras(nombre)}
    if idioma == "en":
        for i, w in enumerate(ws):
            if i == 0 or w.lower() not in MENORES_EN:
                if w[0].islower():
                    F(f"M6 en inglés va en Title Case: «{w}» empieza en minúscula",
                      "la coherencia de mayúsculas dentro del canal es estilo, no dato")
            elif w[0].isupper() and w.lower() not in ("with", "from") and w not in propios_sueltos:
                A(f"M6 «{w}» es palabra menor: en Title Case va en minúscula")
    else:
        tras = {m.end() for m in re.finditer(r"[:?¿¡(]\s*", titulo_nfc)}
        for m in re.finditer(r"[^\W\d_]+", titulo_nfc):
            w = m.group(0)
            if m.start() == 0 or m.start() in tras or w in propios_sueltos or w in permitidas:
                continue
            if w[0].isupper():
                A(f"M6 «{w}» lleva mayúscula sin ser inicio ni nombre propio (mayúscula de frase)")
        if ws and ws[0][0].islower():
            F("M6 el título empieza en minúscula", "es estilo; los nombres propios sí bloquean (M7)")

    # M7 nombres propios
    for nombre in PROPIOS:
        for m in re.finditer(re.escape(nombre), titulo_nfc, flags=re.I):
            if m.group(0) != nombre:
                E(f"M7 nombre propio mal escrito: «{m.group(0)}» debe ser «{nombre}»")

    # M8 palabras prohibidas
    base = {"en": "en", "es": "es", "pt-BR": "pt-BR"}[idioma]
    vetadas = lista(base) + (lista("en+tiky-lumi") if idioma == "en" and canal == "tiky-lumi" else [])
    bajo = " " + re.sub(r"\s+", " ", titulo_nfc.lower()) + " "
    for v in vetadas:
        if re.search(r"(?<![\wáéíóúñçãõâêô])" + re.escape(v) + r"(?![\wáéíóúñçãõâêô])", bajo):
            if flexible and v not in DURAS[base]:
                A(f"M8 palabra sensacionalista: «{v}» · aviso, no bloqueo: la lista era opinión del equipo "
                  "(YouTube no publica palabras); solo se usa si el video la cumple de verdad")
            elif v in DURAS[base]:
                E(f"M8 término bloqueado (línea editorial o promesa engañosa): «{v}»")
            else:
                E(f"M8 palabra o frase prohibida: «{v}»")

    # M9 repeticiones
    cuenta = {}
    for w in ws:
        if len(w) >= 4:
            cuenta[llano(w)] = cuenta.get(llano(w), 0) + 1
    for w, c in cuenta.items():
        if c >= 3:
            F(f"M9 «{w}» se repite {c} veces", "el tope era opinión; cuida que no parezca relleno de palabras "
              "clave (Y18)")
        elif c == 2:
            A(f"M9 «{w}» se repite 2 veces")
    if canal == "tiky-lumi" and sum(w.lower() in PUBLICO for w in ws) > 1:
        E("M9 más de una palabra de público (bebé, niños, toddler…)")

    # M10 y M11 separadores y marcas
    if canal == "tiky-lumi":
        if " - " in titulo_nfc or "|" in titulo_nfc:
            E("M10 separador « - » o «|» no permitido")
        for marca in MARCAS_INFANTILES:
            if marca in tl:
                E(f"M11 marca ajena en un título infantil: «{marca}»")
        if marcas:
            E("M11 el canal infantil no nombra marcas de terceros")
    elif marcas:
        for marca in marcas:
            if llano(marca) not in tl:
                A(f"M11 la marca autorizada «{marca}» no aparece en el título")
        if descripcion is None:
            A("M11 hay marcas de terceros: falta comprobar el descargo en la descripción (--descripcion)")
        elif DESCARGO[idioma] not in descripcion.lower():
            E(f"M11 la descripción no trae el descargo «{DESCARGO[idioma]}…»")

    # M12 cifras
    for m in re.finditer(r"\d+[.,]\d+|\d+/\d+", titulo_nfc):
        cifra = m.group(0)
        miles = re.fullmatch(r"\d{1,3}([.,]\d{3})+", cifra)
        if miles:
            sep = "," if idioma == "en" else "."
            if sep not in cifra:
                E(f"M12 separador de miles de «{cifra}»: en {idioma} es «{sep}»")
        elif not titulo_nfc[:m.start()].rstrip().endswith("≈"):
            E(f"M12 «{cifra}» es decimal o fracción: va aproximada y con «≈» delante")
    if re.search(r"(~|\b(about|around|almost|casi|cerca de|unos|quase|cerca de)\b)\s*\d", titulo_nfc, flags=re.I):
        E("M12 aproximación con palabra o «~» delante de una cifra: se usa «≈»")
    digitos_titulo = re.sub(r"[.,\s]", "", titulo_nfc)
    for r in respuestas:
        if re.sub(r"[.,\s]", "", str(r)) in digitos_titulo:
            F(f"M12 el título revela la respuesta del video ({r})", "la cifra en el título se decide por video y "
              "se mide: «se quedó a mirar» con y sin cifra (PARAMETROS.md, sección 3). Debe coincidir con el video")
    if canal == "tiky-lumi":
        fuera = re.sub(r"\([^)]*\)", "", titulo_nfc)
        if re.search(r"\d", fuera):
            E("M12 en el canal infantil la única cifra es la edad entre paréntesis")

    # M13 duplicados
    usados = json.loads(REGISTRO.read_text(encoding="utf8")) if REGISTRO.exists() else []
    for u in usados:
        if u["canal"] != canal or u["idioma"] != idioma or (proyecto and u.get("proyecto") == proyecto):
            continue
        r = difflib.SequenceMatcher(None, tl, llano(u["titulo"])).ratio()
        if tl == llano(u["titulo"]):
            E(f"M13 idéntico a un título ya usado («{u['titulo']}»)")
        elif r >= 0.90:
            F(f"M13 casi igual a un título ya usado («{u['titulo']}», parecido {r:.2f})",
              "se puede repetir una forma que funcionó si el contenido cambia (hasta 3 seguidas); idéntico sí bloquea")
        elif r >= 0.80:
            A(f"M13 se parece a un título ya usado («{u['titulo']}», parecido {r:.2f})")

    return n, errores, avisos


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("titulo")
    ap.add_argument("--canal", required=True, choices=["tin-y-tan", "tiky-lumi"])
    ap.add_argument("--idioma", required=True, choices=["en", "es", "pt-BR"])
    ap.add_argument("--formato", required=True, choices=["short", "largo"])
    ap.add_argument("--frase", required=True)
    ap.add_argument("--marca", action="append", default=[])
    ap.add_argument("--respuesta", action="append", default=[])
    ap.add_argument("--descripcion")
    ap.add_argument("--proyecto")
    ap.add_argument("--registrar", action="store_true")
    ap.add_argument("--estricto", action="store_true",
                    help="tin-y-tan con las reglas de la versión 1.0 (todo bloquea)")
    a = ap.parse_args()

    desc = Path(a.descripcion).read_text(encoding="utf8") if a.descripcion else None
    n, errores, avisos = revisar(a.titulo, a.canal, a.idioma, a.formato, a.frase, a.marca, a.respuesta, desc,
                                 a.proyecto, a.estricto)
    modo = "infantil" if a.canal == "tiky-lumi" else ("estricto" if a.estricto else "flexible")
    hoy = datetime.date.today().isoformat()
    print(f"Filtro de títulos v{VERSION} ({modo}) · «{a.titulo}» · {n} caracteres · {a.canal} · {a.idioma} · "
          f"{a.formato}")
    for e in errores:
        print("  ERROR ", e)
    for v in avisos:
        print("  AVISO ", v)
    resultado = "PASA" if not errores else "NO PASA"
    print(f"\n{resultado}: {len(errores)} error(es), {len(avisos)} aviso(s). Falta la revisión de una persona "
          "(el video cumple el título, no engaña, línea editorial).")
    print("\nBloque para la ficha:")
    print(json.dumps({"caracteres": n, "filtro": {"version": VERSION, "modo": modo, "fecha": hoy,
                                                   "resultado": resultado,
                                                   "errores": errores, "avisos": avisos}},
                     ensure_ascii=False, indent=2))
    if a.registrar and not errores:
        usados = json.loads(REGISTRO.read_text(encoding="utf8")) if REGISTRO.exists() else []
        usados = [u for u in usados if not (a.proyecto and u.get("proyecto") == a.proyecto
                                            and u["idioma"] == a.idioma and u["canal"] == a.canal)]
        usados.append({"titulo": a.titulo, "canal": a.canal, "idioma": a.idioma, "formato": a.formato,
                       "proyecto": a.proyecto, "fecha": hoy, "filtro": VERSION})
        REGISTRO.write_text(json.dumps(usados, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
        print(f"Anotado en {REGISTRO.relative_to(RAIZ.parent)}")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
