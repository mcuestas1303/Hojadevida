# Manual del equipo de producción

Lo que el equipo tiene que saber para convertir un personaje terminado en contenido que se vea bien,
transmita la emoción buscada, cueste poco y llegue al público que paga. Cada agente lee los capítulos
de su oficio antes de trabajar; nadie trabaja de memoria.

## La regla de oro

> **Objetivo → emoción → lenguaje → herramienta más barata que lo logre → datos para la próxima.**

1. **Objetivo:** qué tiene que pasar después de verlo (seguir, compartir, guardar, aprender, comprar).
2. **Emoción:** qué siente quien lo ve, segundo a segundo (el arco).
3. **Lenguaje:** cámara, luz, actuación, sonido y montaje elegidos *por* esa emoción, no por gusto.
4. **Herramienta:** la ruta más barata que alcanza la calidad; lo que se puede editar no se genera.
5. **Datos:** cada video publicado deja números; el siguiente se decide con ellos.

## Capítulos

| # | Capítulo | Lo leen sobre todo |
|---|---|---|
| 01 | [Objetivo y emoción](01_objetivo_y_emocion.md): arco, gancho y la tabla emoción → lenguaje | director, todos |
| 02 | [Cámara](02_camara.md): planos, ángulos, lentes y movimientos con su frase de prompt | fotografía, prompts |
| 03 | [Luz, color y textura](03_luz_y_color.md) | fotografía, prompts |
| 04 | [Animación y actuación](04_animacion.md): cómo se mueve cada personaje según la emoción | animación, prompts |
| 05 | [Herramientas y costos](05_herramientas.md): qué modelo para qué, precios verificados, rutas baratas | jefe de producción, todos |
| 06 | [Los tres modos](06_modos.md): clip propio, clip para replicar, desde cero | jefe de producción, director |
| 07 | [Edición](07_edicion.md): ritmo, cortes, subtítulos, formatos y recetas de `postpro.py` | editor |
| 08 | [Audio](08_audio.md): voz, música, efectos y mezcla | sonido |
| 09 | [Prompts maestros](09_prompts_maestros.md): la fórmula y ejemplos completos con el elenco | prompts, fotografía, animación |
| 10 | [Algoritmo y monetización](10_algoritmo_y_monetizacion.md): métricas, lectura de estadísticas, requisitos para cobrar | director, jefe de producción |
| 11 | [Retención y revisión](11_retencion_y_revision.md): las 21 reglas por rol (gancho, loop, ritmo, golpes de sonido, gráficos con código, revisión fotograma a fotograma) | todos |

## El equipo

| Agente | Oficio | Entrega en el proyecto |
|---|---|---|
| `director-creativo` | Director creativo **y comercial**: idea, emoción, gancho, público, estadísticas | `02_prompt/direccion.md` §1–2 y §8 |
| `jefe-de-produccion` | Elige el modo y la ruta más barata, presupuesta, frena pérdidas | `02_prompt/direccion.md` §7 y `costos.md` |
| `director-de-fotografia` | Cámara, lente, luz y color de cada toma | `direccion.md` §3 |
| `director-de-animacion` | Actuación y movimiento del personaje; transferencia de movimiento | `direccion.md` §4 |
| `director-de-prompts` | Traduce todo lo anterior al prompt validado | `02_prompt/prompt.md` |
| `disenador-de-sonido` | Voz, música, efectos y mezcla | `direccion.md` §5 y `05_audio/` |
| `editor-de-video` | Montaje, subtítulos, color, formatos de salida | `direccion.md` §6 y `06_final/` |
| `supervisor-de-continuidad` | Revisa que el personaje sea fiel a su carpeta y que el video cumpla la dirección | `revision_produccion.md` |
| `analista-de-video` | Desarma un clip (propio o de referencia) en tomas, ritmo y estilo | `01_referencia/analisis.md` |

Para series infantiles se suma, antes del prompt, el equipo de `infantil/` (pedagoga, guionista, psicóloga).

El flujo completo lo coordina la conversación principal con el comando `/producir`
(`.claude/skills/producir/SKILL.md`).

## De dónde salen los personajes

Solo actúan los personajes **terminados**: los que tienen carpeta en `video-studio/personajes/` y figuran en
`personajes/REGISTRO.md`. La fuente de cada uno es su carpeta en Google Drive (`Personajes/…/01 Diseño aprobado` y
`02 Hojas de personaje`) y su bitácora en `creador-personajes/afinado/`. Lo que está en `03 Pruebas descartadas`
y en «No va» de la bitácora **nunca** se usa.
