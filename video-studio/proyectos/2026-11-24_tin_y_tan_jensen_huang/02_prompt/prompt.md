# Prompt de video para redes — Jensen Huang Is Back as Nvidia CEO After 11 Days

> **ESTADO (2026-11-24, versión 2):** sustituye por completo al prompt de la tarjeta de 1999 (descartado: el dueño eliminó la nostalgia como criterio del canal, `canales/nostalgia-tin-y-tan/PARAMETROS.md`). Este video trata de **la noticia**: Jensen Huang volvió como director ejecutivo de Nvidia a los 11 días. **La voz no está generada, los tiempos son estimados** (ritmo medido en el short 2: Tin ≈ 4,6 sílabas por segundo, Tan ≈ 5,2) y el video no está renderizado. El dueño ordenó que el equipo decida todo con su investigación; no quedan preguntas para él, solo su sí para gastar créditos de voz y para publicar.

<!--
Pieza dibujada con código (sin generador de video). Todas las tomas son método «edición». En lugar de «Prompt de keyframe»
y «Prompt de video» cada toma lleva una «Especificación de dibujo». Los tiempos son estimados con la voz del short 2 y se
reajustan con la voz real. Sin corchetes en el texto: el validador los trata como campos sin llenar.
-->

## 1. Ficha técnica

- **Proyecto:** 2026-11-24_tin_y_tan_jensen_huang
- **Tipo:** short
- **Número:** 3
- **Serie:** ninguna
- **Objetivo de aprendizaje:** no aplica
- **Generador:** ninguno: imagen dibujada con código (palitos.py 1.3 + efectos.py + gráficos propios), armada con ffmpeg
- **Aspecto:** 9:16
- **Duración total:** 30,5 s (la voz estimada va de 0,00 a 29,09 s; cierre de 1,41 s sin voz con el lanzamiento del lápiz; múltiplo de 0,5 s; 915 fotogramas)
- **Resolución de borrador:** 540x960 a 30 fps, prueba de 5 s con un fotograma por pulso (render propio)
- **Resolución final:** 1080x1920 a 30 fps, 915 fotogramas
- **Precio por segundo:** 0 (render propio; no hay servicio de pago)
- **Intentos estimados por toma:** 1
- **Versión:** 2 (tiempos estimados; sin voz ni render)

## 2. Elenco

| Personaje | Papel en este video | Vestuario | Referencia que se sube |
|---|---|---|---|
| @tan | Abre con la pregunta de curiosidad desde el fotograma 0, hace las preguntas del público, dice la pregunta final con la invitación y **lanza el lápiz**. Lado izquierdo con `espejo=True` (centro cuando está sola). | base de su ficha (rodete y bufanda mostaza); objeto de mano `lapiz` solo en las tomas 13 y 14 | personajes/tan/referencias/principal_tin_y_tan.png |
| @tin | Responde con datos; **atrapa el lápiz** en el fotograma 15 y lo lleva en la mano. Lado derecho, sin espejo. | base de su ficha (gorra marrón, lentes, lápiz); `objeto=False` hasta atrapar el lápiz y en las tomas 10 y 11 (acento tomate) | personajes/tin/referencias/principal_tin_y_tan.png |

No se sube nada a un generador: las referencias son el diseño en código (`herramientas/palitos.py`, versión 1.3) y solo sirven para comparar. **Jensen Huang, Sam Altman y Steve Jobs no aparecen dibujados ni imitados ni se les cita: solo se les nombra.** Poses y expresiones usadas (todas existen en `POSES` y `EXPRESIONES`, comprobado el 2026-11-24): `parado`, `explica`, `senala`, `pregunta`, `encoge`, `celebra`, `saluda`; `curiosidad`, `sorpresa`, `feliz`, `risa`, `eureka`. **No se usan** `pensando` ni `concentrado` (se leen como enojo, lección del short 2). Tamaño de los personajes en este video: `alto` = 29 % del alto (557 px) para dejar la banda de subtítulos en español (sección 12).

## 3. Idea en una línea

Tan pregunta lo que el público se pregunta, «¿fue rápido el regreso de Jensen Huang en 11 días?», y Tin responde con los hechos en orden y con fechas (renunció el 12, la junta dijo que no el 17, lo repuso el 23) y con una comparación: Sam Altman volvió en 5 días y Steve Jobs tardó 4.382 días (≈ 12 años). Respuesta: más rápido que Jobs, más lento que Altman. Emoción: curiosidad → tensión → asombro. El lápiz de Tin hace de bumerán: vuelve al empezar y sale lanzado por Tan al terminar.

**Decisiones del equipo (2026-11-24), todas con su porqué** (el dueño ordenó decidir con la investigación):

