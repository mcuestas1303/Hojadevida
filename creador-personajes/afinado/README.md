# Bitácoras de afinado

Una bitácora por personaje (`<personaje>.md`). La lleva el agente `afinador-de-personajes`, y se usa con
`/afinar-personaje <nombre>`. Cada vez que el dueño dice qué le gusta o no, queda anotado aquí: así el prompt mejora
en cada vuelta y nunca se pierde lo que ya funcionaba.

## Estructura de una bitácora

```markdown
# <Nombre> · bitácora de afinado

## Idea del personaje
Una o dos líneas: quién es, qué rol cumple, qué tipo de humor o energía tiene.

## Fijado 🔒
Rasgos que le gustaron. Se copian palabra por palabra en cada versión.
- <rasgo en inglés, tal cual va en el prompt> — desde vN, «frase del dueño»

## En prueba 🧪
Lo que se está cambiando en la vuelta actual.

## No va 🚫
- <lo rechazado> — fecha, «frase del dueño»

## Mejor versión hasta ahora
vN · ID en Higgsfield: `…` · enlace

## Versiones
### vN · fecha
- **Comentario del dueño:** «…»
- **Cambios:** …
- **Modelo:** … · **Referencia:** … · **ID resultado:** … · **Veredicto:** gustó / no gustó / a medias
- **Prompt:**
  (bloque de código con el prompt completo)
```

## Revisión de atención (la agrega el agente revisor-de-atencion)

```markdown
### Revisión de atención · vN · fecha
- **Diseñado para:** nicho … · público … · por qué …
- **Coincide con el público buscado:** ✅ / ⚠️ / ❌ …
- **Notas (1-5):** freno del dedo · miniatura · rasgo icónico · novedad · expresividad · encaje · consistencia
- **Cambios sugeridos:** … (aceptado / rechazado por el dueño)
```

## Cómo se trabaja

1. Abres la vista previa gratis (`../index.html`) si quieres probar colores o peinados sin gastar.
2. Le dices al afinador qué te gusta y qué no, con tus palabras.
3. Te entrega el prompt nuevo (o 2-3 variantes para comparar) y actualiza la bitácora.
   El revisor de atención te dice para qué público está diseñado y qué cambiaría; tú decides qué aceptar.
4. Si te convence, se cotiza en Higgsfield y se genera solo con tu aprobación.
5. Miras el resultado y vuelves al paso 2. Cuando una versión te encanta, queda como «mejor versión» y su ID se usa
   como referencia para que el personaje salga igual en todos los videos.
