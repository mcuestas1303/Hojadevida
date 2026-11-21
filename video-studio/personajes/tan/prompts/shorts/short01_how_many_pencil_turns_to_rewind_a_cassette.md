<!-- Copia archivada. Se edita en proyectos/2026-11-21_tin_y_tan_casete_y_lapiz/02_prompt/prompt.md y se vuelve a archivar. -->
# Prompt de video para redes — How many pencil turns to rewind a cassette?

<!--
Pieza dibujada con código (sin generador de video). Todas las tomas son método «edición»: se resuelven gratis
en el montaje. En lugar de «Prompt de keyframe» y «Prompt de video» cada toma lleva una «Especificación de dibujo».
Los tiempos son del video final (la voz empieza en el segundo 1,0).
-->

## 1. Ficha técnica

- **Proyecto:** 2026-11-21_tin_y_tan_casete_y_lapiz
- **Tipo:** short
- **Número:** 1
- **Serie:** ninguna
- **Objetivo de aprendizaje:** no aplica
- **Generador:** ninguno: imagen dibujada con código (palitos.py + gráficos propios), armada con ffmpeg
- **Aspecto:** 9:16
- **Duración total:** 30 s (gancho de 1,0 s sin voz; la voz de 26,9 s al 110 % va de 1,0 a 27,9 s; cierre de 2,1 s sin voz, de 27,9 a 30,0 s)
- **Resolución de borrador:** 540x960 a 30 fps, prueba de 5 s con un fotograma por pulso (render propio)
- **Resolución final:** 1080x1920 a 30 fps, 900 fotogramas
- **Precio por segundo:** 0 (render propio; no hay servicio de pago)
- **Intentos estimados por toma:** 1

## 2. Elenco

| Personaje | Papel en este video | Vestuario | Referencia que se sube |
|---|---|---|---|
| @tan | Abre el video: recuerda el gesto de rebobinar con lápiz y hace la pregunta. Reacciona a la cifra final. Lado izquierdo del cuadro, con `espejo=True`. | base de su ficha (rodete y bufanda mostaza) | personajes/tan/referencias/principal_tin_y_tan.png |
| @tin | Hace la cuenta con el lápiz amarillo y dice el resultado en minutos. Lado derecho del cuadro, sin espejo. | base de su ficha (gorra marrón, lentes, lápiz) | personajes/tin/referencias/principal_tin_y_tan.png |

No se sube nada a un generador: las referencias son las del diseño en código (`herramientas/palitos.py`, versión 1.1) y se usan solo para comparar el resultado.

## 3. Idea en una línea

Tan recuerda el gesto de rebobinar un casete con un lápiz y Tin hace la cuenta real sobre papel crema, una cifra por plano que solo sube, hasta que 1.170 vueltas resultan ser casi 10 minutos de lápiz para una sola canción: nostalgia que termina en sorpresa.

**Confirmado por el dueño el 2026-11-21:** short vertical 9:16; inglés para Estados Unidos; música hecha con código.

**Decidido por el equipo el 2026-11-21** (el dueño delegó las decisiones técnicas; razones en `00_brief.md`):

1. Gancho A: la pregunta «how many turns?», sin adelantar la cifra. Gancho B, para probar en otra publicación: «1,170 turns?».
2. Objetivo comercial: presencia y línea base de retención; sin llamado a la acción.
3. Público: Estados Unidos, de 45 a 70 años, con núcleo en mayores de 50.
4. Lo produce el Generador de prompts en su conversación, con los agentes del equipo de producción.

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
- **Lienzo y zonas (1080x1920):** zona segura de `formatos.md`: x de 100 a 980 px (9,3 % a 90,7 %), y de 250 a 1670 px (13 % a 87 %). Zona de texto fija: arriba a la izquierda, texto alineado a la izquierda en x = 10 % (108 px), y de 14 % a 24 %. Zona de gráficos con personajes: y de 24 % a 44 %. Los personajes nunca pisan la zona de texto ni la de gráficos: pies a 80 % del alto, `alto` = 34 % (653 px), por lo que la cabeza más alta llega a 46 %. En un plano medio solo de Tin, `alto` = 44 % (845 px), cabeza a 36 %.
- **Lados:** Tan en x = 30 % (324 px) con `espejo=True`; Tin en x = 70 % (756 px) sin espejo; cada uno gesticula hacia afuera. Solos, en x = 50 %.
- **casete (gráfico propio, ancho W, alto 0,63 W, centro dado en cada toma):** cuerpo rectángulo redondeado (radio 0,06 W) relleno marrón `#7A4B2A` con contorno tinta de 0,012 W; etiqueta en x de menos 0,40 W a más 0,40 W y y de menos 0,29 W a menos 0,06 W, rellena `#FFF8EC`, con tres rayas dibujadas `#E6D8B8` y una franja tomate `#C8553D` de 0,03 W arriba, **sin letras**; ventana en x de menos 0,34 W a más 0,34 W y y de menos 0,02 W a más 0,20 W, rellena `#E6D8B8`; dos carretes de radio 0,075 W en x menos 0,17 W y más 0,17 W, y = más 0,09 W, rellenos tinta con 6 dientes `#F3E9D2`; dos tornillos de radio 0,018 W en las esquinas inferiores. Los carretes giran a 720 grados por segundo (2 vueltas por segundo, una vuelta por pulso) salvo que la toma diga otra cosa.
- **lápiz de gráfico:** el de `palitos.lapiz` (cuerpo mostaza `#E8B33B`, punta naranja claro, goma tomate), con largo 0,22 W cuando está en el carrete de un casete. Nunca sale de la ventana del casete (y de menos 0,02 W a más 0,20 W): así no toca la etiqueta.
- **reloj (cronómetro de 10 minutos):** círculo de diámetro 62 % del ancho (670 px), relleno `#FFF8EC`, contorno tinta de 0,012 D, 10 marcas mayores (una por minuto) y 50 menores, la marca de las 10 en tomate, **sin números**; botón rectangular arriba; centro en (50 %, 44 %), de 26,6 % a 61,4 % del alto.
- **Muelles (masa 1, rigidez, amortiguación), declarados por elemento:** `pop` 220 y 20 (entrada de textos y gráficos, escala de 0,85 a 1); `slide` 120 y 16 (personajes y gráficos que se desplazan); `sello` 320 y 26 (empujes de cámara). Contadores: ease-out cúbico sin muelle, para que el valor nunca pase de su final ni retroceda. Todo depende del número de fotograma (30 fps).
- **Transición `borrón`:** corte seco con desenfoque de movimiento horizontal de 18 px en los 2 últimos fotogramas de la toma que sale y en los 2 primeros de la que entra. Cero destellos.

