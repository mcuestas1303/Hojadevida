# Registro de costos

Anota cada generación, también las fallidas: es lo que permite ver qué tomas están
quemando el presupuesto y corregir el prompt en vez de seguir tirando intentos.

| Fecha | Toma | Tipo (keyframe / borrador / final) | Segundos | Intento # | Costo | ¿Sirvió? | Qué falló |
|---|---|---|---|---|---|---|---|

**Hasta el 2026-11-27, nada gastado:** no hay ninguna generación; la tabla está vacía a propósito.

## Costos previstos (2026-11-27)

| Pieza | Voz | Estimación | Estado |
|---|---|---|---|
| Líneas de Tin (8 líneas, 81 sílabas) | Kevin (`f1373f24-3b96-433f-9a68-e595810ef608`) | ≈ 2,0 a 2,3 créditos | **Estimación del diseñador de sonido, no cotización**; falta cotizar y falta el sí del dueño |
| Líneas de Tan (4 líneas, 23 sílabas) | Zelda (`b7aaea29-0c88-5925-90c0-8f66754cda53`) | ≈ 0,6 a 0,7 créditos | Ídem |
| **Total de voz** | | **≈ 2,6 a 3,0 créditos** | Nada gastado |

- **De dónde sale la estimación:** `direccion.md`, sección 5.4 (sonido) y sección 7: 104 sílabas, ≈ 26 a 30 s de voz generada a unos
  0,1 créditos por segundo de voz (`video-studio/consumo.md`). Referencias de lo que costó la voz de los shorts anteriores: ≈ 3,7 (short
  3) y ≈ 3,1 (short 4, 2026-11-26, con una generación por personaje).
- **Cómo se convierte en gasto:** producción cotiza con `estimate_audio_cost` (`seed_audio`) con el texto final de la dirección,
  muestra el número al dueño y espera su sí. **Sin ese sí no se genera.** Recomendación del comercial, como en el short 4: escribir las
  cifras y las siglas del texto que se manda a la voz en letras, para que la voz no pueda leerlas de otra manera. Lo decide producción.
- **Una sola generación por personaje.** Si al oírla falla una palabra, se arregla en edición por código (gratis); regenerar solo
  la línea que falló cuesta ≈ 8 a 9 s de voz (≈ 0,9 créditos) y necesita un nuevo sí del dueño con el número a la vista.
- **Tope del brief:** el de la voz (los shorts 3 y 4 costaron ≈ 3,7 y ≈ 3,1). La estimación queda por debajo del short 3 y a la
  altura del 4.

| Concepto | Costo previsto |
|---|---|
| Imagen y video (keyframes, clips, remates) | 0 créditos: dibujo y grabación por código con el motor de acción |
| Música y efectos de sonido | 0 créditos: por código |
| Composición, subtítulos, portada y firma | 0 créditos: por código |
| **Total previsto del video** | **≈ 2,6 a 3,0 créditos** (solo voz) |

Costo de Claude (tokens) del equipo: **sin dato**, no se lleva en este registro (el resumen del consumo del estudio está en
`video-studio/consumo.md`).
