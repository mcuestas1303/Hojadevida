#!/usr/bin/env python3
"""Audio del short 2 de Tin & Tan, «How Many Days Did We Wait for GTA 6?», hecho con código (numpy + ffmpeg).

Uso (desde la carpeta del proyecto):
    python3 codigo/audio.py              # escribe 05_audio/efectos.wav, musica.wav, mezcla_sin_musica.wav y mezcla.wav
    python3 codigo/audio.py --verificar  # además lista cada golpe con el instante medido

Todo es determinista: el ruido sale de un generador con semilla fija. No usa material de terceros ni del juego.
La voz (05_audio/dialogo_110.mp3) empieza en el fotograma 0, sin retraso. Golpes de la sección 13 del prompt, con los
tiempos reajustados a la voz real. Niveles: golpes bajo la voz a unos -26 LUFS (-12 dB respecto a la voz), música a
-24 LUFS, mezcla final llevada a -14 LUFS con techo de -1 dBTP (ganancia y, si hace falta, limitador de ffmpeg).
Estructura y sonidos comunes: `2026-11-21_tin_y_tan_casete_y_lapiz/codigo/audio_v2.py`.
NADIE HA ESCUCHADO esta mezcla: todo lo de aquí se comprobó con medidas, no al oído.
"""
import json
import re
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

PROY = Path(__file__).resolve().parent.parent
AUDIO = PROY / "05_audio"
SR = 48000
DUR = 28.5
N = int(SR * DUR)
BPM = 120
PULSO = 60.0 / BPM            # 0,5 s: la rejilla del video
FIN_VOZ = 27.33               # la voz va de 0,00 a 27,33 s (05_audio/linea_de_tiempo_voz.md)

LUFS_MUSICA = -24.0
LUFS_VOZ_NOMINAL = -14.0
DB_BAJO_VOZ = -12.0           # golpes bajo la voz: -26 LUFS (lección del short 1: a -38 no se oían)
PICO_FUERA = 10 ** (-6.0 / 20)     # golpes sin voz encima (arranque y cierre): pico de -6 dBFS
LUFS_MEZCLA = -14.0
TECHO_MEZCLA_DBTP = -1.0

# Contadores del render (inicio, fin): el tictac sigue el mismo ease-out cúbico
C_4745, C_4748, C_63, C_4811 = (11.15, 12.9), (15.6, 18.0), (17.75, 18.8), (21.4, 22.8)

# ---------------------------------------------------------------- golpes de la sección 13: (segundo, sonido, a qué va atado)
EVENTOS = [(0.0, "thunk", "arranque, toma 1 (y empalme del bucle)"), (0.0, "zumbido", "vibración del mando, toma 1")]
EVENTOS += [(0.5, "boton", "latido del botón, toma 1")]
EVENTOS += [(t, "clic_borron", f"corte con borrón en {t}") for t in (1.0, 2.0, 9.0, 17.5, 25.5, 27.5)]
EVENTOS += [(t, "clic", f"corte seco en {t}") for t in (5.0, 15.0, 21.0, 23.5)]
EVENTOS += [(3.8, "hoja", "vuelta de hoja, toma 3")]
EVENTOS += [(9.2 + 0.1 * i, f"bloque_{i}", "bloque que se llena, toma 5") for i in range(13)]
EVENTOS += [(C_4745[0], "tictac_4745", "contador de la toma 6 (11,15 a 12,9)")]
EVENTOS += [(t, "pop", "marca bisiesta, toma 7") for t in (13.9, 14.2, 14.5)]
# el primer paso (4,745 a 4,746) llega cuando el ease-out vale 1/6: 0,077 s después de empezar
T_4748 = C_4748[0] + (1 - (5 / 6) ** (1 / 3)) * (C_4748[1] - C_4748[0])
EVENTOS += [(T_4748, "tictac_4748", "contador de la toma 8, 3 pasos (4,746 en 15,74; 4,747 en 16,1; 4,748 en 16,68)")]
EVENTOS += [(17.56 + 0.18 * k, "hoja_corta", "hoja en blanco, toma 9") for k in range(6)]
EVENTOS += [(19.4, "hoja", "vuelta de hoja, toma 9")]
EVENTOS += [(C_4811[0], "tictac_4811", "contador de la toma 10 (21,4 a 22,8; llega en 22,53)")]
# El contador llega a 4,811 en el primer fotograma en que 4748 + 63 * ease-out redondea a 4811 (22,53 s), no al final
# del ease-out: el ding, el pop del texto y el cambio a tomate van atados a ese fotograma (igual que render.t_llegada).
LLEGA_4811 = next(f for f in range(900) if round(63 * (1 - (1 - min(1.0, max(0.0, (f / 30 - C_4811[0]) / (C_4811[1] - C_4811[0])))) ** 3)) == 63) / 30
EVENTOS += [(LLEGA_4811, "ding", "llegada a 4,811 (primer fotograma con el valor final)")]
EVENTOS += [(6.6, "pop", "la fecha entra en la hoja, toma 4")]
EVENTOS += [(t, "pop_grave", "latido del bloque 13, toma 12") for t in (26.0, 26.5, 27.0)]
EVENTOS += [(27.5, "whoosh", "retroceso de cámara, toma 13 (27,5 a 28,3)")]
EVENTOS += [(t, "boton", "latido del botón, toma 13") for t in (27.5, 28.0)]
# El thunk de 28,5 es el del segundo 0,0 de la vuelta siguiente: el video dura 28,5 s justos y no se duplica.
EVENTOS.sort(key=lambda e: e[0])


