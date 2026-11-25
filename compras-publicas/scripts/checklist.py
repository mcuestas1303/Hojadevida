"""Convierte la respuesta de la extensión (prompt 02 partes A, B y C, y los prompt 03) en una lista de verificación en Excel.

Uso:
  python3 compras-publicas/scripts/checklist.py compras-publicas/procesos/<CÓDIGO>/respuesta.md [--salida archivo.xlsx]

Qué hace:
- Lee los bloques "=== TABLA: nombre ===". Tolera variaciones de formato: mayúsculas, negritas, encabezados markdown,
  sin bloque ```csv, punto y coma o tabulador como separador, tablas markdown con |, encabezados sin tildes,
  "N°" en vez de "No.", y archivos guardados en cp1252.
- Si una tabla aparece varias veces (partes A/B/C o prompt 03), JUNTA las versiones: las filas nuevas se agregan
  y las que tienen la misma clave (ítem y atributo, documento, hito, tema...) se reemplazan por la versión posterior.
- Alerta: tablas que faltan, partes cortadas (sin "=== FIN PARTE X ==="), datos clave en N/D, documentos no leídos
  completos, ítems sin especificaciones, tallas que no suman la cantidad, muestras, dudas y temas de
  catalogo/temas.csv que la extensión no confirmó.
- Si el Excel ya existe, conserva lo que el usuario escribió en las columnas de trabajo (Estado, Responsable,
  Costo, Precio, ¿Cumplimos?, etc.).
- Imprime un resumen en JSON. Sale con código 2 (sin escribir el Excel) si la respuesta no tiene ninguna tabla.
"""
import argparse
import csv
import datetime
import io
import json
import os
import re
import sys
import unicodedata
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

AQUI = os.path.dirname(os.path.abspath(__file__))
TEMAS_CSV = os.path.join(AQUI, "..", "catalogo", "temas.csv")

ESPERADAS = {
    "anexos": ["No.", "Nombre del archivo o documento", "Tipo", "Fecha", "¿Leído completo? (Sí/No/Parcial)", "Páginas", "Enlace"],
    "ficha": ["Campo", "Valor", "Fuente"],
    "fechas": ["Hito", "Fecha (DD/MM/AAAA)", "Hora", "Medio o lugar", "Fuente"],
    "garantias": ["Tipo", "Porcentaje o monto", "Vigencia", "Emisor aceptado", "Momento de entrega", "Fuente"],
    "evaluacion": ["Criterio", "Tipo (Cumple-no cumple / Puntaje / Precio)", "Puntaje máximo o regla", "Mínimo para pasar", "Fuente"],
    "condiciones": ["Tema", "Detalle", "Fuente", "Texto literal"],
    "documentos": ["No.", "Documento requerido", "Categoría", "Aplica a", "Formato exigido", "Vigencia máxima", "¿Firma y sello?",
                   "¿Subsanable?", "¿Causa descalificación?", "Momento", "Formulario o anexo modelo", "Fuente", "Texto literal"],
    "presentacion": ["No.", "Requisito de presentación", "Detalle exigido", "Fuente", "Texto literal"],
    "cotizacion": ["Tema", "Detalle exigido", "Fuente", "Texto literal"],
    "items": ["Ítem/Lote", "Descripción", "Cantidad", "Unidad", "Precio de referencia US$", "¿Precio con IVA?", "¿Se adjudica por ítem?",
              "¿Se puede ofertar cantidad parcial?", "¿Muestra?", "Fuente"],
    "distribucion": ["Ítem/Lote", "Talla", "Color", "Cantidad", "Lugar o dependencia", "Fuente"],
    "especificaciones": ["Ítem/Lote", "Atributo", "Valor exigido", "Obligatorio o deseable", "¿Admite equivalente?", "Fuente", "Texto literal"],
    "entregas": ["Entrega No.", "Ítem/Lote", "Cantidad", "Plazo o fecha", "Desde cuándo corre el plazo", "Lugar", "Contacto", "Fuente"],
    "muestras": ["Ítem/Lote", "Cantidad y talla", "¿Con logo?", "Rotulación", "Fecha, hora y lugar de entrega",
                 "¿Se devuelve? (y plazo para retirarla)", "¿Se destruye en pruebas?", "Fuente"],
    "temas": ["Tema", "¿Las bases lo mencionan? (Sí/No)", "Tabla donde quedó", "Fuente"],
    "cobertura": ["Documento", "Sección o numeral", "¿Leída? (Sí/No/Parcial)", "Motivo si no"],
    "dudas": ["No.", "Tipo (Contradicción / Dato faltante / Ambigüedad)", "Descripción", "Pregunta sugerida para el período de consultas", "Fuente"],
}
PARTE = {"anexos": "A", "ficha": "A", "fechas": "A", "garantias": "A", "evaluacion": "A", "condiciones": "A", "cobertura": "A",
         "documentos": "B", "presentacion": "B", "cotizacion": "B",
         "items": "C", "distribucion": "C", "especificaciones": "C", "entregas": "C", "muestras": "C"}
