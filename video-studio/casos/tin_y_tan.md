# Caso: Tin & Tan

> El canal nació el 2026-11-20 como «canal de nostalgia». Desde el 2026-11-24 ya no se define así: ver «Cambio de
> parámetros» más abajo y `canales/nostalgia-tin-y-tan/PARAMETROS.md`. Lo que sigue hasta esa sección es la historia tal como fue.

Registro de cómo se montó el segundo par de personajes. Es el ejemplo de un video **dibujado con
código**, sin generador de video. Sigue las fases de `MANUAL.md` y se actualiza cuando avanza.
El otro ejemplo, con generador de video, es `tiky_y_lumi.md`.

## Fase 0 — Decisiones

| Decisión | Respuesta | Quién | Fecha |
|---|---|---|---|
| Personajes | Tin (hace la cuenta) y Tan (recuerda y pregunta), muñecos de palitos. **Desde el 2026-11-24:** Tan pregunta; Tin responde con datos | Dueño | 2026-11-21 |
| Canal | «Tin & Tan», nuevo y aparte del infantil; por crear | Dueño | 2026-11-21 |
| Formato | Short vertical 9:16 | Dueño | 2026-11-21 |
| Idioma y país | Inglés, Estados Unidos | Dueño | 2026-11-21 |
| Música | Hecha con código | Dueño | 2026-11-21 |
| Voces | Kevin para Tin, Zelda para Tan, aceleradas un 10 % | Dueño | 2026-11-21 |
| Gancho | «how many turns?»; variante para probar: «1,170 turns?» | Equipo | 2026-11-21 |
| Objetivo | Presencia y línea base de retención, sin llamado a la acción | Equipo | 2026-11-21 |
| Edad del público | 45 a 70 años, núcleo en mayores de 50. **Sin efecto desde el 2026-11-24:** sin edad fija | Equipo | 2026-11-21 |
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
| Voz de Tin y de Tan (prueba reutilizada como final) | 3 | — |
| Corrección del remate «For one side» y unidades imperiales (autorizada por el dueño) | 1,8 | — |
| **Video en inglés TIN-EN-S-001** | **4,8** | ≈ 405 mil tokens hasta el render v1, sin contar la revisión y la entrega |
| Voz de Tin en español con Juan (descartada: sonaba a italiano o portugués) | 2,2 | — |
| Prueba de Tan en español con Zelda (MiniMax) | 0,15 | — |
| **Total del proyecto** | **7,15** | |

## Fase 8 — Revisión, entrega y publicación (2026-11-21)

- El equipo de producción revisó el v1 y corrigió el remate («For one song» era falso: 1.170 vueltas son un lado
  entero) y las unidades (pulgadas y pies para EE. UU.). Render v2 gratis.
- Entrega por Drive al publicador; el video se recomprimió a ≈ 2,8 MB (límite de subida de la sesión ≈ 3,1 MB).
- La miniatura horizontal se recortaba en Shorts: se hizo una vertical, y el Canal automatizado armó una versión del
  video que abre con portada (regla nueva de portada de Shorts).
- **Publicado por el dueño el 2026-11-21:** https://youtube.com/shorts/s9r5bmmNykY (la subida privada anterior,
  C9i9Fff5Pu4, se borró). Las metas corren desde ese día: visto frente a deslizado ≥ 60 % a 3 días (2026-11-24),
  duración media ≥ 20 s y ≥ 80 % de vistas desde el feed de Shorts a 7 días (2026-11-28), ≥ 50 % de público de 45 o
  más a 28 días (2026-12-19).
- Hallazgos después de entregar, que se dejaron así por decisión del dueño: «421 ft» debía ser «≈ 422 ft», y las
  cifras con fracción no llevan «≈»; el tomate funciona como segundo acento. Detalle en `07_revision/controles.md`.

## Cambio de parámetros (2026-11-24)

- **Regla del dueño, textual:** «Cambia esas limitantes y define nuevos parámetros; podría ser que los parámetros sean
  flexibles; con este cambio de parámetros considera cambios en todo lo demás si es necesario, incluso en banner e
  imagen de perfil, etc.»
