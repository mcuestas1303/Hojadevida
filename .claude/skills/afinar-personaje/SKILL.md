---
name: afinar-personaje
description: Afina el prompt de un personaje vuelta a vuelta según lo que al dueño le gusta y no le gusta, con bitácora y versiones. Usar con «/afinar-personaje <nombre>», o cuando el dueño diga «afinemos a…», «crea un personaje nuevo», «me gusta / no me gusta esto del personaje», «mejora el prompt».
---

# Afinar un personaje

1. **Identifica el personaje** del argumento o de la conversación. Si es nuevo, pide en una sola pregunta la idea
   base (quién es y qué rol cumple) y un rasgo que quiera sí o sí.
2. **Delega en el agente `afinador-de-personajes`**. Pásale:
   - el nombre del personaje y la ruta de su bitácora (`creador-personajes/afinado/<personaje>.md`);
   - el comentario del dueño **textual**, sin resumirlo;
   - si hay una imagen nueva que el dueño vio, su ID de Higgsfield y su veredicto.
3. **Muestra al dueño** lo que entrega el agente: qué entendió, los cambios, el prompt y las preguntas.
4. **Si el dueño quiere verlo generado:**
   - cotiza primero con `get_cost` en Higgsfield (Nano Banana Pro, 9:16, salvo que el agente sugiera otro);
   - di el costo y genera **solo con su aprobación**, pasando como referencia el ID de la mejor versión si existe;
   - revisa el resultado (descárgalo y míralo) y cuéntale en una línea si cumple los rasgos fijados;
   - anota el ID del resultado en la bitácora (o pídeselo al agente en la siguiente vuelta).
5. **Si no quiere gastar todavía**, sugiere probar colores y peinado en la vista previa gratis
   (`creador-personajes/index.html`).
6. Cuando el dueño diga que una versión le encanta, márcala como **mejor versión** en la bitácora y en
   `creador-personajes/personajes/reserva.md`.
7. Guarda los cambios con un commit en español.
