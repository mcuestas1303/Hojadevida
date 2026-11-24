# Línea de tiempo de la voz (110 %)

Diálogo `dialogo_110.wav`, armado con `codigo/armar_dialogo.py` a partir de `voz_tan_zelda.wav` y
`voz_tin_kevin.wav` (una generación cada una; no se regeneran). Duración del diálogo: 29.58 s.
**En el video la voz entra en el fotograma 14 (0.467 s)**, como pide la firma del lápiz bumerán
(`canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`, sección 7): los tiempos de la tabla son los del video.

Cada línea al 110 % (`atempo=1.1`, sin cambiar el tono), 0.23 s entre líneas. Pausas internas
fijadas en edición: 0.15 s (líneas 2 y 9), 0,20 s (líneas 7 y 10), 0,25 s (línea 11, entre la
pregunta y la invitación) y **0,45 s tras «Apple:»** (línea 8; en el original eran 0,14 s: se alargó con silencio
para el silencio antes del número). La coletilla «That's all, folks.» de los dos archivos no se usa.

Cortes hechos por las pausas medidas (`silencedetect` a −35 dB) y comprobados con `revisar_voz.py --tramos`
(Whisper small.en): el texto de cada tramo es el reconocido. **Ninguna persona ha escuchado el audio.**

| Línea | Quién | Empieza (s) | Termina (s) | Dura (s) | Texto | Segundo tramo empieza (s) | De dónde sale |
|---|---|---|---|---|---|---|---|
| 1 | Tan | 0.47 | 3.46 | 2.99 | Was Jensen Huang's comeback in eleven days fast? | — | `voz_tan_zelda.wav`: 0.47 a 3.68 s («Was Jensen Huang's comeback in eleven days fast?») |
| 2 | Tin | 3.69 | 6.55 | 2.87 | He resigned from Nvidia on November twelfth after a scandal. | 4.96 | `voz_tin_kevin.wav`: 0.27 a 1.47 s («He resigned from Nvidia»); 1.98 a 3.70 s («on November twelfth after a scandal.») |
| 3 | Tin | 6.78 | 9.10 | 2.32 | On the seventeenth the board said it would not bring him back. | — | `voz_tin_kevin.wav`: 4.07 a 6.54 s («On the seventeenth the board said it would not bring him back.») |
| 4 | Tin | 9.33 | 11.74 | 2.41 | Six days later it reinstated him as C E O. | — | `voz_tin_kevin.wav`: 6.86 a 9.45 s («Six days later it reinstated him as C E O.») |
| 5 | Tin | 11.97 | 14.23 | 2.26 | Before that: more than thirty-three years in charge. | — | `voz_tin_kevin.wav`: 9.73 a 12.14 s («Before that: more than thirty-three years in charge.») |
| 6 | Tan | 14.46 | 16.12 | 1.66 | Fast compared to who? | — | `voz_tan_zelda.wav`: 4.76 a 6.52 s («Fast compared to who?») |
| 7 | Tin | 16.35 | 18.77 | 2.42 | Sam Altman at OpenAI: five days. | 18.04 | `voz_tin_kevin.wav`: 12.52 a 14.13 s («Sam Altman at OpenAI:»); 14.36 a 15.11 s («five days.») |
| 8 | Tin | 19.00 | 22.48 | 3.49 | Steve Jobs at Apple: four thousand, three hundred eighty-two days. | 20.63 | `voz_tin_kevin.wav`: 15.64 a 16.92 s («Steve Jobs at Apple:»); 17.06 a 19.07 s («four thousand, three hundred eighty-two days.») |
| 9 | Tan | 22.71 | 24.49 | 1.78 | That is twelve years? | 23.45 | `voz_tan_zelda.wav`: 7.76 a 8.37 s («That is»); 9.04 a 10.15 s («twelve years?») |
| 10 | Tin | 24.72 | 26.73 | 2.00 | Faster than Jobs. Slower than Altman. | 25.90 | `voz_tin_kevin.wav`: 19.43 a 20.47 s («Faster than Jobs.»); 20.73 a 21.61 s («Slower than Altman.») |
| 11 | Tan | 26.96 | 30.05 | 3.09 | Who else came back? Subscribe for the next count. | 28.29 | `voz_tan_zelda.wav`: 11.05 a 12.21 s («Who else came back?»); 13.06 a 14.96 s («Subscribe for the next count.») |

## Dudas de los cortes

- Línea 10: «Slower than Altman.» está pegada a la coletilla en el archivo de Tin (0,15 s entre «Altman» y
  «That's all»). Se cortó en 21,61 s (+0,03 s de margen) con un fundido de salida de 60 ms. Con `revisar_voz.py`
  se oye «Altman» entero y nada de la coletilla; la cola de la «n» solo la puede juzgar una persona.
- El archivo de Tan termina con la coletilla cortada por el generador («folks» con la voz aún sonando): no
  afecta, la coletilla no se usa. «Subscribe for the next count.» tiene 0,82 s de silencio detrás; se tomó
  0,12 s más allá del umbral de −35 dB (hasta 14,96 s) con fundido de 100 ms para no cortar la cola de «count».
- Líneas 5 y 6 conservan dentro una pausa corta del original (0,13 s tras «Before that:» y 0,22 s en «Fast
  compared / to who?») que no se tocó.
- La pronunciación de «Nvidia», «Huang», «OpenAI» y «C E O» no se puede juzgar con medidas: el reconocedor las
  transcribe bien («Nvidia», «Huang's», «OpenAI», «CEO»), y eso solo dice que se entienden.
