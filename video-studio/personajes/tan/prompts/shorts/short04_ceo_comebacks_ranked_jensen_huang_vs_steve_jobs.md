<!-- Copia archivada. Se edita en proyectos/2026-11-24_tin_y_tan_ceo_comebacks/02_prompt/prompt.md y se vuelve a archivar. -->
# Prompt de video para redes — CEO Comebacks Ranked: Jensen Huang vs. Steve Jobs

> **ESTADO (2026-11-24, versión 1):** short 4 de Tin & Tan, el «próximo conteo» que prometió el short 3. **La voz no está generada, los tiempos son estimados** con el ritmo medido en los shorts 2 y 3 (Tin ≈ 4,6 sílabas por segundo, Tan ≈ 5,2, voz al 110 %) y el video no está renderizado. Se reajustan con la voz real. No quedan preguntas para el dueño: solo su sí para los créditos de la voz y para publicar. **Lo que el short 3 rechazó o corrigió viene resuelto de origen** (tabla de la sección 14): lápiz a 8 px o más de las cabezas, panel de subtítulos a 12 px o más, barras con nombre de 56 px, tarjetas con la cifra y la palabra «días», la tarjeta de la cifra del pico nítida 1 s o más, caras sin sonrisa en los datos, cara de Tan en `sorpresa` en la portada, nada fuera de la zona segura, la voz con «almost» donde la cifra es aproximada. **Manda sobre este prompt:** `canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md` (apertura y cierre) y `PARAMETROS.md`.

<!--
Pieza dibujada con código (sin generador de video). Todas las tomas son método «edición». En lugar de «Prompt de keyframe»
y «Prompt de video» cada toma lleva una «Especificación de dibujo». Sin corchetes en el texto: el validador los trata como
campos sin llenar. Los segundos son estimados con la voz de los shorts 2 y 3 y se reajustan con la voz real.
-->

## 1. Ficha técnica

- **Proyecto:** 2026-11-24_tin_y_tan_ceo_comebacks
- **Tipo:** short
- **Número:** 4
- **Serie:** ninguna
- **Objetivo de aprendizaje:** no aplica
- **Generador:** ninguno: imagen dibujada con código (palitos.py 1.4 + efectos.py 1.1 + gráficos propios), armada con ffmpeg
- **Aspecto:** 9:16
- **Duración total:** 31,0 s estimados (la voz va de 0,47 a 30,19 s; cierre de 0,81 s sin voz con el lanzamiento del lápiz; múltiplo de 0,5 s; 930 fotogramas)
- **Resolución de borrador:** 540x960 a 30 fps, prueba de 5 s con un fotograma por pulso (render propio)
- **Resolución final:** 1080x1920 a 30 fps, 930 fotogramas
- **Precio por segundo:** 0 (render propio; no hay servicio de pago)
- **Intentos estimados por toma:** 1
- **Versión:** 1 con tiempos estimados

## 2. Elenco

| Personaje | Papel en este video | Vestuario | Referencia que se sube |
|---|---|---|---|
| @tan | Abre con la pregunta de curiosidad desde el fotograma 0 («Who took longer?»), reacciona con una cara distinta a cada dato («Almost seven years?», «Almost twelve years?»), dice la pregunta final con la invitación y **atrapa el lápiz al abrir y lo lanza al cerrar**. Lado izquierdo con `espejo=True` (centro cuando está sola). | base de su ficha (rodete y bufanda mostaza); objeto de mano `lapiz` solo en las tomas 11 y 12 y en el fotograma de firma | personajes/tan/referencias/principal_tin_y_tan.png |
| @tin | Responde con un dato por plano. Lado derecho, sin espejo. **Va sin lápiz en el plano de firma** (el lápiz es de Tan en f0 a f14 y en los 30 fotogramas finales). | base de su ficha (gorra marrón, lentes, lápiz); `objeto="lapiz"` en las tomas 3 a 6, 9, 10 y 11; `objeto=False` en las tomas 1, 7, 8 y 12 (el acento es el tomate) | personajes/tin/referencias/principal_tin_y_tan.png |

No se sube nada a un generador: las referencias son el diseño en código (`herramientas/palitos.py`, versión 1.4) y solo sirven para comparar. **Jensen Huang, Steve Jobs, Sam Altman, Bob Iger, Michael Dell y Jack Dorsey no aparecen dibujados ni imitados ni se les cita: solo se les nombra.** Poses y expresiones usadas (todas existen en `POSES` y `EXPRESIONES` de `palitos.py` 1.4, comprobado el 2026-11-24): `parado`, `explica`, `senala`, `pregunta`, `encoge`, `saluda`; `curiosidad`, `sorpresa`, `feliz`, `risa`. **No se usan** `pensando` ni `concentrado` (se leen como enojo), ni `celebra` ni `eureka` (festejo sobre un dato de una salida), ni la cara `neutra` de Tin (sigue sin existir en `palitos.py` ni en su ficha: en los datos se usan `curiosidad` y `sorpresa`). `alto` = 505 px (26,3 % del alto) en todos los planos con la banda de subtítulos; 487 px en la portada.

## 3. Idea en una línea

Tan pregunta lo que el público se pregunta, «Jensen Huang volvió como CEO en 11 días: ¿quién tardó más?», y Tin responde con un nombre y una barra por plano, cada una más larga que la anterior: Bob Iger 999 días, Michael Dell 1.063, Jack Dorsey 2.449 y Steve Jobs 4.382 (casi 12 años). Remate: solo Sam Altman, con 5 días, fue más rápido que Huang; los otros cuatro tardaron más. Pregunta nueva: ¿cuánto duraron tras volver? Emoción: curiosidad → asombro creciente → pico → curiosidad nueva. El lápiz de Tan hace de bumerán: vuelve al empezar y sale lanzado al terminar.

**Decisiones del equipo (2026-11-24), todas con su porqué** (el detalle y las fuentes están en `00_brief.md`):

1. **Forma: ranking de seis, medido en días sin el cargo, con Huang como vara.** Responde «who else came back» con un número por persona y la barra más larga sube el asombro (R37, `manual/14`). Mismo método para todos: del día en que deja el puesto de director ejecutivo al día en que vuelve a él, con las dos fechas con día exacto y fuente (Wikipedia en inglés, 2026-11-24; cálculo con `datetime`). Los matices (quién fue destituido, quién siguió en la empresa) van en la descripción.
2. **Se sostiene sin haber visto el short 3:** la pregunta de apertura trae el dato de Huang y la incógnita en una sola frase. Para quien lo vio, Huang es la vara que ya conoce.
3. **Entran seis; quedan fuera Schultz y Page** (a Schultz le falta el día de su salida de 2000 y tuvo tres etapas; a Page, el día de agosto de 2001). No se afirma «todos» ni «el más largo de la historia»: la voz dice «the other four», no «everyone».
4. **El pico es Jobs, 4.382 días, al 61,7 % del video** (≤ 75 %). La voz dice «almost twelve years» porque son 12 años menos un día; la tarjeta en español, «¿Casi 12 años?», y la descripción, «≈ 12 years»: los tres coinciden (lección del short 3). **Se repite el dato de Jobs del short 3:** riesgo declarado en el perfil emocional; se justifica porque la pregunta no se contesta sin la barra más larga y todo lo demás es nuevo.
5. **Nadie sonríe sobre una salida.** En los datos, `curiosidad` y `sorpresa`; `risa` y `feliz` solo en el remate y la invitación. Ni la voz ni la pantalla dicen cómo ni por qué salió nadie.
6. **Cierre decidido con la tabla del manual 14, 4b.3:** respuesta con remate («The other four took longer.») + una pregunta nueva, abierta y respondible por el canal («How long did they stay after coming back?») que es la razón de la **única** invitación («Subscribe for the next count.») + el lápiz lanzado. No se cierra con una pregunta de suspenso sobre una persona. **Compromiso:** el siguiente conteo es el de permanencia tras volver (fechas ya leídas en `00_brief.md`); se publica en 7 días o se avisa en un comentario fijado.
7. **Portada que nombra al sujeto** (regla del dueño, 2026-11-24): «CEO Comebacks / Huang 11 Days / vs. Jobs?» con «CEO» y dos nombres que la gente busca; el «11» (la vara, no la respuesta) en mostaza; el número de Jobs queda oculto. Tan con `sorpresa`, Tin con `sorpresa`, los dos mirando la silla.
8. **Acento por plano:** mostaza en todo el video y **tomate solo en la cifra del pico** (tomas 7 y 8), como en los shorts 2 y 3 (R26, R33). El cuerpo del lápiz, la bufanda y la goma del lápiz son identidad, no acento.
9. **Sin paralaje ni cámara en movimiento en los planos con gráficos:** se leen nombres de 56 px y cifras; el movimiento de cámara sobre texto que se lee va contra `manual/14` (R44) y el short 3 ya mostró que la profundidad se logra con capas, sombras y desenfoque fijo. El único movimiento grande del video es el del lápiz.
10. **Firma del lápiz bumerán** (`FIRMA_LAPIZ_BUMERAN.md`, ya programada en `efectos.py` 1.1 y `palitos.py` 1.4): Tan atrapa en el fotograma 10, la voz entra en el 14, Tin va sin lápiz, el cierre dura 30 fotogramas y el último empalma con el primero.
11. **Subtítulos en español quemados** (encargo del dueño): banda fija entre gráficos y cabezas, tarjetas de dos renglones de ≈ 21 caracteres con la cifra y «días»; sin subtítulo en la portada ni en el cierre.
12. **Una sola mención de cifras con decimales:** «≈ 6.7 years» (2.449 días) va solo en la descripción; en voz y pantalla es «almost seven years» y «¿Casi 7 años?».

## 4. Estilo global

```text
Flat 2D vector drawing on warm cream paper (#F3E9D2) with a faint fixed paper grain and soft vignette, 1970s palette: two neutrals (cream paper, dark ink) plus ONE accent per shot (mustard in every shot except the reveal shots, tomato red only in the reveal shots), character colors (orange, brown, teal) and the pencil (mustard body, red eraser) are identity and not accents, thick dark ink outlines (#2B2420), hand-made stick-figure look, layered depth with contact shadows under feet and objects, distant layers lightly blurred and faded into the paper, no gradients on shapes, no glow, no neon, spring-based motion, fixed camera while any number is on screen.
```

**Negativo global:**

```text
text inside the drawing other than the tables in section 12, brand names or logos, Nvidia, Disney, Dell, Twitter, Apple or OpenAI logo lettering or brand colors, any real person drawn or imitated, faces of real people, photographs, stock charts, money, flags, courtroom or police imagery, neon, gradients on shapes, lens flare, flashes, strobing, negative-color effect, whole-screen white or black, two accent colors in the same shot (the pencil body and the scarf are identity and do not count), tomato red outside the reveal shots (the pencil eraser does not count), extra characters, extra fingers, characters other than Tin and Tan, uppercase centered titles, square placeholder glyphs, symbols that are not in the font, lying-down shadow under the stick figures, smiles on facts about someone leaving a job
```

## 5. Escenarios

- **papel_crema:** fondo `#F3E9D2` con grano fijo y viñeta suave (`efectos.papel`, el mismo grano en todos los fotogramas). Con personajes: línea de suelo `#E6D8B8` de 4 px a **86 % del alto (y = 1651)**, de 9,3 % a 90,7 % del ancho.
- **Zonas (1080x1920), zona segura de `formatos.md`:** x 100–980, y 250–1670.
  - **Texto en inglés (rótulos de cifra):** x = 10 % (108), de y = 13,2 % a 24 % (253–461); cifras al 7 % del alto (134 px).
  - **Gráfico del ranking:** y 480–888, x 100–980 (hueco ≥ 16 px con la banda de subtítulos, que empieza en 905).
  - **Banda de subtítulos en español:** y 905–1085 (47,1 % a 56,5 %), x 100–980 (sección 12).
  - **Personajes:** pies a 86 % (y = 1651), `alto` 505 px, cabeza más alta en y ≈ 1146; nunca pisan la banda ni los gráficos. Tan en x = 30 % con `espejo=True`; Tin en x = 70 % sin espejo; solos, en x = 50 %.
  - **Portada (toma 1 y toma 12):** texto en y 400–700, silla en y 720–1100, caras dentro de x 60–960, y 380–1440.
