#!/usr/bin/env python3
"""Efectos de video y profundidad para los videos dibujados por código (canal «Tin & Tan»).

Biblioteca común (pedido del dueño, 2026-11-23: «quiero que le demos profundidad y comencemos a usar más efectos de
video»). Solo usa Pillow y numpy: no gasta créditos. Todo es determinista: depende del número de fotograma o de un
avance `p` (0 a 1) que calcula quien llama; nada mira el reloj ni usa azar sin semilla.
Estudio: `video-studio/estudios/2026-11-23_efectos_y_profundidad_ejemplos_del_dueno.md`.
Ejemplo completo: `video-studio/proyectos/2026-11-23_prueba_efectos_tin_y_tan/codigo/render.py`.

Uso rápido (un plano con profundidad):

    import efectos as fx, palitos
    lz = fx.LienzoCapa(700, 900)                                   # lienzo transparente, mismo trato que palitos.Lienzo
    palitos.dibujar(lz, "tin", 350, 860, 600)
    tin = fx.Capa(lz.resultado(1.5), z=0, x=400, y=700, esc=1.5,   # la imagen va a 1,5 px por px: aguanta el zoom
                  sombra=dict(dx=14, dy=10, radio=10, opacidad=0.22))
    cam = fx.Camara(x=560, avance=120, foco=0, apertura=0.02, campo=150, niebla=0.35)
    img = fx.componer([pared, tin, primer_plano], cam)             # RGB de 1080x1920 sobre papel con textura

CONVENCIONES
  - Coordenadas «de reposo»: cada capa se dibuja como se ve con la cámara quieta (x = 540, y = 960, avance 0, zoom 1).
    La cámara las desplaza y escala según su profundidad `z` (0 = plano de los personajes; positivo = más lejos;
    negativo = más cerca de la cámara). Distancia de la cámara al plano z = 0: `focal` (1000 por defecto).
  - Las transiciones reciben dos imágenes RGB (a = la que sale, b = la que entra) y un avance p de 0 a 1.
  - Colores: los de `palitos.PALETA`. Ningún efecto saca blanco puro ni negro puro: el destello usa el blanco de
    papel `#FFF8EC` con opacidad limitada y el negativo cambia tinta por papel.

FUNCIONES (con un ejemplo corto de cada una)

  Movimiento
    muelle(t, kc)                 respuesta de un muelle de 0 a 1 (se pasa y vuelve). `0.85 + 0.15 * fx.muelle(t, fx.POP)`
    muelle_exacto(t, kc, dur)     igual, pero vale 1 exacto en t = dur.
    eo(u), eio(u), clamp, lerp    ease-out cúbico, ease in-out cúbico, recorte e interpolación.
    sacudida(f_local, amplitud)   sacudida corta de cámara: `cam.temblor = fx.sacudida(f - f_golpe, 16)`
    golpe_de_zoom(t, cuanto)      factor de zoom de un «zoom de golpe»: `cam.zoom = fx.golpe_de_zoom(t - t0, 0.35)`

  Lienzos, capas y cámara
    LienzoCapa(ancho, alto)       lienzo RGBA transparente con supermuestreo, para dibujar con palitos o con Marco.
    Marco(lz, cx, cy, esc, rot)   sistema local para dibujar objetos (poli, disco, linea, rect, caja, arco).
    Capa(img, z, x, y, esc, ...)  una capa de la escena. `fx.Capa(img, z=800, x=-300, y=-200)`
    Camara(x, y, avance, zoom, foco, apertura, campo, niebla, temblor)
    componer(capas, camara)       paralaje + desenfoque por distancia al foco + niebla + sombras -> imagen RGB.
    desenfocar(img, radio)        desenfoque gaussiano rápido (reduce el tamaño si el radio es grande; respeta el alfa).
    acercar(img, zoom, centro)    zoom de una imagen ya compuesta alrededor de un punto.
    borron(img, px, "h"|"v")      desenfoque de movimiento en una dirección.

  Papel y sombras
    papel(ancho, alto)            papel con grano y viñeta muy suaves; el grano es el mismo en todos los fotogramas.
    sombra_contacto(ancho, alto)  elipse suave para poner bajo los pies. `fx.capa_sombra_contacto(x, y_suelo, 220)`
    sombra_proyectada(img, dx, dy, radio, opacidad)   la sombra de una capa, desplazada y difuminada.
    sombra_de_suelo(img, y_suelo) la sombra tumbada sobre el suelo (aplastada e inclinada).
    con_sombra(img, ...)          la imagen con su sombra proyectada debajo.

  Transiciones (a, b, p)
    revelar_desde_desenfoque(img, p)          el plano entra borroso y se aclara.
    barrido_obturador(a, b, p, direccion)     barrido con borrón direccional y borde de obturador.
    transicion_zoom(a, b, p)                  a se acerca de golpe, corte, b llega con muelle.
    atravesar(a, b, p, centro, radio)         la cámara pasa por un hueco circular de `a` hacia `b`.
    cruce_por_delante(a, b, p, objeto)        algo cruza por delante y esconde el corte. `objeto=fx.barra_de_cruce()`
    congelado_con_marco(a, b, p)              `a` se congela, se vuelve una foto con marco y deja ver `b`.
    salida_del_cuadro(a, b, p, direccion)     `a` sale del cuadro y `b` entra detrás (latigazo).

  Acentos
    destello(img, f_local)        destello de entrada de 2 a 4 fotogramas (blanco de papel, opacidad máxima 0,6).
    negativo_paleta(img, mascara) negativo dentro de la paleta: la tinta pasa a papel y el papel a tinta.
    mascara_circulo(cx, cy, r)    máscara para limitar el negativo o el destello a una zona.
    garabato(base, trazos, p)     dibuja a mano alzada, de a poco: `fx.garabato(img, fx.trazo_circulo(540, 500, 300, 200), p)`
    trazo_subrayado, trazo_flecha, trazo_circulo     los trazos de los garabatos.

  Texto
    T(s), K(s), R(s)              segmentos en tinta, mostaza (palabra clave, con contorno) y tomate (cifra final).
    poner_texto(base, segs, x, tope, tam)     texto con la tipografía del canal; mostaza y tomate llevan contorno.
    palabra_clave(base, segs, x, tope, tam, t)   lo mismo, con entrada de muelle.
    panel_vidrio(base, caja)      panel translúcido que desenfoca lo que tiene detrás.
    texto_vidrio(base, segs, x, tope, tam)    texto sobre su panel de vidrio.
    contador(t, t0, t1, a, b)     entero que solo sube. `fx.K(f"{fx.contador(t, 1.0, 2.2, 0, 60)}")`
    titulares_en_cascada(base, titulares, t, x, tope, tam)   paneles que caen uno tras otro.
    rotulo(base, s)               rótulo pequeño de la zona segura (para pruebas y notas).

  Firma del canal (lápiz bumerán; Tan lanza al final y atrapa al principio)
    geometria_firma(portada)      puntos del vuelo a partir de las medidas de la portada; falla si no hay pasillo.
    lapiz_bumeran(c, geo)         estado de la firma en el fotograma c (c < 0 cierre, c >= 0 apertura), sin dibujar.
    pintar_lapiz_volador(est, geo)   las `Capa` del lápiz en vuelo (obturador de subpasos) y de su sombra de suelo.
    golpes_firma(N)               los sonidos de la firma: (fotograma, nombre, pico en dBFS).
    comprobar_firma(geo, N)       empalme, velocidades y despejes medidos.

  Seguridad
    comprobar_destellos(fotogramas, fps)      falla (DestellosError) si hay más de 3 cambios bruscos de luminosidad
                                              por segundo o un salto a pantalla completa mayor que el umbral.

Versiones:
    1.0 (2026-11-23)  primera versión, hecha para la prueba de efectos de Tin & Tan.
    1.1 (2026-11-24)  firma del canal, el lápiz bumerán (`canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`, §9):
                      geometria_firma, lapiz_bumeran, pintar_lapiz_volador, golpes_firma, comprobar_firma.
                      Solo la variante de partida (bucle, atrapa Tan); «sin retorno» y atrapa="tin" no están escritas.
"""
import math
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import palitos  # noqa: E402
from palitos import PALETA, SS  # noqa: E402

VERSION = "1.1"
W, H, FPS = 1080, 1920, 30
SEG_X0, SEG_X1, SEG_Y0, SEG_Y1 = 100, 980, 250, 1670          # zona segura de los Shorts (formatos.md)
# Inter Display Medium, SIL OFL 1.1. En Windows no viene con el sistema: se deja en herramientas/fuentes/ (no se sube al repositorio).
_FUENTE_LOCAL = __import__("pathlib").Path(__file__).resolve().parent / "fuentes" / "InterDisplay-Medium.otf"
FUENTE = str(_FUENTE_LOCAL) if _FUENTE_LOCAL.is_file() else "/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf"


def _rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


PAPEL, SOMBRA, TINTA = PALETA["papel"], PALETA["papel_sombra"], PALETA["tinta"]
MARRON, MOSTAZA, TOMATE, BLANCO = PALETA["marron"], PALETA["mostaza"], PALETA["tomate"], PALETA["blanco"]
PAPEL_RGB, SOMBRA_RGB, TINTA_RGB, BLANCO_RGB = _rgb(PAPEL), _rgb(SOMBRA), _rgb(TINTA), _rgb(BLANCO)

# ---------------------------------------------------------------- movimiento
POP, SLIDE, SELLO = (220.0, 20.0), (120.0, 16.0), (320.0, 26.0)   # (rigidez, amortiguación), masa 1


def muelle(t, kc=POP, m=1.0):
    """Respuesta de un muelle amortiguado que va de 0 a 1 (se pasa un poco y vuelve). t en segundos."""
    if t <= 0:
        return 0.0
    k, c = kc
    w0 = math.sqrt(k / m)
    z = c / (2 * math.sqrt(k * m))
    wd = w0 * math.sqrt(1 - z * z)
    return 1 - math.exp(-z * w0 * t) * (math.cos(wd * t) + z * w0 / wd * math.sin(wd * t))


def muelle_exacto(t, kc, dur):
    """Igual, pero normalizado para valer exactamente 1 en t = dur."""
    return muelle(min(t, dur), kc) / muelle(dur, kc)


def clamp(u, a=0.0, b=1.0):
    return max(a, min(b, u))


def lerp(a, b, p):
    return a + (b - a) * p


def eo(u):
    """Ease-out cúbico: no se pasa ni retrocede."""
    u = clamp(u)
    return 1 - (1 - u) ** 3


def eio(u):
    """Ease in-out cúbico."""
    u = clamp(u)
    return 4 * u ** 3 if u < 0.5 else 1 - (-2 * u + 2) ** 3 / 2


