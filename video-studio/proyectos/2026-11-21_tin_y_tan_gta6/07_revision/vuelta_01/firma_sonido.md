# Firma del control 3 «Voz y audio» · Short 2 de Tin & Tan (GTA 6)

Firma: **disenador-de-sonido**, 2026-11-23. Pieza auditada: `06_final/tin_y_tan_short02_v1.mp4` (audio AAC estéreo 48 kHz, 28,50 s) y sus pistas en `05_audio/` (`dialogo_110.mp3`, `efectos.wav`, `musica.wav`, `mezcla.wav`).

## Límite de esta auditoría (honesto)

Nadie ha oído esta pieza. Todo lo de abajo es medida con ffmpeg y numpy más el reconocedor `revisar_voz.py` (Whisper small.en, sin conexión). Reconoce palabras: **no juzga naturalidad, acento, pronunciación de «G T A» ni de las cifras, ni si la mezcla se siente bien**. Lo que solo se resuelve al oído está marcado «NO COMPROBABLE SIN OÍDO HUMANO» y es la salvedad de la firma.

Las medidas se reprodujeron aparte (scripts en la carpeta temporal de la sesión; no se cambió ningún archivo del proyecto salvo este y `direccion.md` §5).

## Tabla

| # | Control | Medida | Resultado |
|---|---|---|---|
| 1 | Transcripción de la mezcla FINAL (audio extraído del mp4) contra guion | `revisar_voz.py` sobre el mp4, repetido por mí: **75 palabras, 0 diferencias**. Oído: «Remember buying GTA 5 at midnight? So, how many days did we wait for GTA 6? GTA 5 came out September 17th 2013 13 years times 365 4000 745 days. Add three leap days. 4,748. Plus, 63 days September 17th to November 19th. 4,811 days. Wow, that long? A baby born that day is a teenager now.» Por línea (9 tramos recortados de la línea de tiempo): 9 de 9 coinciden | PASA (palabras) |
| 1b | Pronunciación, acento, «G T A» letra por letra, cifras dichas con naturalidad (lección de la voz de Juan) | Whisper normaliza «four thousand, seven hundred forty-five» y «4000 745»; no oye acento | NO COMPROBABLE SIN OÍDO HUMANO |
| 2a | Relación voz/fondo (efectos+música), RMS por línea, intervalos de la línea de tiempo | Voz −13,0 a −17,0 dB; fondo −19,7 a −22,8 dB. **Voz/fondo: L1 7,5 · L2 5,8 · L3 8,6 · L4 7,8 · L5 7,1 · L6 8,2 · L7 6,5 · L8 6,9 · L9 7,5 dB** (mínimo L2 5,8). En la banda 300–4000 Hz (donde vive la inteligibilidad): 11,3 a 15,6 dB (mínimo L7: 6,4 dB frente a efectos solos, 14 dB frente a música) | PASA |
| 2b | Peor ventana de 200 ms con voz activa (> −22 dB) | Voz/fondo entre −3,5 dB (L5, 14,07 s, «pop» bisiesto de 13,9 a 14,5) y +2,6 dB (L1); L6 −0,2 (17,92, hojas), L7 −0,3 (22,03, tictac), L2 −1,3 (4,01), L4 −1,3 (10,01, bloques), L8 −1,0 (24,04), L9 +0,7 (26,50, pop grave). Son golpes puntuales de menos de 100 ms bajo una sílaba, no un fondo continuo | PASA con vigilancia (la escucha decide) |
| 2c | Prueba de estrés: efectos+música subidos sobre la voz y reconocimiento por línea y completo | **+6, +9, +12, +18 dB: 9 de 9 líneas y el guion completo coinciden, 0 diferencias.** A **+24 dB se rompe**: L1 («GT5»), L5 («At 3 leap days»), L7 («2011 days»), L9 («Baby born…» pierde «A»); completo 2 diferencias. Se rompen juntas; la de peor banda de voz (6,4 dB) es L7. No probé +19 a +23: el margen real está entre 18 y 24 dB | PASA (margen ≥ 18 dB; el reconocedor no es un oído humano, pero la mezcla no depende de él para pasar) |
| 3a | Clics en empalmes de línea y pausas acortadas (21 empalmes de la línea de tiempo, ±15 ms) | Saltos máximos muestra a muestra en la voz: 0,0001 a 0,049 en 20 de 21 empalmes (todos bajo fundido de 8 ms). Detector global (salto > 0,05 y > 25× el entorno): **0 hallazgos** en la voz, en `mezcla.wav` y en el audio del mp4. **Un caso a oír:** 22,23 s (arranque de «eight» tras «Four thousand,»), salto de 0,27 en un solo paso y subida de −89 a −12 dB en 3 ms. **Ya está así en la grabación original** (`voz_tin_kevin.wav` en 21,724 s: −56 a −17 dB en 2 ms), o sea que es el ataque de la sílaba que genera la voz, no un corte del montaje | PASA (0 clics del montaje); el ataque de 22,23 s: NO COMPROBABLE SIN OÍDO HUMANO |
| 3b | Saturación | Pico de muestra del mp4: 0,862 (−1,3 dBFS); **0 muestras ≥ 0,999 y 0 > 0,95**; `mezcla.wav` estéreo: pico 0,861. (Un primer conteo de 194 muestras al tope salió de sumar los dos canales a mono; en estéreo no hay ninguna) | PASA |
| 4 | Final de «now» (línea 9) | La grabación de Tin termina a 25,60 s **con la voz sonando** (−20,9 dB en los últimos 40 ms; sin cola). En el diálogo, el fundido de 120 ms (cos²) lleva la voz de −15 dB (27,21 s) a −53 dB (27,31 s) y a silencio en 27,32 s. «now» (sílaba /aʊ/) mantiene −15 a −20 dB hasta 27,25 s y el fundido la apaga en ≈ 80 ms; una «now» natural cae en 150 a 250 ms. Tras 27,33 s solo queda la música (−24 a −27 dB) hasta el golpe de 27,5 s: **170 ms de música sola**. La voz sigue llegando cortada de origen; el fundido evita el chasquido pero la vocal se acorta | NO COMPROBABLE SIN OÍDO HUMANO (probable: se oye seca/cortita pero sin clic) |
| 5 | Pausas acortadas (duración real, hueco por debajo de −45 dB / de −60 dB) | «So,» 0,095 / 0,080 s · «Wow,» 0,105 / 0,100 · L4 («365:») 0,100 / 0,085 · L5 («days:») 0,095 / 0,080 · L7 («thousand,») 0,110 / 0,100. Ninguna es cero ni pega palabras (mínimo 0,080 s de silencio real, a −60 dB). **Las acortadas con valor por debajo de 0,10 s** son «So,» y L5 a −45 dB y las cuatro primeras a −60 dB. Las no tocadas son del mismo orden (L3 «seventeenth,» 0,09 a 0,115 s; L6 «sixty-three days:» 0,085 a 0,175 s), así que suenan igual de apretadas que el resto de Tin. La constante dice 0,15 s: es el hueco medido entre bordes de tramo (a −35 dB), con 0,055 s de margen de cada palabra dentro; el silencio puro es ≈ 0,095 s | PASA (nadie pegado, ninguna a cero); NO COMPROBABLE SIN OÍDO HUMANO si suenan atropelladas |
| 6 | Velocidad 110 % | Cociente de duración (tramos originales con márgenes y pausa insertada) frente a la línea del diálogo: L1 1,094 · L2 1,097 · L3 1,095 · L4 1,096 · L5 1,098 · L6 1,098 · L7 1,094 · L8 1,097 · L9 1,116 (a la grabación de Tin le faltan 30 ms de margen al final: termina a 25,60 s). Total 1,098. Coincide con `atempo=1,10` (el 0,2 % de diferencia son redondeos y el fundido de 8 ms). Prueba de que el tono no cambia: no medida (es propiedad de `atempo`) | PASA |
| 7a | Golpe del fotograma 0 frente a la primera sílaba | `thunk` y `zumbido` en 0,0004 s; la voz sube de −58 dB (0 a 10 ms) a −28 dB (10 a 20 ms) a −13 dB (20 a 30 ms): la primera sílaba empieza ≈ 15 ms después, dentro del mismo fotograma (33 ms). Voz/fondo en 0 a 0,1 s: **+1,6 dB** (el golpe cubre el inicio de «Re-»); 0,1 a 0,3 s: +9,8 dB. El golpe está pensado así (es el arranque del bucle), pero tapa unos 20 a 30 ms de la «R» | PASA (en tiempo); el efecto sobre «Remember»: NO COMPROBABLE SIN OÍDO HUMANO |
| 7b | Nivel de golpes bajo la voz | Efectos bajo la voz −26,0 LUFS contra voz −14,7 LUFS (−11,3 dB); pico de efecto frente a nivel RMS de la voz en la misma ventana de 50 ms: de −3,3 a +10,8 dB sobre la voz RMS y siempre ≤ al pico de la voz; ningún golpe supera al pico de la voz en su ventana. Los 47 golpes empiezan en su tiempo (≤ 1 ms) | PASA |
| 7c | Silencio/empalme del bucle | Último fotograma de audio (28,50 s): ≈ 0,00004; primero: 0,0002 a −0,0014. Salto en el empalme: 0,0013. Últimos 20 ms: −31,6 dB (solo música, sin voz); primeros 20 ms: −9,6 dB (thunk). Sin clic; la entrada es golpe seco, a propósito. 0,0013 s de desfase de duración entre audio (28,5013 s) y video (28,5000 s): inaudible | PASA |
| 8a | Sonoridad integrada (mp4) | **−14,0 LUFS** (`ebur128`); `postpro.py info` del mp4 confirma 28,50 s, AAC 48 kHz | PASA |
| 8b | Pico real | **−1,3 dBTP** (≤ −1) | PASA |
| 8c | Rango de sonoridad (LRA) | **1,9 LU** (voz sola, `dialogo_110.mp3`: −14,7 LUFS, LRA 1,9, pico −1,7). Volumen parejo, sin saltos | PASA |
| 9 | Música que tape la voz | Voz/música por línea: 5,9 a 10,0 dB (mínimo L2); voz/efectos por línea (sin L3 y L8, sin efectos) 9,8 a 22,9 dB. Estrés +18 dB sin errores | PASA en medida; NO COMPROBABLE SIN OÍDO HUMANO si se siente cargada |
| 10 | Voz, idioma y velocidad según `canales/nostalgia-tin-y-tan/voces.md` | Tan Zelda, Tin Kevin, inglés, 110 % (`atempo`), cada voz a −14 LUFS antes de armar | PASA |

