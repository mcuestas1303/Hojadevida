---
name: afinar-personaje
description: Afina el prompt de un personaje vuelta a vuelta según lo que al dueño le gusta y no le gusta, con bitácora y versiones. Usar con «/afinar-personaje <nombre>», o cuando el dueño diga «afinemos a…», «crea un personaje nuevo», «me gusta / no me gusta esto del personaje», «mejora el prompt».
---

# Afinar un personaje

> Sigue siempre `creador-personajes/PROCEDIMIENTO.md`: la escalera de costos (gratis → Z Image → imagen oficial →
> prueba de video corta → video final), cotizar antes de cada generación y el freno de pérdidas.

1. **Identifica el personaje** del argumento o de la conversación. Si es nuevo, pide en una sola pregunta la idea
   base (quién es y qué rol cumple) y un rasgo que quiera sí o sí.
2. **Delega en el agente `afinador-de-personajes`**. Pásale:
   - el nombre del personaje y la ruta de su bitácora (`creador-personajes/afinado/<personaje>.md`);
   - el comentario del dueño **textual**, sin resumirlo;
   - si hay una imagen nueva que el dueño vio, su ID de Higgsfield y su veredicto.
3. **Pasa el prompt nuevo al agente `revisor-de-atencion`** (con la bitácora y, si hay, el ID o enlace de la última
   imagen generada). Primero dice **para qué público y nicho está diseñado** el personaje y si coincide con el
   buscado; luego evalúa la atención en el feed y propone de 1 a 3 cambios.
4. **Muestra al dueño todo junto, en un solo mensaje:** lo que entendió el afinador, sus cambios y el prompt; después,
   el veredicto de público y las sugerencias del revisor, aunque contradigan su gusto.
   Pregunta qué sugerencias acepta. Las aceptadas vuelven al afinador para una versión nueva; las rechazadas quedan
   anotadas en «No va» con la frase del dueño.
5. **Si el dueño quiere verlo generado:**
   - usa el escalón que toque según `PROCEDIMIENTO.md`: para explorar, **Z Image** (0,15 por imagen); para la
     imagen oficial, Nano Banana Pro o Nano Banana 2;
   - cotiza primero con `get_cost` en Higgsfield;
   - di el costo y genera **solo con su aprobación**, pasando como referencia el ID de la mejor versión si existe;
   - revisa el resultado (descárgalo y míralo) y cuéntale en una línea si cumple los rasgos fijados;
   - anota el ID del resultado y **los créditos gastados** en la bitácora;
   - si dos intentos seguidos fallan, no generes un tercero: vuelve al afinador y al revisor (gratis).
6. **Si no quiere gastar todavía**, sugiere probar colores y peinado en la vista previa gratis
   (`creador-personajes/index.html`).
7. Cuando el dueño diga que una versión le encanta, márcala como **mejor versión** en la bitácora y en
   `creador-personajes/personajes/reserva.md`.
8. Después de generar, pide al revisor que mire **la imagen real**: su opinión sobre la imagen vale más que sobre el
   prompt.
9. Guarda los cambios con un commit en español.
