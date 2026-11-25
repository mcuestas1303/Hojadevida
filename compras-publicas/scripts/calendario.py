"""Calendario de decisiones de compras públicas (COMPRASAL) a partir de los CSV de la extensión de Chrome.

Uso:
  python3 compras-publicas/scripts/calendario.py --datos compras-publicas/datos/uniformes \
      --perfil uniformes --producto "Uniformes y prendas" --anio 2027 --salida calendario_uniformes_2027.xlsx
"""
import argparse
import sys
from collections import Counter
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import datos as D
from datos import sin_tildes

ap = argparse.ArgumentParser()
ap.add_argument("--datos", required=True, help="carpeta con los .csv del prompt 01")
ap.add_argument("--perfil", default="uniformes", choices=sorted(D.PERFILES))
ap.add_argument("--producto", default="Uniformes y prendas")
ap.add_argument("--anio", type=int, default=2027)
ap.add_argument("--salida", required=True)
args = ap.parse_args()
out = args.salida
todo, n_en_dos, mapa_muni, evid_muni, PESO = D.cargar(args.datos, args.perfil)
A0, A1, A2 = args.anio - 3, args.anio - 2, args.anio - 1   # años de datos (p. ej. 2024, 2025 y 2026)
import datetime
HOY = datetime.date.today()
HOY_TXT = ["", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"][HOY.month] + f"-{HOY.year}"
K_COMPRAS, K_C1, K_C2 = f"Compras {A1} / {A2}", f"Compró en {A1}", f"Compró en {A2}"
K_M2, K_TOT = f"Monto {A2}", f"Monto total {A0}–{A2} US$"
inc = todo[todo["Categoría"].notna()].copy()

MES = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
MES3 = ["", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
TRIM = {1: "ene–mar", 2: "abr–jun", 3: "jul–sep", 4: "oct–dic"}
DESDE = {1: "diciembre", 2: "marzo", 3: "junio", 4: "septiembre"}
ABIERTAS = {"Comparación de precios", "Subasta Inversa"}
VERIF = {"Convenios", "Subasta en plataformas privadas"}
DEC_ORD = {"OFERTAR": 0, "PREPARAR": 1, "SOLO POR LOTES": 2, "VERIFICAR": 3, "NO APLICA": 4, "HISTÓRICO": 5}


def decision(monto, mod):
    if mod == "Contratación directa": return "NO APLICA"
    if mod in VERIF: return "VERIFICAR"
    if monto <= 50000 and mod in ABIERTAS: return "OFERTAR"
    if monto <= 150000: return "PREPARAR"
    return "SOLO POR LOTES"


def dinero(m):
    if m < 10000: return f"${round(m / 500) * 500:,.0f}"
    if m < 100000: return f"${round(m / 1000):,.0f} mil"
    if m < 1e6: return f"${round(m / 10000) * 10:,.0f} mil"
    return f"${m / 1e6:,.1f} M"


def repite(anios):
    s = set(anios)
    if {A0, A1, A2} <= s: return f"Sí, {A0}–{A2}"
    if {A1, A2} <= s: return f"Sí, {A1} y {A2}"
    if s == {A0, A2}: return f"¿Cada 2 años? ({A0} y {A2})"
    if s == {A0, A1}: return f"{A0} y {A1} (no en {A2})"
    return f"Solo {min(s)}"


# ---------------------------------------------------------------- nombres de institución
MINUS = {"De", "Del", "Y", "Para", "En"}


def bonito(s):
    if not s.isupper():
        return s
    w = s.title().split()
    return " ".join(x.lower() if i and x in MINUS else x for i, x in enumerate(w))


nombre = inc.sort_values("Año").groupby("Inst")["Institución"].last().map(bonito)
for k in nombre.index:
    nprocs = " ".join(inc[inc["Inst"] == k]["Nombre del proceso"].map(sin_tildes))
    if (k.startswith("8614") or k.startswith("8652") or k == "10001429") and len(k) > 4 and "SAN SALVADOR" not in sin_tildes(nombre[k]):
        nombre[k] += " (Alcaldía San Salvador Centro)"
    if k in ("1000001", "1000002") and "MINEDUCYT" in nprocs:
        nombre[k] += " · proyectos MINEDUCYT"
    if D.es_muni_antiguo(k):
        nombre[k] += f" (antiguo municipio, {D.DEPTO[k[:2]]})"

# ---------------------------------------------------------------- concursos (una fila por compra real)
inc["Dec proc"] = [decision(m, mo) for m, mo in zip(inc["Monto"], inc["Modalidad"])]
agg = inc.groupby("Concurso").agg(
    Inst=("Inst", "first"), Año=("Año", "first"), Mes=("Mes", "first"), AñoMes=("AñoMes", "first"),
    Monto=("Monto", lambda s: s.sum()), Modalidad=("Modalidad", "first"), Categoría=("Categoría", lambda s: s.mode().iloc[0]),
    Nombre=("Nombre del proceso", "first"), Abierto=("Abierto", "any"), Otros=("Otros bienes", "any"),
    Códigos=("Código", lambda s: ", ".join(s)), Filas=("Código", "count"), Cuenta=("Cuenta como", lambda s: " / ".join(sorted(set(s)))),
    Antiguo=("Muni antiguo sin unir", "first"))
# repetidos y relanzamientos: el monto no se suma (se toma el mayor); las partidas agrupadas sí se suman
rep = inc[inc["Cuenta como"].isin(["Posible repetido", "Relanzamiento"])]["Concurso"].unique()
agg.loc[agg.index.isin(rep), "Monto"] = inc[inc["Concurso"].isin(rep)].groupby("Concurso")["Monto"].max()
agg["Dec"] = [decision(m, mo) for m, mo in zip(agg["Monto"], agg["Modalidad"])]
agg["Tamaño"] = agg["Monto"].map(lambda m: "pequeña" if m <= 50000 else "grande")
agg["Peso"] = agg["Categoría"].map(PESO)
agg["Trim"] = (agg["Mes"] - 1) // 3 + 1
C = agg.reset_index()
C2 = C[C["Año"].isin([A1, A2])]

# ---------------------------------------------------------------- líneas por institución y tamaño
lineas = []
for (inst, tam), g in C.groupby(["Inst", "Tamaño"]):
    anios = sorted(set(g["Año"]))
    ult = g[g["Año"] == anios[-1]]
    cnt = Counter(ult["Dec"])
    dec = sorted(cnt, key=lambda k: (-cnt[k], DEC_ORD[k]))[0]
    antiguo = bool(g["Antiguo"].iloc[0])
    if antiguo:
        dec = "HISTÓRICO"
    trim_anios = g.groupby("Trim")["Año"].apply(lambda s: set(s)).to_dict()
    trims = sorted(t for t, a in trim_anios.items() if len(a) >= 2) or sorted(set(ult["Trim"]))
    if len(trims) >= 3:
        t_max = g["Trim"].value_counts().idxmax()
        vigilar = f"Todo el año (más en {TRIM[t_max]})"
    else:
        vigilar = " · ".join(f"{TRIM[t]} (desde {DESDE[t]})" for t in trims)
    g2 = g[g["Año"].isin([A1, A2])]
    n25, n26 = int((g["Año"] == A1).sum()), int((g["Año"] == A2).sum())
    rango = g2[(g2["Monto"] >= 3000) & (g2["Monto"] <= 25000)]
    puntaje = float((rango["Peso"]).sum() + 0.5 * g2[~g2.index.isin(rango.index)]["Peso"].sum()) + (1 if n26 else 0)
    cats = Counter(g["Categoría"])
    peso_dom = PESO[cats.most_common(1)[0][0]]
    mods = Counter(ult["Modalidad"]).most_common()
    ej = g.sort_values(["Año", "Mes"]).iloc[-1]
    rec = {A1, A2} <= set(anios)

    if dec == "OFERTAR":
        paso = "Compra varias veces al año: revisar COMPRASAL cada mes." if len(trims) >= 3 else f"Vigilar COMPRASAL desde {DESDE[trims[0]]}."
    elif dec == "PREPARAR":
        paso = "Monto mediano: pedir bases y ver si el taller cubre todo o una parte."
    elif dec == "SOLO POR LOTES":
        paso = "Compra grande: ofertar solo si se divide en ítems o lotes pequeños."
    elif dec == "VERIFICAR":
        paso = ("Convenios: no es catálogo de inscripción; revisar bases (convenio de cooperación/préstamo o con otra institución)."
                if "Convenios" in ult["Modalidad"].values else
                "Plataformas privadas: probablemente Bolsa de Productos (BOLPROES) con puesto de bolsa; confirmar cómo participar.")
    elif dec == "NO APLICA":
        paso = "Contratación directa: no está abierta a ofertas."
    else:
        paso = f"Municipio suprimido en 2024: ahora es distrito de un municipio nuevo de {D.DEPTO[inst[:2]]}. Buscar al municipio nuevo."
    extras = []
    if g["Abierto"].any():
        extras.append("ABIERTO AHORA.")
    if (ult["AñoMes"] < ult["Año"]).any():
        extras.append(f"Planifica con un año de anticipación: la de {args.anio} puede salir a fines de {A2}.")
    if g["Otros"].any():
        extras.append("Incluye otros bienes: ofertar solo prendas si lo permiten.")
    if peso_dom == 0:
        extras.append("El nombre no dice qué prendas son o es vestuario artístico: revisar bases.")

    por_que = []
    if rec:
        por_que.append(f"{n25} compra(s) en {A1} y {n26} en {A2}")
    if len(rango):
        por_que.append(f"{len(rango)} de $3k–$25k")
    por_que.append(cats.most_common(1)[0][0].split(" (")[0].lower())

    lineas.append({
        "_inst": inst, "_tam": tam, "_ord": DEC_ORD[dec], "_rec": rec, "_n26": n26, "_trims": trims, "_puntaje": puntaje,
        "_peso": peso_dom, "_antiguo": antiguo, "_nanios": len(anios), "_abierto": bool(g["Abierto"].any()),
        "Decisión": dec, "Institución": nombre[inst],
        "Qué compra": " · ".join(c for c, _ in cats.most_common(2)),
        "Ejemplo (último)": ej["Nombre"][:110],
        "Último código": ej["Concurso"].split("+")[0],
        "Cuándo vigilar": vigilar,
        K_C1: ", ".join(MES3[m] for m in sorted(set(g[g["Año"] == A1]["Mes"]))) or "—",
        K_C2: ", ".join(MES3[m] for m in sorted(set(g[g["Año"] == A2]["Mes"]))) or "—",
        K_COMPRAS: f"{n25} / {n26}",
        "Monto típico": dinero(float(g["Monto"].median())),
        K_M2: dinero(float(g[g["Año"] == A2]["Monto"].sum())) if n26 else "—",
        "¿Se repite?": repite(anios),
        "Modalidad": " / ".join(m for m, _ in mods),
        "Por qué está aquí": " · ".join(por_que),
        "Siguiente paso": paso + ((" " + " ".join(extras)) if extras else ""),
        "Código institución": inst,
        "Compras (nº)": len(g),
        K_TOT: round(float(g["Monto"].sum()), 2),
        "Categorías": " · ".join(f"{c} ({n})" for c, n in cats.most_common()),
        "Unido desde": ", ".join(sorted(set(x for x in inc[inc["Inst"] == inst]["Unido desde"] if x))),
        "Códigos": ", ".join(g.sort_values(["Año", "Mes"])["Códigos"]),
    })
L = pd.DataFrame(lineas)
peq, gra = L[L["_tam"] == "pequeña"], L[L["_tam"] == "grande"]
cand = peq[(peq["Decisión"] == "OFERTAR") & peq["_rec"] & (peq["_peso"] > 0)]
top = cand.sort_values(["_puntaje", "_n26"], ascending=False).head(15).copy()
top["_t"] = top["_trims"].map(lambda t: 0 if len(t) >= 3 else t[0])
top = top.sort_values(["_t", "_puntaje"], ascending=[True, False], kind="stable").copy()

of2 = C2[C2["Dec"] == "OFERTAR"]
anual = of2.groupby("Año").agg(n=("Concurso", "count"), monto=("Monto", "sum"))
of2_util = of2[of2["Peso"] > 0]
temp = of2.groupby(["Año", "Mes"]).agg(n=("Concurso", "count"), monto=("Monto", "sum"), inst=("Inst", "nunique")).groupby("Mes").mean()
temp = temp.reindex(range(1, 13), fill_value=0)
abiertos = C[C["Abierto"]].sort_values(["Dec", "Monto"], key=lambda s: s.map(DEC_ORD) if s.name == "Dec" else s)
dic = cand[cand["_trims"].map(lambda t: 1 in t)].sort_values("_puntaje", ascending=False).head(12)

# ---------------------------------------------------------------- estilos
COLOR = {"OFERTAR": "C6EFCE", "PREPARAR": "FFEB9C", "SOLO POR LOTES": "FCE4D6", "VERIFICAR": "DDEBF7", "NO APLICA": "EDEDED", "HISTÓRICO": "EDEDED"}
TXT = {"OFERTAR": "006100", "PREPARAR": "7F6000", "SOLO POR LOTES": "833C0B", "VERIFICAR": "1F4E78", "NO APLICA": "595959", "HISTÓRICO": "808080"}
AZUL = PatternFill("solid", fgColor="1F4E78")
GRIS = PatternFill("solid", fgColor="F2F2F2")
VERDES = {1: "E2EFDA", 2: "A9D08E", 3: "548235"}
fino = Side(style="thin", color="BFBFBF")
BORDE = Border(left=fino, right=fino, top=fino, bottom=fino)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTRO = Alignment(horizontal="center", vertical="center", wrap_text=True)


def encabezado(ws, fila, cols, widths=None):
    for j, h in enumerate(cols, 1):
        c = ws.cell(fila, j, h)
        c.font, c.fill, c.alignment, c.border = Font(bold=True, color="FFFFFF"), AZUL, CENTRO, BORDE
        if widths:
            ws.column_dimensions[get_column_letter(j)].width = widths[j - 1]


def titulo(ws, celda, t, size=12, color="1F4E78"):
    ws[celda] = t
    ws[celda].font = Font(bold=True, size=size, color=color)


def nota(ws, celda, t):
    ws[celda] = t
    ws[celda].font = Font(italic=True, color="595959")


def pintar(c, d):
    c.font = Font(bold=True, color=TXT[d])
    c.fill = PatternFill("solid", fgColor=COLOR[d])


def tabla(ws, fila0, cols, filas, alto=45, gris_si=None):
    r = fila0
    for row in filas:
        r += 1
        for j, col in enumerate(cols, 1):
            c = ws.cell(r, j, row[col])
            c.border, c.alignment = BORDE, WRAP
            if gris_si and row.get(gris_si):
                c.font = Font(color="808080")
        if "Decisión" in cols:
            pintar(ws.cell(r, cols.index("Decisión") + 1), row["Decisión"])
        ws.row_dimensions[r].height = alto
    return r


def texto(ws, r, t, ncol=8, alto=None, bold=False):
    ws.cell(r, 1, t).alignment = WRAP
    if bold:
        ws.cell(r, 1).font = Font(bold=True)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=ncol)
    if alto:
        ws.row_dimensions[r].height = alto


wb = Workbook()

# ================================================================= 1. Resumen
ws = wb.active
ws.title = "1. Resumen"
ws.sheet_view.showGridLines = False
for j, w in enumerate([16, 38, 13, 13, 22, 18, 26, 30], 1):
    ws.column_dimensions[get_column_letter(j)].width = w
titulo(ws, "A1", f"Calendario de oportunidades {args.anio} · {args.producto} en compras públicas", 16)
nota(ws, "A2", f"{args.producto} · COMPRASAL, planes de compra (PAC) {A0}–{A2} · Montos estimados: 'se repite' = se planificó, no confirma que se compró")

r = 4
of_ab = abiertos[abiertos["Dec"] == "OFERTAR"]
titulo(ws, f"A{r}", f"1 · HOY ({HOY_TXT}): {len(of_ab)} procesos abiertos para OFERTAR — revisar si aún reciben ofertas", 13, "006100")
r += 1
cols_ab = ["Decisión", "Institución", "Monto", "Mes PAC", "Modalidad", "Código", "Qué compra"]
encabezado(ws, r, cols_ab)
filas = [{"Decisión": a["Dec"], "Institución": nombre[a["Inst"]], "Monto": dinero(a["Monto"]), "Mes PAC": f"{a['Mes']:02d}/{a['AñoMes']}",
          "Modalidad": a["Modalidad"], "Código": a["Códigos"], "Qué compra": a["Categoría"]} for _, a in abiertos.iterrows()]
r = tabla(ws, r, cols_ab, filas, alto=30)

r += 2
titulo(ws, f"A{r}", f"2 · EN DICIEMBRE: preparar las compras de enero a marzo ({len(dic)} instituciones que suelen comprar en ese trimestre)", 13, "7F6000")
r += 1
cols_dic = ["Decisión", "Institución", "Monto típico", K_COMPRAS, K_C2, "Último código", "Qué compra"]
encabezado(ws, r, cols_dic)
r = tabla(ws, r, cols_dic, dic.to_dict("records"), alto=30)

r += 2
titulo(ws, f"A{r}", "3 · TODO EL AÑO: las 15 mejores instituciones → hoja 2 (Top 15). El calendario mes a mes → hoja 3.", 13)

r += 2
titulo(ws, f"A{r}", f"Lo que hay que saber (con datos de {A1} y {A2})")
msgs = [
    f"• Cada año se planifican unas {anual['n'].mean():.0f} compras de prendas que el taller puede ofertar directamente (hasta $50 mil, comparación de precios o subasta inversa), "
    f"por ≈ {dinero(anual['monto'].mean())} al año. {len(of2_util) / 2:.0f} al año dicen qué prenda compran (el resto es 'textiles y vestuario' sin detalle o vestuario artístico). "
    f"La compra típica es de {dinero(float(of2['Monto'].median()))}.",
    f"• {int(((peq['Decisión'] == 'OFERTAR') & peq['_rec']).sum())} instituciones planificaron compras pequeñas en {A1} y en {A2}. El Top 15 elige entre ellas las que hacen más compras de $3k–$25k "
    "de camisetas, polos, deportivo o uniformes (lo que mejor encaja con un taller pequeño).",
    "• Las compras grandes (más de $50 mil) solo sirven por lotes. 'Convenios' y 'subasta en plataformas privadas' hay que confirmarlas antes (ver Notas).",
]
for t in msgs:
    r += 1
    texto(ws, r, t, alto=32)

r += 2
titulo(ws, f"A{r}", f"Temporada · compras para OFERTAR por mes (promedio por año, {A1}–{A2})")
r += 1
encabezado(ws, r, ["Mes", "Compras / año", "Monto / año", "Instituciones / año"])
mx = temp["n"].max()
for m in range(1, 13):
    r += 1
    t = temp.loc[m]
    for j, v in enumerate([MES[m].capitalize(), round(t["n"], 1), dinero(t["monto"]), round(t["inst"], 1)], 1):
        c = ws.cell(r, j, v)
        c.border, c.alignment = BORDE, (CENTRO if j > 1 else Alignment(vertical="center"))
    nivel = 3 if t["n"] >= 0.75 * mx else 2 if t["n"] >= 0.4 * mx else 1
    ws.cell(r, 2).fill = PatternFill("solid", fgColor=VERDES[nivel])
    if nivel == 3:
        ws.cell(r, 2).font = Font(bold=True, color="FFFFFF")

r += 2
titulo(ws, f"A{r}", "Qué significa cada decisión")
r += 1
encabezado(ws, r, ["Decisión", "Líneas", "Qué hacer"])
ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=8)
DESC = {"OFERTAR": "Hasta $50 mil y por comparación de precios o subasta inversa. El taller puede ofertar directamente.",
        "PREPARAR": "Entre $50 mil y $150 mil, modalidad abierta. Posible si el taller puede crecer o asociarse.",
        "SOLO POR LOTES": "Más de $150 mil. Solo vale la pena si la compra se divide en ítems o lotes pequeños.",
        "VERIFICAR": "Convenios o subasta en plataformas privadas: confirmar cómo se participa antes de invertir tiempo.",
        "NO APLICA": "Contratación directa: la institución elige al proveedor sin concurso.",
        "HISTÓRICO": "Municipio que ya no existe (reorganización de 2024). Sirve como historia; buscar al municipio nuevo."}
