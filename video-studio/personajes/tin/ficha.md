# Tin

> Creado el 2026-11-20 para el canal de videos de palitos (hoy «Tin & Tan»; su definición vigente está en
> `video-studio/canales/nostalgia-tin-y-tan/PARAMETROS.md`, 2026-11-24). Pedido del dueño, textual: *«crea los nuevos
> personajes seria tin & tan es para los videos que parecen palitos»*. **Versión 1 aprobada por el dueño el 2026-11-21** («si me gustan»).
> El diseño vive en código: `video-studio/herramientas/palitos.py` (`PERSONAJES["tin"]`). Las hojas de `referencias/`
> salen de ese archivo con `python3 video-studio/herramientas/palitos.py hojas <carpeta>`.

- **ID:** `@tin`
- **Nombre:** Tin
- **Rol / arquetipo:** el que responde con datos. Toma la pregunta de Tan y la contesta con hechos
  comprobados, cada uno con su fuente; hace la cuenta cuando la cuenta es lo que mejor responde.
- **Edad aparente:** adulto (sin edad marcada)
- **Personalidad en una línea:** preciso y entusiasta con los datos; se emociona cuando la respuesta cierra («eureka»).
- **Público / canal:** adultos, sin edad fija (el que tenga la demanda del tema); canal «Tin & Tan» (inglés, EE. UU.).
  **Nunca** en contenido infantil.
- **Voz:** **Kevin** de Higgsfield (`seed_audio`, voz predefinida `f1373f24-3b96-433f-9a68-e595810ef608`), elegida por el dueño el 2026-11-21 («tiene una energía más encendida al hablar»). En edición se acelera un 10 % sin cambiar el tono (`atempo=1.10`), velocidad elegida por el dueño el 2026-11-21.

## Bloque de identidad

Para cualquier generador de imágenes, si alguna vez hace falta. El dibujo oficial es el de código.

```text
Tin, an original simple stick-figure character drawn in clean flat 2D vector style: a big perfectly round warm orange head with a thick dark brown-black outline, a rounded brown cap with two light seams, a small button on top and a wide light-brown brim, small round dark-rimmed glasses with tiny white glints, dot eyes, short straight eyebrows, a small curved smile with soft pink cheeks, a thin straight dark stick body with rounded line ends, stick arms with small round dot hands, stick legs with small oval dark shoes, holding a short yellow pencil with a red eraser and an orange tip. Cream paper background.
```

## Definición para generar

**Cómo se dibuja:** no se genera con IA. Se dibuja con `video-studio/herramientas/palitos.py` (versión `1.1`), con
`dibujar(lz, "tin", x, suelo, alto, pose, expresion, vista, mira, viento, objeto, espejo)` o, para primeros planos,
`cabeza(...)`. Los colores, medidas, poses y expresiones son los de ese archivo; si se cambian, cambia el personaje y
se registra en la bitácora (`creador-personajes/afinado/tin-y-tan.md`). Costo en créditos: 0.

**Proporciones medibles** (en radios de cabeza, R): cabeza 2 R de diámetro · cuello 0,18 R · torso 1,45 R · brazo
0,78 R + antebrazo 0,72 R · muslo 0,85 R + pierna 0,80 R · altura total ≈ 5,5 R (la cabeza es más de un tercio de la
altura) · grosor de línea del cuerpo 0,15 R · contorno de cabeza y accesorios 0,075 R. Tin y Tan miden lo mismo:
en un plano de los dos se dibujan con el mismo `alto`.

**Con qué hace cada gesto:** por defecto el brazo que gesticula (saluda, señala, pregunta, piensa) queda a la **derecha del cuadro**, y en esa mano lleva el lápiz. En los planos de los dos, Tin va a la derecha del cuadro y **sin** espejo, así gesticula del lado contrario a Tan.