- **Motivo:** el equipo trataba como reglas fijas cosas que nadie midió (canal de nostalgia, público de 45 a 70,
  «pregunta + cuenta + cifra», no repetir tipo de cuenta, filtro de títulos por opinión). Dato del short 1 a las
  48 h: 20,7 % se quedó a mirar, 0 compartidos, 0 suscriptores. Un solo video medido: punto de partida, no prueba.
  El objetivo es entrar al Programa de socios lo antes posible.
- **Corrección del dueño el mismo día:** la primera versión dejaba la nostalgia como «un sabor posible» y la rechazó
  («me seguís colocando nostalgia aun cuando me dijiste que es una limitante; no es lógico»). Quedó **eliminada** como
  criterio: no elige tema, emoción, objeto, público ni título. La cuenta pasó a ser opcional.
- **Qué quedó:** `canales/nostalgia-tin-y-tan/PARAMETROS.md` (lo fijo, los parámetros flexibles con su métrica y la
  bitácora). Tin & Tan explican con hechos comprobados lo que la gente ya está mirando; Tan pregunta, Tin responde
  con datos; el tema lo pone la demanda verificable; revisión cada 5 videos.
- **Qué se cambió con eso** (todo gratis, texto y código): `README.md` y `DESIGN.md` del canal, el plan del Programa
  de socios (secciones 4 y 5), las fichas de Tin y Tan y el registro, `comercial/titulos.md` y `revisar_titulo.py`
  1.1 (lo que era opinión pasó de bloqueo a aviso; `--estricto` devuelve lo anterior), el radar (criterio de encaje y
  paso de actualidad), notas en `manual/13` y `manual/14`, y la marca: banner, descripción y palabras clave nuevos
  (`marca/`, versión anterior en `marca/anterior_2026-11-21/`). La foto de perfil y la marca de agua no cambiaron.
- **Qué no se tocó:** los shorts 1 y 2 (definidos con los parámetros anteriores), los rasgos, colores y voces de Tin
  y Tan, los umbrales y las fuentes del plan.
- **Pendiente:** cargar la marca nueva en YouTube (necesita el sí del dueño; lo hace Keter) y la firma del director
  de fotografía al umbral de `revisar_color.py` para videos con profundidad (`DESIGN.md`).

## Qué enseña este caso (ya está en el manual)

1. En un video hablado, la voz se hace primero y la imagen se ajusta a ella.
2. La voz se prueba con el texto real: si gusta, ya es la voz final.
3. La velocidad y el volumen de la voz se cambian gratis en edición.
4. Un personaje dibujado con código se define igual que uno generado: proporciones, lados, lista de comprobación y fallos conocidos.
5. Las correcciones de código no cuentan como segundo intento.
6. El gancho no entrega la respuesta: abre la pregunta.
7. Los videos terminados se entregan por Drive; el repositorio guarda el código que los rehace.
8. Los nombres propios llevan mayúscula aunque el estilo pida minúsculas (el banner salió «tin & tan»).
9. Las cifras con decimales o fracciones se aproximan y llevan «≈»; se redondea, no se trunca.
10. Un Short lleva su portada dentro del video y una miniatura vertical; la horizontal se recorta.
11. Cada video escribe por qué eligió cada color y cómo ayuda al objetivo (2 neutros + 1 acento).
12. Los controles de calidad bloquean: texto, cifras, voz, imagen, video, color, entrega y marca (`manual/12`).
13. Una regla que nadie midió es una hipótesis: se escribe como parámetro, con su métrica y la señal que lo cambia, y
    se separa de lo que de verdad es fijo (2026-11-24). Lo que el dueño elimina no se deja como «opción».

Nota: el punto 6 («el gancho no entrega la respuesta») era regla hasta el 2026-11-24; ahora la cifra en el título o
en la portada se decide por video y se mide.

## Pendiente

- Revisión de resultados del director creativo cuando el dueño exporte las estadísticas: primera el 2026-11-24
  (visto frente a deslizado, 3 días), luego el 2026-11-28 y el 2026-12-19.
- Versión en español: espera el veredicto del dueño sobre la prueba de Zelda con MiniMax.
- Temas del canal: los pone la demanda verificable (radar y análisis de temáticas); el equipo decide y le informa al
  dueño, que acompaña con ideas y ajustes (`PARAMETROS.md`).
- Cargar en YouTube la marca versión 2 (banner, descripción, palabras clave): espera el sí del dueño.
