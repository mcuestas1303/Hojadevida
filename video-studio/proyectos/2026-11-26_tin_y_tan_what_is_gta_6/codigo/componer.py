#!/usr/bin/env python3
"""Composición final del short 4 de Tin & Tan (TIN-EN-S-004).

Toma los fotogramas del motor de acción (mundo 3D y pelea) y les pone encima, en 2D:
  - en los planos de firma (f0–f29 y los últimos 30): Tin y Tan dibujados con `palitos.py` y el lápiz bumerán del
    canal (`efectos.lapiz_bumeran`, sin cambios), más la portada «GTA 7? / Facts, Checked»;
  - los cuadros de impacto (líneas de tinta, 2 f), los 2 cuadros invertidos con máscara, las radiales y el claro de la
    explosión (con máscara, nunca blanco pleno);
  - la capa de datos (texto en tinta; franja de resaltador amarillo: placa en lo que no es marca, subrayado en los
    nombres de marca) y los subtítulos en español quemados en su franja.
Versión 3 (2026-11-26), por las revisiones de la v2: el reparto del cuadro cambia. Antes la acción iba apretada en la franja
de abajo (y 1105–1700, bajo los botones de Shorts) y el subtítulo cortaba el cuadro por la mitad, tapando el televisor.
Ahora: dato arriba (y 380–700) sobre una TARJETA de papel opaca con borde de tinta (ni el humo ni el fuego le quitan
contraste), acción en el centro (y 705–1390) y subtítulo abajo (y 1376–1552), opaco. Los subtítulos ya no se enciman
(cada uno sale cuando entra el siguiente), el borrón del cierre no toca el texto y el claro de la explosión es un
estallido plano de la paleta con borde de tinta (sin transparencias que ensucien el color).
Escribe 06_final/fotogramas/*.jpg (o el video con --video), 06_final/miniatura.png y 07_revision/medidas_composicion.json.
Gratis: Pillow, numpy y ffmpeg.

Uso: python3 componer.py <carpeta de fotogramas del motor> [--video] [--solo 0,82,...] [--hojas]
"""
import json
import math
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

PROY = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROY.parent.parent / "herramientas"))
import efectos as fx  # noqa: E402
import palitos  # noqa: E402
from efectos import Capa, LienzoCapa  # noqa: E402

W, H, FPS = 1080, 1920, 30
VERSION = "v3"
TL = json.loads((PROY / "05_audio" / "linea_de_tiempo.json").read_text(encoding="utf-8"))
MED = {}                          # medidas del motor (dónde cae en el cuadro cada impacto y la explosión); las carga main()
N, K = TL["N"], TL["K"]
L = {f["id"]: f for f in TL["lineas"]}
TINTA, ACENTO, PANEL, CLARO = (27, 27, 34), (255, 210, 31), (244, 241, 234), (255, 244, 184)
FECHA_SELLO = "Nov 26, 2026"      # fecha de la relectura del remate; se actualiza el día de publicar (dirección, D5)
BANDA = (1376, 1552)              # franja de subtítulos (v3: abajo; antes 905–1085, en mitad del cuadro)
DATOS_Y = (380, 700)              # zona de la capa de datos
X0 = 100

# ---------------------------------------------------------------- firma del lápiz bumerán y portada
SUELO, ALTO = 1651.0, 487.0
X_TAN, X_TIN = 0.24 * W, 0.75 * W
PORTADA_GEO = dict(R=ALTO / 5.53, x_tan=X_TAN, x_tin=X_TIN, suelo=SUELO, texto=(100, 400, 760, 700),
                   objeto=(320, 782, 760, 1039),            # el televisor en blanco, medido en el fotograma 0 del motor
                   cara_tan=(121, 1201, 303, 1364), cara_tin=(741, 1163, 944, 1364))
DX_CUERPO = 0.5
GEO = fx.geometria_firma(PORTADA_GEO, subir=0.0, dx_cuerpo=DX_CUERPO)


palitos.PALETA.update({"tinta": "#1B1B22"})     # la tinta de la paleta C, la misma de la pelea (antes la firma salía en tinta parda)