for d, t in DESC.items():
    n = int((L["Decisión"] == d).sum())
    if not n:
        continue
    r += 1
    ws.cell(r, 1, d)
    ws.cell(r, 2, n).alignment = CENTRO
    ws.cell(r, 3, t).alignment = WRAP
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=8)
    for c in range(1, 9):
        ws.cell(r, c).fill = PatternFill("solid", fgColor=COLOR[d])
        ws.cell(r, c).border = BORDE
    pintar(ws.cell(r, 1), d)
r += 1
nota(ws, f"A{r}", "Una 'línea' = las compras pequeñas (hasta $50 mil) o las grandes de una institución.")

r += 2
titulo(ws, f"A{r}", "Antes de ofertar (lista de control)")
for t in ["☐ Inscribirse como proveedor en COMPRASAL (www.comprasal.gob.sv).",
          "☐ Tener al día las solvencias que piden las bases (Hacienda, seguridad social, municipal).",
          "☐ Cotización tipo por prenda (camisa, polo, camiseta, pantalón, deportivo, chumpa) y por logo DTF, para responder rápido.",
          "☐ Muestras físicas listas: muchas bases piden muestra con la oferta.",
          "☐ En compras grandes: revisar garantías de oferta o cumplimiento y si hay beneficios para MYPE."]:
    r += 1
    texto(ws, r, t)

