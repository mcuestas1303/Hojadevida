#!/usr/bin/env python3
"""Audio del short 3 de Tin & Tan, «Jensen Huang Is Back as Nvidia CEO After 11 Days», hecho con código (numpy + ffmpeg).

Uso (desde la carpeta del proyecto):
    python3 codigo/audio.py              # escribe 05_audio/efectos.wav, musica.wav, mezcla_sin_musica.wav y mezcla.wav
    python3 codigo/audio.py --verificar  # además lista cada golpe con el instante medido

Todo es determinista (ruido con semilla fija). Sin material de terceros. Los tiempos salen de codigo/tiempos.py (la voz
real). La voz (05_audio/dialogo_110.wav) entra en el fotograma 14, después del golpe de la atrapada del lápiz.
Niveles: golpes bajo la voz a unos -26 LUFS (-12 dB respecto a la voz); música en mi menor a 120 BPM a -24 LUFS, 6 dB
más baja durante la firma (de c = -24 a f14); sonidos de la firma del lápiz bumerán con los picos de
FIRMA_LAPIZ_BUMERAN.md §7 (whoosh atado a la velocidad del lápiz, -34 dBFS en el empalme, golpe de atrapada a -12 dBFS);
12 fotogramas de silencio de efectos y música antes del número; mezcla final a -14 LUFS con techo de -1 dBTP.
NADIE HA ESCUCHADO esta mezcla: todo lo de aquí se comprobó con medidas, no al oído.
"""
import json
import re
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tiempos as tm  # noqa: E402
from tiempos import C, FPS  # noqa: E402

PROY = Path(__file__).resolve().parent.parent
AUDIO = PROY / "05_audio"
SR = 48000
DUR = tm.DUR
N = int(SR * DUR)
PULSO = 0.5                   # 120 BPM: la rejilla del video
LUFS_MUSICA = -24.0
LUFS_BAJO_VOZ = -26.0
LUFS_MEZCLA = -14.0
TECHO_MEZCLA_DBTP = -1.0

# ---------------------------------------------------------------- golpes (sección 13 del prompt): (segundo, sonido, a qué va atado)
EVENTOS = [(14 / FPS, "pop_suave", "golpe de la clave «11» de la portada (fotograma 14)")]
EVENTOS += [(C(n), "clic", f"corte a la toma {n}") for n in range(2, 14)]
EVENTOS += [(C(14), "clic_borron", "corte con borrón al plano de cierre (toma 14)")]
EVENTOS += [(tm.T3_CIRCULO[0], "raspado_40", "círculo del 12 (toma 3)")]
EVENTOS += [(C(4), "revelado", "revelado de la mesa desde el desenfoque (toma 4)")]
EVENTOS += [(tm.T5_FLECHA[0], "raspado_50", "flecha del 17 al 23 (toma 5)"), (tm.T5_CIRCULO[0], "raspado_40", "círculo del 23 (toma 5)")]
EVENTOS += [(tm.T5_CRUCES + 0.1 * i, f"cruz_{i}", "cruz del calendario (toma 5)") for i in range(11)]
EVENTOS += [(tm.T7_BARRA[0], "deslizar", "barra de tenencia que crece (toma 7)")]
EVENTOS += [(tm.T9_HUANG, "pop", "marca de Huang (toma 9)"), (tm.T9_ALTMAN, "pop", "marca de Altman en mostaza (toma 9)")]
EVENTOS += [(tm.PICO_SUBIDA[0], "subida", "subida antes del pico (toma 10)")]
EVENTOS += [(tm.CONTADOR[0], "tictac", "contador de 0 a 4,382 (calla al llegar)")]
EVENTOS += [(tm.LLEGA, "ding", "llegada de 4,382: ding grave, acorde de mi mayor y golpe del zoom")]
EVENTOS += [(tm.T13_PASE[0], "whoosh_corto", "pase del lápiz de Tin a Tan (toma 13)")]
EVENTOS.sort(key=lambda e: e[0])
# Firma del lápiz bumerán (efectos.golpes_firma): (segundo, nombre, pico en dBFS)
FIRMA = [((tm.N - 17) / FPS, "chasquido", -20.0), ((tm.N - 15) / FPS, "whoosh_ida", -20.0),
         (0.0, "whoosh_vuelta", -18.0), (10 / FPS, "atrapada", -12.0)]


