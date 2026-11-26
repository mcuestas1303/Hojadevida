# Medidas de la voz real — short 4 (2026-11-26)

Una generación por voz (no se regeneran). Control con `revisar_voz.py` (Whisper small.en): **Tin 67 palabras, 0
diferencias; Tan 14 palabras, 0 diferencias** (`07_revision/voz_voz_tin_kevin.md` y `voz_voz_tan_zelda.md`).
**Ninguna persona ha escuchado el audio.**

| Voz | Archivo | Dura | Habla (suma de tramos) | Al 110 % |
|---|---|---|---|---|
| Tin (Kevin) | `voz_tin_kevin.wav` | 35,72 s | ≈ 25,0 s | ≈ 22,7 s |
| Tan (Zelda) | `voz_tan_zelda.wav` | 8,30 s | ≈ 5,1 s | ≈ 4,7 s |

## Qué cambia frente al plan de la dirección

- La dirección estimó a Tin en ≈ 19,9 s (596 f) con sus pausas. La voz real pide ≈ 22,7 s **sin** pausas: Kevin habló
  más despacio y partió las frases en tramos cortos (0,3 a 0,9 s de silencio entre ellos, que se cierran en edición).
- Con todas las frases el video queda en ≈ 34 a 35 s, fuera de la tolerancia (30 a 33 s). La dirección ya fija el
  orden de recorte (sección 2): primero «Each numbered game tells a new story» con su golpe (≈ 1,7 s de voz), luego la
  pausa del remate y los respiros entre líneas. La tabla de fotogramas se recalcula con estas medidas antes de
  construir la pelea.
- «to GTA 6» suena con entonación de pregunta según el reconocedor («to GTA 6?»); lo juzga un oído humano.
- El archivo de Tan termina sin silencio (−44 dB en los últimos 50 ms): «facts» lleva fundido de salida y la cola la
  juzga una persona.
- Zelda hizo 0,30 s de pausa en «So, GTA 7?» (se temía 0,7 a 0,8 s): no hace falta comprimirla.