def sacudida(f_local, amplitud=14.0, dur=8, semilla=0.0):
    """Sacudida corta de cámara: (dx, dy) en px para el fotograma `f_local` contado desde el golpe. Dura `dur`
    fotogramas y se apaga sola. Se suma a `Camara.temblor`."""
    if f_local < 0 or f_local >= dur:
        return (0.0, 0.0)
    a = amplitud * (1 - f_local / dur) ** 2
    return (a * math.sin(2.4 * f_local + 1.0 + semilla), a * math.cos(3.1 * f_local + 0.4 + 1.7 * semilla))


def golpe_de_zoom(t, cuanto=0.3, kc=SELLO):
    """Zoom de golpe: factor que salta de 1 a 1 + cuanto con un muelle (se pasa un poco y se asienta). t = segundos
    desde el golpe; antes del golpe vale 1."""
    return 1 + cuanto * muelle(t, kc)


# ---------------------------------------------------------------- lienzos y dibujo
class LienzoCapa:
    """Lienzo RGBA transparente con el mismo trato que `palitos.Lienzo` (tiene .img y .d, supermuestreo x3): sirve
    para `palitos.dibujar`, `palitos.cabeza`, `palitos.mando`… y para `Marco`. `resultado(esc)` devuelve la capa
    reducida, a `esc` píxeles por píxel de reposo (1,5 o 2 si la cámara se va a acercar)."""

    def __init__(self, ancho, alto):
        self.ancho, self.alto = ancho, alto
        self.img = Image.new("RGBA", (ancho * SS, alto * SS), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.img)

    def resultado(self, esc=1.0):
        return self.img.resize((int(round(self.ancho * esc)), int(round(self.alto * esc))), Image.LANCZOS)


class Marco:
    """Sistema local para dibujar objetos sobre un lienzo de palitos (x3): origen en (cx, cy) px, escala y rotación
    (grados, sentido horario en pantalla). Viene del render del short 2, con `arco` y `linea` de contorno añadidos."""

    def __init__(self, lz, cx, cy, esc=1.0, rot=0.0):
        self.lz, self.d = lz, lz.d
        self.cx, self.cy, self.esc, self.rot = cx, cy, esc, rot
        a = math.radians(rot)
        self.ca, self.sa = math.cos(a), math.sin(a)

    def xy(self, x, y):
        return (self.cx + self.esc * (x * self.ca - y * self.sa), self.cy + self.esc * (x * self.sa + y * self.ca))

    def p(self, x, y):
        X, Y = self.xy(x, y)
        return (X * SS, Y * SS)

    def poli(self, pts, relleno):
        self.d.polygon([self.p(*q) for q in pts], fill=relleno)

    def disco(self, x, y, r, relleno):
        X, Y = self.p(x, y)
        R = r * self.esc * SS
        self.d.ellipse([X - R, Y - R, X + R, Y + R], fill=relleno)

    def anillo(self, x, y, r, borde, relleno, tinta=TINTA):
        """Disco con contorno hacia adentro."""
        self.disco(x, y, r, tinta)
        if r - borde > 0:
            self.disco(x, y, r - borde, relleno)

    def linea(self, pts, ancho, relleno=TINTA):
        P = [self.p(*q) for q in pts]
        w = max(1, int(round(ancho * self.esc * SS)))
        self.d.line(P, fill=relleno, width=w, joint="curve")
        for q in P:
            self.d.ellipse([q[0] - w / 2, q[1] - w / 2, q[0] + w / 2, q[1] + w / 2], fill=relleno)

    def rect(self, x0, y0, x1, y1, relleno, radio=0.0):
        if radio <= 0:
            self.poli([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], relleno)
            return
        pts = []
        for cx, cy, a0 in ((x1 - radio, y0 + radio, -90), (x1 - radio, y1 - radio, 0),
                           (x0 + radio, y1 - radio, 90), (x0 + radio, y0 + radio, 180)):
            for i in range(9):
                a = math.radians(a0 + 90 * i / 8)
                pts.append((cx + radio * math.cos(a), cy + radio * math.sin(a)))
        self.poli(pts, relleno)

    def caja(self, x0, y0, x1, y1, relleno, borde, radio=0.0, tinta=TINTA):
        """Rectángulo con contorno hacia adentro."""
        self.rect(x0, y0, x1, y1, tinta, radio)
        self.rect(x0 + borde, y0 + borde, x1 - borde, y1 - borde, relleno, max(0.0, radio - borde))

    def poli_borde(self, pts, relleno, borde, tinta=TINTA):
        """Polígono relleno con contorno de línea redonda."""
        self.poli(pts, relleno)
        self.linea(list(pts) + [pts[0]], borde, tinta)