# nombre de tabla -> canónico (se compara por prefijo del nombre normalizado; el orden importa)
ALIAS_TABLA = [("documentosdelproceso", "anexos"), ("anexo", "anexos"), ("inventario", "anexos"), ("ficha", "ficha"),
               ("fecha", "fechas"), ("cronograma", "fechas"), ("plazo", "fechas"), ("garantia", "garantias"),
               ("evalua", "evaluacion"), ("condicion", "condiciones"), ("documento", "documentos"), ("requisitosdedoc", "documentos"),
               ("presenta", "presentacion"), ("cotiza", "cotizacion"), ("precio", "cotizacion"), ("item", "items"),
               ("producto", "items"), ("distribu", "distribucion"), ("talla", "distribucion"), ("especific", "especificaciones"),
               ("entrega", "entregas"), ("muestra", "muestras"), ("tema", "temas"), ("cobertura", "cobertura"),
               ("duda", "dudas"), ("consulta", "dudas"), ("pregunta", "dudas")]
FICHA = {  # campo canónico -> patrón sobre la clave normalizada
    "Código": r"^CODIGO", "Nombre del proceso": r"^NOMBRE", "Institución": r"^INSTITUCION", "Modalidad": r"^MODALIDAD",
    "Monto estimado US$": r"^MONTO(?!.*IVA)", "¿Monto con IVA?": r"MONTO.*IVA", "Estado": r"^ESTADO",
    "Fecha de publicación": r"PUBLICACION",
    "Fecha y hora límite de consultas": r"(CONSULTA|ACLARACION)",
    "Fecha y hora límite de ofertas": r"(LIMITE|CIERRE|RECEPCION|PRESENTACION)\w*OFERTA",
    "Fecha y hora de apertura": r"APERTURA",
    "Medio de presentación (COMPRASAL electrónica / física / ambas)": r"^MEDIO",
    "Dirección de entrega física": r"DIRECCION", "Administrador del contrato o contacto": r"(ADMINISTRADOR|CONTACTO)",
    "Plazo de entrega": r"^PLAZO", "Lugar de entrega": r"^LUGAR", "Forma de pago": r"PAGO", "Vigencia de la oferta": r"VIGENCIA",
    "¿Adjudicación parcial por ítem?": r"PARCIAL", "Beneficio para MYPE o MIPYME": r"(MYPE|MIPYME|RESERVAD)", "Enlace": r"^ENLACE",
}
FICHA_CLAVE = ["Fecha y hora límite de ofertas", "Fecha y hora límite de consultas", "Medio de presentación (COMPRASAL electrónica / física / ambas)",
               "Plazo de entrega", "Lugar de entrega", "Forma de pago", "Vigencia de la oferta"]
COLS_USUARIO = {"2. Documentos": ["Estado", "Responsable", "Observación"],
                "3. Productos": ["Costo unitario US$", "Precio a ofertar US$", "Total US$", "¿Muestra lista?"],
                "4. Especificaciones": ["¿Cumplimos?", "Evidencia (ficha, muestra, foto)"],
                "5. Presentación y cotización": ["Estado"],
                "9. Dudas y consultas": ["¿Enviada?", "Respuesta"]}
MESES = {"ENERO": 1, "FEBRERO": 2, "MARZO": 3, "ABRIL": 4, "MAYO": 5, "JUNIO": 6, "JULIO": 7, "AGOSTO": 8,
         "SEPTIEMBRE": 9, "SETIEMBRE": 9, "OCTUBRE": 10, "NOVIEMBRE": 11, "DICIEMBRE": 12}


# ------------------------------------------------------------------ utilidades
def sin_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFD", str(s).upper()) if unicodedata.category(c) != "Mn")


def clave(s):
    """Clave para comparar encabezados y nombres: sin tildes, sin paréntesis, solo letras y números."""
    s = sin_tildes(s)
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"\b(N[O°º]|NUM|NUMERO|NRO)\b\.?", "NO", s)
    s = s.replace("Nº", "NO").replace("N°", "NO")
    return re.sub(r"[^A-Z0-9]", "", s)


