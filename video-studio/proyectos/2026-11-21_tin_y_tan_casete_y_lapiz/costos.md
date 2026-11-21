# Registro de costos

Anota cada generación, también las fallidas: es lo que permite ver qué tomas están
quemando el presupuesto y corregir el prompt en vez de seguir tirando intentos.

| Fecha | Toma | Tipo (keyframe / borrador / final) | Segundos | Intento # | Costo | ¿Sirvió? | Qué falló |
|---|---|---|---|---|---|---|---|
| 2026-11-21 | Voz de Tin (5 líneas) | audio | 21,8 | 1 | 2,2 | Sí | — |
| 2026-11-21 | Voz de Tan (3 líneas) | audio | 12,5 | 1 | 0,8 | Sí | — |
| 2026-11-21 | Render completo por código (16 tomas, 2 vueltas de revisión) | final | 30,0 | 1 | 0 | Sí | — |
| 2026-11-21 | Efectos y música sintetizados con código | audio | 30,0 | 1 | 0 | Sí (medido; falta escucharlo) | — |
| 2026-11-21 | Voz de Tin, líneas 4, 5, 6 y 8 en pulgadas/pies + «For one side.» (Kevin, job `d86721f1-5d5f-454d-b048-e40bab17e012`) | audio | — | 1 | 1,8 | — | — |

| 2026-11-21 | Voz de Tin en español (Juan), versión ES · job `09be09bb-dc2c-40d5-aa14-74d8bae2a5ba` | audio | 20,4 | 1 | 2,2 | No | El dueño: «Juan se escucha como un italiano o un portugues». No se regenera sin su autorización; la voz de Tan (Marisol) no se generó |
Total gastado: 7,0 créditos (4,8 del video en inglés + 2,2 de la voz de Tin en español descartada)

Total anterior: 4,8 créditos (3 de la prueba de voces reutilizada + 1,8 de la corrección autorizada por el dueño el 2026-11-21).

**Render (2026-11-21):** el video `06_final/tin_y_tan_short01_v1.mp4` se dibujó con `codigo/render.py` (Pillow, numpy y
ffmpeg) y el audio con `codigo/audio.py`. Costó **0 créditos**: no se usó Higgsfield ni ningún servicio de pago. Cada
render tarda unos 81 s en este equipo (4 núcleos) y las correcciones por código no cuestan. El total sigue en 3 créditos.
