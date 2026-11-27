#!/usr/bin/env python3
"""Línea de tiempo del short 4 de Tin & Tan (TIN-EN-S-004) con la voz real.

Corta cada línea de las dos voces (una generación cada una; NO se regeneran) por sus pausas medidas
(`silencedetect=noise=-35dB:d=0.12`; texto de cada tramo comprobado con `revisar_voz.py --tramos`), la acelera al
110 % sin cambiar el tono, cierra las pausas internas y coloca cada línea en su fotograma según la regla de la
dirección (4.1): Tin empieza el dato dos fotogramas después del contacto. Con las duraciones reales calcula TODOS los
fotogramas de la coreografía (K = contacto de cada golpe).

Escribe: 05_audio/dialogo_110.wav (la voz ya colocada en el tiempo del video), 05_audio/linea_de_tiempo.json,
05_audio/linea_de_tiempo.md, 02_prompt/subtitulos_es.srt, 02_prompt/subtitulos.srt y una copia del JSON para el motor
(motor_de_accion/guiones/tin_en_s_004.tiempos.json). Gratis: ffmpeg y numpy.

Decisiones (con su porqué en linea_de_tiempo.md): se quita «Each numbered game tells a new story» (orden de recorte de
la dirección, sección 2) y la suscripción pasa a antes del final (PARAMETROS.md, «Pedir la suscripción», a prueba).
"""
import json
import math
import subprocess
import tempfile
import wave
from pathlib import Path

import numpy as np

PROY = Path(__file__).resolve().parent.parent
AUDIO = PROY / "05_audio"
MOTOR = PROY.parent.parent / "motor_de_accion" / "guiones"
SR, FPS, TEMPO, MARGEN, FUNDIDO = 48000, 30, 1.10, 0.03, 0.008
G = 2                      # respiro entre líneas, en fotogramas (la dirección permite bajar de 6 a 4; con la voz real, 2)
TAN, TIN = "voz_tan_zelda.wav", "voz_tin_kevin.wav"

# id, quién, texto del guion (inglés), subtítulo (español), archivo, tramos [(desde, hasta, pausa antes en s)], fundido final
LINEAS = [
    ("A", "Tan", "Will there be a GTA 7?", "¿Habrá un GTA 7?", TAN, [(0.449, 2.061, None)], None),
    ("T1", "Tin", "GTA is short for Grand Theft Auto:", "GTA es Grand Theft Auto:", TIN, [(1.106, 4.121, None)], None),
    ("T2", "Tin", "a game series that started in 1997,", "una serie de juegos que empezó en 1997", TIN, [(4.668, 7.387, None)], None),
    ("T3", "Tin", "made today by Rockstar Games.", "y que hoy hace Rockstar Games.", TIN, [(7.998, 8.830, None), (9.157, 10.520, 0.09)], None),
    ("T4", "Tin", "GTA 6 came out on November 19, 2026.", "GTA 6 salió el 19 de noviembre de 2026.", TIN,
     [(11.448, 12.644, None), (13.086, 14.646, 0.08), (15.010, 16.095, 0.08)], None),
    ("T5", "Tin", "It's the sixth numbered game.", "Es el sexto juego numerado.", TIN, [(16.573, 17.443, None), (17.807, 18.637, 0.07)], None),
    ("C", "Tan", "Subscribe. We check the facts.", "Suscríbete. Aquí comprobamos los datos.", TAN, [(5.416, 6.285, None), (7.031, 8.300, 0.16)], 0.10),
    ("T6", "Tin", "Rated M: seventeen and over.", "Clasificación M: mayores de 17.", TIN, [(19.176, 19.920, None), (20.249, 21.513, 0.15)], None),
    ("T8", "Tin", "From GTA 5 to GTA 6:", "De GTA 5 a GTA 6:", TIN, [(25.107, 26.275, None), (26.558, 27.586, 0.09)], None),
    ("T9", "Tin", "thirteen years and sixty-three days.", "trece años y sesenta y tres días.", TIN, [(28.105, 29.324, None), (29.673, 31.822, 0.12)], None),
    ("B", "Tan", "So, GTA 7?", "¿Y GTA 7?", TAN, [(2.815, 3.286, None), (3.574, 4.612, 0.16)], None),
    ("T10", "Tin", "Rockstar hasn't announced one. As of today.", "Rockstar no ha anunciado ninguno. A hoy.", TIN,
     [(32.266, 34.050, None), (34.514, 35.393, 0.22)], 0.04),
]
QUITADA = ("T7", "Tin", "Each numbered game tells a new story.", (22.460, 24.657))


