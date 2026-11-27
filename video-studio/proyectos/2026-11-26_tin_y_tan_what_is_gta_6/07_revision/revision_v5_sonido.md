# Revisión v5 · sonido · short 4 de Tin & Tan

## 1. Pieza y límites

- Pieza: `06_final/tin_y_tan_short04_v5.mp4`, sha256 `df6b8a638e86` (comprobado con `sha256sum`). 32.87 s, 986 fotogramas, 30 fps.
- **No pude oír nada.** Todo es medida (audio del mp4 a mono 48 kHz, contra `voz`, `efectos.wav`, `mezcla_final.wav` de `05_audio/`).
- `codigo/audio.py` sin cambios desde el commit ab5e551 (`git diff` vacío). Las voces (`voz_tan_zelda.wav`, `voz_tin_kevin.wav`)
  conservan fecha del 26-nov 20:41; `dialogo_110.wav` del 26-nov 23:36. `efectos.wav`, `musica.wav` y `mezcla_final.wav` se
  regeneraron el 27-nov 00:05 (los vuelve a escribir el motor); su contenido en los puntos medidos coincide con la v4 (abajo).
- El mp4 coincide con `05_audio/mezcla_final.wav`: diferencia máxima 0.0695 (la v4: 0.07), solo AAC.
- No puedo juzgar timbre, naturalidad, acento ni si un sonido «suena bien».

## 2. Niveles (mp4, `ffmpeg ebur128` y `postpro.py info`)

| Medida | v5 | Regla (control 3) | v4 | |
|---|---|---|---|---|
| Integrado | −14.0 LUFS | −14 ±1 | −14.0 | pasa |
| Pico real | −1.4 dBTP | ≤ −1 | −1.4 | pasa, margen 0.4 |
| LRA | 2.1 LU | — | 2.1 | igual |
| Silencio antes del remate | < −90 dBFS de f687.25 a f692.92 (5.67 f); < −60 dBFS de f686.94 a f692.97 (6.03 f) | 6 f | idéntico | pasa |

## 3. Eventos del motor: v4 contra v5

`eventos_y_medidas_del_motor_v5.json` y `..._v4.json`: **49 eventos cada uno, no 53** (53 era la cifra de la v3; la v4 ya los
había reducido a 49). Comparados por nombre y fotograma, en orden: **los 49 son idénticos; no cambia ninguno.** No hay eventos
añadidos ni retirados. Las claves `K` de `05_audio/linea_de_tiempo.json` (K1 82, K2 169, K3 314, K4 574, K5 612, KR 694, K6 886)
son las mismas que en la v4.

## 4. Golpes: cada evento suena en K o K−1

Pico de `efectos.wav` en ventana K−6…K+4, y pico del mp4 en K−3…K+2 (incluye lo demás que suene):

| Golpe | K | Pico de efectos | Nivel efectos | Pico en el mp4 | |
|---|---|---|---|---|---|
| K1 | 82 | f81.04 | −12.1 | −9.2 | K−1, pasa |
| K2 | 169 | f168.03 | −13.0 | −10.0 | K−1, pasa |
| K3 | 314 | f313.06 | −13.0 | −5.4 (f315.05, voz de Tin) | K−1, pasa |
| K4 | 574 | f573.08 | −12.8 | −10.0 | K−1, pasa |
| K5 (mazazo) | 612 | f611.06 | −14.9 | −11.2 | K−1, pasa |
| KR | 694 | f693.44 | −12.0 | −9.0 | K−1, pasa |
| K6 | 886 | f885.03 | −13.0 | −7.6 | K−1, pasa |

Los niveles de mp4 de K1, K2, K4, K5, KR coinciden con la v4 (−9.2, −10.2, −9.9, −12.1, −9.1; K5 sube 0.9 por la voz que cae
justo después, ver 5). El pico de mp4 de K3 y K6 lo da la voz o la música cercana, no el golpe; el golpe sale en K−1 en efectos.

## 5. Mazazo contra la voz, f605–f615

Por medio fotograma (RMS): voz −24…−30 dB hasta f610.0, −35.5 en f610.0, −40 en f610.5, **−72 en f611.0 y silencio desde
f611.5**. Efectos: **−180 dBFS de f606 a f610.9**; el mazazo entra en f611.0 (−20.5, pico −14.9 en efectos, −11.2 en mp4)
y cae a −28 en f612 y −36 en f613. La voz vuelve en f614. El golpe arranca cuando «over» ya terminó y no se superpone. Igual
que la v4. **Pasa.**

## 6. Voz contra el guion

`voz_video_final_v5.md` (Whisper small.en): 74 palabras en el guion, 75 oídas; **sobra «it»** en «GTA 6. **It** came out».
Es el mismo resultado de v2, v3 y v4. La voz no se regeneró (archivos sin tocar) y el tramo T4 es el mismo audio; en la v4 el
tramo aislado se reconocía limpio («GTA 6 came out on November 19, 2026»), así que **por medida es un artefacto del
reconocedor** (arranca un segmento tras la pausa y se inventa «It»). Resto de palabras: coinciden. Para publicar sigue
faltando la escucha de una persona.

## 7. Qué cambió y qué no respecto a la v4

- No cambia: niveles (−14.0 LUFS, −1.4 dBTP, LRA 2.1), los 49 eventos, los 7 K, el silencio de 5.67 f antes del remate,
  la entrada del mazazo en f611, la diferencia mp4-mezcla, el resultado del reconocedor.
- Cambia: nada audible por medida. Solo se regeneraron los archivos de mezcla con el mismo contenido en los puntos medidos.
- La coreografía y las cámaras de la v5 no mueven ningún K ni evento de sonido.

## 8. Defectos

Ninguno nuevo. Siguen abiertos, sin cambio, los de la v4 (a juzgar por el oído del dueño):

| # | Fotograma | Gravedad | Hallazgo |
|---|---|---|---|
| D1 | f14–f60 y f483–f548 | M | El limitador baja picos de la voz de Tan (hasta +4.4 dBFS antes del limitador en C). Puede sonar duro. No medí de nuevo la entrada del limitador: `audio.py` no cambió |
| D2 | f610–f612 | b | El mazazo (−11 a −12 en mp4) queda 1–3 dB más blando que los otros golpes |
| D3 | f609–f611 | b | Entra justo al acabar «over»; el dueño debe oír que no se come la palabra |

## 9. Qué le queda al dueño por escuchar

1. «GTA 6 came out on November 19, 2026» (≈ 10.5–14 s): que no se oiga «it» entre «GTA 6» y «came out».
2. «Subscribe. We check the facts.» (16.1–18.3 s): que se entienda, esté a la par de Tin y no suene áspera (D1).
3. «Rated M: seventeen and over» y el mazazo (f550–f612): que «over» llegue completa y el golpe pegue.
4. Los siete golpes sincronizados con la estrella y la pausa de f687–f692 antes del remate.

El control 3 queda sin firma de PASA para publicar hasta que una persona lo oiga.

Veredicto: APROBADO

Firma: diseñador de sonido, 2026-11-27. Esta firma no es una escucha: nadie del equipo ha oído el audio.
