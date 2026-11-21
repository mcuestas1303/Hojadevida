# Prompt de video para redes — How many pencil turns to rewind a cassette?

> **ESTADO (2026-11-21): esta especificación es la del siguiente render (v3), no la del video v2 que ya existe.**
> El equipo de producción renderizó un v2 antes de recibir este prompt, con `codigo/render_v2.py` y `codigo/audio_v2.py`:
> dura 30,0 s, la voz entra en el segundo 1,0 y el contador de cinta termina en «421 ft». Lo producido está descrito en
> `07_revision/v2_vuelta_01/notas.md`; esa nota y el código son la especificación del v2. Este prompt resuelve justo lo que
> el v2 dejó pendiente (voz desde el fotograma 0, mitad de abajo de las tomas de la cinta y de la división, 27,5 s) y
> corrige el contador a «422 ft» (2.700 s × 1,875 in/s ÷ 12 = 421,875). Renderizarlo rehace una pieza terminada: necesita
> el sí del dueño.
> **Decisión del dueño (2026-11-21, textual: «no asi queda ya»): el v3 no se hace. El video definitivo es el v2.**
> Este prompt queda archivado como referencia para el siguiente short, no se renderiza.
>
> **VERSIÓN 2 (2026-11-21).** Aplica las tres mejoras de la «Revisión del director (2026-11-21)» de `direccion.md`, las
> correcciones de la «Revisión de producción» del supervisor de continuidad (`07_revision/revision_produccion.md`) y la
> solicitud de cambio **aprobada por el dueño**, `video-studio/cambios/2026-11-21_tin_y_tan_remate_y_unidades.md` («si, usa
> For one side y autorizo los 1,8 créditos»). **La voz se rehízo**: es `05_audio/dialogo_110_v2.mp3` (26,0 s,
> `05_audio/linea_de_tiempo_voz_v2.md`), con unidades de EE. UU. y remate «For one side.». El render existente
> `06_final/tin_y_tan_short01_v1.mp4` **corresponde a la v1** (30 s, centímetros, «For one song.») y no sirve para publicar.
>
> **Qué cambió frente a la v1:**
>
> 1. **Gancho nuevo.** El fotograma 0 es el carrete con el lápiz a pantalla completa, ya girando; la línea 1 de Tan empieza
>    en el fotograma 0 (ya no hay 1,0 s mudo); texto «pencil turns?» con «pencil» como palabra clave, que sale a los 0,9 s;
>    el cierre vuelve a ese mismo plano (último fotograma = primero) y el silencio de voz en el empalme del bucle baja de
>    3,1 s a 1,5 s. Todos los tiempos se recalcularon sobre la rejilla de 0,5 s con la voz v2: el video pasa de 30,0 s a
>    **27,5 s** (825 fotogramas) y de 16 tomas a 15.
> 2. **Valle (5,5 a 18,5 s) legible en teléfono a los 50+.** Gráficos 2 a 3 veces más grandes (cinta de 200 px, zigzag de
>    28 px, carrete del diagrama de 400 px, arco, segmento y cortes de 10 px), cifras al 7 % del alto, carretes girando en
>    la toma del C90, una reacción de Tan por dato (solo poses y expresiones de `palitos.py`) y la toma de «una vuelta,
>    4⅓ in» llenando el ancho útil. Personajes y gráficos usan el **tercio de abajo** del cuadro (pies a 86 %).
> 3. **Unidades de EE. UU. y remate corregido, con la voz nueva.** Cifra principal en pantalla: «1⅞ in/s», contador de cinta
>    en pies, «4⅓ in», «÷ 4⅓ in», «1,170 turns» y «for one side». Ya no hay cifras métricas en pantalla.
> 4. **Del supervisor:** otro encuadre y `borrón` en el corte hacia la toma del C90; carrete del plano «una vuelta» de 400 px
>    (≥ 300) con trazos de 10 px (≥ 8); el texto 1 sale a los 0,9 s; los golpes bajo la voz suben de −38 a unos −26 LUFS.
> 5. **Portada:** fotograma del carrete con el lápiz (§8).

<!--
Pieza dibujada con código (sin generador de video). Todas las tomas son método «edición»: se resuelven gratis
en el montaje. En lugar de «Prompt de keyframe» y «Prompt de video» cada toma lleva una «Especificación de dibujo».
Los tiempos son del video final. La voz v2 empieza en el fotograma 0 (segundo 0,0) y se coloca tal cual está en
05_audio/linea_de_tiempo_voz_v2.md.
-->

## 1. Ficha técnica

- **Proyecto:** 2026-11-21_tin_y_tan_casete_y_lapiz
- **Tipo:** short
- **Número:** 1
- **Serie:** ninguna
- **Objetivo de aprendizaje:** no aplica
- **Generador:** ninguno: imagen dibujada con código (palitos.py + gráficos propios), armada con ffmpeg
- **Aspecto:** 9:16
- **Duración total:** 27,5 s (la voz v2 de 26,0 s al 110 % va de 0,0 a 26,0 s, sin gancho mudo; cierre de 1,5 s sin voz, de 26,0 a 27,5 s)
- **Resolución de borrador:** 540x960 a 30 fps, prueba de 5,5 s con un fotograma por pulso (render propio)
- **Resolución final:** 1080x1920 a 30 fps, 825 fotogramas
- **Precio por segundo:** 0 (render propio; no hay servicio de pago)
- **Intentos estimados por toma:** 1
- **Versión:** 2 (la v1, de 30 s, está renderizada en `06_final/tin_y_tan_short01_v1.mp4`)

## 2. Elenco

| Personaje | Papel en este video | Vestuario | Referencia que se sube |
|---|---|---|---|
| @tan | Abre el video: recuerda el gesto de rebobinar con lápiz y hace la pregunta. Reacciona a cada dato (una reacción por dato) y a la cifra final. Lado izquierdo del cuadro con `espejo=True` (en el centro cuando está sola). | base de su ficha (rodete y bufanda mostaza) | personajes/tan/referencias/principal_tin_y_tan.png |
| @tin | Hace la cuenta con el lápiz amarillo y dice el resultado en minutos. Lado derecho del cuadro, sin espejo. | base de su ficha (gorra marrón, lentes, lápiz) | personajes/tin/referencias/principal_tin_y_tan.png |

No se sube nada a un generador: las referencias son las del diseño en código (`herramientas/palitos.py`, versión 1.1) y se usan solo para comparar el resultado.

Poses y expresiones usadas (todas existen en `POSES` y `EXPRESIONES` de `palitos.py` y en las hojas `referencias/poses.png` y `referencias/expresiones.png` de Tin y Tan; comprobado el 2026-11-21): poses `parado`, `saluda`, `senala`, `piensa`, `celebra`, `encoge`, `explica`, `pregunta`, `camina`; expresiones `feliz`, `nostalgia`, `curiosidad`, `pensando`, `concentrado`, `sorpresa`, `risa`, `eureka`. No se inventa ningún rasgo.

## 3. Idea en una línea

Tan recuerda el gesto de rebobinar un casete con un lápiz y Tin hace la cuenta real sobre papel crema, en pulgadas y pies, una cifra por plano que solo sube, hasta que 1.170 vueltas resultan ser casi 10 minutos de lápiz: lo que cuesta rebobinar una cara entera. Nostalgia que termina en sorpresa.

**Confirmado por el dueño el 2026-11-21:** short vertical 9:16; inglés para Estados Unidos; música hecha con código; rehacer la voz con «For one side» y unidades de EE. UU. (solicitud `video-studio/cambios/2026-11-21_tin_y_tan_remate_y_unidades.md`, 1,8 créditos autorizados).

**Decidido por el equipo el 2026-11-21** (el dueño delegó las decisiones técnicas; razones en `00_brief.md`):

