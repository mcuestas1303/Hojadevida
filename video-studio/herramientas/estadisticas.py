#!/usr/bin/env python3
"""Lee las estadisticas exportadas de YouTube Studio, TikTok o Instagram y dice que rinde mas
para el objetivo comercial del video.

Uso:
    estadisticas.py <export.csv> [mas.csv ...] [--etiquetas etiquetas.csv] [--costos costos.csv]
                    [--objetivo monetizar|alcance|recordacion|comunidad|conversion|viralidad]
                    [--salida informe.md]

- Los CSV pueden tener columnas en espanol o ingles; se reconocen solas.
- etiquetas.csv: una fila por video con `id` o `titulo` y las decisiones creativas que se quieren
  comparar (personaje, modo, gancho, emocion, duracion_s, formato, hora...).
- costos.csv: `id` o `titulo` y `creditos` gastados en ese video (sale de costos.md de cada proyecto).
Solo usa la biblioteca estandar de Python. No sube nada a ningun lado.
"""
import argparse
import csv
import re
import statistics
import sys
import unicodedata
from pathlib import Path

# Columna canonica -> nombres posibles (normalizados: minusculas, sin acentos ni signos).
ALIAS = {
    "id": ["contenido", "content", "video id", "id del video", "id", "post id", "id de la publicacion"],
    "titulo": ["titulo del video", "video title", "titulo", "title", "descripcion", "description", "caption"],
    "fecha": ["hora de publicacion del video", "video publish time", "fecha de publicacion", "publish time",
              "fecha", "date", "posted", "hora de publicacion"],
    "duracion": ["duracion", "duration", "video duration", "duracion del video"],
    "vistas": ["vistas", "views", "video views", "visualizaciones", "reproducciones", "plays"],
    "horas": ["tiempo de visualizacion horas", "watch time hours", "tiempo de reproduccion horas"],
    "duracion_media": ["duracion promedio de visualizacion", "average view duration", "average watch time",
                       "tiempo de visualizacion promedio", "tiempo medio de reproduccion"],
    "pct_visto": ["porcentaje promedio visto", "average percentage viewed", "porcentaje visto promedio"],
    "completo": ["watched full video", "vieron el video completo", "visualizaciones completas"],
    "impresiones": ["impresiones", "impressions"],
    "ctr": ["tasa de clics de las impresiones", "impressions click through rate", "ctr"],
    "seguidores": ["suscriptores", "subscribers", "suscriptores obtenidos", "subscribers gained", "new followers",
                   "nuevos seguidores", "seguimientos", "follows"],
    "likes": ["me gusta", "likes"],
    "comentarios": ["comentarios anadidos", "comments added", "comentarios", "comments"],
    "compartidos": ["compartidos", "shares", "veces compartido"],
    "guardados": ["guardados", "saves", "add to favorites", "favoritos"],
    "clics": ["clics en el enlace", "link clicks", "clics", "clicks"],
    "alcance": ["alcance", "reach", "cuentas alcanzadas"],
    "ingresos": ["ingresos estimados usd", "estimated revenue usd", "ingresos estimados", "estimated revenue"],
}

OBJETIVOS = {
    "monetizar": ("horas", "Horas de vista (y retencion)"),
    "alcance": ("vistas", "Vistas"),
    "recordacion": ("guardados_mil", "Guardados por mil vistas"),
    "comunidad": ("seguidores_mil", "Seguidores ganados por mil vistas"),
    "conversion": ("clics_mil", "Clics por mil vistas"),
    "viralidad": ("compartidos_mil", "Compartidos por mil vistas"),
}
MUESTRA_MINIMA = 5