# ---------------------------------------------------------------- utilidades
def tiempo(dur):
    return np.arange(int(round(dur * SR))) / SR


def ruido(rng, dur, f0=None, f1=None):
    """Ruido blanco con semilla, recortado en frecuencia con una máscara de FFT."""
    n = int(round(dur * SR))
    x = rng.standard_normal(n)
    if f0 is None and f1 is None:
        return x
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(n, 1 / SR)
    m = np.ones_like(f)
    if f0:
        m *= 1 / (1 + (f0 / np.maximum(f, 1e-6)) ** 6)
    if f1:
        m *= 1 / (1 + (f / f1) ** 6)
    y = np.fft.irfft(X * m, n)
    return y / (np.max(np.abs(y)) + 1e-12)


def barrido(f_ini, f_fin, dur):
    t = tiempo(dur)
    f = f_ini * (f_fin / f_ini) ** (t / dur)
    return np.sin(2 * np.pi * np.cumsum(f) / SR), t


def ataque(x, ms=1.0):
    n = max(1, int(SR * ms / 1000))
    x = x.copy()
    x[:n] *= np.linspace(0, 1, n)
    return x


def cola(x, ms=5.0):
    n = max(1, min(len(x), int(SR * ms / 1000)))
    x = x.copy()
    x[-n:] *= np.linspace(1, 0, n)
    return x


# ---------------------------------------------------------------- sonidos (mono)
def s_thunk(rng):
    """Golpe seco y grave de 80 ms (más 40 ms de cola): el casete que cae."""
    x, t = barrido(95, 48, 0.12)
    y = x * np.exp(-t / 0.045)
    y[: int(0.006 * SR)] += 0.3 * ruido(rng, 0.006, 200, 2500) * np.linspace(1, 0, int(0.006 * SR))
    return cola(ataque(y, 0.5), 20)


def s_whoosh(rng, dur=0.32):
    x = ruido(rng, dur, 350, 3500)
    t = tiempo(dur)
    env = np.sin(np.pi * np.minimum(1, t / dur)) ** 2
    env[: int(0.004 * SR)] = np.maximum(env[: int(0.004 * SR)], np.linspace(0, 0.25, int(0.004 * SR)))
    return x * env * 1.3


def s_clic(rng, f=1700.0):
    t = tiempo(0.03)
    return ataque(np.sin(2 * np.pi * f * t) * np.exp(-t / 0.004), 0.3) * 0.7


def s_clic_borron(rng):
    y = np.zeros(int(0.09 * SR))
    c = s_clic(rng)
    y[: len(c)] += c
    r = ruido(rng, 0.09, 900, 5000)
    t = tiempo(0.09)
    y += 0.35 * r * np.exp(-t / 0.025)
    return ataque(y, 0.3)