def tiempo(dur):
    return np.arange(int(round(dur * SR))) / SR


def ruido(rng, dur, f0=None, f1=None):
    n = int(round(dur * SR))
    x = rng.standard_normal(n)
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


def s_clic(f=1700.0):
    t = tiempo(0.03)
    return ataque(np.sin(2 * np.pi * f * t) * np.exp(-t / 0.004), 0.3) * 0.7


def s_tic(f):
    t = tiempo(0.03)
    return ataque(np.sin(2 * np.pi * f * t) * np.exp(-t / 0.006), 0.3) * 0.6


def s_raspado(rng, dur):
    """Raspado de lápiz sobre papel: ruido agudo con granos."""
    t = tiempo(dur)
    y = ruido(rng, dur, 2200, 8000) * (0.55 + 0.45 * np.sin(2 * np.pi * 23 * t) ** 2) * np.sin(np.pi * t / dur) ** 0.6
    return cola(ataque(y, 3), 20) * 0.6


def s_campana(f, dur, parciales=((1.0, 1.0), (2.76, 0.45), (5.4, 0.22), (8.93, 0.1))):
    t = tiempo(dur)
    y = np.zeros_like(t)
    for mult, amp in parciales:
        y += amp * np.sin(2 * np.pi * f * mult * t) * np.exp(-t / (dur * 0.28 / mult ** 0.5))
    return cola(ataque(y, 1.0), 30) * 0.6


def sonido(nombre, rng):
    if nombre == "clic":
        return s_clic()
    if nombre == "clic_borron":
        t = tiempo(0.09)
        y = 0.35 * ruido(rng, 0.09, 900, 5000) * np.exp(-t / 0.025)
        c = s_clic()
        y[:len(c)] += c
        return ataque(y, 0.3)
    if nombre in ("pop", "pop_suave"):
        x, t = barrido(260, 640, 0.09)
        return ataque(x * np.exp(-t / 0.03), 1.0) * (0.6 if nombre == "pop_suave" else 1.0)
    if nombre.startswith("raspado_"):
        return s_raspado(rng, int(nombre.split("_")[1]) / 100)
    if nombre == "revelado":
        x, t = barrido(140, 70, 0.22)
        return cola(ataque(x * np.exp(-t / 0.08), 4), 30) * 0.9
    if nombre.startswith("cruz_"):
        return s_tic(520.0 * 2 ** (int(nombre.split("_")[1]) / 12))          # 11 tics que suben un semitono cada uno
    if nombre == "deslizar":
        d = tm.T7_BARRA[1] - tm.T7_BARRA[0]
        t = tiempo(d)
        u = 1 - (1 - t / d) ** 3                                              # sigue el ease-out de la barra
        f = 220 * (660 / 220) ** u
        return cola(ataque(np.sin(2 * np.pi * np.cumsum(f) / SR) * (1 - 0.6 * u), 8), 60) * 0.5
    if nombre == "subida":
        d = tm.PICO_SUBIDA[1] - tm.PICO_SUBIDA[0]
        x, t = barrido(180, 900, d)
        y = (0.6 * x + 0.5 * ruido(rng, d, 500, 4000)) * (t / d) ** 2
        return cola(y, 25)
    if nombre == "tictac":
        d = tm.CONTADOR[1] - tm.CONTADOR[0]
        y = np.zeros(int((d + 0.05) * SR))
        for k in range(17):                                                   # calla al llegar (el ding es el último)
            p = k / 20
            i = int(round((1 - (1 - p) ** (1 / 3)) * d * SR))
            tic = s_tic(620.0 * 2 ** p)
            y[i:i + len(tic)] += tic[: len(y) - i]
        return y
    if nombre == "ding":
        y = np.zeros(int(1.6 * SR))
        c = s_campana(659.26, 1.1)                                            # mi5 grave de campana
        y[:len(c)] += c
        t = tiempo(1.6)
        for f, a in ((82.41, 0.5), (164.81, 0.45), (246.94, 0.35), (329.63, 0.32), (415.30, 0.30), (493.88, 0.22)):
            y += a * 0.5 * np.sin(2 * np.pi * f * t) * np.exp(-t / 0.55)      # acorde de mi mayor abierto (sol sostenido)
        x, tb = barrido(110, 50, 0.14)
        y[:len(x)] += 0.8 * x * np.exp(-tb / 0.05)                            # golpe del zoom
        return cola(ataque(y, 1.5), 80)
    if nombre == "whoosh_corto":
        d = 8 / FPS
        t = tiempo(d)
        return ruido(rng, d, 500, 3000) * np.sin(np.pi * t / d) ** 2
    raise ValueError(nombre)


