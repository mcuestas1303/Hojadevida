<!-- Copia archivada. Se edita en proyectos/2026-11-21_tin_y_tan_casete_y_lapiz/02_prompt/prompt.md y se vuelve a archivar. -->
# Prompt de video para redes — How many pencil turns to rewind a cassette?

> **VERSIÓN 2 (2026-11-21).** Aplica las tres mejoras de la «Revisión del director (2026-11-21)» de `direccion.md`, en su
> **variante gratis** (cero créditos; la voz ya grabada no se rehace ni se regenera). El render existente
> `06_final/tin_y_tan_short01_v1.mp4` **corresponde a la v1**; esta versión no lo reemplaza hasta que se renderice la v2
> (ver §14: rehacer una pieza terminada necesita el sí del dueño).
>
> **Qué cambió frente a la v1:**
>
> 1. **Gancho nuevo.** El fotograma 0 es el carrete con el lápiz a pantalla completa, ya girando; la línea 1 de Tan empieza
>    en el fotograma 0 (ya no hay 1,0 s mudo); texto «pencil turns?» con «pencil» como palabra clave; el cierre vuelve a ese
>    mismo plano (último fotograma = primero) y el silencio de voz en el empalme del bucle baja de 3,1 s a 1,6 s. Todos los
>    tiempos se recalcularon sobre la rejilla de 0,5 s: el video pasa de 30,0 s a **28,5 s** (855 fotogramas) y de 16 tomas a 15.
> 2. **Valle de 6,5 a 20,5 s (ahora 5,5 a 19,5 s) legible en teléfono a los 50+.** Gráficos 2 a 3 veces más grandes (cinta de
>    200 px, zigzag de 24 px, carrete del diagrama de 400 px, arco y segmento de 10 px), cifras al 7 % del alto, carretes
>    girando en la toma del C90, una reacción de Tan por dato (solo poses y expresiones de `palitos.py`) y la toma de «una
>    vuelta, 11 cm» llenando el ancho útil.
> 3. **Remate y unidades de EE. UU., gratis.** La voz sigue diciendo «For one song.»; el texto del remate pasa a «replay song 1» (así la cifra
>    es cierta: estás al final de la cara y rebobinas toda la cara para volver a la primera canción). Las cifras métricas que
>    dice la voz siguen como cifra principal y llevan debajo su equivalente de EE. UU.
> 4. **Portada:** fotograma del carrete con el lápiz (§8).

<!--
Pieza dibujada con código (sin generador de video). Todas las tomas son método «edición»: se resuelven gratis
en el montaje. En lugar de «Prompt de keyframe» y «Prompt de video» cada toma lleva una «Especificación de dibujo».
Los tiempos son del video final. La voz empieza en el fotograma 0 (segundo 0,0) y se coloca tal cual está en
05_audio/linea_de_tiempo_voz.md.
-->

## 1. Ficha técnica

- **Proyecto:** 2026-11-21_tin_y_tan_casete_y_lapiz
- **Tipo:** short
- **Número:** 1
- **Serie:** ninguna
- **Objetivo de aprendizaje:** no aplica
- **Generador:** ninguno: imagen dibujada con código (palitos.py + gráficos propios), armada con ffmpeg
- **Aspecto:** 9:16
- **Duración total:** 28,5 s (la voz de 26,9 s al 110 % va de 0,0 a 26,9 s, sin gancho mudo; cierre de 1,6 s sin voz, de 26,9 a 28,5 s)
- **Resolución de borrador:** 540x960 a 30 fps, prueba de 5,5 s con un fotograma por pulso (render propio)
- **Resolución final:** 1080x1920 a 30 fps, 855 fotogramas
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

Tan recuerda el gesto de rebobinar un casete con un lápiz y Tin hace la cuenta real sobre papel crema, una cifra por plano que solo sube, hasta que 1.170 vueltas resultan ser casi 10 minutos de lápiz: lo que cuesta rebobinar una cara entera para volver a la primera canción. Nostalgia que termina en sorpresa.

**Confirmado por el dueño el 2026-11-21:** short vertical 9:16; inglés para Estados Unidos; música hecha con código.

**Decidido por el equipo el 2026-11-21** (el dueño delegó las decisiones técnicas; razones en `00_brief.md`):

1. Gancho A: «pencil turns?» sobre el carrete con el lápiz, sin adelantar la cifra. Gancho B, para probar en otra publicación: el mismo plano con «1,170 turns?».
2. Objetivo comercial: presencia y línea base de retención; sin llamado a la acción.
3. Público: Estados Unidos, de 45 a 70 años, con núcleo en mayores de 50.
4. Lo produce el Generador de prompts en su conversación, con los agentes del equipo de producción.
5. (v2) Variante gratis de la mejora 3: la voz no se rehace; el remate se corrige en pantalla y las cifras llevan su equivalente de EE. UU.

Fuente de la velocidad de la cinta: Philips Technical Review, vol. 31, 1970 («The design of the Compact Cassette is based on a tape speed of 4.76 cm/s»), https://www.musicaememoria.com/docs/PTechReview-31-1970-077.pdf, visto en resumen de buscador el 2026-11-21; equivale a 1⅞ pulgadas por segundo. Conviene abrir el documento antes de publicar.

## 4. Estilo global

```text
Flat 2D vector drawing on warm cream paper (#F3E9D2), 1970s palette (orange, brown, teal, mustard, tomato red), thick dark ink outlines (#2B2420), hand-made stick-figure look, no gradients, no soft shadows, no glow, no lens effects, crisp anti-aliased lines (supersampled), spring-based motion, static flat camera with small push-ins.
```

**Negativo global:**

```text
text inside the drawing other than the table in section 12, letters on the cassette label, brand names or logos, watermark, gradients, drop shadows, glow, lens flare, blue and orange cinematic grade, extra characters, extra fingers, characters other than Tin and Tan, uppercase centered titles, square placeholder glyphs, symbols that are not in the font
```

## 5. Escenarios

