# Prompt de video para redes — Jensen Huang Is Back: GeForce 256 vs RTX 5090

> **ESTADO (2026-11-24):** la voz **no está generada** (necesita el sí del dueño con la cotización), así que **todos los tiempos son estimados** (sílabas a ritmo del short 2 al 110 %, sección 7) y se reajustan a la voz real; el video **no está renderizado**. No se ha generado nada, no se ha gastado ningún crédito. Es el **primer video del canal con profundidad y efectos** (`manual/14_efectos_y_emocion.md`, sección 7; técnica probada en `2026-11-23_prueba_efectos_tin_y_tan`). Hereda del short 2 el formato, la portada dentro del video, las cifras con dígitos abiertos (`ss01`), la rejilla de 0,5 s y la mezcla (golpes bajo la voz a unos −26 LUFS). La dirección del equipo (`02_prompt/direccion.md`) sigue con la plantilla vacía: las decisiones de abajo salen del brief, del manual 14 y de la prueba de efectos; si el equipo llena la dirección y difiere, manda la dirección.

<!--
Pieza dibujada con código (sin generador de video). Todas las tomas son método «edición»: se resuelven gratis
en el montaje. En lugar de «Prompt de keyframe» y «Prompt de video» cada toma lleva una «Especificación de dibujo».
Los tiempos son del video final y de la voz ESTIMADA (sección 7); se reajustan con la voz real.
Un solo plano continuo puede dividirse en dos tomas encadenadas (sin corte): 3 y 4, 9 y 10, 11 y 12.
-->

## 1. Ficha técnica

- **Proyecto:** 2026-11-24_tin_y_tan_jensen_huang
- **Tipo:** short
- **Número:** 3
- **Serie:** ninguna
- **Objetivo de aprendizaje:** no aplica
- **Generador:** ninguno: imagen dibujada con código (palitos.py + efectos.py + gráficos propios), armada con ffmpeg
- **Aspecto:** 9:16
- **Duración total:** 30,5 s estimados (la voz estimada va de 0,00 a 28,80 s, sin gancho mudo; cierre de 1,7 s sin voz, de 28,8 a 30,5 s; múltiplo de 0,5 s)
- **Resolución de borrador:** 540x960 a 30 fps, prueba de 5 s con un fotograma por pulso (render propio)
- **Resolución final:** 1080x1920 a 30 fps, 915 fotogramas
- **Precio por segundo:** 0 (render propio; no hay servicio de pago)
- **Intentos estimados por toma:** 1
- **Versión:** 1 (voz sin generar; tiempos estimados; render pendiente)

## 2. Elenco

| Personaje | Papel en este video | Vestuario | Referencia que se sube |
|---|---|---|---|
| @tan | Abre con la pregunta nostálgica y hace las dos preguntas de la cuenta; se asombra ante el tamaño; **dice la única invitación a suscribirse**. Lado izquierdo del cuadro con `espejo=True` (en el centro cuando está sola). | base de su ficha (rodete y bufanda mostaza); sin objeto de mano | personajes/tan/referencias/principal_tin_y_tan.png |
| @tin | Cuenta qué es la tarjeta, da la noticia del regreso, aclara que se cuentan transistores y hace la división. Lado derecho del cuadro, sin espejo; su lápiz en las tomas 3, 4 y 5 (el motivo del canal, que no salió en el short 2). | base de su ficha (gorra marrón, lentes, lápiz) | personajes/tin/referencias/principal_tin_y_tan.png |

No se sube nada a un generador: las referencias son las del diseño en código (`herramientas/palitos.py`, versión 1.3) y se usan solo para comparar. **Jensen Huang no aparece dibujado ni imitado: solo se le nombra** (brief). No salen más personajes.

Poses y expresiones usadas (todas existen en `POSES` y `EXPRESIONES` de `palitos.py`, comprobado el 2026-11-24 en `video-studio/personajes/*/ficha.md`): poses `parado`, `saluda`, `senala`, `pregunta`, `explica`, `encoge`, `celebra`; expresiones `feliz`, `nostalgia`, `curiosidad`, `sorpresa`, `risa`, `eureka`. **No se usan `pensando` ni `concentrado`** (se leen como enojo: lección de la revisión del short 2). No se inventa ningún rasgo.

## 3. Idea en una línea

Tan pregunta «¿te acuerdas de poner una de estas en tu PC?» y una tarjeta gráfica de 1999 crece hacia la cámara; Tin dice qué es, que el 23 de noviembre la junta de Nvidia repuso a Jensen Huang como director ejecutivo, y hace una división entre dos objetos: los transistores de la RTX 5090 entre los de aquella tarjeta, **más de 4.000**; el remate es de tamaño (un muro de 4.000 tarjetitas que equivale a un solo chip) y Tan pide una vez, con calidez, que se suscriban. Nostalgia que se vuelve asombro por el tamaño; el que la vivió lo manda a quien armó una PC con él.

**Decidido por el equipo el 2026-11-24** (razones en `00_brief.md` y aquí; el dueño ordenó que el equipo decida todo con su investigación):

1. **Ángulo y cuenta:** «cuántas tarjetas de 1999 caben, en transistores, en una de hoy». Es una división entre dos objetos y el remate es de tamaño: distinto del short 1 (distancia a minutos, remate de tiempo) y del short 2 (días entre dos fechas, remate de edad). Variación obligatoria según `plan_programa_de_socios.md`, 4.3 y P11.
2. **Se dice «más de 4.000» y se usa el número más cauteloso de 1999.** Las fuentes dan 17 o 23 millones de transistores para la GeForce 256. El video dice «hasta 23 millones» (el mayor) y la división da ≈ 4.009: «más de 4.000» es cierto con las dos cifras (con 17 millones daría ≈ 5.424). La descripción lo explica.
3. **Se dice «la RTX 5090», no «el chip de hoy».** Nvidia fabrica chips de centros de datos con más transistores; «de hoy» sería ambiguo. Los 92.200 millones son los de la RTX 5090 (GB202, a la venta desde el 30 de enero de 2025). Por eso el título compara con la «RTX 5090» y no con «Today's GPU».
4. **El vínculo entre la tarjeta y el regreso es la empresa, no la persona.** La tabla de datos del brief no incluye que él dirigiera Nvidia en 1999, y el brief prohíbe afirmar que diseñó la tarjeta. El video dice «Nvidia lanzó la tarjeta en 1999» (implícito: «es la GeForce 256, de 1999») y, aparte, «la junta de Nvidia repuso a Jensen Huang como director ejecutivo». Dos hechos con fuente, uno al lado del otro. Si el comercial quiere «su» tarjeta, primero hay que añadir al brief la fuente de que era CEO en 1999.
5. **Sin motivo, sin juicio, sin «11 días» y sin la palabra que el brief prohíbe para calificar la polémica** (en ningún archivo del proyecto salvo el brief): solo el hecho y su fecha («Nov 23» en pantalla). La voz no dice la fecha para que el video no caduque; la pantalla sí.
6. **Una sola invitación a suscribirse, de Tan, antes del último fotograma** (`plan_programa_de_socios.md`, P6c: palanca del objetivo; YouTube lo permite: support.google.com/youtube/answer/3399767, leída el 2026-11-23). Corta y cálida; sin promesas ni recompensas (prohibido pedirla a cambio de otra). Es la única diferencia de contenido de cierre frente a los shorts 1 y 2.
7. **Un solo cambio «grande» en el primer segundo respecto del short 2: la tarjeta crece hacia la cámara** (efecto 1 de la sección 7 del manual 14, 12 fotogramas). En el short 2 el mando solo retumbaba a escala fija. Lo demás del primer segundo se mantiene igual para poder atribuir el dato: mismo corte en 1,0 s, mismas caras de perfil mirando el objeto, mismo texto de dos palabras de peso. El golpe de la palabra clave dura 12 fotogramas y no cambia lo que se ve en el fotograma 0. Ver «Profundidad y efectos» en la sección 11.
8. **Objetivo comercial:** entrar al Programa de socios lo antes posible (dueño, 2026-11-23). Métricas de este video: se quedó a mirar frente a deslizó (el short 1 dio 20,7 %), retención por segundo, compartidos y suscriptores por cada mil vistas.

Verificación de la cuenta (2026-11-24, con Python): 92.200.000.000 / 23.000.000 = 4.008,7; 92.200.000.000 / 17.000.000 = 5.423,5; 2025 − 1999 = 26 años (no se dice en el video).

## 4. Estilo global

```text
Flat 2D vector drawing on warm cream paper (#F3E9D2), 1970s palette: two neutrals (cream paper, dark ink) plus ONE accent per shot (mustard in every shot except the reveal shots, tomato red only in the reveal shots), character colors (orange, brown, teal) are identity and not accents, thick dark ink outlines (#2B2420), hand-made stick-figure look, 2 to 4 flat layers at different depths with slow parallax, out-of-focus layers softly blurred and faded toward the paper color, thin contact shadows under objects, no gradient fills, no glow, no lens flare, crisp anti-aliased lines (supersampled), spring-based motion with ease-out stops, small camera pushes.
```

**Negativo global:**

```text
text inside the drawing other than the table in section 12, brand logos, Nvidia logo or lettering or its green, any green accent, GeForce or RTX lettering or logo style, Jensen Huang drawn or imitated, a real person's face, gradient fills, drop shadows on the stick figures, glow, lens flare, neon, blue and orange cinematic grade, two accent colors in the same shot, tomato red outside the reveal shots, mustard in the reveal shots other than the characters' own scarf, strobe or flashing, negative color flash over text, glass-panel app look, bouncing karaoke subtitles, extra characters, extra fingers, characters other than Tin and Tan, uppercase centered titles, square placeholder glyphs, symbols that are not in the font
```

## 5. Escenarios