r += 2
titulo(ws, f"A{r}", "Notas")
n_antig = L[L["Decisión"] == "HISTÓRICO"]["_inst"].nunique()
cuenta = inc["Cuenta como"].value_counts()
for t in [f"• Datos: 4 archivos unidos ({len(todo):,} procesos únicos; {n_en_dos} venían en dos archivos). Se cuentan {len(C):,} compras reales: "
          f"{cuenta.get('Partida agrupada', 0)} partidas de presupuesto del mismo mes se juntaron, y {cuenta.get('Posible repetido', 0) + cuenta.get('Relanzamiento', 0)} procesos repetidos o relanzados se cuentan una vez.",
          f"• Municipios: con la reorganización de mayo de 2024, {len(mapa_muni) + 1} municipios antiguos se unieron a su municipio nuevo porque sus compras recientes nombran el distrito "
          f"(ej. 'Distrito de Tejutla' → Chalatenango Centro). Otros {n_antig} quedan como HISTÓRICO: no se pueden unir sin la lista oficial.",
          f"• 2024 puede contar doble en municipios unidos (el antiguo y el nuevo planificaron por separado). Por eso las cifras anuales usan {A1} y {A2}.",
          "• Convenios: la extensión no encontró convenio marco de uniformes en el Catálogo Electrónico; no es para inscribirse.",
          "• Subasta en plataformas privadas: probablemente es la Bolsa de Productos de El Salvador (BOLPROES), donde se participa por medio de un puesto de bolsa. No está confirmado en los datos.",
          "• Excluido: uniformes escolares, tela y materia prima, ropa hospitalaria, solo calzado y servicios o insumos que no son prendas. La categoría sale de palabras clave del nombre: puede fallar."]:
    r += 1
    texto(ws, r, t, alto=30)