def plano_firma(placa, c):
    """Tin y Tan de la portada y el lápiz bumerán sobre la placa del motor (la tienda, entera o rota)."""
    est = fx.lapiz_bumeran(c, GEO)
    tan, tin = est["tan"], est["tin"]
    lz = LienzoCapa(W, H)
    palitos.dibujar(lz, "tan", X_TAN + DX_CUERPO * tan["dx"], SUELO, ALTO, pose=tan["pose"], expresion="curiosidad",
                    vista="perfil", mira=1, viento=tan["viento"], objeto=tan["objeto"], giro_objeto=tan["giro_objeto"],
                    cabeza_giro=tan["cabeza_giro"])
    palitos.dibujar(lz, "tin", X_TIN, SUELO + tin["dy"], ALTO, pose="parado", expresion="curiosidad", vista="perfil",
                    mira=-1, objeto=False, cabeza_giro=tin["cabeza_giro"])
    capas = [fx.capa_sombra_contacto(X_TAN, SUELO, 180), fx.capa_sombra_contacto(X_TIN, SUELO, 180),
             Capa(lz.resultado(), z=0.0, nombre="principal")] + fx.pintar_lapiz_volador(est, GEO)
    return fx.componer(capas, fx.Camara(), fondo=placa)


# ---------------------------------------------------------------- texto
def fuente(tam):
    return fx.fuente(int(round(tam)))


def ancho(s, tam):
    return fuente(tam).getlength(s, features=fx.RASGOS)


