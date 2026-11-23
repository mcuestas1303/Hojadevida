<!-- Copia archivada. Se edita en proyectos/2026-11-21_tin_y_tan_gta6/02_prompt/prompt.md y se vuelve a archivar. -->
# Prompt de video para redes — How Many Days Did We Wait for GTA 6?

> **ESTADO (2026-11-21):** la voz **está generada** (una generación por voz, 3,2 créditos, autorizada por el dueño) y el diálogo está armado al 110 % (`05_audio/dialogo_110.mp3`, `codigo/armar_dialogo.py`). **Los tiempos de este prompt son los reales**, medidos en `05_audio/linea_de_tiempo_voz.md` y reajustados a la rejilla de 0,5 s: 28,5 s, 855 fotogramas. El video **está renderizado** (`06_final/tin_y_tan_short02_v1.mp4`, 0 créditos; `codigo/render.py`, `codigo/audio.py`, `palitos.py` 1.2) y revisado con medidas en `07_revision/vuelta_01/notas.md`. **Falta la escucha:** nadie ha oído las voces ni la mezcla; los cortes de la voz se hicieron por pausas medidas.
> Hereda el formato y las lecciones del short 1 (`2026-11-21_tin_y_tan_casete_y_lapiz`): el objeto y la voz desde el fotograma 0, cifras al 7 % del alto, personajes y gráficos en el tercio de abajo, una reacción de Tan por dato, bucle con último fotograma igual al primero, rejilla de 0,5 s, golpes bajo la voz a unos −26 LUFS y música por código.

<!--
Pieza dibujada con código (sin generador de video). Todas las tomas son método «edición»: se resuelven gratis
en el montaje. En lugar de «Prompt de keyframe» y «Prompt de video» cada toma lleva una «Especificación de dibujo».
Los tiempos son del video final y de la voz real (05_audio/linea_de_tiempo_voz.md), medidos sin escucha.
-->

## 1. Ficha técnica

- **Proyecto:** 2026-11-21_tin_y_tan_gta6
- **Tipo:** short
- **Número:** 2
- **Serie:** ninguna
- **Objetivo de aprendizaje:** no aplica
- **Generador:** ninguno: imagen dibujada con código (palitos.py + gráficos propios), armada con ffmpeg
- **Aspecto:** 9:16
- **Duración total:** 28,5 s (la voz al 110 % va de 0,00 a 27,33 s, sin gancho mudo; cierre de 1,17 s sin voz, de 27,33 a 28,5 s; múltiplo de 0,5 s)
- **Resolución de borrador:** 540x960 a 30 fps, prueba de 5 s con un fotograma por pulso (render propio)
- **Resolución final:** 1080x1920 a 30 fps, 855 fotogramas
- **Precio por segundo:** 0 (render propio; no hay servicio de pago)
- **Intentos estimados por toma:** 1
- **Versión:** 1 (tiempos reajustados a la voz real; video renderizado, pendiente de escucha)

## 2. Elenco

| Personaje | Papel en este video | Vestuario | Referencia que se sube |
|---|---|---|---|
| @tan | Abre el video con la pregunta nostálgica y con el mando en la mano; reacciona a cada dato (una reacción por dato), pregunta cuánto fue la espera y dice «Wow, that long?». Lado izquierdo del cuadro con `espejo=True` (en el centro cuando está sola). | base de su ficha (rodete y bufanda mostaza); objeto de mano `control` en la toma 2 | personajes/tan/referencias/principal_tin_y_tan.png |
| @tin | Hace la cuenta paso a paso y da el remate. Lado derecho del cuadro, sin espejo; su lápiz en la toma 4 (el motivo del canal), objeto de mano `calendario` en la toma 12 y la mano vacía en la toma 10. | base de su ficha (gorra marrón, lentes, lápiz) | personajes/tin/referencias/principal_tin_y_tan.png |

