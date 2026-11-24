# Tan

> Creada el 2026-11-20 para el canal de videos de palitos (hoy «Tin & Tan»; su definición vigente está en
> `video-studio/canales/nostalgia-tin-y-tan/PARAMETROS.md`, 2026-11-24). Pedido del dueño, textual: *«crea los nuevos
> personajes seria tin & tan es para los videos que parecen palitos»*. **Versión 1 aprobada por el dueño el 2026-11-21** («si me gustan»).
> El diseño vive en código: `video-studio/herramientas/palitos.py` (`PERSONAJES["tan"]`).

- **ID:** `@tan`
- **Nombre:** Tan
- **Rol / arquetipo:** la que pregunta (y se asombra). Abre cada video con la pregunta que el público ya se está
  haciendo y reacciona a la respuesta. (Hasta el 2026-11-24 se definía como «la que recuerda»: quedó sin efecto.)
- **Edad aparente:** adulta (sin edad marcada)
- **Personalidad en una línea:** cálida y curiosa; pregunta sin vueltas lo que todos quieren saber y los datos la asombran.
- **Público / canal:** adultos, sin edad fija (el que tenga la demanda del tema); canal «Tin & Tan». **Nunca** en contenido infantil.
- **Voz:** **Zelda** de Higgsfield (`seed_audio`, voz predefinida `b7aaea29-0c88-5925-90c0-8f66754cda53`), elegida por el dueño el 2026-11-21. En edición se acelera un 10 % sin cambiar el tono (`atempo=1.10`), velocidad elegida por el dueño el 2026-11-21.

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
- **Objetos de mano por video (añadido el 2026-11-21, pedido del dueño: «agrega variaciones al sheet si es necesario»):**
  cada prompt puede darle al personaje un objeto de utilería en la mano que gesticula, dibujado con el mismo trazo
  tinta y solo con colores de `PALETA`. El objeto se define en el prompt con medidas en R. Aprobados hasta hoy:
  `lapiz` (el de Tin), `control` (mando de videojuego genérico: cuerpo de 1,1 R × 0,6 R con dos empuñaduras
  redondeadas, relleno mostaza, dos palancas **a la misma altura** y cuatro botones de punto tinta; **sin logotipos ni la forma exacta de
  ningún mando comercial**) y `calendario` (hoja de 0,9 R × 1,0 R, cabecera tomate, número en tinta).
  **Dibujados en `palitos.py` 1.2** (2026-11-21; `objeto="control"`, `objeto="calendario"`). El calendario se dibujó con cabecera **marrón**, como pide el prompt del short 2 (aquí arriba dice tomate: falta que el dueño o el director creativo digan cuál vale).
- **Variaciones permitidas: inclinación de cabeza para mirar arriba o abajo, hasta ±25°** (añadido el 2026-11-23,
  `palitos.py` 1.3: `cabeza_giro` en `dibujar`). La cabeza gira como un bloque (cara, rodete) alrededor de la
  base del cuello; el cuerpo y la bufanda no. No cambia ningún rasgo; con 0 se dibuja igual que siempre. Primer uso: la portada
  del short 2 (los dos miran el mando, 25°).
- **Firma del canal (añadido el 2026-11-24, borrador):** Tan puede lanzar el lápiz de Tin en la firma del canal (lo
  lanza al final del video y lo atrapa al principio, con el brazo `bd` en `saluda`). Detalle en
  `video-studio/canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`.
- **Lo que no es variación:** el vestuario no cambia por la temática del video. Nada de disfraces de personajes de
  terceros ni ropa que imite la de un juego, película o marca.

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