**Lista de comprobación de cada imagen:** cabeza redonda naranja `#E07A2E` con contorno tinta `#2B2420` · gorra marrón con visera clara, botón y dos costuras · lentes redondos con brillo · cejas visibles bajo la visera · ojos de punto · mejillas rosadas cuando la expresión las lleva · cuerpo de palitos de un solo grosor · manos de punto · dos zapatos ovalados · lápiz amarillo con goma roja y punta naranja (salvo `objeto=False`) · fondo papel `#F3E9D2` · ningún texto encima del personaje.

**Fallos conocidos del dibujo** (corregidos en el código; revisar que no vuelvan):

- La visera tapaba las cejas (v1.0, corregido subiendo la gorra).
- En «saluda» y «celebra» la mano quedaba escondida detrás de la cabeza (corregido en los ángulos de la pose).
- En «piensa» la mano no llegaba al mentón (corregido); el lápiz cruza la cara en esa pose: si molesta, `objeto=False`.
- En perfil, la visera se ve como una barra fina: revisar que se lea como gorra.

## Lo que nunca cambia

- Cabeza redonda **naranja** (`#E07A2E`) con contorno tinta (`#2B2420`).
- **Gorra marrón** (`#7A4B2A`) con visera clara (`#9C6A44`), botón y dos costuras.
- **Lentes redondos** con brillo blanco.
- **Lápiz amarillo** en la mano (motivo del canal: el lápiz de rebobinar casetes).
- Cuerpo de palitos de tinta, manos de punto, zapatos ovalados.

## Variaciones permitidas

- Sin lápiz cuando la acción necesita las dos manos (`objeto=False`).
- Expresiones: `feliz`, `nostalgia`, `curiosidad`, `pensando`, `concentrado`, `sorpresa`, `risa`, `eureka`.
  (`nostalgia` es el nombre técnico de una cara en `palitos.py`: ojos cerrados suaves y boca suave. No es un rasgo
  del personaje ni un criterio del canal; se usa como cara de calma o ternura.)
- Poses: `parado`, `saluda`, `senala`, `piensa`, `pregunta`, `explica`, `encoge`, `celebra`, `camina`.
- **Objetos de mano por video (añadido el 2026-11-21, pedido del dueño: «agrega variaciones al sheet si es necesario»):**
  cada prompt puede darle al personaje un objeto de utilería en la mano que gesticula, dibujado con el mismo trazo
  tinta y solo con colores de `PALETA`. El objeto se define en el prompt con medidas en R. Aprobados hasta hoy:
  `lapiz` (el de Tin), `control` (mando de videojuego genérico: cuerpo de 1,1 R × 0,6 R con dos empuñaduras
  redondeadas, relleno mostaza, dos palancas **a la misma altura** y cuatro botones de punto tinta; **sin logotipos ni la forma exacta de
  ningún mando comercial**) y `calendario` (hoja de 0,9 R × 1,0 R, cabecera tomate, número en tinta).
  **Dibujados en `palitos.py` 1.2** (2026-11-21; `objeto="control"`, `objeto="calendario"`). El calendario se dibujó con cabecera **marrón**, como pide el prompt del short 2 (aquí arriba dice tomate: falta que el dueño o el director creativo digan cuál vale).
- **Variaciones permitidas: inclinación de cabeza para mirar arriba o abajo, hasta ±25°** (añadido el 2026-11-23,
  `palitos.py` 1.3: `cabeza_giro` en `dibujar`). La cabeza gira como un bloque (cara, gorra y lentes) alrededor de la
  base del cuello; el cuerpo no. No cambia ningún rasgo; con 0 se dibuja igual que siempre. Primer uso: la portada
  del short 2 (los dos miran el mando, 25°).
- **Lo que no es variación:** el vestuario no cambia por la temática del video. Nada de disfraces de personajes de
  terceros ni ropa que imite la de un juego, película o marca.

## Prohibido

- Cambiar los colores o quitar la gorra o los lentes.
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