# ================================================================= 2. Top 15
tp = wb.create_sheet("2. Top 15")
tp.sheet_view.showGridLines = False
titulo(tp, "A1", f"Top 15 instituciones para ofertar en {args.anio} · ordenadas por cuándo vigilar", 13)
nota(tp, "A2", f"Criterio: compraron en {A1} y {A2}, compras de hasta $50 mil por comparación de precios o subasta inversa. Ranking: más compras de $3k–$25k, "
               "con más peso para camisetas, polos, deportivo y bordado; luego uniformes y operativo; poco para seguridad. 'Se repite' = se planificó en el PAC.")
cols_top = ["Cuándo vigilar", "Institución", "Ejemplo (último)", "Último código", K_COMPRAS, "Monto típico", K_M2,
            K_C1, K_C2, "Modalidad", "Por qué está aquí"]
encabezado(tp, 4, cols_top, [24, 30, 46, 17, 11, 11, 11, 14, 14, 20, 34])
tabla(tp, 4, cols_top, top.to_dict("records"), alto=48)
tp.freeze_panes = "C5"

# ================================================================= 3. Vista anual
va = wb.create_sheet("3. Vista anual")
va.sheet_view.showGridLines = False
titulo(va, "A1", f"Vista anual {args.anio} · instituciones que compraron en {A1} y {A2}", 13)
nota(va, "A2", f"Cada celda = mes en que compró. Verde claro = 1 año · medio = 2 años · oscuro = los 3 años ({A0}–{A2}). Número = monto típico. ● = abierto ahora. ★ = está en el Top 15.")
hdr = ["Decisión", "Institución", "Qué compra", "Compras 25/26"] + MES3[1:]
encabezado(va, 4, hdr, [12, 34, 28, 9] + [8.5] * 12)
top_ids = set(top["_inst"])
r = 4
for sec, etiq, dsec in [("p", "PARA OFERTAR · compras de hasta $50 mil", peq[peq["_rec"] & (peq["Decisión"] != "HISTÓRICO")]),
                        ("g", "GRANDES COMPRADORES · más de $50 mil (seguir, ofertar solo por lotes)", gra[gra["_rec"]])]:
    r += 1
    c = va.cell(r, 1, etiq)
    c.font = Font(bold=True, color="FFFFFF" if sec == "p" else "1F4E78")
    c.fill = PatternFill("solid", fgColor="548235") if sec == "p" else GRIS
    va.merge_cells(start_row=r, start_column=1, end_row=r, end_column=16)
    dsec = dsec.assign(_t=dsec["_trims"].map(lambda t: t[0])).sort_values(["_ord", "_t", "_puntaje"], ascending=[True, True, False])
    for row in dsec.to_dict("records"):
        r += 1
        inst_txt = ("★ " if (sec == "p" and row["_inst"] in top_ids) else "") + row["Institución"]
        for j, v in enumerate([row["Decisión"], inst_txt, row["Qué compra"], row[K_COMPRAS]], 1):
            c = va.cell(r, j, v)
            c.border, c.alignment = BORDE, Alignment(vertical="center", wrap_text=True)
        va.cell(r, 4).alignment = CENTRO
        pintar(va.cell(r, 1), row["Decisión"])
        g = C[(C["Inst"] == row["_inst"]) & (C["Tamaño"] == row["_tam"])]
        for m in range(1, 13):
            c = va.cell(r, 4 + m)
            c.border = BORDE
            gm = g[g["Mes"] == m]
            if len(gm):
                k = min(gm["Año"].nunique(), 3)
                c.value = dinero(float(gm["Monto"].median())) + (" ●" if gm["Abierto"].any() else "")
                c.fill = PatternFill("solid", fgColor=VERDES[k])
                c.font = Font(bold=True, size=8, color="FFFFFF" if k == 3 else "000000")
                c.alignment = CENTRO
        va.row_dimensions[r].height = 28