- **papel_crema:** fondo plano `#F3E9D2` con la viñeta y el grano fijo de `efectos.papel()` (el grano no cambia entre fotogramas). Cuando hay personajes, línea de suelo `#E6D8B8` de 4 px a **86 % del alto (y = 1651 px)**, de 9,3 % a 90,7 % del ancho.
- **Lienzo y zonas (1080x1920):** zona segura de `formatos.md`: x de 100 a 980 px, y de 250 a 1670 px. Zona de texto fija: arriba a la izquierda, alineado a la izquierda en x = 10 % (108 px), de y = 13,2 % a 24 %. **Zona de gráficos de 27 % a 51 %** (518 a 979 px; 460 px de alto, x de 100 a 980). Personajes: pies a 86 %, `alto` = 34 % (653 px), cabeza más alta a 52 %; plano medio de uno solo: `alto` 44 % (845 px). Los personajes nunca pisan la zona de texto ni la de gráficos.
- **Lados:** Tan en x = 30 % con `espejo=True`; Tin en x = 70 % sin espejo; cada uno gesticula hacia afuera. En las tomas 3 a 5 se abren a x = 22 % y 78 % para dejar sitio al pedestal. Solos, en x = 50 %.
- **Profundidad (`efectos.py` 1.0):** `z` = 0 es el plano de los personajes; positivo, más lejos; negativo, más cerca. Distancia focal 1000: una capa a `z` se ve a escala 1000 / (1000 + z). Cada capa se dibuja como se ve con la cámara quieta. Valores de trabajo de la prueba: `apertura` 0,018, `campo` 150, `niebla` 0,30, `desenfoque_max` 60. **En las tomas 1 y 14 (la portada) la apertura es 0: todo nítido.**
- **tarjeta_1999 (gráfico propio, ancho W; es el objeto del video):** tarjeta gráfica **genérica** de la época, vista desde el lado de los componentes, sin logotipos, sin letras y sin ningún verde. Alto de la placa 0,42 W. Placa: rectángulo redondeado (radio 0,02 W), relleno marrón `#7A4B2A`, contorno tinta de 0,012 W. **Escuadra metálica** en el extremo izquierdo: rectángulo de 0,05 W × 0,42 W, relleno `#E6D8B8`, contorno tinta, dos orificios (círculos tinta de radio 0,008 W). **Ventilador:** círculo de radio 0,15 W centrado en (0,36 W; 0,21 W) desde la esquina superior izquierda de la placa, relleno `#E6D8B8`, contorno tinta; 5 aspas curvas en tinta y buje central de radio 0,03 W en papel; gira a 90 grados por segundo (acción secundaria; con ease no, es mecánico y lineal, como el segundero). **Memorias:** 4 rectángulos tinta de 0,07 W × 0,05 W en dos filas a la derecha (x de 0,62 W a 0,95 W). **Dedos del conector:** franja bajo el borde inferior, de 0,62 W × 0,05 W, desde x = 0,12 W, con 14 marcas tinta verticales de 0,004 W; **relleno mostaza `#E8B33B` cuando la tarjeta es el elemento de acento del plano, y marrón `#7A4B2A` en los planos de la revelación y cuando otro elemento lleva el acento**. Altura total del objeto con los dedos: 0,47 W. Mide lo que mide una tarjeta genérica de dibujo: no se afirma ninguna medida real.
- **tarjeta_actual (gráfico propio, ancho W; es «la nueva», la RTX 5090):** tarjeta **genérica** moderna, sin logotipos, sin letras, sin luces de color y sin verde. Alto 0,34 W. Carcasa: rectángulo redondeado (radio 0,03 W) en tinta `#2B2420` con contorno tinta de 0,012 W. **Tres ventiladores:** círculos de radio 0,15 W en x = 0,2 W; 0,5 W y 0,8 W, y = 0,17 W; relleno `#E6D8B8`, 7 aspas finas en tinta y buje marrón `#7A4B2A`. Escuadra izquierda como la de la tarjeta_1999. Dedos del conector como en la tarjeta_1999 (0,04 W de alto; mostaza o marrón con la misma regla). Se reconoce por tamaño y por los tres ventiladores contra uno; el dibujo no copia ninguna tarjeta comercial.
- **pedestal (toma 3 a 5):** columna de museo, 150 px de ancho, de la base de la tarjeta al suelo (y = 1651), relleno `#E6D8B8`, contorno tinta; placa superior de 220 × 26 px. Sombra de contacto en el suelo. La tarjeta_1999 (W = 420 px, alto con dedos 197 px) está de pie sobre la placa, con los dedos metidos en una ranura de la placa (no se ven), centrada en (50 %; 39 %) de modo que su parte alta cae en y = 700 px.
- **pc_beige (fondo, tomas 3 a 5):** siluetas de una torre y de un monitor de tubo, relleno `#E6D8B8` y contorno tinta de 0,008 de su ancho, sin botones con símbolos ni letras (dos bahías de unidad como rectángulos tinta). Torre de 300 × 560 px a la izquierda y monitor de 360 × 330 px a la derecha, en la capa z = +420 (se ven más chicos y se funden con el papel por la niebla).
- **placa_base y ranura (toma 2):** vista de cerca de una placa base: rectángulo `#E6D8B8` con contorno tinta que ocupa de x = 100 a 980 px y de y = 1100 a 1500 px; ranura = rectángulo redondeado tinta de 560 × 44 px con dos muescas; tres chips cuadrados tinta de 70 px y dos condensadores (círculos marrón con contorno tinta de 34 px). Sin letras.
- **manos_de_palitos (toma 2):** dos brazos de tinta de 36 px de grosor (el trazo de cuerpo de los personajes, ampliado) que entran por abajo, terminan en manos de punto de radio 34 px y sostienen la tarjeta por la escuadra y por el borde superior. Son las del espectador (subjetivo): no se reconocen como Tin ni como Tan y no llevan color.
- **die (toma 6):** el chip visto de cerca: cuadrado de 400 × 400 px, relleno mostaza `#E8B33B`, contorno tinta de 10 px; dentro, una cuadrícula de 12 × 12 puntos tinta de 12 px de radio (144 puntos, que representan «interruptores diminutos»; no se dice que sean 144 de nada).
- **pared_de_tarjetas (toma 11 y 12):** cuadrícula de **80 columnas × 50 filas = 4.000 minitarjetas** que llena la zona de gráficos (880 × 460 px; celda de 11 × 9,2 px). Cada minitarjeta es un rectángulo marrón `#7A4B2A` de 9 × 7,4 px con una separación de papel de 2 px y un punto `#E6D8B8` de 3 px (su ventilador). Sin mostaza. Cuatro mil, exactos: el rótulo dice «más de 4.000», así que el dibujo no exagera.
- **ecuación (tomas 9 y 10):** dos filas en la zona de gráficos. Fila 1 (centro en y = 600 px): tarjeta_actual de W = 260 px a la izquierda (x 100 a 360) y el texto «≈ 92 billion» a su derecha. Fila 2 (centro en y = 770 px): el signo «÷» (106 px) en x = 100 a 170, la tarjeta_1999 de W = 180 px (x 190 a 370) y el texto «23 million» a su derecha. Las dos tarjetas pequeñas llevan los dedos en marrón (planos de revelación).
- **Muelles (masa 1, rigidez, amortiguación), declarados por elemento:** `pop` 220 y 20 (entrada de textos y gráficos, escala de 0,85 a 1); `slide` 120 y 16 (personajes y gráficos que se desplazan); `sello` 320 y 26 (empujes de cámara y golpe de zoom). Contadores: ease-out cúbico sin muelle, para que el valor nunca pase de su final ni retroceda. Todo depende del número de fotograma (30 fps).
- **portada (tomas 1 y 14):** el primer segundo **es la portada** (`ENTREGA_YOUTUBE.md`, «Portada de los Shorts»). En el fotograma 0: la tarjeta_1999 de W = 600 px (apariencia) centrada en x = 540 y en y = 910, con los dedos mostaza (su elemento de acento); el alto del objeto con los dedos es 282 px (y 769 a 1051), dentro de la franja 720 a 1100. Sobre ella, el texto del gancho (fila 1 de la sección 12) entre y = 415 y y = 690. Debajo, Tan (x = 24 %) y Tin (x = 76 %) de cuerpo entero, **de perfil y con la cabeza inclinada 25 grados hacia arriba (`cabeza_giro=25`), mirando la tarjeta**, `alto` 487 px, pies a 86 %: las caras quedan, como en el short 2, en x 121 a 303 y x 752 a 955, y 1163 a 1364, dentro de la zona útil de portada (x 60 a 960, y 380 a 1440). La tarjeta crece hasta W = 760 px en 12 fotogramas y a partir de ahí sigue siendo del mismo tamaño hasta que baja hacia el corte (altura con dedos 357 px: y 731 a 1089, dentro de la franja).
- **Transiciones:** `corte seco`; **`corte en el movimiento`** (toma 1 a 2: el corte cae 4 fotogramas después de que arranca el descenso de la tarjeta); `borrón` (corte seco con desenfoque de movimiento horizontal de 18 px en los 2 últimos fotogramas de la toma que sale y en los 2 primeros de la que entra; cero destellos); **`barrido_obturador`** una sola vez, de 6 fotogramas (toma 7 a 8); **`congelado_con_marco`** una sola vez, en el cierre (toma 13 a 14).

## 6. Tomas

<!--
Todas las tomas son «edición»: dibujo por código. Tiempos al décimo de segundo, del video final (30,5 s).
Cada corte cae en un pulso de 0,5 s. Voz: líneas de la sección 7, con tiempos ESTIMADOS.
Cada corte cae en el pulso anterior al inicio de la línea que le toca (de 0,00 a 0,25 s antes).
-->

### Toma 1 — Gancho: la tarjeta de 1999 viene hacia ti