No se sube nada a un generador: las referencias son las del diseño en código (`herramientas/palitos.py`, versión 1.3) y se usan solo para comparar el resultado. Los objetos de mano `control` y `calendario` son las variaciones aprobadas en las fichas el 2026-11-21 («Objetos de mano por video») y **ya están dibujados** en `palitos.py` 1.2 (sección 14).

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
Flat 2D vector drawing on warm cream paper (#F3E9D2), 1970s palette: two neutrals (cream paper, dark ink) plus ONE accent per shot (mustard in every shot except the two reveal shots, tomato red only in the reveal shots), character colors (orange, brown, teal) are identity and not accents, thick dark ink outlines (#2B2420), hand-made stick-figure look, no gradients, no soft shadows, no glow, no lens effects, crisp anti-aliased lines (supersampled), spring-based motion, static flat camera with small push-ins.
```

**Negativo global:**

```text
text inside the drawing other than the table in section 12, brand names or logos, Rockstar Games or Take-Two logos or lettering, neon pink and purple poster palette, game characters, game maps, cars, weapons, police, violence, watermark, gradients, drop shadows, glow, lens flare, blue and orange cinematic grade, two accent colors in the same shot, tomato red outside the reveal shots, mustard in the reveal shots other than the characters' own scarf and pencil, extra characters, extra fingers, characters other than Tin and Tan, uppercase centered titles, square placeholder glyphs, symbols that are not in the font
```

## 5. Escenarios

- **papel_crema:** fondo plano `#F3E9D2` en todos los planos, sin degradado ni textura. Cuando hay personajes, una línea de suelo `#E6D8B8` de 4 px a **86 % del alto (y = 1651 px)**, de 9,3 % a 90,7 % del ancho. Los planos solo de objeto no llevan suelo.
- **Lienzo y zonas (1080x1920):** zona segura de `formatos.md`: x de 100 a 980 px (9,3 % a 90,7 %), y de 250 a 1670 px (13 % a 87 %). Zona de texto fija: arriba a la izquierda, texto alineado a la izquierda en x = 10 % (108 px). Personajes: **pies a 86 %**, `alto` = 34 % (653 px), cabeza más alta a **52 %**; cuando hay uno solo en plano medio, `alto` = 44 % (845 px), cabeza a 42 %. Cifra principal al 7 % del alto (134 px) con su caja de y = 13,2 % a 20,2 %; **zona de gráficos de 27 % a 51 %** (460 px de alto, de x = 100 a 980 px), centro vertical en 39 %. Los personajes nunca pisan la zona de texto ni la de gráficos.
- **Lados:** Tan en x = 30 % (324 px) con `espejo=True`; Tin en x = 70 % (756 px) sin espejo; cada uno gesticula hacia afuera. Solos, en x = 50 %.
- **mando (gráfico propio, ancho W; es el objeto del gancho):** mando de videojuego **genérico**, sin logotipos ni la forma exacta de ningún mando comercial. Cuerpo: rectángulo redondeado de W × 0,40 W (radio 0,16 W). Dos empuñaduras: círculos de radio 0,16 W con centro en (menos 0,34 W, más 0,19 W) y (más 0,34 W, más 0,19 W) respecto al centro del cuerpo; el contorno exterior (cuerpo más empuñaduras) mide W × 0,55 W (a W = 800 px: 800 × 440 px). Relleno mostaza `#E8B33B`, contorno tinta `#2B2420` de 0,012 W (10 px a W = 800). Dos palancas **a la misma altura**: círculos tinta de radio 0,07 W con un círculo interior `#E6D8B8` de 0,035 W, en (menos 0,26 W, más 0,04 W) y (más 0,03 W, más 0,04 W) (antes la derecha iba en más 0,14 W y cortaba el contorno de abajo; a la misma altura se parece menos a un mando comercial). Cuatro botones: puntos tinta de radio 0,028 W en rombo, centrados en (más 0,26 W, menos 0,05 W) y separados 0,06 W en cada eje. Sin letras ni símbolos en los botones. Cuando «late» (golpe de pulso), el botón de abajo del rombo pasa de tinta a papel `#F3E9D2` durante 0,2 s (nunca a tomate: el mando es el acento mostaza del plano).
- **mando en la mano (`control`):** el mismo dibujo a 1,1 R × 0,6 R (R = radio de cabeza del personaje) con las dos palancas y los cuatro botones de punto; sustituye al lápiz en la mano que gesticula.
- **calendario, hoja (gráfico propio, ancho W y alto H):** hoja con rectángulo redondeado (radio 0,03 W), relleno blanco `#FFF8EC` y contorno tinta de 0,012 W; **cabecera marrón** `#7A4B2A` de 0,22 H (en las hojas grande y de la zona de gráficos de las tomas 3, 4 y 9 la cabecera es **mostaza** `#E8B33B` con contorno tinta: es el acento de esas tomas; el calendario de la mano y la hoja de la toma 12, marrón) de alto en la parte de arriba; dos anillas de radio 0,02 W (relleno papel, contorno tinta) en x de menos 0,25 W y más 0,25 W sobre el borde superior; detrás, dos hojas más en `#E6D8B8` desplazadas 14 px hacia abajo (la pila). La fecha va en el cuerpo, alineada a la izquierda con 0,07 W de margen, centrada verticalmente en el cuerpo. **Pasar de hoja:** la hoja gira sobre su borde de arriba: la escala vertical baja de 1 a 0 en 0,15 s (muelle `sello`) y la hoja nueva sube de 0 a 1 en 0,15 s con muelle `pop`. Tamaños: hoja grande de la toma 3 (W = 864 px, H = 1000 px, centro en 50 %, 54 %; texto de fecha al 5,5 % del alto); hoja de zona de gráficos de las tomas 4 y 9 (W = 800 px, H = 385 px más los 28 px de la pila: de 27 % a 48,5 %; texto de fecha al 4,6 % del alto. Ajuste del render: con H = 460 px la pila tocaba el rodete de Tan y la gorra de Tin).
- **calendario en la mano (`calendario`):** hoja de 0,9 R × 1,0 R con cabecera marrón `#7A4B2A` de 0,22 de alto, dos anillas y el número «17» en tinta (fila de la tabla de la sección 12); sustituye al lápiz en la mano que gesticula.
- **tira de 13 años (gráfico propio):** 13 bloques rectangulares de 60 px de ancho y 200 px de alto, separados 8 px, de x = 100 a 980 px, centrados en y = 39 % (de 33,8 % a 44,2 %); relleno papel sombra `#E6D8B8` al empezar y marrón `#7A4B2A` al llenarse, contorno tinta de 8 px; el bloque 13 es el elemento mostaza `#E8B33B` de las tomas 5 y 6 (marrón en las tomas 7 y 8) y pasa a tomate `#C8553D` solo en la toma 12. Los años bisiestos son los bloques 3, 7 y 11 (años de sept. 2015 a sept. 2016, de 2019 a 2020 y de 2023 a 2024: el 29 de febrero de 2016, 2020 y 2024 cae en cada uno). Marca bisiesta: círculo **mostaza** `#E8B33B` con contorno tinta de 4 px, de radio 18 px (36 px de diámetro) centrado 40 px sobre el bloque. Sin letras.
- **Muelles (masa 1, rigidez, amortiguación), declarados por elemento:** `pop` 220 y 20 (entrada de textos y gráficos, escala de 0,85 a 1); `slide` 120 y 16 (personajes y gráficos que se desplazan); `sello` 320 y 26 (empujes de cámara y vueltas de hoja). Contadores: ease-out cúbico sin muelle, para que el valor nunca pase de su final ni retroceda. Todo depende del número de fotograma (30 fps).
- **mando del gancho y portada (tomas 1 y 13):** el primer segundo del video **es la portada** (`ENTREGA_YOUTUBE.md`, «Portada de los Shorts»). El mando de W = 600 px, centro en (50 %, y = 910 px): ocupa x 239–840 e y 744–1075 en el fotograma 0, dentro de la franja y 720–1100 que la regla pide para el objeto (fue de 864 y de 800 px; se redujo para dejar sitio a las caras). Sin etiquetas. «Retumba»: se balancea ±5 grados con un periodo de 0,5 s, ángulo = 5 × seno(4 pi t) grados (28,5 s son 57 periodos exactos, por eso el último fotograma es igual al primero). Estela plana: dos copias del mando en `#E6D8B8` detrás, a los ángulos de t menos 0,04 s y t menos 0,08 s. El botón de abajo late en cada pulso (pasa a papel durante 0,2 s; nunca a tomate). Debajo, Tan (x = 24 %) y Tin (x = 76 %) de cuerpo entero, **de perfil y con la cabeza inclinada 25 grados hacia arriba (`cabeza_giro=25`, `palitos.py` 1.3), mirando el mando**, `alto` 487 px (R = 88 px), pies a 86 %: las caras quedan en x 121–303 y x 752–955, y 1163–1364, dentro de la zona útil de portada (x 60–960, y 380–1440). El botón que late lo hace en la segunda mitad de cada pulso (de 0,27 a 0,47 s): en el fotograma 0 los cuatro botones se ven iguales. Sin empuje de cámara (escala 100 % en toda la toma).
- **Transición `borrón`:** corte seco con desenfoque de movimiento horizontal de 18 px en los 2 últimos fotogramas de la toma que sale y en los 2 primeros de la que entra. Cero destellos.

## 6. Tomas

<!--
Todas las tomas son «edición»: dibujo por código. Tiempos al décimo de segundo, del video final (28,5 s).
Cada corte cae en un pulso de 0,5 s. Voz: líneas de la sección 7, con los tiempos reales de 05_audio/linea_de_tiempo_voz.md.
Cada corte cae en el pulso anterior al inicio de la línea (o del tramo) que le toca: ninguno llega tarde respecto a la voz.
-->

### Toma 1 — Gancho: el mando, ya retumbando

- **Duración:** 1,0 s (de 0,0 a 1,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la portada: «GTA 5?» arriba (y 400–700), el mando en el centro (y 720–1100) y Tan y Tin debajo, de perfil, mirando el mando (sección 5)
- **Cámara:** fija, escala 100 % (sin empuje: las medidas de la portada valen todo el segundo y nada sale de la zona segura)
- **Acción:** el mando ya está retumbando en el fotograma 0 (con su estela) y el botón de abajo late en 0,27 y 0,77; Tan y Tin, completos desde el fotograma 0, lo miran con la cabeza levantada y rebotan al pulso.
- **Audio:** línea 1, Tan (primera parte): "Remember buying G T A five at midnight?" Aquí suena el principio de la línea (la línea entera va de 0,00 a 1,93 s; el corte de 1,0 cae dentro de ella, hacia «G T A»; sin escucha no se sabe en qué sílaba). Golpe 1 de la sección 13.
- **Referencia:** toma 1 del short 1 (objeto a pantalla completa, ya en movimiento)
- **Transición de entrada:** ninguna (primer fotograma; es también el último del bucle). Salida: `borrón` hacia la toma 2.

**Especificación de dibujo:**

- Mando y personajes exactamente como los define la sección 5, con el ángulo de t = 0 (cero grados) y las dos copias de estela. **Sin muelle de entrada ni escala 0,85 en el fotograma 0**: todo está ya en su estado pleno y en movimiento (este fotograma es la portada y el empalme del bucle).
- Texto «GTA 5?» (fila 1 de la tabla de la sección 12) ya entero y quieto en el fotograma 0 (sin `pop`); sale a los 0,9 s. **El primer segundo es la portada** (regla del dueño): el texto va al 12 % del alto, con el tope de las letras en y = 26 % (medido: x 116–848, y 492–682; franja pedida y 400–700, zona útil y 380–1440), a 97 px o más del mando en todo el balanceo.
- **Color:** acento mostaza = el «5» de «GTA 5?» + el mando; el botón que late pasa a papel, no a tomate. Cabezas, gorra y bufanda son identidad, no acento.
- Tan: pose `parado`, expresión `eureka` (sorpresa alegre: en perfil `sorpresa` se le leía seria por la ceja), vista `perfil`, `mira=1` (hacia el centro), `cabeza_giro=25`, x = 24 %, pies a 86 %, `alto` 487 px. Tin: pose `parado`, expresión `sorpresa` (en perfil `curiosidad` dejaba una raya rara en la boca), vista `perfil`, `mira=-1`, `cabeza_giro=25`, x = 76 %, `objeto=False`. Con suelo. Medido en el fotograma 0: texto x 116–848, y 492–682; mando x 239–840, y 744–1075; cara de Tan x 121–303, y 1201–1364; cara de Tin x 752–955, y 1163–1364.

### Toma 2 — Tan recuerda, mando en mano

- **Duración:** 1,0 s (de 1,0 a 2,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio general de Tan sola, de frente
- **Cámara:** empuje lento de 100 % a 102 %
- **Acción:** Tan levanta la mano con el mando mientras acaba la pregunta.
- **Audio:** línea 1, Tan (segunda parte): "Remember buying G T A five at midnight?" Aquí suena el final de la línea, «…five at midnight?» (hasta 1,93 s).
- **Referencia:** toma 2 del short 1 (Tan recuerda)
- **Transición de entrada:** `borrón` desde la toma 1. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `pregunta`, expresión `nostalgia`, vista `frente`, `mira=1`, `espejo=True`, x = 50 %, pies a 86 %, `alto` 44 % (plano medio de una sola, sección 5; con 34 % el mando de la mano medía 130 px y no se leía), `objeto="control"` (mando en la mano que gesticula), `viento` oscilando de menos 0,3 a 0,3 con muelle.
- **Color:** acento mostaza = el mando en la mano (único elemento; sin texto). Sin tomate.
- Sin gráficos y sin texto (el «GTA 5?» ya salió a los 0,9). Con suelo.

### Toma 3 — La hoja de calendario pasa de 2013 a 2026

- **Duración:** 3,0 s (de 2,0 a 5,0)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** subjetivo: la hoja de calendario grande, de frente, llenando el ancho útil
- **Cámara:** empuje de 100 % a 106 %, muelle `sello`
- **Acción:** la hoja dice «Sep 17, 2013» y a los 3,8 s pasa de hoja y queda en «Nov 19, 2026».
- **Audio:** línea 2, Tan: "So, how many days did we wait for G T A six?" (de 2,16 a 5,12 s; «So,» hasta 2,73 y el resto desde 2,83).
- **Referencia:** toma 3 del short 1 (subjetivo del objeto)
- **Transición de entrada:** `borrón` desde la toma 2. Salida: corte seco.

**Especificación de dibujo:**

- Hoja de calendario grande de la sección 5 (W = 864 px, H = 1000 px, centro 50 %, 54 %). «Sep 17, 2013» entra con `pop` en 2,0 y se queda hasta 3,8; la vuelta de hoja de 3,8 a 4,1; «Nov 19, 2026» de 4,1 a 5,0 (filas de la tabla de la sección 12).
- Texto «how many days?» entra en 2,9 y sale en 4,9. La hoja nunca toca la zona de texto (empieza en 28 % del alto).
- **Color:** acento mostaza = «days» (con trazo de tinta) + la cabecera de la hoja; la fecha, en tinta sobre `#FFF8EC`. Sin tomate.
- Sin personajes ni suelo.

### Toma 4 — Dato 1: GTA 5 salió el 17 de septiembre de 2013

- **Duración:** 4,0 s (de 5,0 a 9,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos, con la hoja de fecha en la zona de gráficos
- **Cámara:** empuje lento de 100 % a 103 %
- **Acción:** Tin explica con su lápiz; Tan, nostálgica, saluda; la hoja de la zona de gráficos está en blanco y en 6,6 s (cuando la voz dice «September seventeenth») entra «Sep 17, 2013» con `pop`: Tin sacude el lápiz y Tan sonríe (cambio a mitad de toma).
- **Audio:** línea 3, Tin: "G T A five came out September seventeenth, twenty thirteen." (de 5,35 a 8,83 s).
- **Referencia:** toma 5 del short 1
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 5.

**Especificación de dibujo:**

- Tan (reacción al dato «2013»): pose `saluda`, expresión `nostalgia` y, desde 6,6, `feliz`, vista `frente`, x = 30 %, `espejo=True`, pies a 86 %, `alto` 34 %, `viento` con muelle.
- Tin: pose `explica`, expresión `feliz`, vista `frente`, x = 70 %, sin espejo, `objeto="lapiz"` (su objeto icónico; el video no lo mostraba en ningún plano y el canal lo tiene como motivo que vuelve); el lápiz tiene movimiento secundario de más o menos 3 grados con muelle y una sacudida de 9 grados en 6,6.
- Hoja de calendario de la sección 5 (W = 800 px, de 27 % a 48,5 % con la pila), **con cabecera marrón** (neutro: en este plano el elemento mostaza es el lápiz), en blanco de 5,0 a 6,6 y con «Sep 17, 2013» desde 6,6.
- Texto «GTA 5» al 7 % de 5,1 a 8,9; la fecha queda en la hoja de 6,6 al corte.
- **Color:** acento mostaza = el «5» de «GTA 5» + el lápiz de Tin (único elemento mostaza; la cabecera de la hoja, marrón). La goma tomate del lápiz es parte del objeto (identidad, como en el short 1), no acento.

### Toma 5 — Dato 2: 13 años por 365

- **Duración:** 2,0 s (de 9,0 a 11,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle: la tira de 13 años a todo el ancho útil, con Tan debajo
- **Cámara:** fija
- **Acción:** los 13 bloques se llenan de marrón de izquierda a derecha, uno cada 0,1 s; Tan señala la tira.
- **Audio:** línea 4, Tin (primera parte): "Thirteen years times three sixty-five: four thousand, seven hundred forty-five days." Aquí suena «Thirteen years times three sixty-five:» (de 9,06 a unos 10,98 s).
- **Referencia:** toma 6 del short 1
- **Transición de entrada:** `borrón` desde la toma 4. Salida: corte seco.

**Especificación de dibujo:**

- Tira de 13 años de la sección 5, llenado de 9,2 a 10,4 (cada bloque con muelle `pop`).
- Tan (reacción al dato «13 años»): pose `senala`, expresión `curiosidad` (`concentrado` se leía como enojo: fallo conocido de su ficha), vista `frente`, x = 50 %, `espejo=True`, pies a 86 %, `alto` 34 %.
- Texto «13 × 365» al 7 % de 9,2 a 10,9 (clave: 13). Con suelo.
- **Color:** acento mostaza = el «13» del texto + el bloque 13 (mostaza al llenarse); los otros 12 bloques, marrón. Sin tomate.

### Toma 6 — Dato 3: 4.745 días

- **Duración:** 2,5 s (de 11,0 a 13,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la misma tira ya llena, con un corchete de tinta que la abarca, y Tan debajo
- **Cámara:** fija
- **Acción:** el contador sube de 0 a 4.745; Tan se asombra.
- **Audio:** línea 4, Tin (segunda parte): "Thirteen years times three sixty-five: four thousand, seven hundred forty-five days." Aquí suena «four thousand, seven hundred forty-five days.» (de 11,13 a 13,64 s; el corte de 13,5 cae 0,14 s antes de que acabe «days.»).
- **Referencia:** toma 7 del short 1 (contador que sube)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Tira de la toma 5 con los 13 bloques marrón (el 13, mostaza) y un corchete de tinta `#2B2420` de 10 px de grosor que la abarca de x = 100 a 980 px, a 4 % por debajo de la tira, sin letras.
- Tan (reacción al dato «4.745»): pose `pregunta`, expresión `sorpresa`, vista `frente`, x = 50 %, `espejo=True`, `viento` alto con muelle.
- Contador de 0 a 4.745 (enteros) con ease-out cúbico de 11,15 a 12,9; solo sube y al terminar se queda fijo. Texto «4,745 days» al 7 % de 11,2 a 13,4 (clave: el número).
- **Color:** acento mostaza = el número «4,745» + el bloque 13; corchete en tinta; sin tomate.

### Toma 7 — Dato 4: 3 días bisiestos

- **Duración:** 1,5 s (de 13,5 a 15,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la tira con tres marcas mostaza que aparecen, y Tan debajo
- **Cámara:** fija
- **Acción:** tres círculos mostaza aparecen sobre los bloques 3, 7 y 11, uno cada 0,3 s; Tan explica.
- **Audio:** línea 5, Tin (primera parte): "Add three leap days: four thousand, seven hundred forty-eight." Aquí suena «Add three leap days:» (de 13,87 a unos 15,1 s).
- **Referencia:** toma 10 del short 1 (barra que se divide)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Tira llena de la toma 6 sin el corchete y con el bloque 13 de nuevo en marrón (el acento pasa a las marcas); marcas bisiestas mostaza de la sección 5 que entran con muelle `pop` en 13,9, 14,2 y 14,5 (la tercera, antes del corte de 15,0).
- Tan (reacción al dato «3 días bisiestos»): pose `explica`, expresión `feliz`, vista `frente`, x = 50 %, `espejo=True`, pies a 86 %, `alto` 34 %.
- Texto «+3 leap days» al 7 % de 13,7 a 14,9 (clave: 3). Con suelo.
- **Color:** acento mostaza = el «3» + las tres marcas bisiestas; el bloque 13, marrón. Sin tomate.

### Toma 8 — Dato 5: 4.748 días

- **Duración:** 2,5 s (de 15,0 a 17,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la tira con sus tres marcas mostaza y el corchete de tinta, y Tan debajo
- **Cámara:** fija
- **Acción:** el contador sube de 4.745 a 4.748 y hace un `pop` de escala solo del texto; Tan se queda pensando.
- **Audio:** línea 5, Tin (segunda parte): "Add three leap days: four thousand, seven hundred forty-eight." Aquí suena «four thousand, seven hundred forty-eight.» (de 15,26 a 17,54 s; el corte de 17,5 cae en la cola de «forty-eight.»).
- **Referencia:** toma 7 del short 1
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 9.

**Especificación de dibujo:**

- Tira (bloque 13 en marrón), tres marcas bisiestas mostaza y corchete de tinta (de la toma 6).
- Tan (reacción al dato «4.748»): pose `parado`, expresión `curiosidad` y, al llegar el contador (16,7), `feliz` (`pensando` se leía como molestia), vista `frente`, x = 50 %, `espejo=True`, pies a 86 %, `alto` 34 %.
- Contador de 4.745 a 4.748 con ease-out cúbico desde 15,6: pasa a 4.746 en 15,74, a 4.747 en 16,1 y llega a 4.748 en 16,7, cuando la voz dice «forty-eight»; el `pop` del texto va en ese mismo fotograma; solo sube. Texto «4,748 days» al 7 % de 15,1 a 17,4 (clave: el número).
- **Color:** acento mostaza = el número «4,748» + las tres marcas; sin tomate.

### Toma 9 — Dato 6: 63 días más

- **Duración:** 3,5 s (de 17,5 a 21,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la hoja de calendario en la zona de gráficos, con Tan debajo
- **Cámara:** empuje lento de 100 % a 104 %
- **Acción:** una pila de hojas en blanco pasa rápido; aparece «Sep 17, 2026», pasa de hoja y queda en «Nov 19, 2026»; Tan piensa.
- **Audio:** línea 6, Tin: "Plus sixty-three days: September seventeenth to November nineteenth." (de 17,77 a 21,15 s; el corte de 21,0 cae 0,15 s antes de que acabe «nineteenth.»).
- **Referencia:** toma 8 del short 1
- **Transición de entrada:** `borrón` desde la toma 8. Salida: corte seco.

**Especificación de dibujo:**

- Hoja de calendario de la sección 5 (W = 800 px, de 27 % a 48,5 % con la pila). De 17,5 a 18,6: 6 hojas **en blanco** (sin fecha) pasan de hoja, una cada 0,18 s (para que la zona de gráficos no quede vacía); «Sep 17, 2026» entra con `pop` en 18,6 y se queda hasta 19,25; vuelta de hoja de 19,25 a 19,55 (la hoja nueva sube desde 19,40; «to November…» empieza hacia 19,6 según la envolvente); «Nov 19, 2026» de 19,55 a 21,0.
- Tan (reacción al dato «63 días»): pose `piensa`, expresión `curiosidad` y, cuando la hoja pasa a «Nov 19, 2026» (19,25), `nostalgia` (`pensando` se leía como molestia), vista `frente`, x = 50 %, `espejo=True`, pies a 86 %, `alto` 34 %, `objeto=False` (en `piensa` el objeto cruza la cara).
- Contador de 0 a 63 con ease-out cúbico de 17,75 a 18,8, que se queda fijo. Texto «+63 days» al 7 % de 17,8 a 19,4 (clave: 63); después «GTA 6» al 7 % de 19,5 a 21,0 (clave: 6; 1,5 s; entra cuando la hoja ya dice «Nov 19, 2026»), que dice a qué lanzamiento corresponde la fecha.
- **Color:** acento mostaza = la clave («63», luego «6») + la cabecera de la hoja; sin tomate.

### Toma 10 — Dato 7: 4.811 días

- **Duración:** 2,5 s (de 21,0 a 23,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el contador arriba (pico de emoción)
- **Cámara:** empuje de 100 % a 103 %
- **Acción:** el contador sube de 4.748 a 4.811 mientras Tan celebra y Tin levanta la mano; al llegar, el número pasa a tomate (primer plano de la revelación: aquí no hay acento mostaza).
- **Audio:** línea 7, Tin: "Four thousand, eight hundred eleven days." (de 21,38 a 23,56 s; «eight hundred eleven days.» desde 22,23).
- **Referencia:** toma 11 del short 1 (contador final y celebración)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `celebra`, expresión `sorpresa`, vista `frente`, x = 30 %, `espejo=True`, `viento` alto con muelle.
- Tin: pose `saluda`, expresión `eureka`, vista `frente`, x = 70 %, sin espejo, `objeto=False` (sin lápiz: el lápiz es mostaza y en este plano el único acento es el tomate de la cifra; Tin levanta la mano vacía).
- Contador en la zona de texto (y = 15 %), tamaño 7 %, de 4.748 a 4.811 con ease-out cúbico desde 21,4 que llega a 4.811 en 22,53 (mientras la voz dice «eight hundred eleven», desde 22,23); el cambio a tomate, el `pop` y el ding van en ese mismo fotograma; al llegar pasa de tinta a tomate `#C8553D` con contorno tinta de 0,045 em (sin mostaza en el plano) y hace un `pop` de escala solo del texto (el valor no se pasa). Texto «4,811 days» (fila de la tabla).
- **Color (revelación):** acento tomate = la cifra «4,811» al llegar; nada en mostaza como acento (Tan conserva su bufanda mostaza, que es identidad); Tin sin lápiz.
- Sin gráfico en la zona de gráficos (el pico es la cifra). El texto «4,811 days» **no sale en el corte de 23,5**: sigue toda la toma 11.

### Toma 11 — Tan se asombra

- **Duración:** 2,0 s (de 23,5 a 25,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tan sola, de frente
- **Cámara:** empuje de 100 % a 106 %
- **Acción:** Tan se encoge de hombros con la boca abierta.
- **Audio:** línea 8, Tan: "Wow, that long?" (de 23,79 a 25,27 s; «that long?» desde 24,40).
- **Referencia:** toma 9 del short 1 (respiro de composición)
- **Transición de entrada:** corte seco. Salida: `borrón` hacia la toma 12.

**Especificación de dibujo:**

- Tan: pose `encoge`, expresión `sorpresa`, vista `frente`, x = 50 %, pies a 86 %, `alto` 44 %, `espejo=True`, `objeto=False`.
- **Color:** acento tomate = la cifra «4,811», que sigue de la toma 10 (único acento del plano; sin mostaza como acento); el resto, neutros y los colores propios de Tan.
- Sin gráficos. Texto: «4,811 days» en tomate con trazo de tinta, el mismo de la toma 10, hasta 25,4 (es el pago del video y en la toma 10 solo se veía 0,6 s; no hay dato nuevo, por eso no lleva reacción distinta). La cabeza de Tan empieza en 42 % y no toca el texto. Con suelo.

### Toma 12 — Remate: un bebé de ese día ya es adolescente

- **Duración:** 2,0 s (de 25,5 a 27,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos, con la tira de 13 años completa en la zona de gráficos
- **Cámara:** fija
- **Acción:** la tira de 13 años, ya llena, hace latir su último bloque en tomate tres veces (remate de la revelación: sin mostaza); Tin sostiene el calendario y celebra; Tan se ríe.
- **Audio:** línea 9, Tin (remate): "A baby born that day is a teenager now." (de 25,50 a 27,33 s; el corte de 25,5 cae justo en el inicio de la línea, sin margen).
- **Referencia:** toma 14 del short 1 (remate con los dos riendo)
- **Transición de entrada:** `borrón` desde la toma 11. Salida: `borrón` hacia la toma 13.

**Especificación de dibujo:**

- Tira de 13 años llena (marrón), con el bloque 13 pasando de marrón a tomate con muelle `pop` en 26,0, 26,5 y 27,0, y quedando en tomate hasta el final (es el único elemento de acento del plano; las marcas bisiestas no están).
- Tan (reacción al dato «13 años»): pose `encoge`, expresión `risa`, vista `frente`, x = 30 %, `espejo=True`, pies a 86 %, `alto` 34 %.
- Tin: pose `celebra`, expresión `risa`, vista `frente`, x = 70 %, sin espejo, `objeto="calendario"` (con «17» en el calendario de su mano, cabecera marrón).
- Texto «age 13» al 7 % de 25,7 a 27,4 (clave: 13, en tomate con contorno tinta; el resto, en tinta).

### Toma 13 — Cierre en bucle: vuelve el mando

- **Duración:** 1,0 s (de 27,5 a 28,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** el mismo plano de portada de la toma 1 (mando, Tan y Tin de perfil)
- **Cámara:** fija, escala 100 %
- **Acción:** el mando retumba y Tan y Tin lo miran, ya en el plano exacto del fotograma 0; el último fotograma es igual al primero.
- **Audio:** sin voz (la voz terminó en 27,33: 1,17 s de silencio de voz hasta el empalme; en el fotograma 0 la voz vuelve a entrar sin pausa). Golpes finales de la sección 13.
- **Referencia:** toma 1 de esta versión (cierre en bucle con el plano del inicio)
- **Transición de entrada:** `borrón` desde la toma 12. Salida: bucle al fotograma 0 de la toma 1.

**Especificación de dibujo:**

- Mando y estela de la sección 5, con el ángulo de la fórmula (5 × seno(4 pi t) grados); en 28,5 el ángulo es 0, la escala 100 % y el rebote de Tan y Tin está en la misma fase que en 0: **el fotograma 855 (el que sigue al último, el 854) es igual al fotograma 0**.
- Texto «GTA 5?» entra con `pop` en 27,6 y está a escala 1 en 28,5; sigue sin corte en la toma 1 del bucle (de 0,0 a 0,9). Misma posición y tamaño que en la toma 1 (12 % del alto, y 492–682).

## 7. Audio

- **Voz (generada el 2026-11-21):** Tan con Zelda (líneas 1, 2 y 8) y Tin con Kevin (líneas 3 a 7 y 9), Higgsfield `seed_audio`, **una sola generación por voz** (regla de un solo intento), al 110 % con `atempo=1.10` y normalizada a −14 LUFS. Costo: **3,2 créditos** (0,7 + 2,5), autorizados por el dueño (`costos.md`, `05_audio/voces_generadas.md`).
- **Los tiempos de la voz son los reales**, medidos en `05_audio/linea_de_tiempo_voz.md` (diálogo `05_audio/dialogo_110.mp3`, armado con `codigo/armar_dialogo.py`): cada línea al 110 %, 0,23 s entre líneas, y las pausas internas largas (tras «So,» y «Wow,», y las de Tin de más de 0,35 s en las líneas 4, 5 y 7) acortadas a 0,15 s. Los cortes de cada línea se hicieron por pausas medidas (`silencedetect` a −35 dB): 5 tramos en Tan y 9 en Tin, los esperados. **Nadie ha escuchado las voces**: que cada tramo diga lo que se supone se comprueba al oído antes de publicar.

Guion de voz (líneas numeradas, quién habla, texto exacto, inicio y fin medidos en el diálogo al 110 %):

| Línea | Quién | Empieza (s) | Termina (s) | Dura (s) | Texto exacto (números como se dicen) | Sílabas |
|---|---|---|---|---|---|---|
| 1 | Tan | 0,00 | 1,93 | 1,93 | Remember buying G T A five at midnight? | 12 |
| 2 | Tan | 2,16 | 5,12 | 2,97 | So, how many days did we wait for G T A six? | 13 |
| 3 | Tin | 5,35 | 8,83 | 3,48 | G T A five came out September seventeenth, twenty thirteen. | 16 |
| 4 | Tin | 9,06 | 13,64 | 4,58 | Thirteen years times three sixty-five: four thousand, seven hundred forty-five days. | 21 |
| 5 | Tin | 13,87 | 17,54 | 3,67 | Add three leap days: four thousand, seven hundred forty-eight. | 14 |
| 6 | Tin | 17,77 | 21,15 | 3,38 | Plus sixty-three days: September seventeenth to November nineteenth. | 17 |
| 7 | Tin | 21,38 | 23,56 | 2,17 | Four thousand, eight hundred eleven days. | 10 |
| 8 | Tan | 23,79 | 25,27 | 1,49 | Wow, that long? | 3 |
| 9 | Tin | 25,50 | 27,33 | 1,82 | A baby born that day is a teenager now. | 12 |

Voz total: de 0,00 a 27,33 s; hasta 28,5 hay 1,17 s sin voz y al volver al fotograma 0 la voz entra otra vez sin silencio inicial (silencio total del empalme del bucle: 1,17 s, menos de 2 s). Tramos internos: línea 2, «how many…» desde 2,83; línea 4, «four thousand…» desde 11,13; línea 5, «four thousand…» desde 15,26; línea 7, «eight hundred…» desde 22,23; línea 8, «that long?» desde 24,40.

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

- **Subtítulos:** `02_prompt/subtitulos.srt` con los tiempos reales de la voz.
- **Música:** hecha con código (Python y numpy), patrón de 120 BPM (el pulso de la rejilla) a −24 LUFS, 10 dB por debajo de la voz, anotada en `licencias.md`. Cubre 28,5 s y cierra su fase en el pulso para el bucle (57 pulsos: 14 compases y 1 pulso). Sin música de terceros ni del juego.
- **Efectos:** los de la sección 13, hechos con código, sin material de terceros.

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → Toma 3 → Toma 4 → Toma 5 → Toma 6 → Toma 7 → Toma 8 → Toma 9 → Toma 10 → Toma 11 → Toma 12 → Toma 13 (y vuelve a la toma 1). Las tomas 1 y 13 son el mismo plano.
- **Transiciones:** corte seco; entre planos de objeto o de cámara distinta, el `borrón` de la sección 5 (1→2, 2→3, 4→5, 8→9, 11→12 y 12→13, como dicen las tomas). Sin destellos, sin fundidos.
- **Texto en pantalla:** se dibuja en el mismo render, solo el de la tabla de la sección 12. El texto nunca contradice lo que se oye.
- **Portada:** el fotograma 0, que cumple los 6 puntos de la regla del dueño (`ENTREGA_YOUTUBE.md`, «Portada de los Shorts»): «GTA 5?» (2 palabras, letra de 230 px, clave en mostaza, sin la respuesta) entre y 400 y 700, el mando en el centro (y 720–1100) y las caras de Tan y Tin dentro de la zona útil (x 60–960, y 380–1440), con sorpresa, de perfil y con la cabeza inclinada 25 grados hacia arriba, mirando el mando. `codigo/miniatura.py` guarda ese fotograma como `06_final/portada_short02.png` (1080x1920) y mide las cajas. Alternativa solo para probar aparte: el fotograma de 23,0 s (el «4,811 days» en tomate), que adelanta la respuesta.
- **Formato de salida:** 1080x1920, 30 fps, H.264, yuv420p, AAC a 48 kHz. Archivo `06_final/tin_y_tan_short02_v1.mp4`.
- **Título de la publicación (inglés):** How Many Days Did We Wait for GTA 6?
- **Descripción de la publicación (en inglés, obligatoria; sin llamado a la acción):**

```text
How Many Days Did We Wait for GTA 6? Step by step:

GTA 5 came out on Sep 17, 2013 (original PlayStation 3 and Xbox 360 release). GTA 6 came out on Nov 19, 2026.
Sep 17, 2013 to Sep 17, 2026 is 13 years: 13 × 365 = 4,745 days.
Add 3 leap days (Feb 29 of 2016, 2020 and 2024): 4,748 days.
Sep 17 to Nov 19, 2026: 13 + 31 + 19 = 63 more days.
4,748 + 63 = 4,811 days.
A baby born that day is a teenager now.

Release dates: Wikipedia, "Grand Theft Auto V" and "Grand Theft Auto VI", read on 2026-11-21. The GTA 6 date was not checked on the publisher's website.
Not affiliated with Rockstar Games or Take-Two Interactive.
```

- **Sin llamado a la acción** (ni en el video ni en la descripción): el objetivo es presencia y línea base, y un llamado al final cortaría el bucle.
- **Fechas y fuentes:** Grand Theft Auto V, 17 de septiembre de 2013 (PlayStation 3 y Xbox 360) y Grand Theft Auto VI, 19 de noviembre de 2026 (PlayStation 5 y Xbox Series X/S): Wikipedia en inglés, páginas «Grand Theft Auto V» y «Grand Theft Auto VI», abiertas y leídas el 2026-11-21. La de GTA VI no se leyó en Rockstar Games (sitio sin acceso).

### Título (ficha)

Filtro: `revisar_titulo.py` v1.0 (2026-11-21). Estudio y reglas: `video-studio/comercial/titulos.md`.

| Campo | Valor |
|---|---|
| `titulo_elegido` | How Many Days Did We Wait for GTA 6? |
| `caracteres` | 36 |
| `idioma` | en |
| `canal` | tin-y-tan |
| `formato` | short |
| `publico` | EE. UU., adultos de 30 a 50 años que crecieron con la saga |
| `frase_de_busqueda` | how many days did we wait for gta 6 |
| `fuente_de_la_frase` | `comercial/titulos.md` §3a y §8; volumen: sin dato |
| `formula` | F1 (la pregunta es el título) |
| `alternativa_1` | How Many Days Between GTA 5 and GTA 6? (38 caracteres; frase «how many days between gta 5 and gta 6»; filtro: PASA) |
| `alternativa_2` | How Long Did We Wait for GTA 6? We Counted (42 caracteres; frase «how long did we wait for gta 6»; filtro: PASA) |
| `uso_de_las_alternativas` | Reserva. YouTube no ofrece prueba A/B de títulos en Shorts ni en videos «hechos para niños» (ayuda oficial, leída el 2026-11-21) |
| `filtro` | **PASA** · errores: ninguno · avisos: ninguno |
| `revision_humana` | **Pendiente**: que el video cumpla lo que el título promete, que no engañe y que pase la línea editorial. Firma el director creativo cuando exista el video |
| `medicion` | Visto frente a deslizado, mostrado en el feed y tráfico de búsqueda; a 7 y 28 días; meta: establecer línea base |

El título no lleva la cifra (4,811): es la respuesta del video, y otro canal ya publicó un título con ella (`comercial/titulos.md`, hallazgo 6).

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | 0 s (las 13 tomas son edición; 28,5 s se resuelven en edición) | 0 |
| Keyframes | 0 | 0 |
| Remates en resolución final | 0 | 0 |
| Voz (Tan con Zelda y Tin con Kevin, una generación por voz) | 2 generaciones | 3,2 créditos (0,7 + 2,5), gastados con el sí del dueño |
| **Total estimado** | 0 créditos en imagen y video; voz: 3,2 créditos ya gastados | 0 |

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
- **Rejilla de tiempo:** pulso de 0,5 s (120 BPM, compás de 4 pulsos = 2,0 s); 57 pulsos = 28,5 s (14 compases y 1 pulso). La voz entra en el pulso 0 (fotograma 0). Los 12 cortes caen en 1,0; 2,0; 5,0; 9,0; 11,0; 13,5; 15,0; 17,5; 21,0; 23,5; 25,5 y 27,5 (más el bucle en 28,5). Inicios reales de la voz: 0,00; 2,16; 5,35; 9,06 (y 11,13 dentro de la línea 4); 13,87 (y 15,26 dentro de la línea 5); 17,77; 21,38; 23,79; 25,50; fin en 27,33. Cada corte cae en el pulso anterior al inicio que le toca (de 0,00 a 0,37 s antes): ninguno llega tarde. A cambio, cuatro cortes caen de 0,04 a 0,15 s antes de que acabe la línea anterior (5,0 sobre «six?», 13,5 sobre «days.», 17,5 sobre «forty-eight.» y 21,0 sobre «nineteenth.»), y el de 25,5 no tiene margen (la línea 9 empieza en 25,50). El corte de 1,0 cae dentro de la línea 1. Se revisan al oído.
- **Gancho (0 a 2,0 s):** el fotograma 0 es la portada: el mando en el centro, ya retumbando (con estela), Tan y Tin debajo mirándolo, y «GTA 5?» ya entero (clave: 5, en mostaza; el otro elemento mostaza es el mando), que sale a los 0,9 s, y la voz de Tan ya diciendo «Remember buying G T A five…» desde el fotograma 0. En 1,0 el `borrón` pasa a Tan con el mando en la mano y, en 2,0, a la hoja de calendario que pasa de 2013 a 2026. Sin logo, sin título, sin segundo mudo. Gancho B para otra publicación (se renderiza gratis): el mismo plano con el texto «4,811 days?».
- **Empieza en movimiento:** sí: sin intro ni logo; el mando retumba, el botón de abajo late y Tan y Tin rebotan al pulso desde el fotograma 0.
- **Motivo visual que vuelve:** el mando (tomas 1, 2 y 13), la hoja de calendario (tomas 3, 4, 9 y 12, y el calendario en la mano de Tin), la tira de 13 años (tomas 5 a 8 y 12) y el lápiz mostaza de Tin (toma 4). Se repiten con las mismas formas y colores.
- **Cierre:** el video vuelve al plano exacto del fotograma 0 (la portada: mando en el centro con ángulo 0, Tan y Tin mirándolo, escala 100 %, «GTA 5?» ya entero) y encadena en bucle con la toma 1: el último fotograma es el primero. Cierre de 1,0 s (de 27,5 a 28,5); la voz termina en 27,33; silencio de voz en el empalme: 1,17 s (menos de 2 s).
- **Llamado a la acción:** ninguno. Por qué: el objetivo comercial es presencia y línea base de retención; el canal todavía no existe y un llamado al final cortaría el bucle.

Mapa de ritmo (los tiempos al décimo de segundo; cortes por segundo = cortes que caen dentro del tramo, sin contar el inicio):

| Tramo | Segundos | Pulso o intervalo | Cortes por segundo | Qué pasa (una acción) | Respiro |
|---|---|---|---|---|---|
| Gancho | 0,0–2,0 | 1,0 s y 1,0 s | 1,0 | el mando retumba, Tan recuerda con el mando en la mano | no |
| Pregunta | 2,0–5,0 | 3,0 s | 0,3 | la hoja de calendario pasa de 2013 a 2026 | sí |
| Dato 1 | 5,0–9,0 | 4,0 s | 0,3 | GTA 5 salió el 17 de septiembre de 2013; Tan saluda | sí |
| Cuenta | 9,0–17,5 | 2,0 s, 2,5 s, 1,5 s y 2,5 s | 0,5 | 13 años, 4.745 días, 3 bisiestos, 4.748 | no |
| Fechas | 17,5–21,0 | 3,5 s | 0,3 | 63 días de septiembre a noviembre; héroe: la hoja pasa a «Nov 19, 2026» | no |
| Pico | 21,0–23,5 | 2,5 s | 0,4 | contador hasta 4.811 y celebración | no (pico de emoción) |
| Remate | 23,5–27,5 | 2,0 s y 2,0 s | 0,5 | «Wow, that long?» y el bebé de ese día es adolescente | no (acelera al principio) |
| Cierre | 27,5–28,5 | 1,0 s | 0 | vuelve el mando del primer fotograma | sí |

Total: 12 cortes en 28,5 s. Es una densidad baja a propósito, igual que en el short 1: la voz es continua y cada cifra necesita su plano; la densidad extra va dentro de cada toma (contadores que suben, hojas que pasan, bloques que se llenan, una reacción de Tan por dato, el mando que late a cada pulso).

Lo que sale se va antes de que entre lo siguiente: los textos salen de 0,1 a 0,2 s antes del corte siguiente (el texto 1, a los 0,9 s) y los gráficos con el borrón. El movimiento es mecánica: entradas con `pop` o `slide` (muelle), contadores con ease-out cúbico, el balanceo del mando con un seno de periodo 0,5 s, sin interpolación lineal.

Tipos de plano disponibles y dónde van: detalle o macro (tomas 5 a 8), héroe abierto (tomas 4, 10 y 12; el héroe principal es la 10, con la cifra final, hacia el final del arco), subjetivo y mando a pantalla completa (tomas 1, 3 y 13), revelado (la hoja que pasa de 2013 a 2026 en la toma 3), objeto que salta sobre el mismo fondo (las marcas bisiestas mostaza de la toma 7 y el bloque 13 tomate de la toma 12). Transiciones siempre motivadas (borrón de movimiento). **No más de 3 destellos por segundo:** hay cero (el botón que late es un cambio de color de 0,2 s, no un destello; son 2 por segundo como máximo).

## 12. Texto en pantalla y sistema de diseño

- **Tipografías:** Inter Display Medium con sus **dígitos abiertos** (rasgo OpenType `ss01` de la misma fuente: 3, 4, 6 y 9 alternativos; con los dígitos por defecto el trazo de tinta cerraba las aberturas del 6, el 3 y el 5), licencia SIL Open Font License 1.1 (archivo `/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf`; en Windows, si no está, Segoe UI Semibold, que se anota en `licencias.md` antes de usarla). Siempre en minúsculas cuando es subtítulo, alineadas a la izquierda; las siglas «GTA» y las fechas («Sep», «Nov») conservan su mayúscula inicial porque son nombres propios. No se usa la tipografía de ningún logotipo del juego. Excepción obligatoria (regla del dueño, 2026-11-21): los nombres propios llevan mayúscula inicial («Tin & Tan», «Tin», «Tan»).
- **Paleta:** papel `#F3E9D2` · papel_sombra `#E6D8B8` · tinta `#2B2420` · naranja `#E07A2E` · marrón `#7A4B2A` · verde azulado `#2F7F7A` · mostaza `#E8B33B` (**acento único** de todos los planos salvo la revelación: palabra clave y un elemento) · tomate `#C8553D` (**acento solo de la revelación**, tomas 10, 11 y 12: cifra «4,811», «13» y bloque 13) · rubor `#E9967A` · blanco `#FFF8EC` (cuerpo de la hoja de calendario). Un color de acento por plano; mostaza y tomate nunca comparten plano. La palabra clave en mostaza o en tomate lleva un trazo de tinta de 0,045 em. Los colores propios de los personajes (cabeza, gorra, bufanda, mejillas) no cuentan como acento. Ninguna paleta rosa neón ni morada. Detalle y razones en la sección «Color con intención».
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
- **Subtítulos:** de 1 a 3 palabras, con la palabra clave en mostaza (con trazo de tinta); en la revelación (tomas 10, 11 y 12) la palabra clave va en tomate con trazo de tinta y no hay mostaza como acento. Los subtítulos de las demás tomas, en tinta salvo la clave. Las cifras del valle (filas 4 a 12) van al 7 % del alto.

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| GTA 5? (clave: 5; ya entero en el fotograma 0, sin pop; es la portada) | 0,0 | 0,9 | 10, 26 | 12 |
| how many days? (clave: days) | 2,9 | 4,9 | 10, 15 | 5 |
| Sep 17, 2013 (en la hoja grande, alineado a la izquierda; sin clave) | 2,0 | 3,8 | 15,6, 59,7 | 5,5 |
| Nov 19, 2026 (en la hoja grande; sin clave) | 4,1 | 5,0 | 15,6, 59,7 | 5,5 |
| GTA 5 (clave: 5) | 5,1 | 8,9 | 10, 14 | 7 |
| Sep 17, 2013 (en la hoja de la zona de gráficos; sin clave) | 6,6 | 9,0 | 18,1, 39,2 | 4,6 |
| 13 × 365 (clave: 13) | 9,2 | 10,9 | 10, 14 | 7 |
| 4,745 days (contador de 0 a 4,745; clave: el número) | 11,2 | 13,4 | 10, 14 | 7 |
| +3 leap days (clave: 3) | 13,7 | 14,9 | 10, 14 | 7 |
| 4,748 days (contador de 4,745 a 4,748; clave: el número) | 15,1 | 17,4 | 10, 14 | 7 |
| +63 days (contador de 0 a 63; clave: 63) | 17,8 | 19,4 | 10, 14 | 7 |
| Sep 17, 2026 (en la hoja de la zona de gráficos; sin clave) | 18,6 | 19,25 | 18,1, 39,2 | 4,6 |
| Nov 19, 2026 (en la hoja de la zona de gráficos; sin clave) | 19,4 | 21,0 | 18,1, 39,2 | 4,6 |
| GTA 6 (clave: 6) | 19,5 | 21,0 | 10, 14 | 7 |
| 4,811 days (contador de 4,748 a 4,811; en tinta mientras sube, al llegar el número en tomate con trazo de tinta; se queda durante toda la toma 11) | 21,2 | 25,4 | 10, 15 | 7 |
| age 13 (clave: 13, en tomate con trazo de tinta; «age» en tinta) | 25,7 | 27,4 | 10, 14 | 7 |
| 17 (en el calendario de la mano de Tin; tinta) | 25,5 | 27,5 | sobre la mano de Tin | 3 |
| GTA 5? (clave: 5; entra con pop y sigue sin corte en la fila 1 del bucle) | 27,6 | 28,5 | 10, 26 | 12 |

### Color con intención

Propuesta del prompt (regla del dueño, 2026-11-21; `manual/13_color_con_intencion.md`, sección 6). La sección equivalente de `02_prompt/direccion.md` la escribe el director de fotografía y la valida el director creativo (equipo de producción); este bloque es la propuesta del prompt y, si difiere, manda la dirección.

- **Neutros (2):** papel `#F3E9D2` (fondo de todos los planos; hoja de calendario en `#FFF8EC`, su cuerpo, y suelo `#E6D8B8`) y tinta `#2B2420` (líneas, contornos y todo texto que no sea clave). Contraste tinta/papel 12,6:1; tinta/blanco de la hoja 14,5:1; tinta/papel_sombra 10,8:1 (todos pasan 7:1).
- **Acento (1):** mostaza `#E8B33B`, siempre con contorno de tinta, solo en la palabra clave y en **un** elemento por plano (el mando, la cabecera de la hoja, el bloque 13 o las marcas bisiestas, según la toma). **No va** en: texto que no sea clave, personajes (su bufanda y lápiz son identidad), suelo, tira de bloques (marrón), corchete (tinta) ni en los planos de la revelación. **Tomate `#C8553D` queda reservado a la revelación** (tomas 10 y 11: «4,811»; toma 12: «age 13» y bloque 13) y en esos planos no hay mostaza como acento; nunca comparte plano con la mostaza. Marrón `#7A4B2A` solo como relleno (bloques, cabecera del calendario de la mano), nunca como texto.
- **Por qué esta paleta:** papel crema y tinta marrón remiten a impresos y fotos de los 70 y 80: nostalgia cálida y de saturación baja para el público de 30 a 50 años de EE. UU. que compró GTA 5 en 2013, y se lee bien con la vista de 45 o más. La mostaza lleva el ojo al dato en cada plano; el tomate, guardado para el final, hace que la cifra de la espera y el bebé de 13 años se sientan como un golpe de emoción (hipótesis, no significado fijo).
- **Cómo ayuda al objetivo:** presencia y línea base del canal -> la misma paleta y el mismo acento que el short 1 hacen que el canal se reconozca antes de leer el nombre, y el cambio de mostaza a tomate marca el pico en 22,5 s (toma 10; la cifra en tomate sigue hasta 25,4) -> se verá con retención del segundo 1 al 3, visto frente a deslizado, regreso de espectadores y búsquedas del canal.
- **Riesgos de lectura:** (1) mostaza sobre papel da 1,6:1: solo se lee por el contorno de tinta (contorno contra papel 12,6:1; cifra de 7 % del alto, contorno de 0,045 em); (2) tomate sobre papel da 3,6:1 y tinta sobre tomate 3,5:1: la cifra «4,811» y el «13» se leen por su contorno de tinta y por ser texto grande, no por el relleno; se revisa en teléfono; (3) Tan conserva su bufanda mostaza en las tomas 10, 11 y 12 (identidad, no acento): se vigila que no se lea como segundo acento; (4) rojo contra verde: la cabeza verde azulada de Tan y el tomate no llevan la información (la cifra va también por tamaño, posición y luminosidad del contorno); (5) pantalla chica: cifras al 7 % del alto.
- **Medido (2026-11-21, `revisar_color.py` sobre el video, 29 cuadros; falta la firma del supervisor):** ≈ 93 % del cuadro dentro de la paleta declarada (mínimo 85 %); saturación media ≈ 17 %, luminosidad media ≈ 89 %; entre segundos la luminosidad varía ±2 % y la saturación ±2 %. Contrastes, los de abajo. Detalle en `07_revision/vuelta_01/notas.md`.

Tabla de acento por plano:

| Toma | Mostaza (palabra clave + un elemento) | Tomate |
|---|---|---|
| 1 | «5» de «GTA 5?» + mando | no |
| 2 | mando en la mano de Tan | no |
| 3 | «days» + cabecera de la hoja | no |
| 4 | «5» de «GTA 5» + lápiz de Tin (cabecera de la hoja en marrón) | no |
| 5 | «13» + bloque 13 | no |
| 6 | número «4,745» + bloque 13 | no |
| 7 | «3» + marcas bisiestas | no |
| 8 | número «4,748» + marcas bisiestas | no |
| 9 | «63» y luego «6» + cabecera de la hoja | no |
| 10 | ninguno | cifra «4,811» |
| 11 | ninguno | cifra «4,811» (sigue de la toma 10) |
| 12 | ninguno | «13» de «age 13» + bloque 13 |
| 13 | «5» de «GTA 5?» + mando | no |

Contrastes medidos con `revisar_color.py --contraste` (2026-11-21): tinta/papel 12,6:1; tinta/blanco 14,5:1; tinta/papel_sombra 10,8:1; tinta/mostaza 8,0:1; tinta/tomate 3,5:1; mostaza/papel 1,6:1; tomate/papel 3,6:1; marrón/papel 6,1:1; marrón/papel_sombra 5,2:1.

Campo para `ficha.json`:

```json
"color": {"neutros": [
            "#F3E9D2",
            "#2B2420"
          ], "acento": "#E8B33B",
          "por_que": "papel crema y tinta de impresos de los 70 y 80 (nostalgia cálida, saturación baja) para un público de 30 a 50 años de EE. UU.; la mostaza lleva el ojo al dato y el tomate se reserva a la revelación (tomas 10, 11 y 12), nunca junto a la mostaza",
          "objetivo": "presencia y línea base: misma paleta y acento en todo el canal para reconocerlo; mostaza a tomate marca el pico; métrica: retención del segundo 1 al 3 y regreso de espectadores",
          "medido": "2026-11-21, revisar_color.py: 93 % dentro de la paleta, saturación 17 %, luminosidad 89 %, variación entre segundos ±2 %; falta la firma del supervisor"}
```

En un short, todo texto queda dentro de la zona segura de `formatos.md`. Entrada de cada texto: `pop` con escala de 0,85 a 1 en 8 fotogramas; salida: subir 2 % con ease-in en 3 fotogramas (excepción: la fila 1 en el fotograma 0 está ya a escala 1, y la última fila queda a escala 1 en el último fotograma para que el bucle empalme).

## 13. Sonido

Los golpes bajo la voz van a unos **−26 LUFS** (−12 dB respecto a la voz, que está a −14 LUFS; lección de la revisión del short 1: a −38 LUFS no se oían en un teléfono). Se comprueba al oído. Medido en `05_audio/medidas_audio.json` (2026-11-21): golpes bajo la voz −26,0 LUFS; golpes sin voz encima (arranque y cierre) con pico de −6 dBFS; música −24,0 LUFS; mezcla final −14,0 LUFS con pico real de −1,3 dBTP (con limitador); los 49 golpes empiezan en su tiempo (±12 ms).

| Golpe o efecto | Segundo | A qué corte va atado | Origen y licencia |
|---|---|---|---|
| Golpe seco grave de 80 ms y zumbido corto de vibración del mando | 0,0 | arranque, toma 1 (es también el empalme del bucle: no se duplica) | código, propio (ver licencias.md) |
| Clic de botón, uno por pulso | 0,27 / 0,77 | latidos del botón de la toma 1 (segunda mitad del pulso) | código, propio |
| Clic suave de borrón | 1,0 | corte de toma 1 a toma 2 | código, propio |
| Clic suave de borrón | 2,0 | corte de toma 2 a toma 3 | código, propio |
| Papel que pasa de hoja (tic corto) | 3,8 | vuelta de hoja de la toma 3 | código, propio |
| Clic suave | 5,0 | corte de toma 3 a toma 4 | código, propio |
| Clic suave de borrón | 9,0 | corte de toma 4 a toma 5 | código, propio |
| Tic de bloque que se llena, 13 veces, subiendo de tono | 9,2–10,4 | llenado de la tira en la toma 5 | código, propio |
| Tictac de contador que sube de tono | 11,15–12,9 | contador de la toma 6 | código, propio |
| Pop de marca bisiesta | 13,9 / 14,2 / 14,5 | marcas bisiestas de la toma 7 | código, propio |
| Clic suave | 15,0 | corte de toma 7 a toma 8 | código, propio |
| Tictac de contador (3 pasos) | 15,74 / 16,1 / 16,68 | contador de la toma 8 (el tercero, con el `pop` del texto) | código, propio |
| Clic suave de borrón | 17,5 | corte de toma 8 a toma 9 | código, propio |
| 6 tics de hoja en blanco | 17,56–18,46 | pila de hojas de la toma 9 | código, propio |
| Papel que pasa de hoja (tic corto) | 19,25 | vuelta de hoja de la toma 9 | código, propio |
| Clic suave | 21,0 | corte de toma 9 a toma 10 | código, propio |
| Tictac de contador que sube de tono | 21,4–22,5 | contador de la toma 10 (calla al llegar) | código, propio |
| Ding de campana al llegar a 4,811 | 22,53 | primer fotograma con el valor final de la toma 10 (mismo fotograma que el tomate y el `pop`) |
| Pop de la fecha | 6,6 | «Sep 17, 2013» entra en la hoja de la toma 4 | código, propio | código, propio |
| Clic suave | 23,5 | corte de toma 10 a toma 11 | código, propio |
| Clic suave de borrón | 25,5 | corte de toma 11 a toma 12 | código, propio |
| Pop del bloque 13 (pasa a tomate) (3) | 26,0 / 26,5 / 27,0 | latidos de la toma 12 | código, propio |
| Clic suave de borrón | 27,5 | corte de toma 12 a toma 13 | código, propio |
| Whoosh suave | 27,5–28,3 | vuelve el plano de la portada, toma 13 | código, propio |
| Clic de botón, uno por pulso | 27,77 / 28,27 | latidos del botón de la toma 13 | código, propio |
| Thunk grave idéntico al del segundo 0,0 (cierra el bucle; el del 0,0 lo continúa) | 28,5 | bucle: es el del segundo 0,0 de la vuelta siguiente (el archivo dura 28,5 s justos y no lo duplica) | código, propio |

- **Música:** hecha con código a −24 LUFS (ver sección 7); sin material de terceros ni del juego.
- **Voz:** sí (generada; ver sección 7). Sin retraso: empieza en el fotograma 0.

## 14. Motor y revisión

- **Cómo se hace:** gráficos por código (fotograma a fotograma): Python, Pillow y ffmpeg. Cada fotograma se dibuja en un `Lienzo(1080, 1920)` de `palitos.py`, que ya dibuja al triple de tamaño y reduce con LANCZOS (supermuestreo). Los empujes de cámara recortan el lienzo grande y reducen. Todo depende del número de fotograma, no del reloj. Se guardan PNG numerados y ffmpeg los une con la voz y los efectos (`postpro.py mezclar` o ffmpeg directo). Personajes con `palitos.dibujar(lz, id, x, suelo, alto, pose, expresion, vista, mira, viento, objeto, espejo)`.
- **Qué se añadió a `palitos.py` (versión 1.1 → 1.2, y 1.3 con la inclinación de cabeza `cabeza_giro` para la portada) para renderizar (hecho el 2026-11-21: los puntos 1 a 3 están en `palitos.py`; los gráficos 4 y 5 quedaron en `codigo/render.py` del proyecto, como `hoja_calendario` y `tira_13`; los glifos del punto 6 se comprueban al arrancar el render):**
  1. `objeto="control"`: hoy `objeto` solo conoce el lápiz y se usa como verdadero o falso. Hay que aceptar un nombre de objeto (`"lapiz"`, `"control"`, `"calendario"`; `True` sigue significando el objeto icónico del personaje y `False` ningún objeto) y dibujar el `control` en la mano que gesticula, con las medidas de la sección 5 (1,1 R × 0,6 R, dos palancas, cuatro botones de punto, mostaza con contorno tinta, sin ningún elemento tomate; también para Tan, que no tiene objeto icónico).
  2. `objeto="calendario"`: hoja de 0,9 R × 1,0 R con cabecera marrón `#7A4B2A` (0,22; sin tomate), dos anillas y el número «17» en tinta, con la misma regla de ángulo que el lápiz para las poses `saluda`, `celebra` y `pregunta`.
  3. Gráfico `mando(lz, cx, cy, ancho, angulo, boton_pulsado, estela)` para el mando a pantalla completa (sección 5); el botón pulsado pasa a papel, no a tomate.
  4. Gráfico `hoja_calendario(lz, cx, cy, ancho, alto, texto, vuelta)` para la hoja grande y la de la zona de gráficos, con la vuelta de hoja (escala vertical y muelles `sello` y `pop`) y la pila de hojas; parámetro `cabecera` (`"mostaza"` en las tomas 3, 4 y 9, `"marron"` en el resto).
  5. Gráfico `tira_13(lz, llenos, marcas, corchete, color_ultimo)` para la tira de 13 años: marcas mostaza, corchete de tinta, `color_ultimo` = `"marron"`, `"mostaza"` (tomas 5 y 6) o `"tomate"` (toma 12).
  6. Comprobar los glifos «×», «+» y «:» en la fuente, y regenerar las hojas `referencias/poses.png` solo si cambia alguna pose (no cambia ninguna).
  Costo en créditos: 0.
- **Quién renderiza y autorización:** el render lo hace el equipo de producción. La voz y el montaje los autorizó el dueño (2026-11-21); el render es de 0 créditos y está hecho con los tiempos reales de la voz. Antes de renderizar se crea `03_keyframes/definicion.md` con la entrada de «pieza por código» de `generacion.md` (datos con fuente, paleta con HEX, tipografía y licencia, texto exacto, 28,5 s a 30 fps, rejilla, prohibidos, motor y versión: palitos.py 1.2, Pillow, y costo 0) y se anotan la fuente y la licencia de cada recurso en `licencias.md`.
- **Punto de control:** antes de generar la voz o renderizar se presenta la lista de tomas sobre la rejilla y se espera el visto bueno del dueño.
- **Revisión:** prueba corta de 5 s (de 0,0 a 5,0: gancho, Tan, hoja de calendario y entrada de la toma 4), un fotograma por pulso, hoja de contacto y comprobación de medidas (zona segura, `alto` y x de cada personaje, pies a 86 %, mando de 800 px, el fotograma 0 con el mando ya retumbando y «GTA 5?» legible, hoja de calendario de 864 px o de 800 px sin tocar la zona de texto). Después del render completo, `herramientas/revisar_fotogramas.py` sobre el video y `analizar_video.py <video> <carpeta> --cada 0.5`; se anota en `07_revision/`. Se comprueba al oído que cada corte cae donde dice la sección 6 con la voz real, que la voz arranca en el fotograma 0 y que los golpes se oyen bajo la voz.
- **Qué se marca:** imagen congelada, fotograma vacío (la mitad de abajo del cuadro no debe quedar vacía), texto cortado o tapado, texto que sigue sobre el plano siguiente, elemento fuera de cuadro, tirones, contador que retrocede, glifos cuadrados (en particular «×»), el fotograma 855 (el que sigue al último) distinto del 0, más de 3 destellos por segundo, el mando que se parezca a uno comercial o lleve símbolos, cualquier cosa que recuerde a Rockstar o Take-Two, y en el teléfono: que tira, hoja, mando y cifras se lean (medidas de la sección 5) y que cada dato lleve una reacción de Tan distinta. Nota para el validador: en las tomas con personajes (2, 4, 5, 6, 7, 8, 9, 10, 11 y 12), el bloque de identidad de la ficha no se pega en el prompt porque no hay generador de imágenes; el diseño oficial es el código de `palitos.py` y se comprueba con la lista de comprobación de cada ficha.
- **Vueltas:** las correcciones por código son gratis (salvo servicios de pago, que van a `costos.md`); **las de generador no se repiten sin autorización del dueño** (`generacion.md`). Aquí solo hay generador en la voz: una generación por voz, sin segundos intentos.