## Firma

**FIRMADO con salvedades.**

Se firma que la voz dice el guion palabra por palabra, que resiste una mezcla 18 dB más fuerte de fondo sin perder una palabra, que no hay clics ni saturación de montaje, que la sonoridad está en −14,0 LUFS y −1,3 dBTP y que la velocidad es la del canal. Salvedades (solo al oído, **antes de publicar**, a cargo del dueño o de quien pueda oír):

1. «now» al final: ¿suena cortada o aceptable con el fundido de 120 ms?
2. Ataque de «eight» en 22,23 s (viene de la grabación).
3. «G T A» letra por letra y las cifras (4,745 · 4,748 · 4,811): pronunciación y acento.
4. Pausas de 0,08 a 0,11 s tras «So,», «Wow,», «365:», «days:» y «thousand,»: ¿naturales o atropelladas?
5. Los primeros 100 ms: el `thunk` cubre el inicio de «Remember» (+1,6 dB).

## Arreglos pedidos

Ninguno obligatorio. No bloquea la entrega. Si la escucha confirma la salvedad 1 (y solo entonces, porque mueve el audio):

| Archivo | Constante o tiempo | Hoy | Propuesto | Por qué |
|---|---|---|---|---|
| `codigo/armar_dialogo.py` (bloque del fundido final, `n = int(0.12 * SR)`) | duración del fundido de «now» | 0,12 s | 0,20 s (la voz empieza a caer en 27,13 s en lugar de 27,21 s; nada cambia de lugar ni de duración) | «now» tiene vocal larga; el fundido más largo se parece más a su caída natural. No cambia ningún tiempo de la línea de tiempo |
| `codigo/audio.py` | cola de «now» (nuevo, opcional) | no hay | 0,15 a 0,20 s de reverberación corta o eco muy suave sobre 27,33 a 27,50 s, a −30 LUFS | llenaría los 170 ms de música sola antes del golpe de 27,5 s. Solo si el fundido más largo no basta; se decide al oído |

No pido cambiar `PAUSA_INTERNA` (0,15 s): alargarla mueve todos los cortes de las líneas siguientes (de 0,03 s en «So,» a 0,15 s al llegar a «Wow,») y rompe la rejilla de 0,5 s; solo se tocaría si el oído las siente atropelladas, y entonces se rehace la línea de tiempo entera.

## Hallazgo sobre las herramientas

`revisar_voz.py --tramos` sobre el mp4 marca «el audio termina con voz sonando: posible final cortado» (−31 dB en los últimos 50 ms). Es un falso positivo para la mezcla: en 28,5 s ya no hay voz (termina en 27,33 s) y esos −31 dB son la música. El aviso solo vale sobre la voz sola (`dialogo_110.mp3`), donde sí se confirmó el corte de origen en «now».