- **Profundidad (`efectos.componer`):** la z 0 es el plano de los personajes y del gráfico; positivo = más lejos. Capas lejanas (silla a z +420) se funden con el papel con `niebla` 0,30 y desenfoque fijo `apertura` 0,018; **sin movimiento de cámara en ningún plano con gráficos** (decisión 9). Sombras de contacto (opacidad 0,25 a 0,30) bajo pies y objetos. **Sin sombra tumbada de los muñecos.**
- **silla_director (gráfico propio, el objeto que cuenta el tema; genérica, vacía y sin marca):** silla plegable de director vista de frente y tres cuartos: dos patas en X de madera marrón `#7A4B2A` con contorno tinta de 0,03 H, travesaño, brazos y respaldo y asiento de lona **papel sombra `#E6D8B8`** con dos costuras de tinta; sin letras, sin nombre en el respaldo. Alto H, ancho 0,95 H. En la portada H = 380 px (y 720–1100, centrada en x = 540); en el fotograma 0 está a escala 0,82 (H = 312) y crece a 1,0 en 12 fotogramas con frenada. Es la misma del short 3: el objeto que identifica los videos de directores ejecutivos (R26).
- **ranking (gráfico propio, escala lineal y honesta):** seis filas de **68 px**, de y = 480 a 888, fila 0 arriba: fila 0 Altman (480–548, vacía hasta 22,62 s), fila 1 Huang (548–616), fila 2 Iger (616–684), fila 3 Dell (684–752), fila 4 Dorsey (752–820), fila 5 Jobs (820–888). **Nombre de cada fila a 56 px (2,9 % del alto)**, en tinta, a la izquierda desde x = 100 (el más ancho, «Altman», mide 178 px). **Barras de 40 px de alto** (28 px entre filas), de x = 320 a 980: **660 px = 4.382 días (0,1506 px por día)**: Iger 150 px, Dell 160 px, Dorsey 369 px, Jobs 660 px. **Huang (11 días ≈ 1,7 px) y Altman (5 días ≈ 0,8 px) llevan una marca mínima de 8 px con borde de tinta de 2 px**; es una convención anotada en la descripción («the two shortest are drawn at a minimum width»), no un engaño. Relleno: la barra del plano en curso en mostaza con borde de tinta de 2 px (acento); las ya contadas, en marrón `#7A4B2A` con borde de tinta de 2 px; la marca mínima en mostaza con borde cuando es el acento del plano y en tinta cuando no. **Sin letras dentro de las barras.** Los números no van junto a la barra: van en el rótulo grande y en la tarjeta en español.
- **lápiz libre (gráfico propio, firma del canal):** el lápiz de la ficha de Tin (cuerpo mostaza, punta naranja, goma tomate, contorno tinta) de 2,4 R de largo (R = radio de cabeza) que gira libre con estela plana de dos copias (a los ángulos de 2 y 4 fotogramas antes). Escala de vuelo hasta 1,7 (`FIRMA_LAPIZ_BUMERAN.md` 0b). Las funciones ya existen: `efectos.geometria_firma`, `lapiz_bumeran`, `pintar_lapiz_volador`, `golpes_firma`, `comprobar_firma`.
- **Muelles (masa 1, rigidez, amortiguación) por elemento:** `pop` 220 y 20 (entradas de texto y de filas, escala de 0,85 a 1); `slide` 120 y 16 (personajes y gráficos que se desplazan); `sello` 320 y 26 (zoom de golpe). Contadores y barras: ease-out cúbico, sin muelle, para que el valor nunca pase de su final ni retroceda. Todo depende del número de fotograma (30 fps).
- **Transición entre tomas:** corte seco; cero destellos. No hay desenfoque de movimiento de transición en este video (no hay revelado).

## 6. Tomas

<!--
Todas las tomas son «edición»: dibujo por código. Tiempos al décimo de segundo, del video final (31,0 s, 930 fotogramas), sobre la voz ESTIMADA. Cada corte cae en un pulso de 0,5 s, entre 0,0 y 0,35 s antes del inicio de la línea que le toca.
-->

### Toma 1 — Gancho: la silla vacía y el lápiz que vuelve