va.freeze_panes = "E5"

# ================================================================= 4. Por institución
pi = wb.create_sheet("4. Por institución")
cols_pi = ["Decisión", "Institución", "Código institución", "Qué compra", "¿Se repite?", "Cuándo vigilar", K_C1, K_C2,
           K_COMPRAS, "Compras (nº)", "Monto típico", K_M2, K_TOT, "Modalidad",
           "Categorías", "Siguiente paso", "Ejemplo (último)", "Unido desde", "Códigos"]
encabezado(pi, 1, cols_pi, [13, 34, 11, 30, 18, 26, 14, 14, 10, 9, 11, 11, 14, 22, 38, 50, 46, 24, 40])
L["_grupo"] = L.apply(lambda x: 3 if x["_antiguo"] else (0 if x["_rec"] else (1 if x["_n26"] else 2)), axis=1)
orden = L.sort_values(["_grupo", "_tam", "_ord", "_puntaje"], ascending=[True, False, True, False])
rr = tabla(pi, 1, cols_pi, orden.to_dict("records"), alto=42, gris_si="_antiguo")
for row in pi.iter_rows(min_row=2, min_col=13, max_col=13):
    row[0].number_format = '"$"#,##0'
pi.freeze_panes = "C2"
pi.auto_filter.ref = f"A1:{get_column_letter(len(cols_pi))}{rr}"

