# Revisión v3 · sonido · short 4 de Tin & Tan

## 1. Pieza y límites

- Pieza: `06_final/tin_y_tan_short04_v3.mp4`, sha256 `511571dd5f4d` (comprobado con consola).
- **No pude oír nada.** Todo es medida: `revisar_voz.py` (reconocedor), `ffmpeg ebur128`, energía de `05_audio/efectos.wav`,
  `dialogo_110.wav` y `musica.wav` por fotograma, y fotogramas del video sin audio en torno a cada contacto K.
  Se restó la voz (ganancia estimada +2.9 dB sobre `dialogo_110.wav`) del audio del mp4 para sacar efectos+música por tramo.
  El audio del mp4 coincide con `mezcla_final.wav` (diferencia máx. 0.07 por la recodificación AAC).
- No puedo juzgar timbre, naturalidad de la voz, acento, si un sonido suena «bien» ni la sensación de la mezcla.

## 2. Niveles (medidos en el mp4)

| Medida | Valor | Regla (control 3) | |
|---|---|---|---|
| Integrado | −14.1 LUFS | −14 ±1 | pasa |
| Pico real | −1.1 dBTP | ≤ −1 | pasa, con 0.1 de margen |
| LRA | 2.9 LU | — | parejo |
| Silencio previo al remate | f689–f692 por debajo de −90 dBFS (f688 −90, f693 ya entra el golpe) | 6 f en la dirección (f635–f640 en la versión vieja) | casi: ≈ 5 f (b) |

## 3. Voz contra el guion

`voz_video_final_v3.md`: 74 palabras en el guion, 75 oídas; sobra «it» (igual que v2). Voz sola y un tramo del video: 0 diferencias.
Por medida es un artefacto del reconocedor, pero el control 3 pide escucha: **no lo firmo como PASA sin oído humano** (A).

## 4. Golpes: cada evento suena en su fotograma

- Los 53 eventos de `eventos_y_medidas_del_motor_v3.json` tienen su pico de energía en el fotograma indicado (±0.1 f) en los
  golpes secos: choque_suelo/cajas f60 (+0.07 f), golpe f81 (+0.04), choque_madera f100, golpe_agudo f168, golpe_grave f313,
  bloqueo_tinta f547, vidrio_grieta f562, asterisco_tic f918–923, atrapa f949. Los eventos de rasgueo, silbido y cola tienen su
  máximo 1.5–4 f después de la marca porque son barridos (esperado).
- **Contacto visual (estrella en K) contra sonido:** estrella en f82 (K1), f169 (K2), f314 (K3), f574 (K4), f612 (K5), f694 (KR),
  f886 (K6); sonido en f81, f168, f313, f573, f611, f693, f885 = K−1. Cumple la dirección («K o K−1»). Todos pasan.
- **Pausa de efectos antes del golpe:** K1 (f75–80), K2, K3 y K5: silencio de efectos (−180 a −45 dBFS). KR: silencio total.
  K6 −40 dBFS. **K4 (f573): no hay pausa limpia**: en f567–572 suena la cola de `vidrio_grieta`/`chispas` (−27 dBFS) y
  `fuego_enciende` (b: se pierde un poco el contraste del golpe).
- Silencio total antes del remate: f689–f692 pico −180 dBFS, sin voz ni música; el golpe doble entra en f693. Pasa.

## 5. Voz tapada (voz contra efectos+música)

Por línea (RMS de voz menos RMS de lo demás): 14 a 19 dB en casi todas; música a −28…−31 dBFS RMS, nunca tapa. Peores ventanas de 0.1 s:

- **f609–f611, `mazo_golpe`+`choque_madera`: pico −9.5 dBFS (el más alto del video salvo la explosión) justo encima de la última
  sílaba de «seventeen and over» (línea T6, f550–612).** La voz queda 13 dB por debajo en esa ventana. La dirección (sección 5)
  da −20 a −12 dBFS con voz encima y solo permite −8 a la explosión, que cae en pausa de voz.
- f573, `baston_golpe` −12.8 dBFS sobre «Rated M: seventeen…»: ventana −9.6 dB (voz por debajo del efecto). Dentro del tope −12, al límite (M).
- f738–f744, cola de la explosión (−16 dBFS) sobre el inicio de «thirteen years…» (T9 empieza en f738): −7.7 dB (M).
- f540, `bloqueo_tinta` (−14) en la cola de «We check the facts» (Tan): −13.8 dB (M).
- **Voz de Tan en la línea C («Subscribe. We check the facts.», f483–548): RMS activo −18.8 dBFS contra −14.4 a −15.4 de Tin (4 dB
  menos); B −16.8.** La petición de suscripción es la línea que más importa y es la más baja (M, sube a A si el oído la confirma floja).

## 6. Defectos de la v2 de sonido

| Defecto v2 | Estado | Prueba |
|---|---|---|
| Efectos y contactos sin comprobar (A7) | Resuelto por medida; falta el oído | secciones 4 |
| «it» de más | Sin resolver por medida (voz sola y tramo aislado limpios) | `voz_video_final_v3.md` |
| Choque del mostrador tapaba la voz (−14→−18) | Resuelto: ya no aparece entre las peores ventanas | sección 5 |
| Nadie ha oído el audio | Igual | — |

## 7. Defectos nuevos

| # | Fotograma | Gravedad | Corrección (valores de partida) |
|---|---|---|---|
| S1 | f609–f612 | **B** | `codigo/audio.py`, tabla `SONIDOS`: bajar `mazo_golpe` y su `choque_madera` de −9.5 a ≈ −14 dBFS y acortar su cola; o mover el golpe a f612 y recortar la última palabra no se puede (la voz no se regenera). Alternativa: agachar los efectos 4–6 dB mientras hay voz en `pista_efectos` (hoy es 0.75+0.25·agacha: bajar a 0.5+0.5·agacha) |
| S2 | voz del video completo | A | Escucha humana del «it» antes de firmar el control 3; sin ella no se publica |
| S3 | f483–f548 (línea C) | M | `tiempos.py`/`audio.py`: ganancia por línea de Tan C ≈ +3 dB y bajar un poco A/T de Tin (el pico de voz ya está a −1.6) para igualar el RMS activo |
| S4 | f738–f744 | M | `cola_explosion` de −16 a ≈ −22 dBFS al inicio, o retrasar su entrada hasta f745 |
| S5 | f567–f572 | b | Cortar la cola de `vidrio_grieta`/`chispas` en f566 para dejar pausa antes del golpe 4 |
| S6 | f688–f693 | b | La dirección pide 6 f de silencio total; hay ≈ 5 f. Mover el fin de `subida` un fotograma antes |

## Veredicto

Veredicto: CAMBIOS

Bloquea S1 (el mazazo rompe el techo de efectos con voz de la dirección y cubre la última sílaba de «over») y queda S2
(el «it» no está firmado por oído humano). Todo lo demás (niveles, sincronía con K, silencio del remate) pasa por medida.

Firma: diseñador de sonido, 2026-11-27. Esta firma no es una escucha: nadie del equipo ha oído el audio.