def es_nd(v):
    s = sin_tildes(v).strip().rstrip(".")
    return s in {"", "-", "—", "ND", "N/D", "N.D", "N/A", "NA", "NO APLICA"} or bool(
        re.match(r"^(N/D|N/A|NO APARECE|NO SE ESPECIFICA|NO ESPECIFICA|NO SE INDICA|NO INDICA|NO DICE|SIN DATO|NO DISPONIBLE|NO SE MENCIONA|NO MENCIONA)", s))


def es_si(v):
    return sin_tildes(v).strip().startswith("SI")


def num_item(v):
    d = re.findall(r"\d+", str(v))
    return d[0].lstrip("0") or "0" if d else clave(v)


def a_numero(v):
    s = str(v).replace("$", "").replace("US", "").strip()
    if re.fullmatch(r"\d{1,3}(,\d{3})+(\.\d+)?", s):
        s = s.replace(",", "")
    elif re.fullmatch(r"\d+,\d+", s):
        s = s.replace(",", ".")
    try:
        x = float(s)
        return int(x) if x.is_integer() else x
    except ValueError:
        return None


def fecha(v):
    s = sin_tildes(v).strip()
    m = re.search(r"(\d{1,2})\s*DE\s*([A-Z]+)\s*(DE|DEL)?\s*(\d{4})", s)
    if m and m.group(2) in MESES:
        try:
            return datetime.date(int(m.group(4)), MESES[m.group(2)], int(m.group(1)))
        except ValueError:
            return None
    m = re.search(r"(\d{4})[/\-.](\d{1,2})[/\-.](\d{1,2})", s)
    if m:
        try:
            return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return None
    m = re.search(r"(\d{1,2})[/\-.](\d{1,2})[/\-.](\d{2,4})", s)
    if m:
        a = int(m.group(3))
        a = a + 2000 if a < 100 else a
        try:
            return datetime.date(a, int(m.group(2)), int(m.group(1)))
        except ValueError:
            return None
    return None


def plural(n, uno, varios):
    return f"{n} {uno if n == 1 else varios}"


# ------------------------------------------------------------------ lectura
MARCA = re.compile(r"^[\s>#*_]*=*\s*TABLA\s*:\s*(.+?)\s*=*[\s*_]*$", re.I | re.M)
FIN = re.compile(r"^[\s>#*_]*=*\s*FIN\s+(PARTE\s+([ABC])|REPREGUNTA)", re.I | re.M)


def nombre_tabla(n):
    k = clave(n).lower()
    for pref, canon in ALIAS_TABLA:
        if k.startswith(pref):
            return canon
    return None


def parsear_bloque(cuerpo):
    m = re.search(r"```[A-Za-z]*\s*\n(.*?)```", cuerpo, flags=re.S)
    if m:
        txt = m.group(1)
    else:
        lineas = cuerpo.splitlines()
        ini = next((i for i, l in enumerate(lineas) if l.strip().startswith(('"', "|"))), None)
        if ini is None:
            return []
        txt = "\n".join(lineas[ini:])
    txt = txt.strip()
    if not txt:
        return []
    primera = txt.splitlines()[0]
    if primera.strip().startswith("|"):
        filas = []
        for l in txt.splitlines():
            l = l.strip()
            if not l.startswith("|") or re.fullmatch(r"\|[\s:\-|]+\|?", l):
                continue
            filas.append([c.strip().strip('"') for c in l.strip("|").split("|")])
        return filas
    sep = max([",", ";", "\t"], key=lambda s: primera.count('"' + s + '"') * 10 + primera.count(s))
    filas = [f for f in csv.reader(io.StringIO(txt), delimiter=sep) if len(f) >= 2 and any(x.strip() for x in f)]
    return filas


def mapear_encabezados(tabla, enc):
    canon = {clave(c): c for c in ESPERADAS.get(tabla, [])}
    out = []
    for h in enc:
        k = clave(h)
        c = canon.get(k) or next((v for kk, v in canon.items() if len(k) >= 5 and len(kk) >= 5 and (kk.startswith(k) or k.startswith(kk))), None)
        out.append(c or h.strip())
    return out


