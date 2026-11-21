# Tin

> Creado el 2026-11-20 para el canal de nostalgia de videos de palitos. Pedido del dueño, textual: *«crea los nuevos
> personajes seria tin & tan es para los videos que parecen palitos»*. **Versión 1 aprobada por el dueño el 2026-11-21** («si me gustan»).
> El diseño vive en código: `video-studio/herramientas/palitos.py` (`PERSONAJES["tin"]`). Las hojas de `referencias/`
> salen de ese archivo con `python3 video-studio/herramientas/palitos.py hojas <carpeta>`.

- **ID:** `@tin`
- **Nombre:** Tin
- **Rol / arquetipo:** el que hace la cuenta. Toma la pregunta nostálgica de Tan y la resuelve con números de verdad.
- **Edad aparente:** adulto (sin edad marcada)
- **Personalidad en una línea:** preciso y entusiasta con los números; se emociona con el resultado («eureka»).
- **Público / canal:** adultos, canal de nostalgia (inglés, EE. UU. mayores de 50 según la recomendación sin confirmar).
  **Nunca** en contenido infantil.
- **Voz:** por definir en la prueba de voces (`canales/nostalgia-tin-y-tan/voces.md`). Propuesta: masculina, clara,
  ritmo de explicación.

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
- Poses: `parado`, `saluda`, `senala`, `piensa`, `pregunta`, `explica`, `encoge`, `celebra`, `camina`.

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
