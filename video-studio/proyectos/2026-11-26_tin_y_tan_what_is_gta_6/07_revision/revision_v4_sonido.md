# Revisión v4 · sonido · short 4 de Tin & Tan

## 1. Pieza y límites

- Pieza: `06_final/tin_y_tan_short04_v4.mp4`, sha256 `f4c8224b3707` (comprobado con `sha256sum`).
- **No pude oír nada.** Todo es medida. Método: audio del mp4 (mono, 48 kHz) descompuesto en voz, efectos y música con
  `dialogo_110.wav` (+2.9 dB y +3 dB en la línea C, como hace `audio.py`), `efectos.wav` y `musica.wav` con el agachado de la
  v4. Ajuste por mínimos cuadrados contra el mp4: coeficientes 0.999 / 1.003 / 1.005 y residuo RMS 0.006. La descomposición
  es fiable. El mp4 coincide con `mezcla_final.wav` (diferencia máx. 0.07 por AAC).
- No puedo juzgar timbre, naturalidad, acento, ni si un sonido «suena bien».

## 2. Niveles (medidos en el mp4 con `ffmpeg ebur128`)

| Medida | v4 | Regla (control 3) | v3 | |
|---|---|---|---|---|
| Integrado | −14.0 LUFS | −14 ±1 | −14.1 | pasa |
| Pico real | −1.4 dBTP | ≤ −1 | −1.1 | pasa, margen 0.4 |
| LRA | 2.1 LU | — | 2.9 | parejo |
| Silencio previo al remate | < −90 dBFS de f687.25 a f692.92 (5.7 f); < −60 dBFS de f686.94 a f692.97 (6.0 f) | 6 f | ≈ 5 f | pasa |

## 3. Voz contra el guion

`voz_video_final_v4.md`: 74 palabras en el guion, 75 oídas; sobra «it» en «GTA 6. **It** came out» (igual que v2 y v3). La voz
no se regeneró, así que no es de esperar otro resultado. Prueba nueva que hice:

- El tramo del mp4 de 10.3 a 14.4 s (T4, f316–f428) pasado solo por `revisar_voz.py` se reconoce **«GTA 6 came out on November 19,
  2026.»**, sin «it». La voz original en ese tramo se reconoce «GTA VI / came out on November 19th / 2026». Ya en v3 la voz sola
  daba 0 diferencias.
- **Por medida es un artefacto del reconocedor** (Whisper inventa «It» al arrancar un segmento tras la pausa de f352, 11.7 s,
  donde entra «came out»). No hay palabra de más en ninguna de las tres pruebas aisladas.
- ¿Basta para firmar? **Para presentar al dueño, sí. Para firmar el control 3 como PASA de publicación, no**: la regla pide
  escucha de una persona y nadie del equipo oye. Al dueño le queda **escuchar la frase «GTA 6 came out on November 19, 2026»
  (≈ 10.5–14 s) y confirmar que no se oye «it» entre «GTA 6» y «came out»**; además de oír la línea C y el mazazo (sección 7).

## 4. Golpes: cada evento suena en K o K−1

Pico de `efectos.wav` en el mp4 contra el fotograma de contacto (estrella en K):

| Golpe | K | Ataque / pico del sonido | Nivel | |
|---|---|---|---|---|
| K1 | 82 | f81.0 | −9.2 dBFS | K−1, pasa |
| K2 | 169 | f168.0 | −10.2 | K−1, pasa |
| K3 | 314 | f313.0 | −10.3 | K−1, pasa |
| K4 | 574 | f573.0 | −9.9 | K−1, pasa |
| K5 (mazazo) | 612 | f611.0 | −12.1 | K−1, pasa |
| KR | 694 | f693.0 | −9.1 | K−1, pasa |
| K6 | 886 | f885.0 | −10.4 | K−1, pasa |

Pausa de efectos antes del golpe: fx en −180 dBFS en K5 (f606–f610), K4 (f568–f572), y silencio total en KR. Los 49 eventos de
`eventos_y_medidas_del_motor_v4.json` (53 en v3: se retiraron/renombraron algunos eventos, por eso la lista ya no es idéntica a
la de v3) no mueven ningún K. Pico global de efectos −5.1 dBFS (la explosión, en pausa de voz).

## 5. Medidas pedidas

**S1, f605–f615 (mazazo).** Voz y efectos por 10 ms:
voz −24…−28 dB RMS hasta f610.2, −34/−35 en f610.2–f610.7 y **−46 en f610.8; silencio desde f611.1**. Efectos: **−180 dBFS
hasta f610.7**; el mazazo entra en f610.8–f611.0 con pico **−12.1 dBFS** (v3: −9.5 dBFS desde f609 sobre la voz) y cae a −21
en f612 y −29 en f613. Resultado: el golpe ya no se superpone a «over»; arranca cuando la voz acabó (−46 dB). Pico −12.1
sin voz: dentro del tope de la dirección (−8 sin voz). **Resuelto.**

**S3, línea C.** Nivel activo (frames de 10 ms por encima de −45 dBFS), en el mp4:

| Línea | Activo |
|---|---|
| Tin T1–T5, T6, T8–T10 | −12.5 … −13.5 dBFS |
| Tan A | −12.1 |
| **Tan C** | **−15.9** (en v3, −18.7 con el mismo método: sube 3 dB) |
| Tan B | −15.3 |

La brecha de C contra Tin baja de ≈ 5.5 a **2.4–3.4 dB**; C queda 3.6 dB bajo la A de la propia Tan, y a la par de B. **Mejorado,
no igualado.** Efecto colateral en 6: ver D1.

**S4, f738–f744 (cola de la explosión).** Efectos: RMS −23.9 dBFS, pico −17.7 (v3: −16); voz RMS −12.9. Voz menos efectos en
ventanas de 100 ms desde f738 hasta f742: **+10 a +14 dB** (v3: −7.7). Lo único cercano (f743–f744, ≈ 0 dB) cae en el hueco
entre «thirteen» y «years», donde la voz está en silencio. **Resuelto.**

**S5, f567–f572.** Efectos en −180 dBFS de f568 a f572; el golpe 4 entra en f573 (−9.9). La cola de `vidrio_grieta`/`chispas`
termina en f567 (−31). **Resuelto.**

**S6, silencio antes del remate.** Ver tabla 2: 5.7 fotogramas por debajo de −90 dBFS y 6.0 por debajo de −60; el golpe entra
en f693.0. **Resuelto.**

## 6. Estado de S1–S6

| # | Estado |
|---|---|
| S1 mazazo sobre «seventeen and over» (B) | Resuelto por medida (pico −12.1, sin voz debajo) |
| S2 «it» de más (A) | Artefacto del reconocedor por medida (tramo aislado limpio). Queda la escucha del dueño |
| S3 línea C de Tan baja (M) | Mejorada: brecha de 5.5 a ≈ 2.4–3.4 dB (b) |
| S4 cola de la explosión (M) | Resuelto (+10 a +14 dB sobre las palabras) |
| S5 pausa antes del golpe 4 (b) | Resuelto |
| S6 silencio antes del remate (b) | Resuelto |

## 7. Defectos nuevos

| # | Fotograma | Gravedad | Hallazgo y corrección |
|---|---|---|---|
| D1 | f483–f548 (C) y f14–f60 (A) | M | El limitador blando actúa más de lo que debería sobre la voz de Tan. Antes del limitador la voz llega a **+4.4 dBFS en C** (117 muestras sobre 0 dBFS, 730 sobre −1.6) y a +1.4 en A (126 y 772). El limitador las baja a −1.6 (hasta 6 dB en transitorios, por ejemplo la «b» de «Subscribe»). Es breve (milisegundos) pero puede dar dureza o saturación en esa línea, la que más importa. Si el oído la nota: subir menos la C (+3 → +2 dB) y bajar un poco la A, o limitar la voz de Tan antes de sumar. Tin también roza (3 a 26 muestras por línea): irrelevante |
| D2 | f610–f612 (K5) | b | El mazazo (−12.1) queda 2–3 dB más blando que los demás golpes (−9 a −10). Es el clímax del cartel y suena más suave que K1. Subir `mazo_golpe` a ≈ −14 sin voz arriba no pisa «over» (ya no hay voz en f611+). Solo si el dueño lo oye flojo |
| D3 | f609–f611 | b | La pausa de efectos (f606–f610) deja la entrada del mazazo justo al terminar la voz, sin respiro entre «over» y el golpe: es el efecto buscado, pero el dueño debe oír que «over» no se come. No se puede medir con certeza si el final de la palabra tiene su duración natural (la voz cae a −46 dB en f610.8) |

No hay defectos B ni A nuevos.

## 8. Qué le queda al dueño por escuchar

1. «GTA 6 came out on November 19, 2026» (≈ 10.5–14 s): que no haya «it» entre «GTA 6» y «came out».
2. «Subscribe. We check the facts.» (f483–f548, 16.1–18.3 s): que se entienda bien, que sea igual de fuerte que la voz de Tin y que no suene áspera (D1).
3. «Rated M: seventeen and over» seguido del mazazo (f550–f612): que «over» llegue completa y el golpe pegue sin tapar.
4. Que los siete golpes se sientan sincronizados con la estrella y que el silencio antes del remate (f687–f692) se note como una pausa.

## Veredicto

Veredicto: APROBADO

Presentable al dueño: S1 (el bloqueante de la v3) está resuelto por medida y S3, S4, S5 y S6 también o quedan en menor. Niveles
en regla (−14.0 LUFS, −1.4 dBTP). El «it» es por medida un artefacto del reconocedor, pero **el control 3 sigue sin firma de PASA
para publicar hasta que una persona lo oiga**: la presentación al dueño es precisamente esa escucha. Si el dueño oye el «it»,
es una regeneración de la frase T4 con voz (costo a confirmar por el jefe de producción), no un cambio de mezcla.

Firma: diseñador de sonido, 2026-11-26. Esta firma no es una escucha: nadie del equipo ha oído el audio.