def _velocidad_lapiz():
    """Velocidad (px por fotograma) del lápiz de la firma en la ida (15 intervalos) y en la vuelta (10)."""
    sys.path.insert(0, str(PROY.parent.parent / "herramientas"))
    import render as R
    import efectos as fx
    def v(c):
        a, b = fx._vuelo(c, R.GEO), fx._vuelo(c + 0.25, R.GEO)
        return 4 * float(np.hypot(b[0] - a[0], b[1] - a[1]))
    return [v(c) for c in np.linspace(-15, -0.25, 60)], [v(c) for c in np.linspace(0, 9.75, 40)]


def sonidos_firma(rng):
    """Los cuatro sonidos de la firma con sus picos absolutos (dBFS). El whoosh sigue la velocidad del lápiz y vale
    -34 dBFS a los dos lados del empalme: es uno solo."""
    def db(x):
        return 10 ** (x / 20)
    ida, vuelta = _velocidad_lapiz()
    out = {}
    t = tiempo(0.1)
    y = ruido(rng, 0.1, 1000, 4000) * (t / 0.1) ** 2
    out["chasquido"] = cola(y, 4) / np.max(np.abs(y)) * db(-20)
    d = 15 / FPS
    t = tiempo(d)
    env = np.interp(t, np.linspace(0, d, len(ida)), ida)
    env = db(-34) + (db(-20) - db(-34)) * (env - env[-1]) / (env.max() - env[-1])
    for tc in (1 / FPS, 13 / FPS):                                             # dos pulsos al cruzar la horizontal
        env = env * (1 + 0.35 * np.exp(-((t - tc) / 0.012) ** 2))
    f = 1800 * (900 / 1800) ** (t / d)
    port = np.sin(2 * np.pi * np.cumsum(f) / SR)
    y = (0.75 * ruido(rng, d, 600, 2500) + 0.25 * port)
    out["whoosh_ida"] = ataque(np.clip(1.5 * y / np.max(np.abs(y)), -1, 1) * np.clip(env, 0, db(-20)), 5)
    d = 10 / FPS
    t = tiempo(d)
    env = np.interp(t, np.linspace(0, d, len(vuelta)), vuelta)
    env = db(-34) + (db(-18) - db(-34)) * np.clip((env - env[0]) / (env.max() - env[0]), 0, 1)
    f = 900 * (1700 / 900) ** (t / d)
    y = 0.75 * ruido(rng, d, 600, 2500) + 0.25 * np.sin(2 * np.pi * np.cumsum(f) / SR)
    out["whoosh_vuelta"] = cola(np.clip(1.5 * y / np.max(np.abs(y)), -1, 1) * env, 30)
    t = tiempo(0.12)
    y = np.sin(2 * np.pi * 1200 * t) * np.exp(-t / 0.012) + 0.6 * ruido(rng, 0.12, 700, 3000) * np.exp(-t / 0.018)
    x, tb = barrido(300, 520, 0.05)
    y[:len(x)] += 0.5 * x * np.exp(-tb / 0.02)
    y = cola(ataque(y, 0.4), 20)
    out["atrapada"] = y / np.max(np.abs(y)) * db(-12)
    return out


def poner(pista, x, t, pan=0.0, envolver=False):
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


def ventana_silencio(extra_db_firma=False):
    """Ganancia por muestra: 0 en los 12 fotogramas de silencio antes del número (fundidos de 20 ms)."""
    g = np.ones(N)
    a, b = int(tm.PICO_SILENCIO[0] * SR), int(tm.PICO_SILENCIO[1] * SR)
    r = int(0.02 * SR)
    g[a:b] = 0.0
    g[a - r:a] = np.linspace(1, 0, r)
    g[b:b + r] = np.linspace(0, 1, r)
    return g[:, None]


def pista_efectos():
    rng = np.random.default_rng(20261123)
    bajo, firma = np.zeros((N, 2)), np.zeros((N, 2))
    for t, nombre, _ in EVENTOS:
        poner(bajo, sonido(nombre, rng), t)
    sf = sonidos_firma(rng)
    for t, nombre, _ in FIRMA:
        poner(firma, sf[nombre], t)                      # al centro: el pico absoluto pedido en cada canal
    return bajo, firma


