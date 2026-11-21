# Línea de tiempo de la voz (110 %)

Diálogo `dialogo_110.mp3`, armado con `codigo/armar_dialogo.py` a partir de `voz_tan_zelda.wav` y
`voz_tin_kevin.wav` (una generación cada una). Duración del archivo: 27.38 s; la última línea termina en 27.33 s. En el video la voz empieza en el fotograma 0 (sin retraso): estos tiempos son los del video.

Cada línea al 110 % (`atempo=1.1`, sin cambiar el tono), 0.23 s entre líneas; las pausas internas
largas (tras «So,» y «Wow,», y las de Tin de más de 0,35 s) se acortaron a 0.15 s.

**Cortes hechos por las pausas medidas (`silencedetect` a −35 dB), sin escuchar.** El texto de cada tramo es el
probable por orden y duración: hay que comprobarlo al oído antes de publicar.

| Línea | Quién | Empieza (s) | Termina (s) | Dura (s) | Texto | Segundo tramo empieza (s) | De dónde sale |
|---|---|---|---|---|---|---|---|
| 1 | Tan | 0.00 | 1.93 | 1.93 | Remember buying G T A five at midnight? | — | `voz_tan_zelda.wav`: 0.48 a 2.53 s («Remember buying G T A five at midnight?») |
| 2 | Tan | 2.16 | 5.12 | 2.97 | So, how many days did we wait for G T A six? | 2.83 | `voz_tan_zelda.wav`: 3.50 a 4.08 s («So,»); 4.88 a 7.33 s («how many days did we wait for G T A six?») |
| 3 | Tin | 5.35 | 8.83 | 3.48 | G T A five came out September seventeenth, twenty thirteen. | — | `voz_tin_kevin.wav`: 0.40 a 4.14 s («G T A five came out September seventeenth, twenty thirteen.») |
| 4 | Tin | 9.06 | 13.64 | 4.58 | Thirteen years times three sixty-five: four thousand, seven hundred forty-five days. | 11.13 | `voz_tin_kevin.wav`: 4.84 a 6.95 s («Thirteen years times three sixty-five:»); 7.42 a 10.11 s («four thousand, seven hundred forty-five days.») |
| 5 | Tin | 13.87 | 17.54 | 3.67 | Add three leap days: four thousand, seven hundred forty-eight. | 15.26 | `voz_tin_kevin.wav`: 10.55 a 11.92 s («Add three leap days:»); 12.32 a 14.75 s («four thousand, seven hundred forty-eight.») |
| 6 | Tin | 17.77 | 21.15 | 3.38 | Plus sixty-three days: September seventeenth to November nineteenth. | — | `voz_tin_kevin.wav`: 16.26 a 19.91 s («Plus sixty-three days: September seventeenth to November nineteenth.») |
| 7 | Tin | 21.38 | 23.56 | 2.17 | Four thousand, eight hundred eleven days. | 22.23 | `voz_tin_kevin.wav`: 20.53 a 21.29 s («Four thousand,»); 21.72 a 23.11 s («eight hundred eleven days.») |
| 8 | Tan | 23.79 | 25.27 | 1.49 | Wow, that long? | 24.40 | `voz_tan_zelda.wav`: 8.24 a 8.76 s («Wow,»); 9.45 a 10.34 s («that long?») |
| 9 | Tin | 25.50 | 27.33 | 1.82 | A baby born that day is a teenager now. | — | `voz_tin_kevin.wav`: 23.63 a 25.60 s («A baby born that day is a teenager now.») |

## Dudas de los cortes (sin escucha)

- El número de tramos medidos coincide con el esperado en las dos voces (Tan 5, Tin 9).
- Línea 7 («Four thousand, / eight hundred eleven days.»): el tramo de 20,53 a 21,29 s se supone «Four thousand,» por su duración (0,76 s); no está confirmado al oído.
- Línea 9: el archivo de Tin termina en 25,60 s sin silencio de cola medible; se toma hasta el final. Si la última sílaba («now») quedó cortada por el generador, solo se nota al oído.
- Líneas 3, 4 y 5 conservan dentro una pausa corta (0,16 a 0,24 s en el original) que no se tocó.
- «G T A» letra por letra y la pronunciación de las cifras no se pueden comprobar con medidas.