def norm(texto):
    t = unicodedata.normalize("NFKD", texto or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", t)).strip()


def numero(valor):
    """'1.234', '1,234', '12,5 %', '0:01:23', '83s' -> float (segundos para tiempos)."""
    v = (valor or "").strip().replace("%", "").replace(" ", "").strip()
    if not v or v in {"-", "—"}:
        return None
    if re.fullmatch(r"\d+(:\d{1,2}){1,2}(\.\d+)?", v):
        partes = [float(p) for p in v.split(":")]
        while len(partes) < 3:
            partes.insert(0, 0.0)
        return partes[0] * 3600 + partes[1] * 60 + partes[2]
    v = v.rstrip("s").strip()
    if re.fullmatch(r"\d{1,3}(\.\d{3})+(,\d+)?", v):        # 1.234.567,8
        v = v.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(,\d{3})+(\.\d+)?", v):      # 1,234,567.8
        v = v.replace(",", "")
    else:
        v = v.replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return None


def mapear(encabezados):
    mapa = {}
    for col in encabezados:
        n = norm(col)
        for canon, nombres in ALIAS.items():
            if canon in mapa.values():
                continue
            if n in nombres or any(n.startswith(x) for x in nombres if len(x) > 6):
                mapa[col] = canon
                break
    return mapa


def leer_csv(ruta):
    texto = Path(ruta).read_text(encoding="utf-8-sig", errors="replace")
    muestra = texto[:4096]
    delim = ";" if muestra.count(";") > muestra.count(",") else ("\t" if muestra.count("\t") > muestra.count(",") else ",")
    filas = list(csv.DictReader(texto.splitlines(), delimiter=delim))
    if not filas:
        return []
    mapa = mapear(filas[0].keys())
    if "vistas" not in mapa.values():
        sys.exit(f"{ruta}: no encuentro la columna de vistas. Columnas: {', '.join(filas[0].keys())}")
    videos = []
    for f in filas:
        v = {canon: f.get(col) for col, canon in mapa.items()}
        if norm(v.get("id") or "") == "total" or norm(v.get("titulo") or "") == "total":
            continue   # fila de totales de YouTube Studio
        for k in list(v):
            if k not in ("id", "titulo", "fecha"):
                v[k] = numero(v[k])
        if not v.get("vistas"):
            continue
        v["fuente"] = Path(ruta).name
        videos.append(v)
    return videos


def clave(v):
    return norm(v.get("id") or "") or norm(v.get("titulo") or "")


def leer_tabla_extra(ruta):
    filas = list(csv.DictReader(Path(ruta).read_text(encoding="utf-8-sig").splitlines()))
    tabla = {}
    for f in filas:
        f = {norm(k).replace(" ", "_"): (val or "").strip() for k, val in f.items()}
        k = norm(f.get("id") or "") or norm(f.get("titulo") or "")
        if k:
            tabla[k] = f
    return tabla


def unir_extra(videos, tabla):
    sin_pareja = 0
    for v in videos:
        extra = tabla.get(norm(v.get("id") or "")) or tabla.get(norm(v.get("titulo") or ""))
        if extra:
            v.setdefault("etiquetas", {}).update({k: val for k, val in extra.items() if k not in ("id", "titulo")})
        else:
            sin_pareja += 1
    return sin_pareja


def calcular(v):
    vistas = v["vistas"]
    por_mil = lambda campo: (v[campo] / vistas * 1000) if v.get(campo) is not None else None
    for campo in ("compartidos", "guardados", "seguidores", "comentarios", "clics"):
        v[f"{campo}_mil"] = por_mil(campo)
    inter = [v.get(c) or 0 for c in ("likes", "comentarios", "compartidos", "guardados")]
    v["interaccion"] = sum(inter) / vistas * 100 if any(inter) else None
    if v.get("pct_visto") is None and v.get("duracion_media") and v.get("duracion"):
        v["pct_visto"] = v["duracion_media"] / v["duracion"] * 100
    if v.get("horas") is None and v.get("duracion_media"):
        v["horas"] = v["duracion_media"] * vistas / 3600
    cred = numero((v.get("etiquetas") or {}).get("creditos"))
    v["creditos"] = cred
    v["creditos_mil"] = cred / vistas * 1000 if cred is not None else None


def mediana(valores):
    vals = [x for x in valores if x is not None]
    return statistics.median(vals) if vals else None


def fmt(x, dec=1):
    if x is None:
        return "—"
    if abs(x) >= 1000:
        return f"{x:,.0f}".replace(",", ".")
    return f"{x:.{dec}f}".replace(".", ",")


def informe(videos, objetivo):
    kpi, nombre_kpi = OBJETIVOS[objetivo]
    L = [f"# Informe de estadísticas · objetivo: {objetivo}", "",
         f"- Videos analizados: {len(videos)}",
         f"- Indicador principal: **{nombre_kpi}**"]
    con_kpi = [v for v in videos if v.get(kpi) is not None]
    if not con_kpi:
        L += ["", f"Los datos no traen lo necesario para medir «{nombre_kpi}». Exporta esa columna o elige otro "
                  "objetivo."]
        return "\n".join(L)
    med = mediana(v[kpi] for v in con_kpi)
    L.append(f"- Mediana de la cuenta: {fmt(med, 2)}")
    if len(videos) < MUESTRA_MINIMA:
        L.append(f"- ⚠️ Menos de {MUESTRA_MINIMA} videos: sirve para mirar, no para decidir.")

    L += ["", "## Videos ordenados por el indicador", "",
          "| # | Video | Vistas | Retención % | Compart./mil | Guard./mil | Seg./mil | Horas | Créd./mil vistas | vs. mediana |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for i, v in enumerate(sorted(con_kpi, key=lambda x: x[kpi], reverse=True), 1):
        nombre = (v.get("titulo") or v.get("id") or "?")[:48]
        rel = (v[kpi] / med - 1) * 100 if med else 0
        L.append(f"| {i} | {nombre} | {fmt(v['vistas'], 0)} | {fmt(v.get('pct_visto'))} | "
                 f"{fmt(v.get('compartidos_mil'))} | {fmt(v.get('guardados_mil'))} | {fmt(v.get('seguidores_mil'))} | "
                 f"{fmt(v.get('horas'))} | {fmt(v.get('creditos_mil'), 2)} | {'+' if rel >= 0 else ''}{fmt(rel, 0)} % |")

    etiquetadas = [v for v in con_kpi if v.get("etiquetas")]
    campos = sorted({k for v in etiquetadas for k in v["etiquetas"] if k != "creditos"})
    hallazgos = []
    if campos:
        L += ["", "## Qué decisiones rinden más", "",
              "Mediana del indicador por cada valor de etiqueta, contra la mediana de la cuenta. "
              f"Los grupos con menos de {MUESTRA_MINIMA} videos se marcan con ⚠️.", ""]
        for campo in campos:
            grupos = {}
            for v in etiquetadas:
                valor = v["etiquetas"].get(campo)
                if valor:
                    grupos.setdefault(valor, []).append(v[kpi])
            if len(grupos) < 2:
                continue
            L += [f"### {campo}", "", "| Valor | Videos | Mediana | vs. cuenta |", "|---|---|---|---|"]
            for valor, vals in sorted(grupos.items(), key=lambda kv: statistics.median(kv[1]), reverse=True):
                m = statistics.median(vals)
                rel = (m / med - 1) * 100 if med else 0
                aviso = " ⚠️" if len(vals) < MUESTRA_MINIMA else ""
                L.append(f"| {valor} | {len(vals)}{aviso} | {fmt(m, 2)} | {'+' if rel >= 0 else ''}{fmt(rel, 0)} % |")
                if len(vals) >= MUESTRA_MINIMA and abs(rel) >= 20:
                    hallazgos.append((rel, campo, valor, len(vals)))
            L.append("")
    elif videos:
        L += ["", "_Sin etiquetas: agrega `--etiquetas etiquetas.csv` para saber qué decisiones creativas rinden._"]

    L += ["", "## Para el director", ""]
    if hallazgos:
        for rel, campo, valor, n in sorted(hallazgos, reverse=True):
            verbo = "Repetir" if rel > 0 else "Revisar o dejar"
            L.append(f"- **{verbo}** `{campo} = {valor}`: {'+' if rel > 0 else ''}{fmt(rel, 0)} % frente a la cuenta "
                     f"({n} videos).")
    else:
        L.append(f"- Ninguna decisión se separa todavía de la mediana (±20 % con {MUESTRA_MINIMA} videos o más). "
                 "Sigue probando un cambio por vez.")
    retencion = [v for v in videos if v.get("pct_visto") is not None]
    if retencion:
        bajos = [v for v in retencion if v["pct_visto"] < 0.6 * mediana(x["pct_visto"] for x in retencion)]
        if bajos:
            L.append(f"- {len(bajos)} video(s) con retención muy por debajo de la mediana: revisar el gancho (si se "
                     "van en el segundo 1–2) o la parte lenta (si se van a la mitad) en la curva de cada uno.")
    caros = [v for v in videos if v.get("creditos_mil") is not None]
    if caros:
        mejor = min(caros, key=lambda v: v["creditos_mil"])
        L.append(f"- Más eficiente en créditos: «{(mejor.get('titulo') or mejor.get('id'))[:48]}» "
                 f"({fmt(mejor['creditos_mil'], 2)} créditos por mil vistas).")
    L.append("- No decidas con Shorts de menos de 48–72 h ni con videos largos de menos de 7 días.")
    return "\n".join(L)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv", nargs="+")
    p.add_argument("--etiquetas")
    p.add_argument("--costos")
    p.add_argument("--objetivo", choices=sorted(OBJETIVOS), default="alcance")
    p.add_argument("--salida")
    a = p.parse_args()

    videos = [v for ruta in a.csv for v in leer_csv(ruta)]
    if not videos:
        sys.exit("No encontré videos con vistas en los archivos.")
    avisos = []
    for extra in (a.etiquetas, a.costos):
        if extra:
            faltan = unir_extra(videos, leer_tabla_extra(extra))
            if faltan:
                avisos.append(f"{faltan} video(s) sin fila en {Path(extra).name}")
    for v in videos:
        calcular(v)
    texto = informe(videos, a.objetivo)
    if avisos:
        texto += "\n\n" + "\n".join(f"> {x}" for x in avisos)
    if a.salida:
        Path(a.salida).write_text(texto + "\n", encoding="utf-8")
        print(f"Informe -> {a.salida}")
    else:
        print(texto)


if __name__ == "__main__":
    main()
