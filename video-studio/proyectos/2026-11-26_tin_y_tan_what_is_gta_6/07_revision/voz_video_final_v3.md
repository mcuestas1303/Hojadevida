# Control de voz · tin_y_tan_short04_v3.mp4 (sha256 511571dd5f4d…)

Duración: 32.87 s. Reconocedor: Whisper small.en (sherpa-onnx), sin conexión. Salida de `revisar_voz.py --guion`.

## Lo que se oye

> Will there be a GTA 7? GTA is short for Grand Theft Auto. A game series that started in 1997 made today by Rockstar Games. GTA 6. It came out on November 19th, 2026. It's the sixth numbered game. Subscribe. We check the facts. Rated M 17 and over. From GTA 5 to GTA 6. 13 years and 63 days. So, GTA 7? Rockstar hasn't announced one. As of today.

## Contra el guion

> Will there be a GTA 7? GTA is short for Grand Theft Auto: a game series that started in 1997, made today by Rockstar Games. GTA 6 came out on November 19, 2026. It's the sixth numbered game. Subscribe. We check the facts. Rated M: seventeen and over. From GTA 5 to GTA 6: thirteen years and sixty-three days. So, GTA 7? Rockstar hasn't announced one. As of today.

**NO COINCIDE: 1 diferencia(s)** (74 palabras en el guion, 75 oídas)

- SOBRA: «it»

## Comprobaciones para ubicar la diferencia (diseñador de sonido, 2026-11-27)

- `05_audio/dialogo_110.wav` (voz sola): el reconocedor oye «GTA 6 came out on November 19, 2026», sin «it».
- Tramo de 4.2 s del propio video v3 (10.4–14.6 s, con efectos y música): oye «GTA 6 came out on November 19th, 2026», sin «it».
- Conclusión por medida: el «it» aparece solo al transcribir el video entero (mismo comportamiento que en la v2); la voz no lo
  dice. No se puede descartar por medida un sonido de fondo que el reconocedor tome por palabra: lo decide un oído humano.

Límite: esto reconoce palabras; no juzga naturalidad, acento ni mezcla. Falta la escucha de una persona antes de publicar.