- **papel_crema:** fondo plano `#F3E9D2` en todos los planos, sin degradado ni textura. Cuando hay personajes, una línea de suelo `#E6D8B8` de 4 px a 80 % del alto (y = 1536 px), de 9,3 % a 90,7 % del ancho. Los planos solo de objeto no llevan suelo.
- **Lienzo y zonas (1080x1920):** zona segura de `formatos.md`: x de 100 a 980 px (9,3 % a 90,7 %), y de 250 a 1670 px (13 % a 87 %). Zona de texto fija: arriba a la izquierda, texto alineado a la izquierda en x = 10 % (108 px). Los personajes nunca pisan la zona de texto ni la de gráficos: pies a 80 % del alto, `alto` = 34 % (653 px), por lo que la cabeza más alta llega a 46 %. En un plano medio solo de Tin, `alto` = 44 % (845 px), cabeza a 36 %.
- **Zonas del valle (tomas 5 a 10, v2), pensadas para el teléfono:** cifra principal al 7 % del alto (134 px) con su caja de y = 13,2 % a 20,2 %; equivalente de EE. UU. debajo, al 4,5 % (86 px), con su caja de 20,2 % a 24,7 %; **zona de gráficos de 25 % a 46 %** (403 px de alto, de x = 100 a 980 px). Los personajes quedan debajo, con la cabeza desde 46 %. En las tomas con cifra en la zona de texto, el texto siempre está a la izquierda y el gráfico nunca lo toca.
- **Lados:** Tan en x = 30 % (324 px) con `espejo=True`; Tin en x = 70 % (756 px) sin espejo; cada uno gesticula hacia afuera. Solos, en x = 50 %.
- **carrete a pantalla completa (tomas 1, 3 y 15, v2):** círculo tinta de 80 % del ancho (864 px de diámetro, de x = 108 a 972 px) centrado en (50 %, 52 %), con 6 dientes `#F3E9D2` y sin etiqueta a la vista; ocupa de 29,5 % a 74,5 % del alto y nunca toca la zona de texto (hasta 24 %). Gira a 720 grados por segundo desde el ángulo 0 (en el fotograma 0 y en el último, ángulo 0). El lápiz de gráfico mide 0,9 del diámetro (778 px), gira con él a 720 grados por segundo y su ángulo es de menos 35 grados en el fotograma 0 (ángulo = menos 35 más 720 por t: en 28,5 s son 20.520 grados, un múltiplo exacto de 360, por eso el último fotograma es igual al primero). Para que el fotograma 0 se vea «ya girando», el lápiz lleva una estela plana: dos copias del lápiz en `#E6D8B8` detrás, a menos 18 y menos 36 grados del ángulo actual, sin degradado ni desenfoque.
- **casete (gráfico propio, ancho W, alto 0,63 W, centro dado en cada toma):** cuerpo rectángulo redondeado (radio 0,06 W) relleno marrón `#7A4B2A` con contorno tinta de 0,012 W; etiqueta en x de menos 0,40 W a más 0,40 W y y de menos 0,29 W a menos 0,06 W, rellena `#FFF8EC`, con tres rayas dibujadas `#E6D8B8` y una franja tomate `#C8553D` de 0,03 W arriba, **sin letras**; ventana en x de menos 0,34 W a más 0,34 W y y de menos 0,02 W a más 0,20 W, rellena `#E6D8B8`; dos carretes de radio 0,075 W en x menos 0,17 W y más 0,17 W, y = más 0,09 W, rellenos tinta con 6 dientes `#F3E9D2`; dos tornillos de radio 0,018 W en las esquinas inferiores. Los carretes giran a 720 grados por segundo (2 vueltas por segundo, una vuelta por pulso) salvo que la toma diga otra cosa.
- **lápiz de gráfico:** el de `palitos.lapiz` (cuerpo mostaza `#E8B33B`, punta naranja claro, goma tomate), con largo 0,22 W cuando está en el carrete de un casete. Nunca sale de la ventana del casete (y de menos 0,02 W a más 0,20 W): así no toca la etiqueta.
- **reloj (cronómetro de 10 minutos):** círculo de diámetro 62 % del ancho (670 px), relleno `#FFF8EC`, contorno tinta de 0,012 D, 10 marcas mayores (una por minuto) y 50 menores, la marca de las 10 en tomate, **sin números**; botón rectangular arriba; centro en (50 %, 44 %), de 26,6 % a 61,4 % del alto.
- **Muelles (masa 1, rigidez, amortiguación), declarados por elemento:** `pop` 220 y 20 (entrada de textos y gráficos, escala de 0,85 a 1); `slide` 120 y 16 (personajes y gráficos que se desplazan); `sello` 320 y 26 (empujes de cámara). Contadores: ease-out cúbico sin muelle, para que el valor nunca pase de su final ni retroceda. Todo depende del número de fotograma (30 fps).
- **Transición `borrón`:** corte seco con desenfoque de movimiento horizontal de 18 px en los 2 últimos fotogramas de la toma que sale y en los 2 primeros de la que entra. Cero destellos.

## 6. Tomas

<!--
Todas las tomas son «edición»: dibujo por código. Tiempos al décimo de segundo, del video final (v2: 28,5 s).
Cada corte cae en un pulso de 0,5 s. Voz: línea y texto exactos de 05_audio/linea_de_tiempo_voz.md, SIN desplazar
(la línea 1 empieza en el fotograma 0). Ninguna palabra de la voz se corta.
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
- Texto «pencil turns?» (fila 1 de la tabla de la sección 12) ya entero y quieto en el fotograma 0 (sin `pop`; así el último fotograma puede ser igual), de 0,0 a 2,4.
- Sin personajes ni suelo.

### Toma 2 — Tan recuerda