def clave_fila(tabla, r):
    g = lambda c: clave(r.get(c, ""))
    if tabla == "ficha":
        return campo_ficha(r.get("Campo", ""))
    if tabla in ("items", "muestras"):
        return num_item(r.get("Ítem/Lote", ""))
    if tabla == "especificaciones":
        return (num_item(r.get("Ítem/Lote", "")), g("Atributo"))
    if tabla == "distribucion":
        return (num_item(r.get("Ítem/Lote", "")), g("Talla"), g("Color"), g("Lugar o dependencia"))
    if tabla == "entregas":
        return (g("Entrega No."), num_item(r.get("Ítem/Lote", "")))
    if tabla == "documentos":
        return g("Documento requerido")
    if tabla == "fechas":
        return g("Hito")
    if tabla == "temas":
        return g("Tema")
    if tabla == "anexos":
        return g("Nombre del archivo o documento")
    if tabla in ("condiciones", "cotizacion"):
        return (g("Tema"), clave(r.get("Detalle", r.get("Detalle exigido", "")))[:40])
    if tabla == "cobertura":
        return (g("Documento"), g("Sección o numeral"))
    return tuple(clave(v) for v in r.values())


def campo_ficha(c):
    k = clave(c)
    for canon, pat in FICHA.items():
        if re.search(pat, k):
            if canon == "Fecha y hora límite de ofertas" and "CONSULTA" in k:
                continue
            return canon
    return c.strip()


