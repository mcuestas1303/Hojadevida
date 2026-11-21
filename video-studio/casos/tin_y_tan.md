# Caso: Tin y Tan, canal de nostalgia

Registro de cómo se montó el segundo par de personajes. Es el ejemplo de un video **dibujado con
código**, sin generador de video. Sigue las fases de `MANUAL.md` y se actualiza cuando avanza.
El otro ejemplo, con generador de video, es `tiky_y_lumi.md`.

## Fase 0 — Decisiones

| Decisión | Respuesta | Quién | Fecha |
|---|---|---|---|
| Personajes | Tin (hace la cuenta) y Tan (recuerda y pregunta), muñecos de palitos | Dueño | 2026-11-21 |
| Canal | «Tin & Tan», nuevo y aparte del infantil; por crear | Dueño | 2026-11-21 |
| Formato | Short vertical 9:16 | Dueño | 2026-11-21 |
| Idioma y país | Inglés, Estados Unidos | Dueño | 2026-11-21 |
| Música | Hecha con código | Dueño | 2026-11-21 |
| Voces | Kevin para Tin, Zelda para Tan, aceleradas un 10 % | Dueño | 2026-11-21 |
| Gancho | «how many turns?»; variante para probar: «1,170 turns?» | Equipo | 2026-11-21 |
| Objetivo | Presencia y línea base de retención, sin llamado a la acción | Equipo | 2026-11-21 |
| Edad del público | 45 a 70 años, núcleo en mayores de 50 | Equipo | 2026-11-21 |
| Presupuesto del canal | Propuesta de US$500 en 90 días, sin confirmar | — | — |

## Fase 1 — Los personajes

- Diseñados por el equipo de producción como código: `herramientas/palitos.py` (8 expresiones, 9 poses, 3 vistas).
- Fichas en `personajes/tin/` y `personajes/tan/`. Su «Definición para generar» no describe un prompt de imagen
  sino cómo se dibujan, sus proporciones en radios de cabeza y los fallos conocidos del dibujo.
- Regla de lados: Tan a la izquierda del cuadro con espejo, Tin a la derecha.
- Diseño del canal (paleta, tipografía, movimiento, voz): `canales/nostalgia-tin-y-tan/DESIGN.md`.

## Fase 2 — El canal en lugar de la serie

Este canal no usa `series/`: no es infantil y no pasa por la pedagoga ni la psicóloga. Sus reglas están en
`canales/nostalgia-tin-y-tan/` y en `manual/11_retencion_y_revision.md`.

## Fases 3 a 5 — Short 1, «How many pencil turns to rewind a cassette?»

| Paso | Resultado |
|---|---|
| Proyecto | `nuevo_proyecto.py "Tin y Tan casete y lapiz" --redes` |
| Voz primero | Se probaron las voces con el texto real del video; esa misma grabación es la voz final |
| Línea de tiempo | El diálogo al 110 % dura 26,9 s; los tiempos de la voz mandan sobre la imagen |
| Prompt | 16 tomas, 30 s, rejilla de 0,5 s, 15 cortes; todas las tomas con método «edición» |
| Archivo | `personajes/tan/prompts/shorts/short01_how_many_pencil_turns_to_rewind_a_cassette.md` |

## Fases 6 y 7 — Dibujo y render

- Código en `proyectos/2026-11-21_tin_y_tan_casete_y_lapiz/codigo/`. Se renderiza con `python3 codigo/render.py`
  (unos 81 s) y da siempre el mismo archivo.
- Dos vueltas de revisión con hojas de contacto; decisiones tomadas donde el prompt no alcanzaba en
  `07_revision/decisiones_de_render.md`.
- El video terminado no se guarda en el repositorio.

## Costo

| Concepto | Créditos | Uso de Claude |
|---|---|---|
| Voz de Tin y de Tan | 3 | — |
| Prompt | 0 | 131 mil tokens |
| Dibujo, audio, render y revisión | 0 | 274 mil tokens |
| **Total** | **3** | **405 mil tokens** |

## Qué enseña este caso (ya está en el manual)

1. En un video hablado, la voz se hace primero y la imagen se ajusta a ella.
2. La voz se prueba con el texto real: si gusta, ya es la voz final.
3. La velocidad y el volumen de la voz se cambian gratis en edición.
4. Un personaje dibujado con código se define igual que uno generado: proporciones, lados, lista de comprobación y fallos conocidos.
5. Las correcciones de código no cuentan como segundo intento.
6. El gancho no entrega la respuesta: abre la pregunta.
7. Los videos terminados se entregan por Drive; el repositorio guarda el código que los rehace.

## Pendiente

- Revisión y presentación al dueño: equipo de producción. Nadie ha escuchado todavía el audio montado.
- Ficha de publicación en el formato del publicador de YouTube.
- Crear el canal «Tin & Tan».
- Confirmar el presupuesto del canal.