- **Duración:** 1,0 s (de 1,5 a 2,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio general de Tan sola, de frente, con el casete arriba
- **Cámara:** empuje lento de 100 % a 102 %
- **Acción:** Tan levanta la mano de la pregunta mientras acaba la frase; el lápiz sigue girando en el carrete del casete.
- **Audio:** línea 1, Tan (segunda parte): "Remember rewinding a cassette with a pencil?" Aquí suena «with a pencil?» (de 1,5 a 2,4 s).
- **Referencia:** toma 3 de la v1 (Tan recuerda)
- **Transición de entrada:** `borrón` desde la toma 1. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `pregunta`, expresión `nostalgia`, vista `frente`, `mira=1`, `espejo=True`, x = 50 %, suelo 80 %, `alto` 34 %, `viento` oscilando de menos 0,3 a 0,3 con muelle.
- Casete de W = 52 % (562 px), centro (50 %, 34 %), de 24,8 % a 43,2 % del alto, carretes a 720 grados por segundo; el lápiz de gráfico (largo 0,22 W) ya está dentro del carrete derecho, girando con él (continúa el lápiz de la toma 1).
- Texto «pencil turns?» sigue hasta 2,4 en la zona de texto. Pestañas cortas visibles en los ojos de Tan; la bufanda no tapa el brazo.

### Toma 3 — Subjetivo del carrete

- **Duración:** 1,5 s (de 2,5 a 4,0)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** subjetivo: se mira dentro del carrete, de frente (el mismo carrete de la toma 1)
- **Cámara:** empuje de 100 % a 115 % hacia el centro del carrete, muelle `sello`
- **Acción:** el lápiz da 3 vueltas dentro del carrete, una por pulso.
- **Audio:** línea 2, Tan (primera mitad): "So, how many turns does it really take?" Aquí suena «So, how many turns» (de 2,6 a 4,0 s).
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
- **Audio:** línea 2, Tan (segunda mitad): "So, how many turns does it really take?" Aquí suena «does it really take?» (hasta 5,5 s).
- **Referencia:** toma 5 de la v1
- **Transición de entrada:** `borrón` desde la toma 3. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `pregunta`, expresión `curiosidad`, vista `frente`, `espejo=True`; se desliza de x = 50 % a x = 30 % entre 4,0 y 4,6 con muelle `slide`.
- Tin: entra de x = 118 % a x = 70 % entre 4,0 y 4,6 en pose `camina`, expresión `feliz`, vista `perfil`, `mira=-1`, sin espejo; en 4,6 cambia de golpe a pose `parado`, expresión `feliz`, vista `frente`, `objeto=True`. Revisar que la visera de perfil se lea como gorra.
- Casete de W = 52 % en (50 %, 34 %), carretes a 720 grados por segundo, sin lápiz (el lápiz pasa a la mano de Tin).
- Texto: «how many turns?» sigue hasta 5,4.

### Toma 5 — C90 de 45 minutos

- **Duración:** 3,0 s (de 5,5 a 8,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con un casete grande arriba que ocupa la zona de gráficos
- **Cámara:** empuje lento de 100 % a 103 %
- **Acción:** Tin explica con la mano abierta; Tan reacciona al dato encogiéndose de hombros; el casete gira con la etiqueta libre.
- **Audio:** línea 3, Tin: "A C ninety tape plays forty-five minutes per side." (de 5,7 a 8,1 s)
- **Referencia:** toma 6 de la v1
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 6.

**Especificación de dibujo:**

- Tan (reacción al dato «45 min»): pose `encoge`, expresión `curiosidad`, vista `frente`, x = 30 %, `espejo=True`, `viento` con muelle.
- Tin: pose `explica`, expresión `feliz`, vista `frente`, x = 70 %, sin espejo, `objeto=True`.
- Casete de W = 58 % (626 px, alto 394 px) en (50 %, 35,5 %), de 25,1 % a 45,9 % del alto. **Carretes girando a 720 grados por segundo** (en la v1 estaban quietos; ahora giran: el motivo que vuelve). Etiqueta visible y libre: ningún objeto ni texto encima.
- Texto: «45 min/side» al 7 % de 5,8 a 8,4, caja de 13,2 % a 20,2 %. Sin equivalente de EE. UU. (no es una medida métrica).

### Toma 6 — La cinta pasa a 4,76 cm/s

- **Duración:** 2,5 s (de 8,5 a 11,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle (macro) de un tramo de cinta, de frente, con Tan debajo
- **Cámara:** fija
- **Acción:** la cinta corre de derecha a izquierda con una escala de centímetros; Tan la señala.
- **Audio:** línea 4, Tin (primera parte): "At four point seven six centimeters a second, that's about one hundred twenty-eight meters of tape." Aquí suena «At four point seven six centimeters a second,» (de 8,4 a 11,0 s).
- **Referencia:** toma 7 de la v1
- **Transición de entrada:** `borrón` desde la toma 5. Salida: `borrón` hacia la toma 7.

**Especificación de dibujo:**

- Tira de cinta marrón de 100 % de ancho (sale del cuadro por los dos lados) y **10,4 % de alto (200 px)**, centrada en y = 35,5 % (de 30,3 % a 40,7 %). La v1 tenía 77 px.
- Marcas de tinta cada 12 % del ancho (130 px, un centímetro dibujado), de 6 px de grosor y 60 % del alto de la tira, que se desplazan a 4,76 marcas por segundo (617 px por segundo). Velocidad constante porque la velocidad es el dato; el arranque usa muelle `pop` de 0,2 s.
- Un corchete tomate de un centímetro (de una marca a la siguiente) sobre la tira, de **10 px de grosor**, fijo en x = 50 %, sin letras.
- Tan (reacción al dato «4,76 cm/s»): pose `senala`, expresión `concentrado`, vista `frente`, x = 50 %, `espejo=True`, suelo 80 %, `alto` 34 %.
- Texto: «4.76 cm/s» al 7 % de 8,6 a 10,9 y, debajo, «1⅞ in/s» al 4,5 % (equivalente de EE. UU., sin palabra clave). Sin sombra, sin nada sobre Tan.

### Toma 7 — La cinta se estira a 128,5 m

- **Duración:** 2,5 s (de 11,0 a 13,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto del recorrido de la cinta, de frente, con Tan debajo
- **Cámara:** fija
- **Acción:** la cinta entra por el borde izquierdo y se estira en zigzag mientras el contador sube de 0,0 a 128,5 m; Tan se asombra.
- **Audio:** línea 4, Tin (segunda parte): "At four point seven six centimeters a second, that's about one hundred twenty-eight meters of tape." Aquí suena «that's about one hundred twenty-eight meters of tape.» (hasta 13,3 s).
- **Referencia:** toma 8 de la v1 (la cinta se estira con un contador)
- **Transición de entrada:** `borrón` desde la toma 6. Salida: corte seco.

**Especificación de dibujo:**

- Cinta marrón de **24 px de grosor** (la v1 tenía 11 px) que entra por el borde izquierdo (el casete queda fuera de cuadro) y recorre 5 filas horizontales en y = 28 %, 32 %, 36 %, 40 % y 44 % (separación de 77 px entre ejes), de x = 12 % a x = 88 %, con vueltas redondeadas de radio 38 px; el largo dibujado es proporcional al valor del contador. Todo cabe en la zona de gráficos (de 27,4 % a 44,6 %).
- Tan (reacción al dato «128,5 m»): pose `pregunta`, expresión `sorpresa`, vista `frente`, x = 50 %, `espejo=True`, `viento` alto con muelle.
- Contador de 0,0 a 128,5 con ease-out cúbico de 11,2 a 13,2, un decimal, solo sube; al terminar se queda fijo. Texto «128.5 m» al 7 % y, debajo, su equivalente «≈ 422 ft» al 4,5 %, que sube de 0 a 422 con la misma curva y se queda fijo (filas de la tabla de la sección 12).
- Con suelo (hay personaje).

### Toma 8 — Una vuelta, 11 cm

- **Duración:** 2,5 s (de 13,5 a 16,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el diagrama del carrete llenando el ancho útil (plano héroe, cerca de la mitad del video)
- **Cámara:** fija
- **Acción:** el lápiz da una vuelta en el carrete, su arco se dibuja y se desenrolla en un segmento de 11 cm; Tan reacciona al dato.
- **Audio:** línea 5, Tin: "One pencil turn winds about eleven centimeters." (de 13,6 a 16,0 s)
- **Referencia:** toma 9 de la v1
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 9.

**Especificación de dibujo:**

- Tan (reacción al dato «11 cm»): pose `saluda`, expresión `sorpresa`, vista `frente`, x = 30 %, `espejo=True`.
- Tin: pose `explica`, expresión `feliz`, vista `frente`, x = 70 %, sin espejo, `objeto=True`; el lápiz de su mano tiene movimiento secundario de más o menos 3 grados con muelle.
- Diagrama que **llena la zona de gráficos de borde a borde de la zona segura** (la v1 usaba 160 px y un tercio del ancho): carrete de **diámetro 400 px**, de x = 100 a 500 px, centro (300 px, 35,5 %), de 25,1 % a 45,9 % del alto, con el lápiz de gráfico girando una vuelta de 13,8 a 14,8 (ease in-out); el arco tomate de **10 px** sobre el contorno se dibuja con la vuelta hasta cerrar el círculo; de 14,8 a 15,6 el arco se desenrolla hacia la derecha en un segmento recto tomate de **10 px de grosor** y 480 px de largo (44,4 % del ancho) desde x = 500 px hasta x = 980 px, en y = 35,5 %. El segmento es el dato de 11 cm; sin letras en el dibujo.
- Texto: «11 cm» al 7 % de 13,7 a 15,9 y, debajo, «≈ 4.3 in» al 4,5 %.

### Toma 9 — Tin piensa en los metros

- **Duración:** 1,5 s (de 16,0 a 17,5)
- **Personajes:** @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tin solo, de frente
- **Cámara:** empuje de 100 % a 106 %
- **Acción:** Tin se lleva la mano al mentón para dividir.
- **Audio:** línea 6, Tin (primera parte): "One hundred twenty-eight meters, divided by eleven centimeters..." Aquí suena «One hundred twenty-eight meters,» (de 16,2 a 17,5 s).
- **Referencia:** toma 10 de la v1
- **Transición de entrada:** `borrón` desde la toma 8. Salida: `borrón` hacia la toma 10.

**Especificación de dibujo:**

- Tin: pose `piensa`, expresión `pensando`, vista `frente`, x = 50 %, suelo 80 %, `alto` 44 %, sin espejo, `objeto=False` (en `piensa` el lápiz cruza la cara).
- Sin gráficos. Esta toma repite el dato de la toma 7 (no hay dato nuevo, así que no lleva reacción de Tan: es el respiro de composición entre dos tomas de dos personajes). Texto «128.5 m» al 7 % de 16,1 a 17,4 y, debajo, «≈ 422 ft» al 4,5 % (ya completo, sin contador).

### Toma 10 — La cinta se divide en tramos de 11 cm

- **Duración:** 2,0 s (de 17,5 a 19,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle (macro) de una barra que se subdivide, de frente, con Tan debajo
- **Cámara:** fija
- **Acción:** la barra de 128,5 m se parte en 2, 4, 8, 16, 32 y 64 tramos, una duplicación por cada cuarto de segundo; Tan se encoge de hombros.
- **Audio:** línea 6, Tin (segunda parte): "One hundred twenty-eight meters, divided by eleven centimeters..." Aquí suena «divided by eleven centimeters...» (hasta 19,3 s).
- **Referencia:** toma 11 de la v1
- **Transición de entrada:** `borrón` desde la toma 9. Salida: corte seco.

**Especificación de dibujo:**

- Barra marrón de x = 10 % a x = 90 % (864 px) y **10,4 % de alto (200 px)**, centrada en y = 35,5 % (la v1 tenía 77 px).
- Cortes verticales tomate que aparecen con muelle `pop` en 6 pasos de 0,25 s de 17,6 a 19,1 (2, 4, 8, 16, 32 y 64 tramos): **10 px de grosor** hasta 16 tramos, 6 px con 32 y 4 px con 64 (nunca más del 40 % del ancho de un tramo); de 19,1 a 19,4 los 64 tramos se rellenan de marcas finas, como cuadrícula densa. No se dibujan 1.170 marcas individuales: la barra es un símbolo de la división.
- Tan (reacción al dato «÷ 11 cm»): pose `encoge`, expresión `pensando`, vista `frente`, x = 50 %, `espejo=True`, suelo 80 %, `alto` 34 %.
- Texto: «÷ 11 cm» al 7 % de 17,6 a 19,3 y, debajo, «≈ 4.3 in» al 4,5 %.

### Toma 11 — 1.170 vueltas

- **Duración:** 3,0 s (de 19,5 a 22,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el contador arriba
- **Cámara:** empuje de 100 % a 102 %
- **Acción:** el contador sube de 0 a 1.170 mientras Tan celebra y Tin levanta el lápiz.
- **Audio:** línea 7, Tan: "About eleven hundred seventy turns!" (de 19,5 a 22,5 s)
- **Referencia:** toma 12 de la v1 (contador hasta 1.170 vueltas)
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 12.

**Especificación de dibujo:**

- Tan: pose `celebra`, expresión `sorpresa`, vista `frente`, x = 30 %, `espejo=True`, `viento` alto con muelle.
- Tin: pose `saluda`, expresión `eureka`, vista `frente`, x = 70 %, sin espejo, `objeto=True`.
- Contador en la zona de texto (y = 15 %), tamaño 7 %, de 0 a 1.170 con ease-out cúbico de 19,6 a 21,9; al llegar a 1.170 pasa de tinta y mostaza a tomate y hace un `pop` de escala solo del texto (el valor no se pasa). Texto «1,170 turns» (fila 9 de la tabla).
- Sin gráfico en la zona de gráficos.

### Toma 12 — Reloj revelado

- **Duración:** 2,0 s (de 22,5 a 24,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** revelado desde desenfoque: cronómetro de frente, centrado
- **Cámara:** fija
- **Acción:** el cronómetro se aclara y el lápiz gira en su centro a 2 vueltas por segundo.
- **Audio:** línea 8, Tin (primera parte): "At two turns a second, almost ten minutes. For one song." Aquí suena «At two turns a second,» (de 22,7 a 24,5 s).
- **Referencia:** toma 13 de la v1 (el reloj)
- **Transición de entrada:** `borrón` desde la toma 11. Salida: corte seco.

**Especificación de dibujo:**

- Reloj de la sección 5 en (50 %, 44 %). Desenfoque gaussiano de radio 24 px en 22,5 que baja a 0 en 23,0 (ease-out cúbico).
- Lápiz de gráfico de 0,40 D girando en el centro a 720 grados por segundo desde 22,5 (4 vueltas hasta 24,5). Aguja de minutos tomate quieta en la marca 0.
- Sin personajes. Texto: «2 turns/s» de 22,6 a 24,4.

### Toma 13 — Casi 10 minutos

- **Duración:** 1,5 s (de 24,5 a 26,0)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle del mismo cronómetro, de frente
- **Cámara:** fija
- **Acción:** el lápiz se detiene y la aguja de minutos recorre el 97,5 % de la esfera (585 s de 600 s).
- **Audio:** línea 8, Tin (segunda parte): "At two turns a second, almost ten minutes. For one song." Aquí suena «almost ten minutes.» (de 24,5 a 26,0 s).
- **Referencia:** toma 14 de la v1
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Mismo reloj y posición de la toma 12. El lápiz se detiene en 24,6 con muelle `pop`.
- Aguja tomate de 0 a 351 grados (97,5 % de 360) de 24,6 a 25,6, ease-out cúbico sin pasarse, para en un punto justo antes de la marca tomate de las 10.
- Texto: «almost 10 min» de 24,6 a 25,9 (0,1 s antes del corte, como pide la regla de que lo que sale se va antes de que entre lo siguiente).

### Toma 14 — Remate: rebobinar la cara para volver a la canción 1

- **Duración:** 1,0 s (de 26,0 a 27,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con una nota musical arriba
- **Cámara:** fija
- **Acción:** los dos se ríen mientras la nota musical salta sobre el casete.
- **Audio:** línea 8, Tin (remate): "At two turns a second, almost ten minutes. For one song." Aquí suena «For one song.» (de 26,0 a 26,9 s). La voz no se cambió; el texto en pantalla aclara que esos casi 10 minutos son el costo de rebobinar la cara entera para volver a la primera canción.
- **Referencia:** toma 15 de la v1
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 15.

**Especificación de dibujo:**

- Tan: pose `encoge`, expresión `risa`, vista `frente`, x = 30 %, `espejo=True`.
- Tin: pose `celebra`, expresión `risa`, vista `frente`, x = 70 %, sin espejo, `objeto=True`.
- Casete de W = 40 % (432 px) en (50 %, 34 %), carretes a 720 grados por segundo; sobre su etiqueta no se pone nada. Una corchea mostaza de 8 % del ancho (86 px) con contorno tinta entra con `pop` a (50 %, 26 %), encima del casete y fuera de la etiqueta.
- Texto: «replay song 1» de 26,1 a 26,9 (clave: replay). Es la redacción corta de «to replay song 1» (3 palabras, como manda la regla de subtítulos): estás al final de la cara y rebobinas toda la cara para volver a la primera canción.

### Toma 15 — Cierre en bucle: vuelve el carrete con lápiz

- **Duración:** 1,5 s (de 27,0 a 28,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** el mismo carrete con lápiz a pantalla completa de la toma 1
- **Cámara:** retroceso de 108 % a 100 % centrado en el centro del carrete, muelle `sello`; en 28,5 la escala es 100 %
- **Acción:** el carrete gira con el lápiz, ya en el plano exacto del fotograma 0; el último fotograma es igual al primero.
- **Audio:** sin voz (la voz terminó en 26,9: 1,6 s de silencio de voz hasta el empalme; en el fotograma 0 la voz vuelve a entrar sin pausa). Golpes finales de la sección 13.
- **Referencia:** toma 1 de esta versión (cierre en bucle con el plano del inicio)
- **Transición de entrada:** `borrón` desde la toma 14. Salida: bucle al fotograma 0 de la toma 1.

**Especificación de dibujo:**

- Carrete y lápiz de la sección 5, a 720 grados por segundo desde el ángulo que corresponda a 27,0 (carrete: 19.440 grados = 0 grados; lápiz: menos 35 grados). En 28,5 los dos están en el ángulo del fotograma 0 (carrete 0 grados, lápiz menos 35 grados, escala 100 %, texto «pencil turns?» a escala 1): **el fotograma 855 (el último) es igual al fotograma 0**. El lápiz no sale del carrete.
- Texto «pencil turns?» (fila 13 de la tabla) entra con `pop` en 27,7 y se queda hasta 28,5; sigue sin corte en la toma 1 del bucle (de 0,0 a 2,4).

## 7. Audio

- **Voz:** ya generada y montada: `05_audio/dialogo_110.mp3` (Tan con Zelda, Tin con Kevin, Higgsfield `seed_audio`, al 110 % con `atempo=1.10`, normalizada a −14 LUFS, 8 líneas, 26,9 s). **No se rehace ni se regenera.** Se coloca **sin retraso** (`adelay=0`): empieza en el fotograma 0 (la línea 1 de Tan arranca en 0,0) y termina en 26,9; hasta 28,5 hay 1,6 s sin voz, y al volver al fotograma 0 la voz entra otra vez sin silencio inicial: el silencio total del empalme del bucle es de 1,6 s (en la v1 eran 3,1 s). Los tiempos internos de la voz no se tocan y ninguna palabra se corta. Los cortes del diálogo se hicieron por pausas detectadas, sin escuchar: se comprueba al oído antes del render final.
- **Música:** hecha con código (confirmado por el dueño el 2026-11-21). Se genera con Python y numpy un patrón de 120 BPM (el pulso de la rejilla) a −24 LUFS, 10 dB por debajo de la voz, y se anota en `licencias.md`; no entra al video hasta que él lo decida. Debe cubrir 28,5 s y su fase cerrar en el pulso para el bucle.
- **Efectos:** los de la sección 13, hechos con código (Python y numpy), sin material de terceros.

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → Toma 3 → Toma 4 → Toma 5 → Toma 6 → Toma 7 → Toma 8 → Toma 9 → Toma 10 → Toma 11 → Toma 12 → Toma 13 → Toma 14 → Toma 15 (y vuelve a la toma 1). Los carretes de las tomas 1 y 3 y el de la toma 15 son el mismo plano; la toma 1 es la antigua toma 4 de la v1, subida al inicio.
- **Transiciones:** corte seco; entre planos de objeto o de cámara distinta, el `borrón` de la sección 5. Sin destellos, sin fundidos.
- **Texto en pantalla:** se dibuja en el mismo render, solo el de la tabla de la sección 12. El texto nunca contradice lo que se oye.
- **Portada:** el fotograma del carrete con el lápiz y «pencil turns?»: el fotograma de 0,5 s (fotograma 15) de la toma 1, o el fotograma 0 (son el mismo plano). Reemplaza la recomendación de la v1 (fotograma de 4,0 s).
- **Formato de salida:** 1080x1920, 30 fps, H.264, yuv420p, AAC a 48 kHz. Archivo `06_final/tin_y_tan_short01_v2.mp4` (no sobrescribe el v1).
- **Descripción de la publicación (en inglés, obligatoria):** debe decir que los 3,5 cm son el diámetro promedio del rollo de cinta, que crece mientras se rebobina, y que el resultado es una estimación. Texto propuesto: "Assumes an average spool diameter of 3.5 cm, which grows as the tape winds. Tape speed: 4.76 cm/s (1⅞ in/s). One 45-minute side." La fuente escrita de la velocidad está por confirmar con el dueño: hasta tenerla no se publica.

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | 0 s (las 15 tomas son edición; 28,5 s se resuelven en edición) | 0 |
| Keyframes | 0 | 0 |
| Remates en resolución final | 0 | 0 |
| **Total estimado** | 0 créditos nuevos (la voz ya costó 3 créditos y está en `costos.md`; la v2 no rehace la voz) | 0 |

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
- **Rejilla de tiempo:** pulso de 0,5 s (120 BPM, compás de 4 pulsos = 2,0 s); 57 pulsos = 28,5 s (14 compases y un pulso final de empalme). La voz entra en el pulso 0 (fotograma 0). Los 14 cortes caen en 1,5; 2,5; 4,0; 5,5; 8,5; 11,0; 13,5; 16,0; 17,5; 19,5; 22,5; 24,5; 26,0 y 27,0 (más el bucle en 28,5), a 0,2 s o menos antes del inicio de la frase de voz que corresponde: el corte se adelanta o coincide con la voz, nunca llega tarde por más de 0,1 s (toma 5 a 6 en 8,5, la voz de la línea 4 entra en 8,4). Inicios de la voz: 0,0; 2,6; 5,7; 8,4; 13,6; 16,2; 19,5; 22,7.
- **Gancho (0 a 2,5 s, v2):** el fotograma 0 es el carrete con el lápiz a pantalla completa, ya girando (con estela), con «pencil turns?» ya entero (clave: pencil, en mostaza) y la voz de Tan ya diciendo «Remember rewinding a cassette…» desde el fotograma 0. En 1,5 el `borrón` pasa a Tan y, en 2,5, de vuelta al carrete para «how many turns». Sin logo, sin título, sin segundo mudo. Gancho B para otra publicación (se renderiza gratis): el mismo plano con el texto «1,170 turns?».
- **Empieza en movimiento:** sí: sin intro ni logo; el lápiz gira dentro del carrete desde el fotograma 0 y es el primer fotograma, a tamaño completo.
- **Motivo visual que vuelve:** el carrete con el lápiz (tomas 1, 3 y 15, y el diagrama de la 8), el casete girando (tomas 2, 4, 5 y 14; ahora también en la del C90) y el lápiz amarillo de Tin; el lápiz que gira en el reloj (12). Todos giran a 2 vueltas por segundo, una por pulso. Se repiten con las mismas formas y colores.
- **Cierre:** el video vuelve al plano exacto del fotograma 0 (carrete a pantalla completa, lápiz a menos 35 grados, carrete en ángulo 0, escala 100 %, «pencil turns?» ya entero) y encadena en bucle con la toma 1: el último fotograma es el primero. Cierre de 1,5 s (de 27,0 a 28,5); voz termina en 26,9; silencio de voz en el empalme: 1,6 s (≤ 2 s).
- **Llamado a la acción:** ninguno. Por qué: el objetivo comercial es presencia y línea base de retención; pedir suscripción antes de que el canal exista (lo crea el dueño) no se puede cumplir, y un llamado al final corta el bucle (reglas 3 y 4 del cap. 11: un solo llamado y que el final empalme con el inicio). Si el dueño fija otro objetivo, se añade uno solo en la descripción, no en el video.

Mapa de ritmo (los tiempos al décimo de segundo; cortes por segundo = cortes que caen dentro del tramo, sin contar el inicio):

| Tramo | Segundos | Pulso o intervalo | Cortes por segundo | Qué pasa (una acción) | Respiro |
|---|---|---|---|---|---|
| Gancho | 0,0–2,5 | 1,5 s y 1,0 s | 0,8 | el lápiz gira en el carrete, Tan recuerda el gesto | no |
| Pregunta | 2,5–5,5 | 1,5 s | 0,7 | subjetivo del carrete y entrada de Tin | no |
| Dato 1 | 5,5–8,5 | 3,0 s | 0,3 | un C90 dura 45 min por lado; Tan se encoge | sí |
| Cinta | 8,5–13,5 | 2,5 s | 0,4 | velocidad de la cinta y 128,5 m; Tan señala y se asombra | no |
| Héroe | 13,5–16,0 | 2,5 s | 0,4 | una vuelta de lápiz son 11 cm | no |
| Cuenta | 16,0–19,5 | 1,5 s y 2,0 s | 0,6 | dividir 128,5 m entre 11 cm | no |
| Pico | 19,5–22,5 | 3,0 s | 0,3 | contador hasta 1.170 y celebración | no (pico de emoción) |
| Remate | 22,5–27,0 | 2,0 s, 1,5 s y 1,0 s | 0,7 | el reloj, casi 10 minutos, rebobinar la cara para volver a la canción 1 | no (acelera) |
| Cierre | 27,0–28,5 | 1,5 s | 0 | vuelve el carrete con lápiz del primer fotograma | sí |

Total: 14 cortes en 28,5 s. Es menos que los 52 cambios en 30 s del video viral que cita el cap. 11, porque este video lleva una voz continua de 26,9 s y cada cifra necesita su plano; la densidad extra va dentro de cada toma (subtítulo que cambia, contador que sube, reacción de Tan por dato, carretes a 2 vueltas por segundo). En la v2 cada dato del valle lleva además una reacción distinta de Tan, para que no sea «dos muñecos parados y un dato arriba». Decisión de la dirección de prompts, a revisar por el equipo si el dueño quiere más cortes.

Lo que sale se va antes de que entre lo siguiente: los textos salen de 0,1 a 0,2 s antes del corte siguiente y los gráficos con el borrón. El movimiento es mecánica: entradas con `pop` o `slide` (muelle), contadores con ease-out cúbico, giros a velocidad constante de 720 grados por segundo, sin interpolación lineal salvo la velocidad de la cinta de la toma 6.

Tipos de plano disponibles y dónde van: detalle o macro (tomas 6, 10 y 13), héroe abierto (tomas 4, 5, 8, 11 y 14; el héroe principal es la toma 8 en 13,5–16,0, a la mitad del video), subjetivo y carrete a pantalla completa (tomas 1, 3 y 15), revelado desde desenfoque (toma 12), objeto que salta sobre el mismo fondo (la corchea de la toma 14 y el lápiz de la 2). Transiciones siempre motivadas (borrón de movimiento). **No más de 3 destellos por segundo:** hay cero.

## 12. Texto en pantalla y sistema de diseño

- **Tipografías:** Inter Display Medium, licencia SIL Open Font License 1.1 (archivo `/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf`; en Windows, si no está, Segoe UI Semibold, que se anota en `licencias.md` antes de usarla). Siempre en minúsculas, alineadas a la izquierda.
- **Paleta:** papel `#F3E9D2` · papel_sombra `#E6D8B8` · tinta `#2B2420` · naranja `#E07A2E` · marrón `#7A4B2A` · verde azulado `#2F7F7A` · mostaza `#E8B33B` (palabra clave de los subtítulos) · tomate `#C8553D` (cifra final, goma, alertas) · rubor `#E9967A` · blanco `#FFF8EC`. Un color de acento por plano. La palabra clave en mostaza lleva un trazo de tinta de **0,06 em** (era 0,05 em en la v1: el director vio borrosa la palabra clave a ese tamaño) porque mostaza sobre crema no tiene contraste suficiente.
- **Referencias de movimiento:** `01_referencia/` está vacía (el video de la prueba está en la PC del dueño). Las referencias cargadas son `canales/nostalgia-tin-y-tan/DESIGN.md`, `herramientas/palitos.py` y las hojas de `personajes/tin/referencias/` y `personajes/tan/referencias/`; el movimiento lo definen los muelles de la sección 5.
- **Prohibido:**
  1. Mayúsculas centradas sobre degradado, tarjetas con degradado o cualquier fondo con degradado.
  2. Animaciones lineales de posición o escala (solo muelle o ease-out cúbico; la única velocidad constante es la de la cinta de la toma 6 y los giros de 720 grados por segundo).
  3. El símbolo «→» y cualquier glifo sin comprobar: en la prueba salieron como cuadrados. Se escribe «almost» y la flecha, si hiciera falta, se dibuja. **Excepción de la v2:** «≈» y «⅞» solo en las filas de equivalentes de la tabla de abajo, y solo después de comprobar que la fuente del render los trae (comprobado el 2026-11-21: `InterDisplay-Medium.otf` los dibuja, igual que «÷», «?», «,», «.» y «/»). Si el render usa otra fuente y falta alguno: «≈» se escribe «about» y «1⅞» se escribe «1 7/8».
  4. Un contador que retrocede o que se pasa de su valor final y vuelve (nada de rebote en el valor; el rebote solo es de escala).
  5. Texto encima de un personaje, del casete, del carrete o del reloj.
  6. El lápiz sobre la etiqueta del casete o letras en la etiqueta.
  7. Líneas sin suavizar: ningún dibujo fuera de un `Lienzo` con supermuestreo.
  8. Sombras suaves, resplandor, partículas, confeti y luz azul y naranja sin motivo (la estela del lápiz de la toma 1 es plana, sin degradado ni desenfoque).
  9. Subtítulos de más de 3 palabras, de más de una línea o fuera de la zona segura (la cifra con su equivalente debajo son dos líneas de la misma fila, a distinto tamaño, y cuentan como una pieza).
  10. Cualquier pose, expresión o vista que no esté en `palitos.py`, y cambiar los colores o accesorios de Tin y Tan.
- **Márgenes seguros y escenario:** zona segura de `formatos.md`: x de 9,3 % a 90,7 % y y de 13 % a 87 %. El contenido ocupa el centro de 880x1420 px (81 % del ancho y 74 % del alto). Texto en x = 10 %, y de 14 % a 24 % (de 13,2 % a 24,7 % en las filas con cifra y equivalente); personajes con pies a 80 % y cabeza desde 46 % (36 % en el plano medio de Tin); gráficos entre 25 % y 46 % cuando hay personajes en el valle.
- **Texto exacto:** todo texto en pantalla es el de la tabla de abajo, letra por letra. Los contadores muestran enteros o un decimal (como se indica) entre 0 y su valor final.
- **No afirmar:** ninguna cifra fuera de la tabla «Datos del video» del brief (45 min por lado, 4,76 cm/s, 128,5 m, 11 cm, 1.170 vueltas, 2 vueltas por segundo, casi 10 minutos) **más las tres equivalencias de EE. UU. de la v2, verificadas el 2026-11-21:** «1⅞ in/s» (4,76 cm/s ÷ 2,54 = 1,874 in/s; 1⅞ = 1,875, la velocidad de diseño de 1⅞ ips), «≈ 422 ft» (128,5 m ÷ 0,3048 = 421,59 ft, que redondea a 422; con 128,52 m = 45 min × 60 × 4,76 cm/s da 421,65 ft, también 422; **no** «421 ft») y «≈ 4.3 in» (11 cm ÷ 2,54 = 4,33 in). No mostrar «585 s» ni «9:45»; no decir que la velocidad es exacta en todos los casetes ni citar fuente mientras falte; no nombrar marcas de casete; no mostrar «C90» (lo dice la voz); no escribir «one song» ni «for one song» en pantalla (la cifra de casi 10 minutos es de una cara entera, no de una canción).
- **Subtítulos:** de 1 a 3 palabras, con la palabra clave en mostaza (con trazo de tinta); la cifra final «1,170» pasa a tomate. Las cifras del valle (filas 3 a 8) van al 7 % del alto; su equivalente de EE. UU., debajo, al 4,5 %, en tinta, sin palabra clave.

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| pencil turns? (clave: pencil; ya entero en el fotograma 0, sin pop) | 0,0 | 2,4 | 10, 15 | 6 |
| how many turns? (clave: turns) | 2,7 | 5,4 | 10, 15 | 5 |
| 45 min/side (clave: 45) | 5,8 | 8,4 | 10, 13,2 | 7 |
| 4.76 cm/s (clave: 4.76) | 8,6 | 10,9 | 10, 13,2 | 7 |
| 1⅞ in/s (equivalente de la fila anterior; sin clave) | 8,6 | 10,9 | 10, 20,2 | 4,5 |
| 128.5 m (contador de 0.0 a 128.5; clave: el número) | 11,2 | 13,4 | 10, 13,2 | 7 |
| ≈ 422 ft (contador de 0 a 422; sin clave) | 11,2 | 13,4 | 10, 20,2 | 4,5 |
| 11 cm (clave: 11) | 13,7 | 15,9 | 10, 13,2 | 7 |
| ≈ 4.3 in (sin clave) | 13,7 | 15,9 | 10, 20,2 | 4,5 |
| 128.5 m (clave: 128.5) | 16,1 | 17,4 | 10, 13,2 | 7 |
| ≈ 422 ft (sin clave) | 16,1 | 17,4 | 10, 20,2 | 4,5 |
| ÷ 11 cm (clave: 11) | 17,6 | 19,3 | 10, 13,2 | 7 |
| ≈ 4.3 in (sin clave) | 17,6 | 19,3 | 10, 20,2 | 4,5 |
| 1,170 turns (contador de 0 a 1,170; al llegar, el número en tomate) | 19,6 | 22,4 | 10, 15 | 7 |
| 2 turns/s (clave: 2) | 22,6 | 24,4 | 10, 15 | 5 |
| almost 10 min (clave: 10) | 24,6 | 25,9 | 10, 15 | 5 |
| replay song 1 (clave: replay; redacción corta de «to replay song 1») | 26,1 | 26,9 | 10, 15 | 5 |
| pencil turns? (clave: pencil; entra con pop y sigue sin corte en la fila 1 del bucle) | 27,7 | 28,5 | 10, 15 | 6 |

En un short, todo texto queda dentro de la zona segura de `formatos.md`. Entrada de cada texto: `pop` con escala de 0,85 a 1 en 8 fotogramas; salida: subir 2 % con ease-in en 3 fotogramas (excepción: la fila 1 en el fotograma 0 está ya a escala 1, y la última fila queda a escala 1 en el último fotograma para que el bucle empalme). Antes de renderizar se comprueba que la fuente tiene los glifos «÷», «≈», «⅞», «?», «,», «.» y «/»; si «÷» faltara, se escribe «/ 11 cm».

## 13. Sonido

| Golpe o efecto | Segundo | A qué corte va atado | Origen y licencia |
|---|---|---|---|
| Golpe seco de casete que cae (thunk grave de 80 ms), bajo la voz | 0,0 | arranque, toma 1 (es también el empalme del bucle: no se duplica) | código, propio (ver licencias.md) |
| 2 clics de matraca, uno por vuelta | 0,5 / 1,0 | vueltas del lápiz en la toma 1 | código, propio |
| Clic suave de borrón | 1,5 | corte de toma 1 a toma 2 | código, propio |
| Clic suave de borrón y plop del lápiz asentándose en el carrete | 2,5 | corte de toma 2 a toma 3 | código, propio |
| 3 clics de matraca, uno por vuelta | 2,5 / 3,0 / 3,5 | vueltas del lápiz en la toma 3 | código, propio |
| Clic suave de borrón y pasos de Tin | 4,0 | corte de toma 3 a toma 4 | código, propio |
| Clic suave | 5,5 | corte de toma 4 a toma 5 | código, propio |
| Clic suave de borrón | 8,5 | corte de toma 5 a toma 6 | código, propio |
| Zumbido de cinta bajo (hiss) mientras corre | 8,5–11,0 | toma 6 | código, propio |
| Clic suave de borrón | 11,0 | corte de toma 6 a toma 7 | código, propio |
| Tictac de contador que sube de tono | 11,2–13,2 | contador de la toma 7 | código, propio |
| Clic suave | 13,5 | corte de toma 7 a toma 8 | código, propio |
| Matraca de una vuelta y pitido del arco | 13,8–14,8 | vuelta del lápiz en la toma 8 | código, propio |
| Clic suave de borrón | 16,0 | corte de toma 8 a toma 9 | código, propio |
| Clic suave de borrón | 17,5 | corte de toma 9 a toma 10 | código, propio |
| 6 clics de corte, uno por duplicación | 17,6–19,1 | cortes de la barra en la toma 10 | código, propio |
| Clic suave | 19,5 | corte de toma 10 a toma 11 | código, propio |
| Tictac de contador que sube de tono | 19,6–21,9 | contador de la toma 11 | código, propio |
| Ding de campana al llegar a 1,170 | 21,9 | valor final de la toma 11 | código, propio |
| Clic suave de borrón | 22,5 | corte de toma 11 a toma 12 | código, propio |
| Matraca, una por vuelta | 22,5 / 23,0 / 23,5 / 24,0 | vueltas del lápiz en la toma 12 | código, propio |
| Clic suave | 24,5 | corte de toma 12 a toma 13 | código, propio |
| Campanilla corta al llegar la aguja | 25,6 | fin del recorrido en la toma 13 | código, propio |
| Clic suave | 26,0 | corte de toma 13 a toma 14 | código, propio |
| Nota corta de 3 tonos sobre la corchea | 26,1 | la corchea de la toma 14 | código, propio |
| Clic suave de borrón | 27,0 | corte de toma 14 a toma 15 | código, propio |
| Whoosh suave de retroceso de cámara | 27,0–28,3 | retroceso de la toma 15 | código, propio |
| Matraca, una por vuelta | 27,0 / 27,5 / 28,0 | vueltas del lápiz en la toma 15 | código, propio |
| Thunk grave idéntico al del segundo 0,0 (cierra el bucle; el del 0,0 lo continúa) | 28,5 | bucle: último golpe igual al primero | código, propio |

- **Música:** hecha con código (confirmado por el dueño el 2026-11-21; ver sección 7). Voz a −14 LUFS, golpes a −18 LUFS y música a −24 LUFS.
- **Voz:** sí. `05_audio/dialogo_110.mp3`, sin retraso (empieza en el fotograma 0). Los golpes bajo la voz van a −24 dB respecto a ella para no taparla. El silencio de voz del empalme (26,9 a 28,5 s, 1,6 s) lo llenan solo los golpes, el whoosh y la música.

## 14. Motor y revisión

- **Cómo se hace:** gráficos por código (fotograma a fotograma): Python, Pillow y ffmpeg. Cada fotograma se dibuja en un `Lienzo(1080, 1920)` de `palitos.py`, que ya dibuja al triple de tamaño y reduce con LANCZOS (supermuestreo; el pedido era al menos el doble) para que las líneas queden suaves; los gráficos propios (casete, carrete a pantalla completa, reloj, cinta) se dibujan sobre el mismo lienzo con `lz.d` y las mismas escalas. Los empujes de cámara recortan el lienzo grande y reducen, así no se pierde nitidez. Todo depende del número de fotograma, no del reloj. Se guardan PNG numerados y ffmpeg los une con la voz y los efectos (`postpro.py mezclar` o ffmpeg directo). Personajes con `palitos.dibujar(lz, id, x, suelo, alto, pose, expresion, vista, mira, viento, objeto, espejo)`.
- **Punto de control y autorización (v2):** **renderizar la v2 rehace una pieza ya terminada (la v1) y necesita el sí del dueño** (CLAUDE.md, «Quién decide qué» y «Créditos y cambios»); no cuesta créditos, pero no se renderiza sin ese sí. Antes de renderizar se presenta la lista de tomas de la sección 6 sobre la rejilla de la sección 11 y se espera el visto bueno del equipo; también se actualiza `03_keyframes/definicion.md` con la entrada de «pieza por código» de `generacion.md` (datos con fuente, paleta con HEX, tipografía y licencia, texto exacto, 28,5 s a 30 fps, rejilla, prohibidos, motor y versión: palitos.py 1.1, Pillow 12.3.0, y costo 0). El render v1 (`06_final/tin_y_tan_short01_v1.mp4`) corresponde a la v1 y no se toca; la v2 sale como `tin_y_tan_short01_v2.mp4`.
- **Revisión:** prueba corta de 5,5 s (de 0,0 a 5,5: gancho, Tan, subjetivo y entrada de Tin), un fotograma por pulso, hoja de contacto y comprobación de medidas (zona segura, `alto` y x de cada personaje, etiqueta libre, el fotograma 0 con el lápiz ya girando y la palabra «pencil» legible). Después del render completo, `herramientas/revisar_fotogramas.py` sobre el video y `analizar_video.py <video> <carpeta> --cada 0.5`; se anota en `07_revision/`. Se comprueba al oído que cada corte de la voz cae donde dice la sección 6 y que la voz arranca en el fotograma 0.
- **Qué se marca:** imagen congelada, fotograma vacío, texto cortado o tapado, elemento fuera de cuadro, tirones, demasiado tiempo sin cambio, contador que retrocede, glifos cuadrados (en particular «≈» y «⅞»), lápiz sobre la etiqueta, texto sobre un personaje o sobre el carrete, el fotograma 855 (el último) distinto del 0, más de 3 destellos por segundo, la visera de Tin en perfil (toma 4), y en el teléfono: que cinta, zigzag, carrete del diagrama, arco y segmento se lean (medidas mínimas de la sección 6) y que cada dato lleve una reacción de Tan distinta. Nota para el validador: en las tomas con personajes (2, 4, 5, 6, 7, 8, 9, 10, 11 y 14), el bloque de identidad de la ficha no se pega en el prompt porque no hay generador de imágenes; el diseño oficial es el código de `palitos.py` y se comprueba con la lista de comprobación de cada ficha.
- **Vueltas:** las correcciones por código son gratis (salvo servicios de pago, que van a `costos.md`); **las de generador no se repiten sin autorización del dueño** (`generacion.md`). Aquí no hay generador, así que no hay vueltas de pago.