# mi menor (eólico): bajo y notas del acompañamiento de cada compás de 2,0 s
ACORDES = {"Em": (82.41, (196.00, 246.94, 329.63)), "C": (65.41, (196.00, 261.63, 329.63)),
           "D": (73.42, (220.00, 293.66, 369.99)), "Am": (55.00 * 2, (220.00, 261.63, 329.63)),
           "Bm": (61.74 * 2, (246.94, 293.66, 369.99))}


def pista_musica():
    """Mi menor a 120 BPM: ostinato de bajo en corcheas, colchón suave y un punteo cada negra. Compases de 2,0 s; las
    colas se envuelven al principio para que el bucle empalme. Calla en los 12 fotogramas de silencio antes del número."""
    rng = np.random.default_rng(1205)
    m = np.zeros((N, 2))
    compases = int(np.ceil(DUR / 2.0))
    prog = (["Em", "C", "D", "Em", "Em", "Am", "Bm", "Em"] * 4)[:compases]
    for c, nombre in enumerate(prog):
        t0 = c * 2.0
        bajo, notas = ACORDES[nombre]
        dur_c = min(2.0, DUR - t0)
        tp = tiempo(dur_c)
        colchon = sum(np.sin(2 * np.pi * f * tp + i) for i, f in enumerate(notas)) / 3
        env = np.minimum(1, tp / 0.4) * np.minimum(1, (dur_c - tp) / 0.4)
        poner(m, colchon * env * 0.16, t0, envolver=True)
        for k in range(8):                                   # corcheas
            tk = t0 + k * PULSO / 2
            if tk >= DUR - 1e-9:
                continue
            tb = tiempo(0.22)
            f = bajo * (2 if k in (3, 7) else 1)
            x = (np.sin(2 * np.pi * f * tb) + 0.3 * np.sin(2 * np.pi * 2 * f * tb)) * np.exp(-tb / 0.09)
            poner(m, cola(ataque(x, 5), 20) * (0.5 if k % 2 == 0 else 0.3), tk, envolver=True)
            if k % 2 == 0:
                tn = tiempo(0.45)
                fn = notas[(0, 2, 1, 2)[k // 2]]
                y = (np.sin(2 * np.pi * fn * tn) + 0.3 * np.sin(2 * np.pi * 2 * fn * tn)) * np.exp(-tn / 0.16)
                poner(m, cola(ataque(y, 4), 15) * 0.26, tk, pan=0.3 if k % 4 else -0.3, envolver=True)
            else:
                ts = tiempo(0.05)
                poner(m, ruido(rng, 0.05, 5000, 11000) * np.exp(-ts / 0.012) * 0.07, tk, pan=0.2, envolver=True)
    return m


def atenuacion_firma():
    """Música 6 dB más baja durante la firma: de c = -24 a f14, con rampas de 0,1 s (FIRMA, §7 punto 5)."""
    g = np.ones(N)
    bajo = 10 ** (-6 / 20)
    a, b, r = int((DUR - 24 / FPS) * SR), int(14 / FPS * SR), int(0.1 * SR)
    g[a:] = bajo
    g[a - r:a] = np.linspace(1, bajo, r)
    g[:b] = bajo
    g[b:b + r] = np.linspace(bajo, 1, r)
    return g[:, None]


def leer_voz():
    """El diálogo, a 48 kHz estéreo, desde el fotograma 14. No se cambia su nivel aquí."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(AUDIO / "dialogo_110.wav"),
                        "-ar", str(SR), "-ac", "2", "-f", "f32le", "-"], capture_output=True)
    if r.returncode != 0:
        sys.exit(f"No se pudo leer la voz: {r.stderr.decode()[:300]}")
    v = np.frombuffer(r.stdout, dtype=np.float32).reshape(-1, 2).astype(np.float64)
    pista = np.zeros((N, 2))
    i = int(round(tm.VOZ_ENTRA * SR))
    n = min(len(v), N - i)
    pista[i:i + n] = v[:n]
    return pista


def guardar(ruta, x):
    y = np.clip(np.round(x * 32767.0), -32768, 32767).astype("<i2")
    with wave.open(str(ruta), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(y.tobytes())


def medir(ruta):
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
    for _ in range(3):
        actual, _ = medir_pista(x)
        x = x * 10 ** ((lufs - actual) / 20)
    return x


def limitar(x, techo_db):
    ent, sal = AUDIO / "_lim_in.wav", AUDIO / "_lim_out.wav"
    guardar(ent, x)
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
    bajo, firma = pista_efectos()
    silencio = ventana_silencio()
    bajo = llevar_a(bajo, LUFS_BAJO_VOZ) * silencio
    efectos = bajo + firma
    musica = llevar_a(pista_musica(), LUFS_MUSICA) * silencio * atenuacion_firma()
    sin_musica = voz + efectos
    mezcla = sin_musica + musica
    antes = medir_pista(mezcla)
    limitada, techo = False, TECHO_MEZCLA_DBTP - 0.3
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
    a, b = int(tm.PICO_SILENCIO[0] * SR) + 1000, int(tm.PICO_SILENCIO[1] * SR) - 1000
    niveles = {
        "voz (dialogo_110.wav, desde el fotograma 14, sin tocar)": [lufs_voz, pico_voz],
        "efectos.wav": list(medir(AUDIO / "efectos.wav")),
        "efectos bajo la voz": list(medir_pista(bajo)),
        "musica.wav": list(medir(AUDIO / "musica.wav")),
        "mezcla_sin_musica.wav (sin ganancia final)": list(medir(AUDIO / "mezcla_sin_musica.wav")),
        "mezcla antes de la ganancia final": list(antes),
        "mezcla.wav (final)": list(medir(AUDIO / "mezcla.wav")),
    }
    extra = {
        "pico de efectos y música en el silencio antes del número (dBFS)":
            round(float(20 * np.log10(np.max(np.abs((efectos + musica)[a:b])) + 1e-9)), 1),
        "picos de la firma (dBFS): chasquido, whoosh de ida, whoosh de vuelta, atrapada":
            [round(float(20 * np.log10(np.max(np.abs(firma[int(t * SR):int(t * SR) + int(d * SR)])) + 1e-9)), 1)
             for (t, _, _), d in zip(FIRMA, (0.1, 0.5, 0.3, 0.12))],
        "whoosh a los dos lados del empalme (dBFS, últimos y primeros 20 ms)":
            [round(float(20 * np.log10(np.max(np.abs(firma[-960:])) + 1e-9)), 1),
             round(float(20 * np.log10(np.max(np.abs(firma[:960])) + 1e-9)), 1)],
        "limitador en la mezcla final": limitada,
    }
    if verboso:
        for k, (l, p) in niveles.items():
            print(f"  {k}: {l:.1f} LUFS, pico real {p:.1f} dBTP")
        for k, v in extra.items():
            print(f"  {k}: {v}")
    niveles.update(extra)
    return niveles


def verificar():
    """Lee efectos.wav y comprueba que en cada segundo de la tabla empieza un sonido (subida de energía)."""
    with wave.open(str(AUDIO / "efectos.wav"), "rb") as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").reshape(-1, 2).astype(np.float64) / 32768
    mono = np.abs(x).max(axis=1)
    filas, mal = [], 0
    for t, nombre, que in EVENTOS + [(t, n, "firma del lápiz bumerán") for t, n, _ in FIRMA if n in ("chasquido", "atrapada")]:
        i = int(round(t * SR))
        antes = mono[max(0, i - int(0.004 * SR)):i]
        despues = mono[i:i + int(0.05 * SR)]
        pico = despues.max() if len(despues) else 0.0
        umbral = max(0.25 * pico, (antes.max() if len(antes) else 0.0) * 1.5, 1e-4)
        sobre = np.nonzero(despues >= umbral)[0]
        lento = nombre in ("subida", "deslizar", "whoosh_corto", "chasquido") or nombre.startswith("raspado")
        if pico <= 1e-4 or len(sobre) == 0:
            inicio, ok = None, False
        else:
            inicio = t + sobre[0] / SR
            ok = (inicio - t) <= (0.05 if lento else 0.012)
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
            print(f"  {t:6.2f} s  {n:14s} inicio medido {('%.4f' % i) if i is not None else '—':>8s}  {'bien' if ok else 'REVISAR'}  ({q})")
    print(f"  golpes: {len(filas)}; fuera de su tiempo: {mal}")
    return niveles


if __name__ == "__main__":
    main()