1. **Tema = la noticia.** La demanda está en el regreso (cientos de miles de vistas en horas, lectura del 2026-11-24, `00_analisis_de_tematicas.md`, S2); el tema lo pone la demanda (`PARAMETROS.md`). Sin objetos de época ni nostalgia.
2. **Apertura: una pregunta de curiosidad dicha por Tan desde el fotograma 0** («Was Jensen Huang's comeback in eleven days fast?»). Es una brecha de información real (¿rápido comparado con qué?) que el video cierra en el pico y en el remate (R28, R51; manual 14, sección 4b).
3. **Fechas verificadas hoy** (Wikipedia en inglés, páginas «Removal of Sam Altman from OpenAI», «Steve Jobs», «Jensen Huang», abiertas con `curl` el 2026-11-24; cuentas con `datetime`). Altman: destituido el 2023-11-17 y repuesto el 2023-11-22 = **5 días**. Jobs: carta de renuncia el 1985-09-17 y nombrado director ejecutivo interino el 1997-09-16 = **4.382 días** (11,9975 años). Huang: renuncia el 2026-11-12 y reposición el 2026-11-23 = **11 días**; desde la constitución de Nvidia (1993-04-05) hasta la renuncia = **12.274 días** (33,6 años); del «no» del 17 a la reposición del 23 = **6 días**. **Mismo método para los tres:** del día en que se anuncia la salida al día en que la persona vuelve a ser la cabeza de la empresa. Matiz que va en la descripción: Jobs ya había vuelto a Apple en febrero de 1997 con la compra de NeXT; y Altman fue destituido, no renunció.
4. **El pico es «Steve Jobs, 4.382 días» (≈ 398 veces los 11 días)**, no la proporción «1 día fuera por cada ≈ 1.116 al mando». Por qué: asombro es magnitud comparada con algo conocido (R37), y Jobs es la referencia que el público ya usa para esta noticia; la proporción es abstracta y se entiende peor en 3 s. La proporción 1.116 no se usa en el video (queda en reserva para otra pieza). Se dice también el 5 de Altman: sin él, «el regreso más corto» sería falso (Altman volvió antes).
5. **Se nombra el hecho con las palabras que la gente busca**: «resigned», «reinstated» y **una sola mención neutra del motivo en la voz, «after a scandal»**, sin detalles, sin terceros, sin adjetivos y sin juicio. La descripción trae la misma única mención.
6. **«CEO» y no «director ejecutivo»** en los subtítulos en español: es la forma que usan los titulares en español de la noticia, y es más corta (la banda cabe ≈ 21 caracteres por línea).
7. **Portada con la cifra «11 Days?» a la vista** (parámetro flexible, `PARAMETROS.md`): no es la respuesta del video (la respuesta es «más rápido que Jobs, más lento que Altman»). Se mide contra los shorts 1 y 2, que la ocultaban.
8. **Acento por plano:** mostaza en todo el video y **tomate solo en el pico** (cifra «4.382», tomas 10 y 11), como en el short 2: el cambio de mostaza a tomate marca el golpe y el canal se reconoce (R26, R33).
9. **Cierre decidido con la tabla de decisión del manual 14, sección 4b:** respuesta con remate («Faster than Jobs. Slower than Altman.») + **una pregunta abierta, nueva y respondible por el canal** («Who else came back?») que es la razón de la **única** invitación («Subscribe for the next count.») + el lápiz lanzado. **No se cierra con una pregunta de suspenso sobre el futuro de la persona**: lo único público y pendiente en las fuentes es una comparecencia ante el Congreso, que cuelga de las investigaciones sobre terceros; sería insinuar, invita al juicio y el canal no controla la respuesta (línea editorial y `PARAMETROS.md`, sección 2). Compromiso del canal: el siguiente conteo es el de otros regresos de directores ejecutivos (datos ya verificados el 2026-11-24 en `00_analisis_de_tematicas.md`, S3: Dell, Schultz, Dorsey, cada uno con su matiz). Si no se publica en 7 días, se avisa en un comentario fijado.
10. **El bucle es el vuelo del lápiz** (el último fotograma empalma con el primero), pero **no decide el cierre**: la repetición no es vista calificada (`plan_programa_de_socios.md`, 1.3). El remate y la invitación no se sacrifican por el empalme.
11. **Firma del canal: el lápiz bumerán** (regla del dueño, 2026-11-24). La especificación común del canal es `canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md` y **manda sobre este prompt**; al escribir esto aún no existía y se usó la definición de partida del encargo. Qué hace aquí: al empezar, el lápiz **ya viene girando de vuelta** y Tin lo atrapa en el fotograma 15; al terminar, Tan lo lanza girando fuera del cuadro y esa es la última acción. El objeto que miran las caras en la portada es **la silla de director vacía** (el objeto que cuenta la noticia); el lápiz es el elemento de acento mostaza del plano.
12. **Subtítulos en español quemados** (encargo del dueño): banda fija entre la zona de gráficos y los personajes (sección 12). **El primer segundo (portada) no lleva subtítulo**: la banda tapa la silla (y 720–1100) y la regla de portada pide el cuadro limpio; la línea 1 se subtitula desde 1,0 s.
13. **Sin cambio de foco:** no hay hueco de voz de 8 a 12 fotogramas entre líneas sin romper la rejilla de 0,5 s; no se fuerza (el límite de la prueba es «solo entre líneas»). La profundidad viene de capas, paralaje, sombras y desenfoque fijo del fondo.
14. **Sin «congelado con marco» al cierre** (estaba en el plan anterior): el último movimiento es el lápiz; dos adornos de cierre serían uno sin función (manual 14, sección 1).
15. **Una cosa que cambia por video:** respecto de los shorts 1 y 2 cambia el **tipo de tema** (noticia). Cambian además, por orden del dueño, la profundidad y los efectos y la firma del lápiz: no se podrán separar en la medición; los resultados de este video son «a prueba» (`PARAMETROS.md`, sección 4).

## 4. Estilo global

```text
Flat 2D vector drawing on warm cream paper (#F3E9D2) with a faint fixed paper grain and soft vignette, 1970s palette: two neutrals (cream paper, dark ink) plus ONE accent per shot (mustard in every shot except the reveal shots, tomato red only in the reveal shots), character colors (orange, brown, teal) are identity and not accents, thick dark ink outlines (#2B2420), hand-made stick-figure look, layered depth with parallax, contact shadows under feet and objects, distant layers lightly blurred and faded into the paper, no gradients on shapes, no glow, no neon, spring-based motion, slow camera push-ins.
```

**Negativo global:**

```text
text inside the drawing other than the table in section 12, brand names or logos, Nvidia logo lettering or Nvidia green, any real person drawn or imitated, faces of real people, photographs, stock charts, money, flags, courtroom or police imagery, neon, gradients on shapes, lens flare, flashes, strobing, negative-color effect, whole-screen white or black, two accent colors in the same shot, tomato red outside the reveal shots, extra characters, extra fingers, characters other than Tin and Tan, uppercase centered titles, square placeholder glyphs, symbols that are not in the font, lying-down shadow under the stick figures
```

## 5. Escenarios

- **papel_crema:** fondo `#F3E9D2` con grano fijo y viñeta suave (`efectos.papel`, el mismo grano en todos los fotogramas). Con personajes: línea de suelo `#E6D8B8` de 4 px a **86 % del alto (y = 1651)**, de 9,3 % a 90,7 % del ancho. Planos de objeto solo: sin suelo.
- **Zonas (1080x1920), zona segura de `formatos.md`:** x 100–980, y 250–1670.
  - **Texto en inglés (rótulos):** x = 10 % (108), de y = 13,2 % a 24 % (253–461); cifras al 7 % del alto (134 px).
  - **Gráficos:** de 27 % a 46,5 % (y 518–893), x 100–980.
  - **Banda de subtítulos en español:** y 905–1085 (47,1 % a 56,5 %), x 100–980 (sección 12).
  - **Personajes:** pies a 86 % (y 1651), `alto` 29 % (557 px), cabeza más alta en y 1094; nunca pisan la banda ni los gráficos. Tan en x = 30 % con `espejo=True`; Tin en x = 70 % sin espejo; solos, en x = 50 %.
- **Profundidad (`efectos.componer`):** la z 0 es el plano de los personajes; positivo = más lejos. Cámara con `apertura` 0,018, `campo` 150, `niebla` 0,30, `focal` 1000; capas lejanas (z de +260 a +420) se funden con el papel. Sombras de contacto (opacidad 0,25 a 0,30) bajo pies y objetos; sombra proyectada de objetos 0,22. **Sin sombra tumbada de los muñecos.**
- **silla_director (gráfico propio, el objeto que cuenta la noticia; genérica, vacía y sin marca):** silla plegable de director vista de frente y tres cuartos: dos patas en X de madera marrón `#7A4B2A` con contorno tinta de 0,03 H, travesaño, brazos y respaldo y asiento de lona **papel sombra `#E6D8B8`** (neutro: el acento del plano es el lápiz) con dos costuras de tinta; sin letras, sin nombre en el respaldo. Alto H, ancho 0,95 H. En la portada H = 380 px (y 720–1100, centrada en x = 540); en el fotograma 0 está a escala 0,82 (H = 312, y 754–1066) y crece a 1,0 en 12 fotogramas con frenada.
- **calendario_noviembre (gráfico propio):** hoja de noviembre de 2026 de 7 columnas (domingo a sábado) y 6 filas, ancho 840 px y alto 700 px, cuerpo blanco `#FFF8EC`, contorno tinta de 0,012 W, cabecera marrón `#7A4B2A` de 0,16 H con las siete iniciales (la fecha es el contenido del objeto), números en tinta (el 1 es domingo; el 12 jueves, el 17 martes, el 23 lunes: comprobado con `calendar`). Marcas: círculo mostaza trazado a mano (`trazo_circulo`) sobre el 12, flecha de tinta del 17 al 23 y círculo mostaza sobre el 23; **11 cruces de tinta** (del 13 al 23) que entran una cada 3 fotogramas.
- **mesa_junta (gráfico propio, genérica):** tablero marrón `#7A4B2A` de 800 x 64 px con dos patas, cinco sillas genéricas detrás (rectángulos redondeados de 90 x 150 px, papel sombra con contorno tinta) y a la izquierda la silla_director vacía a escala 1,25. **Ninguna persona, ningún papel con texto.**
- **barras (gráfico propio, escala lineal y honesta):** barras horizontales de 56 px de alto, separadas 36 px, de x = 100 a 980. Tenencia (tomas 6 y 7): 12.274 días = 880 px; 11 días = 0,8 px, **se dibuja una marca de 4 px** (la de 11 días, en mostaza) para que se vea. Comparación (tomas 9 a 12): 4.382 días = 880 px; Huang (11) = 2,2 px y Altman (5) = 1,0 px, **ambos con una marca mínima de 4 px**. Es una convención anotada en la descripción («bars to scale; the shortest are drawn at a minimum width»), no un engaño. Sin letras dentro de las barras.
- **lápiz libre (gráfico propio, firma del canal):** el lápiz de la ficha de Tin (cuerpo amarillo, punta naranja, goma roja, contorno tinta) de 2,4 R de largo (R = radio de cabeza de Tin; a `alto` 487 px, R = 88 px, largo 211 px) que gira libre. **Estela plana:** dos copias en papel sombra detrás, a los ángulos de 2 y 4 fotogramas antes. Escala de vuelo 1,4 (más cerca de la cámara, z de −420) que baja a 1,0 al llegar a la mano.
- **Muelles (masa 1, rigidez, amortiguación) por elemento:** `pop` 220 y 20 (entradas de texto y gráficos, escala de 0,85 a 1); `slide` 120 y 16 (personajes y gráficos que se desplazan); `sello` 320 y 26 (empujes y zoom de golpe). Contadores y barras: ease-out cúbico, sin muelle, para que el valor nunca pase de su final ni retroceda. Todo depende del número de fotograma (30 fps).
- **Transición `borrón`:** corte seco con desenfoque de movimiento horizontal de 18 px en los 2 últimos fotogramas de la toma que sale y en los 2 primeros de la que entra. Cero destellos.

## 6. Tomas

<!--
Todas las tomas son «edición»: dibujo por código. Tiempos al décimo de segundo, del video final (30,5 s, 915 fotogramas),
sobre la voz ESTIMADA. Cada corte cae en un pulso de 0,5 s, a 0,0–0,25 s antes del inicio de la línea que le toca.
-->

### Toma 1 — Gancho: la silla vacía y el lápiz que vuelve

- **Duración:** 1,0 s (de 0,0 a 1,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la portada: texto «Back In / 11 Days?» arriba (y 400–700), la silla_director en el centro (y 720–1100), Tan y Tin debajo de perfil mirando la silla
- **Cámara:** fija, escala 100 %
- **Acción:** el lápiz de Tin ya viene girando de vuelta desde el fotograma 0 (estela plana), baja por el lado derecho, se frena y **Tin lo atrapa en el fotograma 15**; la silla crece de 0,82 a 1,0 en 12 fotogramas; Tan, con el brazo aún extendido del lanzamiento, pregunta.
- **Audio:** línea 1, Tan (primera parte): "Was Jensen Huang's comeback in eleven days fast?" (la línea va de 0,00 a 2,31 s). Vuelo del lápiz con vibrato de 0,0 a 0,5 s y golpe al atrapar en 0,5 s (sección 13).
- **Referencia:** toma 1 del short 2 (objeto en movimiento desde el fotograma 0, portada con caras mirando)
- **Transición de entrada:** ninguna (primer fotograma; es también el último del bucle). Salida: corte en el movimiento hacia la toma 2.

**Especificación de dibujo:**

- Fotograma 0: lápiz libre con centro en (930, 790) a ángulo 35 grados y escala 1,4, estela de dos copias; **el último fotograma del video (el 914) es esta misma imagen con el lápiz saliendo** (toma 14). El lápiz puede pasar de x = 960 (solo es objeto, no cara ni texto); se mide que no toque el texto ni la silla (≥ 40 px).
- Recorrido de llegada (15 fotogramas, ease-out): (930, 790) → (975, 1050) → mano de Tin (≈ 860, 1380; se mide en el render), giro de 2,5 vueltas que se frena, escala de 1,4 a 1,0. En el fotograma 15, `pop` pequeño de 4 px hacia abajo en la mano de Tin y sonido.
- Texto «Back In / 11 Days?» entero y quieto desde el fotograma 0 (es la portada; sin `pop` de entrada), tamaño 12 % del alto, tope de las letras en y = 26 % (medida a repetir: x 116–848, y 492–682); clave «11» en mostaza con contorno de tinta; golpe de la clave en el fotograma 6 (escala 1,0 a 1,18 en 5 fotogramas y asiento en 7). Sale a los 0,9 s.
- Tan: pose `pregunta`, expresión `curiosidad`, vista `perfil`, `mira=1`, `cabeza_giro=25`, x = 24 %, pies a 86 %, `alto` 487 px (el plano de portada es más grande que el resto), `espejo=True`. Tin: pose `parado`, expresión `sorpresa`, vista `perfil`, `mira=-1`, `cabeza_giro=25`, x = 76 %, `objeto=False` hasta el fotograma 15 y `objeto="lapiz"` desde entonces. Las caras quedan dentro de la zona útil de portada (x 60–960, y 380–1440). Con suelo.
- **Sin subtítulo en español** (portada). **Color:** acento mostaza = la clave «11» + el lápiz; la silla es neutra (papel sombra y marrón). Cabezas, gorra y bufanda son identidad, no acento.

### Toma 2 — Tan hace la pregunta

- **Duración:** 1,5 s (de 1,0 a 2,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tan sola, de frente, con la silla pequeña al fondo (capa lejana)
- **Cámara:** empuje lento (avance 0 a 40)
- **Acción:** el brazo de Tan sigue subiendo a través del corte mientras termina la pregunta; la silla se ve lejos y desenfocada detrás.
- **Audio:** línea 1, Tan (segunda parte): «…in eleven days fast?» (hasta 2,31 s). Clic suave del corte.
- **Referencia:** toma 2 del short 2 (Tan pregunta)
- **Transición de entrada:** corte en el movimiento (4 fotogramas después de que arranca el brazo; el primer plano dura 30 fotogramas). Salida: corte seco.

**Especificación de dibujo:**

- Capas: papel z +900; silla_director z +420 (niebla), x = 540; Tan z 0. Tan: pose `pregunta`, expresión `curiosidad`, vista `frente`, `mira=1`, `espejo=True`, x = 50 %, pies a 86 %, `alto` 29 %, `viento` oscilante con muelle.
- Rótulo «11 days?» (clave 11) entra con `pop` en 1,1 y sale en 2,4. Subtítulo ES tarjeta 1 de 1,0 a 2,4.
- **Color:** acento mostaza = la clave «11». La silla, neutra. Con suelo.

### Toma 3 — Renunció el 12 de noviembre

- **Duración:** 4,0 s (de 2,5 a 6,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos, con el calendario de noviembre detrás y la silla en primer plano
- **Cámara:** empuje lento con profundidad (avance 0 a 90, x 540 a 575; ≈ 1 % del ancho por segundo)
- **Acción:** Tin explica con el lápiz; un círculo de tinta mostaza se dibuja sobre el 12 cuando la voz dice «twelfth»; Tan se sorprende.
- **Audio:** línea 2, Tin: "He resigned from Nvidia on November twelfth after a scandal." (de 2,54 a 6,45 s). Raspado de lápiz en el garabato.
- **Referencia:** toma 4 del short 2 (héroe abierto con el objeto del tema)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Capas: papel +900; calendario_noviembre z +260 (niebla 0,30, ligeramente desenfocado: es fondo y su fecha se lee por el rótulo, no por la hoja); silla_director z −220 (primer plano, a la izquierda, x = 150, 60 % de su tamaño de portada, **nítida y sin tapar las caras**); Tan y Tin z 0. Sombras de contacto bajo pies y bajo la silla.
- Tin: pose `explica`, expresión `feliz`, `objeto="lapiz"`, vista `frente`, x = 70 %, sin espejo, lápiz con movimiento secundario de ±3 grados. Tan: pose `senala`, expresión `curiosidad` y, desde 4,5, `sorpresa`, `espejo=True`, x = 30 %.
- `garabato` con `trazo_circulo` sobre el 12 de 4,3 a 4,7 s (12 fotogramas); rótulo «Nov 12» (clave 12) entra con `pop` en 4,2 y sale en 6,4. Subtítulo ES tarjeta 2 de 2,55 a 6,40.
- **Color:** acento mostaza = la clave «12» + el círculo del 12 + el lápiz (el lápiz es identidad de Tin; el círculo y la clave son el acento; se mide que no haya un cuarto elemento mostaza en el calendario). Con suelo.

### Toma 4 — El 17, la junta dijo que no

- **Duración:** 3,5 s (de 6,5 a 10,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con la mesa de junta detrás
- **Cámara:** empuje lento (avance 90 a 150)
- **Acción:** la mesa de junta entra desde el desenfoque; la silla de director vacía queda a la cabecera; Tin señala la mesa; Tan pregunta con la mano.
- **Audio:** línea 3, Tin: "On the seventeenth the board said it would not bring him back." (de 6,68 a 9,72 s). Clic del corte y golpe suave del revelado.
- **Referencia:** toma 4 del short 2
- **Transición de entrada:** corte seco con `revelar_desde_desenfoque` de la mesa (8 fotogramas, de 6,5 a 6,77; uno por video). Salida: corte seco.

**Especificación de dibujo:**

- Capas: papel +900; mesa_junta z +180; Tan y Tin z 0; sombra proyectada de la mesa 0,22. Tin: pose `senala`, expresión `curiosidad`, `objeto="lapiz"`, x = 70 %. Tan: pose `pregunta`, expresión `curiosidad`, `espejo=True`, x = 30 %.
- Rótulo «Nov 17» (clave 17) con `pop` en 7,0, hasta 9,9. Subtítulo ES tarjeta 3 de 6,70 a 9,70.
- **Color:** acento mostaza = la clave «17» + el lápiz como identidad; sin otro elemento mostaza. No hay tachaduras ni cruces sobre la silla (sería juicio sobre la persona). Con suelo.

### Toma 5 — Seis días después, repuesto el 23

- **Duración:** 3,0 s (de 10,0 a 13,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto con el calendario de noviembre en la zona de gráficos
- **Cámara:** fija, escala 100 %
- **Acción:** una flecha de tinta se dibuja del 17 al 23; un círculo mostaza rodea el 23; empiezan a caer las cruces del 13 al 23 (una cada 3 fotogramas, desde 11,9); Tan celebra.
- **Audio:** línea 4, Tin: "Six days later it reinstated him as C E O." (de 9,95 a 13,00 s). Tictac de las cruces con tono que sube.
- **Referencia:** toma 5 del short 1 (tira que se llena)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Calendario_noviembre en la zona de gráficos (W = 780, de 27 % a 46,5 %), z 0; flecha `trazo_flecha` de 10,3 a 10,8; círculo `trazo_circulo` sobre el 23 de 11,3 a 11,7; 11 cruces del 13 al 23 con entrada `pop` de 8 fotogramas, desfase de 3 fotogramas, de 11,9 a 13,0.
- Tin: pose `explica`, expresión `feliz`, `objeto="lapiz"`, x = 70 %. Tan: pose `celebra`, expresión `eureka`, `espejo=True`, x = 30 %, `viento` alto.
- Rótulo «+6 days» (clave 6) de 10,2 a 11,7 y rótulo «Nov 23» (clave 23) de 11,8 a 12,95, ambos al 7 %. Subtítulo ES tarjeta 4 de 10,0 a 13,0.
- **Color:** acento mostaza = la clave y el círculo del 23; flecha y cruces en tinta. Con suelo.

### Toma 6 — Once días

- **Duración:** 1,0 s (de 13,0 a 14,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** el calendario con sus 11 cruces ya puestas y Tan debajo
- **Cámara:** fija
- **Acción:** el rótulo «11 days» entra con `pop`; Tan asiente con la boca abierta.
- **Audio:** línea 5, Tin (primera parte): «Before that:» (de 13,23 a ≈ 14,0 s).
- **Referencia:** toma 6 del short 2
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Calendario de la toma 5 con las 11 cruces; Tan: pose `senala`, expresión `sorpresa`, `espejo=True`, x = 50 %, `alto` 29 %. Rótulo «11 days» (clave 11) de 13,05 a 13,95 (27 fotogramas: es el único texto, ya se leyó en la portada). Subtítulo ES tarjeta 5 empieza en 13,25.
- **Color:** acento mostaza = la clave «11»; Con suelo.

### Toma 7 — 12.274 días al mando

- **Duración:** 2,0 s (de 14,0 a 16,0)
- **Personajes:** @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la barra de tenencia a todo el ancho útil y Tin debajo
- **Cámara:** fija
- **Acción:** una barra larga crece de izquierda a derecha en 30 fotogramas y frena; en su extremo derecho una marca mínima mostaza señala los 11 días; Tin explica.
- **Audio:** línea 5, Tin (segunda parte): «more than thirty-three years in charge.» (hasta 15,77 s).
- **Referencia:** toma 7 del short 2 (cifra grande)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Barra de tenencia (sección 5): marrón, 880 px, crece de 14,1 a 15,1 (`eo`, sin muelle); marca de 4 píxeles mostaza en el extremo. Tin: pose `explica`, expresión `feliz`, `objeto="lapiz"`, x = 50 %, `alto` 29 %.
- Rótulo «12,274 days» (clave: el número) entra con `pop` en 14,3 y queda hasta 15,95. Subtítulo ES tarjeta 5 sigue hasta 15,8.
- **Color:** acento mostaza = la clave + la marca de 11 días; barra marrón (neutro de relleno). Con suelo.

### Toma 8 — Tan: «¿rápido comparado con quién?»

- **Duración:** 1,0 s (de 16,0 a 17,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tan sola, de frente
- **Cámara:** empuje lento (avance 0 a 30)
- **Acción:** Tan se encoge de hombros y pregunta; el rótulo no cambia de lugar.
- **Audio:** línea 6, Tan: "Fast compared to who?" (de 16,00 a 16,96 s).
- **Referencia:** toma 9 del short 2 (respiro de composición)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `encoge`, expresión `curiosidad`, `espejo=True`, x = 50 %, `alto` 29 %, silla_director pequeña al fondo (z +420). Sin rótulo. Subtítulo ES tarjeta 6 de 16,0 a 16,95. Con suelo. **Color:** sin acento (solo neutros y colores de Tan).

### Toma 9 — Sam Altman: 5 días

- **Duración:** 2,5 s (de 17,0 a 19,5)
- **Personajes:** @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** barras de comparación en la zona de gráficos y Tin debajo
- **Cámara:** empuje lento (avance 0 a 50)
- **Acción:** aparece una barra de Huang (11 días, marca de 4 px) y debajo la de Altman (5 días, marca de 4 px) en mostaza; Tin explica.
- **Audio:** línea 7, Tin: "Sam Altman at OpenAI: five days." (de 17,19 a 19,30 s).
- **Referencia:** toma 7 del short 2
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Barras (sección 5) con `pop` de 8 fotogramas; la de Huang en tinta, la de Altman en mostaza. Tin: pose `explica`, expresión `feliz`, `objeto="lapiz"`, x = 50 %.
- Rótulo «5 days» (clave 5) de 17,4 a 19,4. Subtítulo ES tarjeta 7 de 17,2 a 19,4. **Color:** acento mostaza = la clave y la barra de Altman. Con suelo.

### Toma 10 — El pico: Steve Jobs, 4.382 días

- **Duración:** 4,0 s (de 19,5 a 23,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con la barra grande en la zona de gráficos y la cifra arriba (pico de emoción)
- **Cámara:** fija; zoom de golpe suave de +10 % en la llegada de la cifra
- **Acción:** subida de sonido, **silencio de 12 fotogramas**, la barra de Jobs crece a todo el ancho mientras el contador sube de 0 a 4.382 con ease-out; al llegar, la cifra pasa a tomate y el zoom da su golpe; Tan se asombra y Tin levanta la mano vacía.
- **Audio:** línea 8, Tin: "Steve Jobs at Apple: four thousand, three hundred eighty-two days." (de 19,53 a 23,24 s; el número empieza ≈ 21,5).
- **Referencia:** toma 10 del short 2 (contador final)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Barras: las de Huang y Altman (marcas de 4 px, en tinta; la de Altman ya no es mostaza) y la de Jobs en marrón, que crece de 21,85 a 23,05 con el contador.
- Contador de 0 a 4.382 (enteros, formato inglés con coma en pantalla) `fx.contador` de 21,85 a 23,05 (36 fotogramas), ease-out cúbico, solo sube; en tinta mientras sube y en **tomate `#C8553D` con contorno de tinta de 0,045 em** al llegar, con `pop` del texto en ese mismo fotograma. `golpe_de_zoom` de +10 % (5 fotogramas de ida y 8 de asiento) en 23,05. Cifra quieta desde 23,05 (sigue en la toma 11: 45 fotogramas o más).
- Tan: pose `celebra`, expresión `sorpresa`, `espejo=True`, x = 30 %, `viento` alto. Tin: pose `saluda`, expresión `eureka`, **`objeto=False`** (sin lápiz: aquí el único acento es el tomate), x = 70 %.
- Rótulo «4,382 days» (arriba, 7 %): entra con el contador (21,85). Subtítulo ES tarjeta 8 de 19,55 a 21,4 («Steve Jobs, Apple:»); de 21,4 a 23,5 no hay subtítulo (la cifra ya está en grande).
- **Color (revelación):** acento tomate = la cifra; nada mostaza como acento (la bufanda de Tan es identidad). Con suelo.

### Toma 11 — Tan se asombra (la cifra queda quieta)

- **Duración:** 1,0 s (de 23,5 a 24,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano medio de Tan sola con la cifra en tomate arriba y la barra de Jobs detrás
- **Cámara:** fija
- **Acción:** Tan se encoge de hombros con la boca abierta; la cifra no se mueve.
- **Audio:** línea 9, Tan: "That is twelve years?" (de 23,47 a 24,43 s).
- **Referencia:** toma 11 del short 2
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Tan: pose `encoge`, expresión `sorpresa`, `espejo=True`, x = 50 %, `alto` 29 %. Rótulo «4,382 days» en tomate, el mismo de la toma 10, hasta 24,4. Subtítulo ES tarjeta 9 de 23,5 a 24,45. **Color:** acento tomate = la cifra; sin mostaza. Con suelo.

### Toma 12 — Remate: más rápido que Jobs, más lento que Altman

- **Duración:** 2,0 s (de 24,5 a 26,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos con las tres barras en la zona de gráficos
- **Cámara:** fija
- **Acción:** la cifra en tomate sale; el rótulo «11 days» vuelve en mostaza y la marca de Huang pasa a mostaza; Tin asiente y levanta el lápiz; Tan se ríe (respiro tras el pico, sin efectos).
- **Audio:** línea 10, Tin: "Faster than Jobs. Slower than Altman." (de 24,66 a 26,55 s).
- **Referencia:** toma 12 del short 2 (remate con los dos)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Barras de la toma 10 (Jobs marrón, Altman y Huang con marca de 4 px); la marca de Huang en mostaza. Tin: pose `explica`, expresión `risa`, `objeto="lapiz"` (vuelve el lápiz), x = 70 %. Tan: pose `encoge`, expresión `risa`, `espejo=True`, x = 30 %.
- Rótulo «11 days» (clave 11) de 24,6 a 26,4. Subtítulo ES tarjeta 10 de 24,7 a 26,5.
- **Color:** acento mostaza = la clave + la marca de Huang. Sin tomate. Con suelo.

### Toma 13 — Pregunta final e invitación; el lápiz pasa a Tan

- **Duración:** 2,5 s (de 26,5 a 29,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano de los dos con la silla de director vacía entre ellos (el plano del fotograma 0, más pequeño)
- **Cámara:** fija, escala 100 %
- **Acción:** Tan pregunta «¿quién más volvió?», Tin le pasa el lápiz en un arco corto (28,4 a 28,7) y Tan dice la invitación con el lápiz en la mano.
- **Audio:** línea 11, Tan: "Who else came back? Subscribe for the next count." (de 26,78 a 29,09 s). Una sola invitación.
- **Referencia:** toma 12 del short 2 (cierre de firma)
- **Transición de entrada:** corte seco. Salida: corte seco.

**Especificación de dibujo:**

- Silla_director (H = 312, a escala 0,82, centro x = 540, y 754–1066 como en el fotograma 0) entre los dos; Tan: pose `pregunta`, expresión `curiosidad`, vista `frente`, `espejo=True`, x = 30 %; Tin: pose `explica`, expresión `feliz`, x = 70 %. Lápiz libre que pasa de Tin a Tan en 8 fotogramas (28,4–28,67) con giro de media vuelta; desde 28,67 Tan lleva `objeto="lapiz"` y Tin `objeto=False`.
- Rótulos: «Who else?» (clave: else) de 26,85 a 28,1; «Subscribe» (clave) de 28,2 a 28,95. Subtítulo ES tarjeta 11 de 26,8 a 27,9 y tarjeta 12 de 28,0 a 29,1.
- **Color:** acento mostaza = la clave y el lápiz. Con suelo.

### Toma 14 — Cierre en bucle: Tan lanza el lápiz

- **Duración:** 1,5 s (de 29,0 a 30,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** el plano de la toma 13 que se transforma en el de la portada
- **Cámara:** fija, escala 100 %
- **Acción:** Tan, con el lápiz, hace la **anticipación** (6 fotogramas hacia atrás, de 29,63 a 29,83) y lo **lanza** girando (20 fotogramas, de 29,83 a 30,5): el lápiz sale hacia la cámara y hacia arriba a la derecha; el último fotograma es el fotograma 0 (lápiz en (930, 790) a 1,4 de escala y Tan con el brazo extendido).
- **Audio:** sin voz (la voz terminó en ≈ 29,09: 1,41 s de silencio de voz hasta el empalme). Whoosh con vibrato atado al giro (sección 13).
- **Referencia:** toma 1 de esta versión (el vuelo del lápiz cierra el bucle)
- **Transición de entrada:** corte seco. Salida: bucle al fotograma 0 de la toma 1.

**Especificación de dibujo:**

- De 29,0 a 29,6 plano fijo con los dos de frente, respirando (acción secundaria). A 29,63 se pasan, sin corte, a la composición de la portada (personajes de perfil con la cabeza a 25 grados) en 6 fotogramas de `slide`; **el último fotograma debe ser igual al fotograma 0** (diferencia media menor de 3 de 255, como en el short 2). Lápiz libre con estela, z de 0 a −420, escala de 1,0 a 1,4, giro de 3 vueltas con aceleración (ease-in), trayectoria de la mano de Tan (≈ 280, 1380) a (930, 790).
- Texto «Back In / 11 Days?» entra con `pop` en 30,0 y está a escala 1 en 30,5 (igual que el fotograma 0). Sin subtítulo en español en 29,6–30,5 (cuadro de portada limpio). **Color:** acento mostaza = la clave «11» + el lápiz. Con suelo.

## 7. Audio

- **Voz (por generar; una sola generación por voz, regla de un solo intento):** Tan con Zelda (líneas 1, 6, 9 y 11) y Tin con Kevin (líneas 2, 3, 4, 5, 7, 8 y 10), Higgsfield `seed_audio`, voces ya elegidas por el dueño. Después, `atempo=1.10`, −14 LUFS y armado del diálogo como en el short 2 (0,23 s entre líneas, pausas internas largas acortadas a 0,15 s, salvo la de «Apple:», que se deja de 0,45 s a propósito para el silencio antes del número). **Costo: por cotizar con `estimate_audio_cost` antes de pedir el sí del dueño** (la cotización del plan anterior fue 3,7 créditos con un texto parecido). Nadie ha oído las voces: «Nvidia», «Huang», «C E O» y «OpenAI» se comprueban al oído; si el generador lee mal un nombre, se corrige en edición o se pide autorización para regenerar esa voz.

Guion de voz (líneas numeradas, quién habla, texto exacto, inicio y fin estimados):

| Línea | Quién | Empieza (s) | Termina (s) | Dura (s) | Texto exacto (números como se dicen) | Sílabas |
|---|---|---|---|---|---|---|
| 1 | Tan | 0,00 | 2,31 | 2,31 | Was Jensen Huang's comeback in eleven days fast? | 12 |
| 2 | Tin | 2,54 | 6,45 | 3,91 | He resigned from Nvidia on November twelfth after a scandal. | 18 |
| 3 | Tin | 6,68 | 9,72 | 3,04 | On the seventeenth the board said it would not bring him back. | 14 |
| 4 | Tin | 9,95 | 13,00 | 3,04 | Six days later it reinstated him as C E O. | 14 |
| 5 | Tin | 13,23 | 15,77 | 2,54 | Before that: more than thirty-three years in charge. | 11 |
| 6 | Tan | 16,00 | 16,96 | 0,96 | Fast compared to who? | 5 |
| 7 | Tin | 17,19 | 19,30 | 2,11 | Sam Altman at OpenAI: five days. | 9 |
| 8 | Tin | 19,53 | 23,24 | 3,71 | Steve Jobs at Apple: four thousand, three hundred eighty-two days. | 15 |
| 9 | Tan | 23,47 | 24,43 | 0,96 | That is twelve years? | 5 |
| 10 | Tin | 24,66 | 26,55 | 1,89 | Faster than Jobs. Slower than Altman. | 8 |
| 11 | Tan | 26,78 | 29,09 | 2,32 | Who else came back? Subscribe for the next count. | 11 |

Voz total estimada de 0,00 a 29,09 s; hasta 30,5 hay 1,41 s sin voz y al volver al fotograma 0 la voz entra sin silencio inicial (silencio del empalme: 1,41 s, menos de 2 s).

**Pregunta de apertura:** línea 1 («Was Jensen Huang's comeback in eleven days fast?»). **Pregunta de cierre:** línea 11 («Who else came back?»). **Respuesta a la de apertura:** línea 10.

**Texto para generar cada voz (una pieza por personaje; líneas separadas por una línea en blanco; la última es una coletilla descartable para que no llegue cortada la última palabra útil; sin comas en las líneas de Tan: Zelda hace pausas de 0,7 a 0,8 s tras una coma):**

Voz de Tan (Zelda), una sola generación, 4 líneas y coletilla:

```text
Was Jensen Huang's comeback in eleven days fast?

Fast compared to who?

That is twelve years?

Who else came back? Subscribe for the next count.

That's all, folks.
```

Voz de Tin (Kevin), una sola generación, 7 líneas y coletilla:

```text
He resigned from Nvidia on November twelfth after a scandal.

On the seventeenth the board said it would not bring him back.

Six days later it reinstated him as C E O.

Before that: more than thirty-three years in charge.

Sam Altman at OpenAI: five days.

Steve Jobs at Apple: four thousand, three hundred eighty-two days.

Faster than Jobs. Slower than Altman.

That's all, folks.
```

- **Subtítulos:** `02_prompt/subtitulos.srt` (inglés, igual que la voz) y `02_prompt/subtitulos_es.srt` (español, pista para YouTube). Tiempos estimados.
- **Música:** hecha con código (Python y numpy), **mi menor (eólico)** a 120 BPM (el pulso de la rejilla), a −24 LUFS (10 dB bajo la voz): ostinato de bajo en corcheas, pad suave y un riser que sube de 20,5 a 21,3 s; calla 12 fotogramas en 21,1–21,5 s y en 23,05 entra un acorde de **mi mayor** abierto con el ding (de tensión a asombro). **Distinta de la del short 2 (do mayor, 120 BPM)**; la del short 1 se comprueba en su `licencias.md` antes de componer. Sin música de terceros.
- **Efectos:** los de la sección 13, hechos con código, sin material de terceros.

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → … → Toma 14 (y vuelve a la toma 1). Las tomas 1 y 14 comparten el fotograma de empalme.
- **Transiciones (todas motivadas):** corte en el movimiento (1 a 2), revelado desde desenfoque de la mesa (3 a 4, una vez), corte seco en el resto. Sin barridos, sin destellos, sin negativo, sin «atravesar la escena», sin congelado.
- **Texto en pantalla:** se dibuja en el mismo render: los rótulos en inglés de la sección 12 y la banda de subtítulos en español. El texto nunca contradice lo que se oye.
- **Portada:** el fotograma 0 cumple los 6 puntos de la regla del dueño (`ENTREGA_YOUTUBE.md`, «Portada de los Shorts»): «Back In / 11 Days?» (4 palabras en 2 líneas, mayúscula inicial en cada una, clave «11» en mostaza) entre y 400 y 700; **el objeto del centro es la silla de director vacía** (y 720–1100), que es el que cuenta la noticia (esa regla habla de «objeto nostálgico»; aquí manda `PARAMETROS.md`: el objeto es el del tema); las caras de Tan y Tin, de perfil y con la cabeza a 25 grados, mirándola, dentro de la zona útil (x 60–960, y 380–1440). **Excepción a «sin la respuesta ni el número»:** la cifra «11» va a la vista por decisión del equipo (`PARAMETROS.md`: «La cifra en el título o en la portada: se decide por video»); no es la respuesta del video. El video cumple lo que promete la portada. `codigo/miniatura.py` guarda el fotograma 0 como `06_final/portada_short03.png` (1080x1920) y mide las cajas.
- **Formato de salida:** 1080x1920, 30 fps, H.264, yuv420p, AAC a 48 kHz. Archivo `06_final/tin_y_tan_short03_v1.mp4`. Pesa unos 3 MB: se recomprime a CRF 22 si pasa de 3,1 MB.
- **Título de la publicación (inglés):** Jensen Huang Is Back as Nvidia CEO After 11 Days
- **Descripción de la publicación (en inglés, obligatoria; con una línea de suscripción):**

```text
Jensen Huang is back as Nvidia's CEO. Was 11 days fast? We counted.

Timeline:
Nov 12, 2026: Jensen Huang resigned from Nvidia after a scandal.
Nov 17, 2026: Nvidia's board said it would not bring him back.
Nov 23, 2026: the board reinstated him as president and CEO, 6 days later. Nov 12 to Nov 23 is 11 days.
Before that he had led Nvidia since it was incorporated on Apr 5, 1993: 12,274 days, more than 33 years.

Other comebacks, counted the same way (from the day the exit was announced to the day the person was back at the top job):
Sam Altman, OpenAI: removed on Nov 17, 2023, reinstated on Nov 22, 2023: 5 days.
Steve Jobs, Apple: resignation letter on Sep 17, 1985, named interim CEO on Sep 16, 1997: 4,382 days (≈ 12 years). He had rejoined Apple earlier, in February 1997, when it bought his company NeXT.
So 11 days is faster than Jobs and slower than Altman. The exits were different: one resigned, one was removed. Bars are to scale; the shortest are drawn at a minimum width so they can be seen.

Who else came back? Subscribe to Tin & Tan for the next count.

Sources, all read on 2026-11-24: Wikipedia, "Jensen Huang"; Wikipedia, "Nvidia"; Wikipedia, "Removal of Sam Altman from OpenAI"; Wikipedia, "Steve Jobs". Nvidia's own announcement could not be opened, so the Nov 23 date also rests on news channel headlines (CNN, BBC, NBC, CBS, ABC and Fox News).

Not affiliated with Nvidia. Jensen Huang is not involved in this video.
```

- **Etiquetas (en total, menos de 500 caracteres):** Jensen Huang, Nvidia, Jensen Huang is back, Nvidia CEO, Jensen Huang CEO, Jensen Huang reinstated, Jensen Huang resigned, CEO comeback, Sam Altman, Steve Jobs, Tin & Tan, shorts
- **Pasan por `revisar_texto.py`:** la descripción, las etiquetas y `subtitulos.srt` con `--idioma en`; `subtitulos_es.srt` con `--idioma es`; los textos de pantalla del código se pasan antes de renderizar. Resultado y glosario: sección 14.
- **Fuentes y fechas:** Wikipedia en inglés «Jensen Huang» (renuncia el 2026-11-12; reposición el 2026-11-23; «does not intend to reinstate» el 2026-11-17, citado en `00_analisis_de_tematicas.md`), «Nvidia» (constitución el 5 de abril de 1993), «Removal of Sam Altman from OpenAI» (destituido el 17 y repuesto el 22 de noviembre de 2023) y «Steve Jobs» (carta de renuncia el 17 de septiembre de 1985; compra de NeXT cerrada en febrero de 1997; nombrado director ejecutivo interino el 16 de septiembre de 1997), todas leídas el 2026-11-24. Las cadenas (CNN, BBC, NBC, CBS, ABC, Fox News) coinciden en sus títulos de YouTube del mismo día. **El comunicado de Nvidia no se pudo abrir.** El título de The New York Times sobre Jobs es del 17 de septiembre de 1997 (Wikipedia da el 16): la diferencia es de un día y se declara aquí.

### Título (ficha)

Filtro: `revisar_titulo.py` **versión 1.1 (modo flexible)**, corrido el 2026-11-24. Estudio y reglas: `video-studio/comercial/titulos.md`.

| Campo | Valor |
|---|---|
| `titulo_elegido` | Jensen Huang Is Back as Nvidia CEO After 11 Days |
| `caracteres` | 48 |
| `idioma` | en |
| `canal` | tin-y-tan |
| `formato` | short |
| `publico` | EE. UU., adultos que siguen la noticia; sin edad fija (manda el dato de Studio) |
| `frase_de_busqueda` | jensen huang is back |
| `fuente_de_la_frase` | títulos de YouTube del 2026-11-24 (`00_analisis_de_tematicas.md`, «Segunda vuelta», S2: «Jensen Huang Is Back…»); volumen: sin dato |
| `formula` | nombre buscado + palabras de la noticia + cifra a la vista |
| `alternativa_1` | Jensen Huang Nvidia CEO: Back After 11 Days (43 caracteres; frase «jensen huang nvidia ceo»; filtro: PASA, 0 errores, 0 avisos) |
| `alternativa_2` | Jensen Huang Is Back: Was 11 Days Fast? (39 caracteres; frase «jensen huang is back»; filtro: PASA, 0 errores y 1 aviso: M11, la marca «Nvidia» no aparece en el título; se acepta porque el descargo va en la descripción y el título no lo necesita) |
| `uso_de_las_alternativas` | Reserva. YouTube no ofrece prueba A/B de títulos en Shorts (ayuda oficial, leída el 2026-11-21). No se cambia un título publicado antes de los 28 días y sin datos del canal |
| `filtro` | **PASA** · errores: ninguno · avisos: ninguno (corrido con `--marca "Jensen Huang" --marca "Nvidia" --descripcion` y `--proyecto 2026-11-24_tin_y_tan_jensen_huang`) |
| `revision_humana` | **Pendiente**: que el video cumpla lo que el título promete (dice que volvió a los 11 días y la compara con otros regresos), que no engañe y que pase la línea editorial (una sola mención neutra del motivo, sin detalles ni juicio). Firma el director creativo cuando exista el video |
| `medicion` | Visto frente a deslizado, mostrado en el feed y tráfico de búsqueda; a 7 y 28 días; meta: superar el 20,7 % del short 1 |

La cifra «11 Days» está en el título y en la portada a propósito (parámetro flexible); no es la respuesta del video.

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | 0 s (las 14 tomas son edición; 30,5 s se resuelven en edición) | 0 |
| Keyframes | 0 | 0 |
| Remates en resolución final | 0 | 0 |
| Voz (Tan con Zelda y Tin con Kevin, una generación por voz) | 2 generaciones, sin generar | por cotizar con `estimate_audio_cost` (referencia del plan anterior: 3,7 créditos); necesita el sí del dueño |
| **Total estimado** | 0 créditos en imagen y video; voz por cotizar y por autorizar | 0 |

## 10. Restricciones críticas

Van al inicio de cada prompt de video, antes de la descripción. Son las que no se negocian.

```text
CRITICAL: no text, captions, subtitles, logos or watermarks unless listed in section 12.
CRITICAL: the character looks identical in every shot (same design, colors, proportions).
CRITICAL: hard cuts only, no morphing between shots.
CRITICAL: every figure, name or claim on screen comes from the project's facts file, with source and date.
CRITICAL: counters only go up and never pass their final value; no text over a character; no Nvidia logo, lettering or green; all objects are generic drawings with no logos; no real person is drawn, imitated, quoted or given words; the reason for the resignation is named once, neutrally, and never described.
CRITICAL: no flashes: at most 2 sudden brightness changes in any second (hard limit 3); no negative-color effect, no go-through-the-scene transition, no strobing.
```

## 11. Gancho, ritmo y cierre

- **Regla formal de la pieza:** hechos en orden con fecha, una cifra por plano y una comparación honesta; la cifra solo sube; todo corte cae en un pulso de 0,5 s.
- **Rejilla de tiempo:** pulso de 0,5 s; 61 pulsos = 30,5 s. La voz entra en el pulso 0 (fotograma 0). Los 13 cortes caen en 1,0; 2,5; 6,5; 10,0; 13,0; 14,0; 16,0; 17,0; 19,5; 23,5; 24,5; 26,5 y 29,0 (más el bucle en 30,5). Inicios estimados de la voz: 0,00; 2,54; 6,68; 9,95; 13,23; 16,00; 17,19; 19,53; 23,47; 24,66 y 26,78. Cada corte cae de 0,0 a 0,25 s antes de la línea que le toca; los de 13,0 y 14,0 caen dentro de la línea 5 a propósito («Before that:» / el número). Se revisan al oído con la voz real.
- **Gancho (0 a 2,5 s):** el fotograma 0 es la portada: la silla de director vacía, el lápiz de Tin ya girando de vuelta (con estela), «Back In / 11 Days?» entero, Tan y Tin de perfil mirando la silla, y la voz de Tan ya preguntando «Was Jensen Huang's comeback…» desde el fotograma 0. Tin atrapa el lápiz en el fotograma 15. En 1,0 el corte en el movimiento pasa a Tan sola. Sin logo, sin título, sin segundo mudo. **Una sola incógnita abierta:** ¿rápido comparado con quién?
- **Empieza en movimiento:** sí: el lápiz gira y se acerca desde el fotograma 0, la silla crece y Tan y Tin rebotan.
- **Motivo visual que vuelve (con las mismas formas y colores):** la silla_director vacía (tomas 1, 2, 3, 4, 8, 13 y 14), el calendario de noviembre (tomas 3, 5 y 6), las barras (tomas 7 y 9 a 12) y el lápiz de Tin (tomas 1, 3 a 7, 9, 12, 13 y 14).
- **Cierre:** decidido con la tabla de la sección 4b del manual 14 (resumida en 4b.3): **respuesta con remate** (toma 12), **una pregunta abierta, nueva y respondible** (toma 13: «Who else came back?») **que es la razón de la única invitación** («Subscribe for the next count.») y el lápiz lanzado (toma 14) que empalma con el fotograma 0. La pregunta final no es de suspenso sobre la persona. La voz termina en 29,09; silencio de voz en el empalme: 1,41 s.
- **Llamado a la acción:** **uno solo**: «Subscribe for the next count.», dicho por Tan en 28,3 a 29,09 s, corto y sin promesas ni recompensas. Por qué: los suscriptores son uno de los dos umbrales del Programa; el short 1 dio 0 sin pedirla (`plan_programa_de_socios.md`, P6).

Mapa de ritmo (tiempos estimados; cortes por segundo = cortes dentro del tramo, sin contar el inicio):

| Tramo | Segundos | Pulso o intervalo | Cortes por segundo | Qué pasa (una acción) | Respiro |
|---|---|---|---|---|---|
| Gancho | 0,0–2,5 | 1,0 s y 1,5 s | 0,4 | la silla vacía, el lápiz que vuelve y la pregunta de Tan | no |
| Hechos | 2,5–13,0 | 4,0 s, 3,5 s y 3,0 s | 0,2 | renunció el 12; el 17 la junta dijo que no; el 23 lo repuso | sí (planos largos) |
| Cuenta | 13,0–17,0 | 1,0 s, 2,0 s y 1,0 s | 0,75 | 11 días; 12.274 al mando; «¿rápido comparado con quién?» | no |
| Comparación y pico | 17,0–24,5 | 2,5 s, 4,0 s y 1,0 s | 0,3 | Altman 5 días; Jobs 4.382 días (pico en 23,05 s, 75,6 %) | sí (cifra quieta 1,45 s) |
| Remate y cierre | 24,5–30,5 | 2,0 s, 2,5 s y 1,5 s | 0,3 | más rápido que Jobs; pregunta final, invitación y lápiz lanzado | sí (final con movimiento) |

Total: 13 cortes en 30,5 s. Densidad baja a propósito: la voz es continua y cada cifra necesita su plano; la densidad extra va dentro de cada toma (lápiz, barras, cruces, contador, reacciones de Tan).

**Dónde cae el pico:** la subida empieza al 67 % (20,5 s), el silencio de 12 fotogramas al 69 % y la cifra llega al **75,6 %** (23,05 s). Si la voz real lo lleva más allá del 75 %, se recorta la pausa de «Apple:» o la línea 5 en edición (≈ 0,5 s).

Lo que sale se va antes de que entre lo siguiente: los textos salen de 0,05 a 0,2 s antes del corte siguiente. El movimiento es mecánica: entradas con `pop` o `slide`, contadores con ease-out cúbico, el giro del lápiz con ease, sin interpolación lineal en lo vivo.

Tipos de plano disponibles y dónde van: detalle (tomas 6, 7 y 9), héroe abierto (tomas 3, 4, 5, 10, 12 y 13; el principal es la 10, con la cifra), subjetivo (no hay: no hay objeto de época que usar con las manos), revelado (la mesa de junta, toma 4), objeto que salta sobre el mismo fondo (las marcas de 11 y 5 días en las barras). **No más de 3 destellos por segundo:** hay cero (no hay destello ni negativo).

### Profundidad y efectos

Cada efecto sale de `manual/14_efectos_y_emocion.md` (secciones 2, 3, 4, 4b y 6). Procedimiento de 5 pasos: objetivo (Programa de socios) → emoción de ese segundo → punto de mirada → efecto de la tabla → métrica con su segundo. Sellos: **(inv.)** investigación, **(oficio)**, **(hip.)** hipótesis del equipo (manual 14, sección 0). Emoción buscada: **curiosidad → tensión → asombro** (alta activación, R32).

**Tabla A — por toma: capas y z, foco, cámara, sombras, transición y efecto de acento**

| Toma | Capas y su z | Foco | Cámara | Sombras | Transición de entrada | Efecto de acento |
|---|---|---|---|---|---|---|
| 1 (0,0–1,0) | papel +900; silla 0 a −100 (crece); Tan y Tin 0; lápiz libre −420 a 0 | todo nítido | fija | contacto bajo pies y silla | ninguna (bucle) | lápiz que vuelve (15 f) y golpe de «11» (f 6) |
| 2 (1,0–2,5) | papel +900; silla +420 (niebla); Tan 0 | z 0 | avance 0 a 40 | contacto de Tan | corte en el movimiento | `pop` de «11 days?» |
| 3 (2,5–6,5) | papel +900; calendario +260; silla −220; Tan y Tin 0 | z 0 | x 540 a 575, avance 0 a 90 | contacto de pies y silla | corte seco | círculo mostaza sobre el 12 (12 f) |
| 4 (6,5–10,0) | papel +900; mesa +180; Tan y Tin 0 | z 0 | avance 90 a 150 | proyectada de la mesa; contacto | revelado desde desenfoque (8 f) | `pop` de «Nov 17» |
| 5 (10,0–13,0) | papel +900; calendario 0 (zona de gráficos); Tan y Tin 0 | z 0 | fija | contacto de pies | corte seco | flecha, círculo del 23 y 11 cruces |
| 6 (13,0–14,0) | papel +900; calendario 0; Tan 0 | z 0 | fija | contacto de Tan | corte seco | `pop` de «11 days» |
| 7 (14,0–16,0) | papel +900; barra 0; Tin 0 | z 0 | fija | contacto de Tin | corte seco | barra que crece (30 f) |
| 8 (16,0–17,0) | papel +900; silla +420; Tan 0 | z 0 | avance 0 a 30 | contacto de Tan | corte seco | ninguno (respiro) |
| 9 (17,0–19,5) | papel +900; barras 0; Tin 0 | z 0 | avance 0 a 50 | contacto de Tin | corte seco | barra de Altman en mostaza |
| 10 (19,5–23,5) | papel +900; barras 0; Tan y Tin 0 | z 0 | fija; golpe de zoom +10 % en 23,05 | contacto de pies | corte seco | subida, silencio, contador, tomate |
| 11 (23,5–24,5) | papel +900; barras 0; Tan 0 | z 0 | fija | contacto de Tan | corte seco | cifra quieta |
| 12 (24,5–26,5) | papel +900; barras 0; Tan y Tin 0 | z 0 | fija | contacto de pies | corte seco | mostaza de vuelta en «11 days» |
| 13 (26,5–29,0) | papel +900; silla 0; Tan y Tin 0; lápiz libre (arco) | z 0 | fija | contacto de pies y silla | corte seco | pase del lápiz y `pop` de «Subscribe» |
| 14 (29,0–30,5) | las de la toma 13 más el lápiz libre −420 | z 0 | fija | contacto | corte seco | anticipación y lanzamiento del lápiz (26 f) |

**Tabla B — por efecto: las tres respuestas del manual (emoción, punto de mirada, métrica), su dosis y su respaldo**

| N.º | Efecto (herramienta) | Segundo y dosis | Emoción | Punto de mirada | Métrica | Respaldo y sello |
|---|---|---|---|---|---|---|
| 1 | **Firma: el lápiz bumerán llega y Tin lo atrapa** (lápiz libre con estela, giro con frenada, escala 1,4 a 1,0) | 0,0–0,5 s; 15 f; 2,5 vueltas que se frenan; golpe de sonido al atrapar | orientación y curiosidad («algo vuelve») | el lápiz y después la mano de Tin (≈ 860, 1380) | visto frente a deslizado, contra el 20,7 % del short 1; retención 0–1,5 s | R4, R5 **(inv.)** (lo que crece y se acerca atrae); R10 **(inv.)**; R22 **(oficio)** (anticipación y acción superpuesta); que una firma repetida se reconozca (R26 **(inv.)**) y que baje los deslizados: **(hip.)** |
| 2 | **Silla vacía que crece** (capa animada en z, de 0,82 a 1,0) | 0,0–0,4 s; 12 f con frenada; ocupa ≈ 35 % del ancho | curiosidad (una silla vacía es una incógnita) | el centro de la silla (540, 910) | visto frente a deslizado | R28 **(inv.)** (incertidumbre); R4 **(inv.)**. Movimiento secundario: el principal es el lápiz (un solo cambio grande) |
| 3 | **Palabra clave con golpe en mostaza** (`palabra_clave`) más su golpe de sonido | f 6 a 18; 5 f de ida y 7 de asiento; escala 1,0 a 1,18; el texto está entero desde el fotograma 0 y queda hasta 0,9 s | énfasis | «11» | visto frente a deslizado; retención al segundo 1 | R33, R10 **(inv.)**; R39 **(oficio)**. Adaptación: la portada exige el texto entero en el fotograma 0 |
| 4 | **Corte en el movimiento** | 1,0 s, 4 f después de que arranca el brazo de Tan; el primer plano dura 30 f | reorientación sin sobresalto | el brazo y la cara de Tan | que no haya caída en 1,0–1,5 s | R14 **(oficio)**, R13 y R11 **(inv.)** (resumen). Desviación: 1,0 s y no 0,7 s para respetar la rejilla |
| 5 | **Capas con paralaje, desenfoque fijo del fondo y sombras de contacto** (`Capa`, `Camara`, `componer`, `sombra_contacto`) | tomas 2 a 13; 3 capas; cámara ≈ 1 % del ancho por segundo (límite 8 %) | presencia y atención tranquila; credibilidad | los personajes y el rótulo | retención de 2,5 a 13,0 s sin caída | R1, R3, R7 **(inv.)**, R8 **(oficio)**; que retenga más: **(hip.)** |
| 6 | **Revelado desde desenfoque** (`revelar_desde_desenfoque`), una vez | 6,5–6,77 s; 8 f | anticipación breve («¿quién es la junta?») | la mesa y la silla a la cabecera | retención en 6,5 s | R28 **(inv.)**; que lo borroso se lea como «entra algo nuevo»: **(hip.)** |
| 7 | **Garabato que se dibuja** (`trazo_circulo`, `trazo_flecha`, `garabato`) | círculo del 12 en 4,3–4,7 s (12 f); flecha 17 a 23 en 10,3–10,8 s (15 f); círculo del 23 en 11,3–11,7 s (12 f); sin texto debajo | cercanía y curiosidad por el trazo | la fecha rodeada | retención en cada trazo | R28 **(inv.)**; R41 (poca prueba de que enseñe más): **(hip.)** |
| 8 | **Cruces que caen** (11 marcas, una cada 3 f; el patrón de la tira de 13 bloques del short 2) | 11,9–13,0 s; entrada de 8 f, desfase de 3 f | anticipación y satisfacción al contar | la fila de fechas del 13 al 23 | retención de 11,9 a 14,0 s | R22 **(oficio)**; R28 **(inv.)**; la forma: **(hip.)** |
| 9 | **Gráfico que crece** (barras a escala, con marca mínima de 4 px) | tenencia 14,1–15,1 s (30 f con frenada); Jobs 21,85–23,05 s (36 f) | comprensión y asombro ante lo mucho mayor | el extremo de la barra | retención y compartidos | R37 **(inv.)**; su uso en gráficos: **(hip.)**; la escala no engaña: la marca mínima se declara (manual 12, cifras con fuente) |
| 10 | **El pico: subida de sonido, silencio de 12 f, contador que acelera y frena, un zoom de golpe suave, cifra quieta** (`contador`, `golpe_de_zoom`, `acercar`) | subida 20,5–21,3 s; silencio de 21,1 a 21,5 s; contador 21,85–23,05 s (36 f); zoom +10 % (5 f + 8 f); cifra quieta 23,05–24,5 s (≈ 43 f; con la voz real se alarga a 45 f); 75,6 % del video | anticipación → sorpresa → asombro | la cifra «4,382 days» arriba a la izquierda | pico de retención en 23,05 s; compartidos por mil vistas | R22 **(oficio)**, R28, R32, R34, R35 **(inv.)**. Solo zoom, sin destello (manual 4: «uno o el otro») |
| 11 | **Paso a tomate** (mostaza a tomate solo en el pico) | 23,05–24,5 s; un elemento | golpe y recordación de la cifra | la cifra | retención de los segundos 1 a 3 y del 23 al 24 | R33 **(inv.)**; manual 13 |
| 12 | **Plano de respiro tras el pico** | 24,5–26,5 s; 60 f sin efectos nuevos | alivio breve, sin dejar caer la activación | los dos personajes | línea plana en la curva (P1) | el estímulo repetido pierde efecto, R10 **(inv.)**; «picos y respiros» **(hip.)** |
| 13 | **Cierre: respuesta con remate + pregunta abierta + una invitación + lápiz lanzado** (pase del lápiz, anticipación y lanzamiento) | 24,66–30,5 s; pase 8 f (28,4–28,67); anticipación 6 f y lanzamiento 20 f (29,63–30,5); whoosh con vibrato atado al giro | sorpresa y asombro cerrados, curiosidad nueva, gratitud | el lápiz que sale y la boca de Tan | suscriptores por cada mil vistas; compartidos; regreso al canal | R48, R51, R52 **(inv.)** (manual 4b); R50 **(oficio)**; que la pregunta suba los suscriptores: **(hip.)** |
| 14 | **Acción secundaria continua y curvas con frenada** | todo el video: bufanda de Tan (`viento`), lápiz de Tin (±3 grados) | calidez y vida | los personajes | comentarios que nombran a Tin o a Tan | R22 **(oficio)**, R24 **(inv.)** |
| 15 | **Paso de neutro a acento** (mostaza) | la clave y un elemento por plano | foco y recordación | la palabra o la cifra | retención de los segundos 1 a 3 | R33 **(inv.)**; manual 13 |

**Dosis y límites (manual 14, sección 6) que este video respeta:** sin cambio de foco (ver decisión 13); 1 revelado; 1 golpe de zoom de +10 % (máximo +35 %); 1 animación de acercamiento fuerte (el lápiz; la silla es suave); cámara por debajo de ≈ 8 % del ancho por segundo y sin dos movimientos de cámara encadenados; **cero destellos y cero negativos**; sin «atravesar la escena»; sin sombra tumbada de los muñecos; texto sin movimiento mientras se lee; el texto entra con `pop` y se queda 30 f o más (45 f para la cifra del pico). **`efectos.comprobar_destellos` se corre con margen** (máximo 2 cambios bruscos por segundo, no 3) sobre los 915 fotogramas; no hay estrobo; ningún rojo parpadea.

**Cierre, decidido con la tabla del manual (4b.3), resumida:**

| Tipo de cierre | Emoción | Métrica | Riesgo | Decisión aquí |
|---|---|---|---|---|
| Pregunta de suspenso abierta | curiosidad con tensión | regreso, suscriptores | frustración, engaño, insinuación sobre una persona | **No**: el único hecho público pendiente cuelga de investigaciones sobre terceros |
| Respuesta completa con remate | asombro, cierre | retención final, compartidos | «ya está» | **Sí** (toma 12): base |
| Pregunta al espectador para comentar | participación | comentarios | invita al juicio de una persona | **No** |
| Promesa de continuación (pregunta abierta, nueva y respondible) | anticipación | suscriptores, regreso | prometer lo que no se hace | **Sí** (toma 13), con compromiso de publicar el siguiente conteo |
| Bucle perfecto | cierre redondo | duración media > 100 % | la repetición no es vista calificada | **Visual y gratis** (el lápiz), no decide el cierre |
| Invitación a suscribirse | gratitud | suscriptores | súplica, más de una petición | **Sí**, una vez, después del remate y atada a la pregunta |

## 12. Texto en pantalla y sistema de diseño

- **Tipografías:** Inter Display Medium con sus **dígitos abiertos** (`ss01`), licencia SIL Open Font License 1.1 (`/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf`). Rótulos en inglés en minúsculas, a la izquierda, salvo los nombres propios y siglas con mayúscula inicial («Nov», «CEO»); la portada con mayúscula inicial en cada palabra. **Excepción obligatoria (regla del dueño):** los nombres propios llevan mayúscula («Tin & Tan», «Tin», «Tan», «Nvidia», «Jensen Huang»).
- **Paleta:** papel `#F3E9D2` · papel_sombra `#E6D8B8` · tinta `#2B2420` · naranja `#E07A2E` · marrón `#7A4B2A` · verde azulado `#2F7F7A` · mostaza `#E8B33B` (**acento único** salvo en el pico) · tomate `#C8553D` (**acento solo del pico**, tomas 10 y 11: la cifra «4,382») · rubor `#E9967A` · blanco `#FFF8EC` (cuerpo del calendario). Un acento por plano; mostaza y tomate nunca comparten plano. La palabra clave lleva trazo de tinta de 0,045 em. **Ningún verde de Nvidia.**
- **Referencias de movimiento:** `01_referencia/` está vacía. Referencias cargadas: `canales/nostalgia-tin-y-tan/DESIGN.md`, `herramientas/palitos.py`, `herramientas/efectos.py`, las hojas de `personajes/tin/referencias/` y `personajes/tan/referencias/`, el prompt del short 2 y la prueba de efectos (`proyectos/2026-11-23_prueba_efectos_tin_y_tan/07_revision/notas.md`).
- **Prohibido:**
  1. Mayúsculas centradas sobre degradado o cualquier fondo con degradado.
  2. Animaciones lineales de posición o escala en lo vivo (solo muelle o ease-out cúbico; lineal solo en lo mecánico).
  3. Los símbolos «→» y cualquier glifo sin comprobar. «≈» solo si la fuente lo trae (se comprueba antes de renderizar); si no, en la descripción.
  4. Un contador que retrocede o que se pasa de su valor final y vuelve.
  5. Texto encima de un personaje o de la silla. Excepción: la fecha del calendario es el contenido de ese objeto.
  6. Cualquier elemento de Nvidia: logotipo, letra del logo, verde, tarjetas, chips; y cualquier rostro, voz o frase de una persona real.
  7. Líneas sin suavizar: ningún dibujo fuera de un `Lienzo` o `LienzoCapa` con supermuestreo.
  8. Sombras tumbadas de los muñecos, resplandor, partículas, confeti.
  9. Rótulos de más de 3 palabras (salvo la portada, de 4 en 2 líneas), de más de una línea o fuera de la zona segura.
  10. Cambiar los colores o accesorios de Tin y Tan (solo cambia el objeto de la mano).
  11. Tachar, cruzar o señalar con un trazo la silla vacía (sería juicio sobre la persona).
- **Márgenes seguros:** zona segura de `formatos.md` (x 100–980, y 250–1670); portada: zona útil x 60–960, y 380–1440.
- **Texto exacto:** todo texto en pantalla es el de las tablas de abajo, letra por letra. Los contadores muestran enteros entre su valor de inicio y su valor final.
- **No afirmar:** nada fuera de la tabla del brief y de las fechas verificadas hoy:
  - **12 de noviembre de 2026** (renuncia), **17** (la junta dijo que no pensaba reponerlo), **23** (reposición como presidente y director ejecutivo, con efecto inmediato): Wikipedia en inglés, «Jensen Huang», leída el 2026-11-24, y títulos de cadenas; **el comunicado de Nvidia no se pudo abrir**.
  - **11 días, 6 días, 12.274 días (más de 33 años desde el 5 de abril de 1993)**, **5 días** (Altman, 2023-11-17 a 2023-11-22), **4.382 días** (Jobs, 1985-09-17 a 1997-09-16; ≈ 12 años): cálculo con `datetime`, 2026-11-24.
  - **No decir ni mostrar:** el motivo de la renuncia más allá de «after a scandal» (una sola vez, en la voz de la línea 2 y en la descripción), detalles de la vida privada, nombres de terceros, investigaciones o comparecencias, el papel del gobierno o de ningún político en la reposición, el motivo de la junta para cambiar de postura, cifras de bolsa, fortuna o precio de acciones, citas de Huang, que Huang «fue despedido» (renunció), que haya sido «el regreso más corto» o «el más rápido» (Altman volvió en 5 días), superlativos, que Altman renunció (fue destituido; no se dice cómo salió), quién lidera Nvidia hoy más allá de lo dicho, predicciones sobre su permanencia. Del fabricante solo se dice el nombre.

**Rótulos en inglés (los que van en pantalla):**

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| Back In / 11 Days? (clave: 11; entero en el fotograma 0, sin pop; es la portada) | 0,0 | 0,9 | 10, 26 | 12 |
| 11 days? (clave: 11) | 1,1 | 2,4 | 10, 14 | 7 |
| Nov 12 (clave: 12) | 4,2 | 6,4 | 10, 14 | 7 |
| Nov 17 (clave: 17) | 7,0 | 9,9 | 10, 14 | 7 |
| +6 days (clave: 6) | 10,2 | 11,7 | 10, 14 | 7 |
| Nov 23 (clave: 23) | 11,8 | 12,95 | 10, 14 | 7 |
| 11 days (clave: 11) | 13,05 | 13,95 | 10, 14 | 7 |
| 12,274 days (clave: el número) | 14,3 | 15,95 | 10, 14 | 7 |
| 5 days (clave: 5) | 17,4 | 19,4 | 10, 14 | 7 |
| 4,382 days (contador de 0 a 4,382; en tinta mientras sube y en tomate al llegar; sigue en la toma 11) | 21,85 | 24,4 | 10, 15 | 7 |
| 11 days (clave: 11) | 24,6 | 26,4 | 10, 14 | 7 |
| Who else? (clave: else) | 26,85 | 28,1 | 10, 14 | 7 |
| Subscribe (clave) | 28,2 | 28,95 | 10, 14 | 7 |
| Back In / 11 Days? (entra con pop; sigue sin corte en la toma 1) | 30,0 | 30,5 | 10, 26 | 12 |

**Subtítulos en español (quemados en el video; encargo del dueño, 2026-11-24).** La voz sigue en inglés; en pantalla va la traducción al español de cada línea, sincronizada con ella.

- **Dónde va la banda:** fija, de **y = 905 a y = 1085** (47,1 % a 56,5 % del alto) y de x = 100 a x = 980: **entre la zona de gráficos** (que termina en y = 893) **y la cabeza de los personajes** (que empieza en y = 1094, con `alto` de 29 %). Por eso los personajes son más pequeños que en el short 2 (29 % y no 34 %). No tapa personajes ni objetos y no choca con los rótulos en inglés (arriba, y 253–461) ni con las cifras. La parte de abajo (y > 1500) queda libre porque la interfaz de los Shorts (título, canal y botones) la cubre.
- **Formato:** Inter Display Medium a **4,5 % del alto (86 px)**; tinta `#2B2420` sobre un **panel de papel `#F3E9D2` translúcido** (opacidad 0,82, esquinas de 20 px, relleno de 12 px); contraste tinta/papel 12,6:1 (mínimo pedido 7:1). **Máximo 2 líneas y ≈ 21 caracteres por línea** (≤ 856 px medidos con la fuente): con 86 px no caben 32 caracteres en 880 px, por eso las tarjetas son cortas y no literales. Entrada de 3 fotogramas (fundido de la opacidad), sin `pop`; cada tarjeta dura 30 fotogramas o más.
- **Cómo conviven con los rótulos en inglés:** los rótulos de cifra y palabra clave siguen en inglés y en grande; **el subtítulo no repite la cifra ni la fecha si ya están en grande** (por eso omite «11 días», «el 12», «el 17», «5 días» y «4.382»). La portada (0,0–1,0 s y 29,6–30,5 s) **no lleva subtítulo**: la banda taparía la silla y la regla de portada pide el cuadro limpio; la línea 1 se subtitula desde 1,0 s. En la toma 10, de 21,4 a 23,5 s no hay subtítulo: la cifra ya está en grande.
- **Decisiones de redacción:** español neutro, natural y no literal; «CEO» (no «director ejecutivo»: es la forma de los titulares y cabe); «Nvidia», «Jensen Huang», «Sam Altman», «Steve Jobs», «OpenAI» y «Apple» como en inglés; cifras con formato español (12.274, 4.382; en los rótulos en inglés, 12,274 y 4,382).

| Tarjeta | Empieza (s) | Termina (s) | Línea de voz | Texto en español (una línea por renglón) |
|---|---|---|---|---|
| 1 | 1,00 | 2,40 | 1 | ¿Fue rápido el regreso / de Jensen Huang? |
| 2 | 2,55 | 6,40 | 2 | Renunció a Nvidia / tras un escándalo. |
| 3 | 6,70 | 9,70 | 3 | La junta dijo que no / lo repondría. |
| 4 | 10,00 | 13,00 | 4 | Lo repuso como CEO. |
| 5 | 13,25 | 15,80 | 5 | Antes: más de 33 / años al mando. |
| 6 | 16,00 | 16,95 | 6 | ¿Rápido comparado / con quién? |
| 7 | 17,20 | 19,40 | 7 | Sam Altman, OpenAI: |
| 8 | 19,55 | 21,40 | 8 | Steve Jobs, Apple: |
| 9 | 23,50 | 24,45 | 9 | ¿Son 12 años? |
| 10 | 24,70 | 26,50 | 10 | Más rápido que Jobs. / Más lento que Altman. |
| 11 | 26,80 | 27,90 | 11 | ¿Quién más volvió? |
| 12 | 28,00 | 29,10 | 11 | Suscríbete al próximo / conteo. |

### Color con intención

Propuesta del prompt (`manual/13_color_con_intencion.md`); la sección equivalente de `02_prompt/direccion.md` la escribe el director de fotografía y, si difiere, manda la dirección (hoy `direccion.md` está en plantilla).

- **Neutros (2):** papel `#F3E9D2` (fondo de todos los planos; cuerpo del calendario en `#FFF8EC`; suelo `#E6D8B8`) y tinta `#2B2420` (líneas, contornos y todo texto que no sea clave). Contraste tinta/papel 12,6:1; tinta/blanco 14,5:1.
- **Acento (1):** mostaza `#E8B33B`, con contorno de tinta, solo en la palabra clave y en **un** elemento por plano (el lápiz, el círculo, la marca o la barra, según la toma). **No va** en el texto que no es clave, en la silla, en el calendario (salvo el círculo), en las barras (salvo la marca de 11 días y la de Altman en la toma 9). **Tomate `#C8553D` queda reservado al pico** (tomas 10 y 11) y ahí no hay mostaza como acento: por eso Tin no lleva el lápiz en esas dos tomas. Marrón `#7A4B2A` solo como relleno.
- **Por qué esta paleta:** la misma de los shorts 1 y 2, para que el canal se reconozca (R26 inv.); papel y tinta dan contraste alto y lectura fácil (R27 inv.); el acento único se recuerda (R33 inv.) y el cambio a tomate marca el golpe del dato. Para una noticia, la saturación baja evita sensación de alarma o de burla; el significado emocional del color es **hipótesis** (Elliot y Maier, 2014, manual 13).
- **Cómo ayuda al objetivo:** Programa de socios → reconocimiento del canal y un pico visible en la cifra → retención de los segundos 1 a 3 y pico en 23,05 s; regreso de espectadores.
- **Riesgos de lectura:** (1) mostaza sobre papel da 1,6:1: se lee por el contorno de tinta; (2) tinta sobre tomate 3,5:1: la cifra se lee por contorno y tamaño; (3) la bufanda mostaza de Tan es identidad y no debe leerse como segundo acento en las tomas 10 y 11; (4) rojo y verde azulado: la información no depende del tono; (5) el desenfoque y la niebla bajan el porcentaje en paleta (≈ 82–85 % esperado, la prueba midió 82 %): se mide también sobre un fotograma nítido (el 0).
- **Medido:** pendiente (falta el render); lo mide el supervisor con `revisar_color.py`.

Tabla de acento por plano:

| Toma | Mostaza (palabra clave + un elemento) | Tomate |
|---|---|---|
| 1 | «11» + lápiz | no |
| 2 | «11» | no |
| 3 | «12» + círculo del 12 | no |
| 4 | «17» | no |
| 5 | «6» y luego «23» + círculo del 23 | no |
| 6 | «11» | no |
| 7 | número «12,274» + marca de 11 días | no |
| 8 | ninguno | no |
| 9 | «5» + barra de Altman | no |
| 10 | ninguno | cifra «4,382» |
| 11 | ninguno | cifra «4,382» |
| 12 | «11» + marca de Huang | no |
| 13 | «else» y luego «Subscribe» + lápiz | no |
| 14 | «11» + lápiz | no |

Campo para `ficha.json`:

```json
"color": {"neutros": [
            "#F3E9D2",
            "#2B2420"
          ], "acento": "#E8B33B",
          "por_que": "papel y tinta como neutros del canal; mostaza como acento único (clave y un elemento por plano); tomate solo en el pico (la cifra de Jobs) para marcar el golpe; la misma paleta que los shorts 1 y 2 para reconocer el canal",
          "objetivo": "Programa de socios: reconocimiento del canal y un pico visible; métrica: retención de los segundos 1 a 3 y pico de retención en 23,05 s",
          "medido": "pendiente: falta el render"}
```

En un short, todo texto queda dentro de la zona segura. Entrada de cada rótulo: `pop` con escala de 0,85 a 1 en 8 fotogramas; salida: subir 2 % con ease-in en 3 fotogramas (excepción: el rótulo de portada en el fotograma 0 y en el último ya están a escala 1).

## 13. Sonido

Los golpes bajo la voz van a unos **−26 LUFS** (−12 dB respecto a la voz, a −14 LUFS; lección del short 1: a −38 LUFS no se oían). Se comprueba al oído. Cada corte y cada efecto lleva su golpe a ±1 fotograma (manual 14, 2.8).

| Golpe o efecto | Segundo | A qué corte o efecto va atado | Origen y licencia |
|---|---|---|---|
| Whoosh con vibrato (vuelo del lápiz que se frena) | 0,0–0,5 | firma: llegada del lápiz (toma 1) | código, propio |
| Golpe seco al atrapar (thwack, 80 ms) | 0,5 | Tin atrapa el lápiz (f 15) | código, propio |
| Golpe de la clave «11» | 0,2 | `palabra_clave` de la portada (f 6) | código, propio |
| Clic suave | 1,0 | corte en el movimiento, toma 1 a 2 | código, propio |
| Clic suave | 2,5 | corte, toma 2 a 3 | código, propio |
| Raspado de lápiz | 4,3–4,7 | círculo del 12 | código, propio |
| Clic y golpe suave de revelado | 6,5 | corte con revelado, toma 3 a 4 | código, propio |
| Clic suave | 10,0 | corte, toma 4 a 5 | código, propio |
| Raspado de lápiz | 10,3–10,8 y 11,3–11,7 | flecha y círculo del 23 | código, propio |
| Tictac de cruces, 11 veces, subiendo de tono | 11,9–13,0 | cruces del 13 al 23 | código, propio |
| Clic suave | 13,0 | corte, toma 5 a 6 | código, propio |
| Clic suave | 14,0 | corte, toma 6 a 7 | código, propio |
| Deslizar de la barra (tono que sube y frena) | 14,1–15,1 | barra de tenencia | código, propio |
| Clic suave | 16,0 | corte, toma 7 a 8 | código, propio |
| Clic suave | 17,0 | corte, toma 8 a 9 | código, propio |
| Pop de la barra de Altman | 17,5 | barra de Altman | código, propio |
| Clic suave | 19,5 | corte, toma 9 a 10 | código, propio |
| Subida (riser) de 25 fotogramas | 20,5–21,3 | antes del pico | código, propio |
| **Silencio de efectos y música de 12 fotogramas** | 21,1–21,5 | antes del número (cae en la pausa de la voz tras «Apple:») | código, propio |
| Tictac de contador que sube de tono | 21,85–23,05 | contador de 4.382 (calla al llegar) | código, propio |
| Ding grave + acorde de mi mayor abierto + golpe del zoom | 23,05 | llegada de la cifra, paso a tomate y `pop` (mismo fotograma) | código, propio |
| Clic suave | 23,5 | corte, toma 10 a 11 | código, propio |
| Clic suave | 24,5 | corte, toma 11 a 12 (respiro) | código, propio |
| Clic suave | 26,5 | corte, toma 12 a 13 | código, propio |
| Whoosh corto del pase del lápiz | 28,4–28,67 | lápiz de Tin a Tan | código, propio |
| Crujido de anticipación (6 f) | 29,63–29,83 | anticipación del lanzamiento | código, propio |
| **Whoosh con vibrato que se acelera** | 29,83–30,5 | lanzamiento: último movimiento; es el mismo vuelo que abre el bucle (empalme con el 0,0) | código, propio |

- **Música:** mi menor a 120 BPM (sección 7), −24 LUFS; sin material de terceros. **Voz:** sí (por generar); empieza en el fotograma 0 sin retraso.
- Los pasos de música y efectos entre cortes no pueden tener más de 2 golpes fuertes por segundo.

## 14. Motor y revisión

- **Cómo se hace:** gráficos por código (fotograma a fotograma): Python, Pillow, numpy y ffmpeg. Cada plano con capas se compone con `efectos.componer` (`Capa`, `Camara`) desde `LienzoCapa` con supermuestreo; los personajes con `palitos.dibujar(lz, id, x, suelo, alto, pose, expresion, vista, mira, viento, objeto, espejo)`. Todo depende del número de fotograma. Se guardan PNG numerados y ffmpeg los une con la voz, los efectos y la música (`postpro.py mezclar` o ffmpeg directo). `codigo/render.py` de este proyecto es del prompt anterior (tarjeta de 1999) y **hay que reescribirlo**.
- **Qué hay que dibujar (todo nuevo, genérico y sin marca):**
  1. `silla_director` (sección 5), a escala variable, también pequeña y lejana.
  2. `calendario_noviembre` con sus marcas: círculo, flecha y 11 cruces.
  3. `mesa_junta` con cinco sillas genéricas y la silla de director.
  4. `barras` (tenencia y comparación) con la marca mínima de 4 px.
  5. **`lapiz_libre(lz, x, y, ang, esc, estela)`: el lápiz de Tin girando con estela plana de dos copias**, con la trayectoria de llegada, el pase y el lanzamiento; el lápiz que lleva Tin en la mano sigue siendo `objeto="lapiz"` de `palitos.py` (aquí `objeto="lapiz"` también para Tan en las tomas 13 y 14, aprobado en su ficha). Costo: 0.
  6. Banda de subtítulos en español: panel translúcido y texto con medida previa (`ancho_texto`) para que ninguna línea pase de 856 px.
  7. Comprobar los glifos «¿», «?», «,», «.», «:», «+», «&» y, si se usa, «≈» en la fuente antes de renderizar.
- **Quién renderiza y autorización:** el equipo de producción renderiza (0 créditos); **la voz necesita la cotización y el sí del dueño**; publicar también. Antes de renderizar se revisa `03_keyframes/definicion.md` y se anotan fuente y licencia de cada recurso en `licencias.md`.
- **Controles (todo gratis, en `07_revision/`):**
  - **Texto:** `revisar_texto.py` con 0 errores. Corrido el 2026-11-24 sobre `subtitulos.srt`, la descripción y las etiquetas (`--idioma en`) y sobre `subtitulos_es.srt` (`--idioma es`): resultado en el informe final. Los textos de pantalla del código se pasan antes de renderizar.
  - **Destellos:** `efectos.comprobar_destellos` con margen (máximo 2 por segundo) y `postpro.py destellos`; mirada fotograma a fotograma a la llegada de la cifra (zoom y tomate) y al lanzamiento del lápiz.
  - **Fotogramas:** `revisar_fotogramas.py` y `analizar_video.py --cada 0.5`; hojas de contacto miradas una por una.
  - **Medidas:** zona segura en los 915 fotogramas; portada (texto y 492–682, silla y 754–1066, caras dentro de x 60–960 e y 380–1440); la banda de subtítulos (y 905–1085) sin tocar gráficos ni cabezas; cada línea de subtítulo ≤ 856 px; pies a 86 %; `alto` 29 %.
  - **Bucle:** el fotograma 915 (el que sigue al último) igual al 0 (diferencia media menor de 3 de 255); el lápiz sale en la toma 14 y entra en la toma 1.
  - **Color:** `revisar_color.py` (paleta, contraste, saltos); se espera ≈ 82–85 % en paleta con profundidad, y se mide también el fotograma 0.
  - **Cifras:** recalcular con `datetime` (11, 6, 12.274, 5, 4.382) y comparar pantalla, subtítulos, guion y descripción; los contadores solo suben.
  - **Oído:** que cada corte caiga donde dice la sección 6 con la voz real, que «Nvidia», «Huang», «C E O» y «OpenAI» suenen bien, que la pausa tras «Apple:» sea de ≈ 0,45 s y que el golpe del lápiz se oiga bajo la voz.
- **Qué se marca:** imagen congelada, fotograma vacío, texto cortado o tapado, texto que sigue sobre el plano siguiente, elemento fuera de cuadro, tirones, contador que retrocede, glifos cuadrados, el fotograma 915 distinto del 0, más de 2 destellos por segundo, cualquier cosa que recuerde a Nvidia (verde, ojo, logotipo), cualquier rostro o silueta que se lea como una persona real, la silla que parezca tachada o señalada, una expresión de Tan o de Tin que se lea como burla o enojo, y en el teléfono: que silla, calendario, barras, cifras y subtítulos se lean. Nota para el validador: en las tomas con personajes el bloque de identidad de la ficha no se pega en el prompt porque no hay generador de imágenes; el diseño oficial es el código de `palitos.py` y se comprueba con la lista de comprobación de cada ficha.
- **Vueltas:** las correcciones por código son gratis; **las de generador no se repiten sin autorización del dueño** (`generacion.md`). Aquí solo hay generador en la voz: una generación por voz, sin segundos intentos.