def s_plop(rng):
    x, t = barrido(260, 640, 0.09)
    return ataque(x * np.exp(-t / 0.03), 1.0)




def s_zumbido(rng):
    """Zumbido corto de vibración del mando: 0,22 s de onda grave con trémolo."""
    t = tiempo(0.22)
    y = np.tanh(2.5 * np.sin(2 * np.pi * 62 * t)) * (0.6 + 0.4 * np.sin(2 * np.pi * 31 * t))
    return cola(ataque(y * np.exp(-t / 0.09), 4.0), 30) * 0.35


def s_boton(rng):
    """Clic de botón: dos golpes muy cortos (bajar y soltar)."""
    y = np.zeros(int(0.07 * SR))
    for t0, f, a in ((0.0, 1500.0, 0.7), (0.035, 2100.0, 0.4)):
        c = s_clic(rng, f) * a
        i = int(t0 * SR)
        y[i:i + len(c)] += c
    return y


def s_hoja(rng, dur=0.13):
    """Papel que pasa de hoja: un tic corto y un soplo de ruido que se apaga."""
    t = tiempo(dur)
    y = ruido(rng, dur, 1800, 9000) * np.exp(-t / (dur * 0.3)) * 0.6
    c = s_clic(rng, 2300.0) * 0.6
    y[:len(c)] += c
    return cola(ataque(y, 0.3), 10)


def s_tic(f):
    t = tiempo(0.03)
    return ataque(np.sin(2 * np.pi * f * t) * np.exp(-t / 0.006), 0.3) * 0.6




def s_tictac(dur, progresos, f0=620.0, f1=1240.0):
    """Tictac de contador: un tic en el instante en que el valor (ease-out cúbico) llega a cada progreso p (0 a 1);
    el tono sube con el valor."""
    y = np.zeros(int((dur + 0.05) * SR))
    for p in progresos:
        u = 1 - (1 - p) ** (1 / 3)              # instante en que el ease-out llega a p
        i = int(round(u * dur * SR))
        tic = s_tic(f0 * (f1 / f0) ** p)
        y[i:i + len(tic)] += tic[: len(y) - i]
    return y


def s_campana(f, dur, parciales=((1.0, 1.0), (2.76, 0.45), (5.4, 0.22), (8.93, 0.1))):
    t = tiempo(dur)
    y = np.zeros_like(t)
    for mult, amp in parciales:
        y += amp * np.sin(2 * np.pi * f * mult * t) * np.exp(-t / (dur * 0.28 / mult ** 0.5))
    return cola(ataque(y, 1.0), 30) * 0.6


def s_pulsada(f, dur, decae=0.16):
    t = tiempo(dur)
    y = np.sin(2 * np.pi * f * t) + 0.32 * np.sin(2 * np.pi * 2 * f * t) + 0.1 * np.sin(2 * np.pi * 3 * f * t)
    return cola(ataque(y * np.exp(-t / decae), 4.0), 15) * 0.5




def sonido(nombre, rng):
    if nombre == "thunk":
        return s_thunk(rng)
    if nombre == "zumbido":
        return s_zumbido(rng)
    if nombre == "boton":
        return s_boton(rng)
    if nombre == "whoosh":
        return s_whoosh(rng, 0.8) * 0.6
    if nombre == "clic":
        return s_clic(rng)
    if nombre == "clic_borron":
        return s_clic_borron(rng)
    if nombre == "hoja":
        return s_hoja(rng)
    if nombre == "hoja_corta":
        return s_hoja(rng, 0.08) * 0.8
    if nombre.startswith("bloque_"):
        return s_tic(520.0 * 2 ** (int(nombre.split("_")[1]) / 12))      # 13 tics que suben un semitono cada uno
    if nombre == "tictac_4745":
        return s_tictac(C_4745[1] - C_4745[0], [k / 22 for k in range(22)])
    if nombre == "tictac_4748":
        y = s_tictac(C_4748[1] - C_4748[0], [1 / 6, 3 / 6, 5 / 6], 880.0, 1100.0)      # cuando el valor pasa a 46, 47 y 48
        return y[int(round((T_4748 - C_4748[0]) * SR)):]
    if nombre == "tictac_4811":
        return s_tictac(C_4811[1] - C_4811[0], [k / 20 for k in range(16)])     # calla al llegar (ding en 22,53)
    if nombre == "pop":
        return s_plop(rng)
    if nombre == "pop_grave":
        x, t = barrido(180, 420, 0.10)
        return ataque(x * np.exp(-t / 0.035), 1.0)
    if nombre == "ding":
        return s_campana(1318.5, 0.9)
    raise ValueError(nombre)


