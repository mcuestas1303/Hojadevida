# Tan

> Creada el 2026-11-20 para el canal de nostalgia de videos de palitos. Pedido del dueño, textual: *«crea los nuevos
> personajes seria tin & tan es para los videos que parecen palitos»*. **Versión 1 aprobada por el dueño el 2026-11-21** («si me gustan»).
> El diseño vive en código: `video-studio/herramientas/palitos.py` (`PERSONAJES["tan"]`).

- **ID:** `@tan`
- **Nombre:** Tan
- **Rol / arquetipo:** la que recuerda. Abre cada video con la pregunta nostálgica («Remember…?») y reacciona al
  resultado.
- **Edad aparente:** adulta (sin edad marcada)
- **Personalidad en una línea:** cálida y curiosa; los recuerdos la ponen tierna y los resultados la sorprenden.
- **Público / canal:** adultos, canal de nostalgia. **Nunca** en contenido infantil.
- **Voz:** **Zelda** de Higgsfield (`seed_audio`, voz predefinida `b7aaea29-0c88-5925-90c0-8f66754cda53`), elegida por el dueño el 2026-11-21. Se acelera un poco en edición; velocidad por elegir (`canales/nostalgia-tin-y-tan/voces.md`).

## Bloque de identidad

```text
Tan, an original simple stick-figure character drawn in clean flat 2D vector style: a big perfectly round deep teal head with a thick dark brown-black outline, a round darker-teal hair bun on top tied with a mustard-yellow band, dot eyes with tiny eyelash flicks, short straight eyebrows, a small curved smile with soft pink cheeks, a chunky mustard-yellow knitted scarf wrapped around her neck with two ends hanging on one side, a thin straight dark stick body with rounded line ends, stick arms with small round dot hands, stick legs with small oval dark shoes. Cream paper background.
```

## Definición para generar

**Cómo se dibuja:** no se genera con IA. Se dibuja con `video-studio/herramientas/palitos.py` (versión `1.1`), con
`dibujar(lz, "tan", x, suelo, alto, pose, expresion, vista, mira, viento, objeto, espejo)` o, para primeros planos,
`cabeza(...)`. Los colores, medidas, poses y expresiones son los de ese archivo; si se cambian, cambia el personaje y
se registra en la bitácora (`creador-personajes/afinado/tin-y-tan.md`). Costo en créditos: 0.

**Proporciones medibles** (en radios de cabeza, R): cabeza 2 R de diámetro · cuello 0,18 R · torso 1,45 R · brazo
0,78 R + antebrazo 0,72 R · muslo 0,85 R + pierna 0,80 R · altura total ≈ 5,5 R (la cabeza es más de un tercio de la
altura) · grosor de línea del cuerpo 0,15 R · contorno de cabeza y accesorios 0,075 R. Tin y Tan miden lo mismo:
en un plano de los dos se dibujan con el mismo `alto`.

**Con qué hace cada gesto:** por defecto el brazo que gesticula queda a la **derecha del cuadro**. En los planos de los dos, Tan va a la izquierda del cuadro y **con `espejo=True`**: gesticula hacia la izquierda, del lado contrario a Tin, y las puntas de la bufanda pasan al otro lado para no taparle el brazo.

**Lista de comprobación de cada imagen:** cabeza redonda verde azulado `#2F7F7A` con contorno tinta · rodete arriba, verde azulado oscuro, con cinta mostaza · pestañas cortas en los ojos abiertos (no deben parecer cejas inclinadas) · bufanda mostaza enrollada al cuello con dos puntas · cuerpo de palitos de un solo grosor · manos de punto · dos zapatos ovalados · fondo papel `#F3E9D2` · ningún texto encima del personaje.

**Fallos conocidos del dibujo** (corregidos en el código; revisar que no vuelvan):

- Las pestañas largas e inclinadas se leían como cejas de enojo (corregido: cortas y casi horizontales).
- La bufanda se veía rígida, como dos reglas, y en perfil salía recta hacia atrás como un moño (corregido: rollo redondeado y puntas que caen).
- Con el brazo del lado de las puntas, la bufanda tapa el brazo: usar `espejo` para que el gesto quede del otro lado.

## Lo que nunca cambia

- Cabeza redonda **verde azulado** (`#2F7F7A`) con contorno tinta (`#2B2420`).
- **Rodete** verde azulado oscuro (`#23615D`) con cinta mostaza.
- **Bufanda mostaza** (`#E8B33B` / `#C9932A`) con dos puntas que cuelgan; en animación, las puntas se mueven con
  física de muelle (`viento`).
- Pestañas cortas en los ojos abiertos.
- Cuerpo de palitos de tinta, manos de punto, zapatos ovalados.

## Variaciones permitidas

- Expresiones y poses: las mismas de Tin (ver `palitos.py`).

## Prohibido

- Cambiar los colores o quitar el rodete o la bufanda.
- Parecerse a los muñecos de otros canales de palitos (en particular «Doodle Digest»).
- Aparecer en el canal infantil o con Tiky y Lumi.

## Referencias

| Archivo | Qué es |
|---|---|
| `referencias/principal_tin_y_tan.png` | Imagen principal de los dos |
| `referencias/vueltas.png` | Frente, perfil derecho e izquierdo, espalda |
| `referencias/expresiones.png` | Las 8 expresiones |
| `referencias/poses.png` | Las 9 poses |

## Prompts

Los prompts de video donde sale están en `prompts/`, por tipo. La lista completa está en `prompts/INDICE.md`.
