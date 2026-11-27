# La Duda (personaje sin nombre en pantalla)

> **Hoja v2 aprobada por el dueño el 2026-11-26** («sí apruebo la hoja»). Está en el elenco (`REGISTRO.md`). Vale la
> «Versión 2» de más abajo; la descripción de la versión 1 (solo la madeja) se conserva como historia. Idea del dueño, textual: «crear un tercero y bajo concepto sería la duda; considero que no hay necesidad de
> mencionar nombre en el video; solo es un personaje que aparece y desaparece y tanto Tin y Tan pelean con él».
> El dueño aprobó avanzar con la ficha, la solicitud de cambio y una prueba técnica («Sí, avanza así»). Solicitud:
> `video-studio/cambios/2026-11-26_tercer_personaje_la_duda.md`.

> **Versión 2 (2026-11-26), corrección del dueño, textual:** «No. Debe tener manos, pies y cuerpo; esa forma podría ser la
> cabeza; hacele un sheet de personaje». **Lo que sigue abajo describe la versión 1 (solo la madeja) y queda sin efecto en
> todo lo que contradiga esto:**
>
> - **Cuerpo:** de palitos, de tinta, con torso que se inclina, dos brazos con manos de punto y dos piernas con pies
>   ovalados. La madeja con el rizo de pregunta y los dos huecos de papel es **la cabeza**.
> - **Medidas** (R = radio de cabeza de Tin y Tan): cabeza 1,35 R de radio · torso 1,9 R · brazo 0,95 R + antebrazo 0,9 R ·
>   muslo 1,05 R + pierna 1,0 R · grosor 0,19 R. Mide ≈ 1,25 veces lo que Tin y Tan; crecida, hasta ≈ 1,5 veces su tamaño.
> - **Pelea con el cuerpo:** guardia, golpe, patada, recibe y caído. Ya no ataca con un mechón.
> - **Se borra empezando por la cabeza.**
> - **Hoja:** `referencias/hoja_v2_2026-11-26.png` (frente, perfil, espalda, guardia, crecida, golpe, patada, recibe, caído
>   y borrándose, con Tin a la misma escala). Código: `canales/nostalgia-tin-y-tan/pruebas/2026-11-26_pelea_con_la_duda/duda_v2.py`.
> - **Color (enmienda del 2026-11-27, pedido del dueño: «con el rival ocupa un color fucsia neon»):** en la hoja
>   Noche su tinta es fucsia neón `#FF2BD6`, con hollín `#0B0F1F` cuando queda chamuscado; nunca rojo. En las hojas claras
>   sigue en tinta oscura. Detalle: `cambios/2026-11-27_rival_fucsia_neon.md`. Antes decía: por ahora solo tinta. Queda abierto hasta saber qué pidió el dueño sobre los colores.
> - **Armas (dueño, 2026-11-26):** puede pelear con armas **dibujadas con tinta** (bastón, espada), igual que Tin y Tan.
>   Nunca armas de fuego ni sangre. Esto deja sin efecto «no lleva armas» y «ataca solo con el cuerpo» de más abajo.
> - Siguen igual: sin nombre en pantalla, sin voz, sin boca, no representa a nadie, no aparece en el canal infantil.

- **ID:** `@duda`
- **Nombre:** «la Duda» es el nombre de trabajo del equipo. **En el video no se dice ni se escribe**: ni en la voz, ni en
  los subtítulos, ni en el título, ni en la portada. Se entiende por el dibujo.
- **Rol / arquetipo:** el rival. Es la pregunta sin responder hecha cuerpo: aparece cuando Tan hace la pregunta, crece
  mientras nadie responde y se encoge con cada dato comprobado. Tin y Tan pelean contra ella, juntos.
- **Edad aparente:** ninguna. No es una persona ni un animal.
- **Personalidad en una línea:** terca y juguetona; estorba, empuja y se agranda, pero nunca es cruel ni da miedo.
- **Público / canal:** solo el canal «Tin & Tan». **Nunca** en contenido infantil ni con Tiky y Lumi.
- **Voz:** ninguna. No habla. Sus sonidos (rasgueo de lápiz al aparecer, goma al borrarse) los define el diseñador de
  sonido en cada proyecto.

## Bloque de identidad

