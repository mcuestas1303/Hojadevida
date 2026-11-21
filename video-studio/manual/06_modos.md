# 06 · Los tres modos de trabajo

Todo proyecto empieza diciendo en `00_brief.md` cuál es su **modo**. El jefe de producción elige la ruta y el
presupuesto según el modo.

## Modo A · Clip propio

El dueño entrega un clip suyo (grabado por él o con permiso). Se aprovecha lo que ya existe: es el modo más barato.

| Qué se quiere | Ruta | Costo |
|---|---|---|
| Solo editarlo (cortar, ritmo, subtítulos, música, color, 9:16) | `editor-de-video` con `postpro.py` | **0** |
| Meter a un personaje haciendo lo mismo que el clip | `motion_control` (imagen del personaje + clip) o `hf_mult_motion_control` | 7 por segundo a 720p con Genjutsu (cotizar) |
| Convertir el clip entero al estilo de juguete | Genjutsu Styles (p. ej. *Rounded Toy CGI*) | cotizar en el formulario |
| Cambiar un objeto o una prenda | `hf_mult_replace_object` | cotizar |
| Agregar un personaje que reacciona al clip | toma nueva (modo C) montada en pantalla dividida o en corte | según tomas |

Pasos: `nuevo_proyecto.py <nombre> <clip>` → el `analista-de-video` describe tomas y ritmo → el director decide qué se
conserva → el jefe de producción elige la ruta → edición.

## Modo B · Clip para replicar

Se toma la **fórmula** de un video que funciona (estructura, ritmo, encuadres, tipo de gancho, remate) y se rehace
con nuestros personajes. **No se calca** el video de otro (decisión del dueño, 2026-11-07).

| Se copia | No se copia |
|---|---|
| Estructura de tomas y duración de cada una | Personas reales, caras, voces |
| Tipo de gancho y de remate | Música con derechos, audio original |
| Encuadres y movimientos de cámara | Marcas, logos, textos literales |
| Ritmo de corte | Personajes ajenos ni su estética reconocible |

Pasos: el `analista-de-video` hace la tabla de tomas de la referencia → el director la adapta al personaje y al
objetivo → fotografía y animación reescriben cada toma en nuestro lenguaje → prompts.
Si el valor del trend es **el movimiento exacto** (un baile), el dueño graba su propia versión y se pasa al modo A
con transferencia de movimiento.

## Modo C · Desde cero con IA

Del brief y el personaje al video, sin material previo.

1. **Director:** objetivo, emoción, gancho, arco (cap. 01) y público (cap. 10).
2. **Fotografía + animación:** plan de cada toma (cap. 02–04).
3. **Prompts:** keyframe y video de cada toma (cap. 09), validados.
4. **Producción:** keyframes baratos → aprobación → borradores 480p → aprobación → finales.
5. **Sonido y edición:** voz, música, efectos, montaje y salida por plataforma.
6. **Continuidad:** revisa antes de entregar.

## Combinaciones habituales

- **C + A:** se genera al personaje y se monta sobre un clip propio (el dueño como «el normal» de la dupla con Spike).
- **B → A:** la referencia da la estructura; el dueño graba el movimiento; se transfiere al personaje.
- **Serie infantil:** siempre C, con el equipo de `infantil/` antes del prompt.
