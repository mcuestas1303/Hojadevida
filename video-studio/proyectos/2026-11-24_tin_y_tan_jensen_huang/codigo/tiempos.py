#!/usr/bin/env python3
"""Línea de tiempo del short 3 de Tin & Tan, derivada de la voz real (05_audio/linea_de_tiempo.json, que escribe
armar_dialogo.py). La leen render.py, audio.py, miniatura.py y comprobar_video.py: un solo sitio para los tiempos.

Reglas: 30 fps; rejilla de 0,5 s; la toma 1 (portada y apertura de la firma) dura 30 fotogramas; cada corte cae en el
pulso más cercano al centro de la pausa entre dos líneas; la toma 14 (cierre de la firma del lápiz bumerán) dura 30
fotogramas y la voz termina antes de c = -17 (FIRMA_LAPIZ_BUMERAN.md, §2.2). Uso: python3 codigo/tiempos.py (imprime la tabla).
"""
import json
from pathlib import Path

PROY = Path(__file__).resolve().parent.parent
FPS = 30
_D = json.loads((PROY / "05_audio" / "linea_de_tiempo.json").read_text(encoding="utf-8"))
LINEAS = _D["lineas"]
VOZ_ENTRA = _D["voz_entra"]


def L(n):
    """Inicio (s) de la línea n (1 a 11) en el video."""
    return LINEAS[n - 1]["empieza"]


def E(n):
    return LINEAS[n - 1]["termina"]


def P(n):
    """Inicio del segundo tramo de la línea n (tras su pausa interna)."""
    return LINEAS[n - 1]["tramos"][1]


def _pulso(x):
    return round(x * 2) / 2


def _entre(n):
    """Pulso más cercano al centro de la pausa entre la línea n - 1 y la n."""
    return _pulso((E(n - 1) + L(n)) / 2)


def F(t):
    return int(round(t * FPS))


# Cortes de las 14 tomas (CORTES[i] = inicio de la toma i + 1; el último es el final del video)
# Toma 6 («11 days» con las 11 cruces): va medio segundo antes del inicio de la línea 5, sobre el final de la línea 4
# («…as C E O.») y «Before that:», para que el rótulo no coincida con «more than thirty-three years» (vuelta 2).
_c6 = _entre(5) - 0.5
_c14 = max(_pulso(E(11)), _pulso(E(11) - 13 / FPS + 0.2499))        # la voz termina en c <= -17 (0,433 s tras el corte)
while E(11) > _c14 + 13 / FPS:
    _c14 += 0.5
CORTES = [0.0, 1.0, _entre(2), _entre(3), _entre(4), _c6, _c6 + 1.0, _entre(6), _entre(7), _entre(8), _entre(9),
          _entre(10), _entre(11), _c14, _c14 + 1.0]
DUR = CORTES[-1]
N = F(DUR)


def C(n):
    """Inicio (s) de la toma n (1 a 14); C(15) = final."""
    return CORTES[n - 1]


BORRONES = [C(14)]                 # el plano de cierre de la firma entra por borrón (FIRMA, §2.2)

# ---------------------------------------------------------------- instantes de cada toma (todos salen de la voz)
T3_CIRCULO = (P(2) + 0.55, P(2) + 0.95)             # círculo del 12: mientras suena «November twelfth»
T4_REVELADO = (C(4), C(4) + 8 / FPS)
T5_MARCA_17 = (C(5) + 0.1, C(5) + 0.4)              # círculo de tinta en el 17: el origen de «+6 days»
T5_FLECHA = (C(5) + 0.45, C(5) + 1.0)
T5_CIRCULO = (C(5) + 1.4, C(5) + 1.8)
T5_CRUCES = C(6) - 1.1                               # 11 cruces, una cada 3 fotogramas
T7_BARRA = (C(7) + 0.1, C(7) + 0.9)
T9_HUANG = C(9) + 0.3
T9_ALTMAN = min(P(7) - 0.1, C(10) - 1.2)            # «five days»
PICO_SUBIDA = (P(8) - 1.2, P(8) - 0.4)
PICO_SILENCIO = (P(8) - 0.4, P(8))                   # 12 fotogramas sin efectos ni música, en la pausa tras «Apple:»
VALOR_JOBS = 4382
_llega = C(11) - 13 / FPS                            # el zoom de golpe (5 + 8 fotogramas) cabe antes del corte
CONTADOR = (P(8) + 0.25, P(8) + 0.25 + (_llega - P(8) - 0.25) / 0.9515)


def contador(t):
    u = max(0.0, min(1.0, (t - CONTADOR[0]) / (CONTADOR[1] - CONTADOR[0])))
    return int(round(VALOR_JOBS * (1 - (1 - u) ** 3)))


