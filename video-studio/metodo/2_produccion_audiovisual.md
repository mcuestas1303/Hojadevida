# Método del Equipo de producción audiovisual — del paquete de prompt al video publicado

> **Origen:** pedido del dueño (2026-11-26): «y luego el método que tendría el equipo de producción audiovisual para
> producir el prompt». Recibe el paquete de `metodo/1_generador_de_prompts.md`. Versión 0.1. Lo ya probado en los shorts 1
> a 3 se dice; lo del formato de acción y del universo todavía no se ha producido completo.

> **De quién es este método (dueño, 2026-11-26):** del Equipo de producción audiovisual. El Generador de prompts entrega
> el paquete y no produce.

## 0. Orden entre imagen y audio (decisión de producción, 2026-11-26)

El dueño propuso: «el video va primero y después va el audio». **Producción lo adopta desde el video siguiente al short 4,
con una precisión:** lo primero es la imagen *en borrador*, no la imagen terminada.

1. **Animática muda** (pasada en seco del motor, 0 créditos, ≈ 1 min): coreografía, cámaras y tiempos de cada golpe,
   medidos con `codigo/control_encuadre.py` hasta que dé PASA. Aquí se decide cuánto dura cada tramo.
2. **Voz**, generada una sola vez, con la duración de cada línea ya conocida por la animática. Si una línea sale más
   larga o más corta, se absorbe en edición (velocidad del canal ±10 %) y en los tramos de reposo de la imagen, que
   están para eso; no se regenera.
3. **Render de la imagen** con los tiempos finales, y después **efectos, música y mezcla**, cada sonido en su fotograma.

- **Por qué:** con la voz primero (short 4) los golpes quedaron atados a las pausas de la voz y la pelea se corrigió tres
  veces; la imagen por código es gratis y se puede rehacer, la voz cuesta créditos y tiene un solo intento. Lo caro se
  genera cuando ya se sabe qué tiene que durar.
- **Cómo se mide si fue buena decisión:** número de versiones de imagen hasta pasar la puerta (short 4: cuatro) y
  retención en los golpes en la lectura de Studio a 48 horas.
- **Excepción:** el short 4 conserva su voz ya generada y sus tiempos (no se regenera sin el sí del dueño).
- En la tabla de abajo esto cambia el orden de trabajo a **A3 → A5 (en borrador) → A4 → A5 (final) → A6 → A8 → A7 → A9**.

## 0b. Antes de escribir una pelea y antes de renderizar

Se lee `metodo/registro_de_fallos.md`: los patrones de fallo que ya costaron versiones, la lista de comprobación previa
al render (sección 3) y el banco de movimientos. Al cerrar cada versión se le añade una fila a su bitácora. Regla que sale
de ahí: **todo defecto que un revisor encuentre a ojo y se pueda medir se convierte en prueba del control antes de
corregirlo.**

## 1. Qué recibe y control de entrada

El paquete P1 a P12. **No se empieza a producir si falta una pieza marcada «bloquea»**; se devuelve con la lista de lo que
falta (regla «ninguna prueba a medias»).

| Control de entrada | Quién |
|---|---|
| El paquete está completo y el prompt pasó `validar_prompt.py` | `jefe-de-produccion` |
| Todo personaje del elenco está en `personajes/REGISTRO.md` con hoja aprobada | `supervisor-de-continuidad` |
| La lista de piezas dice de dónde sale cada una | `jefe-de-produccion` |
| Los pedidos que bloquean están cerrados | `jefe-de-produccion` |

## 2. Los pasos

