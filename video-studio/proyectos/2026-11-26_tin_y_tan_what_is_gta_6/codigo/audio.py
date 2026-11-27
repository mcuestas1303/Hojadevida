#!/usr/bin/env python3
"""Sonido del short 4 de Tin & Tan (TIN-EN-S-004): efectos, percusión y mezcla. Todo por código (numpy), 0 créditos.

Lee 05_audio/linea_de_tiempo.json (voz y fotogramas) y los eventos que marca el guion del motor
(`eventos.json` de la grabación: cada golpe, choque, explosión e implosión con su fotograma) y escribe:
  05_audio/efectos.wav, 05_audio/musica.wav, 05_audio/mezcla_final.wav y 05_audio/medidas_audio.json.
Reglas (dirección, sección 5): el golpe suena en el contacto o un fotograma antes; nada de efectos en la pausa de cada
golpe (K−6 a K−1); silencio total, también de música, antes del remate; explosión en la expansión; música solo de
percusión a 120 pulsos por minuto (un pulso cada 15 f), sin melodía; voz a −14 LUFS; −6 dB de música desde c −24.
Nadie ha oído estos sonidos: los valida un oído humano.

Uso: python3 audio.py <eventos.json>
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
SR, FPS = 48000, 30
TL = json.loads((AUDIO / "linea_de_tiempo.json").read_text(encoding="utf-8"))
N, K = TL["N"], TL["K"]
DUR = N / FPS
rng = np.random.default_rng(4004)


def t_(d):
    return np.arange(int(d * SR)) / SR


def ruido(d, f0=None, f1=None):
    x = rng.standard_normal(int(d * SR))
    if f0 is None:
        return x
    X = np.fft.rfft(x); fr = np.fft.rfftfreq(len(x), 1 / SR)
    X[(fr < f0) | (fr > f1)] = 0
    y = np.fft.irfft(X, len(x))
    return y / (np.abs(y).max() + 1e-9)


def env(d, ataque=0.002, caida=6.0):
    t = t_(d)
    return np.minimum(1, t / ataque) * np.exp(-caida * t / d)


def barrido(f_a, f_b, d):
    t = t_(d)
    f = f_a * (f_b / f_a) ** (t / d)
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


def tono(f, d, caida=6.0, parciales=((1, 1.0),)):
    t = t_(d)
    return sum(a * np.sin(2 * np.pi * f * k * t) for k, a in parciales) * env(d, 0.001, caida)


def suma(*xs):
    n = max(len(x) for x in xs); y = np.zeros(n)
    for x in xs:
        y[:len(x)] += x
    return y


def retraso(x, s):
    return np.concatenate([np.zeros(int(s * SR)), x])


def golpe(f=150.0, d=0.14):
    return suma(barrido(f, f * 0.33, d) * env(d, 0.001, 5), 0.5 * ruido(0.03, 800, 5000) * env(0.03, 0.0005, 5))


def madera(f=240.0, d=0.28):
    return suma(tono(f, d, 9, ((1, 1), (2.3, 0.5), (3.9, 0.25))), 0.6 * ruido(0.06, 300, 4000) * env(0.06, 0.0005, 5))


def silbido(f_a=900, f_b=2600, d=0.16):
    x = ruido(d, 500, 6000) * np.sin(np.pi * t_(d) / d) ** 2
    return 0.7 * x + 0.3 * barrido(f_a, f_b, d) * np.sin(np.pi * t_(d) / d) ** 2


def cajas():
    return suma(*[retraso(0.6 * madera(rng.uniform(300, 700), 0.09), rng.uniform(0, 0.45)) for _ in range(6)])


def metal(f):
    return tono(f, 0.3, 7, ((1, 1), (2.76, 0.4), (5.4, 0.2)))


def chispas(d=0.35, n=22):
    y = np.zeros(int(d * SR))
    for _ in range(n):
        i = rng.integers(0, len(y) - 300); y[i:i + 200] += ruido(200 / SR, 3000, 12000)[:200] * np.linspace(1, 0, 200) * rng.uniform(0.3, 1)
    return y


SONIDOS = {  # nombre: (función, pico en dBFS)
    "trazo_de_tinta": (lambda: ruido(16 / FPS, 1500, 7000) * (0.55 + 0.45 * np.sin(2 * np.pi * 23 * t_(16 / FPS))) * np.sin(np.pi * t_(16 / FPS) / (16 / FPS)) ** 0.5, -24),
    "choque_suelo": (lambda: suma(golpe(90, 0.3), 0.4 * ruido(0.15, 100, 1200) * env(0.15)), -15),
    "cajas_caen": (cajas, -20),
    "silbido": (silbido, -22),
    "silbido_corto": (lambda: silbido(1200, 3000, 0.1), -24),
    "silbido_sube": (lambda: silbido(500, 3200, 0.22), -22),
    "silbido_caida": (lambda: silbido(2800, 500, 0.16), -26),
    "golpe": (golpe, -13),
    "golpe_agudo": (lambda: golpe(190, 0.12), -13),
    "golpe_grave": (lambda: golpe(115, 0.18), -13),
    "golpe_doble": (lambda: suma(golpe(150, 0.16), retraso(golpe(110, 0.2), 0.012)), -12),
    "choque_madera": (madera, -15),
    "choque_madera_bajo": (madera, -20),      # v4 (S1): el que acompaña al mazazo, bajo la voz
    "choque_madera_agudo": (lambda: madera(420, 0.18), -17),
    "choque_pilar": (lambda: suma(madera(160, 0.35), golpe(70, 0.3)), -18),   # v2: cae sobre «GTA six»; a −14 el reconocedor oía un «it» de más
    "roce_suelo": (lambda: ruido(0.4, 300, 2500) * np.sin(np.pi * t_(0.4) / 0.4) ** 1.5, -24),
    "postes_caen": (lambda: suma(*[retraso(metal(f), i * 3 / FPS) for i, f in enumerate((1250, 1480, 1120, 1660))]), -19),
    "bloqueo_tinta": (lambda: suma(tono(900, 0.14, 8, ((1, 1), (1.5, 0.6))), ruido(0.02, 1000, 8000) * env(0.02, 0.0005, 4)), -14),
    "vidrio_grieta": (lambda: suma(ruido(0.1, 3000, 12000) * env(0.1, 0.0005, 6), *[retraso(0.4 * tono(f, 0.2, 9), s) for f, s in ((3400, 0.01), (4700, 0.04), (5900, 0.07))]), -17),
    "chispas": (chispas, -22),
    "fuego_enciende": (lambda: ruido(0.45, 80, 900) * (t_(0.45) / 0.45) ** 1.5 * env(0.45, 0.001, 0.8), -22),
    "fuego_crece": (lambda: ruido(0.6, 60, 1100) * np.sin(np.pi * t_(0.6) / 0.6), -20),
    "baston_golpe": (lambda: suma(tono(320, 0.16, 8, ((1, 1), (2.0, 0.5))), ruido(0.02, 800, 6000) * env(0.02, 0.0005, 4)), -13),
    "baston_golpe_grave": (lambda: suma(tono(270, 0.18, 8, ((1, 1), (2.0, 0.5))), ruido(0.02, 800, 6000) * env(0.02, 0.0005, 4)), -13),
    "mazo_golpe": (lambda: suma(barrido(95, 38, 0.26) * env(0.26, 0.001, 7.0), 0.5 * ruido(0.08, 100, 1500) * env(0.08)), -16),   # v4 (S1): más bajo y más corto, cae sobre «seventeen and over»
    "campanilla_caja": (lambda: tono(2093, 0.7, 5, ((1, 1), (1.5, 0.35), (2.0, 0.2))), -18),
    "subida": (lambda: (0.6 * ruido(11 / FPS, 400, 5000) + 0.4 * barrido(180, 900, 11 / FPS)) * (t_(11 / FPS) / (11 / FPS)) ** 2, -18),
    "explosion": (lambda: suma(barrido(70, 28, 1.3) * env(1.3, 0.004, 3.5), 0.8 * ruido(1.0, 40, 3000) * env(1.0, 0.002, 4.5)), -8),
    "cola_explosion": (lambda: suma(0.8 * ruido(1.3, 30, 300) * env(1.3, 0.05, 3), 0.25 * chispas(1.0, 40)), -23),   # v4 (S4): no pisa el arranque de «thirteen years»
    "implosion": (lambda: (0.5 * barrido(2400, 90, 0.56) + 0.5 * ruido(0.56, 200, 6000)) * (t_(0.56) / 0.56) ** 1.8, -13),
    "gotas": (lambda: suma(*[retraso(0.5 * tono(rng.uniform(700, 1500), 0.06, 7), rng.uniform(0, 0.25)) for _ in range(6)]), -24),
    "asterisco_tic": (lambda: suma(tono(2500, 0.03, 6), 0.5 * ruido(0.012, 2000, 9000) * env(0.012, 0.0003, 4)), -20),
    "escurre": (lambda: (0.6 * ruido(0.5, 400, 3000) + 0.4 * barrido(900, 180, 0.5)) * np.sin(np.pi * t_(0.5) / 0.5), -24),
    "atrapa": (lambda: suma(golpe(210, 0.07), ruido(0.015, 1500, 7000) * env(0.015, 0.0003, 4)), -18),
    # firma del lápiz bumerán (FIRMA_LAPIZ_BUMERAN.md, sección 7)
    "firma_whoosh_regreso": (lambda: silbido(2200, 700, 10 / FPS), -18),
    "firma_atrapada": (lambda: suma(golpe(220, 0.08), ruido(0.02, 1500, 7000) * env(0.02, 0.0003, 4)), -12),
    "firma_chasquido": (lambda: ruido(3 / FPS, 1500, 8000) * env(3 / FPS, 0.0005, 5), -20),
    "firma_whoosh_ida": (lambda: silbido(700, 2400, 15 / FPS), -20),
}


def db(x):
    return 10 ** (x / 20)


def poner(pista, x, f, pico_db):
    x = x / (np.abs(x).max() + 1e-9) * db(pico_db)
    a = int(f / FPS * SR)
    if a >= len(pista):
        return
    x = x[:len(pista) - a]
    pista[a:a + len(x)] += x


def pausas():
    """Tramos sin efectos (la pausa de cada golpe) y el silencio total antes del remate. (inicio, fin, también música)"""
    ks = [K[k] for k in ("K1", "K2", "K3", "KB", "K4", "K5", "K6")]
    return [(k - 6, k - 1, False) for k in ks] + [(K["KR"] - 7, K["KR"] - 1, True)]      # v4 (S6): 6 f de silencio total medidos


def puerta(solo_total=False):
    g = np.ones(int(DUR * SR))
    r = int(0.012 * SR)
    for a, b, total in pausas():
        if solo_total and not total:
            continue
        i, j = int(a / FPS * SR), int(b / FPS * SR)
        g[i:j] = 0
        g[max(0, i - r):i] = np.minimum(g[max(0, i - r):i], np.linspace(1, 0, min(r, i)))
    return g


def pista_efectos(eventos):
    p = np.zeros(int(DUR * SR))
    usados = []
    for e in eventos:
        if e["nombre"] not in SONIDOS:
            raise SystemExit(f"Falta el sonido «{e['nombre']}»")
        fn, pico = SONIDOS[e["nombre"]]
        poner(p, fn(), e["cuadro"], pico); usados.append((e["cuadro"], e["nombre"], pico))
    for f, n in ((0, "firma_whoosh_regreso"), (10, "firma_atrapada"), (N - 17, "firma_chasquido"), (N - 15, "firma_whoosh_ida")):
        fn, pico = SONIDOS[n]; poner(p, fn(), f, pico); usados.append((f, n, pico))
    # crepitar del fuego: del encendido al choque final, y la cola hasta la implosión
    for a, b, nivel in ((K["tele_punta"] + 12, K["tele_choque"], -34), (K["enfria"], K["implosion"], -36)):
        d = (b - a) / FPS
        poner(p, chispas(d, int(d * 28)) + 0.4 * ruido(d, 100, 700), a, nivel)
    g = puerta()
    # el contacto (K−1 / K) no se calla: la puerta termina en K−1
    return p * g, sorted(usados)


def pista_musica():
    """Solo percusión, 120 pulsos por minuto (un pulso cada 15 f). Sube una capa tras cada golpe; calla en las pausas."""
    p = np.zeros(int(DUR * SR))
    bombo = lambda: barrido(110, 42, 0.16) * env(0.16, 0.001, 5)
    palo = lambda: tono(420, 0.05, 6, ((1, 1), (2.4, 0.4)))
    plato = lambda: ruido(0.04, 6000, 13000) * env(0.04, 0.0005, 5)
    caja = lambda: suma(ruido(0.09, 900, 6000) * env(0.09, 0.0005, 5), 0.5 * tono(190, 0.08, 7))
    capas = [(30, 1), (K["K1"], 2), (K["K2"], 3), (K["K3"], 4), (K["K4"], 5), (K["K5"], 6), (TL_f("T9"), 1), (K["K6"] + 20, 0.5)]
    def nivel(f):
        n = 0
        for a, v in capas:
            if f >= a:
                n = v
        return n
    for f in range(30, N - 30, 15):
        n = nivel(f); pulso = (f - 30) // 15
        if K["KR"] - 8 <= f < TL_f("T9") or n == 0:
            continue
        if n == 0.5:
            if pulso % 2 == 0:
                poner(p, palo(), f, -30)
            continue
        poner(p, bombo(), f, -22 if pulso % 2 == 0 else -27)
        if n >= 2:
            poner(p, plato(), f + 7.5, -32)
        if n >= 3 and pulso % 2 == 1:
            poner(p, caja(), f, -26)
        if n >= 4:
            poner(p, palo(), f + 3.75, -31); poner(p, palo(), f + 11.25, -31)
        if n >= 5 and pulso % 4 == 3:
            poner(p, caja(), f + 7.5, -29)
        if n >= 6:
            poner(p, plato(), f + 3.75, -34); poner(p, plato(), f + 11.25, -34)
    g = puerta()
    a = int((N - 24) / FPS * SR)
    g[a:] *= db(-6)
    return p * g


def TL_f(lid):
    return next(l["f0"] for l in TL["lineas"] if l["id"] == lid)


def leer(ruta):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(ruta), "-ar", str(SR), "-ac", "1", "-f", "f32le", "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32).astype(np.float64)


def guardar(ruta, x):
    y = np.clip(np.round(x * 32767.0), -32768, 32767).astype("<i2")
    with wave.open(str(ruta), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(y.tobytes())


def medir(ruta):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(ruta), "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True)
    res = r.stderr[r.stderr.rfind("Summary:"):]
    lufs = float(re.search(r"I:\s+(-?[\d.]+)", res).group(1)); pico = float(re.search(r"Peak:\s+(-?[\d.]+)", res).group(1))
    return lufs, pico


def main():
    ev = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))["eventos"]
    n = int(DUR * SR)
    voz = leer(AUDIO / "dialogo_110.wav"); voz = np.pad(voz, (0, max(0, n - len(voz))))[:n]
    efectos, usados = pista_efectos(ev)
    musica = pista_musica() * db(12.0)       # ≈ −30 LUFS: por debajo de la voz y de los golpes
    # la música y los efectos largos se agachan bajo la voz (envolvente de la voz, 60 ms)
    e = np.abs(voz); k = int(0.06 * SR); e = np.convolve(e, np.ones(k) / k, mode="same")
    agacha = 1 - 0.45 * np.clip(e / 0.05, 0, 1)
    total = puerta(solo_total=True)
    # v4 (S3): la línea de Tan «Subscribe. We check the facts.» estaba ≈ 4 dB por debajo de las de Tin; se sube 3 dB con rampas de 30 ms
    lc = next(l for l in TL["lineas"] if l["id"] == "C"); c0, c1 = int(lc["f0"] / FPS * SR), int(lc["f1"] / FPS * SR); r = int(0.03 * SR); gan = np.ones(n)
    gan[c0:c1] = db(3.0); gan[max(0, c0 - r):c0] = np.linspace(1, db(3.0), min(r, c0)); gan[c1:c1 + r] = np.linspace(db(3.0), 1, len(gan[c1:c1 + r]))
    voz = voz * gan
    # v4 (S1): los efectos se agachan más bajo la voz (antes 0.75 + 0.25·agacha)
    mezcla = voz + efectos * (0.55 + 0.45 * agacha) + musica * agacha
    mezcla *= total
    guardar(AUDIO / "efectos.wav", efectos); guardar(AUDIO / "musica.wav", musica)
    guardar(AUDIO / "_m.wav", mezcla)
    l, p = medir(AUDIO / "_m.wav")
    mezcla *= db(-14.0 - l)
    techo = db(-1.6)
    if np.abs(mezcla).max() > techo:             # limitador suave solo en los picos (la explosión)
        s = np.abs(mezcla) > techo * 0.8
        mezcla[s] = np.sign(mezcla[s]) * (techo * 0.8 + (techo * 0.2) * np.tanh((np.abs(mezcla[s]) - techo * 0.8) / (techo * 0.2)))
    guardar(AUDIO / "mezcla_final.wav", mezcla)
    (AUDIO / "_m.wav").unlink()
    l2, p2 = medir(AUDIO / "mezcla_final.wav")
    guardar(AUDIO / "_v.wav", voz); lv, pv = medir(AUDIO / "_v.wav"); (AUDIO / "_v.wav").unlink()
    lm, _ = medir(AUDIO / "musica.wav"); le, pe = medir(AUDIO / "efectos.wav")
    i0, i1 = int((K["KR"] - 6) / FPS * SR), int((K["KR"] - 1) / FPS * SR)
    medidas = {"mezcla_LUFS": l2, "mezcla_pico_dBTP": p2, "voz_LUFS": lv, "musica_LUFS": lm, "efectos_LUFS": le, "efectos_pico_dBFS": pe,
               "silencio_total_f": [K["KR"] - 6, K["KR"] - 1], "pico_en_el_silencio": float(np.abs(mezcla[i0:i1]).max()),
               "eventos": [{"f": f, "sonido": s, "pico_dBFS": d} for f, s, d in usados]}
    (AUDIO / "medidas_audio.json").write_text(json.dumps(medidas, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print({k: v for k, v in medidas.items() if k != "eventos"}, len(usados), "eventos")


if __name__ == "__main__":
    main()
