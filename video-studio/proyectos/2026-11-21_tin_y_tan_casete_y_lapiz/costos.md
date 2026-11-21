# Registro de costos

Anota cada generación, también las fallidas: es lo que permite ver qué tomas están
quemando el presupuesto y corregir el prompt en vez de seguir tirando intentos.

| Fecha | Toma | Tipo (keyframe / borrador / final) | Segundos | Intento # | Costo | ¿Sirvió? | Qué falló |
|---|---|---|---|---|---|---|---|
| 2026-11-21 | Voz de Tin (5 líneas) | audio | 21,8 | 1 | 2,2 | Sí | — |
| 2026-11-21 | Voz de Tan (3 líneas) | audio | 12,5 | 1 | 0,8 | Sí | — |
| 2026-11-21 | Render completo por código (16 tomas, 2 vueltas de revisión) | final | 30,0 | 1 | 0 | Sí | — |
| 2026-11-21 | Efectos y música sintetizados con código | audio | 30,0 | 1 | 0 | Sí (medido; falta escucharlo) | — |

Total gastado: 3 créditos (prueba de voces, reutilizada como voz del video).

**Render (2026-11-21):** el video `06_final/tin_y_tan_short01_v1.mp4` se dibujó con `codigo/render.py` (Pillow, numpy y
ffmpeg) y el audio con `codigo/audio.py`. Costó **0 créditos**: no se usó Higgsfield ni ningún servicio de pago. Cada
render tarda unos 81 s en este equipo (4 núcleos) y las correcciones por código no cuestan. El total sigue en 3 créditos.