def poner(pista, x, t, pan=0.0, envolver=False):
    """Suma el sonido mono x en la pista estéreo, empezando en el segundo t. pan de -1 (izq.) a 1 (der.)."""
    i = int(round(t * SR))
    gi, gd = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    n = len(x)
    if envolver:
        idx = (i + np.arange(n)) % N
        np.add.at(pista[:, 0], idx, x * gi * 1.4142)
        np.add.at(pista[:, 1], idx, x * gd * 1.4142)
    else:
        n = min(n, N - i)
        if n > 0:
            pista[i:i + n, 0] += x[:n] * gi * 1.4142
            pista[i:i + n, 1] += x[:n] * gd * 1.4142


# ---------------------------------------------------------------- pistas
def pista_efectos():
    """Devuelve (fuera_de_la_voz, bajo_la_voz): dos pistas estéreo sin escalar. «Fuera» son el golpe y el zumbido del
    arranque (fotograma 0, donde la voz apenas empieza) y todo lo que suena después de que la voz termina."""
    rng = np.random.default_rng(20130917)
    fuera, bajo = np.zeros((N, 2)), np.zeros((N, 2))
    for t, nombre, _ in EVENTOS:
        destino = fuera if (t < 0.01 or t >= FIN_VOZ) else bajo
        poner(destino, sonido(nombre, rng), t)
    return fuera, bajo


ACORDES = {  # bajo, y tres notas para el arpegio
    "C": (65.41 * 2, (261.63, 329.63, 392.00)),
    "Am": (55.00 * 2, (220.00, 261.63, 329.63)),
    "F": (43.65 * 2, (220.00, 261.63, 349.23)),
    "G": (49.00 * 2, (196.00, 246.94, 293.66)),
}
PROGRESION = ["C", "Am", "F", "G"] * 3 + ["C", "F", "G"]      # 14 compases de 2,0 s y un pulso (sol) que vuelve al do


def pista_musica():
    """Patrón de 120 BPM en do mayor: bajo en los pulsos 1 y 3, arpegio en corcheas, bombo suave y un shaker.
    57 pulsos (28,5 s): 14 compases y un pulso suelto; las colas se envuelven al principio para que el bucle empalme."""
    rng = np.random.default_rng(120)
    m = np.zeros((N, 2))
    t_b = tiempo(0.12)
    bombo = np.sin(2 * np.pi * np.cumsum(110 * (48 / 110) ** (t_b / 0.12)) / SR) * np.exp(-t_b / 0.035)
    for c, nombre in enumerate(PROGRESION):
        t0 = c * 4 * PULSO
        bajo, notas = ACORDES[nombre]
        for pulso in (0, 2):
            if t0 + pulso * PULSO >= DUR - 1e-9:
                continue
            tb = tiempo(0.9)
            x = (np.sin(2 * np.pi * bajo * tb) + 0.25 * np.sin(2 * np.pi * 2 * bajo * tb)) * np.exp(-tb / 0.32)
            poner(m, cola(ataque(x, 6), 30) * 0.55, t0 + pulso * PULSO, envolver=True)
            poner(m, bombo * 0.5, t0 + pulso * PULSO, envolver=True)
        for k in range(8):                                  # corcheas
            if t0 + k * PULSO / 2 >= DUR - 1e-9:
                continue
            f = notas[(0, 1, 2, 1, 0, 2, 1, 2)[k]]
            poner(m, s_pulsada(f, 0.5, 0.17) * 0.5, t0 + k * PULSO / 2, pan=0.3 if k % 2 else -0.3, envolver=True)
            if k % 2:                                       # shaker a contratiempo
                ts = tiempo(0.05)
                poner(m, ruido(rng, 0.05, 5000, 11000) * np.exp(-ts / 0.012) * 0.12, t0 + k * PULSO / 2, pan=0.2,
                      envolver=True)
    return m