1. Gancho A: «pencil turns?» sobre el carrete con el lápiz, sin adelantar la cifra. Gancho B, para probar en otra publicación: el mismo plano con «1,170 turns?».
2. Objetivo comercial: presencia y línea base de retención; sin llamado a la acción.
3. Público: Estados Unidos, de 45 a 70 años, con núcleo en mayores de 50.
4. Lo produce el Generador de prompts en su conversación, con los agentes del equipo de producción.
5. (v2) Todas las cifras en pantalla van en unidades de EE. UU. como cifra principal; no se muestran métricas en pantalla (la descripción de la publicación sí da los centímetros).

Fuente de la velocidad de la cinta: P. van der Lely y G. Missriegler, «Audio tape cassettes», Philips Technical Review, vol. 31, 1970, n.º 3, p. 77: «The design of the Compact Cassette is based on a tape speed of 4.76 cm/s» y «4.76 cm/s (1⅞ inch/s)». https://www.musicaememoria.com/docs/PTechReview-31-1970-077.pdf, **abierto y leído el 2026-11-21**.

## 4. Estilo global

```text
Flat 2D vector drawing on warm cream paper (#F3E9D2), 1970s palette (orange, brown, teal, mustard, tomato red), thick dark ink outlines (#2B2420), hand-made stick-figure look, no gradients, no soft shadows, no glow, no lens effects, crisp anti-aliased lines (supersampled), spring-based motion, static flat camera with small push-ins.
```

**Negativo global:**

```text
text inside the drawing other than the table in section 12, letters on the cassette label, brand names or logos, watermark, gradients, drop shadows, glow, lens flare, blue and orange cinematic grade, extra characters, extra fingers, characters other than Tin and Tan, uppercase centered titles, square placeholder glyphs, symbols that are not in the font
```

## 5. Escenarios

- **papel_crema:** fondo plano `#F3E9D2` en todos los planos, sin degradado ni textura. Cuando hay personajes, una línea de suelo `#E6D8B8` de 4 px a **86 % del alto (y = 1651 px)**, de 9,3 % a 90,7 % del ancho (v2: baja de 80 % a 86 % para usar el tercio de abajo; el límite de la zona segura es 87 %). Los planos solo de objeto no llevan suelo.
- **Lienzo y zonas (1080x1920):** zona segura de `formatos.md`: x de 100 a 980 px (9,3 % a 90,7 %), y de 250 a 1670 px (13 % a 87 %). Zona de texto fija: arriba a la izquierda, texto alineado a la izquierda en x = 10 % (108 px). Los personajes nunca pisan la zona de texto ni la de gráficos: **pies a 86 %**, `alto` = 34 % (653 px), por lo que la cabeza más alta llega a **52 %**. En un plano medio solo de Tin, `alto` = 44 % (845 px), pies a 86 %, cabeza a 42 %.
- **Zonas del valle (tomas 5 a 10, v2), pensadas para el teléfono:** cifra principal al 7 % del alto (134 px) con su caja de y = 13,2 % a 20,2 %; **zona de gráficos de 27 % a 51 %** (460 px de alto, de x = 100 a 980 px), centro vertical en 39 %. Los personajes quedan debajo (cabeza desde 52 %, pies a 86 %): la mitad de abajo del cuadro deja de estar vacía.
- **Lados:** Tan en x = 30 % (324 px) con `espejo=True`; Tin en x = 70 % (756 px) sin espejo; cada uno gesticula hacia afuera. Solos, en x = 50 %.
- **carrete a pantalla completa (tomas 1, 3 y 15, v2):** círculo tinta de 80 % del ancho (864 px de diámetro, de x = 108 a 972 px) centrado en (50 %, 54 %), con 6 dientes `#F3E9D2` y sin etiqueta a la vista; ocupa de 31,5 % a 76,5 % del alto y nunca toca la zona de texto (hasta 24,7 %). Gira a 720 grados por segundo desde el ángulo 0 (en el fotograma 0 y en el último, ángulo 0). El lápiz de gráfico mide 0,9 del diámetro (778 px), gira con él a 720 grados por segundo y su ángulo es de menos 35 grados en el fotograma 0 (ángulo = menos 35 más 720 por t: en 27,5 s son 19.800 grados, un múltiplo exacto de 360, por eso el último fotograma es igual al primero). Para que el fotograma 0 se vea «ya girando», el lápiz lleva una estela plana: dos copias del lápiz en `#E6D8B8` detrás, a menos 18 y menos 36 grados del ángulo actual, sin degradado ni desenfoque.
- **casete (gráfico propio, ancho W, alto 0,63 W, centro dado en cada toma):** cuerpo rectángulo redondeado (radio 0,06 W) relleno marrón `#7A4B2A` con contorno tinta de 0,012 W; etiqueta en x de menos 0,40 W a más 0,40 W y y de menos 0,29 W a menos 0,06 W, rellena `#FFF8EC`, con tres rayas dibujadas `#E6D8B8` y una franja tomate `#C8553D` de 0,03 W arriba, **sin letras**; ventana en x de menos 0,34 W a más 0,34 W y y de menos 0,02 W a más 0,20 W, rellena `#E6D8B8`; dos carretes de radio 0,075 W en x menos 0,17 W y más 0,17 W, y = más 0,09 W, rellenos tinta con 6 dientes `#F3E9D2`; dos tornillos de radio 0,018 W en las esquinas inferiores. Los carretes giran a 720 grados por segundo (2 vueltas por segundo, una vuelta por pulso) salvo que la toma diga otra cosa.
- **lápiz de gráfico:** el de `palitos.lapiz` (cuerpo mostaza `#E8B33B`, punta naranja claro, goma tomate), con largo 0,22 W cuando está en el carrete de un casete. Nunca sale de la ventana del casete (y de menos 0,02 W a más 0,20 W): así no toca la etiqueta.
- **reloj (cronómetro de 10 minutos):** círculo de diámetro 62 % del ancho (670 px), relleno `#FFF8EC`, contorno tinta de 0,012 D, 10 marcas mayores (una por minuto) y 50 menores, la marca de las 10 en tomate, **sin números**; botón rectangular arriba; centro en (50 %, 52 %) (v2: baja del 44 %), de 34,8 % a 69,2 % del alto.
- **Muelles (masa 1, rigidez, amortiguación), declarados por elemento:** `pop` 220 y 20 (entrada de textos y gráficos, escala de 0,85 a 1); `slide` 120 y 16 (personajes y gráficos que se desplazan); `sello` 320 y 26 (empujes de cámara). Contadores: ease-out cúbico sin muelle, para que el valor nunca pase de su final ni retroceda. Todo depende del número de fotograma (30 fps).
- **Transición `borrón`:** corte seco con desenfoque de movimiento horizontal de 18 px en los 2 últimos fotogramas de la toma que sale y en los 2 primeros de la que entra. Cero destellos.

## 6. Tomas

<!--
Todas las tomas son «edición»: dibujo por código. Tiempos al décimo de segundo, del video final (v2: 27,5 s).
Cada corte cae en un pulso de 0,5 s. Voz: línea y texto exactos de 05_audio/linea_de_tiempo_voz_v2.md, SIN desplazar
(la línea 1 empieza en el fotograma 0). Ninguna palabra de la voz se corta. Los cortes dentro de una línea (10,5; 17,0;
23,5 y 25,0) son estimados por sílabas y se afinan al oído antes del render.
-->

### Toma 1 — Gancho: carrete con lápiz a pantalla completa