def ff(*a):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *a], check=True)


def leer(ruta):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(ruta), "-ar", str(SR), "-ac", "1", "-f", "f32le", "-"],
                       capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.float32).astype(np.float64)


def guardar(ruta, x):
    y = np.clip(np.round(x * 32767.0), -32768, 32767).astype("<i2")
    with wave.open(str(ruta), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(y.tobytes())


def trozo(x, desde, hasta, fundido_fin):
    a, b = int(max(0, desde - MARGEN) * SR), min(len(x), int((hasta + MARGEN) * SR))
    y = x[a:b].copy()
    n = int(FUNDIDO * SR); y[:n] *= np.linspace(0, 1, n)
    n = int(fundido_fin * SR); y[-n:] *= np.linspace(1, 0, n)
    return y


def cortar():
    """Devuelve {id: (muestras al 110 %, [inicio de cada tramo en s dentro de la línea])}."""
    out = {}
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp); normal = {}
        for n in (TAN, TIN):
            ff("-i", str(AUDIO / n), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", str(SR), "-ac", "1", str(tmp / n))
            normal[n] = leer(tmp / n)
        for lid, _, _, _, archivo, tramos, fin in LINEAS:
            piezas, cortes = [], [0.0]
            for j, (a, b, pausa) in enumerate(tramos):
                if j:
                    piezas.append(np.zeros(int(max(0.0, pausa * TEMPO - 2 * MARGEN) * SR)))
                    cortes.append((sum(len(p) for p in piezas) + MARGEN * SR) / SR / TEMPO)
                piezas.append(trozo(normal[archivo], a, b, (fin or FUNDIDO) if j == len(tramos) - 1 else FUNDIDO))
            guardar(tmp / "c.wav", np.concatenate(piezas))
            ff("-i", str(tmp / "c.wav"), "-af", f"atempo={TEMPO}", "-ar", str(SR), str(tmp / "l.wav"))
            out[lid] = (leer(tmp / "l.wav"), cortes)
    return out


def plan(d, corte):
    """d: {id: fotogramas (techo)}; corte: {id: [fotograma relativo de cada tramo]}. Devuelve (inicio de cada línea, K)."""
    L, K = {}, {}
    L["A"] = 14
    K["rival_entra"], K["rival_crece"], K["pisoton"] = 30, 46, 60
    K["K1"] = 82; L["T1"] = 84
    e = lambda i: L[i] + d[i]
    K["K2"] = max(144, e("T1") + G - 2); L["T2"] = K["K2"] + 2
    L["T3"] = e("T2") + G
    K["rival_ataca"] = L["T3"] + 14          # el brazo pasa de largo; Tin se agacha 2 f antes
    K["cartel"] = L["T3"] + 8                # el rival parte el cartel con el brazo al cargar
    K["salto_mostrador"] = L["T3"] + 32
    K["K3"] = max(e("T3") + G - 2, K["salto_mostrador"] + 26); L["T4"] = K["K3"] + 2
    L["T5"] = e("T4") + G; K["dibuja_baston"] = L["T5"]
    L["C"] = e("T5") + G
    K["dibuja_espada"] = L["C"] + corte["C"][1] + 2   # después de «Subscribe.»: el plano vuelve al general
    K["KB"] = max(e("C") + G - 2, K["dibuja_espada"] + 30); L["T6"] = K["KB"] + 2
    K["K4"] = L["T6"] + corte["T6"][1] - 2   # el bastón cae justo antes de «seventeen and over»
    assert K["K4"] - 12 >= K["KB"] + 6, "no cabe la anticipación del bastón tras el bloqueo"
    K["tele_punta"] = K["KB"] + 14
    K["K5"] = max(e("T6") + G - 2, K["K4"] + 38); L["T8"] = K["K5"] + 2
    K["mazo"] = K["K5"] - 26                                   # Tin añade el bloque (8 f) y lo lanza (5 f), sobre el final de la línea
    K["carrera"] = max(e("T8") - 8, K["K5"] + 46)
    K["KR"] = K["carrera"] + 23
    assert K["KR"] - 6 >= e("T8"), "la pausa del remate pisa la voz"
    K["tele_choque"] = K["KR"] + 21; K["invertidos"] = K["KR"] + 23; K["radiales"] = K["KR"] + 25; K["claro"] = K["KR"] + 30
    K["bola"] = K["KR"] + 34; K["enfria"] = K["KR"] + 45
    L["T9"] = K["KR"] + 44
    L["B"] = e("T9") + G
    K["K6"] = max(e("B") + G - 2, L["B"] + 14); L["T10"] = K["K6"] + 2
    K["implosion"] = K["K6"] + 2; K["implosion_fin"] = K["K6"] + 19
    K["armas_gotas"] = K["K6"] + 22; K["asterisco"] = K["K6"] + 32; K["escurre"] = K["K6"] + 40; K["escurre_fin"] = K["K6"] + 55
    K["lapiz_a_tan"] = K["K6"] + 57
    N = max(K["K6"] + 64 + 30, e("T10") + 17)
    K["N"] = N; K["cierre"] = N - 30
    return L, K


PORTADA = dict(cx=0.0, z=0.0, D=8.66, h=2.03)       # suelo de z = 0 en y = 1651 px y el televisor en y ≈ 780–1040 (medidas de portada)


def planos(L, K):
    """Versión 3: las cámaras de la pelea ya no salen de aquí; viven en el guion del motor
    (`motor_de_accion/guiones/tin_en_s_004.js`, tabla PLANOS), porque ahora acompañan carreras y vuelos y dependen de la
    coreografía. Aquí queda solo el plano de portada de la firma y los fotogramas de los efectos de composición."""
    post = {"impacto": [K["K1"] + 18, K["K1"] + 19, K["K3"] + 22, K["K3"] + 23, K["tele_punta"], K["tele_punta"] + 1],
            "invertidos": [K["invertidos"], K["invertidos"] + 1], "radiales": list(range(K["radiales"], K["radiales"] + 5)),
            "claro": list(range(K["claro"], K["claro"] + 4))}
    return [dict(f0=0, nombre="P1 portada", **PORTADA, tipo="firma"), dict(f0=K["cierre"], nombre="P22 portada", **PORTADA, tipo="firma")], post


def srt(filas, campo):
    def t(f):
        ms = round(f / FPS * 1000); return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"
    return "\n".join(f"{i}\n{t(f['f0'])} --> {t(f['f1'])}\n{f[campo]}\n" for i, f in enumerate(filas, 1))


def main():
    clips = cortar()
    d = {k: math.ceil(len(v[0]) / SR * FPS) for k, v in clips.items()}
    corte = {k: [round(c * FPS) for c in v[1]] for k, v in clips.items()}
    L, K = plan(d, corte)
    N = K["N"]
    assert 900 <= N <= 990, f"el video dura {N} f ({N / FPS:.2f} s): fuera de 30 a 33 s"
    pista = np.zeros(int(N / FPS * SR) + SR // 10)
    filas = []
    for lid, quien, texto, es, archivo, tramos, _ in LINEAS:
        x = clips[lid][0]; a = int(L[lid] / FPS * SR); pista[a:a + len(x)] += x
        filas.append({"id": lid, "quien": quien, "texto": texto, "es": es, "f0": L[lid], "f1": L[lid] + d[lid], "dura_f": d[lid],
                      "tramos_f": [L[lid] + c for c in corte[lid]], "archivo": archivo, "origen": [(a_, b_) for a_, b_, _ in tramos]})
    filas.sort(key=lambda f: f["f0"])
    for a, b in zip(filas, filas[1:]):
        assert b["f0"] >= a["f1"], f"las líneas {a['id']} y {b['id']} se pisan"
    assert filas[-1]["f1"] <= N - 17, "la voz pisa la suelta del lápiz (c -17)"
    guardar(AUDIO / "dialogo_110.wav", pista[:int(N / FPS * SR)])
    pl, post = planos(L, K)
    datos = {"planos": pl, "post": post, "portada": PORTADA, "fps": FPS, "N": N, "duracion_s": round(N / FPS, 3), "tempo": TEMPO, "respiro_f": G, "lineas": filas, "K": K,
             "quitada": {"id": QUITADA[0], "texto": QUITADA[2], "origen": QUITADA[3]}}
    txt = json.dumps(datos, indent=1, ensure_ascii=False) + "\n"
    (AUDIO / "linea_de_tiempo.json").write_text(txt, encoding="utf-8")
    (MOTOR / "tin_en_s_004.tiempos.json").write_text(txt, encoding="utf-8")
    # subtítulos: sin subtítulo en los planos de portada (f0–f29 y cierre)
    # cada subtítulo sale cuando entra el siguiente (antes se pisaban 67 ms: dos textos encimados 2 o 3 fotogramas)
    sub = [dict(f, f0=max(f["f0"], 30), f1=min(f["f1"] + 4, K["cierre"], filas[i + 1]["f0"] if i + 1 < len(filas) else N)) for i, f in enumerate(filas)]
    (PROY / "02_prompt" / "subtitulos_es.srt").write_text(srt(sub, "es"), encoding="utf-8")
    (PROY / "02_prompt" / "subtitulos.srt").write_text(srt(sub, "texto"), encoding="utf-8")
    sus = next(f for f in filas if f["id"] == "C")
    md = [f"# Línea de tiempo con la voz real — short 4 ({N} f = {N / FPS:.2f} s)", "",
          "Hecha por `codigo/tiempos.py` con `voz_tin_kevin.wav` y `voz_tan_zelda.wav` (una generación cada una; no se",
          "regeneran). Cada línea al 110 % (`atempo=1.10`), pausas internas cerradas (0,07 a 0,22 s), respiro de "
          f"{G} f entre líneas. **Ninguna persona ha escuchado el audio.**", "",
          "| Línea | Quién | f inicio | f fin | s inicio | Dura (f) | Texto | Subtítulo |", "|---|---|---|---|---|---|---|---|"]
    md += [f"| {f['id']} | {f['quien']} | {f['f0']} | {f['f1']} | {f['f0'] / FPS:.2f} | {f['dura_f']} | {f['texto']} | {f['es']} |" for f in filas]
    md += ["", "## Contactos y momentos (fotogramas)", "", "| Clave | f | s |", "|---|---|---|"]
    md += [f"| {k} | {v} | {v / FPS:.2f} |" for k, v in sorted(K.items(), key=lambda kv: kv[1])]
    md += ["", "## Decisiones del equipo (con su porqué)", "",
           "1. **Se quita «Each numbered game tells a new story.»** Con todas las frases el video medía ≈ 34 a 35 s (la voz de",
           "   Tin salió ≈ 2,8 s más larga que la estimada). Es la primera del orden de recorte de la dirección (sección 2) y la",
           "   de fuente más débil. **El golpe del bastón (4) se conserva**: cae en «seventeen and over», como respuesta al",
           "   bloqueo, y deja los siete golpes y la mecha del televisor.",
           f"2. **La suscripción va en f{sus['f0']}–f{sus['f1']} ({sus['f0'] / FPS:.1f} s; {100 * sus['f0'] / N:.0f} % del video), no al cierre.**",
           "   `PARAMETROS.md` («Pedir la suscripción», a prueba desde el 2026-11-26; el dueño lo confirmó hoy): una vez, con voz,",
           "   antes del final, en la primera mitad y pegada al dato fuerte. Va justo después de «GTA 6 came out on November 19,",
           "   2026. It's the sixth numbered game.» (el dato del título), en el único hueco donde Tin no habla y no hay contacto:",
           "   mientras el rival dibuja su espada. No lleva texto en pantalla (solo su subtítulo). El cierre queda con la firma.",
           "3. **«So, GTA 7?» la dice Tan** (D2 de la dirección) y el remate «Rockstar hasn't announced one. As of today.» termina",
           f"   en f{filas[-1]['f1']} (c −{N - filas[-1]['f1']}; la firma pide c −17 o antes).",
           "4. **Respiro entre líneas de 2 f** y la pausa de voz del remate recortada (el dato entra durante el enfriamiento de la",
           "   explosión, no en el pico): es lo que deja el video dentro de 30 a 33 s sin tocar ninguna otra frase.",
           "5. No se movieron: los desfases de cada golpe (anticipación K −12 a −7, pausa K −6 a −1, contacto K y K +1, voz en",
           "   K +2) ni las reglas 2.1.", ""]
    (AUDIO / "linea_de_tiempo.md").write_text("\n".join(md), encoding="utf-8")
    print(f"N = {N} f ({N / FPS:.2f} s)")
    for f in filas:
        print(f"  {f['id']:4s} {f['quien']} f{f['f0']}-f{f['f1']}  {f['tramos_f']}")
    print({k: v for k, v in sorted(K.items(), key=lambda kv: kv[1])})


if __name__ == "__main__":
    main()
