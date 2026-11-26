#!/usr/bin/env python3
"""Sonidos de la prueba hechos con código (numpy), atados al fotograma de cada evento. 0 créditos.
Uso: python3 sonido.py salida/eventos.json salida/sonido.wav"""
import json
import sys
import wave

import numpy as np

SR = 48000
rng = np.random.default_rng(1977)


def env(n, ataque, caida):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(ataque, 1e-4)) * np.exp(-t / caida)


def filtra(x, corte):                       # paso bajo de un polo
    a = np.exp(-2 * np.pi * corte / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i, v in enumerate(x):
        acc = (1 - a) * v + a * acc
        y[i] = acc
    return y


def golpe(dur=0.28, tono=110, cuerpo=0.9):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = tono * (1 + 2.2 * np.exp(-t / 0.018))
    bajo = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.001, 0.07)
    chasq = filtra(rng.standard_normal(n), 2600) * env(n, 0.0005, 0.016) * 2.2
    return cuerpo * bajo + chasq


def choque(dur=0.7, corte=900):
    n = int(dur * SR)
    return filtra(rng.standard_normal(n), corte) * env(n, 0.002, 0.16) * 3.0 + golpe(dur, 62, 1.1)[:n]


def madera(dur=0.6):
    n = int(dur * SR)
    x = np.zeros(n)
    for k in range(9):
        i = int(rng.uniform(0, 0.25) * SR)
        g = golpe(0.12, rng.uniform(260, 620), 0.5)
        x[i:i + len(g)] += g[:n - i] * rng.uniform(0.4, 1.0)
    return x + choque(dur, 1500) * 0.5


def explosion(dur=1.6):
    n = int(dur * SR)
    t = np.arange(n) / SR
    ruido = filtra(rng.standard_normal(n), 420) * env(n, 0.004, 0.45) * 5.0
    sub = np.sin(2 * np.pi * np.cumsum(48 * (1 + 1.4 * np.exp(-t / 0.08))) / SR) * env(n, 0.002, 0.5) * 1.3
    return ruido + sub + golpe(0.3, 80, 1.2).tolist().__len__() * 0 + np.pad(golpe(0.3, 80, 1.2), (0, n - int(0.3 * SR)))


def silbido(dur=0.22, sube=True):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = rng.standard_normal(n)
    y = filtra(x, 3200) - filtra(x, 700)
    forma = np.sin(np.pi * t / dur) ** 2
    return y * forma * 1.6


def implosion(dur=0.55):
    x = explosion(dur + 0.2)[: int(dur * SR)][::-1].copy()      # una explosión al revés: el sonido se recoge
    return x * np.linspace(0.2, 1.0, len(x))


def fuego(dur=0.5):
    n = int(dur * SR)
    return (filtra(rng.standard_normal(n), 1800) - filtra(rng.standard_normal(n), 300)) * env(n, 0.05, 0.25) * 1.5


SONIDOS = {"silbido_caida": lambda: silbido(0.4), "choque_suelo": choque, "silbido": silbido, "golpe": golpe,
           "choque_madera": madera, "fuego_enciende": fuego, "explosion": explosion, "choque_pilar": lambda: choque(0.6, 600),
           "golpe_doble": lambda: np.concatenate([golpe(), np.zeros(1)])  + np.pad(golpe(0.28, 150, 0.8), (int(0.03 * SR), 0))[: int(0.28 * SR) + 1],
           "implosion": implosion, "estallido_final": lambda: golpe(0.3, 200, 0.7) + np.pad(silbido(0.2), (0, int(0.3 * SR) - int(0.2 * SR)))}
NIVEL = {"explosion": 1.0, "choque_suelo": 0.8, "golpe": 0.85, "golpe_doble": 0.9, "choque_madera": 0.75, "implosion": 0.8,
         "choque_pilar": 0.6, "silbido": 0.35, "silbido_caida": 0.4, "fuego_enciende": 0.4, "estallido_final": 0.6}


def main():
    d = json.load(open(sys.argv[1]))
    total = int((d["cuadros"] / d["fps"] + 0.6) * SR)
    mezcla = np.zeros(total)
    for e in d["eventos"]:
        s = SONIDOS[e["nombre"]]()
        s = s / (np.max(np.abs(s)) + 1e-9) * NIVEL[e["nombre"]]
        i = int(e["cuadro"] / d["fps"] * SR)
        s = s[: total - i]
        mezcla[i:i + len(s)] += s
    mezcla = np.tanh(mezcla * 1.1) * 0.89                      # limitador suave; pico ≈ -1 dBFS
    with wave.open(sys.argv[2], "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((mezcla * 32767).astype("<i2").tobytes())
    print("pico", round(float(np.max(np.abs(mezcla))), 3), "duración", round(total / SR, 2))


if __name__ == "__main__":
    main()