```text
An original abstract creature made of a single tangled dark ink scribble, like a ball of pencil doodle drawn on cream paper: one continuous thick dark brown-black line looping over itself into a rough round mass, with two blank paper-colored oval holes where eyes would be (no pupils, no mouth, no nose, no face), and one curl of the same line rising from the top in the shape of the hook of a question mark, without the dot. No limbs; when it strikes, one strand of the scribble stretches out and ends in a round ink blob. Flat 2D, same line weight as a stick figure, no color other than the ink and the paper showing through.
```

## Definición para generar

**Cómo se dibuja:** no se genera con IA. Se dibuja con código, igual que Tin y Tan. Hoy vive en la prueba
`canales/nostalgia-tin-y-tan/pruebas/2026-11-26_pelea_con_la_duda/prueba_pelea.py` (función `duda`); si el dueño la
aprueba, pasa a `herramientas/palitos.py`. Costo en créditos: 0.

**Medidas** (R = radio de cabeza de Tin y Tan; ellos miden ≈ 5,5 R):

| Estado | Diámetro de la madeja | Cuándo |
|---|---|---|
| Entera | ≈ 5 R (tan ancha como ellos de altos; con el rizo los supera) | al aparecer |
| Crecida | hasta ≈ 7 R | mientras la pregunta sigue sin respuesta, o cuando gana un asalto |
| Golpeada | baja ≈ 1 R por cada dato | después de cada dato comprobado |
| Resto | un trazo suelto de ≈ 1,5 R | cuando un dato no está confirmado: no se borra del todo |

Grosor de línea: 0,085 del radio de la madeja (parecido al del cuerpo de Tin y Tan). Ojos: dos óvalos del color del papel
con contorno de tinta, sin pupilas. Rizo: la curva de un signo de pregunta, **sin el punto**.

**Cómo se mueve:** el trazo «hierve» (cambia un poco cada 3 fotogramas). Aparece dibujándose de un solo trazo y se va
borrándose en sentido contrario. Al recibir un dato se achata y se encoge. Ataca con un mechón que se estira; nunca con
objetos.

**Lista de comprobación de cada imagen:** una sola línea de tinta `#2B2420` · dos huecos de papel, sin pupilas ni boca ·
rizo de pregunta sin punto · sin brazos ni piernas · sin color propio (el acento del video no la pinta) · sin rótulo ni
nombre · más ancha que la cabeza de Tin y Tan en todos los estados menos el resto.

## Lo que nunca cambia

- Hecha de tinta sobre papel, de una sola línea; sin cara humana, sin boca, sin voz.
- No representa a ninguna persona, marca, grupo ni creencia. Es la pregunta del video, nada más.
- No sangra, no muere y no lleva armas. Se borra, y por eso puede volver.
- Tin y Tan la enfrentan juntos; nunca pelean entre sí.
- Los golpes son de dibujo: estrella de impacto, gotas de tinta breves y pausa de impacto. Sin sangre roja ni armas de fuego.
- El lápiz bumerán no la golpea: el lápiz es herramienta y firma, no arma.

## Variaciones permitidas

- **Forma según el tema:** la madeja puede tomar la silueta de lo que se pregunta (dos madejas cuando el tema es una
  comparación entre dos cosas). Siempre con el rizo y los dos huecos.
- **Desenlace:** no pierde siempre igual. Puede ganar un asalto, puede quedar un resto y puede partirse en dos. El
  desenlace lo decide el dato del video (política de YouTube sobre contenido repetitivo:
  https://support.google.com/youtube/answer/1311392?hl=en).
- **Tamaño:** entre el resto y ≈ 7 R.

## Prohibido

- Decir o escribir su nombre en el video, el título, la portada o los subtítulos.
- Darle cara humana, boca, dientes, garras, cuernos u ojos con pupila; hacerla de miedo.
- Pintarla de rojo o de cualquier color; sangre, heridas, armas.
- Usarla para representar a una persona real, una marca o un grupo de personas.
- Que Tin y Tan se ensañen: la pelea termina cuando se borra.
- Aparecer en el canal infantil.

## Referencias

| Archivo | Qué es |
|---|---|
| `referencias/hoja_borrador_2026-11-26.png` | Hoja del borrador: entera, golpeada, zarpazo, borrándose y resto, con Tin para la escala |

## Pendiente antes de pasar al elenco

1. El sí del dueño a esta ficha y a la hoja.
2. Revisión del `revisor-de-atencion` y del director de animación.
3. Pasar la función a `palitos.py` y sacar la hoja definitiva; fila en `REGISTRO.md`; carpeta en Drive.