# ================================================================= 5. Procesos
pr = wb.create_sheet("5. Procesos")
cols_pr = ["Decisión", "Año PAC", "Mes PAC", "Institución", "Categoría", "Nombre del proceso", "Modalidad", "Monto US$", "Cuenta como",
           "Estado", "Código", "Enlace", "Archivo de origen"]
encabezado(pr, 1, cols_pr, [12, 8, 9, 32, 26, 70, 22, 11, 16, 18, 18, 28, 11])
p = inc.sort_values(["Año", "AñoMes", "Mes", "Monto"])
filas = [{"Decisión": "HISTÓRICO" if x["Muni antiguo sin unir"] else x["Dec proc"], "Año PAC": x["Año"], "Mes PAC": f"{x['Mes']:02d}/{x['AñoMes']}",
          "Institución": nombre[x["Inst"]], "Categoría": x["Categoría"], "Nombre del proceso": x["Nombre del proceso"], "Modalidad": x["Modalidad"],
          "Monto US$": x["Monto"], "Cuenta como": x["Cuenta como"], "Estado": x["Estado"], "Código": x["Código"], "Enlace": x["Enlace"],
          "Archivo de origen": x["Fuente"]} for _, x in p.iterrows()]
rr = tabla(pr, 1, cols_pr, filas, alto=15)
for row in pr.iter_rows(min_row=2):
    row[7].number_format = '"$"#,##0'
    for c in row:
        c.alignment = Alignment(vertical="top")