- **Duración:** 1,0 s (de 0,0 a 1,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** la portada: texto del gancho arriba (y 415 a 690), la tarjeta_1999 en el centro (y 731 a 1089) y Tan y Tin debajo, de perfil, mirándola
- **Cámara:** fija; todo nítido (apertura 0). El acercamiento es de la capa de la tarjeta, no de la cámara, para que los personajes y el texto no cambien de lugar
- **Acción:** la tarjeta ya viene hacia la cámara en el fotograma 0 (su ventilador ya gira); en 12 fotogramas pasa de 600 a 760 px de ancho con frenada; en el fotograma 6 la palabra clave da su golpe; desde el fotograma 26 la tarjeta empieza a bajar 30 px (anticipa la inserción de la toma 2).
- **Audio:** línea 1, Tan (primera parte): "Remember putting one of these in your P C?" Aquí suena «Remember putting one of these…» (el corte de 1,0 cae dentro de la línea, hacia «one of these»; sin escucha no se sabe en qué sílaba). Golpe 1 y golpe de palabra de la sección 13.
- **Referencia:** toma 1 del short 2 (objeto en movimiento desde el fotograma 0, portada con caras); efecto 1 de `manual/14`, sección 7.1
- **Transición de entrada:** ninguna (primer fotograma; es también el último del bucle). Salida: `corte en el movimiento` hacia la toma 2.

**Especificación de dibujo:**

- Tarjeta_1999 como en la sección 5, como `Capa` con `z` animado de −100 (W aparente 600 px) a −290 (W aparente 760 px) con ease-out cúbico en los fotogramas 0 a 12: **en el fotograma 0 ya hay velocidad** (el ease-out arranca rápido). Sombra proyectada sobre el papel (dx 14, dy 10, radio 10, opacidad 0,22) porque la tarjeta «flota». Dedos mostaza.
- Texto «Jensen Huang / Is Back» (fila 1 de la sección 12) en dos líneas, **entero y quieto en el fotograma 0** (sin `pop`), letra de 128 px, tope de la primera línea en y = 415; «Back» en mostaza con trazo de tinta de 0,045 em. En el fotograma 6 «Back» da el **golpe** (escala 1,0 a 1,18 en 5 fotogramas con `pop` y asiento en 7; el resto del texto no se mueve). Sale en el corte de 1,0 (30 fotogramas visibles).
- Tan: pose `parado`, expresión `eureka` (sorpresa alegre; en perfil `sorpresa` se le leía seria), vista `perfil`, `mira=1`, `cabeza_giro=25`, x = 24 %, pies a 86 %, `alto` 487 px, `objeto=False`. Tin: pose `parado`, expresión `sorpresa`, vista `perfil`, `mira=-1`, `cabeza_giro=25`, x = 76 %, `objeto=False` (el lápiz es mostaza y la tarjeta ya lleva el acento). Con suelo y sombra de contacto (opacidad 0,25). Los dos rebotan al pulso de 0,5 s con la bufanda de Tan en movimiento secundario.
- **Color:** acento mostaza = «Back» + los dedos del conector de la tarjeta (único elemento). Cabezas, gorra y bufanda son identidad.
- Medidas que el render debe comprobar en el fotograma 0 y en el 12: texto dentro de x 108 a 942 e y 415 a 690; tarjeta dentro de y 720 a 1100; caras dentro de x 60 a 960 e y 380 a 1440; el texto a 40 px o más de la tarjeta.

### Toma 2 — Subjetivo: las manos meten la tarjeta en la ranura

- **Duración:** 1,5 s (de 1,0 a 2,5)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** subjetivo y macro: la placa base de una PC en la mitad de abajo, la ranura en el centro y la tarjeta bajando entre dos manos
- **Cámara:** empuje lento con profundidad (la cámara se mete 110 unidades), sin cortes dentro de la toma (45 fotogramas)
- **Acción:** dos manos de palitos bajan la tarjeta_1999 hasta que los dedos dorados entran en la ranura; asienta con un pequeño rebote en 2,2 s y la toma sigue 0,3 s.
- **Audio:** línea 1, Tan (final): "Remember putting one of these in your P C?" Aquí suena «…in your P C?» (hasta unos 2,30 s). Clic de inserción de la sección 13.
- **Referencia:** efecto 5 de `manual/14`, sección 7.1 (subjetivo o macro de las manos usando el objeto)
- **Transición de entrada:** `corte en el movimiento` desde la toma 1 (la tarjeta, que ya bajaba, sigue bajando: mismo centro en x, tamaño dentro del ±10 %). Salida: corte seco.

**Especificación de dibujo:**

- Capas (z): papel (+900), placa_base y ranura (+60), tarjeta_1999 de W = 700 px (−120), manos_de_palitos (−220). Foco en −120 (la tarjeta y los dedos), apertura 0,018, campo 120: las manos quedan nítidas y la placa casi (1 o 2 px de desenfoque).
- Sombra proyectada de la tarjeta sobre la placa (dx 10, dy 14, radio 8) que sube de opacidad 0,15 a 0,30 al acercarse y, al asentar, sombra de contacto bajo los dedos.
- **Color:** acento mostaza = los dedos del conector (único elemento; la ranura, la placa y las manos, en neutros). Sin texto. Sin tomate.
- Movimiento secundario: las manos oscilan ±2 grados con muelle y la tarjeta rebota 8 px al asentar (se pasa menos del 12 %). El ventilador de la tarjeta sigue girando.

### Toma 3 — La tarjeta, en su pedestal: capas, sombras y foco

- **Duración:** 3,5 s (de 2,5 a 6,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto: la tarjeta_1999 sobre su pedestal en el centro, Tan a la izquierda y Tin a la derecha, mirándola; las siluetas de una PC al fondo
- **Cámara:** empuje lento con barrido mínimo (la cámara va de x = 540 a 580 y se mete de 0 a 90 unidades: ≈ 1 % del ancho por segundo, muy por debajo del 8 % del límite)
- **Acción:** Tin señala la tarjeta con el lápiz y Tan la mira con nostalgia; al final de la toma, **el foco pasa de la tarjeta a Tin** mientras Tin acaba de decir el año (cambio de foco de 12 fotogramas en la pausa entre líneas).
- **Audio:** línea 2, Tin: "That's the G Force two fifty-six, from nineteen ninety-nine." (de 2,55 a 5,68 s; «That's the G Force two fifty-six,» hasta 4,25 y «from nineteen ninety-nine.» desde 4,40).
- **Referencia:** efectos 4 y de cambio de foco de `manual/14` (capas con paralaje, sombras de contacto, `Camara.foco`); prueba de efectos, técnicas 1 y 2
- **Transición de entrada:** corte seco desde la toma 2. Salida: ninguna (continúa, sin corte, en la toma 4).

**Especificación de dibujo:**

- Capas (z): papel (+900); pc_beige (+420, con niebla); pedestal y tarjeta_1999 de W = 420 px (−260, la más cercana a la cámara de las nítidas); Tan y Tin (0); **primer plano: un cable de tinta de 36 px en un lazo grande en la esquina inferior izquierda (−320), siempre desenfocado** (el lápiz de Tin no puede ir ahí: es mostaza y competiría con el acento).
- Foco: de 2,5 a 5,68 en z = −260 (la tarjeta nítida; Tan y Tin a 260 unidades del foco, con 4 o 5 px de desenfoque: se les ve el gesto y no se les lee la cara, y ninguno habla en esta toma); de 5,68 a 6,08 el foco viaja a z = 0 (Tin y Tan nítidos; la tarjeta queda con 4 o 5 px). Apertura 0,03, campo 100.
- Sombras: contacto bajo el pedestal y bajo los pies de Tan y Tin (opacidad 0,25 a 0,30). Sin sombra tumbada de los muñecos (la prueba de efectos la descartó: con palitos es una mancha).
- Tan: pose `pregunta`, expresión `nostalgia`, vista `frente`, `mira=1`, `espejo=True`, x = 22 %, pies a 86 %, `alto` 34 %, `objeto=False`, `viento` oscilando. Tin: pose `senala`, expresión `feliz`, vista `frente`, `mira=-1`, x = 78 %, `objeto="lapiz"` (movimiento secundario de ±3 grados).
- Texto «GeForce 256» de 2,7 a 4,3 y «1999» de 4,4 a 5,9 (filas 2 y 3 de la sección 12), con `pop`.
- **Color:** acento mostaza = la clave del texto («256»; luego «1999») + el lápiz de Tin (único elemento: los dedos de la tarjeta están dentro de la ranura del pedestal y no se ven). Sin tomate.

### Toma 4 — Tin da la noticia del regreso (el mismo plano continúa)

- **Duración:** 3,0 s (de 6,0 a 9,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** el mismo héroe abierto de la toma 3; la cámara se acerca a Tin; la tarjeta queda a un lado, desenfocada
- **Cámara:** sigue el empuje de la toma 3 (avance de 90 a 150 y x de 580 a 600); sin cortes ni nuevos movimientos de cámara encadenados
- **Acción:** Tin se vuelve hacia la cámara y explica con el lápiz; entra la fecha y después el hecho; Tan escucha con curiosidad. Un cambio a mitad de toma (a los 7,5 s Tin levanta el lápiz y Tan asiente) para que los 3 s no queden planos.
- **Audio:** línea 3, Tin: "Nvidia's board brought Jensen Huang back as C E O." (de 6,08 a 9,06 s).
- **Referencia:** prueba de efectos, técnica 1 (profundidad); lección del short 2 (planos largos con un cambio a mitad)
- **Transición de entrada:** continúa de la toma 3 (sin corte). Salida: corte seco.

**Especificación de dibujo:**

- Mismas capas y sombras que la toma 3, con el foco en z = 0. Tin: pose `explica`, expresión `feliz`, `objeto="lapiz"`. Tan: pose `parado`, expresión `curiosidad`, `espejo=True`. Posiciones de la toma 3.
- Texto «Nov 23» de 6,2 a 7,5 y «Back as CEO» de 7,6 a 8,9 (filas 4 y 5), con `pop`; nunca sobre un personaje.
- **Color:** acento mostaza = la clave («23», luego «CEO») + el lápiz de Tin. Sin tomate.
- No se dibuja a Jensen Huang ni nada que lo sugiera (ni foto, ni silueta, ni sombra).

### Toma 5 — Tan pregunta: la tarjeta nueva aparece desde el desenfoque

- **Duración:** 2,5 s (de 9,0 a 11,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos; en la zona de gráficos, las dos tarjetas lado a lado: la de 1999, chica, a la izquierda, y la nueva, grande, a la derecha
- **Cámara:** fija
- **Acción:** Tan pregunta con la mano levantada; la tarjeta_actual **aparece desde el desenfoque** en 8 fotogramas (a los 9,3 s) en cuanto Tan empieza a hablar; Tin sonríe.
- **Audio:** línea 4, Tan: "How many of those are in a new one?" (de 9,31 a 11,26 s; el corte de 11,5 cae justo antes de la línea 5).
- **Referencia:** técnica 4 de la prueba de efectos (`revelar_desde_desenfoque`); efecto de revelado de `manual/14`, 2.2
- **Transición de entrada:** corte seco desde la toma 4. Salida: `borrón` hacia la toma 6.

**Especificación de dibujo:**

- Capas (z): papel (+900); tarjeta_1999 de W = 300 px (0; x 100 a 400, y centro 39 %); tarjeta_actual de W = 416 px (−200: se ve a W = 500 px, x 440 a 940; y centro 39 %); Tan y Tin (0). Foco en 0; **la tarjeta_actual entra con `revelar_desde_desenfoque` (radio 42 a 0 en 8 fotogramas, f 279 a 287) y se queda nítida**. Sombra proyectada de las dos tarjetas (opacidad 0,2). El ventilador de la tarjeta_1999 sigue girando; los tres de la nueva, también (más lento).
- Tan: pose `pregunta`, expresión `curiosidad`, vista `frente`, `espejo=True`, x = 30 %, `alto` 34 %, `objeto=False`. Tin: pose `parado`, expresión `feliz`, vista `frente`, x = 70 %, `objeto=False` (la tarjeta_1999 lleva los dedos mostaza: ahora es ella el elemento).
- Texto «RTX 5090» de 9,4 a 11,4 (fila 6), con `pop`.
- **Color:** acento mostaza = la clave («5090») + los dedos de la tarjeta_1999 (único elemento); los dedos de la nueva, marrón. Sin tomate.

### Toma 6 — Se cuentan transistores, no velocidad

- **Duración:** 2,0 s (de 11,5 a 13,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** detalle: el chip (die) en la zona de gráficos, con Tan y Tin debajo
- **Cámara:** fija
- **Acción:** el chip entra con `pop`; un círculo de tinta lo rodea, dibujándose a mano (garabato); Tin explica y Tan asiente.
- **Audio:** línea 5, Tin: "We're counting transistors, not speed." (de 11,51 a 13,36 s).
- **Referencia:** técnica 9 de la prueba de efectos (garabatos de tinta); `manual/14`, 2.7
- **Transición de entrada:** `borrón` desde la toma 5. Salida: corte seco.

**Especificación de dibujo:**

- Die de la sección 5 en el centro de la zona de gráficos (centro en x = 540, y = 750), con `pop`. Garabato `trazo_circulo` de 12 fotogramas (f 358 a 370) alrededor del die, grosor 9 px, tinta; un solo trazo.
- Capas (z): papel (+900), die (−100, con sombra proyectada), personajes (0). Foco en −100; apertura 0,018.
- Tan: pose `parado`, expresión `curiosidad`, vista `frente`, `espejo=True`, x = 30 %, `alto` 34 %. Tin: pose `explica`, expresión `feliz`, x = 70 %, `objeto=False` (el die es mostaza).
- Texto en dos líneas «transistors, / not speed» (fila 7), tamaño 5,5 %, de 11,6 a 13,4; clave: «transistors».
- **Color:** acento mostaza = la clave + el die (único elemento). Sin tomate.

### Toma 7 — La tarjeta de 1999: hasta 23 millones

- **Duración:** 3,0 s (de 13,5 a 16,5)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe de objeto (cerca de la mitad del video): la tarjeta_1999 grande en la zona de gráficos, con Tan debajo
- **Cámara:** empuje lento con profundidad (avance de 0 a 70)
- **Acción:** la tarjeta_1999 flota sobre el papel con su ventilador girando; Tan la mira; el rótulo entra.
- **Audio:** línea 6, Tin: "That card had up to twenty-three million transistors." (de 13,61 a 16,38 s).
- **Referencia:** técnica 1 de la prueba de efectos; plano héroe (`manual/14`, sección 4)
- **Transición de entrada:** corte seco desde la toma 6. Salida: **`barrido_obturador`** hacia la toma 8 (6 fotogramas, f 492 a 498).

**Especificación de dibujo:**

- Capas (z): papel (+900); sombra proyectada de la tarjeta sobre el papel (dx 14, dy 10, radio 10, opacidad 0,22); tarjeta_1999 de W = 800 px (−150), centrada en (50 %; 39 %); Tan (0). Foco en −150.
- Tan: pose `parado`, expresión `curiosidad`, vista `frente`, `espejo=True`, x = 50 %, `alto` 34 %, `objeto=False`.
- Texto «up to / 23 million» (fila 8): «up to» al 4,5 % y «23 million» al 7 %, de 13,6 a 16,4; clave: «23».
- **Color:** acento mostaza = «23» + los dedos de la tarjeta (único elemento). Sin tomate.

### Toma 8 — La RTX 5090: unos 92.000 millones

- **Duración:** 3,5 s (de 16,5 a 20,0)
- **Personajes:** @tan
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe de objeto: la tarjeta_actual grande en la zona de gráficos, con Tan debajo
- **Cámara:** empuje lento con profundidad (avance de 0 a 70)
- **Acción:** la tarjeta nueva entra con el barrido y se asienta con frenada; sus tres ventiladores giran; Tan se asombra un poco más que en la toma anterior.
- **Audio:** línea 7, Tin: "The R T X fifty-ninety has about ninety-two billion." (de 16,63 a 20,03 s).
- **Referencia:** toma 7 de esta pieza (mismo plano, otro objeto)
- **Transición de entrada:** `barrido_obturador` desde la toma 7. Salida: corte seco.

**Especificación de dibujo:**

- Capas como la toma 7, con la tarjeta_actual de W = 840 px (−150), centrada en (50 %; 39 %); su alto con dedos es 0,38 W = 319 px. Dedos mostaza.
- Tan: pose `parado`, expresión `sorpresa`, vista `frente`, `espejo=True`, x = 50 %, `alto` 34 %, `objeto=False`.
- Texto «RTX 5090 / ≈ 92 billion» (fila 9): «RTX 5090» al 4,5 % y «≈ 92 billion» al 7 %, de 16,6 a 19,9; clave: «92».
- **Color:** acento mostaza = «92» + los dedos de la tarjeta_actual (único elemento). Sin tomate.

### Toma 9 — «Divide them»: la ecuación entre dos objetos

- **Duración:** 1,0 s (de 20,0 a 21,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto de los dos; en la zona de gráficos, la ecuación de dos filas (sección 5)
- **Cámara:** fija
- **Acción:** las dos tarjetas «vuelan» a sus filas con `slide`, entran los textos y el signo «÷»; Tin levanta la mano y Tan espera. La subida de sonido corre bajo «Divide them.» y, al terminar la línea, el silencio de 12 fotogramas.
- **Audio:** línea 8, Tin: "Divide them." (de 20,28 a 20,98 s). **Silencio total de 12 fotogramas de 20,98 a 21,38 s** (ni voz, ni música, ni efectos). Subida de la sección 13.
- **Referencia:** «subida de sonido, silencio de 10 a 12 fotogramas» de `manual/14`, 7.1 efecto 6
- **Transición de entrada:** corte seco desde la toma 8. Salida: ninguna (continúa en la toma 10).

**Especificación de dibujo:**

- Ecuación de la sección 5. Las tarjetas pequeñas con los **dedos marrón** (plano de revelación: ningún elemento mostaza). Textos «≈ 92 billion» y «÷ 23 million» al 5,5 % (fila 10), en tinta y sin clave.
- Tan: pose `parado`, expresión `curiosidad`, vista `frente`, `espejo=True`, x = 30 %, `alto` 34 %. Tin: pose `saluda`, expresión `feliz`, x = 70 %, `objeto=False`.
- **Color:** ni mostaza ni tomate todavía: el plano está en neutros; el tomate llega con la cifra.

### Toma 10 — El pico: más de 4.000 (el mismo plano continúa)

- **Duración:** 3,0 s (de 21,0 a 24,0)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto con la cifra arriba (pico de emoción)
- **Cámara:** fija hasta la cifra; en el fotograma de llegada, **un solo golpe de zoom suave de +10 %** (5 fotogramas de ida con `sello` y 8 de asiento) con origen en el centro de la cifra; después, quieta
- **Acción:** el contador sube de 250 a 4.000 con ease (acelera y frena) en 36 fotogramas (de 21,0 a 22,2); al llegar, el número pasa a tomate, aparece el «+» con un `pop` y la cifra se queda quieta 54 fotogramas; Tan celebra y Tin levanta la mano.
- **Audio:** línea 9, Tin: "More than four thousand." (de 21,38 a 22,48 s; «four thousand» hacia 22,0 a 22,48). Tictac y ding de la sección 13. Línea 10, Tan: "Four thousand of these in one of those?" (de 22,73 a 24,48 s) suena sobre la cifra quieta; el corte de 24,0 cae dentro de «in one of those?».
- **Referencia:** toma 10 del short 2 (contador y celebración); efecto 6 de `manual/14`, 7.1
- **Transición de entrada:** continúa de la toma 9. Salida: corte seco.

**Especificación de dibujo:**

- Contador de 250 a 4.000 en la zona de texto (y = 15 %), tamaño 7 %, ease-out cúbico de 21,0 a 22,2; **el valor llega a 4.000 en el mismo fotograma que el tomate, el «+» y el `pop`** (lección del short 2: el `pop` y el sonido atados al fotograma de llegada). Solo sube; nunca pasa de 4.000; nunca se ve «0». Al llegar, el texto «4,000+» pasa de tinta a tomate `#C8553D` con contorno tinta de 0,045 em.
- Mientras la cifra se lee **nada se mueve detrás de ella**: la ecuación queda quieta; solo hay la respiración de los personajes (acción secundaria de amplitud pequeña).
- Subtítulo fijo bajo la cifra «transistors, not speed» al 3,5 % en tinta (fila 12), de 21,4 a 27,4.
- Tan: pose `celebra`, expresión `sorpresa`, vista `frente`, `espejo=True`, x = 30 %, `viento` alto con muelle; desde 22,73 (cuando habla) mantiene la expresión. Tin: pose `saluda`, expresión `eureka`, x = 70 %, `objeto=False`.
- **Color (revelación):** acento tomate = la cifra «4,000+» al llegar; **nada en mostaza como acento** (Tan conserva su bufanda mostaza, que es identidad).

### Toma 11 — El muro de 4.000 tarjetas crece

- **Duración:** 1,5 s (de 24,0 a 25,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto; la pared_de_tarjetas llena la zona de gráficos; la cifra sigue arriba
- **Cámara:** fija
- **Acción:** la pared se llena de arriba abajo, fila por fila, con ease-out (gráfico que crece, 30 fotogramas: de 24,0 a 25,0); Tan se encoge de hombros con la boca abierta; la última fila cae en 25,0 y la pared queda quieta 15 fotogramas.
- **Audio:** línea 10, Tan (final): "Four thousand of these in one of those?" (hasta 24,48 s). Línea 11, Tin (inicio): "That whole wall, in transistors, is one chip." (desde 24,73 s; «That whole wall,» ya con la pared completa). Cascada de la sección 13.
- **Referencia:** «gráfico que crece» y asombro de `manual/14`, 2.7 y sección 3
- **Transición de entrada:** corte seco desde la toma 10 (el corte cae durante «in one of those?», con la cifra de tomate ya leída 54 fotogramas). Salida: continúa en la toma 12.

**Especificación de dibujo:**

- Pared_de_tarjetas de la sección 5, filas apareciendo cada 0,6 fotogramas (50 filas en 30 fotogramas). Capas (z): papel (+900); pared (0). Sombra de contacto fina bajo la pared (opacidad 0,15).
- Cifra «4,000+» en tomate arriba y subtítulo «transistors, not speed» al 3,5 %, quietos.
- Tan: pose `encoge`, expresión `sorpresa`, vista `frente`, `espejo=True`, x = 30 %. Tin: pose `parado`, expresión `feliz`, x = 70 %, `objeto=False`.
- **Color (revelación):** acento tomate = la cifra; la pared, en marrón y papel (neutros).

### Toma 12 — Todo el muro es un solo chip (la pared se pliega)

- **Duración:** 2,0 s (de 25,5 a 27,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** héroe abierto: a la izquierda la pared encogida, a la derecha la tarjeta_actual, y el signo «=» entre las dos
- **Cámara:** fija
- **Acción:** la pared se encoge y se desplaza a la izquierda (36 fotogramas con ease, de 25,5 a 26,7); la tarjeta_actual entra deslizándose desde la derecha y se asienta; el signo «=» aparece con `pop` y las dos quedan a la misma altura; Tin señala; Tan se ríe.
- **Audio:** línea 11, Tin: "That whole wall, in transistors, is one chip." (de 24,73 a 27,16 s; «is one chip.» sobre la tarjeta que entra).
- **Referencia:** toma 11 (continuación); remate de tamaño (`manual/14`, 2.7 y sección 3: «la magnitud comparada con algo conocido»)
- **Transición de entrada:** continúa de la toma 11. Salida: corte seco.

**Especificación de dibujo:**

- Pared encogida a 380 × 237 px (x 100 a 480; centro en y = 750). Tarjeta_actual de W = 380 px (x 600 a 980; alto 0,38 W = 144 px; centro en y = 750). Signo «=» de tinta, 100 px, centrado en x = 540, entra en 26,7 con `pop`. Dedos de la tarjeta, marrón.
- Cifra «4,000+» en tomate arriba y subtítulo «transistors, not speed» al 3,5 %, quietos hasta 27,4.
- Tan: pose `encoge`, expresión `risa`, vista `frente`, `espejo=True`, x = 30 %. Tin: pose `senala`, expresión `eureka`, x = 70 %, `objeto=False`.
- **Color (revelación):** acento tomate = la cifra; sin mostaza como acento.

### Toma 13 — Cierre de firma: Tin y Tan, y la invitación

- **Duración:** 2,0 s (de 27,5 a 29,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** plano fijo de respiro de los dos, de frente, saludando a cámara
- **Cámara:** fija, escala 100 % (respiro de 60 fotogramas)
- **Acción:** Tin y Tan saludan con el mismo gesto en todos los videos; Tan dice la invitación; entra la palabra «Subscribe» con su nombre debajo.
- **Audio:** línea 12, Tan: "Subscribe and count with us." (de 27,50 a 28,80 s; **la única invitación a suscribirse**). Después, 0,7 s de silencio de voz.
- **Referencia:** efecto 7 de `manual/14`, 7.1 (cierre de firma); `plan_programa_de_socios.md`, P6c
- **Transición de entrada:** corte seco desde la toma 12 (con un respiro de voz de unos 0,34 s antes de la invitación). Salida: **`congelado_con_marco`** hacia la toma 14.

**Especificación de dibujo:**

- Tan: pose `saluda`, expresión `feliz`, vista `frente`, `espejo=True`, x = 30 %, `alto` 34 %. Tin: pose `saluda`, expresión `feliz`, vista `frente`, x = 70 %, `objeto=False`. Los dos saludan hacia afuera. Suelo y sombra de contacto.
- Texto «Subscribe» (clave, entero) al 7 % de 27,7 a 29,4 y «Tin & Tan» al 3,8 %, en tinta, debajo, de 27,7 a 29,4 (filas 14 y 15).
- **Color:** acento mostaza = «Subscribe» (palabra clave; sin elemento mostaza aparte). Sin tomate.

### Toma 14 — Congelado con marco y vuelta a la portada (bucle)

- **Duración:** 1,0 s (de 29,5 a 30,5)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** papel_crema
- **Encuadre:** el cierre se congela como una foto con marco, cae, y aparece exactamente el plano del fotograma 0
- **Cámara:** fija
- **Acción:** el plano de la toma 13 se congela, se reduce a una foto con marco que gira 4 grados y cae (22 fotogramas, de 29,5 a 30,25); detrás aparece el plano de la portada (tarjeta de 600 px, texto, Tan y Tin de perfil); queda quieto 8 fotogramas. **El último fotograma es igual al primero.**
- **Audio:** sin voz (la voz terminó en 28,80: 1,7 s de silencio de voz hasta el empalme; en el fotograma 0 la voz vuelve a entrar sin pausa). Clic de cámara y thunk de la sección 13.
- **Referencia:** técnica 11 de la prueba de efectos (`congelado_con_marco`), que ahí se guardó «para un cierre»; `manual/14`, 2.4
- **Transición de entrada:** `congelado_con_marco` desde la toma 13. Salida: bucle al fotograma 0 de la toma 1.

**Especificación de dibujo:**

- `congelado_con_marco(a, b, p)` con a = la toma 13, b = el plano del fotograma 0 de la toma 1 (tarjeta de 600 px aparente en z = −100, ángulo cero, estela ninguna), escala 0,62, giro −4, marco 26, salida 0,68. **Sin destello** (el de la prueba se quitó).
- Texto «Jensen Huang / Is Back» (fila 16) forma parte del plano b y llega entero; la palabra clave no da su golpe aquí (solo en el fotograma 6 de la toma 1). Tan y Tin rebotan al pulso de 0,5 s: 61 pulsos en 30,5 s, así que **el fotograma 915 (el que sigue al último, el 914) es igual al fotograma 0**.
- **Color:** acento mostaza = «Back» + los dedos de la tarjeta, como en la toma 1.

## 7. Audio

- **Voz (no generada):** Tan con Zelda (líneas 1, 4, 10 y 12) y Tin con Kevin (líneas 2, 3, 5, 6, 7, 8, 9 y 11), Higgsfield `seed_audio`, ajustes por defecto, **una sola generación por voz** (regla de un solo intento), al 110 % con `atempo=1.10` y normalizada a −14 LUFS, como en el short 2. **Necesita el sí del dueño con la cotización de `estimate_audio_cost`** (estimado por analogía con el short 2: ≈ 0,8 créditos para Tan y ≈ 2,5 para Tin, ≈ 3,3 en total; no se ha cotizado).
- **Tiempos estimados.** Ritmo medido del short 2 (`2026-11-21_tin_y_tan_gta6/05_audio/linea_de_tiempo_voz.md`, 110 %): ≈ 4,7 sílabas por segundo en las frases de Tin y ≈ 5,2 en las de Tan, más 0,15 s por cada pausa interna (coma o dos puntos) y 0,25 s entre líneas. Dos pausas están diseñadas más largas: 0,40 s entre las líneas 2 y 3 (para el cambio de foco de 12 fotogramas) y 0,40 s entre las líneas 8 y 9 (el silencio de 12 fotogramas antes de la cifra). **Se reajustan con la voz real** (cortes por `silencedetect` a −35 dB, como en el short 2) y los cortes del video se afinan después; nadie ha oído nada.
- **Pausas del generador:** Zelda hizo pausas de 0,7 a 0,8 s tras una coma en el short 2. Por eso las líneas de Tan de este video **no llevan comas** (las de Tin sí, y se acortan a 0,15 s en edición).
- **Pronunciación (decisión del equipo):** «GeForce 256» se escribe **«G Force two fifty-six»** para el generador: «G Force» con espacio (sin guion, que puede provocar una pausa) se lee «jee force», que es como se dice «GeForce»; «two fifty-six» evita que lea «two hundred fifty-six». La RTX 5090 se escribe **«R T X fifty-ninety»** (como se dice en inglés de EE. UU.) y «CEO», «PC», con las letras separadas, como «G T A» en el short 2. **«Jensen Huang» y «Nvidia» van tal cual** (no se puede comprobar el acento sin oír; si sale mal, se corrige en edición, o se pide autorización para regenerar esa voz; no se regenera por cuenta propia). En los subtítulos y en pantalla va lo que se lee: «GeForce 256», «RTX 5090», «CEO», «PC».
- **Final de archivo:** la grabación de Tin del short 2 llegó cortada en «now» (palabra corta abierta). Aquí **la última línea útil de cada voz termina en consonante** («us» y «chip») **y cada pieza lleva al final una coletilla que se descarta en el montaje** («That's all, folks.»), así, si el generador recorta el final, se pierde la coletilla y no la frase.

Guion de voz (líneas numeradas, quién habla, texto exacto, inicio y fin ESTIMADOS en el diálogo al 110 %):

| Línea | Quién | Empieza (s) | Termina (s) | Dura (s) | Texto exacto (números como se dicen) | Sílabas |
|---|---|---|---|---|---|---|
| 1 | Tan | 0,00 | 2,30 | 2,30 | Remember putting one of these in your P C? | 12 |
| 2 | Tin | 2,55 | 5,68 | 3,13 | That's the G Force two fifty-six, from nineteen ninety-nine. | 14 |
| 3 | Tin | 6,08 | 9,06 | 2,98 | Nvidia's board brought Jensen Huang back as C E O. | 14 |
| 4 | Tan | 9,31 | 11,26 | 1,95 | How many of those are in a new one? | 10 |
| 5 | Tin | 11,51 | 13,36 | 1,85 | We're counting transistors, not speed. | 8 |
| 6 | Tin | 13,61 | 16,38 | 2,77 | That card had up to twenty-three million transistors. | 13 |
| 7 | Tin | 16,63 | 20,03 | 3,40 | The R T X fifty-ninety has about ninety-two billion. | 16 |
| 8 | Tin | 20,28 | 20,98 | 0,70 | Divide them. | 3 |
| 9 | Tin | 21,38 | 22,48 | 1,10 | More than four thousand. | 5 |
| 10 | Tan | 22,73 | 24,48 | 1,75 | Four thousand of these in one of those? | 9 |
| 11 | Tin | 24,73 | 27,16 | 2,43 | That whole wall, in transistors, is one chip. | 10 |
| 12 | Tan | 27,50 | 28,80 | 1,30 | Subscribe and count with us. | 6 |

Voz total: de 0,00 a 28,80 s; hasta 30,5 hay 1,7 s sin voz y al volver al fotograma 0 la voz entra otra vez sin silencio inicial (silencio total del empalme: 1,7 s, menos de 2 s). Tramos internos: línea 2, «from nineteen ninety-nine.» desde 4,40; línea 9, «four thousand.» desde 22,0.

**Texto para generar cada voz (una pieza por personaje; las líneas van separadas por una línea en blanco; las letras sueltas se leen letra por letra):**

Voz de Tan (Zelda), una sola generación, 5 líneas (la última, coletilla que se descarta):

```text
Remember putting one of these in your P C?

How many of those are in a new one?

Four thousand of these in one of those?

Subscribe and count with us.

That's all, folks.
```

Voz de Tin (Kevin), una sola generación, 9 líneas (la última, coletilla que se descarta):

```text
That's the G Force two fifty-six, from nineteen ninety-nine.

Nvidia's board brought Jensen Huang back as C E O.

We're counting transistors, not speed.

That card had up to twenty-three million transistors.

The R T X fifty-ninety has about ninety-two billion.

Divide them.

More than four thousand.

That whole wall, in transistors, is one chip.

That's all, folks.
```

Los cortes de cada pieza en líneas se hacen por las pausas medidas, como en el short 2, y se comprueban al oído antes de publicar (en particular «G Force», «R T X fifty-ninety», «Nvidia» y «Huang»).

- **Subtítulos:** `02_prompt/subtitulos.srt` (12 líneas, las del guion escritas como se leen), con los tiempos estimados; se reajustan con la voz real. Lección del short 2: el `.srt` lleva lo que se lee en pantalla, no la grafía del generador.
- **Idioma:** inglés de EE. UU. Un solo idioma (el canal no es de series).
- **Música:** hecha con código (Python y numpy), **distinta de la de los shorts 1 y 2** (variación): en re dórico (modo menor cálido, no el tono mayor del short 2), con un acorde cada 2,0 s (sensación de 60 por minuto aunque los cortes sigan la rejilla de 0,5 s), timbre de piano eléctrico suave y bajo redondo, sin el patrón de 120 BPM del short 2. A −24 LUFS, 10 dB por debajo de la voz; calla en el silencio de 20,98 a 21,38 s y vuelve con el ding a los 22,2 s. Cubre 30,5 s y su último acorde (1,5 s) resuelve a la tónica del primero para el bucle. Se anota en `licencias.md`. Sin música de terceros.
- **Efectos:** los de la sección 13, hechos con código, sin material de terceros.

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → Toma 3 → Toma 4 → Toma 5 → Toma 6 → Toma 7 → Toma 8 → Toma 9 → Toma 10 → Toma 11 → Toma 12 → Toma 13 → Toma 14 (y vuelve a la toma 1). Las tomas 3 y 4, 9 y 10, y 11 y 12 son tres planos continuos partidos para describirlos: no hay corte entre ellas.
- **Transiciones (todas motivadas):** `corte en el movimiento` (1 a 2), corte seco (2 a 3, 4 a 5, 6 a 7, 8 a 9, 10 a 11, 12 a 13), `borrón` (5 a 6), `barrido_obturador` una vez (7 a 8) y `congelado_con_marco` una vez (13 a 14). Sin destellos, sin negativo, sin «atravesar la escena».
- **Texto en pantalla:** se dibuja en el mismo render, solo el de la tabla de la sección 12. El texto nunca contradice lo que se oye.
- **Portada:** el fotograma 0, que cumple los 6 puntos de la regla del dueño (`ENTREGA_YOUTUBE.md`, «Portada de los Shorts»): «Jensen Huang / Is Back» (4 palabras en 2 líneas, mayúscula inicial en cada una, «Back» en mostaza, sin la cifra ni la respuesta) entre y 415 y 690, la tarjeta_1999 en el centro (y 769 a 1051 en el fotograma 0; 731 a 1089 desde el 12), y las caras de Tan y Tin dentro de la zona útil (x 60 a 960, y 380 a 1440), de perfil y con la cabeza inclinada 25 grados hacia arriba, mirando la tarjeta. `codigo/miniatura.py` (copia del del short 2) guarda ese fotograma como `06_final/portada_short03.png` (1080x1920) y mide las cajas. El video cumple lo que promete la portada: dice que Jensen Huang volvió (línea 3) y cuenta la tarjeta (el título y la portada no prometen más: no dicen «más rápida» ni dan la cifra).
- **Formato de salida:** 1080x1920, 30 fps, H.264, yuv420p, AAC a 48 kHz. Archivo `06_final/tin_y_tan_short03_v1.mp4`. Pesa unos 3 MB: se recomprime a CRF 22 si pasa de 3,1 MB (`ENTREGA_YOUTUBE.md`, «Límite de subida desde la nube»).
- **Título de la publicación (inglés):** Jensen Huang Is Back: GeForce 256 vs RTX 5090
- **Descripción de la publicación (en inglés, obligatoria; con una línea de suscripción):**

```text
Jensen Huang is back as Nvidia's CEO (announced Nov 23, 2026). Nvidia launched the GeForce 256 in 1999. How many of those fit in the RTX 5090? We counted transistors, not speed.

GeForce 256 (launched Oct 11, 1999): up to 23 million transistors. Wikipedia's "Transistor count" table lists 17 million; 1999 press reports said ≈ 23 million. We use the larger number, so the result is the cautious one.
GeForce RTX 5090 (GB202, on sale since Jan 30, 2025): ≈ 92.2 billion transistors.
≈ 92.2 billion ÷ 23 million ≈ 4,009, so more than 4,000. With 17 million it is ≈ 5,424.

This counts transistors only. It says nothing about speed, price or performance.

Want more counts like this? Subscribe to Tin & Tan.

Sources, all read on 2026-11-24: Wikipedia, "Jensen Huang"; Wikipedia, "GeForce 256"; Wikipedia, "Transistor count"; Wikipedia, "GeForce RTX 50 series". Nvidia's own announcement could not be opened, so the return date also rests on news channel headlines.

Not affiliated with Nvidia. Jensen Huang is not involved in this video.
```

- **Etiquetas (en total, menos de 500 caracteres):** Jensen Huang, Nvidia, GeForce 256, RTX 5090, graphics card, 1999, retro PC, nostalgia, transistors, Tin & Tan, shorts
- **Pasan por `revisar_texto.py --idioma en`** (descripción, etiquetas, `subtitulos.srt` y los textos de pantalla del código): 0 errores (2026-11-24; los nombres «Nvidia», «GeForce» y «RTX» se añadieron a `video-studio/glosario.txt` con su porqué; «Jensen» y «Huang» ya los conoce el diccionario). Ni la voz, ni el título, ni la descripción, ni las etiquetas usan la palabra que el brief prohíbe para calificar la polémica.
- **Fuentes y fechas:** Wikipedia en inglés, «Jensen Huang» (reposición el 23 de noviembre de 2026), «GeForce 256» (11 de octubre de 1999), «Transistor count» (17 millones; 92.200 millones para el GB202) y «GeForce RTX 50 series» (a la venta desde el 30 de enero de 2025), todas leídas el 2026-11-24; las cadenas de noticias (CNN, BBC, NBC, CBS, ABC, Fox) coinciden en sus títulos de YouTube del mismo día. **El comunicado de Nvidia no se pudo abrir.** La cifra de 23 millones de 1999 solo se vio en un resumen de buscador.

### Título (ficha)

Filtro: `revisar_titulo.py` v1.0 (2026-11-24). Estudio y reglas: `video-studio/comercial/titulos.md`.

| Campo | Valor |
|---|---|
| `titulo_elegido` | Jensen Huang Is Back: GeForce 256 vs RTX 5090 |
| `caracteres` | 45 |
| `idioma` | en |
| `canal` | tin-y-tan |
| `formato` | short |
| `publico` | EE. UU., adultos de 45 a 62 años que armaban o compraban una PC en 1999; secundario, de 30 a 45 que juegan hoy |
| `frase_de_busqueda` | jensen huang is back |
| `fuente_de_la_frase` | los títulos de YouTube del 2026-11-24 (`00_analisis_de_tematicas.md`, «Segunda vuelta», S2: «Jensen Huang Is Back…», «JENSEN HUANG IS BACK!!!»); volumen: sin dato |
| `formula` | nombre buscado al inicio + dos objetos que se comparan |
| `alternativa_1` | Jensen Huang Is Back: 1999 GeForce 256 vs Now (45 caracteres; misma frase; filtro: PASA) |
| `alternativa_2` | Jensen Huang Is Back: GeForce 256 vs Today's GPU (48 caracteres; misma frase; filtro: PASA; menos exacta: «Today's» es ambiguo, ver la decisión 3 de la sección 3) |
| `uso_de_las_alternativas` | Reserva. YouTube no ofrece prueba A/B de títulos en Shorts (ayuda oficial, leída el 2026-11-21). No se cambia un título publicado antes de los 28 días y sin datos del canal |
| `filtro` | **PASA** · errores: ninguno · avisos: ninguno (corrido con `--marca "GeForce 256" --marca "Jensen Huang" --marca "RTX 5090" --respuesta 4000 --descripcion`) |
| `revision_humana` | **Pendiente**: que el video cumpla lo que el título promete (dice que Jensen Huang volvió, compara las dos tarjetas en transistores y aclara que no es velocidad), que no engañe y que pase la línea editorial (sin motivo, sin juicio). Firma el director creativo cuando exista el video |
| `medicion` | Visto frente a deslizado, mostrado en el feed y tráfico de búsqueda; a 7 y 28 días; meta: superar el 20,7 % del short 1 |

El título no lleva la cifra (4.000): es la respuesta del video. **Riesgo declarado:** la frase buscada es la noticia; el video es nostalgia con una cuenta. Por eso el video dice el hecho en los primeros 9 s y el título dice el objeto («GeForce 256 vs RTX 5090»); la persona que firma decide si basta.

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | 0 s (las 14 tomas son edición; 30,5 s se resuelven en edición) | 0 |
| Keyframes | 0 | 0 |
| Remates en resolución final | 0 | 0 |
| Voz (Tan con Zelda y Tin con Kevin, una generación por voz) | 2 generaciones, sin generar | ≈ 3,3 créditos estimados (≈ 0,8 + ≈ 2,5, por analogía con el short 2); cotizar con `estimate_audio_cost`; necesita el sí del dueño |
| **Total estimado** | 0 créditos en imagen y video; voz: ≈ 3,3 créditos por autorizar | 0 |

## 10. Restricciones críticas

Van al inicio de cada prompt de video, antes de la descripción. Son las que no se negocian.

```text
CRITICAL: no text, captions, subtitles, logos or watermarks unless listed in section 12.
CRITICAL: the character looks identical in every shot (same design, colors, proportions).
CRITICAL: hard cuts only, no morphing between shots.
CRITICAL: every figure, name or claim on screen comes from the project's facts file, with source and date.
CRITICAL: counters only go up and never pass their final value; no text over a character; no Nvidia logo, lettering or green; both cards are generic drawings with no logos; Jensen Huang is only named, never drawn; the video counts transistors and never says or shows speed, price or performance.
CRITICAL: no flashes: at most 3 sudden brightness changes in any second (target: zero); no negative-color effect, no go-through-the-scene transition.
```

## 11. Gancho, ritmo y cierre

- **Regla formal de la pieza:** una cuenta que es **una división entre dos objetos** (los transistores de la RTX 5090 entre los de la tarjeta de 1999) y un remate **de tamaño**; la cifra solo sube, y todo corte cae en un pulso de 0,5 s.
- **Rejilla de tiempo:** pulso de 0,5 s (los cortes); 61 pulsos = 30,5 s. La voz entra en el pulso 0 (fotograma 0). Los 10 cortes caen en 1,0; 2,5; 9,0; 11,5; 13,5; 16,5; 20,0; 24,0; 27,5 y 29,5 (más el bucle en 30,5); los planos continuos pasan por 6,0; 21,0 y 25,5 sin corte. Inicios estimados de la voz: 0,00; 2,55; 6,08; 9,31; 11,51; 13,61; 16,63; 20,28; 21,38; 22,73; 24,73 y 27,50. Cada corte cae de 0,0 a 0,25 s antes del inicio de la línea que le toca; el de 20,0 cae 0,03 s antes de que acabe la línea 7 y el de 24,0 cae dentro de la línea 10 a propósito (la pared aparece mientras Tan pregunta). Se revisan al oído con la voz real.
- **Gancho (0 a 2,5 s):** el fotograma 0 es la portada: la tarjeta de 1999 ya viene hacia la cámara y su ventilador gira, el texto «Jensen Huang / Is Back» ya entero, Tan y Tin debajo mirándola, y la voz de Tan ya diciendo «Remember putting one of these…» desde el fotograma 0. En 1,0 el `corte en el movimiento` pasa a las manos que meten la tarjeta en la ranura (el gesto que hicieron) y en 2,5 al plano de los dos con la tarjeta en su pedestal. Sin logo, sin título, sin segundo mudo. Una sola incógnita abierta: «¿cuántas de estas caben en una nueva?».
- **Empieza en movimiento:** sí: sin intro ni logo; la tarjeta crece hacia la cámara (ease-out: ya tiene velocidad en el fotograma 0), el ventilador gira y Tan y Tin rebotan al pulso.
- **Motivo visual que vuelve:** la tarjeta_1999 (tomas 1, 2, 3 a 5, 7, 9 a 10 en pequeña y 14), la tarjeta_actual (tomas 5, 8, 9 y 12) y el lápiz de Tin (tomas 3, 4 y 5). Se repiten con las mismas formas y colores.
- **Cierre:** firma del canal (toma 13: Tin y Tan saludan con el mismo gesto, Tan dice la invitación y aparece el nombre del canal) y luego `congelado_con_marco` que cae y deja el plano exacto del fotograma 0: el último fotograma es el primero. La voz termina en 28,80; silencio de voz en el empalme: 1,7 s (menos de 2 s).
- **Llamado a la acción:** **uno solo**: «Subscribe and count with us.», dicha por Tan en 27,5 a 28,8 s, corta y cálida; sin promesas ni recompensas. Por qué: el objetivo del dueño es entrar al Programa de socios y los suscriptores son uno de sus dos umbrales (`plan_programa_de_socios.md`, P6c); el short 1 dio 0 suscriptores sin pedirla.

Mapa de ritmo (los tiempos al décimo de segundo; cortes por segundo = cortes que caen dentro del tramo, sin contar el inicio):

| Tramo | Segundos | Pulso o intervalo | Cortes por segundo | Qué pasa (una acción) | Respiro |
|---|---|---|---|---|---|
| Gancho | 0,0–2,5 | 1,0 s y 1,5 s | 0,4 | la tarjeta viene hacia ti y las manos la meten en la ranura | no |
| Presentación | 2,5–9,0 | 6,5 s (un plano continuo) | 0,0 | la tarjeta en su pedestal; foco a Tin; el regreso del 23 de noviembre | sí |
| Pregunta y cuenta | 9,0–20,0 | 2,5 s; 2,0 s; 3,0 s y 3,5 s | 0,36 | la tarjeta nueva aparece; transistores, no velocidad; hasta 23 millones; 92.000 millones | no |
| Pico | 20,0–24,0 | 1,0 s y 3,0 s (continuos) | 0,0 | «Divide them», silencio, contador hasta 4.000+ | sí (cifra quieta 54 fotogramas) |
| Remate | 24,0–27,5 | 1,5 s y 2,0 s (continuos) | 0,3 | el muro de 4.000 tarjetas equivale a un chip | no |
| Cierre | 27,5–30,5 | 2,0 s y 1,0 s | 0,3 | firma, invitación, congelado y vuelta | sí |

Total: 10 cortes en 30,5 s. Densidad baja a propósito (la voz es continua y cada cifra necesita su plano); la densidad extra va dentro de cada toma (ventiladores que giran, profundidad que se mueve, contador, muro que se llena, una reacción de Tan por dato). Todas las líneas de Tan mueven una reacción distinta: nostalgia, curiosidad, sorpresa, asombro y risa.

Lo que sale se va antes de que entre lo siguiente: los textos salen 0,1 s antes del corte siguiente (el de la portada, en el corte de 1,0). El movimiento es mecánica: entradas con `pop` o `slide` (muelle), contadores con ease-out cúbico, rotación del ventilador lineal (es mecánica), sin interpolación lineal en lo vivo.

Tipos de plano disponibles y dónde van: detalle o macro (tomas 2, 6, 7 y 8), héroe abierto (tomas 3, 4, 5, 9 a 13; el principal es la 10, con la cifra), subjetivo (toma 2), revelado desde desenfoque (la tarjeta nueva, toma 5), objeto que salta sobre el mismo fondo (las dos tarjetas en las tomas 7 y 8). **No más de 3 destellos por segundo:** hay cero (no hay destello ni negativo; el barrido y el congelado pasan `efectos.comprobar_destellos`).

### Profundidad y efectos

Cada efecto sale de `manual/14_efectos_y_emocion.md` (la sección 7.1, y la 2.2, 2.4, 2.7 y 2.8 donde se dice). Procedimiento de 5 pasos: objetivo (Programa de socios) → emoción de ese segundo → punto de mirada → efecto de la tabla → métrica con su segundo. Las tres respuestas (emoción, punto de mirada, métrica) van en la tabla B. Sellos: **(inv.)** investigación, **(oficio)** oficio, **(hip.)** hipótesis del equipo (ver manual 14, sección 0).

**Tabla A — por toma: capas y z, foco, cámara, sombras, transición y efecto de acento**

| Toma | Capas y su z | Foco | Cámara | Sombras | Transición de entrada | Efecto de acento |
|---|---|---|---|---|---|---|
| 1 (0,0–1,0) | papel +900; Tan y Tin 0; tarjeta −100 a −290 | todo nítido (apertura 0) | fija | contacto bajo los pies; proyectada de la tarjeta | ninguna (bucle) | tarjeta que crece (12 f) y golpe de «Back» (f 6) |
| 2 (1,0–2,5) | papel +900; placa +60; tarjeta −120; manos −220 | z −120 | empuje con profundidad: avance 0 a 110 | proyectada de la tarjeta sobre la placa; contacto al asentar | `corte en el movimiento` | clic de inserción y rebote de 8 px |
| 3 (2,5–6,0) | papel +900; pc_beige +420 (niebla); tarjeta y pedestal −260; Tan y Tin 0; cable −320 | −260, y de 5,68 a 6,08 viaja a 0 | x 540 a 580, avance 0 a 90 | contacto bajo pedestal y pies | corte seco | cambio de foco (12 f) |
| 4 (6,0–9,0) | las de la toma 3 | 0 | continúa: avance 90 a 150, x 580 a 600 | las de la toma 3 | continúa | `pop` de «Nov 23» y de «Back as CEO» |
| 5 (9,0–11,5) | papel +900; tarjeta_1999 0; tarjeta_actual −200; Tan y Tin 0 | 0 | fija | proyectada de las dos tarjetas; contacto de los personajes | corte seco | revelado desde desenfoque de la tarjeta nueva (8 f) |
| 6 (11,5–13,5) | papel +900; die −100; Tan y Tin 0 | −100 | fija | proyectada del die | `borrón` | garabato: círculo de tinta (12 f) |
| 7 (13,5–16,5) | papel +900; tarjeta_1999 −150; Tan 0 | −150 | avance 0 a 70 | proyectada de la tarjeta | corte seco | `pop` del rótulo «23 million» |
| 8 (16,5–20,0) | papel +900; tarjeta_actual −150; Tan 0 | −150 | avance 0 a 70 | proyectada de la tarjeta | `barrido_obturador` (6 f) | `pop` del rótulo «≈ 92 billion» |
| 9 (20,0–21,0) | papel +900; ecuación 0; Tan y Tin 0 | 0 | fija | contacto de los personajes | corte seco | subida de sonido y silencio de 12 f |
| 10 (21,0–24,0) | las de la toma 9 | 0 | fija; golpe de zoom +10 % en la llegada | contacto de los personajes | continúa | contador, tomate y `pop` del «+» |
| 11 (24,0–25,5) | papel +900; pared 0; Tan y Tin 0 | 0 | fija | contacto de la pared (0,15) | corte seco | gráfico que crece (30 f) |
| 12 (25,5–27,5) | papel +900; pared encogida 0; tarjeta_actual 0; Tan y Tin 0 | 0 | fija | contacto | continúa | pliegue de la pared (36 f) y `pop` del «=» |
| 13 (27,5–29,5) | papel +900; Tan y Tin 0 | 0 | fija, 100 % | contacto bajo los pies | corte seco | saludo igual en todos los videos y `pop` de «Subscribe» |
| 14 (29,5–30,5) | a = la toma 13; b = el fotograma 0 | 0 | fija | contacto | `congelado_con_marco` (22 f) | foto con marco que cae |

**Tabla B — por efecto: las tres respuestas del manual (emoción, punto de mirada, métrica), su dosis y su respaldo**

| N.º | Efecto (herramienta) | Segundo y dosis | Emoción | Punto de mirada | Métrica | Respaldo y sello |
|---|---|---|---|---|---|---|
| 1 | **Objeto de época nítido que crece hacia cámara** (capa animada en z) — es el **único cambio grande del primer segundo** | 0,0–0,4 s; 12 f con frenada; de 600 a 760 px (70 % del ancho) | alerta leve y curiosidad | el centro de la tarjeta (540, 910) | visto frente a deslizado, contra el 20,7 % del short 1 | R4, R5 **(inv.)** para el mecanismo; R30 **(inv.)** para el objeto (los que tuvieron una en 1999 están en el pico de reminiscencia); que baje los deslizados: **(hip.)** |
| 2 | **Palabra clave con golpe en mostaza** (`palabra_clave`) más su golpe de sonido | f 6 a 18 (0,2–0,6 s); 5 f de ida, 7 de asiento; escala 1,0 a 1,18; el texto está entero desde el fotograma 0 y queda 30 f | énfasis | «Back» | visto frente a deslizado; retención al segundo 1 | R33, R10 **(inv.)**; R39 **(oficio)**. **Adaptación:** la portada exige el texto entero en el fotograma 0, así que la palabra no entra: da el golpe estando ya puesta |
| 3 | **Corte en el movimiento** | en 1,0 s, 4 f después de que la tarjeta arranca su descenso; el primer plano dura 30 f (≥ 20) | reorientación sin sobresalto | la tarjeta, que sigue bajando entre las manos | que no haya caída en 1,0–1,5 s | R14 **(oficio)**, R13 **(inv.)** (resumen), R11 **(inv.)** (resumen). **Desviación del manual:** el manual dice ≈ 0,7 s; aquí 1,0 s para respetar la rejilla de 0,5 s y para no cambiar el momento del primer corte respecto del short 2 (atribución del dato) |
| 4 | **Capas con paralaje y sombras de contacto** (`Capa`, `Camara`, `componer`, `sombra_contacto`) | 2,5–9,0 s; 3 capas y primer plano; cámara ≈ 1 % del ancho por segundo (límite 8 %) | presencia, atención tranquila; solidez | la tarjeta sobre el pedestal y luego Tin | retención de 2,5 a 9,0 s sin caída | R1, R3, R8 **(inv.)/(oficio)**; que se perciba más cuidado y se deslice menos: **(hip.)** |
| 5 | **Subjetivo o macro de las manos usando el objeto** | 1,0–2,5 s; 45 f sin cortes dentro de la toma | nostalgia sensorial, «yo estuve ahí» | los dedos dorados entrando en la ranura | compartidos por mil vistas; comentarios «yo también» | R21 **(oficio)**, R29, R30, R31 **(inv.)**; que lleve a enviarlo: **(hip.)** |
| 6 | **Cambio de foco** (`Camara.foco`) | de 5,68 a 6,08 s; 12 f; solo entre líneas de voz (la pausa de 0,40 s está diseñada para esto) | curiosidad que se resuelve | de la tarjeta a Tin | retención en 6,0 s | R9 **(oficio)**, R7 **(inv.)**; que la mirada siga al foco en un Short: **(hip.)** |
| 7 | **Revelado desde desenfoque** (`revelar_desde_desenfoque`), una vez | 9,3–9,57 s; 8 f (6 a 10) | anticipación breve | la tarjeta nueva a la derecha | retención en 9,3 s | R28 **(inv.)**; que lo borroso se lea como recuerdo: **(hip.)**. No va en el fotograma 0 |
| 8 | **Garabato que se dibuja** (`trazo_circulo`, `garabato`), uno solo | 11,95–12,35 s; 12 f; sin texto debajo | cercanía, curiosidad por el trazo | el die del chip | retención de 11,5 a 13,5 s | R28 **(inv.)**; R41 (poca prueba de que enseñe más): **(hip.)** |
| 9 | **Barrido de obturador**, una vez | 16,4–16,6 s; 6 f | energía, avance en el tiempo (de 1999 a hoy) | la tarjeta nueva que entra | que no haya caída en 16,5 s | cap. 02 **(oficio)**; riesgo R44 **(inv.)** (dentro del límite: 1 barrido, sin encadenar) |
| 10 | **El pico: subida de sonido, silencio de 12 f, contador que acelera y frena, un zoom de golpe suave, cifra quieta** (`contador`, `golpe_de_zoom`, `acercar`) | 20,1–22,2 s subida y silencio; contador 36 f; zoom +10 % (5 f + 8 f); cifra quieta 54 f; 73 % del video | anticipación y luego sorpresa y asombro | la cifra «4,000+» arriba a la izquierda | pico de retención hacia 22,2 s; compartidos por mil | R22 **(oficio)**, R28, R32, R34, R35 **(inv.)**. Solo zoom, sin destello (manual 7.1: «uno o el otro») |
| 11 | **Gráfico que crece** (la pared de 4.000 tarjetas) | 24,0–25,0 s; 30 f con frenada (20 a 40) | asombro por el tamaño | el centro de la pared | retención de 24 a 27 s; compartidos | R37 **(inv.)** (asombro ante lo mucho mayor); su uso en gráficos: **(hip.)** |
| 12 | **Cierre de firma con congelado con marco** (`congelado_con_marco`) y una sola invitación | 27,5–30,5 s; respiro de 60 f y congelado de 22 f | calidez, recuerdo de álbum, gratitud | Tin y Tan, y «Subscribe» | suscriptores por cada mil vistas | R26, R27, R34 **(inv.)**; R20 **(oficio)**; que una firma repetida convierta: **(hip.)** |
| 13 | **Acción secundaria continua y curvas con frenada** | todo el video: bufanda de Tan (`viento`), lápiz de Tin (±3 grados), ventiladores de las tarjetas | calidez, vida | los personajes | comentarios que nombran a Tin o a Tan; suscriptores | R22 **(oficio)**, R24 **(inv.)**; que el apego lleve a suscribirse: **(hip.)** |
| 14 | **Paso de neutro a acento** (mostaza y tomate) | la clave y un elemento por plano; el tomate solo de 22,2 a 27,4 s | foco y recordación; la cifra como golpe | la palabra o la cifra que lleva el acento | retención de los segundos 1 a 3 | R33 **(inv.)**; cap. 13 |

**Dosis y límites (manual 14, sección 6) que este video respeta:** 1 cambio de foco (máximo 1 cada 5 s); 1 revelado (máximo 2 por video); 1 barrido (máximo 2 para 45 a 70 años); 1 golpe de zoom de +10 % (máximo +35 %, y 1 para 45 a 70 años); 1 sola animación de acercamiento (máximo 2); cámara por debajo de ≈ 8 % del ancho por segundo y sin dos movimientos de cámara encadenados; cero destellos y cero negativos; **ningún «atravesar la escena»** (no hay un hueco natural en una tarjeta: la prueba obligó a ampliar ×33 y marcaba 3 cambios de luz en 0,15 s, en el límite; no aporta una emoción que el pico ya da); sin sombra tumbada de los muñecos; texto sin movimiento mientras se lee; el texto entra con `pop` y se queda 30 f o más (45 f para la cifra). **`efectos.comprobar_destellos` debe pasar** sobre los 915 fotogramas; el barrido y el congelado son los únicos tramos con cambios de luminosidad grandes y se miran fotograma a fotograma.

**Lo que se descarta de la lista de moda** (manual 14, 7.2) **y por qué:** estrobo (destellos, negativos a pantalla completa y cortes de menos de 8 f al pulso), subtítulos que saltan y cambian de color en cada palabra, y estética de aplicación (vidrio, degradados, neón, órbitas): ninguno está en este video. **Tampoco se usan** el negativo de paleta (una vez como máximo y solo sobre el objeto: se evita porque cuenta como destello y la prueba lo dejó para una firma que aquí es el congelado), el destello, la ráfaga de cortes (el público de 45 a 62 años; máximo 12 f por plano) ni la órbita (los muñecos son planos).

**Qué se espera medir y qué no se puede atribuir:** solo hay tres videos y los temas cambian; la comparación con el short 1 (20,7 %) y con el short 2 es orientativa, no una prueba. El único cambio del primer segundo es el 1, así que si el visto frente a deslizado cambia, la hipótesis principal es la tarjeta que crece; los demás efectos (2 a 14) se evalúan por la retención de su propio tramo. **Con profundidad, el porcentaje de color dentro de la paleta baja** (≈ 82 a 85 % esperado, contra el 93 % del short 2: el desenfoque y la niebla crean mezclas de tinta y papel que no están en la lista; la prueba midió 82 %); está anotado como esperado y se pide al supervisor que lo mida también sobre un fotograma nítido (por ejemplo el 0).

## 12. Texto en pantalla y sistema de diseño

- **Tipografías:** Inter Display Medium con sus **dígitos abiertos** (rasgo OpenType `ss01`, para todas las cifras de la pieza), licencia SIL Open Font License 1.1 (archivo `/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf`; en Windows, si no está, Segoe UI Semibold, que se anota en `licencias.md` antes de usarla). Contorno de las claves de 0,045 em, dibujando primero el trazo y encima el relleno. Subtítulos y rótulos **en minúsculas**, alineados a la izquierda; **excepción: la portada, con mayúscula inicial en cada palabra** (regla del dueño, `DESIGN.md`), y los nombres propios («Jensen Huang», «Nvidia», «GeForce», «RTX», «Tin & Tan», «Nov» y las siglas «CEO»), que llevan mayúscula inicial. Glifos comprobados el 2026-11-24 en la fuente: «≈», «÷», «=», «+», «–», «&», «,», «.», «:» y «?». No se usa la tipografía de ningún logotipo de la marca.
- **Paleta:** papel `#F3E9D2` · papel_sombra `#E6D8B8` · tinta `#2B2420` · naranja `#E07A2E` · marrón `#7A4B2A` · verde azulado `#2F7F7A` · mostaza `#E8B33B` (**acento único** de todos los planos salvo la revelación: palabra clave y un elemento) · tomate `#C8553D` (**acento solo de la revelación**, tomas 10 a 12: la cifra «4,000+») · rubor `#E9967A`. Un color de acento por plano; mostaza y tomate nunca comparten plano. La palabra clave en mostaza o en tomate lleva un trazo de tinta de 0,045 em. Los colores propios de los personajes no cuentan como acento. **Ningún verde de marca** (el verde azulado de Tan es identidad, no un verde de Nvidia). Detalle y razones en «Color con intención».
- **Referencias de movimiento:** `01_referencia/` está vacía (no hay video de referencia). Las referencias cargadas son `canales/nostalgia-tin-y-tan/DESIGN.md`, `herramientas/palitos.py` (1.3), `herramientas/efectos.py` (1.0), las hojas de `personajes/tin/referencias/` y `personajes/tan/referencias/`, el prompt del short 2 y `2026-11-23_prueba_efectos_tin_y_tan/07_revision/notas.md`; el movimiento lo definen los muelles de la sección 5.
- **Prohibido:**
  1. Mayúsculas centradas sobre degradado, tarjetas con degradado o cualquier fondo con degradado de relleno (el desenfoque de profundidad y la niebla de las capas lejanas **no** son degradados: son los de la prueba de efectos).
  2. Animaciones lineales de posición o escala de lo vivo (solo muelle o ease-out cúbico; lo mecánico —el ventilador que gira— sí es lineal).
  3. Texto de vidrio o paneles translúcidos, subtítulos que saltan o cambian de color por palabra, neón, órbitas: estética de aplicación (manual 14, 7.2).
  4. Un contador que retrocede o que se pasa de su valor final y vuelve (el rebote solo es de escala).
  5. Texto encima de un personaje o de la tarjeta, salvo las cifras que son el rótulo de un objeto en su zona de gráficos.
  6. Cualquier elemento de Nvidia: logotipo, letra del logo o de «GeForce» o «RTX» en su tipografía, el verde de marca, luces de color en las tarjetas; tampoco la cara de Jensen Huang, una caricatura, una silueta o su voz.
  7. Líneas sin suavizar: ningún dibujo fuera de un `Lienzo` o `LienzoCapa` con supermuestreo.
  8. Sombras tumbadas de los muñecos, resplandor, partículas, confeti, destellos y negativo.
  9. Subtítulos de más de 3 palabras o de más de una línea (los rótulos de objeto de las filas 8 y 9 llevan 4 palabras en dos líneas y se declaran: la aclaración «up to» no se quita, es lo que hace cierta la cifra), o fuera de la zona segura.
  10. Cualquier pose, expresión o vista que no esté en `palitos.py`, y cambiar los colores o accesorios de Tin y Tan (solo cambia el objeto de la mano: aquí solo el lápiz, o ninguno).
- **Márgenes seguros y escenario:** zona segura de `formatos.md`: x de 9,3 % a 90,7 % y y de 13 % a 87 %. Texto en x = 10 % y de 13,2 % a 24 %; personajes con pies a 86 % y cabeza desde 52 %; gráficos entre 27 % y 51 %. Excepción declarada: la portada (tomas 1 y 14) usa el texto entre y 415 y 690 por la regla del dueño.
- **Texto exacto:** todo texto en pantalla es el de la tabla de abajo, letra por letra. Los contadores muestran enteros entre su valor de inicio y su valor final.
- **No afirmar:** ninguna cifra ni dato fuera de la tabla «Datos del video» del brief, verificados el 2026-11-24:
  - **La junta de Nvidia repuso a Jensen Huang como presidente y director ejecutivo el 23 de noviembre de 2026** (Wikipedia en inglés, «Jensen Huang», y títulos de cadenas en YouTube; el comunicado de Nvidia no se pudo abrir).
  - **GeForce 256: lanzada el 11 de octubre de 1999; 17 millones de transistores según «Transistor count», ≈ 23 millones según la prensa de 1999** (esta cifra solo se vio en un resumen de buscador). **RTX 5090 (GB202): 92.200 millones de transistores; a la venta desde el 30 de enero de 2025.**
  - **La cuenta: 92.200 millones ÷ 23 millones ≈ 4.009; ÷ 17 millones ≈ 5.424; se dice «más de 4.000».** (cálculo, comprobado con Python).
  - **No decir ni mostrar:** rendimiento («4.000 veces más rápida» es falso; la cuenta es de transistores y el video lo dice dos veces), precio, bolsa, fortuna, motivo de la renuncia o del regreso, nada de la vida privada ni de investigaciones, los «11 días», nada del gobierno de EE. UU., que Jensen Huang diseñó la tarjeta o que dirigía la empresa en 1999, que la RTX 5090 es «la más potente» o «la más grande» (ningún superlativo), que «hoy» el chip de Nvidia con más transistores es ese (los de centros de datos tienen más), y ninguna cifra de 5.424 en pantalla.
- **Subtítulos:** de 1 a 3 palabras (salvo los dos rótulos declarados), con la palabra clave en mostaza (con trazo de tinta); en la revelación (tomas 10 a 12) la cifra va en tomate con trazo de tinta y no hay mostaza como acento. Cifras del valle al 7 % del alto.

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| Jensen Huang / Is Back (2 líneas; clave: Back; ya entero en el fotograma 0, sin pop; es la portada; mayúscula inicial en cada palabra) | 0,0 | 1,0 | 10, 21,6 | 6,7 |
| GeForce 256 (clave: 256) | 2,7 | 4,3 | 10, 14 | 7 |
| 1999 (clave: 1999) | 4,4 | 5,9 | 10, 14 | 7 |
| Nov 23 (clave: 23) | 6,2 | 7,5 | 10, 14 | 7 |
| Back as CEO (clave: CEO) | 7,6 | 8,9 | 10, 14 | 7 |
| RTX 5090 (clave: 5090) | 9,4 | 11,4 | 10, 14 | 7 |
| transistors, / not speed (2 líneas; clave: transistors) | 11,6 | 13,4 | 10, 14 | 5,5 |
| up to / 23 million (2 líneas; «up to» al 4,5 %; clave: 23) | 13,6 | 16,4 | 10, 14 | 7 |
| RTX 5090 / ≈ 92 billion (2 líneas; «RTX 5090» al 4,5 %; clave: 92) | 16,6 | 19,9 | 10, 14 | 7 |
| ≈ 92 billion (en la ecuación, fila 1; tinta, sin clave) | 20,1 | 23,9 | 38,5, 31,3 | 5,5 |
| ÷ 23 million (en la ecuación, fila 2; tinta, sin clave) | 20,2 | 23,9 | 9,3, 40 | 5,5 |
| 4,000+ (contador de 250 a 4,000; en tinta mientras sube, al llegar el número en tomate con trazo de tinta y el «+» con pop) | 21,0 | 27,4 | 10, 14 | 7 |
| transistors, not speed (subtítulo fijo bajo la cifra, tinta) | 21,4 | 27,4 | 10, 22 | 3,5 |
| = (signo entre la pared y la tarjeta; tinta) | 26,7 | 27,4 | 50, 39 | 5,2 |
| Subscribe (clave: Subscribe entera) | 27,7 | 29,4 | 10, 14 | 7 |
| Tin & Tan (tinta; nombres propios con mayúscula) | 27,7 | 29,4 | 10, 22 | 3,8 |
| Jensen Huang / Is Back (en el plano b del congelado; entero; bucle) | 29,9 | 30,5 | 10, 21,6 | 6,7 |

### Color con intención

Propuesta del prompt (regla del dueño, 2026-11-21; `manual/13_color_con_intencion.md`, sección 6). La sección equivalente de `02_prompt/direccion.md` la escribe el director de fotografía y la valida el director creativo; este bloque es la propuesta del prompt y, si difiere, manda la dirección.

- **Neutros (2):** papel `#F3E9D2` (fondo de todos los planos y suelo `#E6D8B8`) y tinta `#2B2420` (líneas, contornos y todo texto que no sea clave). Contraste tinta/papel 12,6:1; tinta/papel_sombra 10,8:1 (los dos pasan 7:1).
- **Acento (1):** mostaza `#E8B33B`, siempre con contorno de tinta, solo en la palabra clave y en **un** elemento por plano (los dedos dorados de la tarjeta, el lápiz de Tin o el chip, según la toma). **No va** en: texto que no sea clave, personajes (su bufanda y lápiz son identidad), suelo, pared de tarjetas (marrón) ni en los planos de la revelación. **Tomate `#C8553D` queda reservado a la revelación** (tomas 10 a 12: la cifra «4,000+») y nunca comparte plano con la mostaza. Marrón `#7A4B2A` solo como relleno (placa de la tarjeta, minitarjetas, dedos en la revelación), nunca como texto. **Ningún verde** salvo el verde azulado de Tan (identidad).
- **Por qué esta paleta:** papel crema y tinta marrón remiten a impresos y fotos de los 70 y 80, y las placas marrón y los dedos dorados, a una PC de 1999 vista con cariño: nostalgia cálida y de saturación baja para el público de 45 a 62 años de EE. UU., que se lee bien con su vista. La mostaza lleva el ojo al dato; el tomate, guardado para el final, hace que «más de 4.000» se sienta como un golpe de emoción (hipótesis, no significado fijo). Se evita a propósito el verde de Nvidia: no es la marca la que habla, es la tarjeta del recuerdo.
- **Cómo ayuda al objetivo:** Programa de socios → la misma paleta y el mismo acento de los shorts 1 y 2 hacen que el canal se reconozca antes de leer el nombre, y el paso de mostaza a tomate marca el pico en 22,2 s → se verá con la retención del segundo 1 al 3, visto frente a deslizado, y los suscriptores por mil vistas.
- **Riesgos de lectura:** (1) mostaza sobre papel da 1,6:1: solo se lee por el contorno de tinta; (2) tomate sobre papel da 3,6:1 y tinta sobre tomate 3,5:1: la cifra se lee por su contorno, por ser texto grande y por la posición, se revisa en teléfono; (3) rojo contra verde: la cabeza verde azulada de Tan y el tomate no llevan la información; (4) **con profundidad, el desenfoque y la niebla bajan el porcentaje en paleta** (la prueba midió ≈ 82 %; el plano nítido, 91 %): es lo esperado y no un error; (5) pantalla chica: cifras al 7 % del alto; (6) Tan conserva su bufanda mostaza en la revelación (identidad, no acento): se vigila que no se lea como segundo acento.
- **Medido:** pendiente (no hay video). Se pide al supervisor correr `revisar_color.py` sobre el video, sobre el fotograma 0 y sobre el tramo de 21,0 a 27,5 s por separado, y anotar el porcentaje con y sin desenfoque (umbral de la herramienta 85 %: se espera un aviso explicado, no un error).

Tabla de acento por plano:

| Toma | Mostaza (palabra clave + un elemento) | Tomate |
|---|---|---|
| 1 | «Back» + dedos de la tarjeta | no |
| 2 | dedos de la tarjeta (sin texto) | no |
| 3 | «256» y luego «1999» + lápiz de Tin | no |
| 4 | «23» y luego «CEO» + lápiz de Tin | no |
| 5 | «5090» + dedos de la tarjeta de 1999 | no |
| 6 | «transistors» + el chip | no |
| 7 | «23» + dedos de la tarjeta | no |
| 8 | «92» + dedos de la tarjeta nueva | no |
| 9 | ninguno (neutros) | no |
| 10 | ninguno | cifra «4,000+» |
| 11 | ninguno | cifra «4,000+» (sigue) |
| 12 | ninguno | cifra «4,000+» (sigue) |
| 13 | «Subscribe» | no |
| 14 | «Back» + dedos de la tarjeta (plano b, como en la toma 1) | no |

Contrastes (medidos en el short 2 con `revisar_color.py --contraste`, 2026-11-21, mismos colores): tinta/papel 12,6:1; tinta/papel_sombra 10,8:1; tinta/mostaza 8,0:1; tinta/tomate 3,5:1; mostaza/papel 1,6:1; tomate/papel 3,6:1; marrón/papel 6,1:1.

Campo para `ficha.json`:

```json
"color": {"neutros": [
            "#F3E9D2",
            "#2B2420"
          ], "acento": "#E8B33B",
          "por_que": "papel crema y tinta de impresos de los 70 y 80 (nostalgia cálida, saturación baja) para un público de 45 a 62 años de EE. UU.; la mostaza lleva el ojo al dato y el tomate se reserva a la cifra del pico (tomas 10 a 12), nunca junto a la mostaza; sin el verde de Nvidia",
          "objetivo": "Programa de socios: misma paleta y acento en todo el canal para reconocerlo; mostaza a tomate marca el pico; métrica: retención del segundo 1 al 3, visto frente a deslizado y suscriptores por mil vistas",
          "medido": "pendiente: el porcentaje en paleta baja con profundidad (≈ 82 a 85 % esperado); se mide también el fotograma nítido"}
```

En un short, todo texto queda dentro de la zona segura de `formatos.md`. Entrada de cada texto: `pop` con escala de 0,85 a 1 en 8 fotogramas; salida: subir 2 % con ease-in en 3 fotogramas (excepciones: la fila 1 en el fotograma 0 está ya a escala 1; la última fila llega entera con el plano b y queda a escala 1 en el último fotograma para que el bucle empalme).

## 13. Sonido

Los golpes bajo la voz van a unos **−26 LUFS** (−12 dB respecto a la voz, que está a −14 LUFS; lección del short 1: a −38 LUFS no se oían en un teléfono). Cada corte y cada efecto llevan su sonido atado al fotograma (±1 f; `manual/14`, 2.8). **Nadie ha oído nada: se comprueba al oído.** Variación respecto del short 2: no hay clics de botón al pulso ni el zumbido del mando; hay un zumbido de ventilador que sube de tono, un ding de campana más grave y una cascada de tics.

| Golpe o efecto | Segundo | A qué corte o efecto va atado | Origen y licencia |
|---|---|---|---|
| Thunk grave de 80 ms y zumbido de ventilador que sube de tono (0,0 a 0,4 s) | 0,0 | arranque, toma 1: la tarjeta que crece (es también el empalme del bucle: no se duplica) | código, propio (ver licencias.md) |
| Tic seco de énfasis | 0,2 | golpe de la palabra clave «Back» (f 6) | código, propio |
| Clic suave y soplo corto | 1,0 | corte en el movimiento, toma 1 a 2 | código, propio |
| Clac seco de inserción | 2,2 | la tarjeta asienta en la ranura, toma 2 | código, propio |
| Clic suave | 2,5 | corte de toma 2 a toma 3 | código, propio |
| Pop | 2,7 y 4,4 | textos «GeForce 256» y «1999» | código, propio |
| Soplo de aire de 12 fotogramas | 5,68–6,08 | cambio de foco de la toma 3 a Tin | código, propio |
| Pop | 6,2 y 7,6 | textos «Nov 23» y «Back as CEO» | código, propio |
| Clic suave | 9,0 | corte de toma 4 a toma 5 | código, propio |
| Zumbido corto de 8 fotogramas que se aclara | 9,3 | la tarjeta nueva aparece desde el desenfoque | código, propio |
| Pop | 9,4 | texto «RTX 5090» | código, propio |
| Clic suave de borrón | 11,5 | corte de toma 5 a toma 6 | código, propio |
| Pop | 11,6 | texto «transistors, not speed» | código, propio |
| Rasguño de lápiz sobre papel | 11,95–12,35 | el garabato que rodea el chip | código, propio |
| Clic suave | 13,5 | corte de toma 6 a toma 7 | código, propio |
| Pop | 13,6 | rótulo «up to 23 million» | código, propio |
| Whoosh de 6 fotogramas y golpe seco | 16,4–16,6 | barrido de toma 7 a toma 8 | código, propio |
| Pop | 16,6 | rótulo «≈ 92 billion» | código, propio |
| Clic suave | 20,0 | corte de toma 8 a toma 9 | código, propio |
| Subida (riser) de 25 fotogramas | 20,15–20,98 | antes de la cifra, bajo «Divide them.» | código, propio |
| **Silencio total de 12 fotogramas** (voz, música y efectos) | 20,98–21,38 | justo antes del contador | código, propio |
| Tictac de contador que sube de tono | 21,38–22,2 | contador de la toma 10 (calla al llegar) | código, propio |
| Ding de campana grave y golpe seco; vuelve la música | 22,2 | primer fotograma con el valor final: el mismo fotograma que el tomate, el «+», el `pop` y el golpe de zoom | código, propio |
| Clic suave | 24,0 | corte de toma 10 a toma 11 | código, propio |
| Cascada de tics que sube de tono (50 filas) | 24,0–25,0 | la pared de 4.000 tarjetas que crece | código, propio |
| Whoosh suave | 25,5–26,5 | la pared se encoge y la tarjeta nueva entra | código, propio |
| Clic y pop | 26,7 | la tarjeta se asienta y entra el signo «=» | código, propio |
| Clic suave | 27,5 | corte de toma 12 a toma 13 | código, propio |
| Pop | 27,7 | texto «Subscribe» y «Tin & Tan» | código, propio |
| Clic de obturador de cámara | 29,5 | el cierre se congela como foto, toma 13 a 14 | código, propio |
| Thunk grave idéntico al del segundo 0,0 (cierra el bucle; el del 0,0 lo continúa) | 30,5 | bucle: es el del segundo 0,0 de la vuelta siguiente (el archivo dura 30,5 s justos y no lo duplica) | código, propio |

- **Música:** hecha con código a −24 LUFS (ver sección 7); sin material de terceros.
- **Voz:** sí (por generar; ver sección 7). Sin retraso: empieza en el fotograma 0.

## 14. Motor y revisión

- **Cómo se hace:** gráficos por código (fotograma a fotograma): Python, Pillow, numpy y ffmpeg. Cada plano se compone con `efectos.componer` (capas con `z`, cámara con foco y niebla) y los personajes se dibujan con `palitos.dibujar(lz, id, x, suelo, alto, pose, expresion, vista, mira, viento, objeto, espejo, cabeza_giro)` en un `LienzoCapa` con supermuestreo. Todo depende del número de fotograma, no del reloj. Se guardan PNG numerados y ffmpeg los une con la voz y los efectos. Costo de render estimado con la prueba de efectos (≈ 10 s de reloj por segundo de video con profundidad, 4 procesos): **≈ 5 a 6 minutos para los 915 fotogramas**.
- **Qué hay que añadir al código (nada de esto existe todavía; costo en créditos: 0):**
  1. `herramientas/palitos.py` **no cambia** (los dos personajes y sus poses son los de la versión 1.3; `git diff` debe quedar vacío, igual que en la prueba de efectos).
  2. Gráficos nuevos en `codigo/render.py` del proyecto (o, si el equipo los reutiliza, en `efectos.py`): `tarjeta_1999(marco, ancho, dedos, giro_ventilador)` y `tarjeta_actual(marco, ancho, dedos, giro_ventiladores)` (secciones 5), `pc_beige(marco)` (torre y monitor), `placa_base_y_ranura(marco)`, `manos_de_palitos(marco, posicion)`, `die(marco, lado)`, `pared_de_tarjetas(marco, filas_visibles)` y `ecuacion(marco, ...)`; también el `pedestal` y el cable de primer plano. Sin ningún logotipo, letra ni verde.
  3. Planos por capas con `efectos.Capa`, `Camara` (con `foco` animado entre las líneas de voz, `apertura`, `campo`, `niebla`), `componer`, `revelar_desde_desenfoque`, `barrido_obturador`, `congelado_con_marco`, `golpe_de_zoom` (con `acercar(img, zoom, centro)` para que el zoom salga de la cifra), `trazo_circulo` y `garabato`, `contador`, `sombra_contacto`, `sombra_proyectada`, `papel`. No hace falta tocar `efectos.py`; si el zoom con origen en la cifra no sale limpio con `acercar`, se añade un parámetro `centro` a `golpe_de_zoom` y se anota en el encabezado de versiones.
  4. `codigo/audio.py` (copia del del short 2): los golpes de la sección 13, la música en re dórico, el silencio de 12 fotogramas y el armado del diálogo con las dos pausas de 0,40 s; `codigo/miniatura.py` para la portada.
  5. Comprobar al arrancar el render los glifos «≈», «÷», «=», «+», «–» y «&» (ya comprobados con la fuente instalada el 2026-11-24) y `la opción de fuente ss01 de Pillow (features con ss01)` (necesita libraqm: disponible).
- **Quién renderiza y autorización:** el render lo hace el equipo de producción (0 créditos). **La voz necesita el sí del dueño con la cotización.** Antes de renderizar se llena `03_keyframes/definicion.md` (hecho en borrador: pieza por código y las dos voces) y se anotan la fuente y la licencia de cada recurso en `licencias.md`.
- **Punto de control:** antes de generar la voz o renderizar se presenta la lista de tomas sobre la rejilla y se espera el visto bueno del dueño o la decisión del equipo según `CLAUDE.md`; con la voz real se reajustan los tiempos y se vuelve a archivar el prompt.
- **Revisión:** prueba corta de 5 s (de 0,0 a 5,0: portada, tarjeta que crece, manos, plano con capas y el cambio de foco), un fotograma por pulso, hoja de contacto y comprobación de medidas (zona segura, `alto` y x de cada personaje, pies a 86 %, tarjeta dentro de y 720 a 1100 en los fotogramas 0 y 12, texto de la portada entre y 415 y 690 a 40 px o más de la tarjeta, caras dentro de la zona útil). Después del render completo: `efectos.comprobar_destellos` (debe pasar; informe en `07_revision/`), `postpro.py destellos`, `herramientas/revisar_fotogramas.py`, `analizar_video.py <video> <carpeta> --cada 0.5` y `revisar_color.py` (video, fotograma 0 y tramo 21,0–27,5 s; se espera un aviso por el desenfoque, explicado), `revisar_texto.py --idioma en` sobre `subtitulos.srt`, el código del render, la descripción y las etiquetas, `revisar_titulo.py` sobre el título y `revisar_voz.py` sobre la mezcla (guion contra lo que se oye). Se comprueba al oído que cada corte cae donde dice la sección 6 con la voz real, que la voz arranca en el fotograma 0, que los golpes se oyen bajo la voz, el silencio de 12 fotogramas y que «G Force», «R T X fifty-ninety» y «Nvidia» suenan bien.
- **Qué se marca:** imagen congelada, fotograma vacío (la mitad de abajo no debe quedar vacía), texto cortado o tapado, texto que sigue sobre el plano siguiente, elemento fuera de cuadro, tirones, contador que retrocede o que se ve en «0», glifos cuadrados, el fotograma 915 (el que sigue al último) distinto del 0, más de 3 destellos por segundo, **caras borrosas mientras su personaje habla** (el foco solo cambia entre líneas), una tarjeta que se parezca a una comercial o lleve logotipo, letra o verde, cualquier cosa que recuerde a Nvidia o dibuje a Jensen Huang, expresiones que se lean como enojo, y en el teléfono: que la tarjeta, los rótulos y la cifra se lean y que cada dato lleve una reacción de Tan distinta. Nota para el validador: en las tomas con personajes (1, 3 a 6 y 9 a 14), el bloque de identidad de la ficha no se pega en el prompt porque no hay generador de imágenes; el diseño oficial es el código de `palitos.py` y se comprueba con la lista de comprobación de cada ficha.
- **Vueltas:** las correcciones por código son gratis (salvo servicios de pago, que van a `costos.md`); **las de generador no se repiten sin autorización del dueño** (`generacion.md`). Aquí solo hay generador en la voz: una generación por voz, sin segundos intentos.