def leer_voz():
    """La voz tal cual está, convertida a 48 kHz estéreo, desde el fotograma 0. No se cambia su nivel aquí."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(AUDIO / "dialogo_110.mp3"),
                        "-ar", str(SR), "-ac", "2", "-f", "f32le", "-"], capture_output=True)
    if r.returncode != 0:
        sys.exit(f"No se pudo leer la voz: {r.stderr.decode()[:300]}")
    v = np.frombuffer(r.stdout, dtype=np.float32).reshape(-1, 2).astype(np.float64)
    pista = np.zeros((N, 2))
    n = min(len(v), N)
    pista[:n] = v[:n]
    return pista


# ---------------------------------------------------------------- archivos y medición
def guardar(ruta, x):
    y = np.clip(np.round(x * 32767.0), -32768, 32767).astype("<i2")
    with wave.open(str(ruta), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(y.tobytes())


def medir(ruta):
    """Sonoridad integrada (LUFS, EBU R128) y pico real (dBTP) con el filtro ebur128 de ffmpeg."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(ruta), "-af", "ebur128=peak=true",
                        "-f", "null", "-"], capture_output=True, text=True)
    resumen = r.stderr[r.stderr.rfind("Summary:"):]
    lufs = float(re.search(r"I:\s+(-?[\d.]+|-?inf) LUFS", resumen).group(1).replace("inf", "70"))
    pico = float(re.search(r"Peak:\s+(-?[\d.]+|-?inf) dBFS", resumen).group(1).replace("inf", "99"))
    return lufs, pico


def medir_pista(x, nombre="_medida.wav"):
    ruta = AUDIO / nombre
    guardar(ruta, x)
    try:
        return medir(ruta)
    finally:
        ruta.unlink()


def llevar_a(x, lufs):
    """Escala la pista hasta la sonoridad integrada pedida (dos pasadas, porque la puerta de R128 no es lineal)."""
    for _ in range(3):
        actual, _ = medir_pista(x)
        x = x * 10 ** ((lufs - actual) / 20)
    return x


def limitar(x, techo_db):
    """Limitador de ffmpeg (alimiter, anticipación de 5 ms) sobre la pista; devuelve la pista limitada."""
    ent, sal = AUDIO / "_lim_in.wav", AUDIO / "_lim_out.wav"
    with wave.open(str(ent), "wb") as w:              # 24 bits no hace falta: 16 bits, como el resto
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(np.clip(np.round(x * 32767.0), -32768, 32767).astype("<i2").tobytes())
    try:
        subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(ent), "-af",
                        f"alimiter=limit={10 ** (techo_db / 20):.5f}:attack=5:release=60:level=false", "-ar", str(SR),
                        str(sal)], check=True)
        with wave.open(str(sal), "rb") as w:
            y = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").reshape(-1, 2).astype(np.float64) / 32768
    finally:
        ent.unlink(missing_ok=True)
        sal.unlink(missing_ok=True)
    out = np.zeros_like(x)
    n = min(len(x), len(y))
    out[:n] = y[:n]
    return out