pr.freeze_panes = "D2"
pr.auto_filter.ref = f"A1:{get_column_letter(len(cols_pr))}{rr}"
r = rr + 2
excl = todo[todo["Categoría"].isna()]["Excluido por"].value_counts()
pr.cell(r, 1, "Excluidos: " + "; ".join(f"{k} ({v})" for k, v in excl.items())).font = Font(italic=True)
r += 1
pr.cell(r, 1, "Municipios unidos: " + "; ".join(f"{todo[todo['Clave'] == a]['Institución'].iloc[0]} → {nombre.get(b, b)} [{evid_muni[a]}]" for a, b in mapa_muni.items())
        + "; Alcaldía de San Salvador → San Salvador Centro").font = Font(italic=True)

for hoja in wb.worksheets:
    hoja.page_setup.orientation = "landscape"
    hoja.page_setup.paperSize = hoja.PAPERSIZE_LETTER
    hoja.page_setup.fitToWidth = 1
    hoja.page_setup.fitToHeight = 0
    hoja.sheet_properties.pageSetUpPr.fitToPage = True
wb.save(out)

print(f"Listo: {out}")
print(f"  compras reales {len(C)} · líneas {len(L)} · compran en {A1} y {A2} (OFERTAR) {int(((peq['Decisión'] == 'OFERTAR') & peq['_rec']).sum())} · abiertos {len(abiertos)}")
print(f"  municipios unidos {len(mapa_muni) + 1} · históricos sin unir {L[L['Decisión'] == 'HISTÓRICO']['_inst'].nunique()}")