- **Duración:** 1,0 s (de 0,0 a 1,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la portada: texto «CEO Comebacks / Huang 11 Days / vs. Jobs?» arriba (y 400–700), la silla_director en el centro (y 720–1100), Tan y Tin debajo, de perfil, mirando la silla
- **Cámara:** fija, escala 100 %
- **Acción:** el lápiz ya viene girando de vuelta desde el fotograma 0 (estela plana) y **Tan lo atrapa en el fotograma 10**; la silla crece de 0,82 a 1,0 en 12 fotogramas; «11» da su golpe de escala en el fotograma 6; la voz de Tan entra en el fotograma 14.
- **Audio:** línea 1, Tan (primera parte): "Jensen Huang came back as C E O in eleven days." (entra en 0,47 s). Vuelo con vibrato de 0,0 a 0,33 s y golpe seco al atrapar en 0,33 s (sección 13).
- **Referencia:** toma 1 del short 3 (misma geometría de portada y de firma)
- **Transición de entrada:** ninguna (primer fotograma; es también el último del bucle). Salida: corte en el movimiento hacia la toma 2.

**Especificación de dibujo:**

- Fotograma 0: lápiz libre en el punto de partida de `efectos.geometria_firma` con la misma geometría de portada del short 3 (Tan x 24 %, Tin x 76 %, perfil, pies a 86 %, `alto` 487 px, cabeza a 25 grados); **el último fotograma del video (el 929) es el instante anterior del mismo vuelo** (diferencia media menor de 3 de 255). Medidas que se comprueban con `comprobar_firma` en todos los fotogramas de la firma: lápiz a **8 px o más de cualquier cabeza**, a 30 px o más del texto y de la silla, centro dentro de x 60–960, y 380–1440 (FIRMA §11).
- Brazo de Tan en el empalme, al soltar y al atrapar: `BD_FIRMA` de `efectos.py` 1.1 (95°, 108°). Atrapada en el fotograma 10 con retroceso del brazo (−10°) y del cuerpo (−6 px); la oscilación del lápiz baja a menos de 2 grados en el fotograma 25.
- Texto «CEO Comebacks / Huang 11 Days / vs. Jobs?» entero y quieto desde el fotograma 0 (es la portada; sin `pop` de entrada), tres renglones a 92 px (≈ 4,8 % del alto), alineado a la izquierda en x = 108, de y = 400 a ≈ 690; **medidas con la fuente: «CEO Comebacks» 703 px, «Huang 11 Days» 585 px, «vs. Jobs?» 384 px**, todas dentro de x 100–980 también con el golpe de escala de 1,18 (829, 691 y 453 px). Hueco ≥ 30 px hasta la silla (y 720). Clave «11» en mostaza con contorno de tinta de 0,045 em; golpe de la clave en el fotograma 6 (escala 1,0 a 1,18 en 5 fotogramas y asiento en 7). El texto sale a los 0,9 s.
- Tan: pose `pregunta`, **expresión `sorpresa`** (la cara de curiosidad se leyó como duda en el short 3), vista `perfil`, `mira=1`, `cabeza_giro=25`, `espejo=True`. Tin: pose `parado`, expresión `sorpresa`, vista `perfil`, `mira=-1`, `cabeza_giro=25`, **`objeto=False`**. Las caras quedan dentro de la zona útil de portada. Con suelo.
- **Sin subtítulo en español** (portada). **Color:** acento mostaza = la clave «11» + el lápiz (cuerpo mostaza: identidad del objeto, un solo acento usado en el título y en un elemento); silla neutra.

### Toma 2 — Huang, la vara de medir

- **Duración:** 3,0 s (de 1,0 a 4,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tan sola, de frente, con la fila de Huang en el gráfico y la silla pequeña al fondo (capa lejana)
- **Cámara:** fija
- **Acción:** el brazo de Tan sigue subiendo a través del corte mientras termina la pregunta; entra la fila 1 con su nombre «Huang» y su marca de 8 px; el rótulo «11 days» entra cuando la voz dice «eleven days».
- **Audio:** línea 1, Tan (resto): «…as C E O in eleven days. Who took longer?» (hasta 4,08 s). Clic suave del corte; pop de la fila.
- **Referencia:** toma 2 del short 3 (Tan pregunta tras el corte en el movimiento)
- **Transición de entrada:** corte en el movimiento (4 fotogramas después de que arranca el brazo; el primer plano dura 30 fotogramas). Salida: corte seco.

**Especificación de dibujo:**

- Capas: papel z +900; silla_director z +420 (niebla, x = 540); ranking y Tan z 0. Tan: pose `pregunta`, expresión `curiosidad`, vista `frente`, `mira=1`, `espejo=True`, x = 50 %, pies a 86 %, `alto` 505 px, `viento` oscilante con muelle.
- Fila 1: nombre «Huang» con `pop` en 1,20; marca mínima de 8 px mostaza con borde de tinta, `pop` en 1,40. Rótulo «11 days» (clave 11) con `pop` en 2,40, hasta 3,95. Tarjetas ES 1 (1,00 a 3,20) y 2 (3,25 a 4,30; cruza el corte de 4,0 s).
- **Color:** acento mostaza = la clave «11» + la marca de Huang. La silla, neutra. Con suelo.

### Toma 3 — Bob Iger, 999 días

- **Duración:** 3,5 s (de 4,0 a 7,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el ranking arriba: filas 1 (Huang) y 2 (Iger)
- **Cámara:** fija
- **Acción:** entra el nombre «Iger»; la barra de 150 px crece cuando la voz dice el número; Tin explica con el lápiz; Tan mira la barra con curiosidad.
- **Audio:** línea 2, Tin: "Bob Iger at Disney: nine hundred ninety-nine days." (de 4,31 a 7,29 s). Clic del corte; pop del nombre; deslizar de la barra.
- **Referencia:** toma 9 del short 3 (Tin explica con la barra)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Fila 2: nombre «Iger» con `pop` en 4,40; barra mostaza de 150 px, ease-out cúbico de 5,77 a 6,50 (22 fotogramas). La marca de Huang pasa a tinta y su nombre queda. Rótulo «999 days» (clave: el número) con `pop` en 5,77 (cuando la voz empieza el número), hasta 7,45. Tarjeta ES 3: «Bob Iger, Disney:» desde 4,31 y segundo renglón «999 días.» desde 5,77, hasta 7,45.
- Tin: pose `explica`, expresión `curiosidad`, `objeto="lapiz"`, x = 70 %, lápiz con movimiento secundario de ±3 grados. Tan: pose `pregunta`, expresión `curiosidad`, `espejo=True`, x = 30 %.
- **Color:** acento mostaza = la clave «999» + la barra de Iger (el lápiz es identidad). Con suelo.

### Toma 4 — Michael Dell, 1.063 días

- **Duración:** 3,0 s (de 7,5 a 10,5)
- **Personajes:** @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tin solo, de frente, con el ranking arriba: filas 1 a 3
- **Cámara:** fija
- **Acción:** entra el nombre «Dell»; la barra de 160 px crece al decir el número; Tin señala la barra.
- **Audio:** línea 3, Tin: "Michael Dell at Dell: one thousand, sixty-three days." (de 7,52 a 10,43 s). Clic del corte; pop del nombre; deslizar de la barra.
- **Referencia:** toma 7 del short 2 (cifra grande con Tin)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Fila 3: nombre «Dell» con `pop` en 7,60; barra mostaza de 160 px de 8,75 a 9,50; la barra de Iger pasa a marrón. Rótulo «1,063 days» (clave: el número) con `pop` en 8,75, hasta 10,45. Tarjeta ES 4: «Michael Dell, Dell:» desde 7,52 y «1.063 días.» desde 8,75, hasta 10,45.
- Tin: pose `senala`, expresión `curiosidad`, `objeto="lapiz"`, vista `frente`, x = 50 %. Sin segundo personaje en este plano.
- **Color:** acento mostaza = la clave «1,063» + la barra de Dell. Con suelo.

### Toma 5 — Jack Dorsey, 2.449 días

- **Duración:** 4,0 s (de 10,5 a 14,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con el ranking arriba: filas 1 a 4 (el plano cerca de la mitad del video)
- **Cámara:** fija
- **Acción:** entra el nombre «Dorsey»; la barra de 369 px crece al decir el número; Tan abre los ojos y se inclina hacia la barra; Tin explica.
- **Audio:** línea 4, Tin: "Jack Dorsey at Twitter: two thousand, four hundred forty-nine days." (de 10,66 a 14,43 s). Clic del corte; pop del nombre; deslizar de la barra.
- **Referencia:** toma 4 del short 3 (héroe abierto de los dos con el objeto del tema)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Fila 4: nombre «Dorsey» con `pop` en 10,80; barra mostaza de 369 px de 12,11 a 13,00 (27 fotogramas); la de Dell pasa a marrón. Rótulo «2,449 days» (clave: el número) con `pop` en 12,11, hasta 14,45. Tarjeta ES 5: «Jack Dorsey, Twitter:» desde 10,66 y «2.449 días.» desde 12,11, hasta 14,45.
- Tin: pose `explica`, expresión `curiosidad`, `objeto="lapiz"`, x = 70 %. Tan: pose `senala`, expresión `sorpresa`, `espejo=True`, x = 30 %.
- **Color:** acento mostaza = la clave «2,449» + la barra de Dorsey. Con suelo.

### Toma 6 — Tan: «¿casi siete años?»

- **Duración:** 1,5 s (de 14,5 a 16,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tan sola, de frente, con el ranking arriba (filas 1 a 4) y la silla pequeña al fondo
- **Cámara:** fija
- **Acción:** Tan se encoge de hombros con la boca abierta y repite la magnitud en años; el gráfico no cambia de lugar (respiro antes del pico).
- **Audio:** línea 5, Tan: "Almost seven years?" (de 14,83 a 15,80 s). Clic del corte.
- **Referencia:** toma 8 del short 3 (respiro de composición)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Capas: papel z +900; silla z +420; ranking y Tan z 0. Tan: pose `encoge`, expresión `sorpresa`, `espejo=True`, x = 50 %, `alto` 505 px. Rótulo «almost 7 years?» (clave 7) con `pop` en 14,80, hasta 15,95 (34 fotogramas). Tarjeta ES 6: «¿Casi 7 años?» de 14,80 a 15,95. La barra de Dorsey pasa a marrón.
- **Color:** acento mostaza = la clave «7»; sin otro elemento mostaza. Con suelo.

### Toma 7 — El pico: Steve Jobs, 4.382 días

- **Duración:** 4,5 s (de 16,0 a 20,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con las seis filas a la vista y la cifra arriba (pico de emoción)
- **Cámara:** fija; zoom de golpe suave de +10 % en la llegada de la cifra
- **Acción:** entra el nombre «Jobs»; subida de sonido; **silencio de 12 fotogramas**; el contador sube de 0 a 4.382 con ease-out mientras la barra de Jobs crece a 660 px; al llegar, la cifra pasa a tomate y el zoom da su golpe; Tan se asombra y Tin levanta la mano vacía.
- **Audio:** línea 6, Tin: "Steve Jobs at Apple: four thousand, three hundred eighty-two days." (de 16,20 a 20,27 s; el número empieza ≈ 17,73). Riser de 16,45 a 17,28, silencio de 17,28 a 17,68, tictac del contador y ding en la llegada.
- **Referencia:** toma 10 del short 3 (contador final)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Ranking completo menos Altman: filas 1 a 5. Nombre «Jobs» con `pop` en 16,35. Barra de Jobs en marrón (no en mostaza: el único acento del plano es el tomate), de 0 a 660 px con el contador. Las marcas de Huang y las barras anteriores en tinta y marrón.
- Contador de 0 a 4.382 (enteros, formato inglés con coma en pantalla) `fx.contador` de **17,93 a 19,13 s (36 fotogramas)**, ease-out cúbico, solo sube y nunca pasa de 4.382; arranca 0,2 s después de que la voz empieza el número y llega **0,4 s o más antes de que la voz termine** (si la voz real es más corta, se reajusta con ella); en tinta mientras sube y en **tomate `#C8553D` con contorno de tinta de 0,045 em** al llegar, con `pop` del texto en ese mismo fotograma. `golpe_de_zoom` de +10 % (5 fotogramas de ida y 8 de asiento) en 19,13. Cifra quieta desde 19,13 y a través del corte (86 fotogramas hasta 22,0, más de los 45 mínimos).
- Rótulo «4,382 days» (arriba, 7 %): entra con el contador (17,93). Tarjeta ES 7: «Steve Jobs, Apple:» de 16,20 a 20,85 y, **como segundo renglón, «4.382 días.» desde la llegada del contador (19,13) hasta 20,85 (1,7 s nítida)**, para no adelantar la cifra.
- Tan: pose `senala`, expresión `sorpresa`, `espejo=True`, x = 30 %. Tin: pose `saluda`, expresión `sorpresa`, **`objeto=False`** (sin lápiz: aquí el único acento es el tomate), x = 70 %.
- **Color (revelación):** acento tomate = la cifra; nada mostaza como acento (la bufanda de Tan es identidad). Con suelo.

### Toma 8 — Tan: «¿casi doce años?» (la cifra queda quieta)

- **Duración:** 1,5 s (de 20,5 a 22,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tan sola con la cifra en tomate arriba y las cinco filas detrás
- **Cámara:** fija
- **Acción:** Tan se encoge de hombros con la boca abierta; la cifra no se mueve (respiro de 60 a 90 fotogramas tras el pico, sin efectos).
- **Audio:** línea 7, Tan: "Almost twelve years?" (de 20,87 a 21,84 s). Clic del corte.
- **Referencia:** toma 11 del short 3
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `encoge`, expresión `sorpresa`, `espejo=True`, x = 50 %, `alto` 505 px. Rótulo «4,382 days» en tomate, el mismo de la toma 7, hasta 21,95. Tarjeta ES 8: «¿Casi 12 años?» de 20,87 a 21,95 (1,08 s; justa: no acortar). **Color:** acento tomate = la cifra; sin mostaza. Con suelo.

### Toma 9 — Altman: el único más rápido que Huang

- **Duración:** 3,0 s (de 22,0 a 25,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con las seis filas a la vista
- **Cámara:** fija
- **Acción:** la cifra en tomate sale; entra la fila 0 con «Altman» y su marca de 8 px en mostaza, **arriba de la de Huang**; el rótulo «5 days» entra con la voz; Tin explica y levanta el lápiz; los dos con `curiosidad`.
- **Audio:** línea 8, Tin (primera parte): "Only Sam Altman was faster than Huang: five days." (de 22,19 a 24,94 s). Clic del corte; pop de la fila.
- **Referencia:** toma 12 del short 3 (remate con los dos)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Fila 0: nombre «Altman» con `pop` en 22,62 (cuando la voz dice «Sam Altman»); marca de 8 px mostaza con borde de tinta, `pop` en 22,80. Las demás filas en tinta y marrón (la de Jobs, marrón). Rótulo «5 days» (clave 5) de 24,45 a 25,50 (entra con «five days»). Tarjeta ES 9: «Solo Altman fue más / rápido: 5 días.» de 22,19 a 25,05 (los dos renglones juntos: es la misma frase y el rótulo grande ya coincide con la voz).
- Tin: pose `explica`, expresión `curiosidad`, `objeto="lapiz"` (vuelve el lápiz), x = 70 %. Tan: pose `pregunta`, expresión `curiosidad`, `espejo=True`, x = 30 %.
- **Color:** acento mostaza = la clave «5» + la marca de Altman. Sin tomate. Con suelo.

### Toma 10 — Remate: los otros cuatro tardaron más

- **Duración:** 2,0 s (de 25,0 a 27,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con las seis filas a la vista (el ranking completo)
- **Cámara:** fija
- **Acción:** el rótulo «4 took longer» entra; Tin asiente y levanta el lápiz; Tan se ríe (alegría solo aquí y en la invitación: ya no se habla de una salida sino de una cuenta resuelta).
- **Audio:** línea 8, Tin (resto): "The other four took longer." (de 25,09 a 26,61 s). Clic del corte.
- **Referencia:** toma 12 del short 2 (remate con los dos)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Mismo ranking de la toma 9, sin movimiento: Altman, Huang, Iger, Dell, Dorsey y Jobs, cada uno con su nombre y su barra. Rótulo «4 took longer» (clave 4) de 25,55 a 26,95. Tarjeta ES 10: «Los otros cuatro / tardaron más.» de 25,09 a 26,95.
- Tin: pose `explica`, expresión `risa`, `objeto="lapiz"`, x = 70 %. Tan: pose `encoge`, expresión `risa`, `espejo=True`, x = 30 %.
- **Color:** acento mostaza = la clave «4» (y el lápiz como identidad). Sin tomate. Con suelo. El ranking sale a 26,90.

### Toma 11 — Pregunta final e invitación; el lápiz pasa a Tan

- **Duración:** 3,0 s (de 27,0 a 30,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano de los dos con la silla de director vacía entre ellos (el plano del fotograma 0, más pequeño)
- **Cámara:** fija, escala 100 %
- **Acción:** Tan pregunta «¿cuánto duraron tras volver?», Tin le pasa el lápiz en un arco corto (28,50 a 28,77) y Tan dice la invitación con el lápiz en la mano.
- **Audio:** línea 9, Tan: "How long did they stay after coming back? Subscribe for the next count." (de 26,96 a 30,19 s). Una sola invitación. Whoosh corto del pase del lápiz.
- **Referencia:** toma 13 del short 3 (cierre de firma)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Silla_director (H = 312, a escala 0,82, centro x = 540, y 754–1066 como en el fotograma 0) entre los dos; Tan: pose `pregunta`, expresión `curiosidad`, vista `frente`, `espejo=True`, x = 30 %; Tin: pose `explica`, expresión `feliz`, x = 70 %. Lápiz libre que pasa de Tin a Tan en 8 fotogramas (28,50–28,77) con giro de media vuelta; desde 28,77 Tan lleva `objeto="lapiz"` y Tin `objeto=False`.
- Rótulos: «How long?» (clave: long) de 27,05 a 28,85; «Subscribe» (clave) de 28,93 a 29,97. Tarjeta ES 11: «¿Cuánto duraron / tras volver?» de 26,96 a 28,90; tarjeta ES 12: «Suscríbete al próximo / conteo.» de 28,93 a 29,97.
- **Color:** acento mostaza = la clave y el lápiz. Con suelo.

### Toma 12 — Cierre en bucle: Tan lanza el lápiz

- **Duración:** 1,0 s (de 30,0 a 31,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** el plano de la toma 11 que se transforma en el de la portada
- **Cámara:** fija, escala 100 %
- **Acción:** Tan, con el lápiz, hace la **anticipación** (6 fotogramas hacia atrás, f906 a f911, de 30,20 a 30,37) y lo **lanza** girando (suelta en f915, 30,5 s); el lápiz sale hacia arriba y hacia la cámara; el último fotograma (f929) es el instante anterior al fotograma 0.
- **Audio:** sin voz (la voz termina en ≈ 30,19, 24 fotogramas antes del final: el límite es 17). Crujido de anticipación y whoosh con vibrato atado al giro (sección 13).
- **Referencia:** toma 1 de esta versión (el vuelo del lápiz cierra el bucle)
- **Transición de entrada:** corte seco. Salida: bucle al fotograma 0 de la toma 1.

**Especificación de dibujo:**

- De 30,0 a 30,2 plano fijo con los dos de frente, respirando (acción secundaria). Sin corte, se pasan a la composición de la portada (personajes de perfil con la cabeza a 25 grados) en 6 fotogramas de `slide`; **el último fotograma debe ser el paso de vuelo anterior al fotograma 0** (diferencia media menor de 3 de 255). Lápiz libre con estela, escala de 1,0 a 1,7, giro horario de 330° con aceleración, trayectoria de `efectos.geometria_firma`. Expresiones de Tan y Tin: las de la portada (`sorpresa`), no `concentrado`.
- Texto «CEO Comebacks / Huang 11 Days / vs. Jobs?» entra con `pop` en 30,0 y llega a escala 1 antes del final, igual que el fotograma 0. Sin subtítulo en español de 29,97 a 31,0 (cuadro de portada limpio). **Color:** acento mostaza = la clave «11» + el lápiz. Con suelo.

## 7. Audio

- **Voz (por generar; una sola generación por voz, regla de un solo intento):** Tan con Zelda (líneas 1, 5, 7 y 9) y Tin con Kevin (líneas 2, 3, 4, 6 y 8), Higgsfield `seed_audio`, voces ya elegidas por el dueño. Después, `atempo=1.10`, −14 LUFS y armado del diálogo como en el short 3 (0,23 s o más entre líneas, pausas internas largas acortadas a 0,15 s, salvo la de «Apple:», que se deja de 0,45 s a propósito para el silencio antes del número). **Costo: por cotizar con `estimate_audio_cost` antes de pedir el sí del dueño** (por analogía con el short 3, 3,7 créditos, y con la prueba de voces, ≈ 3,5 créditos; no es una cotización). Nadie ha oído las voces: «Iger», «Huang», «Dorsey», «C E O» y «Twitter» se comprueban al oído; si el generador lee mal un nombre, se pide autorización para regenerar esa voz (no hay segundo intento por cuenta propia).

Guion de voz (líneas numeradas, quién habla, texto exacto, inicio y fin estimados):

| Línea | Quién | Empieza (s) | Termina (s) | Dura (s) | Texto exacto (números como se dicen) | Sílabas |
|---|---|---|---|---|---|---|
| 1 | Tan | 0,47 | 4,08 | 3,61 | Jensen Huang came back as C E O in eleven days. Who took longer? | 18 |
| 2 | Tin | 4,31 | 7,29 | 2,98 | Bob Iger at Disney: nine hundred ninety-nine days. | 13 |
| 3 | Tin | 7,52 | 10,43 | 2,91 | Michael Dell at Dell: one thousand, sixty-three days. | 12 |
| 4 | Tin | 10,66 | 14,43 | 3,77 | Jack Dorsey at Twitter: two thousand, four hundred forty-nine days. | 16 |
| 5 | Tan | 14,83 | 15,80 | 0,97 | Almost seven years? | 5 |
| 6 | Tin | 16,20 | 20,27 | 4,07 | Steve Jobs at Apple: four thousand, three hundred eighty-two days. | 16 |
| 7 | Tan | 20,87 | 21,84 | 0,97 | Almost twelve years? | 5 |
| 8 | Tin | 22,19 | 26,61 | 4,42 | Only Sam Altman was faster than Huang: five days. The other four took longer. | 19 |
| 9 | Tan | 26,96 | 30,19 | 3,23 | How long did they stay after coming back? Subscribe for the next count. | 16 |

Voz total estimada de 0,47 a 30,19 s; los 0,81 s finales no llevan voz y al volver al fotograma 0 la voz entra sin silencio inicial (silencio del empalme: 0,81 + 0,47 = 1,28 s, menos de 2 s). Pausas elegidas a propósito: 0,40 s antes de la línea 5 y de la 6 (los cortes de 14,5 y 16,0 caen justo antes), 0,60 s antes de la línea 7 (silencio tras el pico), 0,35 s antes de la 8 y 0,35 s antes de la 9.

**Pregunta de apertura:** línea 1 («Who took longer?»). **Pregunta de cierre:** línea 9 («How long did they stay after coming back?»). **Respuesta a la de apertura:** línea 8 («The other four took longer.»).

**Texto para generar cada voz (una pieza por personaje; líneas separadas por una línea en blanco; la última es una coletilla descartable para que no llegue cortada la última palabra útil; sin comas en las líneas de Tan: Zelda hace pausas de 0,7 a 0,8 s tras una coma; sin cifras con dígitos y con las siglas separadas):**

Voz de Tan (Zelda), una sola generación, 4 líneas y coletilla:

```text
Jensen Huang came back as C E O in eleven days. Who took longer?

Almost seven years?

Almost twelve years?

How long did they stay after coming back? Subscribe for the next count.

That's all, folks.
```

Voz de Tin (Kevin), una sola generación, 5 líneas y coletilla:

```text
Bob Iger at Disney: nine hundred ninety-nine days.

Michael Dell at Dell: one thousand, sixty-three days.

Jack Dorsey at Twitter: two thousand, four hundred forty-nine days.

Steve Jobs at Apple: four thousand, three hundred eighty-two days.

Only Sam Altman was faster than Huang: five days. The other four took longer.

That's all, folks.
```

- **Subtítulos:** `02_prompt/subtitulos.srt` (inglés, igual que la voz, 9 líneas) y `02_prompt/subtitulos_es.srt` (español completo, pista para YouTube, 9 líneas). Tiempos estimados.
- **Música:** hecha con código (Python y numpy), **re menor (eólico)** a 120 BPM (el pulso de la rejilla), a −24 LUFS (10 dB bajo la voz): ostinato de bajo en corcheas, pad suave y un riser que sube de 16,45 a 17,28 s; calla 12 fotogramas en 17,28–17,68 s y en 19,13 entra un acorde de **re mayor** abierto con el ding (de tensión a asombro). **Distinta de la del short 2 (do mayor) y de la del short 3 (mi menor a mi mayor)**; las de los shorts 1 a 3 se comprueban en sus `licencias.md` antes de componer. Sin música de terceros.
- **Efectos:** los de la sección 13, hechos con código, sin material de terceros.

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → … → Toma 12 (y vuelve a la toma 1). Las tomas 1 y 12 comparten el vuelo del lápiz.
- **Transiciones (todas motivadas):** corte en el movimiento (1 a 2), corte seco en el resto. Sin revelado, sin barridos, sin destellos, sin negativo, sin «atravesar la escena», sin congelado.
- **Texto en pantalla:** se dibuja en el mismo render: los rótulos en inglés de la sección 12 y la banda de subtítulos en español. El texto nunca contradice lo que se oye.
- **Portada:** el fotograma 0 cumple la regla del dueño (`ENTREGA_YOUTUBE.md`, «Portada de los Shorts», con la regla nueva del 2026-11-24 en `DESIGN.md`): «CEO Comebacks / Huang 11 Days / vs. Jobs?» (tres renglones a 92 px, mayúscula inicial en cada palabra, clave «11» en mostaza) entre y 400 y 700; **el texto nombra al sujeto con las palabras que la gente busca («CEO» y los apellidos Huang y Jobs)**; la silla de director vacía en el centro (y 720–1100); las caras de Tan y Tin, de perfil y con la cabeza a 25 grados, mirándola y con `sorpresa`, dentro de la zona útil (x 60–960, y 380–1440). **Excepción a «sin la respuesta ni el número»:** el «11» va a la vista por decisión del equipo (`PARAMETROS.md`: «La cifra en el título o en la portada: se decide por video»); es la vara y no la respuesta (la respuesta es el número de Jobs, que queda oculto). El video cumple lo que promete la portada: compara a Huang con Jobs y con otros cuatro. `codigo/miniatura.py` guarda el fotograma 0 como `06_final/portada_short04.png` (1080x1920) y mide las cajas.
- **Formato de salida:** 1080x1920, 30 fps, H.264, yuv420p, AAC a 48 kHz. Archivo `06_final/tin_y_tan_short04_v1.mp4`. Pesa unos 3 MB: se recomprime a CRF 22 si pasa de 3,1 MB.
- **Título de la publicación (inglés):** CEO Comebacks Ranked: Jensen Huang vs. Steve Jobs
- **Descripción de la publicación (en inglés, obligatoria; con una línea de suscripción):**

```text
How long can a CEO be gone and still come back? We counted six comebacks, in days.

Jensen Huang, Nvidia: resigned as CEO on Nov 12, 2026; the board reinstated him on Nov 23, 2026. That is 11 days, our yardstick.

Counted the same way for everyone, from the day the person left the CEO job to the day the person was back in it:
Sam Altman, OpenAI: removed Nov 17, 2023; reinstated Nov 22, 2023: 5 days.
Jensen Huang, Nvidia: Nov 12 to Nov 23, 2026: 11 days.
Bob Iger, Disney: Feb 25, 2020 to Nov 20, 2022: 999 days.
Michael Dell, Dell: Mar 4, 2004 to Jan 31, 2007: 1,063 days.
Jack Dorsey, Twitter (now X): Oct 16, 2008 to Jul 1, 2015, as interim CEO: 2,449 days (≈ 6.7 years).
Steve Jobs, Apple: resignation letter Sep 17, 1985; named interim CEO Sep 16, 1997: 4,382 days (≈ 12 years).

What the numbers do not say: the exits were different. Altman was removed by the board; Huang and Jobs resigned; Iger, Dell and Dorsey gave up the CEO job and kept other roles (Iger was executive chairman until the end of 2021; Dell and Dorsey stayed on as chairman). Jobs had rejoined Apple earlier, in February 1997, when it bought his company NeXT. We only count days without the CEO title. Bars are to scale; the two shortest are drawn at a minimum width of 8 pixels so they can be seen.

Next count: how long each of them stayed after coming back. Subscribe to Tin & Tan.

Sources, all read on 2026-11-24: Wikipedia, "Jensen Huang"; "Removal of Sam Altman from OpenAI"; "Bob Iger"; "Michael Dell"; "Jack Dorsey"; "Dick Costolo"; "Steve Jobs". Days calculated with Python. We did not open the companies' own announcements.

Not affiliated with Nvidia, OpenAI, Disney, Dell, Twitter, X or Apple. None of the people named is involved in this video.
```

- **Etiquetas (en total, menos de 500 caracteres):** CEO comebacks, CEO comeback, CEO returns, Jensen Huang, Jensen Huang is back, Steve Jobs, Bob Iger, Michael Dell, Jack Dorsey, Sam Altman, Nvidia CEO, Disney CEO, Tin & Tan, shorts
- **Pasan por `revisar_texto.py`:** la descripción, las etiquetas y `subtitulos.srt` con `--idioma en`; `subtitulos_es.srt` con `--idioma es`; los textos de pantalla del código se pasan antes de renderizar. Resultado en la sección 14.
- **Fuentes y fechas:** Wikipedia en inglés, leídas con `curl` el 2026-11-24: «Jensen Huang» (renuncia el 12 y reposición el 23 de noviembre de 2026), «Removal of Sam Altman from OpenAI» (destituido el 17 y repuesto el 22 de noviembre de 2023), «Bob Iger» (Chapek nombrado el 25 de febrero de 2020; regreso el 20 de noviembre de 2022), «Michael Dell» (deja el 4 de marzo de 2004; regresa el 31 de enero de 2007; una sola página), «Jack Dorsey» (Williams director el 16 de octubre de 2008) y «Dick Costolo» (deja el 1 de julio de 2015, Dorsey interino), «Steve Jobs» (carta de renuncia el 17 de septiembre de 1985; nombrado director interino el 16 de septiembre de 1997). **El comunicado de Nvidia y las páginas de las empresas no se abrieron**; el título del NYT sobre Jobs es del 17 de septiembre de 1997 (Wikipedia da el 16): un día de diferencia, declarado.

### Título (ficha)

Filtro: `revisar_titulo.py` **versión 1.1 (modo flexible)**, corrido el 2026-11-24. Estudio y reglas: `video-studio/comercial/titulos.md`.

| Campo | Valor |
|---|---|
| `titulo_elegido` | CEO Comebacks Ranked: Jensen Huang vs. Steve Jobs |
| `caracteres` | 49 |
| `idioma` | en |
| `canal` | tin-y-tan |
| `formato` | short |
| `publico` | EE. UU., adultos que siguen la noticia de Huang o buscan regresos de directores ejecutivos; sin edad fija (manda el dato de Studio) |
| `frase_de_busqueda` | ceo comebacks |
| `fuente_de_la_frase` | títulos de YouTube del 2026-11-24 en `00_analisis_de_tematicas.md` (S2): «CEO Comeback Speedrun: Jobs vs Huang vs Altman», «Steve Jobs Came Back. Can Jensen Huang?»; volumen de búsqueda: sin dato |
| `formula` | búsqueda del tema + «Ranked» (cumple: es un ranking) + los dos nombres que la gente busca |
| `alternativa_1` | CEO Comebacks in Days: Jensen Huang vs. Steve Jobs (50 caracteres; frase «ceo comebacks»; filtro: PASA, 0 errores, 0 avisos) |
| `alternativa_2` | CEO Comebacks Counted: Jensen Huang vs. Steve Jobs (50 caracteres; frase «ceo comebacks»; filtro: PASA, 0 errores, 0 avisos) |
| `descartadas` | «6 CEO Comebacks, Counted: Jensen Huang vs. Jobs» (aviso M11: la marca «Steve Jobs» no aparece) y «Who Took Longer Than Jensen Huang? 4 CEO Comebacks» (3 avisos de posición de la frase) |
| `uso_de_las_alternativas` | Reserva. YouTube no ofrece prueba A/B de títulos en Shorts (ayuda oficial, leída el 2026-11-21). No se cambia un título publicado antes de los 28 días y sin datos del canal |
| `filtro` | **PASA** · errores: ninguno · avisos: ninguno (corrido con `--marca "Jensen Huang" --marca "Steve Jobs" --descripcion` y `--proyecto 2026-11-24_tin_y_tan_ceo_comebacks`) |
| `revision_humana` | **Pendiente**: que el video cumpla lo que el título promete (ranking de seis regresos en días, con Huang y Jobs en los extremos de la comparación), que no engañe («Ranked» es por días sin el cargo, no por importancia) y que pase la línea editorial. Firma el director creativo cuando exista el video |
| `medicion` | Visto frente a deslizado, mostrado en el feed y tráfico de búsqueda por «ceo comebacks» y por los nombres; a 7 y 28 días; meta: superar el 20,7 % del short 1 y comparar con el short 3 |

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | 0 s (las 12 tomas son edición; 31,0 s se resuelven en edición) | 0 |
| Keyframes | 0 | 0 |
| Remates en resolución final | 0 | 0 |
| Voz (Tan con Zelda y Tin con Kevin, una generación por voz) | 2 generaciones, sin generar | por cotizar con `estimate_audio_cost` (referencia del short 3: 3,7 créditos); necesita el sí del dueño |
| **Total estimado** | 0 créditos en imagen y video; voz por cotizar y por autorizar | 0 |

## 10. Restricciones críticas

Van al inicio de cada prompt de video, antes de la descripción. Son las que no se negocian.

```text
CRITICAL: no text, captions, subtitles, logos or watermarks unless listed in section 12.
CRITICAL: the character looks identical in every shot (same design, colors, proportions).
CRITICAL: hard cuts only, no morphing between shots.
CRITICAL: every figure, name or claim on screen comes from the project's facts file, with source and date.
CRITICAL: counters only go up and never pass their final value; no text over a character; no company logo, lettering or brand color; all objects are generic drawings with no logos; no real person is drawn, imitated, quoted or given words; nobody is said to have been fired, to have resigned or to have left for any reason in the voice or on screen; no smile on a fact about someone leaving a job.
CRITICAL: no flashes: at most 2 sudden brightness changes in any second (hard limit 3); no negative-color effect, no go-through-the-scene transition, no strobing.
```

## 11. Gancho, ritmo y cierre

- **Regla formal de la pieza:** un nombre y una barra por plano, cada barra más larga que la anterior; la cifra solo sube; ningún número se lee con la cámara en movimiento; todo corte cae en un pulso de 0,5 s.
- **Rejilla de tiempo:** pulso de 0,5 s; 62 pulsos = 31,0 s. La voz entra en el fotograma 14. Los 11 cortes caen en 1,0; 4,0; 7,5; 10,5; 14,5; 16,0; 20,5; 22,0; 25,0; 27,0 y 30,0 (más el bucle en 31,0). Inicios estimados de la voz: 0,47; 4,31; 7,52; 10,66; 14,83; 16,20; 20,87; 22,19; 26,96 (entre 0,0 y 0,35 s después del corte que les toca; el corte de 4,0 cae 0,31 s antes de la línea 2). Se revisan al oído con la voz real.
- **Gancho (0 a 4 s):** el fotograma 0 es la portada: la silla de director vacía, el lápiz que vuelve (con estela), «CEO Comebacks / Huang 11 Days / vs. Jobs?» entero, Tan y Tin de perfil mirando la silla con `sorpresa`. Tan atrapa el lápiz en el fotograma 10 y su voz entra en el 14. En 1,0 el corte en el movimiento pasa a Tan sola con la vara de Huang. **Una sola incógnita abierta:** ¿quién tardó más?
- **Empieza en movimiento:** sí: el lápiz gira y se acerca desde el fotograma 0, la silla crece y Tan retrocede al atrapar.
- **Motivo visual que vuelve (con las mismas formas y colores):** la silla_director vacía (tomas 1, 2, 6, 11 y 12), el ranking de filas con nombre y barra (tomas 2 a 10) y el lápiz de Tin y de Tan (tomas 1, 3 a 6, 9 a 12).
- **Cierre:** decidido con la tabla de la sección 4b del manual 14 (resumida abajo): **respuesta con remate** (tomas 9 y 10), **una pregunta abierta, nueva y respondible** (toma 11: «How long did they stay after coming back?») **que es la razón de la única invitación** («Subscribe for the next count.») y el lápiz lanzado (toma 12), que empalma con el fotograma 0. La pregunta final no es de suspenso sobre una persona. La voz termina en 30,19; silencio de voz en el empalme: 1,28 s.
- **Llamado a la acción:** **uno solo**: «Subscribe for the next count.», dicho por Tan en 29,03 a 30,19 s, corto y sin promesas ni recompensas. Por qué: los suscriptores son uno de los dos umbrales del Programa (`plan_programa_de_socios.md`); el short 1 dio 0 sin pedirla.

Mapa de ritmo (tiempos estimados; cortes por segundo = cortes que caen dentro del tramo, sin contar el inicio):

| Tramo | Segundos | Pulso o intervalo | Cortes por segundo | Qué pasa (una acción) | Respiro |
|---|---|---|---|---|---|
| Gancho | 0,0–4,0 | 1,0 s y 3,0 s | 0,50 | la silla vacía, el lápiz que vuelve, la pregunta de Tan y la vara de Huang | no |
| Lista | 4,0–14,5 | 3,5 s, 3,0 s y 4,0 s | 0,29 | Iger 999, Dell 1.063, Dorsey 2.449: una barra más larga cada vez | sí (planos largos) |
| Reacción | 14,5–16,0 | 1,5 s | 0,67 | Tan: «casi siete años» | no |
| Pico | 16,0–22,0 | 4,5 s y 1,5 s | 0,33 | Jobs: subida, silencio, contador, zoom y tomate; Tan: «casi doce años»; cifra quieta 2,9 s | sí (cifra quieta de 19,13 a 22,0) |
| Remate y cierre | 22,0–31,0 | 3,0 s, 2,0 s, 3,0 s y 1,0 s | 0,33 | solo Altman fue más rápido; los otros cuatro; pregunta final, invitación y lápiz lanzado | sí (final con movimiento) |

Total: 11 cortes en 31,0 s. Densidad baja a propósito: la voz es casi continua y cada cifra necesita su plano; la densidad extra va dentro de cada toma (barras, pop de nombres, contador, reacciones de Tan, lápiz).

**Dónde cae el pico:** la subida empieza al 53 % (16,45 s), el silencio de 12 fotogramas al 56 % y la cifra llega al **61,7 %** (19,13 s). Si la voz real lo lleva más allá del 75 % no hace falta recortar nada: hay 8 s de margen.

Lo que sale se va antes de que entre lo siguiente: los textos salen de 0,05 a 0,2 s antes del corte siguiente (los rótulos que cruzan un corte son los que pertenecen al mismo gráfico, que no cambia). El movimiento es mecánica: entradas con `pop` o `slide`, contadores y barras con ease-out cúbico, el giro del lápiz con ease, sin interpolación lineal en lo vivo.

Tipos de plano disponibles y dónde van: detalle (tomas 4, 6 y 8), héroe abierto (tomas 3, 5, 7, 9, 10 y 11; el principal es la 5, cerca de la mitad, y la 7, con la cifra), subjetivo (no hay: no hay objeto de época que usar con las manos), revelado (no hay: ver decisión 9 y la tabla B), objeto que salta sobre el mismo fondo (las marcas mínimas de Huang y Altman). **No más de 3 destellos por segundo:** hay cero (no hay destello ni negativo).

### Profundidad y efectos

Cada efecto sale de `manual/14_efectos_y_emocion.md` (secciones 2, 3, 4, 4b y 6). Procedimiento de 5 pasos: objetivo (Programa de socios) → emoción de ese segundo → punto de mirada → efecto de la tabla → métrica con su segundo. Sellos: **(inv.)** investigación, **(oficio)**, **(hip.)** hipótesis del equipo (manual 14, sección 0). Emoción buscada: **curiosidad → asombro creciente → pico** (alta activación, R32).

**Tabla A — por toma: capas y z, foco, cámara, sombras, transición y efecto de acento**

| Toma | Capas y su z | Foco | Cámara | Sombras | Transición de entrada | Efecto de acento |
|---|---|---|---|---|---|---|
| 1 (0,0–1,0) | papel +900; silla 0 (crece); Tan y Tin 0; lápiz libre −420 a 0 | todo nítido | fija | contacto bajo pies y silla | ninguna (bucle) | lápiz que vuelve (10 f) y golpe de «11» (f 6) |
| 2 (1,0–4,0) | papel +900; silla +420 (niebla); ranking y Tan 0 | z 0 | fija | contacto de Tan | corte en el movimiento | fila de Huang con `pop` |
| 3 (4,0–7,5) | papel +900; ranking y personajes 0 | z 0 | fija | contacto de pies | corte seco | barra de Iger |
| 4 (7,5–10,5) | papel +900; ranking y Tin 0 | z 0 | fija | contacto de Tin | corte seco | barra de Dell |
| 5 (10,5–14,5) | papel +900; ranking y personajes 0 | z 0 | fija | contacto de pies | corte seco | barra de Dorsey |
| 6 (14,5–16,0) | papel +900; silla +420; ranking y Tan 0 | z 0 | fija | contacto de Tan | corte seco | ninguno (respiro) |
| 7 (16,0–20,5) | papel +900; ranking y personajes 0 | z 0 | fija; golpe de zoom +10 % en 19,13 | contacto de pies | corte seco | subida, silencio, contador, tomate |
| 8 (20,5–22,0) | papel +900; ranking y Tan 0 | z 0 | fija | contacto de Tan | corte seco | cifra quieta |
| 9 (22,0–25,0) | papel +900; ranking y personajes 0 | z 0 | fija | contacto de pies | corte seco | fila de Altman y «5 days» |
| 10 (25,0–27,0) | papel +900; ranking y personajes 0 | z 0 | fija | contacto de pies | corte seco | «4 took longer» |
| 11 (27,0–30,0) | papel +900; silla 0; Tan y Tin 0; lápiz libre (arco) | z 0 | fija | contacto de pies y silla | corte seco | pase del lápiz y `pop` de «Subscribe» |
| 12 (30,0–31,0) | las de la toma 11 más el lápiz libre −420 | z 0 | fija | contacto | corte seco | anticipación y lanzamiento del lápiz (25 f) |

**Tabla B — por efecto: las tres respuestas del manual (emoción, punto de mirada, métrica), su dosis y su respaldo**

| N.º | Efecto (herramienta) | Segundo y dosis | Emoción | Punto de mirada | Métrica | Respaldo y sello |
|---|---|---|---|---|---|---|
| 1 | **Firma: el lápiz bumerán llega y Tan lo atrapa** (lápiz libre con estela, giro horario, escala hasta 1,7) | 0,0–0,5 s; atrapada en f10; golpe de sonido; voz en f14 | orientación y curiosidad («algo vuelve») | el lápiz y la mano de Tan | visto frente a deslizado, contra el 20,7 % del short 1; retención 0–1,5 s | R4, R5 **(inv.)** (lo que crece y se acerca atrae); R10 **(inv.)**; R22 **(oficio)** (anticipación y acción superpuesta); que una firma repetida se reconozca (R26 **(inv.)**) y baje los deslizados: **(hip.)** |
| 2 | **Silla vacía que crece** (capa animada, de 0,82 a 1,0) | 0,0–0,4 s; 12 f con frenada; ≈ 35 % del ancho | curiosidad (una silla vacía es una incógnita) | el centro de la silla (540, 910) | visto frente a deslizado | R28 **(inv.)** (incertidumbre); R4 **(inv.)**; movimiento secundario: el principal es el lápiz |
| 3 | **Palabra clave con golpe en mostaza** (`palabra_clave`) y golpe de sonido | f 6 a 18; 5 f de ida y 7 de asiento; escala 1,0 a 1,18; texto entero desde el fotograma 0, hasta 0,9 s | énfasis | «11» | visto frente a deslizado; retención al segundo 1 | R33, R10 **(inv.)**; R39 **(oficio)**; adaptación: la portada exige el texto entero en el fotograma 0 |
| 4 | **Corte en el movimiento** | 1,0 s, 4 f después de que arranca el brazo de Tan; el primer plano dura 30 f | reorientación sin sobresalto | el brazo y la cara de Tan | que no haya caída en 1,0–1,5 s | R14 **(oficio)**, R13 y R11 **(inv.)** |
| 5 | **Capas, sombras de contacto y desenfoque fijo del fondo** (`Capa`, `componer`, `sombra_contacto`), sin cámara | tomas 1 a 12; la silla lejana en tomas 2, 6 y 11 | presencia y atención tranquila; credibilidad | los personajes y el rótulo | retención de 4,0 a 14,5 s sin caída | R1, R3, R7 **(inv.)**, R8 **(oficio)**; que retenga más: **(hip.)** |
| 6 | **Gráfico que crece, una fila por plano** (barras a escala con nombre y marca mínima de 8 px) | Iger 5,77–6,50; Dell 8,75–9,50; Dorsey 12,11–13,00; Jobs 17,93–19,13; ease-out cúbico | comprensión y asombro creciente ante lo mucho mayor | el extremo de la barra y el nombre | retención en cada barra; compartidos | R37 **(inv.)**; su uso en un ranking de seis: **(hip.)**; la escala no engaña: la marca mínima se declara (manual 12, cifras con fuente) |
| 7 | **El pico: subida de sonido, silencio de 12 f, contador que acelera y frena, un zoom de golpe suave, cifra quieta** (`contador`, `golpe_de_zoom`) | subida 16,45–17,28 s (25 f); silencio 17,28–17,68 s; contador 17,93–19,13 s (36 f); zoom +10 % (5 f + 8 f); cifra quieta 19,13–22,0 s (86 f); 61,7 % del video | anticipación → sorpresa → asombro | la cifra «4,382 days» arriba a la izquierda | pico de retención en 19,13 s; compartidos por mil vistas | R22 **(oficio)**, R28, R32, R34, R35 **(inv.)**; solo zoom, sin destello (manual 4: «uno o el otro») |
| 8 | **Paso a tomate** (mostaza a tomate solo en el pico) | 19,13–22,0 s; un elemento | golpe y recordación de la cifra | la cifra | retención de los segundos 1 a 3 y de 19 a 22 s | R33 **(inv.)**; manual 13 |
| 9 | **Plano de respiro tras el pico** | 20,5–22,0 s; 45 f sin efectos nuevos (la cifra ya lleva 41 f quieta en la toma 7) | alivio breve sin dejar caer la activación | Tan y la cifra | línea plana en la curva (P1) | el estímulo repetido pierde efecto, R10 **(inv.)**; «picos y respiros» **(hip.)** |
| 10 | **Cierre: respuesta con remate + pregunta abierta + una invitación + lápiz lanzado** (pase del lápiz, anticipación y lanzamiento) | 22,19–31,0 s; pase 8 f (28,50–28,77); anticipación 6 f (30,20–30,37); suelta en 30,5; whoosh con vibrato atado al giro | sorpresa cerrada, curiosidad nueva, gratitud | el lápiz que sale y la boca de Tan | suscriptores por cada mil vistas; compartidos; regreso al canal | R48, R51, R52 **(inv.)** (manual 4b); R50 **(oficio)**; que la pregunta suba los suscriptores: **(hip.)** |
| 11 | **Acción secundaria continua y curvas con frenada** | todo el video: bufanda de Tan (`viento`), lápiz de Tin (±3 grados) | calidez y vida | los personajes | comentarios que nombran a Tin o a Tan | R22 **(oficio)**, R24 **(inv.)** |
| 12 | **Paso de neutro a acento** (mostaza) | la clave y un elemento por plano | foco y recordación | la palabra o la barra | retención de los segundos 1 a 3 | R33 **(inv.)**; manual 13 |

**Dosis y límites (manual 14, sección 6) que este video respeta:** sin cambio de foco (no cabe en la rejilla: no hay hueco de voz de 8 a 12 f entre líneas sin romper los cortes); **sin revelado y sin paralaje** (decisión 9); 1 golpe de zoom de +10 % (máximo +35 %); 1 animación de acercamiento fuerte (el lápiz; la silla es suave); **cámara fija en todo el video**; cero destellos y cero negativos; sin «atravesar la escena»; sin sombra tumbada de los muñecos; texto sin movimiento mientras se lee; el texto entra con `pop` y se queda 30 f o más (45 f o más para la cifra del pico). **`efectos.comprobar_destellos` se corre con margen** (máximo 2 cambios bruscos por segundo, no 3) sobre los 930 fotogramas; no hay estrobo; ningún rojo parpadea.

**Cierre, decidido con la tabla del manual (4b.3), resumida:**

| Tipo de cierre | Emoción | Métrica | Riesgo | Decisión aquí |
|---|---|---|---|---|
| Pregunta de suspenso abierta | curiosidad con tensión | regreso, suscriptores | frustración, engaño, insinuación sobre una persona | **No**: no hay hecho pendiente que el canal pueda prometer |
| Respuesta completa con remate | asombro, cierre | retención final, compartidos | «ya está» | **Sí** (tomas 9 y 10): base |
| Pregunta al espectador para comentar | participación | comentarios | invita al juicio de una persona | **No** |
| Promesa de continuación (pregunta abierta, nueva y respondible) | anticipación | suscriptores, regreso | prometer lo que no se hace | **Sí** (toma 11), con compromiso de publicar el conteo de permanencia en 7 días |
| Bucle perfecto | cierre redondo | duración media > 100 % | la repetición no es vista calificada | **Visual y gratis** (el lápiz), no decide el cierre |
| Invitación a suscribirse | gratitud | suscriptores | súplica, más de una petición | **Sí**, una vez, después del remate y atada a la pregunta |

## 12. Texto en pantalla y sistema de diseño

- **Tipografías:** Inter Display Medium con sus **dígitos abiertos** (`ss01`), licencia SIL Open Font License 1.1 (`/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf`). Rótulos en inglés en minúsculas, a la izquierda, salvo los nombres propios y siglas con mayúscula inicial («Huang», «Iger», «CEO»); la portada con mayúscula inicial en cada palabra. **Excepción obligatoria (regla del dueño):** los nombres propios llevan mayúscula («Tin & Tan», «Tin», «Tan», «Jensen Huang», «Steve Jobs», «Sam Altman»).
- **Paleta:** papel `#F3E9D2` · papel_sombra `#E6D8B8` · tinta `#2B2420` · naranja `#E07A2E` · marrón `#7A4B2A` · verde azulado `#2F7F7A` · mostaza `#E8B33B` (**acento único** salvo en el pico) · tomate `#C8553D` (**acento solo del pico**, tomas 7 y 8: la cifra «4,382»; además la goma del lápiz, que es identidad) · rubor `#E9967A`. Un acento por plano; **mostaza y tomate nunca comparten plano como acento** (la bufanda de Tan, el cuerpo del lápiz y la goma son identidad y no cuentan). La palabra clave lleva trazo de tinta de 0,045 em. **Ningún color de marca de terceros.**
- **Referencias de movimiento:** `01_referencia/` está vacía. Referencias cargadas: `canales/nostalgia-tin-y-tan/DESIGN.md`, `FIRMA_LAPIZ_BUMERAN.md`, `herramientas/palitos.py`, `herramientas/efectos.py`, las hojas de `personajes/tin/referencias/` y `personajes/tan/referencias/`, y el prompt y las firmas del short 3.
- **Prohibido:**
  1. Mayúsculas centradas sobre degradado o cualquier fondo con degradado.
  2. Animaciones lineales de posición o escala en lo vivo (solo muelle o ease-out cúbico; lineal solo en lo mecánico).
  3. Los símbolos «→» y cualquier glifo sin comprobar. «≈» solo si la fuente lo trae (comprobado el 2026-11-24 con Pillow: «≈», «¿», «?», «,», «.», «:», «+» y «&» existen), y solo en la descripción.
  4. Un contador que retrocede o que se pasa de su valor final y vuelve.
  5. Texto encima de un personaje o de la silla.
  6. Cualquier logotipo, letra de marca o color de Nvidia, Disney, Dell, Twitter, Apple u OpenAI; y cualquier rostro, voz o frase de una persona real.
  7. Líneas sin suavizar: ningún dibujo fuera de un `Lienzo` o `LienzoCapa` con supermuestreo.
  8. Sombras tumbadas de los muñecos, resplandor, partículas, confeti.
  9. Rótulos de más de 3 palabras (salvo la portada, de 7 palabras en 3 renglones por la regla de portada), de más de una línea o fuera de la zona segura.
  10. Cambiar los colores o accesorios de Tin y Tan (solo cambia el objeto de la mano).
  11. Una barra o marca sin su nombre al lado (56 px o más), una marca de menos de 8 px o sin borde de tinta de 2 px, y un nombre dentro de una barra.
  12. Un rótulo grande que diga algo distinto de lo que dice la voz en ese momento.
  13. Una tarjeta en español con menos de 30 fotogramas, o la cifra del pico nítida menos de 1 s.
- **Márgenes seguros:** zona segura de `formatos.md` (x 100–980, y 250–1670); portada: zona útil x 60–960, y 380–1440.
- **Texto exacto:** todo texto en pantalla es el de las tablas de abajo, letra por letra. Los contadores muestran enteros entre su valor de inicio y su valor final.
- **No afirmar:** nada fuera de la tabla del brief y de las fechas verificadas hoy:
  - **Cuentas con `datetime`, 2026-11-24:** Altman 5 días (2023-11-17 a 2023-11-22), Huang 11 (2026-11-12 a 2026-11-23), Iger 999 (2020-02-25 a 2022-11-20), Dell 1.063 (2004-03-04 a 2007-01-31), Dorsey 2.449 (2008-10-16 a 2015-07-01; ≈ 6,7 años; «almost seven years» en la voz), Jobs 4.382 (1985-09-17 a 1997-09-16; ≈ 12 años; «almost twelve years» en la voz).
  - **No decir ni mostrar:** cómo ni por qué salió nadie (ni «resigned», «fired», «scandal», «removed» en la voz ni en pantalla; solo la descripción dice «removed» y «resigned»), detalles de la vida privada, nombres de terceros (sucesores, juntas, investigadores), cifras de bolsa, fortuna o salario, citas de ninguno, que sean «todos» los regresos o «el más largo» o «el más rápido de la historia», que los otros cuatro «fracasaran» o «perdieran», quién lidera hoy ninguna de las empresas, predicciones sobre su permanencia. De cada empresa solo se dice el nombre.

**Rótulos en inglés (los que van en pantalla):**

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| CEO Comebacks / Huang 11 Days / vs. Jobs? (clave: 11; entero en el fotograma 0, sin pop; es la portada; tres renglones) | 0,00 | 0,90 | 10, 20,8 | 4,8 |
| 11 days (clave: 11) | 2,40 | 3,95 | 10, 14 | 7 |
| 999 days (clave: el número) | 5,77 | 7,45 | 10, 14 | 7 |
| 1,063 days (clave: el número) | 8,75 | 10,45 | 10, 14 | 7 |
| 2,449 days (clave: el número) | 12,11 | 14,45 | 10, 14 | 7 |
| almost 7 years? (clave: 7) | 14,80 | 15,95 | 10, 14 | 7 |
| 4,382 days (contador de 0 a 4,382; en tinta mientras sube y en tomate al llegar; sigue en la toma 8) | 17,93 | 21,95 | 10, 14 | 7 |
| 5 days (clave: 5) | 24,45 | 25,50 | 10, 14 | 7 |
| 4 took longer (clave: 4) | 25,55 | 26,95 | 10, 14 | 7 |
| How long? (clave: long) | 27,05 | 28,85 | 10, 14 | 7 |
| Subscribe (clave) | 28,93 | 29,97 | 10, 14 | 7 |
| CEO Comebacks / Huang 11 Days / vs. Jobs? (entra con pop; sigue sin corte en la toma 1) | 30,00 | 31,00 | 10, 20,8 | 4,8 |
| Altman (nombre de la fila 0; en tinta) | 22,62 | 26,90 | 9,3, 25,5 | 2,9 |
| Huang (nombre de la fila 1; en tinta) | 1,20 | 26,90 | 9,3, 29 | 2,9 |
| Iger (nombre de la fila 2; en tinta) | 4,40 | 26,90 | 9,3, 32,5 | 2,9 |
| Dell (nombre de la fila 3; en tinta) | 7,60 | 26,90 | 9,3, 36 | 2,9 |
| Dorsey (nombre de la fila 4; en tinta) | 10,80 | 26,90 | 9,3, 39,5 | 2,9 |
| Jobs (nombre de la fila 5; en tinta) | 16,35 | 26,90 | 9,3, 43 | 2,9 |

**Subtítulos en español (quemados en el video; encargo del dueño, 2026-11-24).** La voz sigue en inglés; en pantalla va la traducción al español de cada línea, sincronizada con ella.

- **Dónde va la banda:** fija, de **y = 905 a y = 1085** (47,1 % a 56,5 % del alto) y de x = 100 a x = 980: **entre el gráfico** (que termina en y = 888) **y la cabeza de los personajes** (que empieza en y ≈ 1146 con `alto` 505). No tapa personajes ni objetos y no choca con los rótulos en inglés (arriba, y 253–461). La parte de abajo (y > 1500) queda libre porque la interfaz de los Shorts la cubre.
- **Formato:** Inter Display Medium a **4,5 % del alto (86 px)**; tinta `#2B2420` sobre un **panel de papel `#F3E9D2` translúcido** (opacidad 0,82, esquinas de 20 px, relleno de 12 px); contraste tinta/papel 12,6:1 (mínimo pedido 7:1). **Máximo 2 líneas y ≈ 21 caracteres por línea** (≤ 856 px medidos con la fuente el 2026-11-24: la más ancha, «Suscríbete al próximo», mide 824 px). Entrada de 3 fotogramas (fundido de la opacidad), sin `pop`; **cada tarjeta dura 30 fotogramas o más**; hueco ≥ 12 px entre el panel y las cabezas y ≥ 16 px entre el panel y el gráfico; **nada dibujado bajo el panel**.
- **Cómo conviven con los rótulos en inglés:** los rótulos grandes siguen en inglés. **Las tarjetas llevan la cifra y la palabra «días»** (millares con punto: 1.063, 2.449, 4.382), con la lección del short 3: sin «días» quien no lee inglés no entiende la cifra. En las tomas con número, **el segundo renglón (la cifra) entra con la voz** (tarjetas 3, 4 y 5) o **con la llegada del contador** (tarjeta 7, para no adelantar el pico). La portada (0,0–1,0 s y 29,97–31,0 s) **no lleva subtítulo**.
- **Decisiones de redacción:** español neutro, natural y no literal; «CEO» (forma de los titulares); «Disney», «Dell», «Twitter», «Apple» y los nombres como en inglés; «¿Casi 7 años?» y «¿Casi 12 años?» llevan la aproximación que lleva la voz.

| Tarjeta | Empieza (s) | Termina (s) | Línea de voz | Texto en español (una línea por renglón) |
|---|---|---|---|---|
| 1 | 1,00 | 3,20 | 1 | Jensen Huang volvió / de CEO en 11 días. |
| 2 | 3,25 | 4,30 | 1 | ¿Quién tardó más? |
| 3 | 4,31 | 7,45 | 2 | Bob Iger, Disney: / 999 días. (el segundo renglón entra en 5,77 s) |
| 4 | 7,52 | 10,45 | 3 | Michael Dell, Dell: / 1.063 días. (el segundo renglón entra en 8,75 s) |
| 5 | 10,66 | 14,45 | 4 | Jack Dorsey, Twitter: / 2.449 días. (el segundo renglón entra en 12,11 s) |
| 6 | 14,80 | 15,95 | 5 | ¿Casi 7 años? |
| 7 | 16,20 | 20,85 | 6 | Steve Jobs, Apple: / 4.382 días. (el segundo renglón entra en 19,13 s, con la llegada del contador: nítido 1,7 s) |
| 8 | 20,87 | 21,95 | 7 | ¿Casi 12 años? |
| 9 | 22,19 | 25,05 | 8 | Solo Altman fue más / rápido: 5 días. |
| 10 | 25,09 | 26,95 | 8 | Los otros cuatro / tardaron más. |
| 11 | 26,96 | 28,90 | 9 | ¿Cuánto duraron / tras volver? |
| 12 | 28,93 | 29,97 | 9 | Suscríbete al próximo / conteo. |

### Color con intención

Propuesta del prompt (`manual/13_color_con_intencion.md`); la sección 3b de `02_prompt/direccion.md` la completa y, si difiere, manda la dirección.

- **Neutros (2):** papel `#F3E9D2` (fondo de todos los planos; suelo y lona de la silla en `#E6D8B8`) y tinta `#2B2420` (líneas, contornos y todo texto que no sea clave, incluidos los nombres de las filas y los subtítulos). Contraste tinta/papel 12,6:1.
- **Acento (1):** mostaza `#E8B33B`, con contorno de tinta, solo en la palabra clave y en **un** elemento por plano (el lápiz, la marca de 8 px o la barra en curso, según la toma). **No va** en el texto que no es clave, en la silla, en los nombres de las filas ni en las barras ya contadas (marrón `#7A4B2A`, relleno neutro). **Tomate `#C8553D` queda reservado al pico** (tomas 7 y 8) y ahí no hay mostaza como acento: por eso Tin no lleva el lápiz en esas dos tomas.
- **Por qué esta paleta:** la misma de los shorts 1 a 3, para que el canal se reconozca (R26 inv.); papel y tinta dan contraste alto y lectura fácil (R27 inv.); el acento único se recuerda (R33 inv.) y el cambio a tomate marca el golpe del dato más grande. Para una lista de salidas y regresos de personas reales, la saturación baja evita alarma y burla; el significado emocional del color es **hipótesis** (Elliot y Maier, 2014, manual 13).
- **Cómo ayuda al objetivo:** Programa de socios → reconocimiento del canal y un pico visible en la cifra → retención de los segundos 1 a 3 y pico en 19,13 s; regreso de espectadores.
- **Riesgos de lectura:** (1) mostaza sobre papel da 1,6:1: se lee por el contorno de tinta y las marcas de 8 px llevan borde de 2 px (en el short 3 las de 4 px se veían como un hilo pálido); (2) tinta sobre tomate 3,5:1: la cifra se lee por contorno, tamaño y redundancia (la misma cifra va en tinta en la tarjeta); medir el ΔE tomate–naranja de Tin con `revisar_color.py` (en el short 3 se calculó a mano: ≈ 24,7); (3) la bufanda mostaza de Tan y la goma tomate del lápiz son identidad y no se leen como segundo acento; (4) rojo y verde azulado: la información no depende del tono; (5) el desenfoque fijo de la silla baja el porcentaje en paleta: el short 3 midió ≈ 93 % con las mismas capas; piso 85 % (`DESIGN.md`), medido también sobre el fotograma 0 y sobre los cuadros de 17,9 a 22,0 s por separado (lo pidió el director de fotografía).
- **Medido:** pendiente (lo llena el supervisor tras el render).

Tabla de acento por plano:

| Toma | Mostaza (palabra clave + un elemento) | Tomate |
|---|---|---|
| 1 | «11» + lápiz | no |
| 2 | «11» + marca de Huang | no |
| 3 | «999» + barra de Iger | no |
| 4 | «1,063» + barra de Dell | no |
| 5 | «2,449» + barra de Dorsey | no |
| 6 | «7» | no |
| 7 | ninguno | cifra «4,382» |
| 8 | ninguno | cifra «4,382» |
| 9 | «5» + marca de Altman | no |
| 10 | «4» (+ lápiz como identidad) | no |
| 11 | «long» y luego «Subscribe» + lápiz | no |
| 12 | «11» + lápiz | no |

Campo para `ficha.json`:

```json
"color": {"neutros": [
            "#F3E9D2",
            "#2B2420"
          ], "acento": "#E8B33B",
          "por_que": "papel y tinta como neutros del canal; mostaza como acento único (clave y un elemento por plano); tomate solo en el pico (la cifra de Jobs) para marcar el golpe; la misma paleta que los shorts 1 a 3 para reconocer el canal",
          "objetivo": "Programa de socios: reconocimiento del canal y un pico visible; métrica: retención de los segundos 1 a 3 y pico de retención en 19,13 s",
          "medido": "pendiente de render"}
```

En un short, todo texto queda dentro de la zona segura. Entrada de cada rótulo: `pop` con escala de 0,85 a 1 en 8 fotogramas; salida: subir 2 % con ease-in en 3 fotogramas (excepción: el rótulo de portada en el fotograma 0 y en el último ya están a escala 1).

## 13. Sonido

Los golpes bajo la voz van a unos **−26 LUFS** (−12 dB respecto a la voz, a −14 LUFS; lección del short 1: a −38 LUFS no se oían); los dos sonidos de la firma a −20 dBFS de pico como pide la especificación. Se comprueba al oído. Cada corte y cada efecto lleva su golpe a ±1 fotograma (manual 14, 2.8).

| Golpe o efecto | Segundo | A qué corte o efecto va atado | Origen y licencia |
|---|---|---|---|
| Whoosh con vibrato (vuelo del lápiz que se frena) | 0,00–0,33 | firma: llegada del lápiz (toma 1) | código, propio |
| Golpe seco al atrapar (thwack, 80 ms) | 0,33 | Tan atrapa el lápiz (f 10) | código, propio |
| Golpe de la clave «11» | 0,20 | `palabra_clave` de la portada (f 6) | código, propio |
| Clic suave | 1,0 | corte en el movimiento, toma 1 a 2 | código, propio |
| Pop de fila (nombre y marca) | 1,20 y 1,40 | fila de Huang | código, propio |
| Clic suave | 4,0 | corte, toma 2 a 3 | código, propio |
| Pop de nombre y deslizar de la barra (tono que sube y frena) | 4,40 y 5,77–6,50 | fila de Iger | código, propio |
| Clic suave | 7,5 | corte, toma 3 a 4 | código, propio |
| Pop de nombre y deslizar de la barra | 7,60 y 8,75–9,50 | fila de Dell | código, propio |
| Clic suave | 10,5 | corte, toma 4 a 5 | código, propio |
| Pop de nombre y deslizar de la barra | 10,80 y 12,11–13,00 | fila de Dorsey | código, propio |
| Clic suave | 14,5 | corte, toma 5 a 6 | código, propio |
| Clic suave | 16,0 | corte, toma 6 a 7 | código, propio |
| Pop de nombre | 16,35 | fila de Jobs | código, propio |
| Subida (riser) de 25 fotogramas | 16,45–17,28 | antes del pico | código, propio |
| **Silencio de efectos y música de 12 fotogramas** | 17,28–17,68 | antes del número (cae en la pausa de la voz tras «Apple:») | código, propio |
| Tictac de contador que sube de tono | 17,93–19,13 | contador de 4.382 (calla al llegar) | código, propio |
| Ding grave + acorde de re mayor abierto + golpe del zoom | 19,13 | llegada de la cifra, paso a tomate y `pop` (mismo fotograma) | código, propio |
| Clic suave | 20,5 | corte, toma 7 a 8 (la cifra queda quieta) | código, propio |
| Clic suave | 22,0 | corte, toma 8 a 9 | código, propio |
| Pop de nombre y de marca | 22,62 y 22,80 | fila de Altman | código, propio |
| Clic suave | 25,0 | corte, toma 9 a 10 | código, propio |
| Clic suave | 27,0 | corte, toma 10 a 11 | código, propio |
| Whoosh corto del pase del lápiz | 28,50–28,77 | lápiz de Tin a Tan | código, propio |
| Clic suave | 30,0 | corte, toma 11 a 12 | código, propio |
| Crujido de anticipación (6 f) | 30,20–30,37 | anticipación del lanzamiento | código, propio |
| **Whoosh con vibrato que se acelera** | 30,37–31,0 | lanzamiento: último movimiento; es el mismo vuelo que abre el bucle (empalme con el 0,0) | código, propio |

- **Música:** re menor a 120 BPM (sección 7), −24 LUFS; sin material de terceros. **Voz:** sí (por generar); empieza en el fotograma 14 (0,47 s), después del golpe de la atrapada.
- Los pasos de música y efectos entre cortes no pueden tener más de 2 golpes fuertes por segundo. En los 34 fotogramas de la firma no suena nada que no esté en la especificación de `FIRMA_LAPIZ_BUMERAN.md` (sección 7).

## 14. Motor y revisión

- **Cómo se hace:** gráficos por código (fotograma a fotograma): Python, Pillow, numpy y ffmpeg. Cada plano con capas se compone con `efectos.componer` (`Capa`, `Camara`) desde `LienzoCapa` con supermuestreo; los personajes con `palitos.dibujar(lz, id, x, suelo, alto, pose, expresion, vista, mira, viento, objeto, espejo)`. Todo depende del número de fotograma. Se guardan PNG numerados y ffmpeg los une con la voz, los efectos y la música (`postpro.py mezclar` o ffmpeg directo). El `codigo/render.py` del short 3 (`proyectos/2026-11-24_tin_y_tan_jensen_huang/codigo/`) se toma como punto de partida para la silla, el lápiz libre, la banda de subtítulos y los controles; **el ranking, el texto de portada y las tarjetas son nuevos**.
- **Qué hay que dibujar (todo genérico y sin marca):**
  1. `silla_director` (sección 5), a escala variable, también pequeña y lejana (ya existe en el código del short 3).
  2. **`ranking`**: seis filas de 68 px con nombre a 56 px, barras de 40 px a 0,1506 px por día y marcas mínimas de 8 px con borde de 2 px; entradas con `pop` y barras con ease-out cúbico.
  3. `lapiz_libre` y la firma (ya programados: `efectos.py` 1.1), con la geometría de portada del short 3.
  4. Banda de subtítulos en español: panel translúcido y texto con medida previa (`ancho_texto`) para que ninguna línea pase de 856 px; segundo renglón que entra en su segundo.
  5. Texto de portada de tres renglones con medida previa (703, 585 y 384 px).
  6. Glifos «¿», «?», «,», «.», «:», «+» y «&» comprobados en la fuente el 2026-11-24 (existen).
- **Lo que el short 3 dejó resuelto y aquí viene resuelto de origen** (firmas del supervisor, vueltas 1 a 3, y firma de fotografía):

| Defecto del short 3 | Dónde queda resuelto aquí |
|---|---|
| El lápiz pasaba por delante de la cara de Tan (vuelta 1) | `comprobar_firma` mide todos los fotogramas: 8 px o más a cualquier cabeza; brazo `BD_FIRMA` (95°, 108°) |
| La «q» tocaba el rodete y el panel velaba cabezas | `alto` 505 px; hueco panel–cabeza ≥ 12 px medido en todos los fotogramas con tarjeta |
| Barras sin nombre; marcas de 4 px casi invisibles | nombre a 56 px junto a cada fila; marcas de 8 px con borde de 2 px |
| Cifras solo en inglés en las tarjetas | tarjetas con la cifra y «días», millares con punto |
| Tarjeta de la cifra del pico visible 9 fotogramas | «4.382 días.» entra con la llegada del contador y dura 1,7 s |
| Cara de Tan en la portada serena (se leía como duda) | `sorpresa` en la portada y en el empalme |
| Sonrisa de Tin y festejo de Tan sobre una renuncia y una reposición | solo `curiosidad` y `sorpresa` en los datos; `risa` y `feliz` en el remate y la invitación |
| «That is twelve years?» sin aproximación en la voz | «Almost seven years?» y «Almost twelve years?» |
| Silla de primer plano fuera de la zona segura | no hay silla de primer plano |
| Flecha y círculos del calendario poco legibles | no hay calendario |
| Dos acentos «mostaza» (lápiz y clave) y goma tomate | declarados como identidad en el negativo, la paleta y la tabla de acento |
| Portada con dos renglones que no nombraban al sujeto | tres renglones que nombran «CEO», «Huang» y «Jobs» (regla del 2026-11-24) |
| Cierre de 0,95 s, voz hasta 30,05 s (c = −28) | cierre de 30 fotogramas; voz termina en c = −24 |

- **Quién renderiza y autorización:** el equipo de producción renderiza (0 créditos); **la voz necesita la cotización y el sí del dueño**; publicar también. Antes de renderizar se revisa `03_keyframes/definicion.md` y se anotan fuente y licencia de cada recurso en `licencias.md`.
- **Controles (todo gratis, en `07_revision/`):**
  - **Texto:** `revisar_texto.py` con 0 errores. Corrido el 2026-11-24 sobre `subtitulos.srt`, la descripción y las etiquetas (`--idioma en`) y sobre `subtitulos_es.srt` (`--idioma es`): 0 errores en los tres. Los textos de pantalla del código se pasan antes de renderizar.
  - **Destellos:** `efectos.comprobar_destellos` con margen (máximo 2 por segundo) y `postpro.py destellos`; mirada fotograma a fotograma a la llegada de la cifra (zoom y tomate) y al lanzamiento del lápiz.
  - **Fotogramas:** `revisar_fotogramas.py` y `analizar_video.py --cada 0.5`; hojas de contacto miradas una por una.
  - **Medidas:** zona segura en los 930 fotogramas; portada (texto y 400–700, silla y 720–1100, caras dentro de x 60–960 e y 380–1440); la banda de subtítulos (y 905–1085) sin tocar gráficos ni cabezas; cada línea de subtítulo ≤ 856 px; pies a 86 %; `alto` 505 px; cada nombre de fila a 56 px; cada tarjeta 30 fotogramas o más; cada marca mínima 8 px con borde de 2 px.
  - **Bucle y firma:** `comprobar_firma` (los 10 puntos de §11 de `FIRMA_LAPIZ_BUMERAN.md`); el fotograma 930 igual al 0 (diferencia media menor de 3 de 255).
  - **Color:** `revisar_color.py` (paleta, contraste, saltos) sobre el video, el fotograma 0 y los cuadros de 17,9 a 22,0 s; ΔE tomate–naranja medido con la herramienta.
  - **Cifras:** recalcular con `datetime` (5, 11, 999, 1.063, 2.449, 4.382) y comparar pantalla, subtítulos, guion y descripción; los contadores solo suben.
  - **Oído:** que cada corte caiga donde dice la sección 6 con la voz real; que «Iger», «Huang», «Dorsey», «C E O» y «Twitter» suenen bien; que la pausa tras «Apple:» sea de ≈ 0,45 s; que el golpe del lápiz se oiga bajo la voz.
- **Qué se marca:** imagen congelada, fotograma vacío, texto cortado o tapado, texto que sigue sobre el plano siguiente, elemento fuera de cuadro, tirones, contador que retrocede, glifos cuadrados, el fotograma 930 distinto del 0, más de 2 destellos por segundo, cualquier cosa que recuerde a una marca (logotipo, color, letra), cualquier rostro o silueta que se lea como una persona real, una expresión de Tan o de Tin que se lea como burla o enojo, una sonrisa en un dato de una salida, y en el teléfono: que nombres, barras, cifras y subtítulos se lean. Nota para el validador: en las tomas con personajes el bloque de identidad de la ficha no se pega en el prompt porque no hay generador de imágenes; el diseño oficial es el código de `palitos.py` y se comprueba con la lista de comprobación de cada ficha.
- **Vueltas:** las correcciones por código son gratis; **las de generador no se repiten sin autorización del dueño** (`generacion.md`). Aquí solo hay generador en la voz: una generación por voz, sin segundos intentos.
