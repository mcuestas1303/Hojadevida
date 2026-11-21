<!-- Copia archivada. Se edita en proyectos/2026-11-21_tin_y_tan_gta6/02_prompt/prompt.md y se vuelve a archivar. -->
# Prompt de video para redes — How many days did we wait for GTA 6?

> **ESTADO (2026-11-21):** la voz **no está generada**; todos los tiempos de voz de este prompt son **estimados** (ritmo medido en el short 1, ver sección 7) y se reajustan a la rejilla de 0,5 s cuando exista la voz. El render está **pendiente de autorización del dueño** (la voz necesita cotización y su sí; el render es de 0 créditos). Nada se ha generado ni renderizado.
> Hereda el formato y las lecciones del short 1 (`2026-11-21_tin_y_tan_casete_y_lapiz`): el objeto y la voz desde el fotograma 0, cifras al 7 % del alto, personajes y gráficos en el tercio de abajo, una reacción de Tan por dato, bucle con último fotograma igual al primero, rejilla de 0,5 s, golpes bajo la voz a unos −26 LUFS y música por código.

<!--
Pieza dibujada con código (sin generador de video). Todas las tomas son método «edición»: se resuelven gratis
en el montaje. En lugar de «Prompt de keyframe» y «Prompt de video» cada toma lleva una «Especificación de dibujo».
Los tiempos son del video final y los de la voz son ESTIMADOS (la voz no existe todavía).
-->

## 1. Ficha técnica

- **Proyecto:** 2026-11-21_tin_y_tan_gta6
- **Tipo:** short
- **Número:** 2
- **Serie:** ninguna
- **Objetivo de aprendizaje:** no aplica
- **Generador:** ninguno: imagen dibujada con código (palitos.py + gráficos propios), armada con ffmpeg
- **Aspecto:** 9:16
- **Duración total:** 26,5 s estimados (la voz estimada de 25,2 s al 110 % va de 0,0 a 25,2 s, sin gancho mudo; cierre de 1,3 s sin voz, de 25,2 a 26,5 s; se ajusta cuando exista la voz, siempre en múltiplos de 0,5 s)
- **Resolución de borrador:** 540x960 a 30 fps, prueba de 5 s con un fotograma por pulso (render propio)
- **Resolución final:** 1080x1920 a 30 fps, 795 fotogramas
- **Precio por segundo:** 0 (render propio; no hay servicio de pago)
- **Intentos estimados por toma:** 1
- **Versión:** 1 (borrador de especificación; voz sin generar)

## 2. Elenco

| Personaje | Papel en este video | Vestuario | Referencia que se sube |
|---|---|---|---|
| @tan | Abre el video con la pregunta nostálgica y con el mando en la mano; reacciona a cada dato (una reacción por dato), pregunta cuánto fue la espera y dice «Wow, that long?». Lado izquierdo del cuadro con `espejo=True` (en el centro cuando está sola). | base de su ficha (rodete y bufanda mostaza); objeto de mano `control` en la toma 2 | personajes/tan/referencias/principal_tin_y_tan.png |
| @tin | Hace la cuenta paso a paso y da el remate. Lado derecho del cuadro, sin espejo; objeto de mano `calendario` en las tomas 4 y 12 (lápiz en el resto). | base de su ficha (gorra marrón, lentes, lápiz) | personajes/tin/referencias/principal_tin_y_tan.png |

No se sube nada a un generador: las referencias son las del diseño en código (`herramientas/palitos.py`, versión 1.1) y se usan solo para comparar el resultado. Los objetos de mano `control` y `calendario` son las variaciones aprobadas en las fichas el 2026-11-21 («Objetos de mano por video») y están **pendientes de dibujar** en `palitos.py` (sección 14).

Poses y expresiones usadas (todas existen en `POSES` y `EXPRESIONES` de `palitos.py`, comprobado el 2026-11-21): poses `parado`, `saluda`, `senala`, `piensa`, `celebra`, `encoge`, `explica`, `pregunta`; expresiones `feliz`, `nostalgia`, `curiosidad`, `pensando`, `concentrado`, `sorpresa`, `risa`, `eureka`. No se inventa ningún rasgo.

## 3. Idea en una línea

Tan pregunta «¿te acuerdas de comprar GTA 5 a medianoche?» y Tin hace la cuenta real, un dato por plano y sobre papel crema: 13 años, 4.745 días, 3 días bisiestos, 63 días más, 4.811 días de espera hasta GTA 6, y el remate cierto: quien nació ese día ya es adolescente. Nostalgia que termina en sorpresa; el que espera lo comparte («no puede ser tanto»).

**Decidido por el equipo el 2026-11-21** (razones en `00_brief.md`):

1. Ángulo único: los días entre los lanzamientos de GTA V y GTA VI, con dos fechas firmes (fuente: Wikipedia en inglés, leída el 2026-11-21; la de GTA VI no se pudo comprobar en el sitio de Rockstar, y la descripción lo dice).
2. Objetivo comercial: presencia y línea base de retención; sin llamado a la acción. Público: EE. UU., de 30 a 50 años.
3. Solo se **nombra** el juego («GTA 5», «GTA 6» en la tipografía del canal). Nada de Rockstar ni de Take-Two: ni logotipo, ni letra del logo, ni paleta rosa neón, ni personajes, ni mapa, ni autos, ni armas, ni policía, ni violencia.
4. Datos y descargo: solo los de la tabla «Datos del video» del brief, y el descargo «Not affiliated with Rockstar Games or Take-Two Interactive.» en la descripción.

Verificación de la cuenta (2026-11-21, con `datetime` de Python): 17-sep-2013 a 17-sep-2026 = 4.748 días; 13 × 365 = 4.745; días bisiestos entre medias: 29-feb de 2016, 2020 y 2024 = 3; 17-sep-2026 a 19-nov-2026 = 13 + 31 + 19 = 63; 4.748 + 63 = **4.811**; del 17-sep-2013 al 19-nov-2026 hay 4.811 días.

## 4. Estilo global

```text
Flat 2D vector drawing on warm cream paper (#F3E9D2), 1970s palette (orange, brown, teal, mustard, tomato red), thick dark ink outlines (#2B2420), hand-made stick-figure look, no gradients, no soft shadows, no glow, no lens effects, crisp anti-aliased lines (supersampled), spring-based motion, static flat camera with small push-ins.
```

**Negativo global:**

```text
text inside the drawing other than the table in section 12, brand names or logos, Rockstar Games or Take-Two logos or lettering, neon pink and purple poster palette, game characters, game maps, cars, weapons, police, violence, watermark, gradients, drop shadows, glow, lens flare, blue and orange cinematic grade, extra characters, extra fingers, characters other than Tin and Tan, uppercase centered titles, square placeholder glyphs, symbols that are not in the font
```

## 5. Escenarios