## 6. Tomas

<!--
Todas las tomas son «edición»: dibujo por código. Tiempos al décimo de segundo, del video final.
Cada corte cae en un pulso de 0,5 s. Voz: línea y texto exactos de 05_audio/linea_de_tiempo_voz.md, desplazada 1,0 s.
-->

### Toma 1 — Casete entra girando

- **Duración:** 0,5 s (de 0,0 a 0,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto del casete, de frente, centrado
- **Cámara:** fija
- **Acción:** el casete sube de (50 %, 62 %) a (50 %, 46 %) y se endereza; ya está en movimiento en el fotograma 0.
- **Audio:** sin voz. Golpe 1 de la sección 13.
- **Referencia:** escena 1 de la prueba de 30 s (el casete entra girando)
- **Transición de entrada:** ninguna (primer fotograma). Salida: corte directo a la toma 2 sin borrón porque el empuje continúa el mismo movimiento.

**Especificación de dibujo:**

- Casete de W = 70 % del ancho (756 px, alto 476 px), centro final (50 %, 46 %): ocupa de 33,6 % a 58,4 % del alto.
- Fotograma 0: centro (50 %, 62 %), rotación menos 12 grados, escala 0,9, carretes en ángulo 0. Entra con muelle `slide` hasta (50 %, 46 %), rotación 0, escala 1.
- Carretes a 720 grados por segundo desde el fotograma 0. Sin lápiz. Sin personajes.
- El texto «how many turns?» entra en 0,2 (fila 1 de la tabla de la sección 12).

### Toma 2 — Empuje al carrete

- **Duración:** 0,5 s (de 0,5 a 1,0)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle (macro) del carrete izquierdo del casete
- **Cámara:** empuje de 100 % a 135 % centrado en el carrete izquierdo (38,1 %, 49,5 %), muelle `sello`
- **Acción:** la cámara se mete en el carrete que sigue girando.
- **Audio:** sin voz. Golpe 2.
- **Referencia:** escena 1 de la prueba de 30 s
- **Transición de entrada:** continuación de la toma 1. Salida: `borrón` hacia la toma 3.

**Especificación de dibujo:**

- Mismo casete de la toma 1, quieto en (50 %, 46 %). Solo se mueve la cámara y los carretes (720 grados por segundo).
- Los textos son una capa aparte que no escala con la cámara.

### Toma 3 — Tan recuerda

- **Duración:** 2,5 s (de 1,0 a 3,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio general de Tan sola, de frente, con el casete arriba
- **Cámara:** empuje lento de 100 % a 104 %
- **Acción:** Tan levanta la mano de la pregunta mientras habla y, al decir «pencil», el lápiz cae al carrete del casete.
- **Audio:** línea 1, Tan: "Remember rewinding a cassette with a pencil?" (de 1,0 a 3,4 s)
- **Referencia:** escena 1 de la prueba de 30 s
- **Transición de entrada:** `borrón` desde la toma 2. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `pregunta`, expresión `nostalgia`, vista `frente`, `mira=1`, `espejo=True`, x = 50 %, suelo 80 %, `alto` 34 %, `viento` oscilando de menos 0,3 a 0,3 con muelle.
- Casete de W = 52 % (562 px), centro (50 %, 34 %), de 24,8 % a 43,2 % del alto, carretes a 720 grados por segundo. El lápiz de gráfico (largo 0,22 W) entra al carrete derecho en 2,8 con muelle `pop`.
- Texto: «rewinding a cassette» de 1,5 a 3,4 en la zona de texto.
- Pestañas cortas visibles en los ojos de Tan; la bufanda no tapa el brazo.

### Toma 4 — Subjetivo del carrete

- **Duración:** 1,5 s (de 3,5 a 5,0)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** subjetivo: se mira dentro del carrete, de frente
- **Cámara:** empuje de 100 % a 120 % hacia el centro del carrete
- **Acción:** el lápiz da 3 vueltas dentro del carrete, una por pulso.
- **Audio:** línea 2, Tan (primera mitad): "So, how many turns does it really take?" Aquí suena «So, how many turns» (de 3,6 a 5,0 s).
- **Referencia:** escena 3 de la prueba de 30 s (el lápiz gira dentro del carrete)
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 5.

**Especificación de dibujo:**

- Carrete a pantalla completa: círculo tinta de 60 % del ancho (648 px) centrado en (50 %, 50 %), 6 dientes `#F3E9D2`. Sin etiqueta a la vista.
- Lápiz de gráfico de 0,9 del diámetro del carrete, girando 1.080 grados en 1,5 s (una vuelta cada 0,5 s) con muelle `pop` en el arranque.
- Texto: «how many turns?» entra en 3,7 (sigue en la toma 5).

### Toma 5 — Tin entra

- **Duración:** 1,5 s (de 5,0 a 6,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el casete arriba
- **Cámara:** fija
- **Acción:** Tan se corre a la izquierda y Tin entra caminando por la derecha hasta su lugar.
- **Audio:** línea 2, Tan (segunda mitad): "So, how many turns does it really take?" Aquí suena «does it really take?» (hasta 6,5 s).
- **Referencia:** escena 1 de la prueba de 30 s
- **Transición de entrada:** `borrón` desde la toma 4. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `pregunta`, expresión `curiosidad`, vista `frente`, `espejo=True`; se desliza de x = 50 % a x = 30 % entre 5,0 y 5,6 con muelle `slide`.
- Tin: entra de x = 118 % a x = 70 % entre 5,0 y 5,6 en pose `camina`, expresión `feliz`, vista `perfil`, `mira=-1`, sin espejo; en 5,6 cambia de golpe a pose `parado`, expresión `feliz`, vista `frente`, `objeto=True`. Revisar que la visera de perfil se lea como gorra.
- Casete de W = 52 % en (50 %, 34 %), carretes a 720 grados por segundo, sin lápiz.
- Texto: «how many turns?» sigue hasta 6,4.

### Toma 6 — C90 de 45 minutos

- **Duración:** 3,0 s (de 6,5 a 9,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el casete arriba
- **Cámara:** empuje lento de 100 % a 103 %
- **Acción:** Tin explica con la mano abierta mientras el casete se queda quieto y la etiqueta muestra el lado A.
- **Audio:** línea 3, Tin: "A C ninety tape plays forty-five minutes per side." (de 6,7 a 9,1 s)
- **Referencia:** escena 2 de la prueba de 30 s
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 7.

**Especificación de dibujo:**

- Tan: pose `parado`, expresión `curiosidad`, vista `frente`, x = 30 %, `espejo=True`.
- Tin: pose `explica`, expresión `feliz`, vista `frente`, x = 70 %, sin espejo, `objeto=True`.
- Casete de W = 52 % en (50 %, 34 %). Carretes quietos en esta toma (respiro). Etiqueta visible y libre: ningún objeto ni texto encima.
- Texto: «45 min/side» de 6,8 a 9,4.

### Toma 7 — La cinta pasa a 4,76 cm/s

- **Duración:** 2,5 s (de 9,5 a 12,0)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle (macro) de un tramo de cinta, de frente
- **Cámara:** fija
- **Acción:** la cinta corre de derecha a izquierda con una escala de centímetros.
- **Audio:** línea 4, Tin (primera parte): "At four point seven six centimeters a second, that's about one hundred twenty-eight meters of tape." Aquí suena «At four point seven six centimeters a second,» (de 9,4 a 12,0 s).
- **Referencia:** escena 2 de la prueba de 30 s
- **Transición de entrada:** `borrón` desde la toma 6. Salida: `borrón` hacia la toma 8.

**Especificación de dibujo:**

- Tira de cinta marrón de 100 % de ancho (sale del cuadro por los dos lados) y 4 % de alto (77 px), centrada en y = 45 %.
- Marcas de tinta cada 12 % del ancho (un centímetro dibujado), que se desplazan a 4,76 marcas por segundo (572 px por segundo). Velocidad constante porque la velocidad es el dato; el arranque usa muelle `pop` de 0,2 s.
- Un corchete tomate de un centímetro (de una marca a la siguiente) sobre la tira, fijo en x = 50 %, sin letras.
- Sin personajes. Texto: «4.76 cm/s» de 9,6 a 11,9.

### Toma 8 — La cinta se estira a 128,5 m

- **Duración:** 2,5 s (de 12,0 a 14,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto del recorrido de la cinta, de frente
- **Cámara:** fija
- **Acción:** la cinta sale del casete y se estira en zigzag mientras el contador sube de 0,0 a 128,5 m.
- **Audio:** línea 4, Tin (segunda parte): "At four point seven six centimeters a second, that's about one hundred twenty-eight meters of tape." Aquí suena «that's about one hundred twenty-eight meters of tape.» (hasta 14,3 s).
- **Referencia:** escena 2 de la prueba de 30 s (la cinta se estira con un contador)
- **Transición de entrada:** `borrón` desde la toma 7. Salida: corte seco.

**Especificación de dibujo:**

- Casete pequeño de W = 24 % (259 px) con centro (76 %, 22 %), carretes a 720 grados por segundo.
- Cinta marrón de 1 % del ancho (11 px) que sale del casete y recorre 5 filas horizontales en y = 33 %, 43 %, 53 %, 63 % y 73 %, de x = 12 % a x = 88 %, con vueltas redondeadas; el largo dibujado es proporcional al valor del contador.
- Contador de 0,0 a 128,5 con ease-out cúbico de 12,2 a 14,2, un decimal, solo sube; al terminar se queda fijo. Texto «128.5 m» (fila 6 de la tabla de la sección 12).
- Sin personajes ni suelo.

### Toma 9 — Una vuelta, 11 cm

- **Duración:** 2,5 s (de 14,5 a 17,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el diagrama del carrete arriba (plano héroe, cerca de la mitad del video)
- **Cámara:** fija
- **Acción:** el lápiz da una vuelta en el carrete, su arco se dibuja y se desenrolla en un segmento de 11 cm.
- **Audio:** línea 5, Tin: "One pencil turn winds about eleven centimeters." (de 14,6 a 17,0 s)
- **Referencia:** escena 3 de la prueba de 30 s
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 10.

**Especificación de dibujo:**

- Tan: pose `parado`, expresión `curiosidad`, vista `frente`, x = 30 %, `espejo=True`.
- Tin: pose `explica`, expresión `feliz`, vista `frente`, x = 70 %, sin espejo, `objeto=True`; el lápiz de su mano tiene movimiento secundario de más o menos 3 grados con muelle.
- Diagrama en la zona de gráficos: carrete de diámetro 160 px, centro (22 %, 35 %), con el lápiz de gráfico girando una vuelta de 14,8 a 15,8 (ease in-out); el arco tomate de 3 px sobre el contorno se dibuja con la vuelta hasta cerrar el círculo; de 15,8 a 16,6 el arco se desenrolla hacia la derecha en un segmento recto tomate de 503 px (46,6 % del ancho) desde x = 34 % hasta x = 80,6 %, en y = 35 %. El segmento es el dato de 11 cm; sin letras en el dibujo.
- Texto: «11 cm» de 14,7 a 16,9.

### Toma 10 — Tin piensa en los metros

- **Duración:** 1,5 s (de 17,0 a 18,5)
- **Personajes:** @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tin solo, de frente
- **Cámara:** empuje de 100 % a 106 %
- **Acción:** Tin se lleva la mano al mentón para dividir.
- **Audio:** línea 6, Tin (primera parte): "One hundred twenty-eight meters, divided by eleven centimeters..." Aquí suena «One hundred twenty-eight meters,» (de 17,2 a 18,5 s).
- **Referencia:** escena 4 de la prueba de 30 s
- **Transición de entrada:** `borrón` desde la toma 9. Salida: `borrón` hacia la toma 11.

**Especificación de dibujo:**

- Tin: pose `piensa`, expresión `pensando`, vista `frente`, x = 50 %, suelo 80 %, `alto` 44 %, sin espejo, `objeto=False` (en `piensa` el lápiz cruza la cara).
- Sin gráficos. Texto: «128.5 m» de 17,1 a 18,4 (subtítulo de 5 %).

### Toma 11 — La cinta se divide en tramos de 11 cm

- **Duración:** 2,0 s (de 18,5 a 20,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle (macro) de una barra que se subdivide, de frente
- **Cámara:** fija
- **Acción:** la barra de 128,5 m se parte en 2, 4, 8, 16, 32 y 64 tramos, una duplicación por cada cuarto de segundo.
- **Audio:** línea 6, Tin (segunda parte): "One hundred twenty-eight meters, divided by eleven centimeters..." Aquí suena «divided by eleven centimeters...» (hasta 20,3 s).
- **Referencia:** escena 4 de la prueba de 30 s
- **Transición de entrada:** `borrón` desde la toma 10. Salida: corte seco.

**Especificación de dibujo:**

- Barra marrón de x = 10 % a x = 90 % (864 px) y 4 % de alto, centrada en y = 40 %.
- Cortes verticales tomate de 3 px que aparecen con muelle `pop` en 6 pasos de 0,25 s de 18,6 a 20,1 (2, 4, 8, 16, 32 y 64 tramos); de 20,1 a 20,4 los 64 tramos se rellenan de marcas finas, como cuadrícula densa. No se dibujan 1.170 marcas individuales: la barra es un símbolo de la división.
- Sin personajes. Texto: «÷ 11 cm» de 18,6 a 20,3.

### Toma 12 — 1.170 vueltas

- **Duración:** 3,0 s (de 20,5 a 23,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el contador arriba
- **Cámara:** empuje de 100 % a 102 %
- **Acción:** el contador sube de 0 a 1.170 mientras Tan celebra y Tin levanta el lápiz.
- **Audio:** línea 7, Tan: "About eleven hundred seventy turns!" (de 20,5 a 23,5 s)
- **Referencia:** escena 4 de la prueba de 30 s (contador hasta 1.170 vueltas)
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 13.

**Especificación de dibujo:**

- Tan: pose `celebra`, expresión `sorpresa`, vista `frente`, x = 30 %, `espejo=True`, `viento` alto con muelle.
- Tin: pose `saluda`, expresión `eureka`, vista `frente`, x = 70 %, sin espejo, `objeto=True`.
- Contador en la zona de texto (y = 15 %), tamaño 7 %, de 0 a 1.170 con ease-out cúbico de 20,6 a 22,9; al llegar a 1.170 pasa de tinta y mostaza a tomate y hace un `pop` de escala solo del texto (el valor no se pasa). Texto «1,170 turns» (fila 10 de la tabla).
- Sin gráfico en la zona de gráficos.

### Toma 13 — Reloj revelado

- **Duración:** 2,0 s (de 23,5 a 25,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** revelado desde desenfoque: cronómetro de frente, centrado
- **Cámara:** fija
- **Acción:** el cronómetro se aclara y el lápiz gira en su centro a 2 vueltas por segundo.
- **Audio:** línea 8, Tin (primera parte): "At two turns a second, almost ten minutes. For one song." Aquí suena «At two turns a second,» (de 23,7 a 25,5 s).
- **Referencia:** escena 5 de la prueba de 30 s (el reloj)
- **Transición de entrada:** `borrón` desde la toma 12. Salida: corte seco.

**Especificación de dibujo:**

- Reloj de la sección 5 en (50 %, 44 %). Desenfoque gaussiano de radio 24 px en 23,5 que baja a 0 en 24,0 (ease-out cúbico).
- Lápiz de gráfico de 0,40 D girando en el centro a 720 grados por segundo desde 23,5 (4 vueltas hasta 25,5). Aguja de minutos tomate quieta en la marca 0.
- Sin personajes. Texto: «2 turns/s» de 23,6 a 25,4.

### Toma 14 — Casi 10 minutos

- **Duración:** 1,5 s (de 25,5 a 27,0)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle del mismo cronómetro, de frente
- **Cámara:** fija
- **Acción:** el lápiz se detiene y la aguja de minutos recorre el 97,5 % de la esfera (585 s de 600 s).
- **Audio:** línea 8, Tin (segunda parte): "At two turns a second, almost ten minutes. For one song." Aquí suena «almost ten minutes.» (de 25,5 a 27,0 s).
- **Referencia:** escena 5 de la prueba de 30 s
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Mismo reloj y posición de la toma 13. El lápiz se detiene en 25,6 con muelle `pop`.
- Aguja tomate de 0 a 351 grados (97,5 % de 360) de 25,6 a 26,6, ease-out cúbico sin pasarse, para en un punto justo antes de la marca tomate de las 10.
- Texto: «almost 10 min» de 25,6 a 26,9 (0,1 s antes del corte, como pide la regla de que lo que sale se va antes de que entre lo siguiente).

### Toma 15 — Para una sola canción

- **Duración:** 1,0 s (de 27,0 a 28,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con una nota musical arriba
- **Cámara:** fija
- **Acción:** los dos se ríen mientras la nota musical salta sobre el casete.
- **Audio:** línea 8, Tin (remate): "At two turns a second, almost ten minutes. For one song." Aquí suena «For one song.» (de 27,0 a 27,9 s).
- **Referencia:** escena 5 de la prueba de 30 s
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 16.

**Especificación de dibujo:**

- Tan: pose `encoge`, expresión `risa`, vista `frente`, x = 30 %, `espejo=True`.
- Tin: pose `celebra`, expresión `risa`, vista `frente`, x = 70 %, sin espejo, `objeto=True`.
- Casete de W = 40 % (432 px) en (50 %, 34 %), carretes a 720 grados por segundo; sobre su etiqueta no se pone nada. Una corchea mostaza de 8 % del ancho (86 px) con contorno tinta entra con `pop` a (50 %, 26 %), encima del casete y fuera de la etiqueta.
- Texto: «for one song» de 27,1 a 27,9.

### Toma 16 — Cierre en bucle

- **Duración:** 2,0 s (de 28,0 a 30,0)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto del casete, igual que la toma 1
- **Cámara:** fija
- **Acción:** el casete gira con el lápiz en su carrete y, en 29,4, el lápiz sale y el casete baja a la posición del primer fotograma.
- **Audio:** sin voz (la voz terminó en 27,9). Golpes finales de la sección 13.
- **Referencia:** escena 6 de la prueba de 30 s (cierre en bucle con el plano del inicio)
- **Transición de entrada:** `borrón` desde la toma 15. Salida: bucle al fotograma 0 de la toma 1.

**Especificación de dibujo:**

- Casete de W = 70 % en (50 %, 46 %), carretes a 720 grados por segundo desde ángulo 0 en 28,0 (en 30,0 vuelven a ángulo 0 porque son 1.440 grados). Lápiz de gráfico en el carrete izquierdo, dentro de la ventana.
- En 29,4 el lápiz sale hacia arriba y desaparece en 0,2 s; de 29,4 a 30,0 el casete baja con muelle `slide` a (50 %, 62 %), rotación menos 12 grados, escala 0,9. El fotograma 900 es igual al fotograma 0 de la toma 1.
- Sin texto.

## 7. Audio

- **Voz:** ya generada y montada: `05_audio/dialogo_110.mp3` (Tan con Zelda, Tin con Kevin, Higgsfield `seed_audio`, al 110 % con `atempo=1.10`, normalizada a −14 LUFS, 8 líneas, 26,9 s). Se coloca con un retraso de 1,0 s (`adelay=1000`): empieza en el segundo 1,0 y termina en 27,9. Los tiempos de la voz no se tocan. Los cortes del diálogo se hicieron por pausas detectadas, sin escuchar: se comprueba al oído antes del render final.
- **Música:** hecha con código (confirmado por el dueño el 2026-11-21). Se genera con Python y numpy un patrón de 120 BPM (el pulso de la rejilla) a −24 LUFS, 10 dB por debajo de la voz, y se anota en `licencias.md`; no entra al video hasta que él lo decida.
- **Efectos:** los de la sección 13, hechos con código (Python y numpy), sin material de terceros.

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → Toma 3 → Toma 4 → Toma 5 → Toma 6 → Toma 7 → Toma 8 → Toma 9 → Toma 10 → Toma 11 → Toma 12 → Toma 13 → Toma 14 → Toma 15 → Toma 16 (y vuelve a la toma 1).
- **Transiciones:** corte seco; entre planos de objeto o de cámara distinta, el `borrón` de la sección 5. Sin destellos, sin fundidos.
- **Texto en pantalla:** se dibuja en el mismo render, solo el de la tabla de la sección 12.
- **Formato de salida:** 1080x1920, 30 fps, H.264, yuv420p, AAC a 48 kHz.
- **Descripción de la publicación (en inglés, obligatoria):** debe decir que los 3,5 cm son el diámetro promedio del rollo de cinta, que crece mientras se rebobina, y que el resultado es una estimación. Texto propuesto: "Assumes an average spool diameter of 3.5 cm, which grows as the tape winds. Tape speed: 4.76 cm/s." La fuente escrita de la velocidad está por confirmar con el dueño: hasta tenerla no se publica.

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | 0 s (las 16 tomas son edición; 30 s se resuelven en edición) | 0 |
| Keyframes | 0 | 0 |
| Remates en resolución final | 0 | 0 |
| **Total estimado** | 0 créditos nuevos (la voz ya costó 3 créditos y está en `costos.md`) | 0 |

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
- **Rejilla de tiempo:** pulso de 0,5 s (120 BPM, compás de 4 pulsos = 2,0 s); 60 pulsos = 15 compases = 30,0 s. La voz entra en el pulso 2 (1,0 s). Los 15 cortes caen en 0,5; 1,0; 3,5; 5,0; 6,5; 9,5; 12,0; 14,5; 17,0; 18,5; 20,5; 23,5; 25,5; 27,0 y 28,0 (más el bucle en 30,0), a 0,2 s o menos del inicio de la frase de voz que corresponde: el corte se adelanta o coincide con la voz, nunca llega tarde por más de 0,1 s (toma 6 a 7 en 9,5, la voz entra en 9,4).
- **Gancho (0 a 1 s):** movimiento y pregunta. El casete ya está girando en el fotograma 0, sube con muelle y en 0,5 la cámara se mete en el carrete; el texto «how many turns?» entra en 0,2 con «turns» en mostaza. Sin voz, sin logo, sin título. Gancho B para otra publicación (se renderiza gratis): el mismo plano con el texto «almost 10 min?».
- **Empieza en movimiento:** sí: sin intro ni logo; el casete gira y se mueve desde el fotograma 0.
- **Motivo visual que vuelve:** el casete girando (tomas 1, 2, 3, 5, 6, 8, 15 y 16; el carrete en la 4 y el 9; el lápiz que gira en 13) y el lápiz amarillo de Tin. Los dos giran a 2 vueltas por segundo, una por pulso. Se repiten con las mismas formas y colores.
- **Cierre:** el casete vuelve a la posición del primer fotograma (50 %, 62 %, rotación menos 12 grados, escala 0,9, carretes en ángulo 0) y el video encadena en bucle con la toma 1. Cierre de 2,0 s sin voz (de 28,0 a 30,0).
- **Llamado a la acción:** ninguno. Por qué: el objetivo comercial está por confirmar y la propuesta de la coordinación es medir retención y formato; pedir suscripción antes de que el canal exista (lo crea el dueño) no se puede cumplir, y un llamado al final corta el bucle (reglas 3 y 4 del cap. 11: un solo llamado y que el final empalme con el inicio). Si el dueño fija otro objetivo, se añade uno solo en la descripción, no en el video.

Mapa de ritmo (los tiempos al décimo de segundo; cortes por segundo = cortes que caen dentro del tramo, sin contar el inicio):

| Tramo | Segundos | Pulso o intervalo | Cortes por segundo | Qué pasa (una acción) | Respiro |
|---|---|---|---|---|---|
| Gancho | 0,0–1,0 | 0,5 s | 2,0 | casete entra, empuje al carrete, pregunta con la palabra clave en mostaza | no |
| Pregunta | 1,0–3,5 | 2,5 s | 0,4 | Tan recuerda el gesto del lápiz | sí |
| Entra Tin | 3,5–6,5 | 1,5 s | 0,7 | subjetivo del carrete y entrada de Tin | no |
| Dato 1 | 6,5–9,5 | 3,0 s | 0,3 | un C90 dura 45 min por lado | sí |
| Cinta | 9,5–14,5 | 2,5 s | 0,4 | velocidad de la cinta y 128,5 m | no |
| Héroe | 14,5–17,0 | 2,5 s | 0,4 | una vuelta de lápiz son 11 cm | no |
| Cuenta | 17,0–20,5 | 1,5 s y 2,0 s | 0,6 | dividir 128,5 m entre 11 cm | no |
| Pico | 20,5–23,5 | 3,0 s | 0,3 | contador hasta 1.170 y celebración | no (pico de emoción) |
| Remate | 23,5–28,0 | 2,0 s, 1,5 s y 1,0 s | 0,7 | el reloj, casi 10 minutos, una canción | no (acelera) |
| Cierre | 28,0–30,0 | 2,0 s | 0 | el casete vuelve al primer plano | sí |

Total: 15 cortes en 30 s. Es menos que los 52 cambios en 30 s del video viral que cita el cap. 11, porque este video lleva una voz continua de 26,9 s y cada cifra necesita su plano; la densidad extra va dentro de cada toma (subtítulo que cambia, contador que sube, personaje que entra, carretes a 2 vueltas por segundo). Decisión de la dirección de prompts, a revisar por el equipo si el dueño quiere más cortes.

Lo que sale se va antes de que entre lo siguiente: los textos salen de 0,1 a 0,2 s antes del corte siguiente y los gráficos con el borrón. El movimiento es mecánica: entradas con `pop` o `slide` (muelle), contadores con ease-out cúbico, giros a velocidad constante de 720 grados por segundo, sin interpolación lineal salvo la velocidad de la cinta de la toma 7.

Tipos de plano disponibles y dónde van: detalle o macro (tomas 2, 7, 11 y 14), héroe abierto (tomas 1, 5, 6, 9, 12, 15 y 16; el héroe principal es la toma 9 en 14,5–17,0, a la mitad del video), subjetivo (toma 4), revelado desde desenfoque (toma 13), objeto que salta sobre el mismo fondo (la corchea de la toma 15 y el lápiz de la 3). Transiciones siempre motivadas (borrón de movimiento). **No más de 3 destellos por segundo:** hay cero.

## 12. Texto en pantalla y sistema de diseño

- **Tipografías:** Inter Display Medium, licencia SIL Open Font License 1.1 (archivo `/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf`; en Windows, si no está, Segoe UI Semibold, que se anota en `licencias.md` antes de usarla). Siempre en minúsculas, alineadas a la izquierda.
- **Paleta:** papel `#F3E9D2` · papel_sombra `#E6D8B8` · tinta `#2B2420` · naranja `#E07A2E` · marrón `#7A4B2A` · verde azulado `#2F7F7A` · mostaza `#E8B33B` (palabra clave de los subtítulos) · tomate `#C8553D` (cifra final, goma, alertas) · rubor `#E9967A` · blanco `#FFF8EC`. Un color de acento por plano. La palabra clave en mostaza lleva un trazo de tinta de 0,05 em porque mostaza sobre crema no tiene contraste suficiente.
- **Referencias de movimiento:** `01_referencia/` está vacía (el video de la prueba está en la PC del dueño). Las referencias cargadas son `canales/nostalgia-tin-y-tan/DESIGN.md`, `herramientas/palitos.py` y las hojas de `personajes/tin/referencias/` y `personajes/tan/referencias/`; el movimiento lo definen los muelles de la sección 5.
- **Prohibido:**
  1. Mayúsculas centradas sobre degradado, tarjetas con degradado o cualquier fondo con degradado.
  2. Animaciones lineales de posición o escala (solo muelle o ease-out cúbico; la única velocidad constante es la de la cinta de la toma 7 y los giros de 720 grados por segundo).
  3. Los símbolos «≈» y «→» y cualquier glifo sin comprobar: en la prueba salieron como cuadrados. Se escribe «almost» y la flecha, si hiciera falta, se dibuja.
  4. Un contador que retrocede o que se pasa de su valor final y vuelve (nada de rebote en el valor; el rebote solo es de escala).
  5. Texto encima de un personaje, del casete o del reloj.
  6. El lápiz sobre la etiqueta del casete o letras en la etiqueta.
  7. Líneas sin suavizar: ningún dibujo fuera de un `Lienzo` con supermuestreo.
  8. Sombras suaves, resplandor, partículas, confeti y luz azul y naranja sin motivo.
  9. Subtítulos de más de 3 palabras, de más de una línea o fuera de la zona segura.
  10. Cualquier pose, expresión o vista que no esté en `palitos.py`, y cambiar los colores o accesorios de Tin y Tan.
- **Márgenes seguros y escenario:** zona segura de `formatos.md`: x de 9,3 % a 90,7 % y y de 13 % a 87 %. El contenido ocupa el centro de 880x1420 px (81 % del ancho y 74 % del alto). Texto en x = 10 %, y de 14 % a 24 %; personajes con pies a 80 % y cabeza desde 46 % (36 % en el plano medio de Tin); gráficos entre 24 % y 44 % cuando hay personajes.
- **Texto exacto:** todo texto en pantalla es el de la tabla de abajo, letra por letra. Los contadores muestran enteros o un decimal (como se indica) entre 0 y su valor final.
- **No afirmar:** ninguna cifra fuera de la tabla «Datos del video» del brief (45 min por lado, 4,76 cm/s, 128,5 m, 11 cm, 1.170 vueltas, 2 vueltas por segundo, casi 10 minutos); no mostrar «585 s» ni «9:45»; no decir que la velocidad es exacta en todos los casetes ni citar fuente mientras falte; no nombrar marcas de casete; no mostrar «C90» (lo dice la voz).
- **Subtítulos:** de 1 a 3 palabras, con la palabra clave en mostaza (con trazo de tinta); la cifra final «1,170» pasa a tomate.

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| how many turns? (clave: turns) | 0,2 | 1,3 | 10, 15 | 6 |
| rewinding a cassette (clave: cassette) | 1,5 | 3,4 | 10, 15 | 5 |
| how many turns? (clave: turns) | 3,7 | 6,4 | 10, 15 | 5 |
| 45 min/side (clave: 45) | 6,8 | 9,4 | 10, 15 | 5 |
| 4.76 cm/s (clave: 4.76) | 9,6 | 11,9 | 10, 15 | 5 |
| 128.5 m (contador de 0.0 a 128.5; clave: el número) | 12,2 | 14,4 | 10, 15 | 7 |
| 11 cm (clave: 11) | 14,7 | 16,9 | 10, 15 | 5 |
| 128.5 m (clave: 128.5) | 17,1 | 18,4 | 10, 15 | 5 |
| ÷ 11 cm (clave: 11) | 18,6 | 20,3 | 10, 15 | 5 |
| 1,170 turns (contador de 0 a 1,170; al llegar, el número en tomate) | 20,6 | 23,4 | 10, 15 | 7 |
| 2 turns/s (clave: 2) | 23,6 | 25,4 | 10, 15 | 5 |
| almost 10 min (clave: 10) | 25,6 | 26,9 | 10, 15 | 5 |
| for one song (clave: song) | 27,1 | 27,9 | 10, 15 | 5 |

En un short, todo texto queda dentro de la zona segura de `formatos.md`. Entrada de cada texto: `pop` con escala de 0,85 a 1 en 8 fotogramas; salida: subir 2 % con ease-in en 3 fotogramas. Antes de renderizar se comprueba que la fuente tiene los glifos «÷», «?», «,», «.» y «/»; si «÷» faltara, se escribe «/ 11 cm».

## 13. Sonido

| Golpe o efecto | Segundo | A qué corte va atado | Origen y licencia |
|---|---|---|---|
| Golpe seco de casete que cae (thunk grave de 80 ms) | 0,0 | arranque, toma 1 | código, propio (ver licencias.md) |
| Whoosh corto de empuje | 0,5 | corte de toma 1 a toma 2 | código, propio |
| Clic suave de borrón | 1,0 | corte de toma 2 a toma 3 | código, propio |
| Plop del lápiz al caer en el carrete | 2,8 | movimiento dentro de la toma 3 | código, propio |
| Clic suave de borrón | 3,5 | corte de toma 3 a toma 4 | código, propio |
| 3 clics de matraca, uno por vuelta | 3,5 / 4,0 / 4,5 | vueltas del lápiz en la toma 4 | código, propio |
| Clic suave de borrón y pasos de Tin | 5,0 | corte de toma 4 a toma 5 | código, propio |
| Clic suave | 6,5 | corte de toma 5 a toma 6 | código, propio |
| Clic suave de borrón | 9,5 | corte de toma 6 a toma 7 | código, propio |
| Zumbido de cinta bajo (hiss) mientras corre | 9,5–12,0 | toma 7 | código, propio |
| Clic suave de borrón | 12,0 | corte de toma 7 a toma 8 | código, propio |
| Tictac de contador que sube de tono | 12,2–14,2 | contador de la toma 8 | código, propio |
| Clic suave | 14,5 | corte de toma 8 a toma 9 | código, propio |
| Matraca de una vuelta y pitido del arco | 14,8–15,8 | vuelta del lápiz en la toma 9 | código, propio |
| Clic suave de borrón | 17,0 | corte de toma 9 a toma 10 | código, propio |
| Clic suave de borrón | 18,5 | corte de toma 10 a toma 11 | código, propio |
| 6 clics de corte, uno por duplicación | 18,6–20,1 | cortes de la barra en la toma 11 | código, propio |
| Clic suave | 20,5 | corte de toma 11 a toma 12 | código, propio |
| Tictac de contador que sube de tono | 20,6–22,9 | contador de la toma 12 | código, propio |
| Ding de campana al llegar a 1,170 | 22,9 | valor final de la toma 12 | código, propio |
| Clic suave de borrón | 23,5 | corte de toma 12 a toma 13 | código, propio |
| Matraca, una por vuelta | 23,5 / 24,0 / 24,5 / 25,0 | vueltas del lápiz en la toma 13 | código, propio |
| Clic suave | 25,5 | corte de toma 13 a toma 14 | código, propio |
| Campanilla corta al llegar la aguja | 26,6 | fin del recorrido en la toma 14 | código, propio |
| Clic suave | 27,0 | corte de toma 14 a toma 15 | código, propio |
| Nota corta de 3 tonos sobre la corchea | 27,1 | la corchea de la toma 15 | código, propio |
| Clic suave de borrón | 28,0 | corte de toma 15 a toma 16 | código, propio |
| Matraca, una por vuelta | 28,0 / 28,5 / 29,0 | vueltas del lápiz en la toma 16 | código, propio |
| Whoosh de salida del lápiz y thunk grave idéntico al del segundo 0,0 | 29,4 / 30,0 | bucle: último golpe igual al primero | código, propio |

- **Música:** hecha con código (confirmado por el dueño el 2026-11-21; ver sección 7). Voz a −14 LUFS, golpes a −18 LUFS y música a −24 LUFS.
- **Voz:** sí. `05_audio/dialogo_110.mp3`, retrasada 1,0 s. Los golpes bajo la voz van a −24 dB respecto a ella para no taparla.

## 14. Motor y revisión

- **Cómo se hace:** gráficos por código (fotograma a fotograma): Python, Pillow y ffmpeg. Cada fotograma se dibuja en un `Lienzo(1080, 1920)` de `palitos.py`, que ya dibuja al triple de tamaño y reduce con LANCZOS (supermuestreo; el pedido era al menos el doble) para que las líneas queden suaves; los gráficos propios (casete, reloj, cinta) se dibujan sobre el mismo lienzo con `lz.d` y las mismas escalas. Los empujes de cámara recortan el lienzo grande y reducen, así no se pierde nitidez. Todo depende del número de fotograma, no del reloj. Se guardan PNG numerados y ffmpeg los une con la voz y los efectos (`postpro.py mezclar` o ffmpeg directo). Personajes con `palitos.dibujar(lz, id, x, suelo, alto, pose, expresion, vista, mira, viento, objeto, espejo)`.
- **Punto de control:** antes de renderizar se presenta la lista de tomas de la sección 6 sobre la rejilla de la sección 11 y se espera el visto bueno del equipo y la autorización del dueño; también se entrega `03_keyframes/definicion.md` con la entrada de «pieza por código» de `generacion.md` (datos con fuente, paleta con HEX, tipografía y licencia, texto exacto, 30 s a 30 fps, rejilla, prohibidos, motor y versión: palitos.py 1.1, Pillow 12.3.0, y costo 0).
- **Revisión:** prueba corta de 5 s (de 0,0 a 5,0: gancho, Tan y entrada de Tin), un fotograma por pulso, hoja de contacto y comprobación de medidas (zona segura, `alto` y x de cada personaje, etiqueta libre). Después del render completo, `herramientas/revisar_fotogramas.py` sobre el video y `analizar_video.py <video> <carpeta> --cada 0.5`; se anota en `07_revision/`. Se comprueba al oído que cada corte de la voz cae donde dice la sección 6.
- **Qué se marca:** imagen congelada, fotograma vacío, texto cortado o tapado, elemento fuera de cuadro, tirones, demasiado tiempo sin cambio, contador que retrocede, glifos cuadrados, lápiz sobre la etiqueta, texto sobre un personaje, el fotograma 900 distinto del 0, más de 3 destellos por segundo, y la visera de Tin en perfil (toma 5). Nota para el validador: en las tomas con personajes (3, 5, 6, 9, 10, 12 y 15), el bloque de identidad de la ficha no se pega en el prompt porque no hay generador de imágenes; el diseño oficial es el código de `palitos.py` y se comprueba con la lista de comprobación de cada ficha.
- **Vueltas:** las correcciones por código son gratis (salvo servicios de pago, que van a `costos.md`); **las de generador no se repiten sin autorización del dueño** (`generacion.md`). Aquí no hay generador, así que no hay vueltas de pago.