@lru_cache(maxsize=64)
def bloque(renglones, semilla=7):
    """renglones: tupla de (tam, ((texto, estilo), ...)); estilo: '' tinta, 'placa' franja llena, 'subr' subrayado (40 %
    inferior, para nombres de marca), 'sello' recuadro de tinta. Devuelve (imagen RGBA, cajas de cada renglón)."""
    rng = np.random.default_rng(semilla)
    m = 40
    anchos = [sum(ancho(t, tam) for t, _ in segs) for tam, segs in renglones]
    alto = sum(int(tam * 1.42) for tam, _ in renglones)
    img = Image.new("RGBA", (int(max(anchos)) + 2 * m, alto + 2 * m), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    y, cajas = m, []
    for (tam, segs), aw in zip(renglones, anchos):
        f = fuente(tam)
        asc = 0.74 * tam                       # altura de las mayúsculas de Inter Display
        base = y + int(tam * 1.02)
        x = float(m)
        for t, estilo in segs:
            w = ancho(t, tam)
            j = lambda a: float(rng.uniform(-a, a))
            if estilo == "placa":
                cae = 0.035 * w * 0.5         # ≈ 2° de inclinación de trazo de mano
                p = [(x - 0.14 * tam + j(4), base - asc - 0.20 * tam + cae + j(3)), (x + w + 0.14 * tam + j(4), base - asc - 0.20 * tam - cae + j(3)),
                     (x + w + 0.18 * tam + j(4), base + 0.24 * tam - cae + j(3)), (x - 0.18 * tam + j(4), base + 0.24 * tam + cae + j(3))]
                d.polygon(p, fill=ACENTO + (255,))
            elif estilo == "subr":
                cae = 0.035 * w * 0.5
                p = [(x - 0.06 * tam + j(5), base - 0.36 * asc + cae + j(3)), (x + w + 0.08 * tam + j(5), base - 0.36 * asc - cae + j(3)),
                     (x + w + 0.03 * tam + j(5), base + 0.10 * tam - cae + j(3)), (x - 0.10 * tam + j(5), base + 0.10 * tam + cae + j(3))]
                d.polygon(p, fill=ACENTO + (255,))
            elif estilo == "sello":
                d.rounded_rectangle([x - 0.3 * tam, base - asc - 0.28 * tam, x + w + 0.3 * tam, base + 0.3 * tam], radius=int(0.2 * tam),
                                    outline=TINTA + (255,), width=max(3, int(0.07 * tam)), fill=PANEL + (235,))
            x += w
        x = float(m)
        for t, _ in segs:
            d.text((x, base), t, font=f, fill=TINTA + (255,), anchor="ls", features=fx.RASGOS)
            x += ancho(t, tam)
        cajas.append((m, base - asc, m + aw, base))
        y += int(tam * 1.42)
    return img, m, cajas


@lru_cache(maxsize=32)
def tarjeta(tam, m):
    """Tarjeta de papel opaca con borde de tinta, del tamaño del bloque de texto: el dato se lee igual sobre la pared, el
    humo o el fuego (tinta sobre #F4F1EA ≈ 15:1)."""
    img = Image.new("RGBA", tam, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    a = 16
    d.rounded_rectangle([m - 30 + 7, m - a + 9, tam[0] - m + 30 + 7, tam[1] - m + a + 9], radius=20, fill=TINTA + (255,))      # sombra dura de tinta, de viñeta
    d.rounded_rectangle([m - 30, m - a, tam[0] - m + 30, tam[1] - m + a], radius=20, fill=PANEL + (255,), outline=TINTA + (255,), width=5)
    return img


def pegar(base, img, x, y, esc=1.0, alfa=1.0):
    if alfa <= 0:
        return
    im = img
    if esc != 1.0:
        im = img.resize((max(1, int(img.width * esc)), max(1, int(img.height * esc))), Image.LANCZOS)
        y += (img.height - im.height) / 2
    if alfa < 1:
        im = im.copy()
        im.putalpha(im.getchannel("A").point(lambda v: int(v * alfa)))
    base.paste(im, (int(round(x)), int(round(y))), im)


def R(tam, *segs):
    return (tam, tuple((s if isinstance(s, tuple) else (s, "")) for s in segs))


# Capa de datos: (entra, sale, y del tope, renglones). Un dato a la vez; entra con golpe de 5 f, se asienta y no se mueve.
def datos():
    d = []
    r1 = R(64, ("GTA", "subr"), " = ", ("Grand Theft Auto", "subr"))
    r2 = R(60, "a game series · ", ("since 1997", "placa"))
    r3 = R(60, "made today by ", ("Rockstar Games", "subr"))
    f2 = L["T2"]["f0"] + int(0.62 * L["T2"]["dura_f"])            # cuando se dice el año
    fuera = K["K3"] - 8
    f3 = L["T3"]["f0"] + 2                                        # la tarjeta crece un renglón con cada dato; los anteriores no se mueven
    d += [(L["T1"]["f0"] + 2, f2, 404, (r1,), "tarjeta 1"), (f2, f3, 404, (r1, r2), "tarjeta 2"), (f3, fuera, 404, (r1, r2, r3), "tarjeta 3")]
    d.append((K["K3"] + 24, L["T5"]["f0"] - 2, 410, (R(132, ("GTA 6", "subr")), R(62, "out since ", ("Nov 19, 2026", "placa"))), "GTA 6"))
    d.append((L["T5"]["f0"] + 2, L["C"]["f0"] - 2, 430, (R(74, "the ", ("sixth", "placa"), " numbered game"),), "sexto"))
    d.append((L["T6"]["f0"] + 2, K["mazo"] + 10, 430, (R(88, "rated M · ", ("17 and over", "placa")),), "rated M"))
    d.append((L["T8"]["f0"] + 2, K["carrera"] - 2, 440, (R(60, "from GTA 5 to GTA 6"),), "de 5 a 6"))
    d.append((K["radiales"] + 31, L["B"]["f1"] - 6, 400, (R(106, ("13 years, 63 days", "placa")), R(54, "GTA 5: Sep 17, 2013"), R(54, "GTA 6: Nov 19, 2026")), "la cuenta"))
    d.append((L["T10"]["f0"] + 2, K["cierre"] - 2, 372, (R(84, ("GTA 7", "subr"), ":"), R(104, ("not announced", "placa")), R(50, (f"as of {FECHA_SELLO}", "sello"))), "respuesta"))
    return d


DATOS = datos()
PORTADA_TXT = (R(150, ("GTA 7", "subr"), "?"), R(92, "Facts, Checked"))


def capa_datos(base, f, medidas=None):
    for f0, f1, y, rens, nombre in DATOS:
        if not (f0 <= f < f1):
            continue
        img, m, cajas = bloque(rens)
        t = f - f0 if nombre not in ("tarjeta 2", "tarjeta 3") else 9
        esc = 1.0 if t >= 5 else 0.86 + 0.14 * fx.eo(t / 5.0) + 0.05 * math.sin(math.pi * t / 5.0)
        alfa = min(1.0, (t + 1) / 2.0) * (min(1.0, (f1 - f) / 3.0) if nombre not in ("tarjeta 1", "tarjeta 2") else 1.0)
        pegar(base, tarjeta(img.size, m), X0 - m, y - m, esc, alfa)
        pegar(base, img, X0 - m, y - m, esc, alfa)
        if medidas is not None and t == 5:
            medidas.setdefault("datos", []).append({"dato": nombre, "entra": f0, "quieto_desde": f0 + 5, "sale": f1, "quieto_f": f1 - 3 - (f0 + 5),
                                                    "caja": [X0, y + int(cajas[0][1] - m), X0 + img.width - 2 * m, y + img.height - 2 * m]})


def partir(texto, tam, tope):
    """Uno o dos renglones equilibrados (sin palabra huérfana)."""
    if ancho(texto, tam) <= tope:
        return [texto]
    pal = texto.split()
    cortes = [(max(ancho(" ".join(pal[:i]), tam), ancho(" ".join(pal[i:]), tam)), i) for i in range(1, len(pal))]
    _, i = min(cortes)
    return [" ".join(pal[:i]), " ".join(pal[i:])]


@lru_cache(maxsize=32)
def panel_subtitulo(texto):
    tam = 54
    ren = partir(texto, tam, 760)
    assert len(ren) <= 2 and max(ancho(r, tam) for r in ren) <= 800, texto
    aw = max(ancho(r, tam) for r in ren)
    alto = int(len(ren) * tam * 1.3 + 34)
    assert alto <= BANDA[1] - BANDA[0], texto
    img = Image.new("RGBA", (int(aw) + 72, alto), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, img.width - 1, img.height - 1], radius=22, fill=PANEL + (255,), outline=TINTA + (255,), width=3)     # opaco: 15:1 sobre cualquier fondo
    for i, r in enumerate(ren):
        d.text((img.width / 2, 17 + int(tam * 1.02) + i * tam * 1.3), r, font=fuente(tam), fill=TINTA + (255,), anchor="ms", features=fx.RASGOS)
    return img


def subtitulos(base, f):
    ls = TL["lineas"]
    for i, l in enumerate(ls):
        sig = ls[i + 1]["f0"] if i + 1 < len(ls) else N
        a, b = max(l["f0"], 30), min(l["f1"] + 4, K["cierre"], sig)      # sale cuando entra el siguiente: nunca dos a la vez
        if a <= f < b:
            img = panel_subtitulo(l["es"])
            pegar(base, img, (W - img.width) / 2, (BANDA[0] + BANDA[1]) / 2 - img.height / 2)


# ---------------------------------------------------------------- cuadros de impacto y explosión
@lru_cache(maxsize=4)
def lineas_radiales(cx, cy, n, dentro, semilla):
    rng = np.random.default_rng(semilla)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for i in range(n):
        a = i / n * 2 * math.pi + rng.uniform(-0.05, 0.05)
        r0 = dentro * rng.uniform(0.85, 1.35)
        w = rng.uniform(0.008, 0.028)
        p0 = (cx + math.cos(a) * r0, cy + math.sin(a) * r0)
        d.polygon([p0, (cx + math.cos(a - w) * 2600, cy + math.sin(a - w) * 2600), (cx + math.cos(a + w) * 2600, cy + math.sin(a + w) * 2600)], fill=TINTA + (255,))
    return img


@lru_cache(maxsize=4)
def estallido_claro(cx, cy, r, semilla):
    """Claro de la explosión: estallido plano de la paleta (#FFF4B8) con borde de tinta y escalón duro. Sin transparencia."""
    rng = np.random.default_rng(semilla)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    n = 22
    pts = [(cx + math.cos(i / n * 2 * math.pi) * r * (1.0 if i % 2 else 0.74) * rng.uniform(0.92, 1.08), cy + math.sin(i / n * 2 * math.pi) * r * (1.0 if i % 2 else 0.74) * rng.uniform(0.92, 1.08)) for i in range(n)]
    d.polygon(pts, fill=CLARO + (255,))
    d.line(pts + [pts[0]], fill=TINTA + (255,), width=12, joint="curve")
    return img


def efectos_post(img, f):
    P = TL["post"]
    if f in P["impacto"]:
        k = P["impacto"].index(f)
        cx, cy = MED.get(("impacto_estante_px", "impacto_mostrador_px", "impacto_tele_px")[k // 2], (540, 1000))
        r = lineas_radiales(int(cx), int(cy), 30, 470, 11 + k // 2)
        img.paste(r, (0, 0), r)
    elif f in P["invertidos"]:                 # una sola vez, 2 f, con máscara circular y a media mezcla
        cx, cy = MED.get("explosion_px", (540, 700))
        m = fx.mascara_circulo(int(cx), int(cy), 300, suave=6.0)
        img = fx.negativo_paleta(img, mascara=m, mezcla=0.55)
    elif f in P["radiales"]:
        cx, cy = MED.get("radiales_px", (540, 760))
        r = lineas_radiales(int(cx), int(cy), 26, 520, 31 + (f - P["radiales"][0]) // 2)
        img.paste(r, (0, 0), r)
    elif f in P["claro"]:                      # estallido plano de la paleta, ≤ 30 % del cuadro, 4 f; nunca blanco pleno
        cx, cy = MED.get("claro_px", (540, 740))
        k = f - P["claro"][0]
        e = estallido_claro(int(cx), int(cy), 330 + 40 * k, 5 + k // 2)
        img.paste(e, (0, 0), e)
    return img


def fotograma(carpeta, f, medidas=None):
    img = Image.open(carpeta / f"f_{f:04d}.jpg").convert("RGB")
    firma = f < 30 or f >= K["cierre"]
    borra = (40, 110, 50)[f - (K["cierre"] - 2)] if K["cierre"] - 2 <= f <= K["cierre"] else 0     # el borrón de 3 f de la firma
    if firma:
        img = plano_firma(img, f if f < 30 else f - N).convert("RGB")
        if borra:
            img = fx.borron(img, borra)        # v3: se emborrona la escena, nunca el texto
        bl, m, _ = bloque(PORTADA_TXT, 3)
        pegar(img, bl, X0 - m, 396 - m)
    else:
        img = efectos_post(img, f)
        if borra:
            img = fx.borron(img, borra)
        capa_datos(img, f, medidas)
        subtitulos(img, f)
    return img


def main():
    carpeta = Path(sys.argv[1])
    ev = carpeta.parent / "eventos.json"
    if ev.is_file():
        MED.update({k: v for k, v in json.loads(ev.read_text())["medidas"].items() if k.endswith("_px")})
    solo = None
    if "--solo" in sys.argv:
        solo = [int(x) for x in sys.argv[sys.argv.index("--solo") + 1].split(",")]
    salida = PROY / "06_final"
    (salida / "fotogramas").mkdir(parents=True, exist_ok=True)
    medidas = {"firma": fx.comprobar_firma(GEO, N), "portada": PORTADA_GEO, "fecha_sello": FECHA_SELLO}
    if "--video" in sys.argv:
        mp4 = salida / f"tin_y_tan_short04_{VERSION}_sin_audio.mp4"
        ff = subprocess.Popen(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                               "-i", "-", "-c:v", "libx264", "-preset", "slow", "-crf", "15", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(mp4)], stdin=subprocess.PIPE)
        lum = []
        for f in range(N):
            img = fotograma(carpeta, f, medidas)
            lum.append(fx.luminosidad(img))
            if f == 0:
                img.save(salida / "miniatura.png")
            if f % 6 == 0 or f in TL["post"]["impacto"] + TL["post"]["invertidos"] + TL["post"]["claro"]:
                img.resize((540, 960), Image.LANCZOS).save(salida / "fotogramas" / f"f_{f:04d}.jpg", quality=88)
            ff.stdin.write(img.tobytes())
            if f % 100 == 0:
                print("fotograma", f, flush=True)
        ff.stdin.close(); ff.wait()
        medidas["destellos"] = fx.comprobar_destellos(lum, estricto=False)
        (PROY / "07_revision").mkdir(exist_ok=True)
        (PROY / "07_revision" / "medidas_composicion.json").write_text(json.dumps(medidas, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
        print("destellos:", {k: v for k, v in medidas["destellos"].items() if k != "limites"})
        print("firma:", medidas["firma"])
    else:
        for f in (solo or range(N)):
            fotograma(carpeta, f, medidas).save(salida / "fotogramas" / f"p_{f:04d}.jpg", quality=90)
        print("firma:", medidas["firma"]["pasa"], medidas["firma"]["despejes_px"])


if __name__ == "__main__":
    main()
