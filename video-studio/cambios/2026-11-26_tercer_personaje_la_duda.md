# Solicitud de cambio — tercer personaje («la Duda») y peleas en Tin & Tan

- **Fecha:** 2026-11-26
- **Pedido del dueño, textual:** «la vez pasada te pasé unos videos de stickman; el concepto de ese formato es acción
  […] es entretenido ver a dos pelear […] Analízalo para empalmar esos formatos y ver si lo incorporamos en el 4.º
  video». Y hoy: «¿Por qué no modificamos a Tin y Tan?»; «¿Qué te parece crear un tercero y bajo concepto sería la duda?
  Considero que no hay necesidad de mencionar nombre en el video; solo es un personaje que aparece y desaparece y tanto
  Tin y Tan pelean con él»; «Sí, avanza así».
- **Estado:** PRESENTADA AL DUEÑO (aprobó la idea y avanzar; falta su sí a la ficha del personaje)

## Qué toca de lo ya definido

| Definición | Archivo | Cómo está hoy | Cómo quedaría | ¿Choca con algo? |
|---|---|---|---|---|
| Elenco | `personajes/REGISTRO.md` | Solo Tiky, Lumi, Spike, Tin y Tan | Se añade `@duda`, solo para el canal Tin & Tan | No, si el dueño aprueba la ficha. Hasta entonces figura en «Todavía no cargados» |
| Forma de explicar | `canales/nostalgia-tin-y-tan/PARAMETROS.md` | Tres datos, línea de tiempo, comparación, cuenta, ranking | Se añade «pelea contra la pregunta»: cada dato comprobado es un golpe | No: es un valor más del parámetro flexible. Se anota en la bitácora cuando se use |
| Recomendación del estudio | `estudios/2026-11-26_accion_stickman_y_tin_y_tan.md` | Vía A: dos «figurantes de tinta» pelean; Tin y Tan apadrinan | Vía nueva: Tin y Tan pelean juntos contra un rival abstracto | Sustituye la vía A. Se conserva todo lo demás: nivel 0–1, sin sangre roja ni armas de fuego, primer dato antes del segundo 5 |
| Tin y Tan no golpean ni reciben golpes | mismo estudio, 4.4 | Así lo proponía | Golpean y reciben empujones del rival; nunca entre ellos | Decisión del dueño |
| Dibujo de Tin y Tan | `herramientas/palitos.py` 1.4 | Torso vertical, pies clavados, 9 poses | Hacen falta: inclinar el cuerpo, agacharse, saltar y 7 poses de combate | La prueba lo resolvió sin tocar `palitos.py` (capa girada alrededor de los pies). Pasarlo a la herramienta es la versión 1.5 |
| Fichas de Tin y de Tan | `personajes/tin/ficha.md`, `personajes/tan/ficha.md` | Poses y expresiones de `palitos.py` | Se añaden las poses de combate como variación permitida | No cambia ningún rasgo |
| Firma del lápiz bumerán | `canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md` | El lápiz vuelve al inicio y se lanza al final | Igual. El lápiz nunca golpea al rival | No |
| Rol de Tan y de Tin | fichas | Tan pregunta; Tin responde con datos | Igual: la pregunta de Tan hace aparecer al rival; cada dato de Tin (o de Tan) lo encoge | No |

## Qué deja de valer

| Pieza ya hecha | ¿Sigue sirviendo? | Qué habría que rehacer | Créditos |
|---|---|---|---|
| Shorts 1, 2 y 3 | Sí, no se tocan | Nada | 0 |
| Prompt del short 4 (ranking de regresos de directores ejecutivos), en pausa | No para el short 4: seguía la línea del short 3 y el dato no lo respalda | Se escribe un prompt nuevo cuando haya tema y ficha aprobada | 0 (nunca se generó) |
| Sección 4.4 del estudio («figurantes de tinta») | No | Nada: queda como alternativa descartada | 0 |

**Costo total de aplicar el cambio:** 0 créditos. Todo es dibujo por código. La voz del short 4 se cotiza cuando haya guion.

## Opinión del equipo

| Quién | Opinión | Condiciones |
|---|---|---|
| Generador (coordina) | A favor. Mantiene a Tin y Tan del mismo lado, sirve para cualquier tema y el que recibe los golpes es una idea, no una figura humana | Que sea más grande que ellos; que no pierda siempre igual; que se borre y no muera |
| Prueba técnica (0 créditos) | Se puede dibujar por código: 6 s con aparición, zarpazo, esquiva, golpe, contraataque, patada y borrado. Informe: `canales/nostalgia-tin-y-tan/pruebas/2026-11-26_pelea_con_la_duda/informe.md` | La coreografía de la prueba tiene defectos que se corrigen en producción (ver informe) |
| Director de animación, director creativo, supervisor, `revisor-de-atencion` | **Sin consultar todavía** | Revisan la ficha después del sí del dueño |

## Dudas para aclarar con el dueño

- ¿Aprueba la ficha y la hoja del borrador (`personajes/duda/`)?
- Con una parte grande del público entre 13 y 17 años, ¿mantiene el nivel propuesto (golpe de dibujo, sin sangre roja ni armas)?

## Decisión del dueño

Idea aprobada el 2026-11-26 («Sí, avanza así»). Ficha del personaje: pendiente.
