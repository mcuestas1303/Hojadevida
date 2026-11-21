#!/usr/bin/env python3
"""Audio del short «How many pencil turns to rewind a cassette?», hecho con código (numpy + ffmpeg).

Uso (desde la carpeta del proyecto):
    python3 codigo/audio.py            # escribe 05_audio/efectos.wav, musica.wav, mezcla.wav y mezcla_sin_musica.wav
    python3 codigo/audio.py --verificar  # además comprueba que cada golpe cae en su tiempo y mide niveles

Todo es determinista: el ruido sale de un generador con semilla fija. No usa material de terceros.
La voz (05_audio/dialogo_110_v2.mp3) no se toca: solo se convierte a 48 kHz y se retrasa 1,0 s.
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
DUR = 30.0
N = int(SR * DUR)
BPM = 120
PULSO = 60.0 / BPM            # 0,5 s: la rejilla del video
RETRASO_VOZ = 1.0             # la voz entra en el segundo 1,0
FIN_VOZ = 27.1                # y termina en 27,1 (voz v2)

# Niveles pedidos por el prompt (sección 13)
LUFS_GOLPES = -18.0           # pista de efectos completa
LUFS_MUSICA = -24.0
DB_BAJO_VOZ = -12.0           # v2: a -24 no se oían (revisión del supervisor)
_DB_V1 = -24.0           # golpes que suenan debajo de la voz, respecto a la voz
LUFS_VOZ_NOMINAL = -14.0
TECHO_GOLPES = 10 ** (-3.0 / 20)   # ningún golpe pasa de −3 dBFS: se redondea con tanh en vez de recortar
TECHO_MEZCLA_DBTP = -1.0
MAX_EMPUJE = 2.0                   # lo más que se empuja un golpe contra el techo (6 dB): más ensucia el sonido

# ---------------------------------------------------------------- golpes de la sección 13: (segundo, sonido, a qué va atado)
CORTES_BORRON = [1.0, 3.5, 5.0, 6.5, 9.5, 12.0, 16.5, 17.5, 23.0, 27.5]   # «clic suave de borrón» en la tabla de sonido
CORTES_SECOS = [14.0, 19.5, 24.5, 26.0]                          # «clic suave»

EVENTOS = [(0.0, "thunk", "arranque, toma 1"), (0.5, "whoosh", "corte 1 a 2")]
EVENTOS += [(t, "clic_borron", f"corte en {t}") for t in CORTES_BORRON]
EVENTOS += [(t, "clic", f"corte en {t}") for t in CORTES_SECOS]
EVENTOS += [(2.8, "plop", "lápiz al carrete, toma 3")]
EVENTOS += [(t, "matraca", "vuelta del lápiz, toma 4") for t in (3.5, 4.0, 4.5)]
EVENTOS += [(t, "paso", "pasos de Tin, toma 5") for t in (5.0, 5.2, 5.4)]
EVENTOS += [(9.5, "hiss", "cinta que corre, toma 7 (9,5 a 12,0)")]
EVENTOS += [(12.2, "tictac_a", "contador de la toma 8 (12,2 a 13,6)")]
EVENTOS += [(14.3, "vuelta_y_pitido", "vuelta del lápiz y arco, toma 9 (14,3 a 15,3)")]
EVENTOS += [(17.6 + 0.25 * i, f"corte_{i}", "duplicación de la barra, toma 11") for i in range(6)]
EVENTOS += [(19.6, "tictac_b", "contador de la toma 12 (19,6 a 21,9)")]
EVENTOS += [(21.9, "ding", "llegada a 1,170")]
EVENTOS += [(t, "matraca", "vuelta del lápiz, toma 13") for t in (23.0, 23.5, 24.0, 24.5)]
EVENTOS += [(25.6, "campanilla", "llega la aguja, toma 14")]
EVENTOS += [(26.1, "nota3", "la corchea, toma 15")]
EVENTOS += [(t, "matraca", "vuelta del lápiz, toma 16") for t in (27.5, 28.0, 28.5, 29.0)]
EVENTOS += [(29.4, "whoosh", "el casete vuelve a la pose del inicio, toma 16")]
# El thunk de 30,0 es el del segundo 0,0 de la vuelta siguiente: el video dura 30,0 s justos y no cabe otro.
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


def s_matraca(rng):
    t = tiempo(0.045)
    y = 0.8 * ruido(rng, 0.045, 1500, 5500) * np.exp(-t / 0.006)
    y += 0.6 * np.sin(2 * np.pi * 920 * t) * np.exp(-t / 0.012)
    return ataque(y, 0.3)


def s_paso(rng):
    t = tiempo(0.09)
    y = np.sin(2 * np.pi * 115 * t) * np.exp(-t / 0.03)
    y += 0.3 * ruido(rng, 0.09, 150, 900) * np.exp(-t / 0.012)
    return ataque(y, 1.0) * 0.8


def s_hiss(rng, dur=2.5):
    x = ruido(rng, dur, 3500, 11000)
    t = tiempo(dur)
    env = np.minimum(1, t / 0.03) * np.minimum(1, (dur - t) / 0.2)
    return x * env * 0.22


def s_tic(f):
    t = tiempo(0.03)
    return ataque(np.sin(2 * np.pi * f * t) * np.exp(-t / 0.006), 0.3) * 0.6


def s_tictac(dur, pasos=26, f0=620.0, f1=1240.0):
    """Tictac de contador: un tic cada vez que el valor (ease-out cúbico) avanza 1/pasos; el tono sube con el valor."""
    y = np.zeros(int((dur + 0.05) * SR))
    for k in range(pasos):
        p = k / pasos                           # progreso del valor
        u = 1 - (1 - p) ** (1 / 3)              # instante en que el ease-out llega a p
        i = int(round(u * dur * SR))
        tic = s_tic(f0 * (f1 / f0) ** p)
        y[i:i + len(tic)] += tic[: len(y) - i]
    return y


def s_vuelta_y_pitido(rng):
    """Matraca de una vuelta (8 clics que siguen el ease in-out del giro) y un pitido que sube mientras se dibuja el arco."""
    dur = 1.0
    y = np.zeros(int((dur + 0.06) * SR))
    for k in range(8):
        p = k / 8
        # inversa del ease in-out cúbico
        u = (p / 4) ** (1 / 3) if p < 0.5 else 1 - ((1 - p) / 4) ** (1 / 3)
        i = int(round(u * dur * SR))
        m = s_matraca(rng) * 0.8
        y[i:i + len(m)] += m[: len(y) - i]
    t = tiempo(dur)
    u = t / dur
    e = np.where(u < 0.5, 4 * u ** 3, 1 - (-2 * u + 2) ** 3 / 2)
    f = 660 * (990 / 660) ** e
    pit = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.minimum(1, t / 0.02) * np.minimum(1, (dur - t) / 0.05) * 0.22
    y[: len(pit)] += pit
    return y


def s_corte(rng, i):
    t = tiempo(0.035)
    f = 2000 * 2 ** (i / 12 * 2)
    y = np.sin(2 * np.pi * f * t) * np.exp(-t / 0.005) + 0.5 * ruido(rng, 0.035, 2500, 9000) * np.exp(-t / 0.004)
    return ataque(y, 0.3) * 0.7


def s_campana(f, dur, parciales=((1.0, 1.0), (2.76, 0.45), (5.4, 0.22), (8.93, 0.1))):
    t = tiempo(dur)
    y = np.zeros_like(t)
    for mult, amp in parciales:
        y += amp * np.sin(2 * np.pi * f * mult * t) * np.exp(-t / (dur * 0.28 / mult ** 0.5))
    return cola(ataque(y, 1.0), 30) * 0.6


def s_nota3():
    y = np.zeros(int(0.5 * SR))
    for k, f in enumerate((523.25, 659.25, 783.99)):      # do, mi, sol: el tono de la música
        n = s_pulsada(f, 0.26)
        i = int(k * 0.075 * SR)
        y[i:i + len(n)] += n
    return y


def s_pulsada(f, dur, decae=0.16):
    t = tiempo(dur)
    y = np.sin(2 * np.pi * f * t) + 0.32 * np.sin(2 * np.pi * 2 * f * t) + 0.1 * np.sin(2 * np.pi * 3 * f * t)
    return cola(ataque(y * np.exp(-t / decae), 4.0), 15) * 0.5


def sonido(nombre, rng):
    if nombre == "thunk":
        return s_thunk(rng)
    if nombre == "whoosh":
        return s_whoosh(rng)
    if nombre == "clic":
        return s_clic(rng)
    if nombre == "clic_borron":
        return s_clic_borron(rng)
    if nombre == "plop":
        return s_plop(rng)
    if nombre == "matraca":
        return s_matraca(rng)
    if nombre == "paso":
        return s_paso(rng)
    if nombre == "hiss":
        return s_hiss(rng)
    if nombre == "tictac_a":
        return s_tictac(2.0)
    if nombre == "tictac_b":
        return s_tictac(2.3)
    if nombre == "vuelta_y_pitido":
        return s_vuelta_y_pitido(rng)
    if nombre.startswith("corte_"):
        return s_corte(rng, int(nombre[-1]))
    if nombre == "ding":
        return s_campana(1318.5, 0.9)
    if nombre == "campanilla":
        return s_campana(1760.0, 0.35)
    if nombre == "nota3":
        return s_nota3()
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
    """Devuelve (fuera_de_la_voz, bajo_la_voz): dos pistas estéreo sin escalar."""
    rng = np.random.default_rng(19700401)
    fuera, bajo = np.zeros((N, 2)), np.zeros((N, 2))
    for t, nombre, _ in EVENTOS:
        destino = bajo if RETRASO_VOZ <= t < FIN_VOZ else fuera
        poner(destino, sonido(nombre, rng), t)
    return fuera, bajo


ACORDES = {  # bajo, y tres notas para el arpegio
    "C": (65.41 * 2, (261.63, 329.63, 392.00)),
    "Am": (55.00 * 2, (220.00, 261.63, 329.63)),
    "F": (43.65 * 2, (220.00, 261.63, 349.23)),
    "G": (49.00 * 2, (196.00, 246.94, 293.66)),
}
PROGRESION = ["C", "Am", "F", "G"] * 3 + ["C", "F", "G"]      # 15 compases de 2,0 s; el último lleva de vuelta al primero


def pista_musica():
    """Patrón de 120 BPM en do mayor: bajo en los pulsos 1 y 3, arpegio en corcheas, bombo suave y un shaker.
    Las colas se envuelven al principio para que el bucle del video empalme."""
    rng = np.random.default_rng(120)
    m = np.zeros((N, 2))
    t_b = tiempo(0.12)
    bombo = np.sin(2 * np.pi * np.cumsum(110 * (48 / 110) ** (t_b / 0.12)) / SR) * np.exp(-t_b / 0.035)
    for c, nombre in enumerate(PROGRESION):
        t0 = c * 4 * PULSO
        bajo, notas = ACORDES[nombre]
        for pulso in (0, 2):
            tb = tiempo(0.9)
            x = (np.sin(2 * np.pi * bajo * tb) + 0.25 * np.sin(2 * np.pi * 2 * bajo * tb)) * np.exp(-tb / 0.32)
            poner(m, cola(ataque(x, 6), 30) * 0.55, t0 + pulso * PULSO, envolver=True)
            poner(m, bombo * 0.5, t0 + pulso * PULSO, envolver=True)
        for k in range(8):                                  # corcheas
            f = notas[(0, 1, 2, 1, 0, 2, 1, 2)[k]]
            poner(m, s_pulsada(f, 0.5, 0.17) * 0.5, t0 + k * PULSO / 2, pan=0.3 if k % 2 else -0.3, envolver=True)
        for k in (1, 3, 5, 7):                              # shaker a contratiempo
            ts = tiempo(0.05)
            poner(m, ruido(rng, 0.05, 5000, 11000) * np.exp(-ts / 0.012) * 0.12, t0 + k * PULSO / 2, pan=0.2, envolver=True)
    return m


def leer_voz():
    """La voz tal cual está, convertida a 48 kHz estéreo y retrasada 1,0 s. No se cambia su nivel."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(AUDIO / "dialogo_110_v2.mp3"),
                        "-ar", str(SR), "-ac", "2", "-f", "f32le", "-"], capture_output=True)
    if r.returncode != 0:
        sys.exit(f"No se pudo leer la voz: {r.stderr.decode()[:300]}")
    v = np.frombuffer(r.stdout, dtype=np.float32).reshape(-1, 2).astype(np.float64)
    pista = np.zeros((N, 2))
    i = int(RETRASO_VOZ * SR)
    n = min(len(v), N - i)
    pista[i:i + n] = v[:n]
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