- **papel_crema:** fondo plano `#F3E9D2` en todos los planos, sin degradado ni textura. Cuando hay personajes, una línea de suelo `#E6D8B8` de 4 px a **86 % del alto (y = 1651 px)**, de 9,3 % a 90,7 % del ancho. Los planos solo de objeto no llevan suelo.
- **Lienzo y zonas (1080x1920):** zona segura de `formatos.md`: x de 100 a 980 px (9,3 % a 90,7 %), y de 250 a 1670 px (13 % a 87 %). Zona de texto fija: arriba a la izquierda, texto alineado a la izquierda en x = 10 % (108 px). Personajes: **pies a 86 %**, `alto` = 34 % (653 px), cabeza más alta a **52 %**; cuando hay uno solo en plano medio, `alto` = 44 % (845 px), cabeza a 42 %. Cifra principal al 7 % del alto (134 px) con su caja de y = 13,2 % a 20,2 %; **zona de gráficos de 27 % a 51 %** (460 px de alto, de x = 100 a 980 px), centro vertical en 39 %. Los personajes nunca pisan la zona de texto ni la de gráficos.
- **Lados:** Tan en x = 30 % (324 px) con `espejo=True`; Tin en x = 70 % (756 px) sin espejo; cada uno gesticula hacia afuera. Solos, en x = 50 %.
- **mando (gráfico propio, ancho W; es el objeto del gancho):** mando de videojuego **genérico**, sin logotipos ni la forma exacta de ningún mando comercial. Cuerpo: rectángulo redondeado de W × 0,40 W (radio 0,16 W). Dos empuñaduras: círculos de radio 0,16 W con centro en (menos 0,34 W, más 0,19 W) y (más 0,34 W, más 0,19 W) respecto al centro del cuerpo; el contorno exterior (cuerpo más empuñaduras) mide W × 0,55 W (a W = 864 px: 864 × 475 px). Relleno mostaza `#E8B33B`, contorno tinta `#2B2420` de 0,012 W (10 px a W = 864). Dos palancas: círculos tinta de radio 0,07 W con un círculo interior `#E6D8B8` de 0,035 W, en (menos 0,24 W, más 0,02 W) y (más 0,12 W, más 0,14 W). Cuatro botones: puntos tinta de radio 0,028 W en rombo, centrados en (más 0,26 W, menos 0,05 W) y separados 0,06 W en cada eje. Sin letras ni símbolos en los botones. Cuando «late» (golpe de pulso), el botón de abajo del rombo pasa a tomate `#C8553D` durante 0,2 s.
- **mando en la mano (`control`):** el mismo dibujo a 1,1 R × 0,6 R (R = radio de cabeza del personaje) con las dos palancas y los cuatro botones de punto; sustituye al lápiz en la mano que gesticula.
- **calendario, hoja (gráfico propio, ancho W y alto H):** hoja con rectángulo redondeado (radio 0,03 W), relleno blanco `#FFF8EC` y contorno tinta de 0,012 W; **cabecera tomate** `#C8553D` de 0,22 H de alto en la parte de arriba; dos anillas de radio 0,02 W (relleno papel, contorno tinta) en x de menos 0,25 W y más 0,25 W sobre el borde superior; detrás, dos hojas más en `#E6D8B8` desplazadas 14 px hacia abajo (la pila). La fecha va en el cuerpo, alineada a la izquierda con 0,07 W de margen, centrada verticalmente en el cuerpo. **Pasar de hoja:** la hoja gira sobre su borde de arriba: la escala vertical baja de 1 a 0 en 0,15 s (muelle `sello`) y la hoja nueva sube de 0 a 1 en 0,15 s con muelle `pop`. Tamaños: hoja grande de la toma 3 (W = 864 px, H = 1000 px, centro en 50 %, 54 %; texto de fecha al 5,5 % del alto); hoja de zona de gráficos de las tomas 4 y 9 (W = 800 px, H = 460 px, centro en 50 %, 39 %; texto de fecha al 4,6 % del alto).
- **calendario en la mano (`calendario`):** hoja de 0,9 R × 1,0 R con cabecera tomate de 0,22 de alto, dos anillas y el número «17» en tinta (fila de la tabla de la sección 12); sustituye al lápiz en la mano que gesticula.
- **tira de 13 años (gráfico propio):** 13 bloques rectangulares de 60 px de ancho y 200 px de alto, separados 8 px, de x = 100 a 980 px, centrados en y = 39 % (de 33,8 % a 44,2 %); relleno papel sombra `#E6D8B8` al empezar y marrón `#7A4B2A` al llenarse, contorno tinta de 8 px. Los años bisiestos son los bloques 3, 7 y 11 (años de sept. 2015 a sept. 2016, de 2019 a 2020 y de 2023 a 2024: el 29 de febrero de 2016, 2020 y 2024 cae en cada uno). Marca bisiesta: círculo tomate de radio 18 px (36 px de diámetro) centrado 40 px sobre el bloque. Sin letras.
- **Muelles (masa 1, rigidez, amortiguación), declarados por elemento:** `pop` 220 y 20 (entrada de textos y gráficos, escala de 0,85 a 1); `slide` 120 y 16 (personajes y gráficos que se desplazan); `sello` 320 y 26 (empujes de cámara y vueltas de hoja). Contadores: ease-out cúbico sin muelle, para que el valor nunca pase de su final ni retroceda. Todo depende del número de fotograma (30 fps).
- **mando a pantalla completa (tomas 1 y 13):** el mando de W = 864 px (80 % del ancho), centro en (50 %, 54 %) de x = 108 a 972 px y de 41,7 % a 66,3 % del alto, sin etiquetas. «Retumba»: se balancea ±5 grados con un periodo de 0,5 s, ángulo = 5 × seno(4 pi t) grados (el periodo es un pulso; 26,5 s son 53 periodos exactos, por eso el último fotograma es igual al primero). Estela plana: dos copias del mando en `#E6D8B8` detrás, a los ángulos de t menos 0,04 s y t menos 0,08 s. El botón de abajo late en cada pulso (tomate 0,2 s con muelle `pop`).
- **Transición `borrón`:** corte seco con desenfoque de movimiento horizontal de 18 px en los 2 últimos fotogramas de la toma que sale y en los 2 primeros de la que entra. Cero destellos.

## 6. Tomas

<!--
Todas las tomas son «edición»: dibujo por código. Tiempos al décimo de segundo, del video final (26,5 s).
Cada corte cae en un pulso de 0,5 s. Voz: líneas de la sección 7, con tiempos ESTIMADOS; se reajustan cuando exista la voz.
Los cortes caen antes del inicio estimado de la línea siguiente (de 0,05 a 0,25 s antes).
-->

### Toma 1 — Gancho: el mando, ya retumbando