def leer_respuesta(ruta):
    for enc in ("utf-8-sig", "cp1252"):
        try:
            texto = open(ruta, encoding=enc).read()
            break
        except UnicodeDecodeError:
            continue
    texto = texto.replace("\r\n", "\n")
    marcas = list(MARCA.finditer(texto))
    tablas, versiones, desconocidas, partes_ini, cambios = {}, {}, [], set(), []
    fines = {m.group(2).upper() if m.group(2) else "R": m.start() for m in FIN.finditer(texto)}
    for i, m in enumerate(marcas):
        fin = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
        f2 = FIN.search(texto, m.end(), fin)
        cuerpo = texto[m.end(): f2.start() if f2 else fin]
        t = nombre_tabla(m.group(1))
        if not t:
            desconocidas.append(m.group(1).strip())
            continue
        filas = parsear_bloque(cuerpo)
        if not filas:
            versiones.setdefault(t, 0)
            tablas.setdefault(t, {})
            continue
        enc = mapear_encabezados(t, filas[0])
        nuevas = [dict(zip(enc, [x.strip() for x in f] + [""] * (len(enc) - len(f)))) for f in filas[1:]]
        if t == "ficha":
            for r in nuevas:
                r["Campo"] = campo_ficha(r.get("Campo", ""))
        actual = tablas.setdefault(t, {})
        agregadas = corregidas = 0
        for r in nuevas:
            k = clave_fila(t, r)
            if k in actual:
                if actual[k] != r:
                    corregidas += 1
                actual[k] = r
            else:
                actual[k] = r
                agregadas += 1
        versiones[t] = versiones.get(t, 0) + 1
        if versiones[t] > 1 and t != "temas" and t != "dudas" and (agregadas or corregidas):
            cambios.append(f"Tabla '{t}': una versión posterior agregó {plural(agregadas, 'fila', 'filas')} y corrigió {plural(corregidas, 'fila', 'filas')}.")
        tablas.setdefault(t + "__enc", enc)
        if t in PARTE:
            partes_ini.add(PARTE[t])
    T = {k: (list(v.values()) if isinstance(v, dict) else v) for k, v in tablas.items()}
    return T, desconocidas, partes_ini, set(fines), cambios


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("respuesta")
    ap.add_argument("--salida")
    a = ap.parse_args()
    T, desconocidas, partes_ini, fines, cambios = leer_respuesta(a.respuesta)
    encontradas = [t for t in ESPERADAS if t in T]
    if not encontradas:
        print("La respuesta no tiene ninguna tabla reconocible ('=== TABLA: nombre ==='). "
              "¿La extensión se detuvo antes de responder o cambió el formato? No se escribió el Excel.", file=sys.stderr)
        sys.exit(2)
    carpeta = os.path.dirname(os.path.abspath(a.respuesta))
    ficha = {r.get("Campo", ""): r.get("Valor", "") for r in T.get("ficha", [])}
    codigo = ficha.get("Código") if not es_nd(ficha.get("Código", "")) else os.path.basename(carpeta)
    codigo = re.sub(r"[^\w\-]", "_", codigo)
    salida = a.salida or os.path.join(carpeta, f"checklist_{codigo}.xlsx")

    alertas = []

    def alerta(n, t):
        alertas.append((n, t))

    for p in sorted(partes_ini - fines):
        alerta("ALTA", f"La Parte {p} no termina con '=== FIN PARTE {p} ===': la respuesta puede estar cortada. Revisar o repetir esa parte.")
    for p in sorted({"A", "B", "C"} - partes_ini):
        alerta("ALTA", f"No hay tablas de la Parte {p} del prompt 02: falta correr esa parte.")
    for t in ESPERADAS:
        if t not in T and PARTE.get(t) in partes_ini:
            alerta("ALTA", f"Falta la tabla '{t}'.")
        elif t in T:
            falt = [h for h in ESPERADAS[t] if h not in T[t + "__enc"]]
            if falt:
                alerta("MEDIA", f"Tabla '{t}': faltan las columnas {', '.join(falt)}.")
    for d in desconocidas:
        alerta("MEDIA", f"Tabla no reconocida y no usada: '{d}'. Revisar si trae información.")
    for c in cambios:
        alerta("INFO", c)

    for campo in FICHA_CLAVE:
        if es_nd(ficha.get(campo, "")):
            alerta("ALTA", f"Ficha: '{campo.split(' (')[0]}' está vacío o N/D.")

    hoy = datetime.date.today()
    limite = fecha(ficha.get("Fecha y hora límite de ofertas", ""))
    for r in T.get("fechas", []):
        h = sin_tildes(r.get("Hito", ""))
        if "OFERTA" in h and "APERTURA" not in h and re.search(r"LIMITE|CIERRE|RECEPCION|PRESENTACION", h):
            limite = fecha(r.get("Fecha (DD/MM/AAAA)", "")) or limite
    if limite is None:
        alerta("ALTA", "No se pudo leer la fecha límite de ofertas (falta o tiene un formato raro). Confirmarla en COMPRASAL.")

    for r in T.get("documentos", []):
        if es_nd(r.get("Fuente", "")):
            alerta("MEDIA", f"Documento sin fuente: {r.get('Documento requerido', '')}")
    items = sorted(T.get("items", []), key=lambda r: (len(num_item(r.get("Ítem/Lote", ""))), num_item(r.get("Ítem/Lote", ""))))
    specs = T.get("especificaciones", [])
    con_spec = {num_item(r.get("Ítem/Lote", "")) for r in specs}
    for r in specs:
        if es_nd(r.get("Valor exigido", "")):
            alerta("MEDIA", f"Especificación sin valor: ítem {r.get('Ítem/Lote', '')} · {r.get('Atributo', '')}")
    dist = {}
    for r in T.get("distribucion", []):
        q = a_numero(r.get("Cantidad", ""))
        if q is not None:
            dist[num_item(r.get("Ítem/Lote", ""))] = dist.get(num_item(r.get("Ítem/Lote", "")), 0) + q
    for r in items:
        it = num_item(r.get("Ítem/Lote", ""))
        q = a_numero(r.get("Cantidad", ""))
        r = dict(r, **{"Ítem/Lote": it})
        if q is None:
            alerta("ALTA", f"Ítem {r.get('Ítem/Lote', '')} sin cantidad clara: '{r.get('Cantidad', '')}'.")
        elif it in dist and abs(dist[it] - q) > 0.01:
            alerta("ALTA", f"Ítem {r.get('Ítem/Lote', '')}: la distribución por tallas suma {dist[it]:g} y la cantidad es {q:g}.")
        if "items" in T and "especificaciones" in T and it not in con_spec:
            alerta("ALTA", f"Ítem {r.get('Ítem/Lote', '')} no tiene ninguna especificación.")
        if es_si(r.get("¿Muestra?", "")):
            alerta("RECORDATORIO", f"Ítem {r.get('Ítem/Lote', '')} pide MUESTRA: revisar cantidad, fecha y lugar en la hoja Productos.")
    logo = [r for r in specs if "LOGO" in sin_tildes(r.get("Atributo", "")) and "TECNICA" in sin_tildes(r.get("Atributo", ""))]
    for r in logo:
        v = sin_tildes(r.get("Valor exigido", ""))
        if v and not es_nd(v) and not re.search(r"DTF|TRANSFER|CUALQUIER|LIBRE|ESTAMPAD|IMPRES", v):
            alerta("RECORDATORIO", f"Ítem {r.get('Ítem/Lote', '')}: la técnica de logo exigida es '{r.get('Valor exigido', '')}' (no menciona DTF).")
    for r in T.get("anexos", []):
        if not es_si(r.get("¿Leído completo? (Sí/No/Parcial)", "")):
            alerta("ALTA", f"Documento del proceso que no se leyó completo: {r.get('Nombre del archivo o documento', '')}")
    for r in T.get("cobertura", []):
        if not es_si(r.get("¿Leída? (Sí/No/Parcial)", "")):
            alerta("ALTA", f"Sección que no se leyó: {r.get('Documento', '')} · {r.get('Sección o numeral', '')} ({r.get('Motivo si no', '')})")
    n_dudas = len(T.get("dudas", []))
    if n_dudas:
        alerta("MEDIA", f"Hay {plural(n_dudas, 'duda', 'dudas')}: " + ("enviarla" if n_dudas == 1 else "enviarlas") + " como consulta antes de la fecha límite de consultas.")

    temas_resp = {clave(r.get("Tema", "")): r for r in T.get("temas", [])}
    no_conf = []
    with open(TEMAS_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["Parte"] not in partes_ini:
                continue
            k = clave(row["Tema"])
            r = temas_resp.get(k) or next((v for kk, v in temas_resp.items() if kk[:12] == k[:12]), None)
            if r is None or es_nd(r.get("¿Las bases lo mencionan? (Sí/No)", "")):
                no_conf.append(row["Tema"])
            elif es_si(r.get("¿Las bases lo mencionan? (Sí/No)", "")) and es_nd(r.get("Tabla donde quedó", "")):
                alerta("MEDIA", f"Tema '{row['Tema']}': las bases lo mencionan pero no dice en qué tabla quedó.")
    for t in no_conf:
        alerta("VERIFICAR", f"La extensión no confirmó si las bases hablan de: {t}.")

    # ------------------------------------------------------------ conservar trabajo del usuario
    previo = {}
    if os.path.exists(salida):
        try:
            wb0 = load_workbook(salida)
            for hoja_n, cols in COLS_USUARIO.items():
                if hoja_n not in wb0.sheetnames:
                    continue
                w0 = wb0[hoja_n]
                enc0 = [c.value for c in w0[1]]
                for row in w0.iter_rows(min_row=2, values_only=True):
                    if not row or row[0] is None:
                        continue
                    d = dict(zip(enc0, row))
                    k = (hoja_n, str(row[0]), str(row[1]))
                    v = {c: d.get(c) for c in cols if d.get(c) not in (None, "") and not str(d.get(c)).startswith("=")}
                    if v:
                        previo[k] = v
        except Exception as e:  # el archivo puede estar abierto o dañado
            alerta("MEDIA", f"No se pudo leer el Excel anterior para conservar tus notas ({e}). Se guardó una versión nueva.")
            salida = salida.replace(".xlsx", f"_{hoy:%Y%m%d}.xlsx")

    # ------------------------------------------------------------ Excel
    AZUL = PatternFill("solid", fgColor="1F4E78")
    fino = Side(style="thin", color="BFBFBF")
    BORDE = Border(left=fino, right=fino, top=fino, bottom=fino)
    WRAP = Alignment(wrap_text=True, vertical="top")
    NIVEL = {"ALTA": "F8CBAD", "MEDIA": "FFEB9C", "VERIFICAR": "DDEBF7", "RECORDATORIO": "E2EFDA", "INFO": "EDEDED"}
    wb = Workbook()

    def poner(c, v):
        c.value = v
        if isinstance(v, str) and v[:1] in ("=", "+", "@"):
            c.data_type = "s"

    def hoja(nombre, cols, filas, extra=(), anchos=None, lista=None, numericas=()):
        ws = wb.create_sheet(nombre)
        enc = list(cols) + list(extra)
        for j, h in enumerate(enc, 1):
            c = ws.cell(1, j, h)
            c.font, c.fill, c.border = Font(bold=True, color="FFFFFF"), AZUL, BORDE
            c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
            ws.column_dimensions[get_column_letter(j)].width = (anchos or {}).get(h, 14 if h in extra else 22)
        for i, r in enumerate(filas, 2):
            for j, h in enumerate(cols, 1):
                v = r.get(h, "")
                if h in numericas and a_numero(v) is not None:
                    v = a_numero(v)
                c = ws.cell(i, j)
                poner(c, v)
                c.alignment, c.border = WRAP, BORDE
                if isinstance(v, str) and es_nd(v) and h not in ("Formulario o anexo modelo", "Motivo si no"):
                    c.fill = PatternFill("solid", fgColor="FCE4D6")
            k = (nombre, str(r.get(cols[0], "")), str(r.get(cols[1], "")))
            for j, h in enumerate(extra, len(cols) + 1):
                c = ws.cell(i, j)
                c.border = BORDE
                if h in previo.get(k, {}):
                    poner(c, previo[k][h])
        if lista and filas:
            dv = DataValidation(type="list", formula1=f'"{lista}"', allow_blank=True)
            ws.add_data_validation(dv)
            col = get_column_letter(len(cols) + 1)
            dv.add(f"{col}2:{col}{len(filas) + 1}")
        ws.freeze_panes = "B2"
        if filas:
            ws.auto_filter.ref = f"A1:{get_column_letter(len(enc))}{len(filas) + 1}"
        return ws

    def anexar(ws, titulo, cols, filas):
        base = ws.max_row + 2
        ws.cell(base, 1, titulo).font = Font(bold=True, size=12, color="1F4E78")
        for j, h in enumerate(cols, 1):
            c = ws.cell(base + 1, j, h)
            c.font, c.fill, c.border = Font(bold=True, color="FFFFFF"), AZUL, BORDE
            c.alignment = Alignment(wrap_text=True, horizontal="center")
        for i, r in enumerate(filas, base + 2):
            for j, h in enumerate(cols, 1):
                c = ws.cell(i, j)
                poner(c, r.get(h, ""))
                c.alignment, c.border = WRAP, BORDE

    ws = wb.active
    ws.title = "1. Resumen"
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 34
    ws.column_dimensions["B"].width = 95
    ws["A1"] = f"Lista de verificación de oferta · {codigo}"
    ws["A1"].font = Font(bold=True, size=15, color="1F4E78")
    ws["A2"] = ficha.get("Nombre del proceso", "")
    ws["A3"] = ficha.get("Institución", "")
    ws["A2"].font = ws["A3"].font = Font(italic=True, color="595959")
    r = 5
    ws.cell(r, 1, "Fecha límite de ofertas").font = Font(bold=True)
    if limite:
        dias = (limite - hoy).days
        txt = "YA VENCIÓ" if dias < 0 else "vence HOY" if dias == 0 else ("queda 1 día" if dias == 1 else f"quedan {dias} días")
        c = ws.cell(r, 2, f"{limite:%d/%m/%Y} · {txt}")
        c.font = Font(bold=True, color="C00000" if dias < 5 else "000000")
    else:
        ws.cell(r, 2, "NO SE PUDO LEER · confirmar en COMPRASAL").font = Font(bold=True, color="C00000")
    r += 1
    for k in ["Fecha y hora límite de consultas", "Modalidad", "Monto estimado US$", "¿Monto con IVA?",
              "Medio de presentación (COMPRASAL electrónica / física / ambas)", "Plazo de entrega", "Lugar de entrega", "Forma de pago",
              "Vigencia de la oferta", "¿Adjudicación parcial por ítem?", "Beneficio para MYPE o MIPYME", "Enlace"]:
        ws.cell(r, 1, k.split(" (")[0]).font = Font(bold=True)
        poner(ws.cell(r, 2), ficha.get(k, "N/D") or "N/D")
        ws.cell(r, 2).alignment = WRAP
        r += 1
    r += 1
    resumen = [("Documentos a presentar", len(T.get("documentos", []))), ("Ítems", len(items)),
               ("Especificaciones", len(specs)), ("Requisitos de presentación", len(T.get("presentacion", []))),
               ("Entregas", len(T.get("entregas", []))), ("Muestras", len(T.get("muestras", []))), ("Dudas para consultar", n_dudas)]
    for k, v in resumen:
        ws.cell(r, 1, k).font = Font(bold=True)
        ws.cell(r, 2, v).alignment = Alignment(horizontal="left")
        r += 1
    r += 1
    ws.cell(r, 1, f"ALERTAS ({len(alertas)})").font = Font(bold=True, size=12, color="C00000")
    r += 1
    for nivel, t in sorted(alertas, key=lambda x: list(NIVEL).index(x[0])):
        ws.cell(r, 1, nivel).fill = PatternFill("solid", fgColor=NIVEL[nivel])
        ws.cell(r, 1).font = Font(bold=True)
        ws.cell(r, 2, t).alignment = WRAP
        r += 1
    r += 1
    ws.cell(r, 1, "Cómo usar esta lista").font = Font(bold=True)
    for t in ["Marca el estado en las columnas de la derecha de las hojas 2, 3, 4, 5 y 9. Si vuelves a generar el archivo, lo que escribiste se conserva.",
              "Las celdas en naranja son datos N/D: confírmalos en las bases o pregúntalos en el período de consultas.",
              "VERIFICAR = la extensión no confirmó si las bases hablan de ese tema; no significa que el requisito exista."]:
        r += 1
        ws.cell(r, 2, t).alignment = WRAP

    hoja("2. Documentos", ESPERADAS["documentos"], T.get("documentos", []), extra=COLS_USUARIO["2. Documentos"],
         anchos={"Documento requerido": 40, "Texto literal": 50, "Formato exigido": 28}, lista="Pendiente,En trámite,Listo,No aplica")
    w3 = hoja("3. Productos", ESPERADAS["items"], items, extra=COLS_USUARIO["3. Productos"],
              anchos={"Descripción": 45}, numericas=("Cantidad", "Precio de referencia US$"))
    ic, ip, it_ = (ESPERADAS["items"].index("Cantidad") + 1, len(ESPERADAS["items"]) + 2, len(ESPERADAS["items"]) + 3)
    for i in range(2, len(items) + 2):
        if w3.cell(i, it_).value in (None, ""):
            w3.cell(i, it_).value = f"=IF({get_column_letter(ip)}{i}=\"\",\"\",{get_column_letter(ic)}{i}*{get_column_letter(ip)}{i})"
    anexar(w3, "Distribución por tallas y colores", ESPERADAS["distribucion"], T.get("distribucion", []))
    anexar(w3, "Entregas", ESPERADAS["entregas"], T.get("entregas", []))
    anexar(w3, "Muestras", ESPERADAS["muestras"], T.get("muestras", []))
    hoja("4. Especificaciones", ESPERADAS["especificaciones"],
         sorted(specs, key=lambda x: (len(num_item(x.get("Ítem/Lote", ""))), num_item(x.get("Ítem/Lote", "")))),
         extra=COLS_USUARIO["4. Especificaciones"], anchos={"Valor exigido": 40, "Texto literal": 50}, lista="Sí,No,Duda")
    w5 = hoja("5. Presentación y cotización", ESPERADAS["presentacion"], T.get("presentacion", []), extra=COLS_USUARIO["5. Presentación y cotización"],
              anchos={"Requisito de presentación": 34, "Detalle exigido": 50, "Texto literal": 50}, lista="Pendiente,Listo")
    anexar(w5, "Cómo cotizar", ESPERADAS["cotizacion"], T.get("cotizacion", []))
    hoja("6. Fechas", ESPERADAS["fechas"], sorted(T.get("fechas", []), key=lambda x: fecha(x.get("Fecha (DD/MM/AAAA)", "")) or datetime.date.max),
         anchos={"Hito": 40})
    w7 = hoja("7. Garantías y condiciones", ESPERADAS["garantias"], T.get("garantias", []), anchos={"Tipo": 34})
    anexar(w7, "Condiciones del contrato", ESPERADAS["condiciones"], T.get("condiciones", []))
    hoja("8. Evaluación", ESPERADAS["evaluacion"], T.get("evaluacion", []), anchos={"Criterio": 40, "Puntaje máximo o regla": 40})
    hoja("9. Dudas y consultas", ESPERADAS["dudas"], T.get("dudas", []), extra=COLS_USUARIO["9. Dudas y consultas"],
         anchos={"Descripción": 45, "Pregunta sugerida para el período de consultas": 50}, lista="No,Sí")
    w10 = hoja("10. Documentos y cobertura", ESPERADAS["anexos"], T.get("anexos", []), anchos={"Nombre del archivo o documento": 45, "Enlace": 40})
    anexar(w10, "Cobertura de lectura", ESPERADAS["cobertura"], T.get("cobertura", []))
    anexar(w10, "Temas revisados", ESPERADAS["temas"], T.get("temas", []))
    for w in wb.worksheets:
        w.page_setup.orientation = "landscape"
        w.page_setup.fitToWidth, w.page_setup.fitToHeight = 1, 0
        w.sheet_properties.pageSetUpPr.fitToPage = True
    wb.save(salida)
    print(json.dumps({"salida": salida, "codigo": codigo, "fecha_limite": str(limite) if limite else None,
                      "partes": sorted(partes_ini), "partes_completas": sorted(partes_ini & fines),
                      "tablas_encontradas": encontradas, "tablas_desconocidas": desconocidas,
                      "notas_conservadas": len(previo), "conteos": dict(resumen),
                      "alertas": [{"nivel": n, "texto": t} for n, t in alertas]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