| Paso | Qué hace | Quién | Con qué | Sale |
|---|---|---|---|---|
| A1 | **Plan de producción:** ruta de cada plano (código, generado o mixto), orden, máquina donde se produce, tiempo | `jefe-de-produccion` | `motor_de_accion/`, cotizaciones | Plan y `costos.md` previsto |
| A2 | **Cotizar** lo que se genere con créditos y pedir el sí del dueño con el número a la vista | Conversación principal | `estimate_*_cost` | Su sí por pieza |
| A3 | **Construir lo que falta** en el motor: entorno del tema, utilería que se rompe, efectos, poses, piezas del universo (pistas, cicatrices) | `director-de-animacion`, `editor-de-video` | `motor_de_accion/` | Piezas nuevas con entrada en `catalogo.json` |
| A4 | **Voz:** generar las líneas (una sola vez), acelerar según el canal, línea de tiempo | `disenador-de-sonido` | `generate_audio`, `postpro.py` | `05_audio/` |
| A5 | **Animar:** guion de la pelea con los tiempos de golpe medidos; cámara; cambios de velocidad | `director-de-animacion` | Motor; estudio de referencias | Guion del video en `guiones/` |
| A6 | **Generar** los planos aprobados con créditos, **una sola vez por pieza** | Conversación principal | `generate_video`, definición cerrada | `04_clips/` |
| A7 | **Sonido:** golpes, choques, explosiones, música si la hay; cada sonido en su fotograma | `disenador-de-sonido` | `sonidos/`, `postpro.py` | Mezcla a −14 LUFS |
| A8 | **Montaje:** render, dato en pantalla, subtítulos quemados y `.srt`, firma, portada en el primer segundo | `editor-de-video` | `render.js`, `ensamblar.py`, `postpro.py` | `06_final/` |
| A9 | **Revisión**, todo bloqueante: fotogramas a 2 f/s, destellos, voz contra guion, color, texto y nombres, continuidad con la hoja de personaje, universo (pista cobrada y sembrada donde dice el brief), «se entiende solo», requisitos del formato uno por uno | `supervisor-de-continuidad`, `director-de-fotografia` | `revisar_fotogramas.py`, `comprobar_destellos`, `revisar_voz.py`, `revisar_color.py`, `revisar_texto.py` | `07_revision/` con firmas; rúbrica puntuada con `puntuar_ficha.py` |
| A9b | **Puerta de presentación (bloquea).** Cada oficio (animación, fotografía, sonido, edición, continuidad) revisa la pieza terminada y firma en `07_revision/firmas.md` sobre el sha256 de ESA pieza; si alguno dice CORREGIR, se corrige y se vuelve a firmar. **Sin `puerta_de_presentacion.py` en PASA no se le presenta nada al dueño ni se le dice «listo para revisar»** | Cada oficio; la corre la conversación principal | `herramientas/puerta_de_presentacion.py <proyecto> <pieza>` | `07_revision/revision_<versión>_<oficio>.md` y `firmas.md` |
| A10 | **Presentar la prueba completa al dueño** (en la conversación de producción) | Conversación principal | — | Su sí, o cambios por `cambios/` |
| A11 | **Entrega al publicador:** carpeta con el código de trazabilidad en el Drive, video, miniatura, subtítulos, `ficha.json` | `editor-de-video` | `entrega.py`, `ENTREGA_YOUTUBE.md` | `08_entrega/` y Drive |
| A11b | **Reporte de publicación** al dueño: qué se consideró, objetivos y cómo se conecta con el anterior y el siguiente. Va antes de pedirle el sí | Conversación principal | `plantillas/reporte_de_publicacion.md` | Reporte en `08_entrega/` (lo secreto, en el Drive) |
| A12 | **Publicación** en privado; pública solo con el sí del dueño a ese video. Un Short público no se reemplaza. La fecha sale del calendario de publicación, que también está en el Google Calendar del dueño con avisos | Publicador (Keter) | Studio | Enlace y hora en `registro_codigos.md` y en el reporte |
| A13 | **Cierre:** catálogo al día (qué se usó y qué se creó), registro de pistas, `consumo.md`, caso del canal | `jefe-de-produccion`, `supervisor-de-continuidad` | — | Biblioteca y registros al día |
| A14 | **Medición** a 48 horas, 7 y 28 días; vuelve al motor (paso 1) | `director-creativo`, Keter | Studio | Lectura en `estadisticas/datos/`; bitácora de parámetros |

## 3. Bifurcaciones en producción

| Si pasa esto… | Se hace esto | Quién decide |
|---|---|---|
| Una pieza generada sale mal | Se informa qué falló y cuánto cuesta rehacerla; **no se regenera** sin el sí del dueño para esa pieza. Antes se ve si se resuelve en edición o por código | Dueño |
| El código no alcanza la calidad de un plano | Se cotiza ese plano por la ruta generada y se le lleva | Dueño |
| El entorno o un efecto no está a tiempo | Se reutiliza uno de la biblioteca con ese tema y se anota como ajuste (regla de adaptación) | Equipo |
| La revisión encuentra un error de texto, de dato o de identidad | No sale. Se corrige y se vuelve a revisar | Supervisor |
| La revisión encuentra que falta un requisito del formato | No se presenta la prueba; se dice qué falta | Supervisor |
| El tema caduca durante la producción | Regla de adaptación: el hueco hereda otro tema del radar; lo construido queda en la biblioteca | Equipo; se informa al dueño |
| La máquina de producción no está disponible | Se produce por software en la nube (más lento) o se espera; se informa | Jefe de producción |
| El video publicado no se reparte | No se resube. Regla de adaptación (página arrancada, remake con su costo) | Dueño para el remake |
| Aparece un aviso o restricción de la plataforma | Se informa al dueño ese día; el siguiente video no depende de este | Dueño |

## 4. Lo que el equipo de producción devuelve siempre

El video en `06_final/`, la entrega, la revisión firmada, la rúbrica, los costos reales, las piezas nuevas en el
catálogo, el registro de pistas al día y, después, la lectura de Studio.