- **Duración:** 1,5 s (de 0,0 a 1,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** el mando a pantalla completa, de frente (el «mando a pantalla completa» de la sección 5)
- **Cámara:** empuje de 100 % a 106 % centrado en el centro del mando, muelle `sello`; en el fotograma 0 la escala es 100 %
- **Acción:** el mando ya está retumbando en el fotograma 0 (con su estela) y el botón de abajo late en 0,0, 0,5 y 1,0.
- **Audio:** línea 1, Tan (primera parte): "Remember buying G T A five at midnight?" Aquí suena «Remember buying G T A five» (de 0,0 a unos 1,5 s). Golpe 1 de la sección 13.
- **Referencia:** toma 1 del short 1 (objeto a pantalla completa, ya en movimiento)
- **Transición de entrada:** ninguna (primer fotograma; es también el último del bucle). Salida: `borrón` hacia la toma 2.

**Especificación de dibujo:**

- Mando exactamente como lo define la sección 5, con el ángulo de t = 0 (cero grados) y las dos copias de estela. **Sin muelle de entrada ni escala 0,85 en el fotograma 0**: todo está ya en su estado pleno y en movimiento (este fotograma es la portada y el empalme del bucle).
- Texto «GTA 5?» (fila 1 de la tabla de la sección 12) ya entero y quieto en el fotograma 0 (sin `pop`); sale a los 1,4 s.
- Sin personajes ni suelo.

### Toma 2 — Tan recuerda, mando en mano

- **Duración:** 1,0 s (de 1,5 a 2,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio general de Tan sola, de frente
- **Cámara:** empuje lento de 100 % a 102 %
- **Acción:** Tan levanta la mano con el mando mientras acaba la pregunta.
- **Audio:** línea 1, Tan (segunda parte): "Remember buying G T A five at midnight?" Aquí suena «at midnight?» (de unos 1,5 a 2,35 s).
- **Referencia:** toma 2 del short 1 (Tan recuerda)
- **Transición de entrada:** `borrón` desde la toma 1. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `pregunta`, expresión `nostalgia`, vista `frente`, `mira=1`, `espejo=True`, x = 50 %, pies a 86 %, `alto` 34 %, `objeto="control"` (mando en la mano que gesticula), `viento` oscilando de menos 0,3 a 0,3 con muelle.
- Sin gráficos y sin texto (el «GTA 5?» ya salió a los 1,4). Con suelo.

### Toma 3 — La hoja de calendario pasa de 2013 a 2026

- **Duración:** 2,5 s (de 2,5 a 5,0)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** subjetivo: la hoja de calendario grande, de frente, llenando el ancho útil
- **Cámara:** empuje de 100 % a 106 %, muelle `sello`
- **Acción:** la hoja dice «Sep 17, 2013» y a los 3,9 s pasa de hoja y queda en «Nov 19, 2026».
- **Audio:** línea 2, Tan: "So, how many days did we wait for G T A six?" (de 2,55 a unos 5,05 s, estimado).
- **Referencia:** toma 3 del short 1 (subjetivo del objeto)
- **Transición de entrada:** `borrón` desde la toma 2. Salida: corte seco.

**Especificación de dibujo:**

- Hoja de calendario grande de la sección 5 (W = 864 px, H = 1000 px, centro 50 %, 54 %). «Sep 17, 2013» entra con `pop` en 2,5 y se queda hasta 3,9; la vuelta de hoja de 3,9 a 4,2; «Nov 19, 2026» de 4,2 a 4,9 (filas de la tabla de la sección 12).
- Texto «how many days?» entra en 2,7 y sale en 4,9. La hoja nunca toca la zona de texto (empieza en 28 % del alto).
- Sin personajes ni suelo.

### Toma 4 — Dato 1: GTA 5 salió el 17 de septiembre de 2013

- **Duración:** 3,5 s (de 5,0 a 8,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos, con la hoja de fecha en la zona de gráficos
- **Cámara:** empuje lento de 100 % a 103 %
- **Acción:** Tin sostiene un calendario y explica; Tan, nostálgica, saluda; la hoja de la zona de gráficos dice «Sep 17, 2013».
- **Audio:** línea 3, Tin: "G T A five came out September seventeenth, twenty thirteen." (de 5,25 a unos 8,35 s, estimado).
- **Referencia:** toma 5 del short 1
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 5.

**Especificación de dibujo:**

- Tan (reacción al dato «2013»): pose `saluda`, expresión `nostalgia`, vista `frente`, x = 30 %, `espejo=True`, pies a 86 %, `alto` 34 %, `viento` con muelle.
- Tin: pose `explica`, expresión `feliz`, vista `frente`, x = 70 %, sin espejo, `objeto="calendario"`; el calendario de su mano tiene movimiento secundario de más o menos 3 grados con muelle.
- Hoja de calendario de la sección 5 (W = 800 px, H = 460 px, centro 50 %, 39 %, de 27 % a 51 %) con «Sep 17, 2013» dentro.
- Texto «GTA 5» al 7 % de 5,1 a 6,4; después, la fecha queda en la hoja hasta 8,4. «17» en el calendario de la mano de Tin (fila de la tabla).

### Toma 5 — Dato 2: 13 años por 365

- **Duración:** 2,0 s (de 8,5 a 10,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle: la tira de 13 años a todo el ancho útil, con Tan debajo
- **Cámara:** fija
- **Acción:** los 13 bloques se llenan de marrón de izquierda a derecha, uno cada 0,1 s; Tan señala la tira.
- **Audio:** línea 4, Tin (primera parte): "Thirteen years times three sixty-five: four thousand, seven hundred forty-five days." Aquí suena «Thirteen years times three sixty-five:» (de 8,55 a unos 10,3 s, estimado).
- **Referencia:** toma 6 del short 1
- **Transición de entrada:** `borrón` desde la toma 4. Salida: corte seco.

**Especificación de dibujo:**

- Tira de 13 años de la sección 5, llenado de 8,7 a 10,0 (cada bloque con muelle `pop`).
- Tan (reacción al dato «13 años»): pose `senala`, expresión `concentrado`, vista `frente`, x = 50 %, `espejo=True`, pies a 86 %, `alto` 34 %.
- Texto «13 × 365» al 7 % de 8,7 a 10,4 (clave: 13). Con suelo.

### Toma 6 — Dato 3: 4.745 días

- **Duración:** 2,0 s (de 10,5 a 12,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la misma tira ya llena, con un corchete tomate que la abarca, y Tan debajo
- **Cámara:** fija
- **Acción:** el contador sube de 0 a 4.745; Tan se asombra.
- **Audio:** línea 4, Tin (segunda parte): "Thirteen years times three sixty-five: four thousand, seven hundred forty-five days." Aquí suena «four thousand, seven hundred forty-five days.» (de unos 10,5 a 12,55 s, estimado).
- **Referencia:** toma 7 del short 1 (contador que sube)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Tira de la toma 5 con los 13 bloques marrón y un corchete tomate de 10 px de grosor que la abarca de x = 100 a 980 px, a 4 % por debajo de la tira, sin letras.
- Tan (reacción al dato «4.745»): pose `pregunta`, expresión `sorpresa`, vista `frente`, x = 50 %, `espejo=True`, `viento` alto con muelle.
- Contador de 0 a 4.745 (enteros) con ease-out cúbico de 10,7 a 12,2; solo sube y al terminar se queda fijo. Texto «4,745 days» al 7 % de 10,6 a 12,4 (clave: el número).

### Toma 7 — Dato 4: 3 días bisiestos

- **Duración:** 1,5 s (de 12,5 a 14,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la tira con tres marcas tomate que aparecen, y Tan debajo
- **Cámara:** fija
- **Acción:** tres círculos tomate aparecen sobre los bloques 3, 7 y 11, uno cada 0,5 s; Tan explica.
- **Audio:** línea 5, Tin (primera parte): "Add three leap days: four thousand, seven hundred forty-eight." Aquí suena «Add three leap days:» (de 12,75 a unos 13,6 s, estimado).
- **Referencia:** toma 10 del short 1 (barra que se divide)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Tira llena de la toma 6 sin el corchete; marcas bisiestas de la sección 5 que entran con muelle `pop` en 12,9, 13,4 y 13,8 (la tercera, antes del corte de 14,0).
- Tan (reacción al dato «3 días bisiestos»): pose `explica`, expresión `curiosidad`, vista `frente`, x = 50 %, `espejo=True`, pies a 86 %, `alto` 34 %.
- Texto «+3 leap days» al 7 % de 12,7 a 13,9 (clave: 3). Con suelo.

### Toma 8 — Dato 5: 4.748 días

- **Duración:** 1,5 s (de 14,0 a 15,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la tira con sus tres marcas y el corchete tomate, y Tan debajo
- **Cámara:** fija
- **Acción:** el contador sube de 4.745 a 4.748 y hace un `pop` de escala solo del texto; Tan se queda pensando.
- **Audio:** línea 5, Tin (segunda parte): "Add three leap days: four thousand, seven hundred forty-eight." Aquí suena «four thousand, seven hundred forty-eight.» (de unos 13,7 a 15,45 s, estimado).
- **Referencia:** toma 7 del short 1
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 9.

**Especificación de dibujo:**

- Tira, tres marcas bisiestas y corchete tomate (de la toma 6).
- Tan (reacción al dato «4.748»): pose `parado`, expresión `pensando`, vista `frente`, x = 50 %, `espejo=True`, pies a 86 %, `alto` 34 %.
- Contador de 4.745 a 4.748 con ease-out cúbico de 14,1 a 15,2; solo sube. Texto «4,748 days» al 7 % de 14,1 a 15,4 (clave: el número).

### Toma 9 — Dato 6: 63 días más

- **Duración:** 3,5 s (de 15,5 a 19,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la hoja de calendario en la zona de gráficos, con Tan debajo
- **Cámara:** empuje lento de 100 % a 102 %
- **Acción:** una pila de hojas en blanco pasa rápido; aparece «Sep 17, 2026», pasa de hoja y queda en «Nov 19, 2026»; Tan piensa.
- **Audio:** línea 6, Tin: "Plus sixty-three days: September seventeenth to November nineteenth." (de 15,65 a unos 18,95 s, estimado).
- **Referencia:** toma 8 del short 1
- **Transición de entrada:** `borrón` desde la toma 8. Salida: corte seco.

**Especificación de dibujo:**

- Hoja de calendario de la sección 5 (W = 800 px, H = 460 px, centro 50 %, 39 %). De 15,5 a 16,6: 6 hojas **en blanco** (sin fecha) pasan de hoja, una cada 0,18 s (para que la zona de gráficos no quede vacía); «Sep 17, 2026» entra con `pop` en 16,6 y se queda hasta 17,9; vuelta de hoja de 17,9 a 18,2; «Nov 19, 2026» de 18,2 a 18,9.
- Tan (reacción al dato «63 días»): pose `piensa`, expresión `pensando`, vista `frente`, x = 50 %, `espejo=True`, pies a 86 %, `alto` 34 %, `objeto=False` (en `piensa` el objeto cruza la cara).
- Contador de 0 a 63 con ease-out cúbico de 15,7 a 17,0, que se queda fijo. Texto «+63 days» al 7 % de 15,7 a 18,1 (clave: 63); después «GTA 6» al 7 % de 18,2 a 18,9 (clave: 6), que dice a qué lanzamiento corresponde la fecha.

### Toma 10 — Dato 7: 4.811 días

- **Duración:** 2,5 s (de 19,0 a 21,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el contador arriba (pico de emoción)
- **Cámara:** empuje de 100 % a 103 %
- **Acción:** el contador sube de 4.748 a 4.811 mientras Tan celebra y Tin levanta el lápiz; al llegar, el número pasa a tomate.
- **Audio:** línea 7, Tin: "Four thousand, eight hundred eleven days." (de 19,15 a unos 21,15 s, estimado).
- **Referencia:** toma 11 del short 1 (contador final y celebración)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `celebra`, expresión `sorpresa`, vista `frente`, x = 30 %, `espejo=True`, `viento` alto con muelle.
- Tin: pose `saluda`, expresión `eureka`, vista `frente`, x = 70 %, sin espejo, `objeto=True` (lápiz).
- Contador en la zona de texto (y = 15 %), tamaño 7 %, de 4.748 a 4.811 con ease-out cúbico de 19,4 a 21,0; al llegar pasa de tinta y mostaza a tomate y hace un `pop` de escala solo del texto (el valor no se pasa). Texto «4,811 days» (fila de la tabla).
- Sin gráfico en la zona de gráficos (el pico es la cifra).

### Toma 11 — Tan se asombra

- **Duración:** 1,0 s (de 21,5 a 22,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tan sola, de frente
- **Cámara:** empuje de 100 % a 106 %
- **Acción:** Tan se encoge de hombros con la boca abierta.
- **Audio:** línea 8, Tan: "Wow, that long?" (de 21,55 a unos 22,35 s, estimado).
- **Referencia:** toma 9 del short 1 (respiro de composición)
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 12.

**Especificación de dibujo:**

- Tan: pose `encoge`, expresión `sorpresa`, vista `frente`, x = 50 %, pies a 86 %, `alto` 44 %, `espejo=True`, `objeto=False`.
- Sin gráficos y sin texto (no hay dato nuevo: repite el de la toma 10, por eso no lleva reacción distinta). Con suelo.

### Toma 12 — Remate: un bebé de ese día ya es adolescente

- **Duración:** 3,0 s (de 22,5 a 25,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos, con la tira de 13 años completa en la zona de gráficos
- **Cámara:** fija
- **Acción:** la tira de 13 años, ya llena, hace latir su último bloque en tomate tres veces; Tin sostiene el calendario y celebra; Tan se ríe.
- **Audio:** línea 9, Tin (remate): "A baby born that day is a teenager now." (de 22,55 a unos 25,2 s, estimado).
- **Referencia:** toma 14 del short 1 (remate con los dos riendo)
- **Transición de entrada:** `borrón` desde la toma 11. Salida: `borrón` hacia la toma 13.

**Especificación de dibujo:**

- Tira de 13 años llena (marrón), con el bloque 13 pasando a tomate con muelle `pop` en 23,1, 23,6 y 24,1, y quedando en tomate hasta el final.
- Tan (reacción al dato «13 años»): pose `encoge`, expresión `risa`, vista `frente`, x = 30 %, `espejo=True`, pies a 86 %, `alto` 34 %.
- Tin: pose `celebra`, expresión `risa`, vista `frente`, x = 70 %, sin espejo, `objeto="calendario"` (con «17» en el calendario de su mano).
- Texto «age 13» al 7 % de 22,7 a 25,4 (clave: 13, en tomate).

### Toma 13 — Cierre en bucle: vuelve el mando

- **Duración:** 1,0 s (de 25,5 a 26,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** el mismo mando a pantalla completa de la toma 1
- **Cámara:** retroceso de 106 % a 100 % centrado en el centro del mando, muelle `sello`; en 26,5 la escala es 100 %
- **Acción:** el mando retumba, ya en el plano exacto del fotograma 0; el último fotograma es igual al primero.
- **Audio:** sin voz (la voz estimada terminó en 25,2: 1,3 s de silencio de voz hasta el empalme; en el fotograma 0 la voz vuelve a entrar sin pausa). Golpes finales de la sección 13.
- **Referencia:** toma 1 de esta versión (cierre en bucle con el plano del inicio)
- **Transición de entrada:** `borrón` desde la toma 12. Salida: bucle al fotograma 0 de la toma 1.

**Especificación de dibujo:**

- Mando y estela de la sección 5, con el ángulo de la fórmula (5 × seno(4 pi t) grados); en 26,5 el ángulo es 0 y la escala 100 %: **el fotograma 795 (el último) es igual al fotograma 0**.
- Texto «GTA 5?» entra con `pop` en 25,6 y está a escala 1 en 26,5; sigue sin corte en la toma 1 del bucle (de 0,0 a 1,4).

## 7. Audio

- **Voz (SIN GENERAR):** Tan con Zelda (líneas 1, 2 y 8) y Tin con Kevin (líneas 3 a 7 y 9), Higgsfield `seed_audio`, **una sola generación por voz** (regla de un solo intento), al 110 % con `atempo=1.10` y normalizada a −14 LUFS. Costo: **por cotizar con `estimate_audio_cost`; necesita el sí del dueño** antes de generar.
- **Los tiempos de la voz son ESTIMADOS** (la voz no existe todavía). Método: el ritmo medido en el short 1 (`05_audio/linea_de_tiempo_voz_v2.md`, voces al 110 %): unas 5,0 a 5,3 sílabas por segundo dentro de una frase (línea 1: 13 sílabas en 2,44 s; línea 3: 13 en 2,50 s; línea 5: 13 en 2,61 s) y unos 0,2 s de pausa entre líneas. Cuando exista la voz, se miden las pausas reales, se reajustan los cortes a la rejilla de 0,5 s (siempre antes de la línea siguiente y sin cortar palabras) y se recalcula la duración del video.

Guion de voz (líneas numeradas, quién habla, texto exacto, inicio y fin estimados):

| Línea | Quién | Empieza (s) | Termina (s) | Dura (s) | Texto exacto (números como se dicen) | Sílabas |
|---|---|---|---|---|---|---|
| 1 | Tan | 0,00 | 2,35 | 2,35 | Remember buying G T A five at midnight? | 12 |
| 2 | Tan | 2,55 | 5,05 | 2,50 | So, how many days did we wait for G T A six? | 13 |
| 3 | Tin | 5,25 | 8,35 | 3,10 | G T A five came out September seventeenth, twenty thirteen. | 16 |
| 4 | Tin | 8,55 | 12,55 | 4,00 | Thirteen years times three sixty-five: four thousand, seven hundred forty-five days. | 21 |
| 5 | Tin | 12,75 | 15,45 | 2,70 | Add three leap days: four thousand, seven hundred forty-eight. | 14 |
| 6 | Tin | 15,65 | 18,95 | 3,30 | Plus sixty-three days: September seventeenth to November nineteenth. | 17 |
| 7 | Tin | 19,15 | 21,15 | 2,00 | Four thousand, eight hundred eleven days. | 10 |
| 8 | Tan | 21,55 | 22,35 | 0,80 | Wow, that long? | 3 |
| 9 | Tin | 22,55 | 25,20 | 2,65 | A baby born that day is a teenager now. | 12 |

Voz total estimada: de 0,0 a 25,2 s; hasta 26,5 hay 1,3 s sin voz y al volver al fotograma 0 la voz entra otra vez sin silencio inicial (silencio total del empalme del bucle: 1,3 s, menos de 2 s).

**Texto para generar cada voz (una pieza por personaje; las líneas van separadas por una línea en blanco; «G T A» se lee letra por letra):**

Voz de Tan (Zelda), una sola generación, 3 líneas:

```text
Remember buying G T A five at midnight?

So, how many days did we wait for G T A six?

Wow, that long?
```

Voz de Tin (Kevin), una sola generación, 6 líneas:

```text
G T A five came out September seventeenth, twenty thirteen.

Thirteen years times three sixty-five: four thousand, seven hundred forty-five days.

Add three leap days: four thousand, seven hundred forty-eight.

Plus sixty-three days: September seventeenth to November nineteenth.

Four thousand, eight hundred eleven days.

A baby born that day is a teenager now.
```

Los cortes de cada pieza en líneas se hacen por las pausas medidas, como en el short 1, y se comprueban al oído antes de publicar. Si el generador lee mal «G T A», se corrige en edición (gratis) o se pide autorización al dueño para regenerar esa voz; no se regenera por cuenta propia.

- **Subtítulos:** `02_prompt/subtitulos.srt` con los tiempos estimados (se reajustan junto con la voz).
- **Música:** hecha con código (Python y numpy), patrón de 120 BPM (el pulso de la rejilla) a −24 LUFS, 10 dB por debajo de la voz, anotada en `licencias.md`. Debe cubrir 26,5 s y cerrar su fase en el pulso para el bucle (53 pulsos). Sin música de terceros ni del juego.
- **Efectos:** los de la sección 13, hechos con código, sin material de terceros.

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → Toma 3 → Toma 4 → Toma 5 → Toma 6 → Toma 7 → Toma 8 → Toma 9 → Toma 10 → Toma 11 → Toma 12 → Toma 13 (y vuelve a la toma 1). Las tomas 1 y 13 son el mismo plano.
- **Transiciones:** corte seco; entre planos de objeto o de cámara distinta, el `borrón` de la sección 5 (1→2, 2→3, 4→5, 8→9, 11→12 y 12→13, como dicen las tomas). Sin destellos, sin fundidos.
- **Texto en pantalla:** se dibuja en el mismo render, solo el de la tabla de la sección 12. El texto nunca contradice lo que se oye.
- **Portada:** el fotograma 0 (o el de 0,5 s, que es el mismo plano): el mando con el «GTA 5?». Alternativa para probar en otra publicación: el fotograma de 21,0 s (el «4,811 days» en tomate con los dos celebrando).
- **Formato de salida:** 1080x1920, 30 fps, H.264, yuv420p, AAC a 48 kHz. Archivo `06_final/tin_y_tan_short02_v1.mp4`.
- **Título de la publicación (inglés):** How many days did we wait for GTA 6?
- **Descripción de la publicación (en inglés, obligatoria; sin llamado a la acción):**

```text
How many days did we wait for GTA 6? Step by step:

GTA 5 came out on Sep 17, 2013 (original PlayStation 3 and Xbox 360 release). GTA 6 came out on Nov 19, 2026.
Sep 17, 2013 to Sep 17, 2026 is 13 years: 13 x 365 = 4,745 days.
Add 3 leap days (Feb 29 of 2016, 2020 and 2024): 4,748 days.
Sep 17 to Nov 19, 2026: 13 + 31 + 19 = 63 more days.
4,748 + 63 = 4,811 days.
A baby born that day is a teenager now.

Release dates: Wikipedia, "Grand Theft Auto V" and "Grand Theft Auto VI", read on 2026-11-21. The GTA 6 date was not checked on the publisher's website.
Not affiliated with Rockstar Games or Take-Two Interactive.
```

- **Sin llamado a la acción** (ni en el video ni en la descripción): el objetivo es presencia y línea base, y un llamado al final cortaría el bucle.
- **Fechas y fuentes:** Grand Theft Auto V, 17 de septiembre de 2013 (PlayStation 3 y Xbox 360) y Grand Theft Auto VI, 19 de noviembre de 2026 (PlayStation 5 y Xbox Series X/S): Wikipedia en inglés, páginas «Grand Theft Auto V» y «Grand Theft Auto VI», abiertas y leídas el 2026-11-21. La de GTA VI no se leyó en Rockstar Games (sitio sin acceso).

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | 0 s (las 13 tomas son edición; 26,5 s se resuelven en edición) | 0 |
| Keyframes | 0 | 0 |
| Remates en resolución final | 0 | 0 |
| Voz (Tan con Zelda y Tin con Kevin, una generación por voz) | 2 generaciones | por cotizar con `estimate_audio_cost`; necesita el sí del dueño |
| **Total estimado** | 0 créditos en imagen y video; voz por cotizar, necesita el sí del dueño | 0 |

## 10. Restricciones críticas

Van al inicio de cada prompt de video, antes de la descripción. Son las que no se negocian.

```text
CRITICAL: no text, captions, subtitles, logos or watermarks unless listed in section 12.
CRITICAL: the character looks identical in every shot (same design, colors, proportions).
CRITICAL: hard cuts only, no morphing between shots.
CRITICAL: every figure, name or claim on screen comes from the project's facts file, with source and date.
CRITICAL: counters only go up and never pass their final value; no text over a character; nothing from Rockstar Games or Take-Two Interactive (logo, lettering, neon pink palette, characters, map, cars, weapons, police, violence); the controller is generic and has no logos.
```

## 11. Gancho, ritmo y cierre

- **Regla formal de la pieza:** un solo dato por plano, sobre el mismo papel crema, y la cuenta solo sube; todo corte cae en un pulso de 0,5 s, que es lo que dura un balanceo del mando.
- **Rejilla de tiempo:** pulso de 0,5 s (120 BPM, compás de 4 pulsos = 2,0 s); 53 pulsos = 26,5 s (13 compases y 1 pulso). La voz entra en el pulso 0 (fotograma 0). Los 12 cortes caen en 1,5; 2,5; 5,0; 8,5; 10,5; 12,5; 14,0; 15,5; 19,0; 21,5; 22,5 y 25,5 (más el bucle en 26,5). Inicios de la voz **estimados**: 0,00; 2,55; 5,25; 8,55; 12,75; 15,65; 19,15; 21,55; 22,55. Cada corte entre líneas cae de 0,05 a 0,25 s antes de la línea siguiente; los cortes dentro de una línea (1,5; 10,5 y 14,0) están estimados por sílabas y se afinan al oído cuando exista la voz. El corte de 19,0 deja solo 0,05 s de margen sobre la voz estimada: es el primero que se revisa.
- **Gancho (0 a 2,5 s):** el fotograma 0 es el mando a pantalla completa, ya retumbando (con estela), con «GTA 5?» ya entero (clave: 5, en mostaza), que sale a los 1,4 s, y la voz de Tan ya diciendo «Remember buying G T A five…» desde el fotograma 0. En 1,5 el `borrón` pasa a Tan con el mando en la mano y, en 2,5, a la hoja de calendario que pasa de 2013 a 2026. Sin logo, sin título, sin segundo mudo. Gancho B para otra publicación (se renderiza gratis): el mismo plano con el texto «4,811 days?».
- **Empieza en movimiento:** sí: sin intro ni logo; el mando retumba y el botón de abajo late desde el fotograma 0, a tamaño completo.
- **Motivo visual que vuelve:** el mando (tomas 1, 2 y 13), la hoja de calendario (tomas 3, 4, 9 y 12, y el calendario en la mano de Tin), la tira de 13 años (tomas 5 a 8 y 12) y el lápiz amarillo de Tin. Se repiten con las mismas formas y colores.
- **Cierre:** el video vuelve al plano exacto del fotograma 0 (mando a pantalla completa, ángulo 0, escala 100 %, «GTA 5?» ya entero) y encadena en bucle con la toma 1: el último fotograma es el primero. Cierre de 1,0 s (de 25,5 a 26,5); la voz estimada termina en 25,2; silencio de voz en el empalme: 1,3 s (menos de 2 s).
- **Llamado a la acción:** ninguno. Por qué: el objetivo comercial es presencia y línea base de retención; el canal todavía no existe y un llamado al final cortaría el bucle.

Mapa de ritmo (los tiempos al décimo de segundo; cortes por segundo = cortes que caen dentro del tramo, sin contar el inicio):

| Tramo | Segundos | Pulso o intervalo | Cortes por segundo | Qué pasa (una acción) | Respiro |
|---|---|---|---|---|---|
| Gancho | 0,0–2,5 | 1,5 s y 1,0 s | 0,8 | el mando retumba, Tan recuerda con el mando en la mano | no |
| Pregunta | 2,5–5,0 | 2,5 s | 0,4 | la hoja de calendario pasa de 2013 a 2026 | sí |
| Dato 1 | 5,0–8,5 | 3,5 s | 0,3 | GTA 5 salió el 17 de septiembre de 2013; Tan saluda | sí |
| Cuenta | 8,5–15,5 | 2,0 s, 2,0 s, 1,5 s y 1,5 s | 0,6 | 13 años, 4.745 días, 3 bisiestos, 4.748 | no |
| Fechas | 15,5–19,0 | 3,5 s | 0,3 | 63 días de septiembre a noviembre; héroe: la hoja pasa a «Nov 19, 2026» | no |
| Pico | 19,0–21,5 | 2,5 s | 0,4 | contador hasta 4.811 y celebración | no (pico de emoción) |
| Remate | 21,5–25,5 | 1,0 s y 3,0 s | 0,5 | «Wow, that long?» y el bebé de ese día es adolescente | no (acelera al principio) |
| Cierre | 25,5–26,5 | 1,0 s | 0 | vuelve el mando del primer fotograma | sí |

Total: 12 cortes en 26,5 s. Es una densidad baja a propósito, igual que en el short 1: la voz es continua y cada cifra necesita su plano; la densidad extra va dentro de cada toma (contadores que suben, hojas que pasan, bloques que se llenan, una reacción de Tan por dato, el mando que late a cada pulso).

Lo que sale se va antes de que entre lo siguiente: los textos salen de 0,1 a 0,2 s antes del corte siguiente (el texto 1, a los 1,4 s) y los gráficos con el borrón. El movimiento es mecánica: entradas con `pop` o `slide` (muelle), contadores con ease-out cúbico, el balanceo del mando con un seno de periodo 0,5 s, sin interpolación lineal.

Tipos de plano disponibles y dónde van: detalle o macro (tomas 5 a 8), héroe abierto (tomas 4, 10 y 12; el héroe principal es la 10, con la cifra final, hacia el final del arco), subjetivo y mando a pantalla completa (tomas 1, 3 y 13), revelado (la hoja que pasa de 2013 a 2026 en la toma 3), objeto que salta sobre el mismo fondo (las marcas bisiestas de la toma 7 y el bloque 13 de la toma 12). Transiciones siempre motivadas (borrón de movimiento). **No más de 3 destellos por segundo:** hay cero (el botón que late es un cambio de color de 0,2 s, no un destello; son 2 por segundo como máximo).

## 12. Texto en pantalla y sistema de diseño

- **Tipografías:** Inter Display Medium, licencia SIL Open Font License 1.1 (archivo `/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf`; en Windows, si no está, Segoe UI Semibold, que se anota en `licencias.md` antes de usarla). Siempre en minúsculas cuando es subtítulo, alineadas a la izquierda; las siglas «GTA» y las fechas («Sep», «Nov») conservan su mayúscula inicial porque son nombres propios. No se usa la tipografía de ningún logotipo del juego.
- **Paleta:** papel `#F3E9D2` · papel_sombra `#E6D8B8` · tinta `#2B2420` · naranja `#E07A2E` · marrón `#7A4B2A` · verde azulado `#2F7F7A` · mostaza `#E8B33B` (palabra clave de los subtítulos; relleno del mando) · tomate `#C8553D` (cifra final, cabecera del calendario, marcas bisiestas, alertas) · rubor `#E9967A` · blanco `#FFF8EC`. Un color de acento por plano. La palabra clave en mostaza lleva un trazo de tinta de 0,06 em. Ninguna paleta rosa neón ni morada.
- **Referencias de movimiento:** `01_referencia/` está vacía (no hay video de referencia). Las referencias cargadas son `canales/nostalgia-tin-y-tan/DESIGN.md`, `herramientas/palitos.py`, las hojas de `personajes/tin/referencias/` y `personajes/tan/referencias/` y el prompt del short 1; el movimiento lo definen los muelles de la sección 5.
- **Prohibido:**
  1. Mayúsculas centradas sobre degradado, tarjetas con degradado o cualquier fondo con degradado.
  2. Animaciones lineales de posición o escala (solo muelle o ease-out cúbico; la única repetición uniforme es el balanceo del mando).
  3. Los símbolos «≈» y «→» y cualquier glifo sin comprobar. **Antes de renderizar se comprueba que la fuente trae «×», «+», «?», «,», «.» y «:»** (en el short 1 se comprobó «÷»; «×» y «+» no están comprobados). Si «×» faltara, «13 x 365» con la letra x.
  4. Un contador que retrocede o que se pasa de su valor final y vuelve (nada de rebote en el valor; el rebote solo es de escala).
  5. Texto encima de un personaje, del mando o de la tira. Excepción: la fecha de la hoja de calendario y el «17» del calendario de la mano son el contenido de ese objeto.
  6. Cualquier elemento de Rockstar Games o de Take-Two Interactive: logotipo, letra del logo, paleta rosa neón, personajes, mapa, autos, armas, policía, violencia, música o metraje del juego.
  7. Líneas sin suavizar: ningún dibujo fuera de un `Lienzo` con supermuestreo.
  8. Sombras suaves, resplandor, partículas, confeti y luz azul y naranja sin motivo (la estela del mando es plana, sin degradado ni desenfoque).
  9. Subtítulos de más de 3 palabras, de más de una línea o fuera de la zona segura.
  10. Cualquier pose, expresión o vista que no esté en `palitos.py`, y cambiar los colores o accesorios de Tin y Tan (solo cambia el objeto de la mano, como dicen sus fichas).
  11. Un mando que copie la forma de un mando comercial, o con símbolos en los botones.
- **Márgenes seguros y escenario:** zona segura de `formatos.md`: x de 9,3 % a 90,7 % y y de 13 % a 87 %. El contenido ocupa el centro de 880x1420 px. Texto en x = 10 % y de 13,2 % a 24 %; personajes con pies a 86 % y cabeza desde 52 % (42 % en el plano medio de uno solo); gráficos entre 27 % y 51 % cuando hay personajes.
- **Texto exacto:** todo texto en pantalla es el de la tabla de abajo, letra por letra. Los contadores muestran enteros entre su valor de inicio y su valor final.
- **No afirmar:** ninguna cifra ni dato fuera de la tabla «Datos del video» del brief, verificados el 2026-11-21:
  - **17 de septiembre de 2013** (lanzamiento de GTA V en PlayStation 3 y Xbox 360) y **19 de noviembre de 2026** (lanzamiento de GTA VI), según Wikipedia en inglés, leída el 2026-11-21; la de GTA VI no se leyó en Rockstar Games.
  - **13 años; 13 × 365 = 4.745; 3 días bisiestos (2016, 2020, 2024); 4.748; 63 días (13 + 31 + 19); 4.811 días** (comprobado con `datetime`).
  - **Quien nació ese día tiene 13 años y es adolescente** (aritmética).
  - No decir ni mostrar: ventas, vistas de tráileres, clasificación por edades, motivos de los retrasos, número de retrasos, contenido del juego, plataformas distintas de las del brief, «most anticipated», «biggest», «record» ni ningún superlativo; tampoco «midnight launch» como hecho (el «at midnight?» de Tan es una pregunta, no una afirmación); tampoco quién es el estudio ni sus personajes; ni «GTA 6» con la tipografía del logo.
- **Subtítulos:** de 1 a 3 palabras, con la palabra clave en mostaza (con trazo de tinta); la cifra final «4,811» y «13» del remate pasan a tomate. Las cifras del valle (filas 4 a 12) van al 7 % del alto.

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| GTA 5? (clave: 5; ya entero en el fotograma 0, sin pop) | 0,0 | 1,4 | 10, 15 | 6 |
| how many days? (clave: days) | 2,7 | 4,9 | 10, 15 | 5 |
| Sep 17, 2013 (en la hoja grande, alineado a la izquierda; sin clave) | 2,5 | 3,9 | 14,8, 54 | 5,5 |
| Nov 19, 2026 (en la hoja grande; sin clave) | 4,2 | 4,9 | 14,8, 54 | 5,5 |
| GTA 5 (clave: 5) | 5,1 | 6,4 | 10, 13,2 | 7 |
| Sep 17, 2013 (en la hoja de la zona de gráficos; sin clave) | 5,0 | 8,4 | 18, 41,7 | 4,6 |
| 17 (en el calendario de la mano de Tin; tinta) | 5,0 | 8,4 | sobre la mano de Tin | 3 |
| 13 × 365 (clave: 13) | 8,7 | 10,4 | 10, 13,2 | 7 |
| 4,745 days (contador de 0 a 4,745; clave: el número) | 10,6 | 12,4 | 10, 13,2 | 7 |
| +3 leap days (clave: 3) | 12,7 | 13,9 | 10, 13,2 | 7 |
| 4,748 days (contador de 4,745 a 4,748; clave: el número) | 14,1 | 15,4 | 10, 13,2 | 7 |
| +63 days (contador de 0 a 63; clave: 63) | 15,7 | 18,1 | 10, 13,2 | 7 |
| Sep 17, 2026 (en la hoja de la zona de gráficos; sin clave) | 16,6 | 17,9 | 18, 41,7 | 4,6 |
| Nov 19, 2026 (en la hoja de la zona de gráficos; sin clave) | 18,2 | 18,9 | 18, 41,7 | 4,6 |
| GTA 6 (clave: 6) | 18,2 | 18,9 | 10, 13,2 | 7 |
| 4,811 days (contador de 4,748 a 4,811; al llegar, el número en tomate) | 19,2 | 21,4 | 10, 15 | 7 |
| age 13 (clave: 13, en tomate) | 22,7 | 25,4 | 10, 13,2 | 7 |
| 17 (en el calendario de la mano de Tin; tinta) | 22,5 | 25,4 | sobre la mano de Tin | 3 |
| GTA 5? (clave: 5; entra con pop y sigue sin corte en la fila 1 del bucle) | 25,6 | 26,5 | 10, 15 | 6 |

En un short, todo texto queda dentro de la zona segura de `formatos.md`. Entrada de cada texto: `pop` con escala de 0,85 a 1 en 8 fotogramas; salida: subir 2 % con ease-in en 3 fotogramas (excepción: la fila 1 en el fotograma 0 está ya a escala 1, y la última fila queda a escala 1 en el último fotograma para que el bucle empalme).

## 13. Sonido

Los golpes bajo la voz van a unos **−26 LUFS** (−12 dB respecto a la voz, que está a −14 LUFS; lección de la revisión del short 1: a −38 LUFS no se oían en un teléfono). Se comprueba al oído.

| Golpe o efecto | Segundo | A qué corte va atado | Origen y licencia |
|---|---|---|---|
| Golpe seco grave de 80 ms y zumbido corto de vibración del mando | 0,0 | arranque, toma 1 (es también el empalme del bucle: no se duplica) | código, propio (ver licencias.md) |
| Clic de botón, uno por pulso | 0,5 / 1,0 | latidos del botón de la toma 1 | código, propio |
| Clic suave de borrón | 1,5 | corte de toma 1 a toma 2 | código, propio |
| Clic suave de borrón | 2,5 | corte de toma 2 a toma 3 | código, propio |
| Papel que pasa de hoja (tic corto) | 3,9 | vuelta de hoja de la toma 3 | código, propio |
| Clic suave | 5,0 | corte de toma 3 a toma 4 | código, propio |
| Clic suave de borrón | 8,5 | corte de toma 4 a toma 5 | código, propio |
| Tic de bloque que se llena, 13 veces, subiendo de tono | 8,7–10,0 | llenado de la tira en la toma 5 | código, propio |
| Tictac de contador que sube de tono | 10,7–12,2 | contador de la toma 6 | código, propio |
| Pop de marca bisiesta | 12,9 / 13,4 / 13,8 | marcas bisiestas de la toma 7 | código, propio |
| Clic suave | 14,0 | corte de toma 7 a toma 8 | código, propio |
| Tictac de contador (3 pasos) | 14,1–15,2 | contador de la toma 8 | código, propio |
| Clic suave de borrón | 15,5 | corte de toma 8 a toma 9 | código, propio |
| 6 tics de hoja en blanco | 15,5–16,6 | pila de hojas de la toma 9 | código, propio |
| Papel que pasa de hoja (tic corto) | 17,9 | vuelta de hoja de la toma 9 | código, propio |
| Clic suave | 19,0 | corte de toma 9 a toma 10 | código, propio |
| Tictac de contador que sube de tono | 19,4–21,0 | contador de la toma 10 | código, propio |
| Ding de campana al llegar a 4,811 | 21,0 | valor final de la toma 10 | código, propio |
| Clic suave | 21,5 | corte de toma 10 a toma 11 | código, propio |
| Clic suave de borrón | 22,5 | corte de toma 11 a toma 12 | código, propio |
| Pop del bloque 13 en tomate (3) | 23,1 / 23,6 / 24,1 | latidos de la toma 12 | código, propio |
| Clic suave de borrón | 25,5 | corte de toma 12 a toma 13 | código, propio |
| Whoosh suave de retroceso de cámara | 25,5–26,3 | retroceso de la toma 13 | código, propio |
| Clic de botón, uno por pulso | 25,5 / 26,0 | latidos del botón de la toma 13 | código, propio |
| Thunk grave idéntico al del segundo 0,0 (cierra el bucle; el del 0,0 lo continúa) | 26,5 | bucle: último golpe igual al primero | código, propio |

- **Música:** hecha con código a −24 LUFS (ver sección 7); sin material de terceros ni del juego.
- **Voz:** sí (por generar; ver sección 7). Sin retraso: empieza en el fotograma 0.

## 14. Motor y revisión

- **Cómo se hace:** gráficos por código (fotograma a fotograma): Python, Pillow y ffmpeg. Cada fotograma se dibuja en un `Lienzo(1080, 1920)` de `palitos.py`, que ya dibuja al triple de tamaño y reduce con LANCZOS (supermuestreo). Los empujes de cámara recortan el lienzo grande y reducen. Todo depende del número de fotograma, no del reloj. Se guardan PNG numerados y ffmpeg los une con la voz y los efectos (`postpro.py mezclar` o ffmpeg directo). Personajes con `palitos.dibujar(lz, id, x, suelo, alto, pose, expresion, vista, mira, viento, objeto, espejo)`.
- **Qué hay que añadir a `palitos.py` (versión 1.1 → 1.2) antes de renderizar; lo hace quien renderice, no este prompt:**
  1. `objeto="control"`: hoy `objeto` solo conoce el lápiz y se usa como verdadero o falso. Hay que aceptar un nombre de objeto (`"lapiz"`, `"control"`, `"calendario"`; `True` sigue significando el objeto icónico del personaje y `False` ningún objeto) y dibujar el `control` en la mano que gesticula, con las medidas de la sección 5 (1,1 R × 0,6 R, dos palancas, cuatro botones de punto, mostaza, contorno tinta; también para Tan, que no tiene objeto icónico).
  2. `objeto="calendario"`: hoja de 0,9 R × 1,0 R con cabecera tomate (0,22), dos anillas y el número «17» en tinta, con la misma regla de ángulo que el lápiz para las poses `saluda`, `celebra` y `pregunta`.
  3. Gráfico `mando(lz, cx, cy, ancho, angulo, boton_pulsado, estela)` para el mando a pantalla completa (sección 5).
  4. Gráfico `hoja_calendario(lz, cx, cy, ancho, alto, texto, vuelta)` para la hoja grande y la de la zona de gráficos, con la vuelta de hoja (escala vertical y muelles `sello` y `pop`) y la pila de hojas.
  5. Gráfico `tira_13(lz, llenos, marcas, corchete, ultimo_tomate)` para la tira de 13 años.
  6. Comprobar los glifos «×», «+» y «:» en la fuente, y regenerar las hojas `referencias/poses.png` solo si cambia alguna pose (no cambia ninguna).
  Costo en créditos: 0.
- **Quién renderiza y autorización:** el render lo hace el equipo de producción. **Pendiente de autorización del dueño**: la voz (por cotizar) y el render. Hasta que la voz exista no se renderiza el video final: los tiempos de este prompt son estimados. Antes de renderizar se crea `03_keyframes/definicion.md` con la entrada de «pieza por código» de `generacion.md` (datos con fuente, paleta con HEX, tipografía y licencia, texto exacto, 26,5 s a 30 fps, rejilla, prohibidos, motor y versión: palitos.py 1.2, Pillow, y costo 0) y se anotan la fuente y la licencia de cada recurso en `licencias.md`.
- **Punto de control:** antes de generar la voz o renderizar se presenta la lista de tomas sobre la rejilla y se espera el visto bueno del dueño.
- **Revisión:** prueba corta de 5 s (de 0,0 a 5,0: gancho, Tan, hoja de calendario y entrada de la toma 4), un fotograma por pulso, hoja de contacto y comprobación de medidas (zona segura, `alto` y x de cada personaje, pies a 86 %, mando de 864 px, el fotograma 0 con el mando ya retumbando y «GTA 5?» legible, hoja de calendario de 864 px o de 800 px sin tocar la zona de texto). Después del render completo, `herramientas/revisar_fotogramas.py` sobre el video y `analizar_video.py <video> <carpeta> --cada 0.5`; se anota en `07_revision/`. Se comprueba al oído que cada corte cae donde dice la sección 6 con la voz real, que la voz arranca en el fotograma 0 y que los golpes se oyen bajo la voz.
- **Qué se marca:** imagen congelada, fotograma vacío (la mitad de abajo del cuadro no debe quedar vacía), texto cortado o tapado, texto que sigue sobre el plano siguiente, elemento fuera de cuadro, tirones, contador que retrocede, glifos cuadrados (en particular «×»), el fotograma 795 (el último) distinto del 0, más de 3 destellos por segundo, el mando que se parezca a uno comercial o lleve símbolos, cualquier cosa que recuerde a Rockstar o Take-Two, y en el teléfono: que tira, hoja, mando y cifras se lean (medidas de la sección 5) y que cada dato lleve una reacción de Tan distinta. Nota para el validador: en las tomas con personajes (2, 4, 5, 6, 7, 8, 9, 10, 11 y 12), el bloque de identidad de la ficha no se pega en el prompt porque no hay generador de imágenes; el diseño oficial es el código de `palitos.py` y se comprueba con la lista de comprobación de cada ficha.
- **Vueltas:** las correcciones por código son gratis (salvo servicios de pago, que van a `costos.md`); **las de generador no se repiten sin autorización del dueño** (`generacion.md`). Aquí solo hay generador en la voz: una generación por voz, sin segundos intentos.