def construir(verboso=True):
    voz = leer_voz()
    lufs_voz, pico_voz = medir_pista(voz)
    fuera, bajo = pista_efectos()
    # 1) los golpes que suenan bajo la voz quedan 24 dB por debajo de ella (−14 − 24 = −38 LUFS medidos con R128)
    bajo = llevar_a(bajo, LUFS_VOZ_NOMINAL + DB_BAJO_VOZ)
    # 2) los del gancho y el cierre (sin voz) se suben hasta que la pista completa de efectos mida −18 LUFS
    #    sin pasar del techo de −3 dBFS (limitador suave con tanh). Si el techo no deja llegar, se dice lo que midió.
    def techo(x):
        return TECHO_GOLPES * np.tanh(x / TECHO_GOLPES)
    g = 1.0
    for _ in range(8):
        actual, _ = medir_pista(techo(fuera * g) + bajo)
        if abs(LUFS_GOLPES - actual) < 0.05:
            break
        g = min(g * 10 ** ((LUFS_GOLPES - actual) / 20), MAX_EMPUJE / max(1e-9, float(np.max(np.abs(fuera)))))
    fuera_g = techo(fuera * g)
    efectos = fuera_g + bajo
    musica = llevar_a(pista_musica(), LUFS_MUSICA)
    sin_musica = voz + efectos
    mezcla = sin_musica + musica
    guardar(AUDIO / "efectos_v2.wav", efectos)
    guardar(AUDIO / "musica_v2.wav", musica)
    guardar(AUDIO / "mezcla_sin_musica_v2.wav", sin_musica)
    guardar(AUDIO / "mezcla_v2.wav", mezcla)
    niveles = {
        "voz (dialogo_110_v2.mp3 retrasada 1,0 s, sin tocar)": [lufs_voz, pico_voz],
        "efectos.wav": list(medir(AUDIO / "efectos_v2.wav")),
        "efectos bajo la voz (1,0 a 27,9 s)": list(medir_pista(bajo)),
        "efectos fuera de la voz (gancho y cierre)": list(medir_pista(fuera_g)),
        "musica.wav": list(medir(AUDIO / "musica_v2.wav")),
        "mezcla_sin_musica.wav": list(medir(AUDIO / "mezcla_sin_musica_v2.wav")),
        "mezcla.wav": list(medir(AUDIO / "mezcla_v2.wav")),
    }
    pico_muestra = float(np.max(np.abs(mezcla)))
    if verboso:
        for k, (l, p) in niveles.items():
            print(f"  {k}: {l:.1f} LUFS, pico real {p:.1f} dBTP")
        print(f"  pico de muestra de la mezcla: {20 * np.log10(pico_muestra):.2f} dBFS")
    return niveles


def verificar():
    """Lee efectos.wav y comprueba que en cada segundo de la tabla empieza un sonido (subida de energía)."""
    with wave.open(str(AUDIO / "efectos_v2.wav"), "rb") as w:
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
    (AUDIO / "medidas_audio_v2.json").write_text(json.dumps(
        {"niveles_lufs_y_pico_dbtp": niveles,
         "golpes": [{"segundo": t, "sonido": n, "atado_a": q, "inicio_medido": i, "en_su_tiempo": bool(ok)}
                    for t, n, q, i, ok in filas]}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    if "--verificar" in sys.argv:
        for t, n, q, i, ok in filas:
            print(f"  {t:6.2f} s  {n:16s} inicio medido {('%.4f' % i) if i is not None else '—':>8s}  {'bien' if ok else 'REVISAR'}  ({q})")
    print(f"  golpes: {len(filas)}; fuera de su tiempo: {mal}")
    return niveles


if __name__ == "__main__":
    main()