- **Duración:** 1,5 s (de 0,0 a 1,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** el carrete con el lápiz a pantalla completa, de frente (el «carrete a pantalla completa» de la sección 5)
- **Cámara:** empuje de 100 % a 108 % centrado en el centro del carrete, muelle `sello`; en el fotograma 0 la escala es 100 %
- **Acción:** el lápiz ya está girando dentro del carrete en el fotograma 0 (con su estela) y da 3 vueltas, una por pulso.
- **Audio:** línea 1, Tan (primera parte): "Remember rewinding a cassette with a pencil?" Aquí suena «Remember rewinding a cassette» (de 0,0 a 1,5 s). Golpe 1 de la sección 13.
- **Referencia:** toma 4 de la v1 (subjetivo del carrete), subida al inicio
- **Transición de entrada:** ninguna (primer fotograma; es también el último del bucle). Salida: `borrón` hacia la toma 2.

**Especificación de dibujo:**

- Carrete y lápiz exactamente como los define la sección 5 («carrete a pantalla completa»), ángulos del fotograma 0: carrete 0 grados, lápiz menos 35 grados con estela. **Sin muelle de entrada ni escala 0,85 en el fotograma 0**: todo está ya en su estado pleno y en movimiento, porque este fotograma es la portada y el empalme del bucle.
- Texto «pencil turns?» (fila 1 de la tabla de la sección 12) ya entero y quieto en el fotograma 0 (sin `pop`; así el último fotograma puede ser igual). **Sale a los 0,9 s** (antes del corte de 1,5 s, para que no quede texto sobre el plano siguiente).
- Sin personajes ni suelo.

### Toma 2 — Tan recuerda

- **Duración:** 1,0 s (de 1,5 a 2,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio general de Tan sola, de frente, con el casete arriba
- **Cámara:** empuje lento de 100 % a 102 %
- **Acción:** Tan levanta la mano de la pregunta mientras acaba la frase; el lápiz sigue girando en el carrete del casete.
- **Audio:** línea 1, Tan (segunda parte): "Remember rewinding a cassette with a pencil?" Aquí suena «with a pencil?» (de 1,5 a 2,44 s).
- **Referencia:** toma 3 de la v1 (Tan recuerda)
- **Transición de entrada:** `borrón` desde la toma 1. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `pregunta`, expresión `nostalgia`, vista `frente`, `mira=1`, `espejo=True`, x = 50 %, pies a 86 %, `alto` 34 %, `viento` oscilando de menos 0,3 a 0,3 con muelle.
- Casete de W = 52 % (562 px), centro (50 %, 38 %), de 28,7 % a 47,3 % del alto, carretes a 720 grados por segundo; el lápiz de gráfico (largo 0,22 W) ya está dentro del carrete derecho, girando con él (continúa el lápiz de la toma 1).
- Sin texto (el «pencil turns?» ya salió en 0,9). Pestañas cortas visibles en los ojos de Tan; la bufanda no tapa el brazo.

### Toma 3 — Subjetivo del carrete

- **Duración:** 1,5 s (de 2,5 a 4,0)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** subjetivo: se mira dentro del carrete, de frente (el mismo carrete de la toma 1)
- **Cámara:** empuje de 100 % a 115 % hacia el centro del carrete, muelle `sello`
- **Acción:** el lápiz da 3 vueltas dentro del carrete, una por pulso.
- **Audio:** línea 2, Tan (primera mitad): "So, how many turns does it really take?" Aquí suena «So, how many turns» (de 2,67 a 4,0 s).
- **Referencia:** toma 4 de la v1
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 4.

**Especificación de dibujo:**

- Carrete y lápiz de la sección 5 (864 px), a 720 grados por segundo; en 2,5 el carrete lleva 1.800 grados (5 vueltas exactas, ángulo 0) y el lápiz sigue su ángulo continuo, con muelle `pop` en el arranque del empuje. A 115 % el carrete mide 994 px y queda dentro del cuadro; el texto es una capa aparte y no lo toca.
- Texto: «how many turns?» entra en 2,7 (sigue en la toma 4).

### Toma 4 — Tin entra

- **Duración:** 1,5 s (de 4,0 a 5,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el casete arriba
- **Cámara:** fija
- **Acción:** Tan se corre a la izquierda y Tin entra caminando por la derecha hasta su lugar.
- **Audio:** línea 2, Tan (segunda mitad): "So, how many turns does it really take?" Aquí suena «does it really take?» (hasta 5,5 s; la línea termina en 5,59 s).
- **Referencia:** toma 5 de la v1
- **Transición de entrada:** `borrón` desde la toma 3. Salida: `borrón` hacia la toma 5.

**Especificación de dibujo:**

- Tan: pose `pregunta`, expresión `curiosidad`, vista `frente`, `espejo=True`; se desliza de x = 50 % a x = 30 % entre 4,0 y 4,6 con muelle `slide`.
- Tin: entra de x = 118 % a x = 70 % entre 4,0 y 4,6 en pose `camina`, expresión `feliz`, vista `perfil`, `mira=-1`, sin espejo; en 4,6 cambia de golpe a pose `parado`, expresión `feliz`, vista `frente`, `objeto=True`. Revisar que la visera de perfil se lea como gorra.
- Casete de W = 52 % en (50 %, 38 %), carretes a 720 grados por segundo, sin lápiz (el lápiz pasa a la mano de Tin).
- Texto: «how many turns?» sigue hasta 5,4.

### Toma 5 — C90: 45 minutos por lado

- **Duración:** 3,0 s (de 5,5 a 8,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** **otro encuadre que la toma 4** (corrección del supervisor): plano más cerrado, con un casete grande que ocupa la zona de gráficos y los dos personajes en el tercio de abajo
- **Cámara:** empuje lento de 100 % a 104 %
- **Acción:** Tin explica con la mano abierta; Tan reacciona al dato encogiéndose de hombros; el casete gira con la etiqueta libre.
- **Audio:** línea 3, Tin: "A C ninety tape plays forty-five minutes per side." (de 5,82 a 8,33 s)
- **Referencia:** toma 6 de la v1
- **Transición de entrada:** **`borrón`** desde la toma 4 (en la v1 era corte seco y las dos poses cambiaban en el mismo fotograma: el borrón lo cubre). Salida: `borrón` hacia la toma 6.

**Especificación de dibujo:**

- Tan (reacción al dato «45 min»): pose `encoge`, expresión `curiosidad`, vista `frente`, x = 30 %, `espejo=True`, `viento` con muelle.
- Tin: pose `explica`, expresión `feliz`, vista `frente`, x = 70 %, sin espejo, `objeto=True`; el lápiz de su mano tiene movimiento secundario de más o menos 3 grados con muelle.
- Casete de W = 64 % (691 px, alto 435 px) en (50 %, 39 %), de 28,3 % a 49,7 % del alto (en la toma 4 era de 52 % y estaba en 38 %). **Carretes girando a 720 grados por segundo** (en la v1 estaban quietos). Etiqueta visible y libre: ningún objeto ni texto encima.
- Texto: «45 min/side» al 7 % de 5,9 a 8,4, caja de 13,2 % a 20,2 %.

### Toma 6 — La cinta pasa a 1⅞ in/s

- **Duración:** 2,0 s (de 8,5 a 10,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle (macro) de un tramo de cinta, de frente, con Tan debajo
- **Cámara:** fija
- **Acción:** la cinta corre de derecha a izquierda con una escala de marcas; Tan la señala.
- **Audio:** línea 4, Tin (primera parte): "At one and seven-eighths inches a second, that's about four hundred twenty feet of tape." Aquí suena «At one and seven-eighths inches a second,» (de 8,56 a unos 10,5 s).
- **Referencia:** toma 7 de la v1
- **Transición de entrada:** `borrón` desde la toma 5. Salida: `borrón` hacia la toma 7.

**Especificación de dibujo:**

- Tira de cinta marrón de 100 % de ancho (sale del cuadro por los dos lados) y **10,4 % de alto (200 px)**, centrada en y = 39 % (de 33,8 % a 44,2 %). La v1 tenía 77 px.
- Marcas de tinta cada 12 % del ancho (130 px, una unidad dibujada), de 8 px de grosor y 60 % del alto de la tira, que se desplazan a 4,76 marcas por segundo (617 px por segundo; es el dato). Velocidad constante porque la velocidad es el dato; el arranque usa muelle `pop` de 0,2 s.
- Un corchete tomate de una unidad (de una marca a la siguiente) sobre la tira, de **10 px de grosor**, fijo en x = 50 %, sin letras.
- Tan (reacción al dato «1⅞ in/s»): pose `senala`, expresión `concentrado`, vista `frente`, x = 50 %, `espejo=True`, pies a 86 %, `alto` 34 %.
- Texto: «1⅞ in/s» al 7 % de 8,7 a 10,4. Sin equivalente métrico.

### Toma 7 — La cinta se estira hasta 422 ft

- **Duración:** 2,0 s (de 10,5 a 12,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto del recorrido de la cinta, de frente, con Tan debajo
- **Cámara:** fija
- **Acción:** la cinta entra por el borde izquierdo y se estira en zigzag mientras el contador sube de 0 a 422 ft; Tan se asombra.
- **Audio:** línea 4, Tin (segunda parte): "At one and seven-eighths inches a second, that's about four hundred twenty feet of tape." Aquí suena «that's about four hundred twenty feet of tape.» (de unos 10,5 a 12,61 s).
- **Referencia:** toma 8 de la v1 (la cinta se estira con un contador)
- **Transición de entrada:** `borrón` desde la toma 6. Salida: corte seco.

**Especificación de dibujo:**

- Cinta marrón de **28 px de grosor** (la v1 tenía 11 px) que entra por el borde izquierdo (el casete queda fuera de cuadro) y recorre 5 filas horizontales en y = 30 %, 34,5 %, 39 %, 43,5 % y 48 % (separación de 86 px entre ejes), de x = 12 % a x = 88 %, con vueltas redondeadas de radio 43 px; el largo dibujado es proporcional al valor del contador. Todo cabe en la zona de gráficos (de 29,3 % a 48,7 %).
- Tan (reacción al dato «422 ft»): pose `pregunta`, expresión `sorpresa`, vista `frente`, x = 50 %, `espejo=True`, `viento` alto con muelle.
- Contador de 0 a 422 (enteros) con ease-out cúbico de 10,7 a 12,2, solo sube; al terminar se queda fijo. Texto «422 ft» al 7 % (fila de la tabla de la sección 12).
- Con suelo (hay personaje).

### Toma 8 — Una vuelta, 4⅓ in

- **Duración:** 3,0 s (de 12,5 a 15,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el diagrama del carrete llenando el ancho útil (plano héroe, cerca de la mitad del video)
- **Cámara:** fija
- **Acción:** el lápiz da una vuelta en el carrete, su arco se dibuja y se desenrolla en un segmento de 4⅓ in; Tan reacciona al dato.
- **Audio:** línea 5, Tin: "One pencil turn winds about four and a third inches." (de 12,84 a 15,45 s)
- **Referencia:** toma 9 de la v1
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 9.

**Especificación de dibujo:**

- Tan (reacción al dato «4⅓ in»): pose `saluda`, expresión `sorpresa`, vista `frente`, x = 30 %, `espejo=True`.
- Tin: pose `explica`, expresión `feliz`, vista `frente`, x = 70 %, sin espejo, `objeto=True`; el lápiz de su mano tiene movimiento secundario de más o menos 3 grados con muelle.
- Diagrama que **llena la zona de gráficos de borde a borde de la zona segura** (la v1 usaba 160 px y un tercio del ancho; el supervisor pide ≥ 300 px y trazos ≥ 8 px): carrete de **diámetro 400 px**, de x = 100 a 500 px, centro (300 px, 39 %), de 29,2 % a 49,0 % del alto, con el lápiz de gráfico girando una vuelta de 12,9 a 13,9 (ease in-out); el arco tomate de **10 px** sobre el contorno se dibuja con la vuelta hasta cerrar el círculo; de 13,9 a 14,7 el arco se desenrolla hacia la derecha en un segmento recto tomate de **10 px de grosor** y 480 px de largo (44,4 % del ancho) desde x = 500 px hasta x = 980 px, en y = 39 %. El segmento es el dato de 4⅓ in; sin letras en el dibujo.
- Texto: «4⅓ in» al 7 % de 12,9 a 15,4.

### Toma 9 — Tin piensa en los pies

- **Duración:** 1,5 s (de 15,5 a 17,0)
- **Personajes:** @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tin solo, de frente
- **Cámara:** empuje de 100 % a 106 %
- **Acción:** Tin se lleva la mano al mentón para dividir.
- **Audio:** línea 6, Tin (primera parte): "Four hundred twenty feet, divided by four and a third inches..." Aquí suena «Four hundred twenty feet,» (de 15,68 a unos 16,9 s).
- **Referencia:** toma 10 de la v1
- **Transición de entrada:** `borrón` desde la toma 8. Salida: `borrón` hacia la toma 10.

**Especificación de dibujo:**

- Tin: pose `piensa`, expresión `pensando`, vista `frente`, x = 50 %, pies a 86 %, `alto` 44 %, sin espejo, `objeto=False` (en `piensa` el lápiz cruza la cara).
- Sin gráficos. Esta toma repite el dato de la toma 7 (no hay dato nuevo, así que no lleva reacción de Tan: es el respiro de composición entre dos tomas de dos personajes). Texto «422 ft» al 7 % de 15,7 a 16,9 (ya completo, sin contador).

### Toma 10 — La cinta se divide en tramos de 4⅓ in

- **Duración:** 1,5 s (de 17,0 a 18,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle (macro) de una barra que se subdivide, de frente, con Tan debajo
- **Cámara:** fija
- **Acción:** la barra de 422 ft se parte en 2, 4, 8, 16, 32 y 64 tramos, una duplicación cada 0,2 s; Tan se encoge de hombros.
- **Audio:** línea 6, Tin (segunda parte): "Four hundred twenty feet, divided by four and a third inches..." Aquí suena «divided by four and a third inches...» (hasta 18,56 s).
- **Referencia:** toma 11 de la v1
- **Transición de entrada:** `borrón` desde la toma 9. Salida: corte seco.

**Especificación de dibujo:**

- Barra marrón de x = 10 % a x = 90 % (864 px) y **10,4 % de alto (200 px)**, centrada en y = 39 % (la v1 tenía 77 px).
- Cortes verticales tomate que aparecen con muelle `pop` en 6 pasos de 0,2 s de 17,1 a 18,1 (2, 4, 8, 16, 32 y 64 tramos): **10 px de grosor** hasta 16 tramos, 8 px con 32 y 8 px con 64 (el mínimo legible del supervisor; con 64 tramos de 13,5 px queda una cuadrícula densa, que es lo que debe verse); de 18,1 a 18,4 los 64 tramos se rellenan de marcas finas. No se dibujan 1.170 marcas individuales: la barra es un símbolo de la división.
- Tan (reacción al dato «÷ 4⅓ in»): pose `encoge`, expresión `pensando`, vista `frente`, x = 50 %, `espejo=True`, pies a 86 %, `alto` 34 %.
- Texto: «÷ 4⅓ in» al 7 % de 17,1 a 18,4.

### Toma 11 — 1.170 vueltas

- **Duración:** 3,5 s (de 18,5 a 22,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el contador arriba
- **Cámara:** empuje de 100 % a 102 %
- **Acción:** el contador sube de 0 a 1.170 mientras Tan celebra y Tin levanta el lápiz.
- **Audio:** línea 7, Tan: "About eleven hundred seventy turns!" (de 18,79 a 21,84 s)
- **Referencia:** toma 12 de la v1 (contador hasta 1.170 vueltas)
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 12.

**Especificación de dibujo:**

- Tan: pose `celebra`, expresión `sorpresa`, vista `frente`, x = 30 %, `espejo=True`, `viento` alto con muelle.
- Tin: pose `saluda`, expresión `eureka`, vista `frente`, x = 70 %, sin espejo, `objeto=True`.
- Contador en la zona de texto (y = 15 %), tamaño 7 %, de 0 a 1.170 con ease-out cúbico de 18,9 a 21,5; al llegar a 1.170 pasa de tinta y mostaza a tomate y hace un `pop` de escala solo del texto (el valor no se pasa). Texto «1,170 turns» (fila de la tabla).
- Sin gráfico en la zona de gráficos.

### Toma 12 — Reloj revelado

- **Duración:** 1,5 s (de 22,0 a 23,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** revelado desde desenfoque: cronómetro de frente, centrado
- **Cámara:** fija
- **Acción:** el cronómetro se aclara y el lápiz gira en su centro a 2 vueltas por segundo.
- **Audio:** línea 8, Tin (primera parte): "At two turns a second, almost ten minutes. For one side." Aquí suena «At two turns a second,» (de 22,07 a unos 23,5 s).
- **Referencia:** toma 13 de la v1 (el reloj)
- **Transición de entrada:** `borrón` desde la toma 11. Salida: corte seco.

**Especificación de dibujo:**

- Reloj de la sección 5 en (50 %, 52 %). Desenfoque gaussiano de radio 24 px en 22,0 que baja a 0 en 22,5 (ease-out cúbico).
- Lápiz de gráfico de 0,40 D girando en el centro a 720 grados por segundo desde 22,0 (3 vueltas hasta 23,5). Aguja de minutos tomate quieta en la marca 0.
- Sin personajes. Texto: «2 turns/s» de 22,1 a 23,4.

### Toma 13 — Casi 10 minutos

- **Duración:** 1,5 s (de 23,5 a 25,0)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle del mismo cronómetro, de frente
- **Cámara:** fija
- **Acción:** el lápiz se detiene y la aguja de minutos recorre el 97,5 % de la esfera (585 s de 600 s).
- **Audio:** línea 8, Tin (segunda parte): "At two turns a second, almost ten minutes. For one side." Aquí suena «almost ten minutes.» (de unos 23,5 a 25,0 s).
- **Referencia:** toma 14 de la v1
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Mismo reloj y posición de la toma 12. El lápiz se detiene en 23,6 con muelle `pop`.
- Aguja tomate de 0 a 351 grados (97,5 % de 360) de 23,6 a 24,6, ease-out cúbico sin pasarse, para en un punto justo antes de la marca tomate de las 10.
- Texto: «almost 10 min» de 23,6 a 24,9 (0,1 s antes del corte).

### Toma 14 — Remate: for one side

- **Duración:** 1,0 s (de 25,0 a 26,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con una nota musical arriba
- **Cámara:** fija
- **Acción:** los dos se ríen mientras la nota musical salta sobre el casete.
- **Audio:** línea 8, Tin (remate): "At two turns a second, almost ten minutes. For one side." Aquí suena «For one side.» (de unos 25,0 a 26,0 s).
- **Referencia:** toma 15 de la v1
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 15.

**Especificación de dibujo:**

- Tan: pose `encoge`, expresión `risa`, vista `frente`, x = 30 %, `espejo=True`.
- Tin: pose `celebra`, expresión `risa`, vista `frente`, x = 70 %, sin espejo, `objeto=True`.
- Casete de W = 40 % (432 px) en (50 %, 38 %), carretes a 720 grados por segundo; sobre su etiqueta no se pone nada. Una corchea mostaza de 8 % del ancho (86 px) con contorno tinta entra con `pop` a (50 %, 29 %), encima del casete y fuera de la etiqueta.
- Texto: «for one side» de 25,1 a 25,9 (clave: side). Dice lo mismo que la voz.

### Toma 15 — Cierre en bucle: vuelve el carrete con lápiz

- **Duración:** 1,5 s (de 26,0 a 27,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** el mismo carrete con lápiz a pantalla completa de la toma 1
- **Cámara:** retroceso de 108 % a 100 % centrado en el centro del carrete, muelle `sello`; en 27,5 la escala es 100 %
- **Acción:** el carrete gira con el lápiz, ya en el plano exacto del fotograma 0; el último fotograma es igual al primero.
- **Audio:** sin voz (la voz terminó en 26,0: 1,5 s de silencio de voz hasta el empalme; en el fotograma 0 la voz vuelve a entrar sin pausa). Golpes finales de la sección 13.
- **Referencia:** toma 1 de esta versión (cierre en bucle con el plano del inicio)
- **Transición de entrada:** `borrón` desde la toma 14. Salida: bucle al fotograma 0 de la toma 1.

**Especificación de dibujo:**

- Carrete y lápiz de la sección 5, a 720 grados por segundo desde el ángulo que corresponda a 26,0 (carrete: 18.720 grados = 0 grados; lápiz: menos 35 grados). En 27,5 los dos están en el ángulo del fotograma 0 (carrete 0 grados, lápiz menos 35 grados, escala 100 %, texto «pencil turns?» a escala 1): **el fotograma 825 (el último) es igual al fotograma 0**. El lápiz no sale del carrete.
- Texto «pencil turns?» (última fila de la tabla) entra con `pop` en 26,6 y se queda hasta 27,5; sigue sin corte en la toma 1 del bucle (de 0,0 a 0,9).

## 7. Audio

- **Voz:** rehecha y montada: `05_audio/dialogo_110_v2.mp3` (Tan con Zelda y Tin con Kevin, Higgsfield `seed_audio`; las líneas 4, 5, 6 y 8 de Tin se regeneraron en pulgadas y pies, con el remate «For one side.»; al 110 % con `atempo=1.10`, normalizada a −14 LUFS, 8 líneas, 26,0 s; ver `05_audio/linea_de_tiempo_voz_v2.md`). Costó 1,8 créditos, autorizados por el dueño en `video-studio/cambios/2026-11-21_tin_y_tan_remate_y_unidades.md`. Se coloca **sin retraso** (`adelay=0`): empieza en el fotograma 0 (la línea 1 de Tan arranca en 0,0) y termina en 26,0; hasta 27,5 hay 1,5 s sin voz, y al volver al fotograma 0 la voz entra otra vez sin silencio inicial: el silencio total del empalme del bucle es de 1,5 s (en la v1 eran 3,1 s). Los tiempos internos de la voz no se tocan y ninguna palabra se corta. Los cortes del diálogo se hicieron por pausas medidas, sin escuchar: se comprueba al oído antes de publicar. La voz v1 (`dialogo_110.mp3`) ya no se usa.
- **Música:** hecha con código y **confirmada por el dueño el 2026-11-21: entra al video.** Se genera con Python y numpy un patrón de 120 BPM (el pulso de la rejilla) a −24 LUFS, 10 dB por debajo de la voz, y se anota en `licencias.md`. Debe cubrir 27,5 s y cerrar su fase en el pulso para el bucle.
- **Efectos:** los de la sección 13, hechos con código (Python y numpy), sin material de terceros.

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → Toma 3 → Toma 4 → Toma 5 → Toma 6 → Toma 7 → Toma 8 → Toma 9 → Toma 10 → Toma 11 → Toma 12 → Toma 13 → Toma 14 → Toma 15 (y vuelve a la toma 1). Los carretes de las tomas 1 y 3 y el de la toma 15 son el mismo plano; la toma 1 es la antigua toma 4 de la v1, subida al inicio.
- **Transiciones:** corte seco; entre planos de objeto o de cámara distinta, el `borrón` de la sección 5 (incluido el corte hacia la toma 5, la del C90). Sin destellos, sin fundidos.
- **Texto en pantalla:** se dibuja en el mismo render, solo el de la tabla de la sección 12. El texto nunca contradice lo que se oye.
- **Portada:** el fotograma del carrete con el lápiz y «pencil turns?»: el fotograma de 0,5 s (fotograma 15) de la toma 1, o el fotograma 0 (son el mismo plano). Reemplaza la recomendación de la v1 (fotograma de 4,0 s).
- **Formato de salida:** 1080x1920, 30 fps, H.264, yuv420p, AAC a 48 kHz. Archivo `06_final/tin_y_tan_short01_v2.mp4` (no sobrescribe el v1).
- **Descripción de la publicación (en inglés, obligatoria):** debe decir que el diámetro promedio del rollo de cinta es de 1.4 in (3.5 cm), que crece mientras se rebobina, y que el resultado es una estimación. Texto propuesto: "Assumes an average spool diameter of 1.4 in (3.5 cm), which grows as the tape winds. Tape speed: 1⅞ in/s (4.76 cm/s), per Philips Technical Review, vol. 31, 1970. One 45-minute side." La fuente de la velocidad ya se abrió y se leyó el 2026-11-21 (ver §3).

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | 0 s (las 15 tomas son edición; 27,5 s se resuelven en edición) | 0 |
| Keyframes | 0 | 0 |
| Remates en resolución final | 0 | 0 |
| **Total estimado** | 0 créditos para el render v2 (la voz v2 costó 1,8 créditos, ya autorizados y aplicados; la voz v1 costó 3, en `costos.md`) | 0 |

## 10. Restricciones críticas

Van al inicio de cada prompt de video, antes de la descripción. Son las que no se negocian.

```text
CRITICAL: no text, captions, subtitles, logos or watermarks unless listed in section 12.
CRITICAL: the character looks identical in every shot (same design, colors, proportions).
CRITICAL: hard cuts only, no morphing between shots.
CRITICAL: every figure, name or claim on screen comes from the project's facts file, with source and date.
CRITICAL: counters only go up and never pass their final value; no text over a character; the pencil never covers the cassette label.
```

## 11. Gancho, ritmo y cierre

- **Regla formal de la pieza:** una sola cifra por plano, sobre el mismo papel crema, que solo sube; y todo corte cae en un pulso de 0,5 s, que es lo que dura una vuelta de lápiz.
- **Rejilla de tiempo:** pulso de 0,5 s (120 BPM, compás de 4 pulsos = 2,0 s); 55 pulsos = 27,5 s (13 compases y 3 pulsos). La voz entra en el pulso 0 (fotograma 0). Los 14 cortes caen en 1,5; 2,5; 4,0; 5,5; 8,5; 10,5; 12,5; 15,5; 17,0; 18,5; 22,0; 23,5; 25,0 y 26,0 (más el bucle en 27,5). Inicios de la voz v2: 0,00; 2,67; 5,82; 8,56; 12,84; 15,68; 18,79; 22,07. **Con la voz v2 ningún corte llega tarde**: todos caen antes o dentro de la pausa de la frase que corresponde (2,5 a 0,17 s antes de la línea 2; 8,5 a 0,06 s antes de la línea 4; 15,5 y 22,0 dentro de la pausa; 5,5, 12,5 y 18,5 de 0,29 a 0,34 s antes de la línea siguiente, porque la rejilla de 0,5 s no cae en esas pausas y se prefiere cortar antes que después). Los cortes dentro de una línea (10,5; 17,0; 23,5 y 25,0) son estimados por sílabas y se afinan al oído.
- **Gancho (0 a 2,5 s, v2):** el fotograma 0 es el carrete con el lápiz a pantalla completa, ya girando (con estela), con «pencil turns?» ya entero (clave: pencil, en mostaza), que sale a los 0,9 s, y la voz de Tan ya diciendo «Remember rewinding a cassette…» desde el fotograma 0. En 1,5 el `borrón` pasa a Tan y, en 2,5, de vuelta al carrete para «how many turns». Sin logo, sin título, sin segundo mudo. Gancho B para otra publicación (se renderiza gratis): el mismo plano con el texto «1,170 turns?».
- **Empieza en movimiento:** sí: sin intro ni logo; el lápiz gira dentro del carrete desde el fotograma 0 y es el primer fotograma, a tamaño completo.
- **Motivo visual que vuelve:** el carrete con el lápiz (tomas 1, 3 y 15, y el diagrama de la 8), el casete girando (tomas 2, 4, 5 y 14) y el lápiz amarillo de Tin; el lápiz que gira en el reloj (12). Todos giran a 2 vueltas por segundo, una por pulso. Se repiten con las mismas formas y colores.
- **Cierre:** el video vuelve al plano exacto del fotograma 0 (carrete a pantalla completa, lápiz a menos 35 grados, carrete en ángulo 0, escala 100 %, «pencil turns?» ya entero) y encadena en bucle con la toma 1: el último fotograma es el primero. Cierre de 1,5 s (de 26,0 a 27,5); la voz termina en 26,0; silencio de voz en el empalme: 1,5 s (≤ 2 s).
- **Llamado a la acción:** ninguno. Por qué: el objetivo comercial es presencia y línea base de retención; pedir suscripción antes de que el canal exista (lo crea el dueño) no se puede cumplir, y un llamado al final corta el bucle (reglas 3 y 4 del cap. 11: un solo llamado y que el final empalme con el inicio). Si el dueño fija otro objetivo, se añade uno solo en la descripción, no en el video.

Mapa de ritmo (los tiempos al décimo de segundo; cortes por segundo = cortes que caen dentro del tramo, sin contar el inicio):

| Tramo | Segundos | Pulso o intervalo | Cortes por segundo | Qué pasa (una acción) | Respiro |
|---|---|---|---|---|---|
| Gancho | 0,0–2,5 | 1,5 s y 1,0 s | 0,8 | el lápiz gira en el carrete, Tan recuerda el gesto | no |
| Pregunta | 2,5–5,5 | 1,5 s | 0,7 | subjetivo del carrete y entrada de Tin | no |
| Dato 1 | 5,5–8,5 | 3,0 s | 0,3 | un C90 dura 45 min por lado; Tan se encoge (encuadre nuevo) | sí |
| Cinta | 8,5–12,5 | 2,0 s | 0,5 | velocidad de la cinta en 1⅞ in/s y 422 ft; Tan señala y se asombra | no |
| Héroe | 12,5–15,5 | 3,0 s | 0,3 | una vuelta de lápiz son 4⅓ in | no |
| Cuenta | 15,5–18,5 | 1,5 s | 0,7 | dividir 422 ft entre 4⅓ in | no |
| Pico | 18,5–22,0 | 3,5 s | 0,3 | contador hasta 1.170 y celebración | no (pico de emoción) |
| Remate | 22,0–26,0 | 1,5 s y 1,0 s | 0,8 | el reloj, casi 10 minutos, una cara entera | no (acelera) |
| Cierre | 26,0–27,5 | 1,5 s | 0 | vuelve el carrete con lápiz del primer fotograma | sí |

Total: 14 cortes en 27,5 s. Es menos que los 52 cambios en 30 s del video viral que cita el cap. 11, porque este video lleva una voz continua de 26,0 s y cada cifra necesita su plano; la densidad extra va dentro de cada toma (subtítulo que cambia, contador que sube, reacción de Tan por dato, carretes a 2 vueltas por segundo). Decisión de la dirección de prompts, a revisar por el equipo si el dueño quiere más cortes.

Lo que sale se va antes de que entre lo siguiente: los textos salen de 0,1 a 0,2 s antes del corte siguiente (el texto 1, a los 0,9 s) y los gráficos con el borrón. El movimiento es mecánica: entradas con `pop` o `slide` (muelle), contadores con ease-out cúbico, giros a velocidad constante de 720 grados por segundo, sin interpolación lineal salvo la velocidad de la cinta de la toma 6.

Tipos de plano disponibles y dónde van: detalle o macro (tomas 6, 10 y 13), héroe abierto (tomas 4, 5, 8, 11 y 14; el héroe principal es la toma 8 en 12,5–15,5, a la mitad del video), subjetivo y carrete a pantalla completa (tomas 1, 3 y 15), revelado desde desenfoque (toma 12), objeto que salta sobre el mismo fondo (la corchea de la toma 14 y el lápiz de la 2). Transiciones siempre motivadas (borrón de movimiento). **No más de 3 destellos por segundo:** hay cero.

## 12. Texto en pantalla y sistema de diseño

- **Tipografías:** Inter Display Medium, licencia SIL Open Font License 1.1 (archivo `/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf`; en Windows, si no está, Segoe UI Semibold, que se anota en `licencias.md` antes de usarla). Siempre en minúsculas, alineadas a la izquierda, salvo los nombres propios, que llevan mayúscula. Excepción obligatoria (regla del dueño, 2026-11-21): los nombres propios llevan mayúscula inicial («Tin & Tan», «Tin», «Tan»).
- **Paleta:** papel `#F3E9D2` · papel_sombra `#E6D8B8` · tinta `#2B2420` · naranja `#E07A2E` · marrón `#7A4B2A` · verde azulado `#2F7F7A` · mostaza `#E8B33B` (palabra clave de los subtítulos) · tomate `#C8553D` (cifra final, goma, alertas) · rubor `#E9967A` · blanco `#FFF8EC`. Un color de acento por plano. La palabra clave en mostaza lleva un trazo de tinta de **0,06 em** (era 0,05 em en la v1: el director vio borrosa la palabra clave a ese tamaño) porque mostaza sobre crema no tiene contraste suficiente.
- **Referencias de movimiento:** `01_referencia/` está vacía (el video de la prueba está en la PC del dueño). Las referencias cargadas son `canales/nostalgia-tin-y-tan/DESIGN.md`, `herramientas/palitos.py` y las hojas de `personajes/tin/referencias/` y `personajes/tan/referencias/`; el movimiento lo definen los muelles de la sección 5.
- **Prohibido:**
  1. Mayúsculas centradas sobre degradado, tarjetas con degradado o cualquier fondo con degradado.
  2. Animaciones lineales de posición o escala (solo muelle o ease-out cúbico; la única velocidad constante es la de la cinta de la toma 6 y los giros de 720 grados por segundo).
  3. Los símbolos «≈» y «→» y cualquier glifo sin comprobar: en la prueba salieron como cuadrados. Se escribe «almost» y la flecha, si hiciera falta, se dibuja. **Excepción de la v2:** «⅞» y «⅓» solo en las filas «1⅞ in/s», «4⅓ in» y «÷ 4⅓ in» de la tabla de abajo, y solo después de comprobar que la fuente del render los trae (comprobado el 2026-11-21: `InterDisplay-Medium.otf` dibuja «⅞», «⅓» y «÷», igual que «?», «,», «.» y «/»). Si el render usa otra fuente y falta alguno: «1⅞» se escribe «1 7/8» y «4⅓» se escribe «4 1/3». «≈» sigue prohibido (no se usa).
  4. Un contador que retrocede o que se pasa de su valor final y vuelve (nada de rebote en el valor; el rebote solo es de escala).
  5. Texto encima de un personaje, del casete, del carrete o del reloj.
  6. El lápiz sobre la etiqueta del casete o letras en la etiqueta.
  7. Líneas sin suavizar: ningún dibujo fuera de un `Lienzo` con supermuestreo.
  8. Sombras suaves, resplandor, partículas, confeti y luz azul y naranja sin motivo (la estela del lápiz de la toma 1 es plana, sin degradado ni desenfoque).
  9. Subtítulos de más de 3 palabras, de más de una línea o fuera de la zona segura.
  10. Cualquier pose, expresión o vista que no esté en `palitos.py`, y cambiar los colores o accesorios de Tin y Tan.
  11. Cifras métricas en pantalla (cm, m): la voz v2 habla en pulgadas y pies y el texto tampoco las muestra.
- **Márgenes seguros y escenario:** zona segura de `formatos.md`: x de 9,3 % a 90,7 % y y de 13 % a 87 %. El contenido ocupa el centro de 880x1420 px (81 % del ancho y 74 % del alto). Texto en x = 10 %, y de 13,2 % a 24 %; personajes con pies a 86 % y cabeza desde 52 % (42 % en el plano medio de Tin); gráficos entre 27 % y 51 % cuando hay personajes en el valle.
- **Texto exacto:** todo texto en pantalla es el de la tabla de abajo, letra por letra. Los contadores muestran enteros entre 0 y su valor final.
- **No afirmar:** ninguna cifra fuera de las de la tabla «Datos del video» del brief, pasadas a unidades de EE. UU. y verificadas el 2026-11-21:
  - **45 min por lado.**
  - **1⅞ in/s:** 4,76 cm/s ÷ 2,54 = 1,874 in/s; 1⅞ = 1,875, la velocidad de diseño del Philips Technical Review (p. 77: «4.76 cm/s (1⅞ inch/s)»).
  - **422 ft:** una cara dura 45 min × 60 = 2.700 s; 2.700 s × 1,875 in/s = 5.062,5 in; ÷ 12 = **421,875 ft**, que redondea a **422** (con 4,76 cm/s: 128,52 m ÷ 0,3048 = 421,65 ft, también 422). La voz dice «about four hundred twenty feet» (redondeo hablado). **No se muestra «421 ft»** (sería truncar): si el equipo prefiere 421 es un cambio de un número en la especificación, pero 421 no es el redondeo correcto.
  - **4⅓ in:** 11 cm ÷ 2,54 = 4,331 in; 4⅓ = 4,333.
  - **1,170 vueltas:** 5.062,5 in ÷ 4,33 in = 1.169,2 (con 421,875 ft × 12 ÷ 4,3333 = 1.168,3); redondeado a la decena, 1.170, como dice la voz («about eleven hundred seventy»).
  - **2 vueltas por segundo y casi 10 minutos:** 1.170 ÷ 2 = 585 s = 9 min 45 s, «casi 10 minutos».
  - No mostrar «585 s» ni «9:45»; no decir que la velocidad es exacta en todos los casetes; no nombrar marcas de casete; no mostrar «C90» (lo dice la voz); no escribir «one song» ni «for one song» (el remate es «for one side»: casi 10 minutos son una cara entera, no una canción).
- **Subtítulos:** de 1 a 3 palabras, con la palabra clave en mostaza (con trazo de tinta); la cifra final «1,170» pasa a tomate. Las cifras del valle (filas 3 a 7) van al 7 % del alto.

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| pencil turns? (clave: pencil; ya entero en el fotograma 0, sin pop) | 0,0 | 0,9 | 10, 15 | 6 |
| how many turns? (clave: turns) | 2,7 | 5,4 | 10, 15 | 5 |
| 45 min/side (clave: 45) | 5,9 | 8,4 | 10, 13,2 | 7 |
| 1⅞ in/s (clave: 1⅞) | 8,7 | 10,4 | 10, 13,2 | 7 |
| 422 ft (contador de 0 a 422; clave: el número) | 10,7 | 12,4 | 10, 13,2 | 7 |
| 4⅓ in (clave: 4⅓) | 12,9 | 15,4 | 10, 13,2 | 7 |
| 422 ft (clave: 422) | 15,7 | 16,9 | 10, 13,2 | 7 |
| ÷ 4⅓ in (clave: 4⅓) | 17,1 | 18,4 | 10, 13,2 | 7 |
| 1,170 turns (contador de 0 a 1,170; al llegar, el número en tomate) | 18,8 | 21,9 | 10, 15 | 7 |
| 2 turns/s (clave: 2) | 22,1 | 23,4 | 10, 15 | 5 |
| almost 10 min (clave: 10) | 23,6 | 24,9 | 10, 15 | 5 |
| for one side (clave: side) | 25,1 | 25,9 | 10, 15 | 5 |
| pencil turns? (clave: pencil; entra con pop y sigue sin corte en la fila 1 del bucle) | 26,6 | 27,5 | 10, 15 | 6 |

En un short, todo texto queda dentro de la zona segura de `formatos.md`. Entrada de cada texto: `pop` con escala de 0,85 a 1 en 8 fotogramas; salida: subir 2 % con ease-in en 3 fotogramas (excepción: la fila 1 en el fotograma 0 está ya a escala 1, y la última fila queda a escala 1 en el último fotograma para que el bucle empalme). Antes de renderizar se comprueba que la fuente tiene los glifos «÷», «⅞», «⅓», «?», «,», «.» y «/»; si «÷» faltara, se escribe «/ 4⅓ in».

## 13. Sonido

Los golpes bajo la voz suben de −38 a unos **−26 LUFS** (constante `DB_BAJO_VOZ` de `codigo/audio.py`: de −24 a −12 dB respecto a la voz, que está a −14 LUFS), porque a −38 LUFS los clics de los cortes no se oían en un teléfono (revisión del supervisor). Se comprueba al oído.

| Golpe o efecto | Segundo | A qué corte va atado | Origen y licencia |
|---|---|---|---|
| Golpe seco de casete que cae (thunk grave de 80 ms), bajo la voz | 0,0 | arranque, toma 1 (es también el empalme del bucle: no se duplica) | código, propio (ver licencias.md) |
| 2 clics de matraca, uno por vuelta | 0,5 / 1,0 | vueltas del lápiz en la toma 1 | código, propio |
| Clic suave de borrón | 1,5 | corte de toma 1 a toma 2 | código, propio |
| Clic suave de borrón y plop del lápiz asentándose en el carrete | 2,5 | corte de toma 2 a toma 3 | código, propio |
| 3 clics de matraca, uno por vuelta | 2,5 / 3,0 / 3,5 | vueltas del lápiz en la toma 3 | código, propio |
| Clic suave de borrón y pasos de Tin | 4,0 | corte de toma 3 a toma 4 | código, propio |
| Clic suave de borrón | 5,5 | corte de toma 4 a toma 5 | código, propio |
| Clic suave de borrón | 8,5 | corte de toma 5 a toma 6 | código, propio |
| Zumbido de cinta bajo (hiss) mientras corre | 8,5–10,5 | toma 6 | código, propio |
| Clic suave de borrón | 10,5 | corte de toma 6 a toma 7 | código, propio |
| Tictac de contador que sube de tono | 10,7–12,2 | contador de la toma 7 | código, propio |
| Clic suave | 12,5 | corte de toma 7 a toma 8 | código, propio |
| Matraca de una vuelta y pitido del arco | 12,9–13,9 | vuelta del lápiz en la toma 8 | código, propio |
| Clic suave de borrón | 15,5 | corte de toma 8 a toma 9 | código, propio |
| Clic suave de borrón | 17,0 | corte de toma 9 a toma 10 | código, propio |
| 6 clics de corte, uno por duplicación | 17,1 / 17,3 / 17,5 / 17,7 / 17,9 / 18,1 | cortes de la barra en la toma 10 | código, propio |
| Clic suave | 18,5 | corte de toma 10 a toma 11 | código, propio |
| Tictac de contador que sube de tono | 18,9–21,5 | contador de la toma 11 | código, propio |
| Ding de campana al llegar a 1,170 | 21,5 | valor final de la toma 11 | código, propio |
| Clic suave de borrón | 22,0 | corte de toma 11 a toma 12 | código, propio |
| Matraca, una por vuelta | 22,0 / 22,5 / 23,0 | vueltas del lápiz en la toma 12 | código, propio |
| Clic suave | 23,5 | corte de toma 12 a toma 13 | código, propio |
| Campanilla corta al llegar la aguja | 24,6 | fin del recorrido en la toma 13 | código, propio |
| Clic suave | 25,0 | corte de toma 13 a toma 14 | código, propio |
| Nota corta de 3 tonos sobre la corchea | 25,1 | la corchea de la toma 14 | código, propio |
| Clic suave de borrón | 26,0 | corte de toma 14 a toma 15 | código, propio |
| Whoosh suave de retroceso de cámara | 26,0–27,3 | retroceso de la toma 15 | código, propio |
| Matraca, una por vuelta | 26,0 / 26,5 / 27,0 | vueltas del lápiz en la toma 15 | código, propio |
| Thunk grave idéntico al del segundo 0,0 (cierra el bucle; el del 0,0 lo continúa) | 27,5 | bucle: último golpe igual al primero | código, propio |

- **Música:** hecha con código, confirmada por el dueño el 2026-11-21; entra al video (ver sección 7). Voz a −14 LUFS, golpes sobre la voz a −26 LUFS (`DB_BAJO_VOZ` = −12 dB), golpes en el silencio final a −18 LUFS y música a −24 LUFS.
- **Voz:** sí. `05_audio/dialogo_110_v2.mp3`, sin retraso (empieza en el fotograma 0). El silencio de voz del empalme (26,0 a 27,5 s, 1,5 s) lo llenan solo los golpes, el whoosh y la música.

## 14. Motor y revisión

- **Cómo se hace:** gráficos por código (fotograma a fotograma): Python, Pillow y ffmpeg. Cada fotograma se dibuja en un `Lienzo(1080, 1920)` de `palitos.py`, que ya dibuja al triple de tamaño y reduce con LANCZOS (supermuestreo; el pedido era al menos el doble) para que las líneas queden suaves; los gráficos propios (casete, carrete a pantalla completa, reloj, cinta) se dibujan sobre el mismo lienzo con `lz.d` y las mismas escalas. Los empujes de cámara recortan el lienzo grande y reducen, así no se pierde nitidez. Todo depende del número de fotograma, no del reloj. Se guardan PNG numerados y ffmpeg los une con la voz y los efectos (`postpro.py mezclar` o ffmpeg directo). Personajes con `palitos.dibujar(lz, id, x, suelo, alto, pose, expresion, vista, mira, viento, objeto, espejo)`.
- **Quién renderiza y autorización (v2):** el render v2 lo hace el **equipo de producción** (no el Generador). El dueño **ya aprobó el cambio** que rehace la pieza: solicitud `video-studio/cambios/2026-11-21_tin_y_tan_remate_y_unidades.md` («si, usa For one side y autorizo los 1,8 créditos»; render v2 en código con los cambios técnicos de la revisión, 0 créditos). El render v1 (`06_final/tin_y_tan_short01_v1.mp4`) corresponde a la v1 y no se toca; la v2 sale como `tin_y_tan_short01_v2.mp4`. Antes de renderizar se actualiza `03_keyframes/definicion.md` con la entrada de «pieza por código» de `generacion.md` (datos con fuente, paleta con HEX, tipografía y licencia, texto exacto, 27,5 s a 30 fps, rejilla, prohibidos, motor y versión: palitos.py 1.1, Pillow 12.3.0, y costo 0).
- **Revisión:** prueba corta de 5,5 s (de 0,0 a 5,5: gancho, Tan, subjetivo y entrada de Tin), un fotograma por pulso, hoja de contacto y comprobación de medidas (zona segura, `alto` y x de cada personaje, pies a 86 %, etiqueta libre, el fotograma 0 con el lápiz ya girando y la palabra «pencil» legible). Después del render completo, `herramientas/revisar_fotogramas.py` sobre el video y `analizar_video.py <video> <carpeta> --cada 0.5`; se anota en `07_revision/`. Se comprueba al oído que cada corte de la voz cae donde dice la sección 6, que la voz arranca en el fotograma 0 y que los golpes se oyen bajo la voz.
- **Qué se marca:** imagen congelada, fotograma vacío (la mitad de abajo del cuadro no debe quedar vacía), texto cortado o tapado, texto que sigue sobre el plano siguiente, elemento fuera de cuadro, tirones, demasiado tiempo sin cambio de encuadre, contador que retrocede, glifos cuadrados (en particular «⅞» y «⅓»), lápiz sobre la etiqueta, texto sobre un personaje o sobre el carrete, el fotograma 825 (el último) distinto del 0, más de 3 destellos por segundo, la visera de Tin en perfil (toma 4), y en el teléfono: que cinta, zigzag, carrete del diagrama, arco y segmento se lean (medidas mínimas de la sección 6) y que cada dato lleve una reacción de Tan distinta. Nota para el validador: en las tomas con personajes (2, 4, 5, 6, 7, 8, 9, 10, 11 y 14), el bloque de identidad de la ficha no se pega en el prompt porque no hay generador de imágenes; el diseño oficial es el código de `palitos.py` y se comprueba con la lista de comprobación de cada ficha.
- **Vueltas:** las correcciones por código son gratis (salvo servicios de pago, que van a `costos.md`); **las de generador no se repiten sin autorización del dueño** (`generacion.md`). Aquí no hay generador, así que no hay vueltas de pago.