# ---------------------------------------------------------------- desenfoques
def desenfocar(img, radio):
    """Desenfoque gaussiano de `radio` px. Con radios grandes reduce la imagen antes (más rápido, mismo aspecto).
    En imágenes RGBA trabaja con el color premultiplicado, para que los bordes no salgan oscuros."""
    if radio < 0.35:
        return img
    modo = img.mode
    trabajo = img.convert("RGBa") if modo == "RGBA" else img
    f = 1 if radio < 6 else min(8, int(radio // 3))
    if f > 1:
        w, h = trabajo.size
        chico = trabajo.resize((max(1, w // f), max(1, h // f)), Image.BOX)
        chico = chico.filter(ImageFilter.GaussianBlur(radio / f))
        out = chico.resize((w, h), Image.BILINEAR)
    else:
        out = trabajo.filter(ImageFilter.GaussianBlur(radio))
    return out.convert("RGBA") if modo == "RGBA" else out


def borron(img, px, direccion="h"):
    """Desenfoque de movimiento (media móvil de `px` píxeles) horizontal ("h") o vertical ("v"). Imagen RGB."""
    px = int(round(px))
    if px < 2:
        return img
    a = np.asarray(img, dtype=np.float32)
    eje = 1 if direccion == "h" else 0
    izq, der = px // 2, px - px // 2
    relleno = [(0, 0), (0, 0), (0, 0)]
    relleno[eje] = (izq + 1, der)
    c = np.cumsum(np.pad(a, relleno, mode="edge"), axis=eje)
    n = a.shape[eje]
    if eje == 1:
        out = (c[:, px:px + n] - c[:, :n]) / px
    else:
        out = (c[px:px + n] - c[:n]) / px
    return Image.fromarray(np.clip(out + 0.5, 0, 255).astype(np.uint8))


def acercar(img, zoom, centro=None, fondo=PAPEL):
    """Zoom de una imagen ya compuesta alrededor de `centro` (px; por defecto el centro del cuadro). Con zoom < 1 la
    imagen se reduce y se rodea de `fondo`."""
    w, h = img.size
    cx, cy = centro or (w / 2, h / 2)
    if abs(zoom - 1) < 1e-6:
        return img
    if zoom > 1:
        x0, y0 = cx - cx / zoom, cy - cy / zoom
        return img.resize((w, h), Image.BICUBIC, box=(x0, y0, x0 + w / zoom, y0 + h / zoom))
    out = Image.new("RGB", (w, h), fondo)
    chico = img.resize((max(1, int(round(w * zoom))), max(1, int(round(h * zoom)))), Image.LANCZOS)
    out.paste(chico, (int(round(cx * (1 - zoom))), int(round(cy * (1 - zoom)))))
    return out


def _desplazar(img, dx, dy, fondo=PAPEL):
    out = Image.new("RGB", img.size, fondo)
    out.paste(img, (int(round(dx)), int(round(dy))))
    return out


def _mezclar(a, b, m):
    """a * m + b * (1 - m). m: matriz float (alto, ancho) o (alto, ancho, 1) de 0 a 1."""
    A, B = np.asarray(a, dtype=np.float32), np.asarray(b, dtype=np.float32)
    if m.ndim == 2:
        m = m[:, :, None]
    return Image.fromarray(np.clip(A * m + B * (1 - m) + 0.5, 0, 255).astype(np.uint8))


# ---------------------------------------------------------------- papel
@lru_cache(maxsize=4)
def _papel(ancho, alto, grano, vineta, semilla):
    rng = np.random.default_rng(semilla)
    yy, xx = np.mgrid[0:alto, 0:ancho].astype(np.float32)
    r = np.hypot((xx - ancho / 2) / (ancho / 2), (yy - alto / 2) / (alto / 2)) / math.sqrt(2)    # 0 centro, 1 esquina
    v = np.clip((r - 0.45) / 0.55, 0, 1) ** 2 * vineta
    base = np.array(PAPEL_RGB, dtype=np.float32) * (1 - v[:, :, None]) + np.array(SOMBRA_RGB, dtype=np.float32) * v[:, :, None]

    def ruido(div):
        n = rng.normal(0, 1, (alto // div + 2, ancho // div + 2)).astype(np.float32)
        n = np.asarray(Image.fromarray(n).resize((ancho, alto), Image.BICUBIC))
        return n / (n.std() + 1e-6)

    g = grano * (0.7 * ruido(2) + 0.5 * ruido(12) + 0.4 * ruido(60))       # fibra fina, mota y mancha
    out = np.clip(base + g[:, :, None] + 0.5, 0, 255).astype(np.uint8)
    return Image.fromarray(out)


def papel(ancho=W, alto=H, grano=1.6, vineta=0.55, semilla=1977):
    """Papel crema con textura y viñeta muy suaves. El grano es el mismo en todos los fotogramas (no hormiguea) y
    solo aclara u oscurece unos ±3 niveles; la viñeta lleva las esquinas hacia `papel_sombra`, así que todo queda
    dentro de la paleta. `grano=0, vineta=0` devuelve el papel plano de los shorts 1 y 2."""
    if grano <= 0 and vineta <= 0:
        return Image.new("RGB", (ancho, alto), PAPEL)
    return _papel(ancho, alto, float(grano), float(vineta), semilla).copy()


# ---------------------------------------------------------------- sombras
def sombra_proyectada(img, dx=14, dy=10, radio=10, opacidad=0.22, color=TINTA):
    """Sombra de una capa RGBA: su silueta en tinta, desplazada (dx, dy) y difuminada `radio` px. Devuelve una imagen
    RGBA del mismo tamaño que solo tiene la sombra (se compone debajo de la capa)."""
    a = img.getchannel("A")
    corrida = Image.new("L", img.size, 0)
    corrida.paste(a, (int(round(dx)), int(round(dy))))
    corrida = desenfocar(corrida, radio).point(lambda v: int(v * opacidad))
    out = Image.new("RGBA", img.size, _rgb(color) + (0,))
    out.putalpha(corrida)
    return out


def con_sombra(img, dx=14, dy=10, radio=10, opacidad=0.22, color=TINTA):
    """La imagen RGBA con su sombra proyectada debajo (mismo tamaño: deja margen si la sombra se sale)."""
    return Image.alpha_composite(sombra_proyectada(img, dx, dy, radio, opacidad, color), img)


def sombra_de_suelo(img, y_suelo, aplastado=0.22, sesgo=0.55, radio=7, opacidad=0.20, color=TINTA):
    """Sombra tumbada sobre el suelo: la silueta de la capa aplastada (`aplastado` de su alto) e inclinada (`sesgo`
    px a la derecha por cada px de alto; negativo, a la izquierda), con los pies en `y_suelo` (px de la imagen).
    Devuelve una imagen RGBA del mismo tamaño que solo tiene la sombra."""
    a = img.getchannel("A")
    datos = (1, sesgo / aplastado, -sesgo * y_suelo / aplastado, 0, 1 / aplastado, y_suelo * (1 - 1 / aplastado))
    tumbada = a.transform(a.size, Image.AFFINE, datos, resample=Image.BILINEAR)
    tumbada = desenfocar(tumbada, radio).point(lambda v: int(v * opacidad))
    out = Image.new("RGBA", img.size, _rgb(color) + (0,))
    out.putalpha(tumbada)
    return out


@lru_cache(maxsize=64)
def sombra_contacto(ancho, alto=None, opacidad=0.30, color=TINTA):
    """Sombra de contacto: elipse suave de `ancho` x `alto` px (alto = 22 % del ancho si no se da), más oscura en el
    centro. Devuelve una imagen RGBA con margen para el difuminado; su centro es el centro de la imagen."""
    ancho = int(round(ancho))
    alto = int(round(alto if alto else ancho * 0.22))
    m = int(alto * 0.9) + 6
    L = Image.new("L", (ancho + 2 * m, alto + 2 * m), 0)
    d = ImageDraw.Draw(L)
    d.ellipse([m, m, m + ancho, m + alto], fill=int(255 * opacidad * 0.75))
    d.ellipse([m + ancho * 0.2, m + alto * 0.22, m + ancho * 0.8, m + alto * 0.78], fill=int(255 * opacidad))
    L = L.filter(ImageFilter.GaussianBlur(alto * 0.28 + 2))
    out = Image.new("RGBA", L.size, _rgb(color) + (0,))
    out.putalpha(L)
    return out


# ---------------------------------------------------------------- capas y cámara
@dataclass
class Capa:
    """Una capa de la escena.

    img: imagen RGBA. z: profundidad (0 = plano de los personajes; + lejos; - cerca). (x, y): dónde cae la esquina
    superior izquierda de la imagen, en coordenadas de reposo. esc: píxeles de la imagen por píxel de reposo.
    opacidad: 0 a 1. sombra: None o dict(dx, dy, radio, opacidad) para la sombra proyectada sobre lo que hay detrás.
    fija: pegada a la pantalla (rótulos): no la mueve la cámara ni se desenfoca. niebla / desenfoque: valores fijos
    para esta capa en vez de los que calcula la cámara (None = los de la cámara)."""
    img: Image.Image
    z: float = 0.0
    x: float = 0.0
    y: float = 0.0
    esc: float = 1.0
    opacidad: float = 1.0
    sombra: dict = None
    fija: bool = False
    niebla: float = None
    desenfoque: float = None
    nombre: str = ""


def capa_sombra_contacto(x, y, ancho, z=0.0, opacidad=0.30, alto=None):
    """Capa con una sombra de contacto centrada en (x, y) de reposo (el punto donde el objeto toca el suelo)."""
    img = sombra_contacto(int(round(ancho)), int(round(alto)) if alto else None, round(opacidad, 3))
    return Capa(img, z=z, x=x - img.width / 2, y=y - img.height / 2, nombre="sombra de contacto")


@dataclass
class Camara:
    """Cámara de la escena por capas.

    (x, y): punto del plano z = 0 (en coordenadas de reposo) que queda en el centro del cuadro: moverlo es barrer.
    avance: cuánto se mete la cámara en la escena (empuje real: lo cercano crece más que lo lejano).
    zoom: aumento del objetivo (todo crece igual). foco: la z que se ve nítida. apertura: cuánto se desenfoca lo que
    no está en foco (0 = todo nítido; 0,02 es un valor de trabajo). campo: lo que está a menos de esa distancia del
    plano de foco se ve nítido igual (profundidad de campo). niebla: cuánto se funden con el papel las capas
    lejanas (0 = nada; 0,35 es un valor de trabajo). temblor: (dx, dy) px que se suman al final (sacudida)."""
    x: float = W / 2
    y: float = H / 2
    avance: float = 0.0
    zoom: float = 1.0
    foco: float = 0.0
    apertura: float = 0.0
    niebla: float = 0.0
    temblor: tuple = (0.0, 0.0)
    focal: float = 1000.0
    tam: tuple = (W, H)
    desenfoque_max: float = 60.0
    color_niebla: str = PAPEL
    campo: float = 0.0             # profundidad de campo: lo que está a menos de `campo` del plano de foco se ve nítido

    def proyeccion(self, z):
        """(k, tx, ty): un punto (u, v) de reposo de la capa z se ve en (k * u + tx, k * v + ty). None si la capa
        quedó detrás de la cámara (o pegada a ella)."""
        d = self.focal + z - self.avance
        if d < self.focal * 0.06:
            return None
        p, p0 = self.focal / d, self.focal / (self.focal + z)
        k = self.zoom * p / p0
        w, h = self.tam
        tx = w / 2 + (w / 2 - self.x) * p * self.zoom - k * w / 2 + self.temblor[0]
        ty = h / 2 + (h / 2 - self.y) * p * self.zoom - k * h / 2 + self.temblor[1]
        return k, tx, ty

    def radio_desenfoque(self, z):
        """Radio de desenfoque (px) de la capa z: crece con la distancia al plano de foco y es mayor en lo cercano."""
        if self.apertura <= 0:
            return 0.0
        d = max(self.focal * 0.06, self.focal + z - self.avance)
        fuera = max(0.0, abs(z - self.foco) - self.campo)
        return min(self.desenfoque_max, self.apertura * fuera * self.focal / d * self.zoom)

    def cuanta_niebla(self, z):
        if self.niebla <= 0:
            return 0.0
        return clamp(self.niebla * (z - self.avance) / 1000.0, 0.0, 0.6)


def _proyectar(capa, cam, margen):
    """Lleva la capa al cuadro. Devuelve (imagen RGBA de la región, (x0, y0) de la región en pantalla, k) o None."""
    pr = cam.proyeccion(capa.z)
    if pr is None:
        return None
    k, tx, ty = pr
    w, h = cam.tam
    img, esc = capa.img, capa.esc
    s = esc / k                                   # px de imagen por px de pantalla
    if s >= 1.25:                                 # reducir bien antes de recolocar (el bicúbico solo no promedia)
        nw, nh = max(1, int(round(img.width / s))), max(1, int(round(img.height / s)))
        ex, ey = nw / img.width * esc, nh / img.height * esc
        img = img.resize((nw, nh), Image.LANCZOS)
    else:
        ex = ey = esc
    bx0, by0 = k * capa.x + tx, k * capa.y + ty
    bx1, by1 = bx0 + k * img.width / ex, by0 + k * img.height / ey
    x0, y0 = int(math.floor(max(bx0, 0) - margen)), int(math.floor(max(by0, 0) - margen))
    x1, y1 = int(math.ceil(min(bx1, w) + margen)), int(math.ceil(min(by1, h) + margen))
    if x1 - x0 < 1 or y1 - y0 < 1 or bx1 < -margen or by1 < -margen or bx0 > w + margen or by0 > h + margen:
        return None
    datos = (ex / k, 0, ex * ((x0 - tx) / k - capa.x), 0, ey / k, ey * ((y0 - ty) / k - capa.y))
    region = img.transform((x1 - x0, y1 - y0), Image.AFFINE, datos, resample=Image.BICUBIC)
    return region, (x0, y0), k


def _pegar(base, region, x0, y0):
    """alpha_composite de `region` sobre `base` (RGBA) en (x0, y0), recortando lo que se sale."""
    w, h = base.size
    cx0, cy0 = max(0, -x0), max(0, -y0)
    cx1, cy1 = min(region.width, w - x0), min(region.height, h - y0)
    if cx1 <= cx0 or cy1 <= cy0:
        return
    if (cx0, cy0, cx1, cy1) != (0, 0, region.width, region.height):
        region = region.crop((cx0, cy0, cx1, cy1))
    base.alpha_composite(region, (x0 + cx0, y0 + cy0))


def componer(capas, camara=None, fondo=None, sombras=1.0):
    """Compone la escena: devuelve una imagen RGB del tamaño de la cámara.

    capas: lista de `Capa` (se pintan de la más lejana a la más cercana; las `fija` van al final, en el orden dado).
    camara: `Camara` (por defecto, quieta y con todo nítido). fondo: imagen RGB (por defecto `papel()`).
    sombras: multiplica la opacidad de todas las sombras proyectadas (0 = sin sombras; sirve para hacerlas aparecer).
    Por cada capa: paralaje (escala y desplazamiento según z), niebla hacia el color del papel si está lejos,
    desenfoque según la distancia al plano de foco, y su sombra proyectada."""
    cam = camara or Camara()
    base = (fondo if fondo is not None else papel(*cam.tam)).convert("RGBA")
    orden = sorted((c for c in capas if not c.fija), key=lambda c: -c.z)       # estable: a igual z, el orden dado
    for capa in orden:
        if capa.opacidad <= 0:
            continue
        r = capa.desenfoque if capa.desenfoque is not None else cam.radio_desenfoque(capa.z)
        sm = capa.sombra if (capa.sombra and sombras > 0) else None
        margen = 3 * r + 2
        if sm:
            margen = max(margen, abs(sm["dx"]) + abs(sm["dy"]) + 3 * sm["radio"] + 2)
        pr = _proyectar(capa, cam, margen)
        if pr is None:
            continue
        region, (x0, y0), k = pr
        n = capa.niebla if capa.niebla is not None else cam.cuanta_niebla(capa.z)
        if n > 0:
            a = region.getchannel("A")
            region = Image.blend(region.convert("RGB"), Image.new("RGB", region.size, cam.color_niebla), n)
            region.putalpha(a)
        if r >= 0.35:
            region = desenfocar(region, r)
        if capa.opacidad < 1:
            region.putalpha(region.getchannel("A").point(lambda v: int(v * capa.opacidad)))
        if sm:
            _pegar(base, sombra_proyectada(region, sm["dx"] * k, sm["dy"] * k, sm["radio"] * k + r * 0.5,
                                           sm["opacidad"] * sombras * capa.opacidad), x0, y0)
        _pegar(base, region, x0, y0)
    for capa in capas:
        if capa.fija and capa.opacidad > 0:
            img = capa.img
            if capa.opacidad < 1:
                img = img.copy()
                img.putalpha(img.getchannel("A").point(lambda v: int(v * capa.opacidad)))
            _pegar(base, img, int(round(capa.x)), int(round(capa.y)))
    return base.convert("RGB")


# ---------------------------------------------------------------- transiciones
def revelar_desde_desenfoque(img, p, radio=42.0, respiro=0.05):
    """Revelado desde desenfoque: con p = 0 el plano está borroso (`radio` px), un poco más cerca y lavado hacia el
    papel; con p = 1 queda nítido y en su sitio. Pásale un p lineal: el ease-out va dentro."""
    q = 1 - eo(p)
    if q <= 0.002:
        return img
    out = acercar(img, 1 + respiro * q)
    out = desenfocar(out, radio * q ** 1.4)
    return Image.blend(out, Image.new("RGB", img.size, PAPEL), 0.18 * q)


def barrido_obturador(a, b, p, direccion="derecha", borron_px=90, borde=0.16, empuje=0.12):
    """Barrido de obturador: `b` entra tapando a `a` con un borde blando que cruza el cuadro hacia `direccion`
    ("derecha", "izquierda", "abajo", "arriba"); las dos imágenes se corren un poco y llevan borrón de movimiento en
    esa dirección, y el borde lleva una franja de tinta suave (la hoja del obturador)."""
    if p <= 0:
        return a
    if p >= 1:
        return b
    w, h = a.size
    q = eio(p)
    horizontal = direccion in ("derecha", "izquierda")
    signo = 1 if direccion in ("derecha", "abajo") else -1
    largo = w if horizontal else h
    fuerza = math.sin(math.pi * p)
    da, db = signo * empuje * largo * q, -signo * empuje * largo * (1 - q)
    A = _desplazar(a, da if horizontal else 0, 0 if horizontal else da)
    B = _desplazar(b, db if horizontal else 0, 0 if horizontal else db)
    eje = "h" if horizontal else "v"
    A, B = borron(A, borron_px * fuerza, eje), borron(B, borron_px * fuerza, eje)
    s = borde * largo
    pos = np.arange(largo, dtype=np.float32)
    if signo > 0:                                  # el borde va de -s a largo: detrás de él ya se ve b
        canto = -s + (largo + s) * q
        m = np.clip((pos - canto) / s, 0, 1)       # 1 = todavía a
    else:
        canto = largo + s - (largo + s) * q
        m = np.clip((canto - pos) / s, 0, 1)
    franja = 0.30 * fuerza * np.exp(-((pos - (canto + (s / 2 if signo > 0 else -s / 2))) / (0.35 * s)) ** 2)
    m2 = m[None, :] if horizontal else m[:, None]
    f2 = franja[None, :, None] if horizontal else franja[:, None, None]
    m2 = np.broadcast_to(m2, (h, w))
    out = np.asarray(_mezclar(A, B, m2), dtype=np.float32)
    out = out * (1 - f2) + np.array(TINTA_RGB, dtype=np.float32) * f2
    return Image.fromarray(np.clip(out + 0.5, 0, 255).astype(np.uint8))


def transicion_zoom(a, b, p, cuanto=0.45, centro=None, corte=0.4):
    """Corte con zoom de golpe: hasta `corte`, `a` se acerca acelerando y se emborrona; después `b` llega desde más
    cerca (1 + cuanto) y se asienta en 1 con un muelle."""
    if p < corte:
        u = (p / corte) ** 2
        return desenfocar(acercar(a, 1 + cuanto * u, centro), 10 * u)
    u = (p - corte) / (1 - corte)
    z = 1 + cuanto * 0.6 * (1 - muelle_exacto(u * 0.45, SELLO, 0.45))
    return acercar(b, max(1.0, z), centro) if z >= 1 else acercar(b, z, centro)


def atravesar(a, b, p, centro, radio, zoom_b=0.84):
    """Atravesar la escena: la cámara se mete por un hueco circular de `a` (centro y radio en px de `a`: el agujero de
    un carrete, una ventana redonda) y sale en `b`. `a` crece hasta que el hueco llena el cuadro y se desenfoca al
    acercarse; por el hueco se ve `b`, que llega desde un poco más lejos, con el borde del hueco en sombra."""
    if p <= 0:
        return a
    if p >= 1:
        return b
    w, h = a.size
    q = eio(p)
    z_max = 1.25 * math.hypot(w / 2, h / 2) / radio
    za = z_max ** q
    cx, cy = lerp(centro[0], w / 2, eo(p * 1.5)), lerp(centro[1], h / 2, eo(p * 1.5))
    datos = (1 / za, 0, centro[0] - cx / za, 0, 1 / za, centro[1] - cy / za)
    A = a.transform((w, h), Image.AFFINE, datos, resample=Image.BILINEAR, fillcolor=PAPEL)
    A = desenfocar(A, min(34.0, 2.2 * (za - 1)))
    zb = lerp(zoom_b, 1.0, eo(p))
    B = acercar(b, zb)
    R = radio * za
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.hypot(xx - cx, yy - cy)
    borde = max(1.5, min(30.0, 0.04 * R))
    dentro = np.clip((R - d) / borde, 0, 1) * clamp(p / 0.12)                  # 1 = se ve b
    tunel = 0.38 * np.exp(-np.clip(R - d, 0, None) / (0.16 * R + 1)) * (1 - eo(p)) ** 0.5
    Bf = np.asarray(B, dtype=np.float32)
    Bf = Bf * (1 - tunel[:, :, None]) + np.array(TINTA_RGB, dtype=np.float32) * tunel[:, :, None]
    out = np.asarray(A, dtype=np.float32) * (1 - dentro[:, :, None]) + Bf * dentro[:, :, None]
    return Image.fromarray(np.clip(out + 0.5, 0, 255).astype(np.uint8))


@lru_cache(maxsize=8)
def barra_de_cruce(ancho=520, alto=H + 200, color=TINTA, suave=40):
    """Objeto genérico para `cruce_por_delante`: una franja vertical de tinta con los bordes muy blandos (algo que
    pasa pegado a la cámara, fuera de foco). Devuelve una imagen RGBA."""
    L = Image.new("L", (ancho, alto), 0)
    ImageDraw.Draw(L).rectangle([suave * 2, 0, ancho - suave * 2, alto], fill=255)
    L = L.filter(ImageFilter.GaussianBlur(suave))
    out = Image.new("RGBA", (ancho, alto), _rgb(color) + (0,))
    out.putalpha(L)
    return out


def cruce_por_delante(a, b, p, objeto=None, direccion=1, y=None):
    """Algo cruza por delante y esconde el corte: `objeto` (RGBA, tan alto como el cuadro y opaco en su centro) cruza
    de lado a lado; lo que ya dejó atrás es `b` y lo que le falta por pasar es `a`. La costura va detrás del centro
    del objeto. direccion: 1 = de izquierda a derecha; -1 = al revés."""
    w, h = a.size
    objeto = objeto or barra_de_cruce()
    ow = objeto.width
    q = eio(p)
    x_centro = lerp(-ow / 2, w + ow / 2, q) if direccion > 0 else lerp(w + ow / 2, -ow / 2, q)
    costura = int(round(clamp(x_centro, 0, w)))
    out = a.copy()
    if direccion > 0:
        if costura > 0:
            out.paste(b.crop((0, 0, costura, h)), (0, 0))
    elif costura < w:
        out.paste(b.crop((costura, 0, w, h)), (costura, 0))
    oy = int(round((h - objeto.height) / 2 if y is None else y))
    out.paste(objeto, (int(round(x_centro - ow / 2)), oy), objeto)
    return out


def congelado_con_marco(a, b, p, escala=0.62, giro=-4.0, marco=26, salida=0.68):
    """Congelado como transición: `a` (ya congelada: pásale siempre el mismo fotograma) se encoge hasta `escala`, gana
    un marco de papel blanco y una sombra, gira `giro` grados y queda como una foto sobre `b`, que se ve detrás un poco
    desenfocada; desde p = `salida`, la foto cae fuera del cuadro y `b` queda nítida."""
    w, h = a.size
    u = muelle_exacto(min(p, salida) * 0.5 / salida, SLIDE, 0.5) if p > 0 else 0.0     # 0 -> 1 mientras se encoge
    v = clamp((p - salida) / (1 - salida)) ** 2                                         # 0 -> 1 mientras cae
    s = lerp(1.0, escala, u)
    fondo = desenfocar(b, 7 * (1 - v)) if u > 0 else b
    fondo = Image.blend(a, fondo, clamp(u * 3))
    fw, fh = int(round(w * s)), int(round(h * s))
    m = int(round(marco * clamp(u * 2)))
    foto = Image.new("RGBA", (fw + 2 * m, fh + 2 * m), BLANCO_RGB + (255,))
    foto.paste(a.resize((fw, fh), Image.LANCZOS), (m, m))
    if m > 0:
        ImageDraw.Draw(foto).rectangle([0, 0, foto.width - 1, foto.height - 1], outline=TINTA_RGB + (255,), width=3)
    ang = giro * u + 10 * v
    if abs(ang) > 0.01:
        foto = foto.rotate(-ang, resample=Image.BICUBIC, expand=True)
    px = w / 2 - foto.width / 2
    py = h / 2 - foto.height / 2 + v * (h * 0.5 + foto.height * 0.6)
    out = fondo.convert("RGBA")
    if u > 0.02:
        lienzo = Image.new("RGBA", (foto.width + 120, foto.height + 120), (0, 0, 0, 0))
        lienzo.paste(foto, (60, 60))
        _pegar(out, sombra_proyectada(lienzo, 0, 22 * u, 22, 0.30 * clamp(u * 2)), int(round(px - 60)), int(round(py - 60)))
    _pegar(out, foto, int(round(px)), int(round(py)))
    return out.convert("RGB")


def salida_del_cuadro(a, b, p, direccion="arriba", borron_px=160):
    """Salida del cuadro (latigazo): `a` sale hacia `direccion` ("arriba", "abajo", "izquierda", "derecha") acelerando y
    `b` entra pegada detrás y frena; las dos llevan borrón de movimiento mientras dura."""
    if p <= 0:
        return a
    if p >= 1:
        return b
    w, h = a.size
    q = eio(p)
    horizontal = direccion in ("izquierda", "derecha")
    signo = 1 if direccion in ("derecha", "abajo") else -1
    largo = w if horizontal else h
    d = signo * largo * q
    out = Image.new("RGB", (w, h), PAPEL)
    if horizontal:
        out.paste(a, (int(round(d)), 0))
        out.paste(b, (int(round(d - signo * w)), 0))
    else:
        out.paste(a, (0, int(round(d))))
        out.paste(b, (0, int(round(d - signo * h))))
    return borron(out, borron_px * math.sin(math.pi * p), "h" if horizontal else "v")


# ---------------------------------------------------------------- acentos
OPACIDAD_MAX_DESTELLO = 0.6


@lru_cache(maxsize=16)
def mascara_circulo(cx, cy, r, suave=40.0, tam=(W, H)):
    """Máscara (matriz float de 0 a 1) de un círculo de radio r centrado en (cx, cy), con borde blando de `suave` px."""
    yy, xx = np.mgrid[0:tam[1], 0:tam[0]].astype(np.float32)
    return np.clip((r - np.hypot(xx - cx, yy - cy)) / max(1.0, suave) + 0.5, 0, 1)


def destello(img, f_local, dur=3, opacidad=0.5, mascara=None, color=BLANCO):
    """Destello corto de entrada: mezcla la imagen con el blanco de papel durante `dur` fotogramas (2 a 4) contados
    desde `f_local` = 0, cada vez menos. Nunca es blanco puro ni tapa la imagen: la opacidad se recorta a 0,6.
    mascara: matriz de `mascara_circulo` para que el destello salga de un punto en vez de cubrir todo el cuadro."""
    dur = int(clamp(dur, 2, 4))
    if f_local < 0 or f_local >= dur:
        return img
    op = min(opacidad, OPACIDAD_MAX_DESTELLO) * (1 - f_local / dur) ** 1.3
    if mascara is None:
        return Image.blend(img, Image.new("RGB", img.size, color), op)
    return _mezclar(Image.new("RGB", img.size, color), img, mascara * op)


_D = np.array(PAPEL_RGB, dtype=np.float32) - np.array(TINTA_RGB, dtype=np.float32)


def negativo_paleta(img, mascara=None, mezcla=1.0):
    """Negativo dentro de la paleta: la tinta pasa a papel y el papel a tinta; los colores conservan su tono (se
    invierte solo su posición entre tinta y papel), así que nada se vuelve azul ni blanco puro. mascara: matriz de 0 a
    1 (`mascara_circulo`) para limitarlo a una zona: a pantalla completa es un salto de luz grande y
    `comprobar_destellos` lo rechaza. mezcla: 0 a 1."""
    a = np.asarray(img, dtype=np.float32)
    tinta = np.array(TINTA_RGB, dtype=np.float32)
    t = np.clip(((a - tinta) @ _D) / float(_D @ _D), 0.0, 1.0)     # nada queda más oscuro que la tinta
    neg = np.clip(a + (1 - 2 * t)[:, :, None] * _D, 0, 255)
    m = mezcla if mascara is None else (mascara * mezcla)[:, :, None]
    return Image.fromarray(np.clip(a * (1 - m) + neg * m + 0.5, 0, 255).astype(np.uint8))


def trazo_subrayado(x0, x1, y, caida=7.0, doble=False):
    """Trazo de subrayado de x0 a x1 a la altura y (un poco curvo). doble=True vuelve con una segunda pasada."""
    ida = [(lerp(x0, x1, i / 12), y + caida * math.sin(math.pi * i / 12) - caida * 0.4 * i / 12) for i in range(13)]
    if not doble:
        return [ida]
    vuelta = [(lerp(x1 - 12, x0 + 30, i / 10), y + 16 + caida * 0.6 * math.sin(math.pi * i / 10)) for i in range(11)]
    return [ida + vuelta]


def trazo_circulo(cx, cy, rx, ry, vueltas=1.1, inicio=-115.0):
    """Trazo de un círculo (elipse) dibujado a mano: da algo más de una vuelta y termina por fuera de donde empezó."""
    n = 56
    pts = []
    for i in range(n + 1):
        u = i / n
        a = math.radians(inicio + 360 * vueltas * u)
        k = 1 + 0.07 * u
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    return [pts]


def trazo_flecha(p0, p1, curva=0.18, punta=38.0):
    """Trazos de una flecha curva de p0 a p1: el cuerpo y la punta (dos rayas)."""
    (x0, y0), (x1, y1) = p0, p1
    dx, dy = x1 - x0, y1 - y0
    cxm, cym = (x0 + x1) / 2 - dy * curva, (y0 + y1) / 2 + dx * curva
    cuerpo = []
    for i in range(21):
        u = i / 20
        cuerpo.append(((1 - u) ** 2 * x0 + 2 * u * (1 - u) * cxm + u * u * x1,
                       (1 - u) ** 2 * y0 + 2 * u * (1 - u) * cym + u * u * y1))
    ang = math.atan2(y1 - cym, x1 - cxm)
    cabeza = [(x1 - punta * math.cos(ang + s * 0.5), y1 - punta * math.sin(ang + s * 0.5)) for s in (-1, 1)]
    return [cuerpo, [cabeza[0], (x1, y1), cabeza[1]]]


def garabato(base, trazos, p, grosor=9.0, color=TINTA, semilla=1, temblor=2.5):
    """Garabato de tinta que se dibuja solo: pinta sobre `base` (imagen RGB o RGBA, se modifica y se devuelve) la
    fracción p (0 a 1) del largo total de `trazos` (lista de polilíneas en px), con pulso de mano: un temblor fijo
    que depende de la semilla, no del fotograma (no hormiguea)."""
    if p <= 0:
        return base
    fino = []
    total = 0.0
    for pts in trazos:                                   # remuestrear cada trazo a pasos de unos 6 px
        linea = [pts[0]]
        for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
            n = max(1, int(math.hypot(xb - xa, yb - ya) / 6))
            linea += [(lerp(xa, xb, i / n), lerp(ya, yb, i / n)) for i in range(1, n + 1)]
        fino.append(linea)
        total += sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(linea, linea[1:]))
    limite, hecho = total * clamp(p), 0.0
    visibles = []
    f1, f2 = 0.7 * semilla + 0.3, 1.9 * semilla + 1.1
    for linea in fino:
        if hecho >= limite:
            break
        s, corte = hecho, [None]
        for i, (x, y) in enumerate(linea):
            if i:
                s += math.hypot(x - linea[i - 1][0], y - linea[i - 1][1])
            if s > limite:
                break
            corte.append((x + temblor * (math.sin(0.021 * s + f1) + 0.5 * math.sin(0.063 * s + f2)),
                          y + temblor * (math.cos(0.017 * s + f2) + 0.5 * math.sin(0.051 * s + f1))))
        hecho = max(s, hecho)
        if len(corte) > 2:
            visibles.append(corte[1:])
    if not visibles:
        return base
    xs = [q[0] for ln in visibles for q in ln]
    ys = [q[1] for ln in visibles for q in ln]
    m = grosor + 4
    x0, y0 = int(min(xs) - m), int(min(ys) - m)
    cw, ch = int(max(xs) + m) - x0 + 1, int(max(ys) + m) - y0 + 1
    capa = Image.new("RGBA", (cw * SS, ch * SS), _rgb(color) + (0,))
    d = ImageDraw.Draw(capa)
    wpx = max(1, int(round(grosor * SS)))
    relleno = _rgb(color) + (255,)
    for ln in visibles:
        P = [((x - x0) * SS, (y - y0) * SS) for x, y in ln]
        d.line(P, fill=relleno, width=wpx, joint="curve")
        for q in (P[0], P[-1]):
            d.ellipse([q[0] - wpx / 2, q[1] - wpx / 2, q[0] + wpx / 2, q[1] + wpx / 2], fill=relleno)
    capa = capa.resize((cw, ch), Image.LANCZOS)
    base.paste(capa, (x0, y0), capa)
    return base


# ---------------------------------------------------------------- texto
TRAZO_EM = 0.045            # contorno de tinta de la palabra clave (norma del canal desde el short 2)
RASGOS = ["ss01"]           # dígitos abiertos de Inter
CON_TRAZO = (MOSTAZA, TOMATE)


def T(s):
    """Segmento de texto en tinta."""
    return (s, TINTA)


def K(s):
    """Segmento en mostaza con contorno de tinta: la palabra clave."""
    return (s, MOSTAZA)


def R(s):
    """Segmento en tomate con contorno: solo la cifra final."""
    return (s, TOMATE)


@lru_cache(maxsize=64)
def fuente(tam):
    return ImageFont.truetype(FUENTE, tam)


def comprobar_glifos(textos):
    """Ningún cuadrado: cada carácter que se usa tiene que estar en la fuente. Devuelve los caracteres usados."""
    f = fuente(120)
    vacio = bytes(f.getmask("￿"))
    usados = sorted(set("".join(textos)) - {" "})
    faltan = [c for c in usados if bytes(f.getmask(c)) == vacio or f.getmask(c).getbbox() is None]
    if faltan:
        sys.exit(f"La fuente no tiene estos caracteres: {faltan}")
    return usados


def _largo(f, s):
    return f.getlength(s, features=RASGOS)


def _avances(f, s, col, tam):
    if col in CON_TRAZO:                       # espacio extra entre letras del ancho del trazo: los contornos no se pegan
        extra = TRAZO_EM * tam * SS
        return [_largo(f, c) + (extra if i < len(s) - 1 else 0) for i, c in enumerate(s)]
    return [_largo(f, s)]


def ancho_texto(segs, tam):
    """Ancho en px del texto `segs` (tupla de segmentos T/K/R) a `tam` px de cuerpo."""
    f = fuente(int(round(tam * SS)))
    return sum(sum(_avances(f, s, col, tam)) for s, col in segs) / SS


@lru_cache(maxsize=512)
def imagen_texto(segs, tam):
    """segs: tupla de (texto, color). Devuelve (imagen RGBA x3, margen, línea base). Mostaza y tomate llevan contorno
    de tinta de 0,045 em y los dígitos son los abiertos de Inter (ss01), como en el short 2."""
    f = fuente(int(round(tam * SS)))
    sw = max(1, int(round(TRAZO_EM * tam * SS)))
    asc, desc = f.getmetrics()
    margen = sw + 4
    ancho = int(ancho_texto(segs, tam) * SS) + 2 * margen + 4
    img = Image.new("RGBA", (ancho, asc + desc + 2 * margen), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x = float(margen)
    for s, col in segs:
        if col in CON_TRAZO:
            for c, av in zip(s, _avances(f, s, col, tam)):
                d.text((x, margen + asc), c, font=f, fill=col, anchor="ls", stroke_width=sw, stroke_fill=TINTA,
                       features=RASGOS)
                x += av
        else:
            d.text((x, margen + asc), s, font=f, fill=col, anchor="ls", features=RASGOS)
            x += _largo(f, s)
    return img, margen, margen + asc


def poner_texto(base, segs, x, tope, tam, esc=1.0, alfa=1.0):
    """Pega el texto sobre `base` (RGB o RGBA), alineado a la izquierda en x y con el tope de las letras altas en
    `tope`. esc escala alrededor del borde izquierdo y la media altura de las minúsculas (para el pop); alfa 0 a 1."""
    if alfa <= 0:
        return base
    img, margen, linea = imagen_texto(tuple(segs), tam)
    k = esc / SS
    chico = img.resize((max(1, int(round(img.width * k))), max(1, int(round(img.height * k)))), Image.LANCZOS)
    ancla_y = tope + 0.74 * tam - 0.30 * tam
    y = ancla_y - (linea - 0.30 * tam * SS) * k
    if alfa < 1:
        chico.putalpha(chico.getchannel("A").point(lambda v: int(v * alfa)))
    base.paste(chico, (int(round(x - margen * k)), int(round(y))), chico)
    return base


def palabra_clave(base, segs, x, tope, tam, t, kc=POP):
    """Texto con palabra clave (segmento K, mostaza con contorno) que entra con un pop de muelle de 0,85 a 1 y un
    fundido de 2 fotogramas. t: segundos desde que entra."""
    if t < 0:
        return base
    return poner_texto(base, segs, x, tope, tam, esc=0.85 + 0.15 * muelle(t, kc), alfa=min(1.0, t * FPS / 2 + 0.5))


@lru_cache(maxsize=64)
def _mascara_redonda(w, h, radio):
    L = Image.new("L", (w * 2, h * 2), 0)
    ImageDraw.Draw(L).rounded_rectangle([0, 0, w * 2 - 1, h * 2 - 1], radius=radio * 2, fill=255)
    return L.resize((w, h), Image.LANCZOS)


def panel_vidrio(base, caja, radio=26, desenfoque=14, tinte=0.46, alfa=1.0, sombra=True):
    """Panel de «vidrio» al estilo del canal: dentro de `caja` (x0, y0, x1, y1) lo que hay detrás se desenfoca y se
    aclara hacia el blanco de papel; lleva un filo de tinta fino y una sombra suave debajo. No brilla ni tiene
    degradado: es papel vegetal. Modifica `base` (RGB) y la devuelve. alfa: 0 a 1 (para hacerlo entrar)."""
    if alfa <= 0:
        return base
    x0, y0, x1, y1 = (int(round(v)) for v in caja)
    w, h = x1 - x0, y1 - y0
    if w < 4 or h < 4:
        return base
    m = int(desenfoque * 3) + 4
    if sombra:
        s = sombra_contacto(int(w * 0.96), max(8, int(h * 0.30)), round(0.20 * alfa, 3))
        base.paste(s, (int(x0 + w / 2 - s.width / 2), int(y1 - s.height / 2 - h * 0.02)), s)
    zona = (max(0, x0 - m), max(0, y0 - m), min(base.width, x1 + m), min(base.height, y1 + m))
    detras = desenfocar(base.crop(zona), desenfoque).crop((x0 - zona[0], y0 - zona[1], x1 - zona[0], y1 - zona[1]))
    detras = Image.blend(detras, Image.new("RGB", detras.size, BLANCO), tinte)
    filo = ImageDraw.Draw(detras)
    r = int(min(radio, w / 2, h / 2))
    mascara = _mascara_redonda(w, h, r)
    filo.rounded_rectangle([0, 0, w - 1, h - 1], radius=r, outline=TINTA, width=3)
    if alfa < 1:
        mascara = mascara.point(lambda v: int(v * alfa))
    base.paste(detras, (x0, y0), mascara)
    return base


def texto_vidrio(base, segs, x, tope, tam, alfa=1.0, esc=1.0, relleno_x=0.55, relleno_y=0.42, ancho=None):
    """Texto sobre su panel de vidrio: el panel se ajusta al texto (o a `ancho` px si se da, para que no cambie de
    tamaño con un contador). (x, tope): borde izquierdo y tope de las letras altas del texto. Devuelve la caja."""
    aw = ancho if ancho is not None else ancho_texto(tuple(segs), tam)
    caja = (x - relleno_x * tam, tope - relleno_y * tam, x + aw + relleno_x * tam, tope + 0.74 * tam + relleno_y * tam + 0.1 * tam)
    if esc != 1.0:
        cx, cy = (caja[0] + caja[2]) / 2, (caja[1] + caja[3]) / 2
        caja = (cx + (caja[0] - cx) * esc, cy + (caja[1] - cy) * esc, cx + (caja[2] - cx) * esc, cy + (caja[3] - cy) * esc)
    panel_vidrio(base, caja, radio=int(0.36 * tam), alfa=alfa)
    poner_texto(base, segs, x, tope, tam, alfa=alfa)
    return caja


def contador(t, t0, t1, a, b):
    """Contador: entero entre a y b con ease-out cúbico entre los segundos t0 y t1; solo sube y nunca pasa de b."""
    return a + int(round((b - a) * eo((t - t0) / (t1 - t0))))


def titulares_en_cascada(base, titulares, t, x, tope, tam, cada=0.12, paso=None, corrimiento=34):
    """Titulares en cascada: cada titular (tupla de segmentos) entra `cada` segundos después del anterior, cayendo
    desde arriba con muelle, en su panel de vidrio; cada uno queda `paso` px más abajo y `corrimiento` px más a la
    derecha que el anterior. t: segundos desde que entra el primero. Devuelve las cajas."""
    paso = paso if paso is not None else 1.75 * tam
    cajas = []
    for i, segs in enumerate(titulares):
        ti = t - i * cada
        if ti < 0:
            break
        u = muelle(ti, SLIDE)
        y = tope + i * paso - (1 - u) * 0.9 * tam
        cajas.append(texto_vidrio(base, segs, x + i * corrimiento, y, tam, alfa=clamp(ti * FPS / 3 + 0.34)))
    return cajas


def rotulo(base, s, x=SEG_X0 + 8, tope=SEG_Y0 + 20, tam=42):
    """Rótulo pequeño dentro de la zona segura, arriba a la izquierda, sobre una pastilla de papel blanco con filo de
    tinta (se lee sobre cualquier plano). Para pruebas y notas técnicas, no para el video publicado."""
    segs = (T(s),)
    aw = ancho_texto(segs, tam)
    caja = [int(x), int(tope - 0.34 * tam), int(x + aw + 0.9 * tam), int(tope + 0.74 * tam + 0.44 * tam)]
    capa = Image.new("RGBA", ((caja[2] - caja[0]) * 2, (caja[3] - caja[1]) * 2), (0, 0, 0, 0))
    ImageDraw.Draw(capa).rounded_rectangle([0, 0, capa.width - 1, capa.height - 1], radius=int(0.4 * tam) * 2,
                                           fill=BLANCO_RGB + (242,), outline=TINTA_RGB + (255,), width=5)
    capa = capa.resize((caja[2] - caja[0], caja[3] - caja[1]), Image.LANCZOS)
    base.paste(capa, (caja[0], caja[1]), capa)
    poner_texto(base, segs, x + 0.45 * tam, tope, tam)
    return base


# ---------------------------------------------------------------- firma del canal: el lápiz bumerán (1.1)
# Especificación: canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md (secciones 2, 3, 4 y 9). Todo depende de `c`:
# c = 0 es el fotograma 0 del video; c = -1 el último. Cierre: c -30 a -1. Apertura: c 0 a 30.
class FirmaError(ValueError):
    """La portada no deja pasillo para el vuelo del lápiz, o se pidió una variante que no está escrita."""


_R_PRUEBA, _X_PRUEBA, _SUELO_PRUEBA = 88.0651, 259.0, 1651.0          # plano de prueba de la especificación (§2.1)
# Punto de mano H (1.1, corregido tras la vuelta 1 del short 3): con la pose `saluda` (100°, 155°) la mano queda a
# 1,07 R del eje de Tan, pegada a la mejilla, y el lápiz cruzaba la cara al soltarlo y al atraparlo. El brazo de la
# firma va ahora más abierto, BD_FIRMA = (95°, 108°): mano en (x + 1,46 R; suelo − 3,17 R) y centro del lápiz
# H = (x + 1,51 R; suelo − 3,42 R). Los puntos de control guardan su forma respecto de H y de S.
BD_FIRMA, BD_ATRAS = (95.0, 108.0), (-25.0, 20.0)
BD_SALUDA = BD_FIRMA                                # nombre anterior, por compatibilidad
_H_PRUEBA = (259.0 + (0.78 * math.sin(math.radians(95)) + 0.72 * math.sin(math.radians(108)) + 0.05) * 88.0651,
             1651.0 + (-2.88 + 0.78 * math.cos(math.radians(95)) + 0.72 * math.cos(math.radians(108)) - 0.25) * 88.0651)
_B1_PRUEBA = (_H_PRUEBA, (_H_PRUEBA[0] + 110.0, _H_PRUEBA[1] - 10.0), (570.0, 1165.0), (585.0, 1235.0))     # ida: H -> S
_B2_PRUEBA = ((585.0, 1235.0), (597.0, 1290.0), (_H_PRUEBA[0] + 95.0, _H_PRUEBA[1] + 40.0), _H_PRUEBA)    # vuelta: S -> H
F_ANTICIPA, F_IMPULSO, F_SUELTA, F_ATRAPA = -24, -19, -15, 10
MUELLE_LAPIZ = (560.0, 10.0)


def impulso_muelle(t, kc=POP):
    """Respuesta de un muelle a un impulso, normalizada a 1 en su pico (sube, se pasa y se apaga). t en segundos."""
    if t <= 0:
        return 0.0
    k, c = kc
    w0 = math.sqrt(k)
    z = c / (2 * math.sqrt(k))
    wd = w0 * math.sqrt(1 - z * z)
    tp = math.atan2(wd, z * w0) / wd
    return math.exp(-z * w0 * t) * math.sin(wd * t) / (math.exp(-z * w0 * tp) * math.sin(wd * tp))


def _bezier(P, t):
    u = 1 - t
    return (u ** 3 * P[0][0] + 3 * u * u * t * P[1][0] + 3 * u * t * t * P[2][0] + t ** 3 * P[3][0],
            u ** 3 * P[0][1] + 3 * u * u * t * P[1][1] + 3 * u * t * t * P[2][1] + t ** 3 * P[3][1])


def _vuelo(c, geo):
    """(x, y, escala, ángulo) del lápiz en vuelo en el fotograma c (puede llevar decimales): -15 <= c <= 10."""
    if c < 0:
        u = clamp((c - F_SUELTA) / float(-F_SUELTA))
        x, y = _bezier(geo["B1"], 0.65 * (1 - (1 - u) ** 2) + 0.35 * u)
        return x, y, 1 + (geo["s_max"] - 1) * (1 - (1 - u) ** 2), -30 + 220 * (0.75 * (1 - (1 - u) ** 2) + 0.25 * u)
    u = clamp(c / float(F_ATRAPA))
    x, y = _bezier(geo["B2"], 0.753 * eio(u) + 0.247 * u)
    return x, y, geo["s_max"] - (geo["s_max"] - 1) * eio(u), 190 + 110 * (0.666 * eio(u) + 0.334 * u)


def _eje_lapiz(x, y, esc, ang, R):
    """Extremos (goma, punta) del lápiz de `palitos.lapiz` y su medio ancho con contorno, en px."""
    a = math.radians(ang)
    L = 0.95 * R * esc
    dx, dy = math.cos(a) * L, math.sin(a) * L
    return (x - dx * 0.62, y - dy * 0.62), (x + dx * 0.72, y + dy * 0.72), (0.08 + 0.02) * R * esc


def _dist_caja(p, caja):
    dx = max(caja[0] - p[0], 0.0, p[0] - caja[2])
    dy = max(caja[1] - p[1], 0.0, p[1] - caja[3])
    return math.hypot(dx, dy)


def _despeje(x, y, esc, ang, R, caja):
    """Distancia (px) del lápiz a una caja (x0, y0, x1, y1); 0 si la toca."""
    g, p, m = _eje_lapiz(x, y, esc, ang, R)
    return max(0.0, min(_dist_caja((lerp(g[0], p[0], i / 12), lerp(g[1], p[1], i / 12)), caja) for i in range(13)) - m)


def geometria_firma(portada, atrapa="tan", subir=0.0, dx_cuerpo=1.0):
    """Puntos del vuelo a partir de las medidas de la portada del video.

    portada: {"R", "x_tan", "x_tin", "suelo", "texto": caja, "objeto": caja, "cara_tan": caja, "cara_tin": caja}
    (cajas x0, y0, x1, y1 medidas en el fotograma 0; Tan de perfil con `mira=1` y sin espejo). subir: px que sube el
    lazo (S y los puntos de control; la mano no) si el pasillo lo pide (±40 como mucho, §5.1). dx_cuerpo: factor del
    desplazamiento del cuerpo de Tan que aplica el render (1 = el de la especificación).
    Devuelve {"H", "S", "B1", "B2", "R", "s_max", "zona_util", "paso_libre", "portada"}. Falla con FirmaError si en
    algún fotograma del vuelo el lápiz queda a menos de 30 px del texto o del objeto, o si en algún fotograma de la
    firma (en la mano o en vuelo) queda a menos de 8 px de una cabeza."""
    if atrapa != "tan":
        raise FirmaError("Solo está escrita la variante de partida (atrapa Tan); atrapa='tin' es la §4.3, sin programar.")
    R, k = float(portada["R"]), float(portada["R"]) / _R_PRUEBA

    def pt(q, mueve=True):
        return (portada["x_tan"] + (q[0] - _X_PRUEBA) * k, portada["suelo"] + (q[1] - _SUELO_PRUEBA) * k - (subir if mueve else 0.0))
    H = pt(_B1_PRUEBA[0], False)
    B1 = (H, pt(_B1_PRUEBA[1]), pt(_B1_PRUEBA[2]), pt(_B1_PRUEBA[3]))
    B2 = (B1[3], pt(_B2_PRUEBA[1]), pt(_B2_PRUEBA[2]), H)
    geo = {"H": H, "S": B1[3], "B1": B1, "B2": B2, "R": R, "s_max": 1.7, "zona_util": (60, 380, 960, 1440),
           "suelo": float(portada["suelo"]), "portada": dict(portada), "dx_cuerpo": dx_cuerpo}
    geo["paso_libre"] = (portada["cara_tan"][2], portada["objeto"][3], portada["cara_tin"][0], portada["cara_tan"][3])
    inf = _despejes(geo)
    if inf["texto_min"] < 30 or inf["objeto_min"] < 30 or inf["caras_min"] < 8:
        raise FirmaError(f"La portada no deja pasillo para el lápiz: {inf}")
    return geo


def _dist_circulo(x, y, esc, ang, R, cx, cy, r):
    """Distancia (px) del lápiz a un círculo de centro (cx, cy) y radio r; negativa si lo pisa."""
    g, p, m = _eje_lapiz(x, y, esc, ang, R)
    return min(math.hypot(lerp(g[0], p[0], i / 16) - cx, lerp(g[1], p[1], i / 16) - cy) for i in range(17)) - m - r


def cabezas_firma(c, geo):
    """Círculos (cx, cy, r) de las cabezas de Tan y de Tin en el fotograma c del plano de firma, con su inclinación
    (la cabeza gira alrededor de la base del cuello). Radio de Tan: 1,04 R (contorno); el de Tin, 1,04 R más la
    visera, que se mide aparte como un segundo círculo hacia el frente."""
    R, por = geo["R"], geo["portada"]
    base = por["suelo"] - 3.28 * R
    a = math.radians(_cuerpo_tan(c)[3])
    dx = _cuerpo_tan(c)[1] * geo.get("dx_cuerpo", 1.0)
    # al levantar la cara la cabeza se echa hacia atrás: el centro se aleja del lado al que mira
    tan = (por["x_tan"] + dx - R * math.sin(a), base - R * math.cos(a), 1.04 * R)
    b = math.radians(25.0)
    tin = (por["x_tin"] + R * math.sin(b), base - R * math.cos(b), 1.04 * R)
    visera = (tin[0] - 1.0 * R, tin[1] - 0.35 * R, 0.30 * R)
    return tan, tin, visera


def _despejes(geo):
    """Despejes mínimos del lápiz EN TODOS los fotogramas de la firma (c = -30 a 30, en la mano y en vuelo): al texto
    y al objeto (cajas de la portada) y a las cabezas (círculos de `cabezas_firma`; negativo = las pisa)."""
    por = geo["portada"]
    d = {"texto_min": 1e9, "objeto_min": 1e9, "cabeza_tan_min": 1e9, "cabeza_tin_min": 1e9, "centro_en_zona_util": True}
    zu = geo["zona_util"]
    peor = {}
    for c in range(-30, 31):
        if F_SUELTA <= c < F_ATRAPA:
            x, y, s, a = _vuelo(c, geo)
        else:
            bd, dx, giro, _ = _cuerpo_tan(c)
            R = geo["R"]
            mx = por["x_tan"] + dx * geo.get("dx_cuerpo", 1.0) + (0.78 * math.sin(math.radians(bd[0])) + 0.72 * math.sin(math.radians(bd[1])) + 0.05) * R
            my = por["suelo"] + (-2.88 + 0.78 * math.cos(math.radians(bd[0])) + 0.72 * math.cos(math.radians(bd[1])) - 0.25) * R
            x, y, s, a = mx, my, 1.0, -60.0 + giro
        tan, tin, visera = cabezas_firma(c, geo)
        if F_SUELTA <= c < F_ATRAPA:
            d["texto_min"] = min(d["texto_min"], _despeje(x, y, s, a, geo["R"], por["texto"]))
            d["objeto_min"] = min(d["objeto_min"], _despeje(x, y, s, a, geo["R"], por["objeto"]))
            d["centro_en_zona_util"] &= zu[0] <= x <= zu[2] and zu[1] <= y <= zu[3]
        dt = _dist_circulo(x, y, s, a, geo["R"], *tan)
        if dt < d["cabeza_tan_min"]:
            d["cabeza_tan_min"], peor["cabeza_tan_en_c"] = dt, c
        dn = min(_dist_circulo(x, y, s, a, geo["R"], *tin), _dist_circulo(x, y, s, a, geo["R"], *visera))
        if dn < d["cabeza_tin_min"]:
            d["cabeza_tin_min"], peor["cabeza_tin_en_c"] = dn, c
    d["caras_min"] = min(d["cabeza_tan_min"], d["cabeza_tin_min"])
    out = {k: (round(v, 1) if isinstance(v, float) else v) for k, v in d.items()}
    out.update(peor)
    return out


def _cuerpo_tan(c):
    """(bd, dx, giro_objeto, cabeza_giro) de Tan en el fotograma c (decimales permitidos)."""
    if c < 0:
        if c < F_ANTICIPA:
            return BD_SALUDA, 0.0, 0.0, 25.0
        if c <= F_IMPULSO:
            p = eo((c - F_ANTICIPA) / 5.0)
            return (lerp(BD_SALUDA[0], BD_ATRAS[0], p), lerp(BD_SALUDA[1], BD_ATRAS[1], p)), -8 * p, -40 * p, 25 * (1 - p)
        if c < F_SUELTA:
            p = ((c - F_IMPULSO) / 4.0) ** 3
            return (lerp(BD_ATRAS[0], BD_SALUDA[0], p), lerp(BD_ATRAS[1], BD_SALUDA[1], p)), lerp(-8, 10, p), lerp(-40, 30, p), 0.0
        t = (c - F_SUELTA) / 30.0
        im = impulso_muelle(t, POP)
        return (BD_SALUDA[0] + 12 * im, BD_SALUDA[1] + 13 * im), 10 * (1 - muelle(t, SLIDE)), 0.0, 25 * eio((c - F_SUELTA) / 15.0)
    if c < F_ATRAPA:
        return BD_SALUDA, 0.0, 0.0, 25 * (1 - eio((c - 2) / 8.0)) if c > 2 else 25.0
    t = (c - F_ATRAPA) / 30.0
    im = impulso_muelle(t, POP)
    cab = 25 * eio((c - 14) / 8.0)
    return (BD_SALUDA[0] - 10 * im, BD_SALUDA[1] - 10 * im), -6 * (1 - muelle(t, SLIDE)), 14 * (1 - muelle(t, MUELLE_LAPIZ)), cab


def lapiz_bumeran(c, geo, variante="bucle"):
    """Estado de la firma en el fotograma `c` (función pura, no dibuja). c < 0: cierre (reposo desde -30, anticipación
    -24 a -19, impulso -19 a -15, suelta en -15, vuelo de ida hasta 0); c >= 0: apertura (vuelo de vuelta 0 a 10,
    contacto en 10, asentado hacia 25). Devuelve:
      {"c", "fase", "lapiz": {"visible", "en_mano", "x", "y", "esc", "angulo", "v", "omega"},
       "tan": {"pose": dict para `palitos.dibujar`, "dx": px, "expresion": str o None (None = la de la portada),
               "cabeza_giro", "giro_objeto", "objeto": "lapiz" o False, "viento"},
       "tin": {"dy": px, "objeto": False, "cabeza_giro": 25.0}}
    El lápiz «en_mano» lo dibuja `palitos.dibujar` (objeto="lapiz"); en vuelo, `pintar_lapiz_volador`."""
    if variante != "bucle":
        raise FirmaError("Solo está escrita la variante «bucle»; «sin retorno» (§4.2) no está programada.")
    bd, dx, giro, cab = _cuerpo_tan(c)
    dx_antes = _cuerpo_tan(c - 1)[1]
    volando = F_SUELTA <= c < F_ATRAPA
    if c < F_ANTICIPA:
        fase = "reposo"
    elif c <= F_IMPULSO and c < 0:
        fase = "anticipacion"
    elif c < F_SUELTA:
        fase = "impulso"
    elif c < 0:
        fase = "vuelo de ida"
    elif c < F_ATRAPA:
        fase = "vuelo de vuelta"
    else:
        fase = "atrapada" if c < 25 else "reposo"
    if volando:
        x, y, esc, ang = _vuelo(c, geo)
        x2, y2, _, ang2 = _vuelo(min(c + 1, F_ATRAPA) if c + 1 <= F_ATRAPA else c, geo)
        v, om = math.hypot(x2 - x, y2 - y), ang2 - ang
    else:
        (x, y), esc, ang, v, om = geo["H"], 1.0, -60.0 + giro, 0.0, 0.0      # (x, y) se afina abajo, con la pose
    pose = dict(palitos.POSES["saluda"], bd=bd, objeto_arriba=True)
    if not volando:                                   # el lápiz en la mano: donde lo dibuja `palitos` con ese brazo
        (mx, my), _ = palitos.mano_de(geo["portada"]["x_tan"] + dx * geo.get("dx_cuerpo", 1.0), geo["suelo"],
                                      geo["R"] * 5.53, pose, "perfil", 1)
        x, y = mx + 0.05 * geo["R"], my - 0.25 * geo["R"]
    return {"c": c, "fase": fase,
            "lapiz": {"visible": True, "en_mano": not volando, "x": x, "y": y, "esc": esc, "angulo": ang, "v": v, "omega": om},
            "tan": {"pose": pose, "dx": dx, "expresion": "concentrado" if F_ANTICIPA <= c <= -16 else None,
                    "cabeza_giro": cab, "giro_objeto": giro, "objeto": False if volando else "lapiz",
                    "viento": clamp(-0.06 * (dx - dx_antes), -0.8, 0.8)},
            "tin": {"dy": -5 * impulso_muelle((c - F_ATRAPA) / 30.0, POP) if c >= F_ATRAPA else 0.0, "objeto": False,
                    "cabeza_giro": 25.0}}


def pintar_lapiz_volador(est, geo, fps=FPS, obturador=0.5):
    """Las `Capa` del lápiz en vuelo para `componer`: la sombra de suelo y el lápiz (con su sombra proyectada). El
    desenfoque de movimiento es de obturador: el lápiz se pinta en n subpasos dentro de medio fotograma y se promedian
    con alfa premultiplicado (n = 1 + v/10, de 1 a 6). Devuelve [] si el lápiz está en la mano."""
    lp = est["lapiz"]
    if lp["en_mano"] or not lp["visible"]:
        return []
    c, R = est["c"], geo["R"]
    n = int(clamp(round(1 + lp["v"] / 4.0), 1, 16))      # 1.1b: más subpasos (con 6 se veía un abanico de copias)
    pasos = [_vuelo(clamp(c + obturador * ((i + 0.5) / n - 0.5), F_SUELTA, F_ATRAPA), geo) for i in range(n)]
    m = 1.0 * R * geo["s_max"] + 8
    x0, y0 = int(min(q[0] for q in pasos) - m), int(min(q[1] for q in pasos) - m)
    w, h = int(max(q[0] for q in pasos) + m) - x0, int(max(q[1] for q in pasos) + m) - y0
    suma = np.zeros((h, w, 4), dtype=np.float32)
    for x, y, s, a in pasos:
        lz = LienzoCapa(w, h)
        palitos.lapiz(palitos.Pluma(lz, x - x0, y - y0, R * s), 0, 0, angulo=a)
        suma += np.asarray(lz.resultado().convert("RGBa"), dtype=np.float32)
    img = Image.fromarray(np.clip(suma / n + 0.5, 0, 255).astype(np.uint8), "RGBa").convert("RGBA")
    s = lp["esc"]
    k = (s - 1) / (geo["s_max"] - 1)
    capa = Capa(img, z=1000.0 / s - 1000.0, x=x0, y=y0, niebla=0.0, desenfoque=0.0, nombre="lápiz bumerán",
                sombra=dict(dx=14 * s, dy=10 * s, radio=10 * s, opacidad=0.22 - 0.07 * k))
    suelo = capa_sombra_contacto(lp["x"], geo["suelo"], 90 + 50 * k, z=0.0, opacidad=0.26 - 0.12 * k)
    suelo.niebla, suelo.desenfoque = 0.0, 0.0
    return [suelo, capa]


def golpes_firma(N, voz_entra=14):
    """Sonidos de la firma (§7): lista de (fotograma, nombre, pico en dBFS, duración en fotogramas). N = fotogramas
    del video. El whoosh es uno solo que atraviesa el empalme (ida y vuelta al mismo nivel, -34 dBFS, en c = 0)."""
    if voz_entra < 14:
        raise FirmaError("La voz de Tan entra en el fotograma 14 como mínimo (§5.2).")
    return [(N - 17, "chasquido de brazo y suelta", -20.0, 3), (N - 15, "whoosh de ida", -20.0, 15),
            (0, "whoosh de regreso", -18.0, 10), (F_ATRAPA, "golpe de atrapada", -12.0, 4)]


def comprobar_firma(geo, N=None):
    """Mide las condiciones de la firma (§4.1, §8.2 y §11 punto 2): continuidad en el empalme, velocidades máximas y
    despejes. Devuelve un dict con las medidas y "pasa"."""
    def paso(c):
        a, b = _vuelo(c, geo), _vuelo(c + 1, geo)
        return math.hypot(b[0] - a[0], b[1] - a[1]), b[3] - a[3], math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
    antes, despues = paso(-1), paso(0)
    # dirección en el empalme: la tangente de cada curva en S (la cuerda de un fotograma la tuerce la curvatura)
    tg = [math.degrees(math.atan2(q[1] - p[1], q[0] - p[0])) for p, q in ((geo["B1"][2], geo["B1"][3]), (geo["B2"][0], geo["B2"][1]))]
    antes, despues = antes[:2] + (tg[0],), despues[:2] + (tg[1],)
    pasos = [paso(c) for c in range(F_SUELTA, F_ATRAPA)]
    final = lapiz_bumeran(-1, geo)["tan"]
    inf = {"empalme_v_px_f": (round(antes[0], 2), round(despues[0], 2)),
           "empalme_omega_grados_f": (round(antes[1], 2), round(despues[1], 2)),
           "empalme_direccion_grados": (round(antes[2], 1), round(despues[2], 1)),
           "v_max_px_f": round(max(p[0] for p in pasos), 1), "omega_max_grados_f": round(max(p[1] for p in pasos), 1),
           "giro_total_grados": round(_vuelo(F_ATRAPA, geo)[3] - _vuelo(F_SUELTA, geo)[3], 1),
           "escala_max": round(max(_vuelo(c, geo)[2] for c in range(F_SUELTA, F_ATRAPA + 1)), 3),
           "brazo_en_c_-1": tuple(round(v, 2) for v in final["pose"]["bd"]), "cuerpo_dx_en_c_-1": round(final["dx"], 2),
           "cabeza_en_c_-1": round(final["cabeza_giro"], 2), "despejes_px": _despejes(geo)}
    d = inf["despejes_px"]
    inf["pasa"] = (abs(antes[0] - despues[0]) <= 1.0 and abs(antes[1] - despues[1]) <= 0.5 and abs(antes[2] - despues[2]) <= 3.0
                   and inf["v_max_px_f"] <= 90 and inf["omega_max_grados_f"] <= 40 and min(p[1] for p in pasos) > 0
                   and abs(final["pose"]["bd"][0] - BD_FIRMA[0]) <= 2 and abs(final["pose"]["bd"][1] - BD_FIRMA[1]) <= 2
                   and abs(final["dx"]) <= 1 and d["texto_min"] >= 30 and d["objeto_min"] >= 30 and d["caras_min"] >= 8
                   and d["centro_en_zona_util"])
    return inf


# ---------------------------------------------------------------- seguridad
class DestellosError(ValueError):
    """El video tiene destellos de más (ver `comprobar_destellos`)."""


def luminosidad(img):
    """Luminosidad media del fotograma, de 0 a 255 (Rec. 709 sobre los valores sRGB), y la de una rejilla de 16 x 9
    celdas (para ver cambios que ocupan parte del cuadro)."""
    chica = img.convert("L").resize((36, 64), Image.BOX)        # "L" de Pillow usa Rec. 601: basta para comparar
    a = np.asarray(chica, dtype=np.float32)
    return float(a.mean()), a.reshape(16, 4, 9, 4).mean(axis=(1, 3))


def comprobar_destellos(fotogramas, fps=FPS, umbral=10.0, max_por_segundo=3, salto_max=40.0, zona=0.25,
                        umbral_zona=51.0, estricto=True):
    """Control de fotosensibilidad. `fotogramas`: imágenes PIL en orden (o las tuplas que devuelve `luminosidad`).

    Cuenta como «cambio brusco» el paso de un fotograma al siguiente cuando (a) la luminosidad media del cuadro cambia
    `umbral` o más (de 255), o (b) al menos `zona` (25 %) de las celdas de una rejilla de 16 x 9 cambian `umbral_zona`
    o más (20 % de la escala: un destello que no ocupa todo el cuadro). Varios fotogramas seguidos que cambian en el
    mismo sentido (algo oscuro que cruza, un fundido) cuentan como un solo cambio: un destello es un par de cambios
    opuestos. Falla si:
      - en algún tramo de 1 segundo hay más de `max_por_segundo` (3) cambios bruscos, o
      - algún cambio de la luminosidad media pasa de `salto_max` (40 de 255: un salto a pantalla completa).
    Devuelve un dict con las medidas; si falla y `estricto`, lanza DestellosError con el detalle."""
    medidas = [f if isinstance(f, tuple) else luminosidad(f) for f in fotogramas]
    cambios, saltos = [], []
    mayor = (0.0, 0)
    previo = (None, 0)                                    # (fotograma, signo) del último fotograma con cambio
    for i in range(1, len(medidas)):
        d = medidas[i][0] - medidas[i - 1][0]
        dm = abs(d)
        dz = float((np.abs(medidas[i][1] - medidas[i - 1][1]) >= umbral_zona).mean())
        if dm > mayor[0]:
            mayor = (dm, i)
        if dm >= umbral or dz >= zona:
            signo = 1 if d >= 0 else -1
            if not (previo[0] == i - 1 and previo[1] == signo):     # una rampa seguida en el mismo sentido cuenta una vez
                cambios.append(i)
            previo = (i, signo)
        if dm > salto_max:
            saltos.append((i, round(dm, 1)))
    peor, peor_en = 0, None
    for j, i in enumerate(cambios):                       # ventana deslizante de 1 segundo
        n = sum(1 for k in cambios[j:] if k - i < fps)
        if n > peor:
            peor, peor_en = n, i
    informe = {"fotogramas": len(medidas), "cambios_bruscos": len(cambios),
               "fotogramas_con_cambio": cambios, "max_cambios_en_1_s": peor,
               "segundo_del_maximo": None if peor_en is None else round(peor_en / fps, 2),
               "mayor_salto_de_luminosidad": round(mayor[0], 1), "segundo_del_mayor_salto": round(mayor[1] / fps, 2),
               "saltos_a_pantalla_completa": saltos,
               "limites": {"umbral": umbral, "max_por_segundo": max_por_segundo, "salto_max": salto_max},
               "pasa": peor <= max_por_segundo and not saltos}
    if estricto and not informe["pasa"]:
        raise DestellosError(f"Destellos de más: {peor} cambios bruscos en 1 s (máximo {max_por_segundo}) hacia el "
                             f"segundo {informe['segundo_del_maximo']}; saltos a pantalla completa: {saltos}")
    return informe


if __name__ == "__main__":
    print(__doc__)