def construir(verboso=True):
    voz = leer_voz()
    lufs_voz, pico_voz = medir_pista(voz)
    fuera, bajo = pista_efectos()
    bajo = llevar_a(bajo, LUFS_VOZ_NOMINAL + DB_BAJO_VOZ)          # -26 LUFS
    fuera = fuera * PICO_FUERA / float(np.max(np.abs(fuera)))      # pico de -6 dBFS
    efectos = fuera + bajo
    musica = llevar_a(pista_musica(), LUFS_MUSICA)
    sin_musica = voz + efectos
    mezcla = sin_musica + musica
    antes = medir_pista(mezcla)
    # mezcla final: ganancia hasta -14 LUFS; si el pico real pasa de -1 dBTP, limitador y se vuelve a medir
    limitada = False
    techo = TECHO_MEZCLA_DBTP - 0.3
    for _ in range(6):
        l, p = medir_pista(mezcla)
        if abs(l - LUFS_MEZCLA) > 0.05:
            mezcla = mezcla * 10 ** ((LUFS_MEZCLA - l) / 20)
            l, p = medir_pista(mezcla)
        if p > TECHO_MEZCLA_DBTP:
            mezcla = limitar(mezcla, techo)
            limitada = True
            techo -= 0.2
        elif abs(l - LUFS_MEZCLA) <= 0.05:
            break
    guardar(AUDIO / "efectos.wav", efectos)
    guardar(AUDIO / "musica.wav", musica)
    guardar(AUDIO / "mezcla_sin_musica.wav", sin_musica)
    guardar(AUDIO / "mezcla.wav", mezcla)
    niveles = {
        "voz (dialogo_110.mp3, desde el fotograma 0, sin tocar)": [lufs_voz, pico_voz],
        "efectos.wav": list(medir(AUDIO / "efectos.wav")),
        "efectos bajo la voz (0,5 a 27,0 s)": list(medir_pista(bajo)),
        "efectos fuera de la voz (arranque y cierre)": list(medir_pista(fuera)),
        "musica.wav": list(medir(AUDIO / "musica.wav")),
        "mezcla_sin_musica.wav (sin ganancia final)": list(medir(AUDIO / "mezcla_sin_musica.wav")),
        "mezcla antes de la ganancia final": list(antes),
        "mezcla.wav (final)": list(medir(AUDIO / "mezcla.wav")),
    }
    if verboso:
        for k, (l, p) in niveles.items():
            print(f"  {k}: {l:.1f} LUFS, pico real {p:.1f} dBTP")
        print(f"  limitador en la mezcla final: {'sí' if limitada else 'no hizo falta'}")
    niveles["limitador en la mezcla final"] = limitada
    return niveles


def verificar():
    """Lee efectos.wav y comprueba que en cada segundo de la tabla empieza un sonido (subida de energía)."""
    with wave.open(str(AUDIO / "efectos.wav"), "rb") as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").reshape(-1, 2).astype(np.float64) / 32768
    mono = np.abs(x).max(axis=1)
    filas, mal = [], 0
    for t, nombre, que in EVENTOS:
        i = int(round(t * SR))
        antes = mono[max(0, i - int(0.004 * SR)):i]
        despues = mono[i:i + int(0.03 * SR)]
        pico = despues.max() if len(despues) else 0.0
        umbral = max(0.25 * pico, (antes.max() if len(antes) else 0.0) * 1.5, 1e-4)
        sobre = np.nonzero(despues >= umbral)[0]
        if pico <= 1e-4 or len(sobre) == 0:
            inicio, ok = None, False
        else:
            inicio = t + sobre[0] / SR
            ok = (inicio - t) <= 0.012
        mal += 0 if ok else 1
        filas.append((t, nombre, que, inicio, ok))
    return filas, mal


def main():
    AUDIO.mkdir(exist_ok=True)
    print("Audio: efectos, música y mezcla")
    niveles = construir()
    filas, mal = verificar()
    (AUDIO / "medidas_audio.json").write_text(json.dumps(
        {"niveles_lufs_y_pico_dbtp": niveles,
         "golpes": [{"segundo": round(t, 3), "sonido": n, "atado_a": q, "inicio_medido": i, "en_su_tiempo": bool(ok)}
                    for t, n, q, i, ok in filas]}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    if "--verificar" in sys.argv:
        for t, n, q, i, ok in filas:
            print(f"  {t:6.2f} s  {n:16s} inicio medido {('%.4f' % i) if i is not None else '—':>8s}  {'bien' if ok else 'REVISAR'}  ({q})")
    print(f"  golpes: {len(filas)}; fuera de su tiempo: {mal}")
    return niveles


if __name__ == "__main__":
    main()