LLEGA = next(f for f in range(N) if contador(f / FPS) == VALOR_JOBS) / FPS      # primer fotograma con 4,382: el pico
T13_PASE = (P(11) + 0.3, P(11) + 0.3 + 8 / FPS)

# Rótulos en inglés: (entra, sale, clave del texto). Texto exacto de la tabla de la sección 12 del prompt.
ROTULOS = [
    (0.0, 0.9, "portada"),
    (C(2) + 0.1, C(3) - 0.1, "11 days?"),
    (P(2) + 0.4, C(4) - 0.1, "Nov 12"),
    (C(4) + 0.5, C(5) - 0.1, "Nov 17"),
    (C(5) + 0.2, C(5) + 1.3, "+6 days"),
    (C(5) + 1.4, C(6) - 0.05, "Nov 23"),
    (C(6) + 0.05, C(7) - 0.05, "11 days"),
    (C(7) + 0.3, C(8) - 0.05, "12,274 days"),
    (T9_ALTMAN, C(10) - 0.1, "5 days"),
    (CONTADOR[0], C(12) - 0.1, "contador"),
    (C(12) + 0.1, C(13) - 0.1, "11 days"),
    (C(13) + 0.05, P(11) - 0.1, "Who else?"),
    (P(11) + 0.05, C(14) - 0.1, "Subscribe"),
    (C(14), DUR, "portada_cierre"),
]

# Subtítulos en español quemados: (tarjeta, entra, sale, renglones, cuándo aparece cada renglón o None).
# Textos de la vuelta 2 (correcciones del supervisor): la cifra y «días» también en español; «11 días» en la tarjeta 1.
_m = 1 / FPS
SUBTITULOS = [
    (1, C(2), min(E(1) + 0.05, C(3) - _m), ("¿Jensen Huang volvió", "rápido en 11 días?"), None),
    (2, max(L(2), C(3)), min(E(2) + 0.05, C(4) - _m), ("Renunció a Nvidia", "tras un escándalo."), None),
    (3, max(L(3), C(4)), min(E(3) + 0.05, C(5) - _m), ("El 17, la junta dijo", "que no lo repondría."), None),
    (4, max(L(4), C(5)), min(E(4) + 0.05, C(6) - _m), ("Seis días después,", "lo repuso como CEO."), None),
    (5, max(L(5), C(7)), min(E(5) + 0.05, C(8) - _m), ("Antes: más de 33", "años al mando."), None),
    (6, max(L(6), C(8)), min(E(6) + 0.05, C(9) - _m), ("¿Rápido comparado", "con quién?"), None),
    (7, max(L(7), C(9)), min(E(7) + 0.05, C(10) - _m), ("Sam Altman, OpenAI:", "5 días."), (None, T9_ALTMAN)),
    # la cifra en español («4.382», con punto) aparece cuando el contador llega: no se adelanta al pico
    (8, max(L(8), C(10)), C(11) - _m, ("Steve Jobs, Apple:", "4.382 días."), (None, LLEGA)),
    (9, max(L(9), C(11)), min(E(9) + 0.05, C(12) - _m), ("¿Casi 12 años?",), None),
    (10, max(L(10), C(12)), min(E(10) + 0.05, C(13) - _m), ("Más rápido que Jobs.", "Más lento que Altman."), None),
    (11, max(L(11), C(13)), P(11) - 0.08, ("¿Quién más volvió?",), None),
    (12, P(11), min(E(11) + 0.05, C(14) - _m), ("Suscríbete al próximo", "conteo."), None),
]

if __name__ == "__main__":
    print(f"Duración {DUR} s, {N} fotogramas. La voz entra en {VOZ_ENTRA:.3f} s y termina en {E(11):.2f} s.")
    print("Cortes:", CORTES)
    for i, l in enumerate(LINEAS, 1):
        print(f"  línea {i:2d} {l['quien']} {l['empieza']:6.2f}-{l['termina']:6.2f}  {l['texto']}")
    print(f"Contador {CONTADOR[0]:.2f}-{CONTADOR[1]:.2f}; pico (llegada de 4,382) en {LLEGA:.2f} s = {100 * LLEGA / DUR:.1f} % del video")
    for e, s, q in ROTULOS:
        print(f"  rótulo {e:6.2f}-{s:6.2f} ({F(s) - F(e)} f)  {q}")
    for k, e, s, r, _ap in SUBTITULOS:
        print(f"  tarjeta {k:2d} {e:6.2f}-{s:6.2f} ({F(s) - F(e)} f)  {' / '.join(r)}")
