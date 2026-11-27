# Prompt de video para redes — Is GTA 6 Coming to PC? Here's What's Announced

> **ESTADO (2026-11-27, versión 1):** especificación de producción del short 5 de Tin & Tan (`TIN-EN-S-005`, hueco H02 de la tanda 01, «primer pago»), escrita por el director de prompts sobre `00_brief.md` (cerrado), `02_prompt/direccion.md` (secciones 1 a 11, ya unidas) y `perfil_emocional.md`. **Manda la dirección y, donde un oficio contradice a otro, su sección 11 («Reconciliación entre oficios»).** Cada toma de abajo es un plano (P1 a P25) de su sección 3.2, con los cortes ajustados de 11.2 l, los fotogramas y la coreografía de la sección 4, el sonido de la 5, la voz y los textos de la 2.2. **La voz no está generada** (estimada en ≈ 2,6 a 3,0 créditos, sin cotizar ni aprobar) y **los fotogramas son un plan con la voz estimada**: se recalculan con la voz real, sin mover los desfases dentro de cada golpe ni las reglas de 2.1 de la dirección. El video no está renderizado.

> **Cómo se produce:** no hay generador de video ni de imágenes. El video se dibuja y se graba por código con el motor de acción (`video-studio/motor_de_accion/`: escena 3D con Tin, Tan y el rival como dibujos 2D de pie dentro del mundo) y se arma con la voz, los sonidos y la música. Por eso todas las tomas son «edición» y, en lugar de «Prompt de keyframe» y «Prompt de video», cada toma lleva su frase de cámara y su actuación en inglés, que son las que van al guion del motor. El bloque de identidad de cada ficha no se pega en tomas: el diseño oficial es el código (`palitos.py`, cabezas exportadas por `exportar_sprites.py` y la hoja v2 del rival) y se comprueba con la lista de comprobación de cada ficha. Por no haber keyframes ni clips generados, `03_keyframes/definicion.md` no aplica a este video (lo único que se genera es la voz).

> **Notas del director de prompts (contradicciones y huecos encontrados; ninguna cambia una frase de voz, un dato ni lo que el video no afirma):**
> 1. **Reconciliación entre oficios.** Los choques entre fotografía, animación y sonido están en la sección 11 de la dirección, con su dueño. Aquí se aplican así: el lado del farol queda **sin resolver** (se dibuja a la derecha del cuadro, como fija fotografía, hasta que animación y fotografía lo cierren); el tamaño de los personajes (≈ 18–19 % del alto) y el rival grande por profundidad quedan **pendientes de validar por el director creativo**; el lila del rival, **pendiente del dueño**; el cian frente a los colores de las marcas, **pendiente del supervisor**.
> 2. **Cortes ajustados a los K.** Se usan los cortes de fotografía con tres ajustes (f148, f198 y f502) para que cada choque de animación caiga dentro del plano de su golpe. Siguen siendo 25 planos y 24 cortes.
> 3. **Efectos bajo la voz.** Ningún efecto tapa una cifra o un nombre dicho: la grieta bajo «GTA 6» y la implosión bajo «No official PC date» se bajan de nivel (no se mueve ni la imagen ni la voz). Se comprueba con `revisar_voz.py` y de oído.
> 4. **Voz: solo puntuación cambia.** El texto para generar lleva dos cambios de puntuación respecto de 2.2 (coma antes de «and Xbox» y comas en lugar de comillas simples en «GTA 6 for PC»); las palabras son las mismas.
> 5. **Pista `.srt`.** No se sube ninguna pista `.srt` a YouTube (regla del dueño del 2026-11-26): los subtítulos en español van quemados en la imagen. No hay `subtitulos_es.srt` en este proyecto.
> 6. **Sello de fecha.** «as of» y la fecha de la relectura del día de publicar se escriben ese día; hasta entonces es el único texto sin fecha cerrada, y es código.
> 7. **Publicación.** Título, descripción y etiquetas están en `publicacion.md` (comercial). Este prompt no los toca.

## 1. Ficha técnica

- **Proyecto:** 2026-11-26_tin_y_tan_gta_6_on_pc
- **Tipo:** short
- **Número:** 5
- **Serie:** ninguna
- **Objetivo de aprendizaje:** no aplica
- **Generador:** ninguno: dibujo y grabación por código con el motor de acción (three.js grabado con Chromium, `palitos.py`, `efectos.py`, sonidos de `sonidos/sonido.py`) y armado con ffmpeg. Lo único que se genera es la voz (Higgsfield `seed_audio`: Kevin para Tin y Zelda para Tan)
- **Aspecto:** 9:16
- **Duración total:** 31 s (930 fotogramas a 30 f/s; tolerancia 29 a 32 s; se recalcula con la voz real)
- **Resolución de borrador:** 540x960 a 30 f/s; prueba corta de 5 s con un fotograma por pulso (render propio)
- **Resolución final:** 1080x1920 a 30 f/s, H.264, 930 fotogramas
- **Precio por segundo:** 0 (render propio; no hay servicio de pago de imagen ni de video)
- **Intentos estimados por toma:** 1
- **Código previsto:** TIN-EN-S-005 (hueco H02 de la tanda 01; segundo video del formato de acción; primer pago del universo)
- **Objetivo comercial (dueño, 2026-11-23):** entrar al Programa de socios de YouTube lo antes posible. KPI: «se quedó a mirar» a 48 horas no más de 5 puntos por debajo del short 4 a la misma edad (si el short 4 no está público, contra el short 2).
- **Voz:** una generación por personaje, estimada por sonido en ≈ 2,6 a 3,0 créditos (Tin ≈ 2,0 a 2,3 y Tan ≈ 0,6 a 0,7). **Es una estimación, no una cotización, y no está aprobada:** no se genera sin el sí del dueño con el número a la vista.
- **Publicación prevista:** YouTube Shorts, viernes 2026-12-04, 16:00, hora de El Salvador.

## 2. Elenco

| Personaje | Papel en este video | Vestuario | Referencia que se sube |
|---|---|---|---|
| @tan | Pregunta («Is GTA 6 coming to PC?» y «How long last time?»), atrapa el lápiz en f10, embiste de hombro (golpe 2), da la estocada con la regla (golpe 5), invita a suscribirse, mira el objeto que cae 6 fotogramas y da el consejo «Don't download them.»; lanza el lápiz en el cierre. Voz: Zelda al 110 % | Base de su ficha (rodete y bufanda mostaza); `lapiz` solo en los planos de firma y desde f862; `regla_de_tinta` cuando la recibe | personajes/tan/referencias/principal_tin_y_tan.png |
| @tin | Responde con las líneas del brief; empuja (golpe 1), patea (golpe 3), dibuja la `regla_de_tinta` con el lápiz y la usa (golpes 4 y 6), frena la mano de Tan con la regla (bloqueo) y toca el paquete con la punta (el toque). Nunca golpea con el lápiz. Voz: Kevin al 110 % | Base de su ficha (gorra marrón, lentes, lápiz); **sin lápiz** en los planos de firma (f0–f29 y f900–f929); `regla_de_tinta` | personajes/tin/referencias/principal_tin_y_tan.png |
| @duda | El rival: la pregunta hecha cuerpo. Sale de una grieta del suelo (f30), crece a 1,5 veces, falla su contraataque, baja un escalón con cada dato, cambia de táctica y dibuja un paquete que revienta, queda chamuscado y no se borra del todo. Sin nombre en pantalla, sin voz, sin boca | Versión 2: cuerpo de palitos de tinta, madeja como cabeza con rizo de pregunta sin punto y dos huecos de papel por ojos. **En la hoja Noche la tinta es lila `#B79CFF` con hollín `#0B0F1F`** (decisión de fotografía, 11.1 k; **pendiente del dueño**) | personajes/duda/referencias/hoja_v2_2026-11-26.png |

No se sube nada a un generador: las referencias son el diseño en código y solo sirven para comparar. **Ninguna persona real aparece ni se nombra.** Marcas solo nombradas (voz y capa de datos): GTA, Rockstar, PlayStation, Xbox, Red Dead Redemption 2, Malwarebytes y Huntress. «La Duda» es el nombre de trabajo del equipo: no se dice ni se escribe en el video, en la voz, en los subtítulos, en el título ni en la portada. Poses del motor usadas: las de 4.13 de la dirección (`quieto`, `guardia`, `carga`, `golpe`, `embiste`, `patada`, `recibe`, `vuela`, `caido`, `agachado`, `sentado`, `susto`, `esquiva`, `bloqueo`, `dibuja`, `pregunta`, `invita`, `atrapa`, `mazoArriba`, `mazoAbajo`, `corre_arma`, `camina`), más las nuevas de la sección 7 de la dirección; poses de Tan de la ficha (`pregunta`, `saluda`); expresiones: `curiosidad`, `pensando`, `sorpresa`, `feliz`, `eureka`, y `concentrado` solo en las pausas de 6 fotogramas (se lee como enojo: nunca en un dato). Tin y Tan miden ≈ 340–360 px (18–19 % del alto); el rival entra a 1,25 veces su altura y crece a 1,5 **por profundidad** (carril más lejano), no por altura (11.1 b).

## 3. Idea en una línea

La pregunta «¿GTA 6 va a salir en PC?» sale del suelo como un rival de tinta enorme, Tin la tumba con la respuesta oficial antes del segundo 4, y como no se rinde, la miden contra las dos esperas anteriores con una regla de tinta; cuando cambia de táctica y ofrece una caja lisa de tinta, nadie la abre: revienta sola. Queda sin fecha oficial, y por eso no se borra del todo. Quien lo ve debe sentir curiosidad en el arranque, tensión que sube con cada golpe, sorpresa en el paquete que revienta y alivio con humor seco al final, y salir sabiendo qué hacer con un archivo que dice ser «GTA 6 para PC».

## 4. Estilo global

Bloque que se pega igual al final de toda descripción de plano que se pase al motor.

```text
Flat 2D ink drawing: 2D stick-figure characters standing inside a real 3D night loading yard seen with depth and parallax, low camera angles in diagonal. Two neutrals plus one accent: night blue (#141B33 sky and far walls, #27304F ground, #3A4570 near blocks, #1C2444 far blocks, #5A6690 dust, #0B0F1F shadow) and paper cream (#F3E9D2) for the outline of every body, weapons, text and cardboard marks; ONE accent, cyan #4FE3FF, only as a plate behind the key word or figure of a data card. The ink figure is lilac #B79CFF with soot #0B0F1F after the blast. Tin keeps his orange head (#E07A2E), Tan her teal head (#2F7F7A), mustard scarf and pencil (#E8B33B): identity colors, not accents. Light comes from one street lamp as a cold pool on the ground with a hard drawn edge, no gradients; the world far away gets no light. Contact shadows #0B0F1F at 0.55 opacity. Fire is flat, in two hard-edged tones (core #FFE45C, edge #B81414) built in phases and is the only warm light; smoke is #9A6A45 with a #0B0F1F outline and always behind Tan; cardboard is #9A6A45. Impacts are drawn in the same shot, never camera shake. Hard cuts, fixed cameras or slow push-ins and lateral drifts under 8 percent of the width per second, no gradients on shapes, no glow, no neon.
```

**Negativo global:**

```text
any text, logo, box art or typography inside the 3D world, any image, character, logo, typeface, color scheme or music from the game, any real person, any unofficial port, leak, download page, file icon, window or arrow, firearms or firearm silhouettes, blood, red on the ink figure, brown or gray on the ink figure other than soot, gradients on shapes, glow, neon, lens flare, camera shake, zoom, whip pan, strobing, pure white over the whole frame, negative-color frames outside the two masked ones, cyan on characters, weapons, fire, smoke or the world, yellow or orange fire colors outside the two fire tones, blurry particle fire, extra characters, extra fingers, uppercase centered titles, photographs, a mouth or pupils on the ink figure, a third bar, an empty bar, a dotted bar, an arrow or a plus sign on the measures card
```

## 5. Escenarios

- **patio_tienda_de_computadoras** (entorno nuevo; entra al catálogo del motor con los temas tecnología, hardware y compras): patio de carga exterior de una tienda de computadoras, de noche, sin logotipos, sin texto, sin arte en las cajas y sin figuras humanas. Hoja Noche, paleta B (`motor_de_accion/paletas/b_noche_de_tinta.json`). Luz principal: un farol con poste, cuya lámpara es el único punto de máxima luminosidad; su luz es un óvalo frío sobre el suelo con borde duro (no luz real: los personajes no cambian de color). Al inicio está entero; al final conserva todos los daños. Piezas con nombre de catálogo y qué les pasa:

| Pieza (nombre de catálogo) | Dónde | Qué le pasa | Queda así |
|---|---|---|---|
| `pila` de torres con monitor apagado | Centro, entre los carriles de pelea y de fondo (y 720–1100 en la portada) | Golpe 1 (f100–f101): cede la torre de abajo; el monitor se inclina 10° | `torre_de_pc_rota`; la torre de encima cae en f262–f270 (`torre_de_pc_caida`) |
| `cajas_der` (pila de cartón) | Fondo, a la derecha de la pila | Golpe 2 (f146–f147): 5 cajas aplastadas | `cajas_de_carton_rotas` |
| `monitores` (3 sobre un palé) | Fondo, a la izquierda | Golpe 3 (f226–f227): uno revienta en estrella | `monitor_roto` |
| `farol` con poste y lámpara | Lado derecho del cuadro (provisional, 11.1 a2): lámpara x ≈ 700–860, y ≈ 560–640; poste x ≈ 940 | Golpe 4 (f344–f345): el poste se tuerce 8° en la caja de conexiones; la lámpara oscila sin parpadear | `farol_torcido`; cajas al pie, `cajas_carbonizadas` desde f831 |
| `persiana` metálica | Pared de fondo, a la derecha | Golpe 5 (f500–f501): abolladura con la silueta del rival | `persiana_abollada` |
| `pestana` de cartón con marcas | Pared de fondo, x 80–330, y 400–640 | No se toca; segunda marca de asterisco en f812–f815 | Dos asteriscos |
| `caja_registradora_rota` | Extremo izquierdo del suelo, x 60–170, y 1340–1440 | Nada | Igual |
| grieta de entrada | Suelo, lado derecho, x 780–950, y 1350–1420 | Se abre en f30–f45 | Abierta hasta el final (`grieta_del_rival`) |
| `telescopio_de_carton` | Cae por x ≈ 850; reposo en x ≈ 640–720, y ≈ 1380–1420 | Cae en f576–f595 | Queda quieto hasta el final |
| `quemadura_del_paquete` | Suelo, bajo el paquete | f702–f726 | Queda |

**Cámaras del motor:** valores de partida de fotografía (sección 3.2 de la dirección), a probar en la vista previa; velocidad máxima de cámara ≈ 8 % del ancho por segundo. **Reparto del cuadro (1080x1920):** útil x 60–960, y 380–1440 (los pies pueden bajar hasta y ≈ 1650); **franja de subtítulos y 885–1105, prohibida** para caras, contactos, dato y rival; dato y 670–855; tarjeta de medidas desde y 855 hacia arriba (un renglón y ≈ 635–855, dos y ≈ 415–855); pasillo de la firma x 330–750, y 1100–1340, de c −30 a f30, solo para el lápiz. Todas las coordenadas se vuelven a medir en el render.

## 6. Tomas

<!--
Las 25 tomas son los 25 planos de la dirección, sección 3.2 (P1 a P25), sobre 930 fotogramas a 30 f/s, con los cortes ajustados de 11.2 l.
Todas son «edición»: dibujo por código con el motor de acción. «f» es el fotograma desde el inicio. Los segundos de la duración son f/30.
Cada toma trae su frase de cámara en inglés (la de la dirección) y su frase de actuación (la de 4.10).
-->

### Toma 1 — Firma y portada (P1)

- **Duración:** 1,00 s (30 f, f0–f29)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras, entero, con el monitor apagado sobre la pila de torres al centro; la pestaña al fondo y la caja registradora rota ya están, quietas
- **Encuadre:** general frontal de portada a la altura de los ojos. Tan a la izquierda y Tin a la derecha, de perfil, cabeza a 25°, caras de `curiosidad` dentro de la zona útil. Pozo de luz del farol sobre el pasillo
- **Cámara:** fija. Frase de cámara: static locked-off shot, eye level, night loading yard, dark monitor on stacked towers at center
- **Acción:** el lápiz ya viene girando en f0, entero y nítido, en el pasillo; vuelve en 10 f y Tan lo atrapa en f10 con el brazo de firma (95°, 108°); retroceso de brazo y cuerpo. Tin sin lápiz, con su saltito de −5 px. El rival no aparece hasta f30. Frase de actuación: Tan catches the spinning pencil with a small recoil of the arm and lifts her chin to ask the question
- **Audio:** sonidos de la firma `firma_whoosh_regreso` y `firma_atrapada` (f10), los de siempre. Tan empieza en f14: «Is GTA 6 coming to PC?» (termina en f82, dentro de la toma 3)
- **Texto en pantalla:** portada «GTA 6 PC?» y debajo «Facts, Checked», quieta f0–f29, a la derecha de la pestaña. Sin subtítulo
- **Referencia:** firma del canal (`canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`) y portada del short 4

### Toma 2 — El rival sale de la grieta (P2)

- **Duración:** 0,53 s (16 f, f30–f45)
- **Personajes:** @tan, @tin, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** subjetivo de Tan (cámara en su sitio, sin dibujarlo), mirando a la grieta del lado derecho; pozo del farol al fondo
- **Cámara:** empuje lento +3 % (≈ 5,6 % del ancho por segundo). Frase de cámara: low POV from the smaller figure's eye level, slow push-in as a crack opens in the ground and ink rises out of it
- **Acción:** la grieta se abre en f30–f33 (dos trazos del suelo, tres partículas de polvo con contorno); un hilo de tinta lila sube y se dibuja de un trazo (f34–f39); se enrolla en madeja y asoma el cuerpo de palitos, asienta a 1,25 (f40–f45, muelle `POP`). Tan gira la mirada a la grieta en f32; Tin gira la cabeza y da medio paso atrás. Frase de actuación: A thin ink thread climbs out of a crack in the floor, loops into a tangled ball, and swells until it towers over them
- **Audio:** Tan sigue en «Is GTA 6 coming to PC?». `grieta_abre`: **−34 dBFS, solo por debajo de 150 Hz, sin clic** (nombre dicho debajo: 11.1 c1). Música: `tic_de_regla` desde f30, ≈ −34 LUFS
- **Texto en pantalla:** subtítulo desde f30: «¿GTA 6 va a salir en PC?»
- **Referencia:** entrada del rival «sale de una grieta» (inversa de la salida del short 4), conexión P-002

### Toma 3 — El rival crece (P3)

- **Duración:** 1,00 s (30 f, f46–f75)
- **Personajes:** @tan, @tin, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** general bajo en tres cuartos desde la izquierda; el rival crece dentro del pozo del farol; ninguna cabeza del rival a menos de 1,2 R de la de Tin o la de Tan
- **Cámara:** fija. Frase de cámara: low three-quarter wide shot from the left, static, the ink figure grows as the two stick figures step apart
- **Acción:** el rival crece de 1,25 a 1,5 «como gato erizado» (f46–f69, curva suave); el rizo se inclina hacia Tan (f70–f75). Tan retrocede dos pasos de 0,4 u (f46–f62) con `sorpresa` y se recompone; Tin se adelanta a su carril (dos pasos, uno cada 8 f), `camina`. Frase de actuación: Tan shrinks back two steps, eyes wide, scarf swinging; Tin turns his head, takes a half step back, then steps forward and plants both feet
- **Audio:** Tan termina «Is GTA 6 coming to PC?» en f82. Resto bajo de `grieta_abre` plano en −34 dBFS con fundido que termina en f66; `roce_suelo` muy bajo (−34) en f58–f69
- **Texto en pantalla:** subtítulo «¿GTA 6 va a salir en PC?» (hasta f82)
- **Referencia:** el rival crece «sin respuesta»: la pregunta toma cuerpo

### Toma 4 — Golpe 1: el empujón de Tin (P4)

- **Duración:** 0,80 s (24 f, f76–f99)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** medio-general lateral en tres cuartos desde la derecha; el contorno claro de Tin se lee contra la noche
- **Cámara:** fija. Frase de cámara: low three-quarter medium-wide shot from the right, static, a single straight punch
- **Acción:** Tin, sin arma, empuja con las dos manos al pecho del rival (el golpe más corto y seco): anticipación f80–f83 (4 f), pausa f84–f87 (4 f), **contacto f88–f89** (arco de borrón naranja, estrella ≤ 0,6 u en el punto real, 4 gotas), lanzamiento f90–f93 con 3 calcos; vuelo de frente a la pila f94–f99 (reloj 0,5). Tan, en guardia, cambia de apoyo en f101. Frase de actuación: Tin pulls both hands to his chest, holds still for a beat, then shoves the ink figure in a single frame
- **Audio:** pausa de efectos y música f82–f87. `golpe` seco (tono alto, cola ≤ 90 ms) con el pico en f87 y `silbido_corto` en f85, a −10 dBFS. Tin entra en f90: «Not announced.» (hasta f117)
- **Texto en pantalla:** subtítulo desde f90: «No está anunciado.». Dato «GTA 6 on PC:» / «not announced» con sello «as of» y la fecha de la relectura: entra f92, quieto f97–f204, con placa cian llena en «not announced»
- **Referencia:** el golpe de la referencia medida por Keter (pausa, contacto de 2 f, desaceleración en el aire)

### Toma 5 — Una torre se rompe (P5)

- **Duración:** 0,60 s (18 f, f100–f117)
- **Personajes:** @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** primer plano bajo en tres cuartos de la pila de torres; torres `#3A4570`, polvo `#5A6690` con contorno
- **Cámara:** fija. Frase de cámara: low close three-quarter shot of a stack of computer towers, static, one tower splits and falls
- **Acción:** el rival choca contra la pila (f100–f101): cede la torre de abajo (panel abierto, ventilador colgando) y el monitor se inclina 10°; queda `torre_de_pc_rota`. El rival se encoge a 1,35 (f98–f106), se sienta y mira la torre rota (f102–f117). Frase de actuación: The ink figure folds around the shove, flies across the yard into the stack of computer towers, and sits down to stare at the broken one
- **Audio:** `choque_madera_agudo` y `vidrio_grieta` bajo, con el pico en f99 y **≤ −32 dBFS** (debajo de «announced»). Tin: «Not announced.» (f90–f117)
- **Texto en pantalla:** subtítulo «No está anunciado.» (hasta f117); el dato de la toma 4 sigue quieto
- **Referencia:** choque contra el mundo con reacción (A5 y A8); pieza rota con nombre propio, P-007

### Toma 6 — Golpe 2: la embestida de Tan (P6)

- **Duración:** 1,00 s (30 f, f118–f147)
- **Personajes:** @tan, @tin, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** general bajo en tres cuartos desde la izquierda; el rival se levanta y Tan golpea; Tin ya salió por el frente al flanco y no estorba
- **Cámara:** fija. Frase de cámara: low three-quarter wide shot from the left, static, one figure rises and the other strikes it in the body
- **Acción:** el rival se levanta (f118–f127). Tan, tras su carrera corta (f106–f123), frena con el hombro atrás y **espera quieta a que el rival esté de pie** (pausa f124–f129); **contacto f130–f131** (embestida de hombro), lanzamiento f132–f135, vuelo girando una vez f136–f145 (reloj 0,35), choque contra `cajas_der` f146–f147. Rival a 1,2. Frase de actuación: Tan sprints, brakes, twists her shoulder back and holds it still until the figure is standing; then she charges with the shoulder
- **Audio:** `golpe_agudo` (un tono arriba del golpe 1) con el pico en f129, a −10 dBFS; `cajas_caen` con el pico en f145 y **≤ −30 dBFS** (debajo de «Rockstar»). Tin entra en f132: «Rockstar hasn't announced a PC version.» (hasta f206)
- **Texto en pantalla:** subtítulo desde f132: «Rockstar no ha anunciado ninguna versión de PC.» (subrayado cian en «Rockstar»); el dato sigue quieto
- **Referencia:** golpe de Tan distinto del de Tin en quién, con qué, hacia dónde y contra qué

### Toma 7 — El contraataque que falla (P7)

- **Duración:** 1,67 s (50 f, f148–f197)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** general bajo; cajas de cartón entre cámara y acción, fuera de las caras
- **Cámara:** paralaje lateral lento: 0,4 u en 50 f (≈ 6 % del ancho por segundo), de izquierda a derecha. Frase de cámara: low wide shot, slow lateral drift past stacked cardboard boxes, a swing misses and the target dodges
- **Acción:** el rival se pone de pie y se sacude (f148–f163), se echa atrás (f164–f169), pausa (f170–f173) y salta sobre Tin con el brazo en zarpazo (f178–f189, zarpazo en el aire f182–f185 **sin contacto**); Tin lee su pausa, se agacha (f174–f189) y lo deja pasar. El rival aterriza resbalando (f190–f197). Tan camina a C1 a la izquierda y sigue al rival con la cabeza. Nadie golpea al caído. Frase de actuación: The ink figure leans back, holds, then leaps over Tin with one arm swinging, lands on its knees and slides
- **Audio:** `silbido_sube` más largo en el salto (sin golpe: falla); `silbido` en cada esquive; a −24 dBFS como máximo mientras habla Tin. Tin: «Rockstar hasn't announced a PC version.» (hasta f206)
- **Texto en pantalla:** subtítulo «Rockstar no ha anunciado ninguna versión de PC.»; el dato sigue quieto
- **Referencia:** «el rival contraataca una vez y falla»; ninguna espera de más de 45 f sin contacto o esquive entre f150 y f300

### Toma 8 — Golpe 3: la patada de Tin (P8)

- **Duración:** 1,07 s (32 f, f198–f229)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** medio-general en tres cuartos desde la derecha; el pozo del farol rompe en las cajas
- **Cámara:** fija. Frase de cámara: low three-quarter medium-wide shot from the right, static, boxes and a monitor burst apart
- **Acción:** el rival se replanta (f198–f207); Tin da dos zancadas (f200–f205), pausa (f206–f211), **contacto f212–f213** (patada frontal con la planta del pie), lanzamiento f214–f217, vuelo f218–f225 (reloj 0,5, hacia la izquierda y al fondo), choque f226–f227 contra `monitores`: un monitor revienta en estrella (`monitor_roto`) y un trozo de marco vuela f228–f236; Tan salta atrás 0,3 u (f230–f237). Frase de actuación: Tin takes two long strides, plants his back foot, holds, and pushes his sole into the ink figure's chest; The ink figure crashes into a monitor, which bursts in a star of cracks
- **Audio:** `golpe_grave` con el pico en f211, a −10 dBFS; `vidrio_grieta` del monitor con el pico en f225 y ≤ −24 dBFS (≤ −30 si con la voz real cae sobre «PlayStation»). Tin entra en f214: «It's on PlayStation 5, and Xbox Series X and S.» (hasta f295)
- **Texto en pantalla:** subtítulo desde f214: «Está en PlayStation 5 y Xbox Series X\|S.». Dato «out on:» / «PlayStation 5 · Xbox Series X\|S»: entra f216, quieto f221–f296 (subrayado cian en las marcas, nunca placa llena)
- **Referencia:** golpe de Tin con otra parte del cuerpo y otra dirección que el del short 4

### Toma 9 — El rival se tambalea (P9)

- **Duración:** 2,20 s (66 f, f230–f295)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** general alto-medio, casi frontal: el rival se tambalea entre cajas rotas, Tan y Tin se acomodan
- **Cámara:** fija. Frase de cámara: medium-high wide shot, static, the figure staggers among broken boxes
- **Acción:** el rival, sentado entre el vidrio (f228–f239), se pone de pie (f240–f251) y camina hacia Tan 1,0 u (f254–f270), se infla de 1,1 a 1,18. Tin esquiva la torre que cae de la pila (f262–f270, paso atrás de 0,4 u) y queda con `pensando`; Tan camina a su sitio junto a Tin (f270–f301) y cambia la cara a `curiosidad` en f290. Ninguna pose idéntica más de 12 f. Frase de actuación: Tin steps back as the top tower tips and slides off the stack, then stands with his face blank
- **Audio:** Tin: «It's on PlayStation 5, and Xbox Series X and S.» (hasta f295). La torre que cae (f262) no lleva efecto propio (cae bajo «Xbox Series X and S»); si se quiere, `choque_madera_bajo` a ≤ −34 dBFS. Música: `tic_de_regla` + `latido` cada 40 f, ≈ −31 LUFS, agachada 6 dB bajo cada línea
- **Texto en pantalla:** subtítulo «Está en PlayStation 5 y Xbox Series X\|S.» (hasta f295); el dato sigue quieto hasta f296
- **Referencia:** consecuencia que llega tarde (la torre del golpe 1); respiro dentro de la ráfaga 1

### Toma 10 — Detalle: el lápiz dibuja la regla (P10)

- **Duración:** 1,13 s (34 f, f296–f329)
- **Personajes:** @tin
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** macro: la punta del lápiz de Tin dibuja la `regla_de_tinta`; luces del farol desenfocadas al fondo
- **Cámara:** fija (la acción es la mano). Frase de cámara: macro close-up of a pencil tip drawing a long ink ruler, static, distant lamp lights softly out of focus
- **Acción:** un solo trazo de lápiz para el cuerpo de la regla (8 f) y cinco marcas de 3 f cada una, **sin números ni texto** (f296–f321); la empuña (f322–f323) y anticipa en f324. Frase de actuación: Tin draws a ruler in one stroke of the pencil, then five short marks, one by one
- **Audio:** `regla_marcas` (tres marcas) a −26 dBFS en f296–f321, sin voz. Tan, fuera de plano, pregunta desde f302: «How long last time?» (hasta f328). Música: solo `tic`, ≈ −36 LUFS
- **Texto en pantalla:** subtítulo desde f302: «¿Cuánto tardó la vez pasada?»
- **Referencia:** plano de detalle (tipo de plano del manual 11); respiro 1

### Toma 11 — Medida 1: golpe 4 contra el poste (P11)

- **Duración:** 0,47 s (14 f, f330–f343)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** general bajo en tres cuartos desde la izquierda; el poste del farol y la lámpara entran en cuadro
- **Cámara:** fija. Frase de cámara: low three-quarter wide shot from the left, static, a long ruler strikes a figure into a lamp post
- **Acción:** Tin, regla atrás y abajo (f324–f329), pausa f330–f335, **contacto f336–f337** (batazo diagonal ascendente a dos manos contra el rival; estrella 0,6 u y 7 gotas), lanzamiento f338–f341 con 3 calcos, vuelo de 2 f (f342–f343) hacia el poste, a la caja de conexiones. **El rival choca con el poste, no sube a la lámpara** (11.1 a). Frase de actuación: Tin swings the ruler back and low, holds, then swings it up on the diagonal in a single frame
- **Audio:** `regla_golpe` con el pico en f335 (−10 dBFS); `farol_choque` con el pico en f343 y **≤ −30 dBFS** (debajo de «GTA 5»). Tin entra en f338: «GTA 5 took about a year and a half to reach PC.» (hasta f432). Música: pausa alrededor de f336
- **Texto en pantalla:** subtítulo desde f338: «GTA 5 tardó cerca de un año y medio en llegar a PC.»; el dato aún no entra (entra en f374)
- **Referencia:** el golpe más fuerte antes del pico; la barra de «574 days» se dibuja con el golpe

### Toma 12 — Chispas y fuego pequeño (P12)

- **Duración:** 1,00 s (30 f, f344–f373)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** gran angular desde el suelo (contrapicado): la lámpara oscila en la banda alta, las chispas caen sobre las cajas del pie del poste; el rival, pegado al poste
- **Cámara:** fija. Frase de cámara: worm's-eye wide shot, static, sparks fall from a swaying street lamp onto cardboard boxes catching a small flat fire
- **Acción:** choque f344–f345 (el poste se tuerce 8°, `farol_torcido`; polvo con contorno); el rival flota pegado al poste (f346–f351) y cae despacio (f352–f363, reloj 0,25); chispas f344–f349, llama plana pequeña desde f346 (primera luz cálida), humo con contorno desde f358. Tan retrocede medio paso con `sorpresa` (f344–f349); Tin mira al rival (cabeza +25° como máximo). Frase de actuación: The ink figure slams into the lamp post, hangs flat against it, slides down slowly and climbs back up, clinging with its curl
- **Audio:** `chispas` con el pico en f343 y `fuego_enciende` en f346, a −26 dBFS; `fuego_crepita` continuo a −40 dBFS desde f344. Tin: «GTA 5 took about a year and a half to reach PC.»
- **Texto en pantalla:** subtítulo «GTA 5 tardó cerca de un año y medio en llegar a PC.»; el dato entra en f374
- **Referencia:** fuego plano por fases de la referencia medida; la lámpara no parpadea más de 3 veces por segundo

### Toma 13 — La tarjeta de medidas: «574 days» (P13)

- **Duración:** 2,13 s (64 f, f374–f437)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** general bajo con el monitor apagado de la pila siempre al centro; fuego pequeño al fondo a la derecha
- **Cámara:** paralaje lateral lento: 0,5 u en 64 f (≈ 5,8 % del ancho por segundo). Frase de cámara: low wide shot, slow lateral drift, small flat fire at the back right, the dark monitor on the towers stays centered
- **Acción:** el rival cae a 1,0 (f338–f346), **se agarra al poste abajo** (f364–f437, cabeza por debajo de y 1105) con el rizo temblando. Tin gira la regla un cuarto de vuelta (f380–f392) y va a C1 en f436; Tan camina 0,8 u hacia el centro (f364–f437). La barra de «574 days» se dibuja f374–f397, ease-out, **sin sobrepaso**
- **Audio:** Tin: «GTA 5 took about a year and a half to reach PC.» (f338–f432); **ningún efecto nuevo en f372–f412** (la cifra «about a year and a half»); el trazo de la barra, a ≤ −32 dBFS o ninguno; `fuego_crepita` baja a −46 dBFS en f372–f412; sin `latido` en f372–f412
- **Texto en pantalla:** tarjeta de medidas, renglón 1: «GTA 5 → PC» / «574 days» (placa cian llena) / apoyo «about a year and a half · Sep 17, 2013 → Apr 14, 2015»: entra f374, quieta f379–f524. Una sola barra, con sus dos fechas; sin eje, sin segunda barra todavía. Subtítulo «GTA 5 tardó cerca de un año y medio en llegar a PC.» (hasta f432)
- **Referencia:** la medida es un dato quieto de más de 30 f; la tarjeta tapa la pestaña por detrás (única capa que puede)

### Toma 14 — Héroe abierto: la invitación (P14)

- **Duración:** 1,13 s (34 f, f438–f471)
- **Personajes:** @tan, @tin, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** héroe abierto de los dos, de cuerpo entero, en tres cuartos desde la derecha, cerca de la mitad del video; el rival baja del poste al fondo, fuera de las caras
- **Cámara:** fija. Frase de cámara: low three-quarter hero shot of the two figures side by side, static, the ruler passes from one to the other
- **Acción:** Tin lanza la regla a Tan por debajo de la cintura (f438–f441) y vuelve a la guardia; Tan la recibe en f444 mientras camina 0,8 u y dice la invitación con `invita` (la regla queda en la otra mano), **sin mirar a cámara más de lo que dura la frase** y cambiando la cara al menos una vez (`feliz`). El rival baja del poste (f438–f449) y corre por C2 hasta frente a Tan (f448–f471, ≈ 5,5 u/s). Frase de actuación: Tan catches the ruler while walking and invites with an open hand, never turning toward the camera longer than the sentence
- **Audio:** Tan entra en f438: «Subscribe for facts, checked.» (hasta f471). **Silencio de efectos** (ni el pase de la regla ni el rival se oyen) y solo un `tic` por 20 f, agachado al mínimo (≈ −40 LUFS). Nada por encima de la voz
- **Texto en pantalla:** subtítulo desde f438: «Suscríbete: aquí los datos van comprobados.»; el dato (tarjeta de medidas, renglón 1) sigue quieto sin texto propio del pedido
- **Referencia:** pedido de suscripción «a prueba» de `PARAMETROS.md`, uno solo, en movimiento y sin promesa de tema futuro

### Toma 15 — Medida 2: golpe 5 contra la persiana (P15)

- **Duración:** 1,00 s (30 f, f472–f501)
- **Personajes:** @tan, @tin, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** medio-general en tres cuartos desde la derecha; la persiana al fondo
- **Cámara:** fija. Frase de cámara: low three-quarter medium-wide shot from the right, static, a figure slams into a metal shutter and dents it
- **Acción:** Tan, regla atrás (f472–f477), pausa f478–f483, **contacto f484–f485** (estocada recta con la pierna adelantada), lanzamiento f486–f489, vuelo **en profundidad, se achica** f490–f499 (reloj 0,35), choque f500–f501: abolladura con la silueta del rival (`persiana_abollada`, daño que se queda). Rival a 0,9 en su escalón. Frase de actuación: Tan shifts her weight back, holds, and lunges straight in with the ruler; The ink figure flies backward into the shutter, leaves its own silhouette dented in it
- **Audio:** `regla_golpe` con el pico en f483 (−10 dBFS); `persiana_choque` con el pico en f499 y **≤ −30 dBFS** (debajo de «Red Dead Redemption»). Tin entra en f486: «Red Dead Redemption 2: about a year.» (hasta f553)
- **Texto en pantalla:** subtítulo desde f486: «Red Dead Redemption 2: cerca de un año.» (subrayado cian en «Red Dead Redemption 2»)
- **Referencia:** único golpe en profundidad pura; golpe de precisión, no de peso

### Toma 16 — La tarjeta de medidas, segundo renglón (P16)

- **Duración:** 1,73 s (52 f, f502–f553)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras, con la persiana abollada
- **Encuadre:** general bajo en tres cuartos; el rival se despega de la persiana
- **Cámara:** fija. Frase de cámara: low wide shot, static, the large figure peels away from the shutter
- **Acción:** el rival resbala por la persiana (f502–f549; se despega en f554–f565, ya en la toma 17); la llama crece a 1,5 con una caja que cae ardiendo (f500–f511). Tan devuelve la regla a Tin (f532–f536) y Tin la sostiene horizontal, «mide» (f538–f553), con `pensando`. Se dibuja la segunda barra (f529–f552), **más corta que la primera, sin eje común ni tercera barra**. Frase de actuación: Tan tosses the ruler underhand to Tin, who holds it level like a measuring stick
- **Audio:** Tin: «Red Dead Redemption 2: about a year.» (hasta f553). **Ningún efecto por encima de −32 dBFS en f527–f553** (la cifra «about a year»); sin `latido` en ese tramo
- **Texto en pantalla:** la tarjeta de medidas crece al renglón 2 con `SLIDE` en f529: «Red Dead Redemption 2 → PC» / «≈ 1 year» (placa cian llena) / apoyo «Oct 26, 2018 → Nov 5, 2019»; quieta la tarjeta f534–f569. Subtítulo «Red Dead Redemption 2: cerca de un año.»
- **Referencia:** segunda medida; la barra es más corta que la primera y no comparte eje con ella

### Toma 17 — Respiro: el objeto que cae (P17)

- **Duración:** 1,53 s (46 f, f554–f599)
- **Personajes:** @tan, @tin, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras, con el cielo libre de datos
- **Encuadre:** general fijo con el cielo vacío arriba; la caída entera del telescopio (de y 400 a y 1400) cabe con el FOV de 52°; el telescopio cae por x ≈ 850
- **Cámara:** fija. Frase de cámara: static wide shot, empty night sky above, a small cardboard object falls through a torn slit in the air and bounces once
- **Acción:** la tarjeta de medidas sale (f570–f572). **Rasgadura en el cielo del fondo (f576–f579; se cierra sola f584–f591); el telescopio de cartón cae girando una vuelta (f576–f587, ease-in), primer apoyo en f588 (polvillo de cartón con contorno), un solo rebote de ≈ 0,4 u con deriva lateral a la izquierda y reposo a 20° de inclinación en f595.** Tan lo mira 6 f, solo cabeza, sin cambiar la cara (f588–f593); Tin no mira; el rival (0,9) camina a la izquierda 3,3 u (f567–f595) sin gesto hacia el objeto. **Nadie lo comenta.** El rival empieza a dibujar su caja en f596 (los 4 últimos fotogramas de la toma). Frase de actuación: Ink-colored cardboard telescope tumbles out of a tear in the sky, bounces once and lies still; Tan turns her head toward it for six frames without changing her face
- **Audio:** sin voz. `papel_rasga` con el pico en f575 y la cola hasta f579, a −26 dBFS; `caida_objeto`: roce de caída (−28 dBFS), impacto en f587 (−22 dBFS), rebote con el pico en f594 (−30 dBFS) y roce corto; **sin campana, sin tono, sin barrido que suba**. Música: solo `latido` cada 40 f, muy bajo (≈ −38 LUFS), sin `tic`
- **Texto en pantalla:** ninguno (sin subtítulo ni dato: la voz calla)
- **Referencia:** conexión P-006 (el caído, grado ancla: adelanto del short 6); el objeto cae 23 f después de «about a year» (se vuelve a medir con la voz real: 20 f o más)

### Toma 18 — El paquete (P18)

- **Duración:** 1,73 s (52 f, f600–f651)
- **Personajes:** @duda, @tan, @tin
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** medio en tres cuartos desde la derecha, a ras de suelo; la caja lisa de tinta `#3A4570` con borde lila, sin texto ni icono
- **Cámara:** empuje lento +6 % (≈ 3,5 % del ancho por segundo) hacia la caja. Frase de cámara: low three-quarter medium shot, slow push-in toward a plain ink box sliding across the ground
- **Acción:** el rival dibuja una caja lisa de un trazo (f596–f611); la empuja con el pie y se aparta con las manos atrás (f612–f640); la caja desliza ≈ 1,8 u por C2 con frenada, **sin rebote** y se detiene a ≈ 1,0 u de Tan. Tan camina hacia la caja (f622–f641), se agacha y extiende la mano derecha (f642–f651); Tin corre con la regla (f640–f651, 1,2 u) y frena en 6 f. Frase de actuación: The ink figure draws a plain box in one stroke, nudges it with its foot and puts its hands behind its back; Tan walks up to the box, crouches and reaches out one hand
- **Audio:** `trazo_de_tinta` en f596–f611 (−26 dBFS); `paquete_desliza` en f612–f640 (−30 dBFS). Tin entra en f600: «Files that say, GTA 6 for PC, are not from Rockstar.» (hasta f694). Música: `tic` que acelera (cada 20 f hasta f640, cada 15 hasta f670, cada 10 hasta f691); pausa de música f646–f651
- **Texto en pantalla:** subtítulo desde f600: «Los archivos que dicen ser “GTA 6 para PC” no son de Rockstar.». El dato entra en f654 (toma 19)
- **Referencia:** cambio de táctica del rival: del golpe al engaño; suspenso sin golpe

### Toma 19 — El bloqueo (P19)

- **Duración:** 0,87 s (26 f, f652–f677)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** medio en casi perfil, a ras de suelo; Tan, la regla y la caja no se solapan; cabeza de Tin a ≥ 1,2 R de la de Tan
- **Cámara:** fija. Frase de cámara: low near-profile medium shot, static, one figure stops the other's reaching hand with a long ruler
- **Acción:** **la regla de Tin cruza horizontal por delante de la muñeca de Tan, a la altura de su mano, sin estrella ni gotas** (f652–f653); hold de póster f654–f659 (nadie se mueve salvo la regla, que vibra 4 f, ±3°); Tin baja la regla 10° (f660–f667) y Tan retira la mano a su pecho (f656–f663). **Se lee en silueta, sin texto.** Si la regla se lee como un golpe a Tan, Tin se separa 0,3 u y la regla pasa 0,2 u por encima de la muñeca. Frase de actuación: Tin sprints in with the ruler and stops it level across Tan's wrist; both freeze
- **Audio:** `bloqueo_tinta` suave (corte seco, cola ≤ 120 ms) con el pico en f651 y **≤ −30 dBFS** (debajo de «PC»). Tin sigue: «Files that say, GTA 6 for PC, are not from Rockstar.» (hasta f694)
- **Texto en pantalla:** subtítulo «Los archivos que dicen ser “GTA 6 para PC” no son de Rockstar.». Dato «'GTA 6 for PC' files:» / «not from Rockstar» (subrayado cian en «Rockstar»): entra f654, quieto f659–f698; no cubre el gesto
- **Referencia:** el gesto central del video: no tocar el archivo; se copia

### Toma 20 — Detalle: la punta de la regla se acerca (P20)

- **Duración:** 0,73 s (22 f, f678–f699)
- **Personajes:** @duda, @tin
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** primer plano de la caja lisa en el suelo; la punta de la regla entra al cuadro desde lejos; luces del farol desenfocadas al fondo
- **Cámara:** fija. Frase de cámara: close-up of a plain ink box on the ground, static, a ruler tip enters the frame from far away
- **Acción:** Tin retrocede 0,5 u extendiendo la regla (f660–f687), anticipa (f688–f693) y **pausa quieta f694–f699** (nada se mueve salvo la regla que avanza); el rival se acerca a su caja (f664–f699, 1,0 u, lento), la mira y ladea el rizo. Frase de actuación: Tin backs away, stretching the ruler out at full length, and holds still before the tip
- **Audio:** Tin termina «Not from Rockstar.» en f694; **silencio total sin efectos ni música de f692 a f699** (8 f, por debajo de −90 dBFS); voz callada desde f695
- **Texto en pantalla:** el dato «not from Rockstar» queda quieto hasta ≈ f698 y sale en f699; sin subtítulo desde f695
- **Referencia:** el silencio agranda el pico

### Toma 21 — Pico: el paquete revienta (P21)

- **Duración:** 1,10 s (33 f, f700–f732)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras
- **Encuadre:** héroe abierto, gran angular muy bajo y frontal: todo el patio a la vista, la bola de fuego sube del suelo entre las figuras; Tin, Tan, el rival y la caja se ven a la vez
- **Cámara:** fija. Frase de cámara: static ultra-wide low-angle shot, the whole yard in view, a fireball blooms upward from the ground between the figures
- **Acción:** **toque en f700–f701** (Tin, de lejos, con la punta de la regla; una gota de tinta; no es un golpe contra el rival); cuadros invertidos con máscara solo sobre la caja f702–f703 (la única vez en el video); líneas radiales f704–f708; claro con máscara f709–f712 (≤ 30 % del cuadro, opacidad ≤ 0,45; nunca a pantalla completa); bola de fuego plana f713–f722 (cada dibujo dura 2 f, los dos tonos del fuego); enfriamiento f723–f726; humo con contorno desde f727. El rival sale despedido (calcos f704–f707, vuelo f708–f719 a la izquierda, rueda f720–f726) y se sienta chamuscado a 0,8 con hollín `#0B0F1F`, **sin rojo**. **A Tin y a Tan no los alcanza fuego, escombro ni onda**: se cubren y retroceden 0,3 u (Tin con `susto`, Tan con `sorpresa`). Queda la `quemadura_del_paquete`. Frase de actuación: Tin touches the box with the tip of the ruler; both cover their faces and step back
- **Audio:** sin voz (callada f695–f727). `toque_regla` en f700 (único sonido, −22 dBFS; **única excepción a «pico en K −1»**); `tinta_sube` f702–f707 (−34 a −16 dBFS); `explosion` con el pico en f712 (−8 dBFS) y `chispas`; `cola_explosion` baja a −40 dBFS en f727. Sin música
- **Texto en pantalla:** ninguno (el dato no comparte plano con el pico)
- **Referencia:** explosión por fases de la referencia medida; el pico es el paquete, no un golpe

### Toma 22 — Revelado: el humo despeja (P22)

- **Duración:** 2,23 s (67 f, f733–f799)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras, con la quemadura y el cráter
- **Encuadre:** general fijo, revelado: el humo con contorno despeja y deja ver el dato; el rival se vuelve a plantar a 0,8
- **Cámara:** fija. Frase de cámara: static wide shot, thick outlined smoke clears slowly to reveal a singed figure standing up again
- **Acción:** el humo despeja (f727–f760, siempre detrás de Tan); Tin dice el dato con `pensando` (cambio de apoyo f748 y f770); Tan pasa de `sorpresa` a `curiosidad` (f740) y da el consejo con la cabeza (dos negaciones de ±8°, sin dedo ni mano al mentón). El rival mira el cráter (f733–f748), tose humo por el rizo, se pone de pie (f750–f767) y se planta en f768 con el rizo en alto; Tin camina hacia él con la regla en guardia (f786–f799). Frase de actuación: Tin and Tan stand with blank faces; Tan shakes her head twice, slowly; The ink figure stands up and plants itself, curl high
- **Audio:** Tin entra en f728: «Some carry malware.» (hasta f761); Tan en f768: «Don't download them.» (hasta f794; baja y seca, no regaño). `fuego_crepita` bajo y nada más; **consejo (f768–f794): nada por encima de la voz**, crepitar a −46 dBFS y música a cero. Música: `latido` cada 40 f desde f741, muy bajo
- **Texto en pantalla:** subtítulos «Algunos traen programas maliciosos.» (f728–f761) y «No los descargues.» (f768–f794). Dato «some carry malware» (placa cian llena) / apoyo «Malwarebytes, Aug 24, 2026 · Huntress, Sep 9, 2026» (subrayado en las dos marcas): entra f730, quieto f735–f800
- **Referencia:** cara de póquer tras el pico; aviso de seguridad con fuente y fecha

### Toma 23 — Golpe 6: el tajo y la implosión (P23)

- **Duración:** 1,23 s (37 f, f800–f836)
- **Personajes:** @tin, @duda, @tan
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras, con la pestaña en cuadro
- **Encuadre:** general bajo en tres cuartos desde la izquierda; todo colapsa hacia un punto
- **Cámara:** fija (la pestaña queda en cuadro). Frase de cámara: low three-quarter wide shot from the left, static, everything collapses inward into one point and the smoke is pulled away
- **Acción:** Tin, regla arriba (f800–f805) y vertical sobre la cabeza (pausa f806–f811), **contacto f812–f813** (tajo vertical, el único hacia abajo; el rival se aplasta de 0,8 a ≈ 0,5 en 2 f). **Segundo asterisco en la pestaña** en f812–f815 (tres trazos: f812, f813, f814–f815). **Implosión f814–f831:** succión (f814–f815), tres anillos de tinta que se cierran desde 1,6 u (f816–f823), el humo y la llama se estiran en hilos hacia el centro (f824–f829, la llama se apaga), cierre seco (f830–f831); las cajas del pie del poste quedan ennegrecidas. Queda un resto de ≈ 1,5 R con el rizo. Frase de actuación: Tin raises the ruler overhead, holds, and brings it straight down; The ink figure collapses inward as three rings close, pulling the smoke and flame into itself
- **Audio:** pausa de efectos y música f806–f813. `regla_golpe` (grave) y `golpe_grave` con el pico en f811 (−10 dBFS); `asterisco_tic` f812–f815 (−30 dBFS). Tin entra en f814: «No official PC date. As of today.» (hasta f888). `implosion` con el grave (30–150 Hz) a **−30 dBFS** y la banda de la voz recortada a **−40 dBFS**, corte seco en f831 (debajo de «No official PC»: 11.1 c2); `fuego_crepita` se corta en f831
- **Texto en pantalla:** subtítulo desde f814: «No hay fecha oficial para PC. A hoy.». Dato «GTA 6 on PC:» / «no official date» (placa cian llena, la más grande y quieta del final) con sello «as of» y la fecha de la relectura: entra f816, quieto f821–f890
- **Referencia:** el mismo gesto de la medida 1 con resultado distinto: aquí el rival no se borra del todo

### Toma 24 — Remate: el resto gotea (P24)

- **Duración:** 2,10 s (63 f, f837–f899)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras, con todos los daños a la vista, sin humo ni fuego
- **Encuadre:** general fijo; el resto del rival goteando por el borde izquierdo; Tin lanza el lápiz a Tan
- **Cámara:** fija. Frase de cámara: static wide shot, the last ink drips off the left edge, a pencil is tossed between the two figures
- **Acción:** el resto queda sentado con el reposo vivo (f832–f855); **goteo f856–f869** (14 f): se deshace en una gota alargada que se desliza 2,1 u al borde izquierdo con 3 gotas que caen, y sale del cuadro en f869 (31 f antes de c −30), dejando un trazo corto de tinta. La regla de Tin se deshace en gotas (f836–f847) y la mira con `pensando`. Tin camina a su sitio (3,9 u, f832–f893) y le lanza el lápiz a Tan al cruzarse (f858–f862); Tan camina por C1 (3,3 u, f832–f885), lo atrapa en f862, vuelve a C2 y sube el brazo a `saluda` (f886–f899). Frase de actuación: The small ink scrap melts into a long drop and slides off the left edge of the page; Tin and Tan walk back to their marks; Tin flips the pencil to her as they pass
- **Audio:** Tin sigue «No official PC date. As of today.» (termina en f888). `escurre` en f856 y `gotas` f860–f869; las gotas más agudas de la regla en f866 (−28 dBFS); último `tic` de la música en f869; silencio de f890 a f899
- **Texto en pantalla:** subtítulo «No hay fecha oficial para PC. A hoy.» (hasta f888); el dato 12 sale en f891–f893
- **Referencia:** conexión P-005 (salida del rival por el borde izquierdo); alivio con humor seco

### Toma 25 — Cierre de la firma (P25)

- **Duración:** 1,00 s (30 f, f900–f929)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** patio_tienda_de_computadoras, con los daños (excepción declarada del empalme)
- **Encuadre:** general frontal de portada, el mismo cuadro de la toma 1: mismas poses, mismo texto, misma cámara
- **Cámara:** fija. Frase de cámara: static locked-off shot, same framing as the first frame, eye level, night loading yard
- **Acción:** el texto de portada entra en f900 (c −30); anticipación c −24 a c −19 (f906–f911), impulso hasta c −15, suelta en f915 y vuelo de 15 f del lápiz. Tin sin lápiz, cabeza a 25°. Nada más se mueve: el fuego y el humo se acabaron en f831 y el rival salió en f869. El fotograma 930 sería el fotograma 0 salvo el fondo. Frase de actuación: Tan swings her arm back and down, snaps it forward and releases the pencil
- **Audio:** la voz terminó en f888 (c −42); sonidos S1 y S2 de la firma (`firma_chasquido`, `firma_whoosh_ida`) en c −17 a c −1; música ya a cero
- **Texto en pantalla:** portada «GTA 6 PC?» y «Facts, Checked» (como en f0). Sin subtítulo
- **Referencia:** toma 1 de esta versión; el vuelo del lápiz cierra el bucle

## 7. Audio

- **Voz (por generar; una sola generación por voz, sin segundos intentos):** Tan con Zelda (`b7aaea29-0c88-5925-90c0-8f66754cda53`) y Tin con Kevin (`f1373f24-3b96-433f-9a68-e595810ef608`), Higgsfield `seed_audio`, ajustes por defecto; después `atempo=1.10` (voz siempre al 110 %), −14 LUFS por personaje y armado con los fotogramas de la sección 6. **Estimación de sonido: ≈ 2,6 a 3,0 créditos (Tin ≈ 2,0 a 2,3 y Tan ≈ 0,6 a 0,7); no es una cotización y no está aprobada.** La cotiza producción con `estimate_audio_cost` y la autoriza el dueño con el número a la vista. Nadie ha oído las voces: «GTA 6», «GTA 5», «Red Dead Redemption 2», «Xbox Series X and S», «PC» y «malware» se comprueban al oído; `revisar_voz.py` no debe perder ninguna palabra.

Guion de voz (inglés, exacto; los fotogramas son el plan con la voz estimada, ≈ 4,4 sílabas por segundo):

| Quién | Texto exacto | Fotogramas | Toma |
|---|---|---|---|
| Tan | Is GTA 6 coming to PC? | f14–f82 | 1, 2 y 3 |
| Tin | Not announced. | f90–f117 | 4 y 5 |
| Tin | Rockstar hasn't announced a PC version. | f132–f206 | 6, 7 y 8 |
| Tin | It's on PlayStation 5 and Xbox Series X and S. | f214–f295 | 8 y 9 |
| Tan | How long last time? | f302–f328 | 10 |
| Tin | GTA 5 took about a year and a half to reach PC. | f338–f432 | 11, 12 y 13 |
| Tan | Subscribe for facts, checked. | f438–f471 | 14 |
| Tin | Red Dead Redemption 2: about a year. | f486–f553 | 15 y 16 |
| Tin | Files that say 'GTA 6 for PC' are not from Rockstar. | f600–f694 | 18, 19 y 20 |
| Tin | Some carry malware. | f728–f761 | 22 |
| Tan | Don't download them. | f768–f794 | 22 |
| Tin | No official PC date. As of today. | f814–f888 | 23 y 24 |

**Texto para generar cada voz** (una pieza por personaje; cada línea en su propio párrafo con punto final; las palabras son las del guion, sin añadir ni cambiar nada; sin coletilla, porque la cotización es de este texto: si se añade una, hay que recotizar).

Voz de Tan (Zelda), una sola generación:

```text
Is GTA 6 coming to PC?

How long last time?

Subscribe for facts, checked.

Don't download them.
```

Voz de Tin (Kevin), una sola generación:

```text
Not announced.

Rockstar hasn't announced a PC version.

It's on PlayStation 5, and Xbox Series X and S.

GTA 5 took about a year and a half to reach PC.

Red Dead Redemption 2: about a year.

Files that say, GTA 6 for PC, are not from Rockstar.

Some carry malware.

No official PC date. As of today.
```

- **Puntuación distinta de la de 2.2 (las palabras no cambian):** coma antes de «and Xbox» en la línea 4; en la línea 9 se quitan las comillas simples y se ponen comas alrededor de «GTA 6 for PC». Si el generador lee mal una palabra, se regenera solo esa línea (la cotiza producción y la autoriza el dueño): `G T A 6`, luego `G T A six`; `Red Dead Redemption two.` y `About a year.` en frases separadas; `mal ware`; `P C`.
- **Subtítulos:** quemados en la imagen, en español; **no se sube ninguna pista `.srt` a YouTube** (regla del dueño, 2026-11-26). Su texto exacto está en la sección 12.
- **Música:** hecha por código, **solo percusión y sin melodía**, en otro patrón que el del short 4 (F6): `tic_de_regla` a 90 pulsos por minuto (un tic seco de ruido filtrado cada 20 f, sin tono) y `latido` (golpe doble grave de 55 y 48 Hz cada 40 f) solo en los tramos de tensión; los tics se aceleran en el suspenso (f600–f691) y la música cae en cada contacto en lugar de subir. ≈ −30 LUFS a corto plazo, ≥ 14 dB bajo la voz y agachada 6 dB más en cada línea. Silencio total f692–f699; nada de música en f700–f732; a cero desde f900. La confirma el diseñador de sonido; nadie la ha oído.
- **Efectos:** los de la sección 13, hechos con código.

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → … → Toma 25 (y vuelve a la toma 1: el fotograma 930 es el fotograma 0, salvo el fondo).
- **Transiciones:** corte directo. 24 cortes en f30, f46, f76, f100, f118, f148, f198, f230, f296, f330, f344, f374, f438, f472, f502, f554, f600, f652, f678, f700, f733, f800, f837 y f900. Corte de impacto: uno solo, el de f700, con los dos cuadros invertidos con máscara de f702–f703. Cortes en el movimiento: tomas 4, 6, 8, 11, 12, 15 y 23; el resto, secos. Borrón de 3 f solo en la entrada de la toma 25 si el editor conserva el de la firma, y solo sobre la escena, nunca sobre el texto. **Sin zoom, sin barridos, sin cámara lenta de edición, sin reencuadre y sin temblor de cámara.**
- **Texto en pantalla:** se dibuja en el mismo render (capa de datos, subtítulos quemados y portada), nunca dentro del mundo 3D. Detalle en la sección 12. Un dato a la vez; el texto nunca contradice lo que se oye. Sin dato ni subtítulo en f554–f599 y f695–f727.
- **Portada:** el fotograma 0, en 1080x1920 (`miniatura.png`). Texto «GTA 6 PC?» / «Facts, Checked» (cinco palabras y una cifra en dos renglones, mayúscula inicial en cada una), a la derecha de la pestaña (x 360–960, y 400–640); el objeto del centro es el monitor apagado sobre la pila de torres; las caras de Tan y Tin, de perfil, dentro de la zona útil. No da la respuesta ni insinúa fecha o descarga; no usa la tipografía ni los colores del juego.
- **Formato de salida:** 1080x1920, 30 f/s, H.264, audio AAC a 48 kHz; archivo `06_final/tin_y_tan_short05_v1.mp4`. Sin pista `.srt`.

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | 0 s (las 25 tomas son edición; 31 s se resuelven en el motor y en edición) | 0 |
| Keyframes | 0 | 0 |
| Remates en resolución final | 0 | 0 |
| Voz (Kevin para Tin ≈ 2,0 a 2,3 y Zelda para Tan ≈ 0,6 a 0,7; una generación por voz) | 2 generaciones, sin generar | ≈ 2,6 a 3,0 créditos: **estimación de sonido, no cotización**; sin aprobar |
| **Total estimado** | 0 créditos de imagen y de video; la voz, por cotizar y autorizar | ≈ 2,6 a 3,0 créditos |

Lo que reporta `validar_prompt.py` (2026-11-27): elenco @tan, @tin, @duda; 25 tomas, 30,98 s en pantalla, **0 s generados** (todo es edición), presupuesto de generación de video ~0 s con 1 intento por toma; «Listo para generar», sin errores ni avisos. El validador no ve la voz: por eso el gasto real de este video se declara aquí y en `costos.md` cuando el dueño lo autorice.

## 10. Restricciones críticas

Van al inicio de la especificación de cada plano que se pase al motor, antes de la descripción. Son las que no se negocian.

```text
CRITICAL: no text, captions, subtitles, logos or watermarks unless listed in section 12.
CRITICAL: the character looks identical in every shot (same design, colors, proportions).
CRITICAL: hard cuts only, no morphing between shots.
CRITICAL: every figure, name or claim on screen comes from the project's facts file, with source and date.
CRITICAL: nothing from the game on screen: no images, no logos, no typeface, no music, no character names, no plot; plain boxes, a blank monitor, no sign with art.
CRITICAL: nothing about the unofficial port or the leak: no name, no image, no way to get it, no how it runs; the box the ink figure draws is plain ink with no text, icon, arrow, window, file name or ribbon.
CRITICAL: no date, year, window or projection for GTA 6 on PC, in voice or in drawing: two loose bars with two dates each, no shared axis with today, no third bar, no empty or dotted bar, no arrow, no plus sign.
CRITICAL: no real person or brand is ever hit, broken or burned: brand names are text on the data layer only, never objects of the world.
CRITICAL: no firearms or firearm silhouettes, no blood; the ink figure never gets red on its body, never has teeth, claws or pupils, never dies, and nobody hits it while it is down.
CRITICAL: at most 3 flashes per second; never pure white over the whole frame; inverted frames only once, inside a mask.
CRITICAL: the answer is always «not announced», never «won't» and never «will».
```

### Lo que NO debe verse ni oírse

- Ninguna imagen, captura, logotipo, tipografía, música ni nombre de personaje del juego; nada de su trama; ningún tráiler ni «concepto» de aficionados. Cajas lisas, monitor apagado, pantallas apagadas, pestaña de cartón.
- **Nada del port no oficial ni de la filtración:** ni su nombre, ni su imagen, ni cómo conseguirlo, ni qué tal corre; ninguna persona nombrada. El paquete del rival es una caja lisa de tinta: sin texto, icono, flecha, ventana, nombre de archivo ni lazo que lo vuelva deseable.
- Ninguna fecha, año, ventana ni proyección para GTA 6 en PC; ninguna tercera barra, ni vacía ni punteada; ningún eje común entre «hoy» y las dos medidas; la placa final no lleva barra.
- Ninguna persona real; ningún nombre de marca como objeto del mundo (nada rotulado se golpea, se rompe ni se quema).
- Armas de fuego y su silueta; sangre; rojo sobre el rival (lo que salta es tinta); ensañamiento; miedo; nadie golpea al caído.
- El nombre «la Duda» en voz, texto, título o portada; boca o pupilas en el rival.
- Cian en personajes, rival, armas, entorno, fuego, humo, subtítulos o destellos; placa cian llena detrás de un nombre de marca (en las marcas, solo subrayado).
- Colores fuera de la paleta B declarada; blanco puro a pantalla completa; partículas borrosas en el fuego; temblor de cámara.
- Texto, voz o subtítulo sobre el universo (pestaña, caja registradora, grieta, telescopio, marca, goteo): no llevan ninguno. Nadie comenta el objeto que cae.
- Cualquier dato fuera de la sección 12.

## 11. Gancho, ritmo y cierre

- **Regla formal de la pieza:** una pregunta que sale del suelo y se mide con una regla: dos barras sueltas, cada una con sus dos fechas, y un paquete que nadie abre; el último golpe no borra la pregunta.
- **Rejilla de tiempo:** pulso de 20 f (0,67 s, 90 por minuto) de la música; 46,5 pulsos suman los 31 s (930 f). **Los cortes los fija la acción** (pausa, contacto, vuelo y choque, según la dirección) y no todos caen sobre un pulso.
- **Gancho (0 a 1 s):** movimiento y contraste — el lápiz ya girando en f0 y atrapado en f10, «GTA 6 PC?» y «Facts, Checked» sobre una noche azul de tinta con un monitor apagado al centro, y la voz de Tan desde f14; el rival sale de la grieta en f30 y en f69 mide vez y media lo que ellos; el primer golpe cae en f88 y la respuesta oficial se oye desde f90 («Not announced.») y se lee quieta desde f97, en el segundo 3,2.
- **Empieza en movimiento:** sí: sin intro ni logo; el lápiz gira desde el fotograma 0.
- **Motivo visual que vuelve:** la regla de tinta hecha con el lápiz (nace en f296, es el arma de las tomas 11, 14, 15, 19, 20 y 23, se deshace en gotas al final) y el monitor apagado sobre la pila de torres, al centro (portada, tomas 1, 5, 13, 21, 22, 24 y 25). Se repiten con las mismas formas y colores.
- **Cierre:** el último plano es el de portada (misma cámara, mismo texto, mismas poses) con Tan lanzando el lápiz; el fotograma 0 es el paso siguiente de ese vuelo. **Excepción declarada (D6 del short 4):** el fondo del cierre conserva los daños y el del inicio está entero. El bucle devuelve la pregunta: termina con «GTA 6 PC?» en pantalla y vuelve a empezar con ella.
- **Llamado a la acción:** uno solo, de Tan: «Subscribe for facts, checked.» (f438–f471), sin promesa de tema futuro; no hay otro pedido en la voz ni en pantalla.

Mapa de ritmo (los tiempos al décimo de segundo; cortes por segundo = cortes que empiezan dentro del tramo, divididos por su duración):

| Tramo | Segundos | Pulso o intervalo | Cortes por segundo | Qué pasa (una acción) | Respiro |
|---|---|---|---|---|---|
| Gancho | 0,0–2,9 | 20 f | 1,0 (3 cortes) | Firma, portada, el rival sale de la grieta y crece | no |
| Ráfaga 1 (pico 1) | 2,9–9,8 | 20 f | 0,7 (5 cortes) | Golpes 1, 2 y 3, un contraataque que falla; dos datos | no |
| Respiro 1 | 9,9–11,0 | 20 f | 0,9 (1 corte) | Detalle: el lápiz dibuja la regla | sí (≈ 1 s) |
| Subida | 11,0–18,4 | 20 f | 0,8 (6 cortes) | Golpes 4 y 5, la invitación y la tarjeta de medidas que crece | no |
| Respiro 2 | 18,5–20,0 | 20 f | 0,7 (1 corte) | Plano general fijo: cae el telescopio; sin voz | sí (≈ 1,5 s) |
| Suspenso | 20,0–23,3 | 20 f a 10 f | 0,9 (3 cortes) | El paquete, el bloqueo, el detalle: tensión sin golpe | no |
| Pico 2 (el mayor) | 23,3–24,4 | silencio y explosión | 0,9 (1 corte) | El paquete revienta; voz callada | no |
| Respiro 3 | 24,4–26,6 | 40 f | 0,5 (1 corte) | Revelado: el humo despeja; dato y consejo | sí (≈ 2,2 s) |
| Remate | 26,7–30,0 | 30 f, cada vez más espaciado | 0,6 (2 cortes) | Último golpe, implosión, «No official PC date», el resto gotea | sí (≈ 2,1 s, resto y goteo) |
| Firma | 30,0–31,0 | — | 1,0 (1 corte) | Plano de portada y lanzamiento del lápiz | no |

Total: 25 planos y 24 cortes en 31 s (rango del canal: 8 a 25 cortes). Lo que sale se va antes de que entre lo siguiente. El movimiento se describe como mecánica (qué parte se mueve, con qué curva, en qué orden entra y sale). Tipos de plano: detalle (tomas 10 y 20), subjetivo (toma 2), héroe abierto (tomas 14 y 21), revelado (toma 22), general fijo (toma 17). **No más de 3 destellos por segundo.**

### Coreografía de cada golpe (tiempos medidos por Keter a 30 f/s; se copian los tiempos, no los dibujos)

Gramática: anticipación K −12 a K −7 (6 f, movimiento contrario al golpe con frenada); **pausa** K −6 a K −1 (6 f, pose casi quieta, el trazo «hierve», sin efectos de sonido); **contacto** K y K +1 (2 f, salto de posición, arco de borrón del color de quien golpea, estrella ≤ 0,6 u, 5 a 7 gotas de tinta); lanzamiento K +2 a K +5 (3 calcos translúcidos); vuelo y desaceleración con el reloj de la escena a 0,25 a 0,5; choque de 2 f; recuperación de 6 f; el golpe suena en K o K −1; Tin empieza el dato 2 f después del contacto. **Excepciones:** el golpe 1 lleva 4 f de anticipación y 4 de pausa y un vuelo de 6 f; el bloqueo y el toque no llevan estrella, gotas ni arco; en el golpe 4 el choque cae en f344 y la flotación va después.

| Golpe (dato) | Quién y con qué | Anticipación · pausa · contacto | Lanzamiento · vuelo · choque · recuperación | Qué se rompe (se queda) | Fuego, humo, explosión, implosión |
|---|---|---|---|---|---|
| 1 («Not announced.») | Tin, empujón con las dos manos al pecho, sin arma | f80–f83 · f84–f87 · **f88–f89** | f90–f93 · f94–f99 de frente · f100–f101 contra la pila · f90–f95 | `torre_de_pc_rota`; el monitor se inclina | Polvo con contorno; sin fuego |
| 2 («Rockstar hasn't announced…») | Tan, embestida de hombro tras una carrera corta | f118–f123 · f124–f129 · **f130–f131** | f132–f135 · f136–f145 · f146–f147 contra `cajas_der` · f132–f137 | `cajas_de_carton_rotas` | Polvo |
| Contraataque (no es golpe) | El rival salta sobre Tin y falla | f164–f169 · f170–f173 · zarpazo f182–f185 sin contacto | salto f178–f189 · aterriza f190–f191 · resbala f192–f197 · se replanta f198–f207 | Nada | Nada |
| 3 («It's on PlayStation 5…») | Tin, patada frontal con la planta | f200–f205 · f206–f211 · **f212–f213** | f214–f217 · f218–f225 · f226–f227 contra `monitores` · f214–f219 | `monitor_roto`; en f262 cae la torre de encima (`torre_de_pc_caida`) | Chispas pequeñas |
| 4 («GTA 5 took…») | Tin, `regla_de_tinta`, batazo diagonal ascendente | f324–f329 · f330–f335 · **f336–f337** | f338–f341 · f342–f343 · **f344–f345** contra el poste · f338–f343 | `farol_torcido` | Chispas f344–f349; llama pequeña desde f346; humo desde f358 |
| Se la pasan | Tin lanza la regla a Tan (f438–f441) y Tan se la devuelve (f532–f536) | — | — | — | — |
| 5 («Red Dead Redemption 2…») | Tan, `regla_de_tinta`, estocada recta | f472–f477 · f478–f483 · **f484–f485** | f486–f489 · f490–f499 en profundidad · f500–f501 contra la `persiana` · f486–f491 | `persiana_abollada` | La llama crece a 1,5 (f500–f511) |
| Bloqueo («Files that say…») | Tin frena la mano de Tan con la regla | carrera f640–f651 · — · **f652–f653** | hold f654–f659 · suelta f660–f667 | Nada | Nada |
| Toque («Files that say…» y pausa de voz) | Tin, de lejos, con la punta de la regla | f688–f693 · f694–f699 · **f700–f701** | blast f704–f707 · rival f708–f719 · rueda f720–f726 | `quemadura_del_paquete` | Explosión f702–f726; humo f727–f760 |
| 6 («No official PC date…») | Tin, `regla_de_tinta`, tajo vertical | f800–f805 · f806–f811 · **f812–f813** | — (el rival se hunde en sí mismo) | `cajas_carbonizadas`; resto de ≈ 1,5 R | Implosión f814–f831; el resto gotea f856–f869 |

**El rival (versión 2, hoja Noche):** entra a 1,25 veces la altura de Tin y Tan y crece a 1,5 **por profundidad** (f46–f69). **Marcador de avance**, un escalón por dato: 1,5 → 1,35 (f98) → 1,2 (f132–f140) → 1,1 (f214–f222) → 1,0 (f338–f346) → 0,9 (f486–f494, y 0,9 desde f554) → 0,8 chamuscado (f726) → resto de ≈ 1,5 R (f830). Entre un golpe y el siguiente se infla 0,06–0,08 en los 24 f anteriores a la anticipación; nunca pasa de 1,5. Nunca da miedo (se infla como gato erizado), su contraataque falla, se sienta a mirar lo que rompió; sin dientes, garras ni pupilas; **nunca muere**; nadie lo golpea sentado o caído.

**Tin y Tan por tramo:** f0–f29 Tin `parado` sin lápiz con la cara de la portada, cabeza 25°; Tan con el brazo de firma. f30–f117 Tin se adelanta, `concentrado` solo en la pausa, `pensando` al dato; Tan `sorpresa` al retroceder, luego guardia. f118–f295 Tan embiste y esquiva el trozo de monitor; Tin se agacha, patea y esquiva la torre. f296–f437 Tin dibuja la regla y golpea; Tan pregunta con `pregunta`, luego `sorpresa` y `curiosidad`. f438–f553 Tan recibe la regla y usa `invita`, estoca y la devuelve; Tin `pensando`. f554–f599 reposo vivo; solo Tan mira el telescopio, 6 f. f600–f699 Tan camina hacia la caja y extiende la mano; Tin corre, bloquea, retrocede y anticipa. f700–f799 los dos se cubren (Tin `susto`, Tan `sorpresa`), luego cara de póquer; Tan niega con la cabeza dos veces. f800–f899 Tin da el tajo, mira su regla deshacerse y camina a su sitio; Tan atrapa el lápiz y sube el brazo. f900–f929 los dos como en f0. Acción secundaria: bufanda de Tan con muelle; el trazo del rival hierve cada 3 f; **ninguna pose idéntica más de 12 f** salvo las pausas de 6 f y los holds declarados; ninguna encima de un dato.

### Mapa de velocidad (el reloj de la escena cambia; la voz nunca)

| Tramo (f) | Reloj de la escena | Qué se siente |
|---|---|---|
| Anticipaciones (6 f antes de cada pausa) | 1,0 con frenada | Carga |
| Pausas (K −6 a K −1) | Pose casi quieta; el mundo sigue (fuego, humo, polvo) | Aire contenido |
| Contactos (K, K +1) | 1,0, con salto de posición | Golpe seco |
| Lanzamientos | 1,3 con calcos | Violencia de dibujo |
| Vuelos: f94–f99 (0,5), f136–f145 (0,35), f218–f225 (0,5), f352–f363 (0,25), f490–f499 (0,35), f708–f719 (0,4) | 0,25 a 0,5 | El único cámara lenta es la del dibujo |
| Carreras de Tan (f106–f123) y del rival (f448–f471) | 1,3 con borrón | Urgencia (4,5 a 6,2 u/s) |
| Telescopio: caída f576–f587 (ease-in) y rebote f588–f595 (arco) | 1,0 | Peso |
| Explosión f702–f726 | Cada dibujo dura 2 f | Estallido legible |
| Respiro 3: f733–f799 | 1,0, casi nada se mueve | Cara de póquer |
| Implosión f814–f831 | De 0,6 a 1,4 | Colapso hacia adentro |
| Firma: f0–f29 y f900–f929 | La de la firma | Reconocimiento |

### Efectos (fuego por fases, humo, impactos, explosión, implosión, daños)

| Efecto | Dónde y dosis | Qué comunica y qué emoción busca |
|---|---|---|
| Fuego plano por fases | Chispas f344–f349; llama pequeña desde f346; fase 2 (×1,5) desde f500; se apaga con la implosión en f829–f831. Dos tonos con escalón duro: núcleo `#FFE45C`, borde `#B81414`; nunca toca el cuerpo del rival; nunca cubre más de un cuarto del cuadro en dos fotogramas seguidos; es la única luz cálida | Peligro de dibujo; sube la tensión: sobresalto breve |
| Humo con contorno | Desde f358; `#9A6A45` con contorno `#0B0F1F`, siempre detrás de Tan; despeja f727–f760 y deja ver el dato | «Esto se quemó»; despeja para el dato |
| Impactos | Estrella en el punto real del contacto, polvo con contorno irregular (no círculos); **ningún corte de cámara de impacto salvo f700** (11.2 m) | Golpe seco |
| Explosión | Toque f700–f701 · invertidos con máscara f702–f703 · radiales f704–f708 · claro con máscara f709–f712 (≤ 30 % del cuadro, opacidad ≤ 0,45) · bola de fuego plana f713–f722 · enfriamiento f723–f726 · humo f727–f760 | Sorpresa; la trampa le cae a quien la puso |
| Implosión | f814–f831: succión, tres anillos de tinta que se cierran, el humo y la llama se estiran en hilos hacia el centro, cierre seco | Alivio con humor seco: la respuesta honesta no estalla |
| Daños que se quedan | Torre rota y caída, cajas, monitor roto, poste torcido, cajas carbonizadas, persiana abollada, quemadura, grieta, telescopio quieto, trazo del goteo | La pelea tuvo consecuencias; se ven en f900 |

### Firma del lápiz bumerán (no se toca)

- **Apertura (f0–f29, cámara de portada fija):** en f0 el lápiz está en el aire, entero y nítido, en el pasillo; vuelve en 10 f; Tan lo atrapa en f10 con el brazo de firma (95°, 108°); retroceso de brazo y cuerpo; Tin sin lápiz, con su saltito; la voz de Tan entra en f14. El rival no aparece hasta f30.
- **Cierre (f900–f929, misma cámara):** el texto de portada entra en c −30; anticipación c −24 a c −19 (f906–f911); impulso hasta c −15; suelta en c −15 (f915); vuelo de 15 f; la voz termina en f888 (c −42; el tope es c −17). Nada más se mueve: el fuego y el humo se acabaron en f831 y el rival salió en f869.
- **Geometría y despejes:** se calculan con `geometria_firma` sobre el fotograma 0 de este video y pasan `comprobar_firma` sin cambios: 8 px o más a cualquier cabeza en todos los fotogramas, 30 px o más al texto y al objeto del centro (el monitor), centro del lápiz dentro de la zona útil, giro horario, velocidad y escala dentro de los topes. Pasillo libre x 330–750, y 1100–1340: ni humo, ni gota, ni telescopio, ni caja registradora, ni resto del rival, ni regla, ni poste. Los sonidos de la firma son los de siempre.
- **Empalme:** lápiz, brazo, cabeza y cuerpo de Tan, pose de Tin, caras, texto y cámara son los mismos en c −1 y f0. **El fondo no** (daños al final; entero al inicio): la misma excepción del short 4, que necesita la firma del director de animación (la da en 4.9). El telescopio queda fuera del pasillo, a 30 px.

### Conexiones del universo (hueco H02; solo qué se ve, dónde y cuándo)

Ninguna lleva voz, subtítulo ni texto. Las coordenadas las fija fotografía y son el objetivo: se miden en el render. Eventos activos: 38 f (≈ 1,3 s; tope 1,5 s y 45 f); nada activo entre f46 y f575; ninguna toca la franja de subtítulos, el pasillo de la firma ni sale de la zona útil.

| Qué se ve | Cuándo | Dónde (px) | Activo |
|---|---|---|---|
| El lápiz se atrapa y se lanza (la firma) | f0–f10 y f900–f929 | Pasillo de la firma | No |
| P-001: pestaña de cartón con una marca (asterisco) | Quieta desde f0 | x 80–330, y 400–640; a 30 px o más del texto de portada | No |
| P-003: `caja_registradora_rota` | Quieta desde f0 | x 60–170, y 1340–1440 | No |
| P-002: el rival sale de una grieta del suelo, lado derecho | f30–f45 | x 780–950, y 1350–1420 | No cuenta (sustituye a la entrada de siempre) |
| P-007: `torre_de_pc_rota` | f100–f101; queda | La pila del centro | No |
| P-006: el telescopio de cartón cae por una rasgadura y rebota; Tan lo mira 6 f | Caída f576–f587, rebote f588–f595, mirada f588–f593 (≈ 19,2 s; 62 %) | Rasgadura x ≥ 830, y 400–520; reposo x 640–720, y 1380–1420 | Sí: 20 f |
| P-004: segunda marca en la pestaña (asterisco) | f812–f815 | Dentro de la zona de la pestaña, junto al primero | Sí: 4 f |
| P-005: el resto del rival gotea por el borde izquierdo | f856–f869 | Borde izquierdo; termina 31 f antes de c −30 | Sí: 14 f |
| Tin sin lápiz en los planos de firma; el rizo del rival sin punto | Siempre | — | No |

Control «se entiende solo»: quitando todo lo de esta tabla no se pierde ni una frase ni un dato. **La marca es un asterisco porque la pregunta queda sin respuesta oficial**; si el día de publicar hay anuncio de PC, el golpe 1 y el remate se reescriben y la marca pasa a punto. El objeto que cae queda a 23 f de la cifra dicha más cercana (se vuelve a medir con la voz real: 20 f o más).

## 12. Texto en pantalla y sistema de diseño

- **Tipografías:** Inter Display Medium con dígitos abiertos (`ss01`), licencia SIL Open Font License 1.1, la del canal y la del short 4. Minúsculas salvo los nombres propios y siglas, que llevan mayúscula («Tin & Tan», «GTA», «PC», «Rockstar», «PlayStation», «Xbox», «Red Dead Redemption», «Malwarebytes», «Huntress», «Sep», «Apr», «Oct», «Nov», «Aug»); la portada con mayúscula inicial en cada palabra. Nunca la tipografía del juego.
- **Paleta:** neutros: azul noche `#141B33` (fondo y mundo lejano; apoyos `#27304F` suelo, `#3A4570`, `#1C2444`, `#5A6690`, sombra y panel de subtítulo `#0B0F1F`) y papel `#F3E9D2` (línea de los cuerpos, texto, armas y marcas de la pestaña). Acento: cian `#4FE3FF`, **solo detrás del dato** (placa llena en «not announced», «574 days», «≈ 1 year», «some carry malware» y «no official date»; solo subrayado en los nombres de marca y en «Rockstar») y en el relleno de las dos barras de la tarjeta de medidas. Rival: lila `#B79CFF` con hollín `#0B0F1F` (pendiente del dueño). Efectos: fuego núcleo `#FFE45C` y borde `#B81414`; humo y cartón `#9A6A45` con contorno `#0B0F1F`. Identidad (no cuenta como acento): naranja de Tin `#E07A2E`, verde azulado de Tan `#2F7F7A`, mostaza `#E8B33B` (bufanda y lápiz), goma `#C8553D`. Contrastes calculados: texto sobre `#0B0F1F` 15,8:1; `#141B33` sobre cian 11,1:1; portada sobre el cielo 14,1:1; todos sobre 4,5:1. Por qué cada color: sección 3b de la dirección. Se mide con `revisar_color.py` con esta paleta declarada.
- **Referencias de movimiento:** `01_referencia/` está vacía; las referencias de forma son `estudios/2026-11-26_referencias_de_pelea_estudio_de_keter.md` (solo tiempos), la hoja v2 del rival, `canales/nostalgia-tin-y-tan/DESIGN.md` y la paleta B.
- **Prohibido:**
  1. Mayúsculas centradas sobre degradado, y tarjetas con degradado.
  2. Animaciones lineales de posición o escala en lo vivo (solo muelle o ease-out; lineal solo en lo mecánico).
  3. Temblor de cámara y partículas borrosas en el fuego.
  4. Placa de cian llena detrás de un nombre de marca (solo subrayado, el 40 % inferior de la altura de la letra, con extremos irregulares, inclinado ≈ 2°).
  5. El acento cian en personajes, rival, armas, entorno, farol, pestaña, fuego, humo, subtítulos o destellos.
  6. Texto sobre un personaje o sobre un contacto; un dato que se mueva con la cámara o cambie mientras se lee; un dato junto al pico.
  7. Tres capas de texto a la vez (dato, subtítulo y portada nunca coinciden).
  8. Rótulos, carteles, cajas o monitores con texto, logotipo o arte dentro del mundo 3D; la regla de tinta con números.
  9. Una tercera barra, un eje común, una flecha o un signo de suma en la tarjeta de medidas.
  10. Panel de subtítulos translúcido (es opaco al 100 %), y cambiar los colores o accesorios de Tin y Tan.
- **Márgenes seguros y escenario:** zona segura de `formatos.md`; zona útil x 60–960, y 380–1440 (pies hasta y ≈ 1650); dato de y 670–855 (cabe encabezado de 48 px, texto de 86 px y sello de 44 px en el renglón del encabezado, a la derecha); tarjeta de medidas desde y 855 hacia arriba, nunca más arriba de y 380; subtítulos en la franja y 885–1105; pasillo de la firma x 330–750, y 1100–1340. Los personajes miden ≈ 18–19 % del alto; ninguna acción importante detrás de la franja.
- **Texto exacto:** todo texto en pantalla es el de las tablas de abajo, letra por letra. Cada dato entra con muelle `POP` (220, 20, 1), se asienta y no se mueve ni cambia hasta salir (3 f); queda quieto 30 f o más. Un dato a la vez: la tarjeta de medidas es un solo dato que crece de uno a dos renglones (con `SLIDE` (120, 16, 1)). Dato de 86 px o más de alto de letra; apoyo y renglones de tarjeta de 48 px o más; sello de 44 px o más; 3 renglones como máximo a la vista.
- **No afirmar:** que GTA 6 no vaya a salir en PC, y que vaya a salir; ninguna fecha, año, ventana ni proyección para GTA 6 en PC; que GTA 5 tardó «casi dos años» (la cuenta da ≈ 1,6); un número de días para Red Dead Redemption 2 (hay dos fechas posibles: 375 y 405 días); que todo lo que circula como «GTA 6 para PC» sea falso o malicioso; el nombre de ningún proyecto, archivo o persona del port o de la filtración; ningún rumor ni tráiler de aficionados; nada de la trama ni de los personajes del juego; requisitos de PC (no existen oficiales); que el juego sea bueno o malo; ninguna persona real.
- **Subtítulos:** en español, quemados, hasta 2 renglones, sin palabra clave resaltada; siguen a la voz. Sin subtítulo en los planos de portada (f0–f29 y f900–f929), ni en f554–f599 ni en f695–f727. **No se sube pista `.srt` a YouTube.** Cada uno queda dentro de la franja y 885–1105, letra `#F3E9D2` sobre panel opaco `#0B0F1F` al 100 %; el tamaño de la letra lo fija el editor.

**Capa de datos y portada (inglés):**

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| GTA 6 PC? / Facts, Checked | 0,00 | 1,00 | x 33,3–88,9; y 20,8–33,3 | 4,2–4,5 |
| GTA 6 on PC: / not announced, con sello as of y la fecha de la relectura | 3,07 | 6,90 | x 5,6–88,9; y 34,9–44,5 | 4,5 (dato), 2,5 (encabezado) y 2,3 (sello) |
| out on: / PlayStation 5 · Xbox Series X\|S | 7,20 | 10,00 | x 5,6–88,9; y 34,9–44,5 | 4,5 y 2,5 |
| GTA 5 → PC / 574 days / about a year and a half · Sep 17, 2013 → Apr 14, 2015 (renglón 1 de la tarjeta de medidas, con su barra) | 12,47 | 19,07 | x 5,6–88,9; y 33,1–44,5 (1 renglón) | 4,5 y 2,5 |
| Red Dead Redemption 2 → PC / ≈ 1 year / Oct 26, 2018 → Nov 5, 2019 (renglón 2, con su barra más corta) | 17,63 | 19,07 | x 5,6–88,9; y 21,6–44,5 (2 renglones) | 4,5 y 2,5 |
| 'GTA 6 for PC' files: / not from Rockstar | 21,80 | 23,30 | x 5,6–88,9; y 34,9–44,5 | 4,5 y 2,5 |
| some carry malware / Malwarebytes, Aug 24, 2026 · Huntress, Sep 9, 2026 | 24,33 | 26,70 | x 5,6–88,9; y 34,9–44,5 | 4,5 y 2,5 |
| GTA 6 on PC: / no official date, con sello as of y la fecha de la relectura | 27,20 | 29,77 | x 5,6–88,9; y 34,9–44,5 | 4,5 (dato), 2,5 y 2,3 |
| GTA 6 PC? / Facts, Checked (portada de cierre) | 30,00 | 31,00 | x 33,3–88,9; y 20,8–33,3 | 4,2–4,5 |

Las entradas y las quietudes son las de la dirección (sección 2.2) y las de 4.12; las salidas son las de 4.12 o se derivan de la regla «sale en 3 f» y las confirma el editor. **El sello de fecha («as of» más la fecha) se escribe el día de publicar con la fecha de la relectura del hecho que caduca**; es código y se actualiza sin tocar la voz.

**Subtítulos en español (solo quemados):**

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| ¿GTA 6 va a salir en PC? | 1,00 | 2,73 | franja y 46,1–57,6 | franja de 11,5 |
| No está anunciado. | 3,00 | 3,90 | franja y 46,1–57,6 | franja de 11,5 |
| Rockstar no ha anunciado ninguna versión de PC. | 4,40 | 6,87 | franja y 46,1–57,6 | franja de 11,5 |
| Está en PlayStation 5 y Xbox Series X\|S. | 7,13 | 9,83 | franja y 46,1–57,6 | franja de 11,5 |
| ¿Cuánto tardó la vez pasada? | 10,07 | 10,93 | franja y 46,1–57,6 | franja de 11,5 |
| GTA 5 tardó cerca de un año y medio en llegar a PC. | 11,27 | 14,40 | franja y 46,1–57,6 | franja de 11,5 |
| Suscríbete: aquí los datos van comprobados. | 14,60 | 15,70 | franja y 46,1–57,6 | franja de 11,5 |
| Red Dead Redemption 2: cerca de un año. | 16,20 | 18,43 | franja y 46,1–57,6 | franja de 11,5 |
| Los archivos que dicen ser “GTA 6 para PC” no son de Rockstar. | 20,00 | 23,13 | franja y 46,1–57,6 | franja de 11,5 |
| Algunos traen programas maliciosos. | 24,27 | 25,37 | franja y 46,1–57,6 | franja de 11,5 |
| No los descargues. | 25,60 | 26,47 | franja y 46,1–57,6 | franja de 11,5 |
| No hay fecha oficial para PC. A hoy. | 27,13 | 29,60 | franja y 46,1–57,6 | franja de 11,5 |

Texto y subtítulos pasan `revisar_texto.py` (inglés para voz y datos, español para subtítulos) con 0 errores antes de dar el prompt por bueno.

### Color con intención

- **Neutros (2):** azul noche `#141B33` y papel `#F3E9D2`. **Acento (1):** cian `#4FE3FF`, solo detrás del dato y en las dos barras; nunca a la vez que el pico. Tin y Tan conservan sus colores.
- **Cómo ayuda al objetivo:** el primer cuadro se distingue del primer cuadro del short 4 (hoja clara y acento amarillo) y se lee en menos de un segundo (noche, siluetas claras, un monitor apagado); después el cian aparece solo donde hay un dato y el ojo aprende dónde mirar. La placa de «not announced» (al inicio) y la de «no official date» (al final) son la promesa del título y los puntos de más contraste: que la respuesta honesta no pase inadvertida separa este video del clickbait.
- **Riesgos de lectura (por medir):** el cian junto a nombres de marca (**pendiente del supervisor**: comparar con el color oficial de PlayStation, Xbox, Rockstar, Malwarebytes y Huntress; si ΔE < 25, cambia el acento; por eso en las marcas va solo como subrayado); el humo pardo y la cabeza verde azulada de Tan tienen la misma luminosidad (el humo va detrás de Tan, con contorno oscuro, y Tan con contorno claro); cian y lila se acercan en daltonismo (nunca comparten zona); Tan contra el suelo da 2,7:1 (siempre con contorno claro); fondo oscuro con el brillo bajo del teléfono (dato en tarjeta opaca); destellos sobre fondo oscuro (máscara ≤ 30 %, opacidad ≤ 0,45, `comprobar_destellos` es el control crítico); el borde rojo del fuego no parpadea y no toca al rival.

## 13. Sonido

Nadie del equipo ha oído estos sonidos (son sintéticos, por código): los valida un oído humano antes de la prueba. Voz a −14 LUFS; **ningún efecto tapa una cifra o un nombre dicho** (11.1 g2): bajo una palabra de dato, ≤ −30 dBFS si es un nombre y ≤ −32 si es una cifra; ≤ −24 en el resto de la voz; los golpes de contacto (−10 dBFS) caen antes de la voz de Tin (K −1; Tin entra en K +2). Cada golpe suena en K −1; el sonido de cada choque, en el fotograma anterior al choque de animación. «Catálogo» = existe en `motor_de_accion/sonidos/sonido.py`; «nuevo» = hay que construirlo y anotarlo en `catalogo.json`.

| Golpe o efecto | Segundo | A qué corte va atado | Origen y licencia |
|---|---|---|---|
| Firma: regreso del lápiz y atrapada (S3 y S4) | 0,00–0,33 (f0–f10) | Toma 1 | Los de la firma, código propio |
| `grieta_abre`, solo grave, −34 dBFS, fundido hasta f66 | 1,00–2,20 (f30–f66) | Tomas 2 y 3: la grieta | Nuevo, código propio |
| Pausa de efectos y música | 2,73–2,90 (f82–f87) | Toma 3 a 4 | — |
| `silbido_corto` y `golpe` seco (−10 dBFS) | 2,83 (f85) y 2,90 (f87) | Toma 4: golpe 1 | Catálogo, código propio |
| `choque_madera_agudo` y `vidrio_grieta` bajo (≤ −32 dBFS) | 3,30 (f99) | Toma 5: torre rota | Catálogo, código propio |
| `golpe_agudo` (−10 dBFS) y `cajas_caen` (≤ −30 dBFS) | 4,30 (f129) y 4,83 (f145) | Tomas 6: golpe 2 | Catálogo, código propio |
| `silbido_sube` más largo, sin golpe | 5,93–6,30 (f178–f189) | Toma 7: contraataque que falla | Catálogo, código propio |
| `golpe_grave` (−10 dBFS) y `vidrio_grieta` del monitor (≤ −24 dBFS) | 7,03 (f211) y 7,50 (f225) | Toma 8: golpe 3 | Catálogo, código propio |
| `regla_marcas` (tres marcas, −26 dBFS) | 9,87–10,70 (f296–f321) | Toma 10: dibuja la regla | Nuevo, código propio |
| `regla_golpe` (−10 dBFS) y `farol_choque` (≤ −30 dBFS) | 11,17 (f335) y 11,43 (f343) | Toma 11: golpe 4 | Nuevo, código propio |
| `chispas` y `fuego_enciende` (−26 dBFS) | 11,43 (f343) y 11,53 (f346) | Toma 12 | Catálogo, código propio |
| `fuego_crepita` continuo (−40 dBFS; −46 en f372–f412 y f527–f553; cortado f690–f699 y en f831) | 11,47–23,00 y 24,43–27,70 | Tomas 12 a 20 y 22 a 23 | Nuevo, código propio |
| Ningún efecto nuevo sobre la cifra «about a year and a half» | 12,40–13,73 (f372–f412) | Toma 13 | — |
| Silencio de efectos en la invitación | 14,60–15,70 (f438–f471) | Toma 14 | — |
| `regla_golpe` (−10 dBFS) y `persiana_choque` (≤ −30 dBFS) | 16,10 (f483) y 16,63 (f499) | Toma 15: golpe 5 | Nuevo, código propio |
| Ningún efecto por encima de −32 dBFS sobre «about a year» | 17,57–18,43 (f527–f553) | Toma 16 | — |
| `papel_rasga` (−26 dBFS) | 19,10–19,30 (f573–f579) | Toma 17: rasgadura | Nuevo, código propio |
| `caida_objeto`: caída (−28), impacto (−22) en f587 y rebote (−30) en f594 | 19,20–19,80 (f576–f594) | Toma 17: el telescopio | Nuevo, código propio |
| `trazo_de_tinta` (−26 dBFS) | 19,87–20,37 (f596–f611) | Tomas 17 y 18: el paquete se dibuja | Catálogo, código propio |
| `paquete_desliza` (−30 dBFS) | 20,40–21,33 (f612–f640) | Toma 18: la caja desliza | Nuevo, código propio |
| `bloqueo_tinta` suave (≤ −30 dBFS) | 21,70 (f651) | Toma 19: el bloqueo | Catálogo, código propio |
| **Silencio total, sin efectos ni música (8 f)** | 23,07–23,30 (f692–f699) | Toma 20 | — |
| `toque_regla` (−22 dBFS, único sonido) | 23,33 (f700) | Toma 21: el toque | Nuevo, código propio |
| `tinta_sube` (−34 a −16 dBFS) | 23,40–23,57 (f702–f707) | Toma 21 | Nuevo, código propio |
| `explosion` (−8 dBFS) y `chispas` en la expansión | 23,73 (f712) | Toma 21: la bola de fuego | Catálogo, código propio |
| `cola_explosion` hasta −40 dBFS | 23,77–24,23 (f713–f727) | Tomas 21 y 22 | Catálogo, código propio |
| Pausa de efectos y música antes del golpe final | 26,87–27,10 (f806–f813) | Toma 23 | — |
| `regla_golpe` grave y `golpe_grave` (−10 dBFS) | 27,03 (f811) | Toma 23: golpe 6 | Nuevo y catálogo, código propio |
| `asterisco_tic` (−30 dBFS) | 27,07–27,17 (f812–f815) | Toma 23: segunda marca | Catálogo, código propio |
| `implosion`: grave a −30 dBFS, banda de voz a −40 dBFS, corte seco | 27,13–27,70 (f814–f831) | Toma 23: implosión | Catálogo, código propio |
| `escurre` y `gotas` (−28 dBFS); gotas agudas de la regla en f866 | 28,53–28,97 (f856–f869) | Toma 24: el goteo | Catálogo, código propio |
| Último `tic` de la música | 28,97 (f869) | Toma 24 | Nuevo, código propio |
| Firma: lanzamiento del lápiz (S1 y S2) | 30,43–30,97 (c −17 a c −1) | Toma 25 | Los de la firma, código propio |

- **Música:** solo percusión, por código, otro patrón que el del short 4 (7 y 11); sin material de terceros. Licencias: `licencias.md` (lo llena producción con cada recurso).
- **Voz:** sí (por generar con el sí del dueño); empieza en f14 y no tiene silencio inicial en el empalme del bucle.

## 14. Motor y revisión

- **Cómo se hace:** gráficos por código (fotograma a fotograma) con el motor de acción: `node render.js` sobre un guion propio de este video (`guiones/tin_en_s_005.js`; el guion de la pelea todavía vive dentro de `escena.html` y hay que sacarlo), la paleta `b_noche_de_tinta`, el entorno `patio_tienda_de_computadoras` (por construir) y las cabezas oficiales de `exportar_sprites.py`; los sonidos con `sonidos/sonido.py`; el armado con ffmpeg y `postpro.py mezclar`. **Lista de construcción para producción** (quién hace cada pieza): sección 7 de la dirección, tabla de 13 piezas (entorno y versiones rotas, `pestana(marcas)`, `entra_por_grieta`, `sale_goteando`, `objeto_caido`, `telescopio_de_carton`, `regla_de_tinta`, `paquete_de_tinta`, poses nuevas, rival lila, capa de datos con tarjeta de medidas, sonidos nuevos y herramientas de control).
- **Punto de control:** antes de renderizar se presenta la lista de tomas sobre los 930 fotogramas y se espera el visto bueno; **la voz no se genera sin el sí del dueño con el número a la vista.** Con la voz real se recalcula toda la tabla de fotogramas sin mover los desfases de cada golpe ni las reglas de 2.1 de la dirección.
- **Revisión:** `herramientas/revisar_fotogramas.py` sobre el render y su resultado en `07_revision/`. En piezas por código: prueba corta de 5 s con un fotograma por pulso, hoja de contacto a 2 por segundo y todos los fotogramas de los vuelos; comprobación de medidas en el render (zona segura, franja de subtítulos libre de caras, coordenadas de 3.0, pies a y ≈ 1650, ninguna cabeza del rival a menos de 1,2 R de la de Tin o la de Tan). Controles: `revisar_texto.py` con 0 errores; `comprobar_destellos` y `postpro.py destellos` sin avisos (máximo 3 por segundo, margen de 2); `comprobar_firma`; `revisar_color.py` con la paleta declarada (≥ 85 % en el fotograma de control, ≥ 75 % en el final); el par humo–Tan; `revisar_voz.py` sin palabras perdidas; control «se entiende solo» firmado por el supervisor de continuidad; el bucle (fotograma 930 igual al 0 salvo el fondo declarado); la escucha de una persona para los sonidos; los datos contra el archivo de hechos.
- **Qué se marca:** imagen congelada, fotograma vacío, texto cortado o tapado, texto que sigue sobre el plano siguiente, elemento fuera de cuadro, tirones, demasiado tiempo sin cambio, cualquier cosa del juego, un arma que parezca de fuego, rojo sobre el rival, el rival que dé miedo o muera, un golpe sin su pausa de 6 f, un contacto de más de 2 f, un daño que no se quede, un efecto sobre una cifra o un nombre dicho, y en el teléfono que datos, subtítulos y marcas se lean.
- **Vueltas:** las correcciones por código son gratis (salvo servicios de pago, que van a `costos.md`); **las de generador no se repiten sin autorización del dueño** (`generacion.md`): aquí solo hay generador en la voz, una generación por voz y sin segundos intentos.

**Pedidos vigentes del dueño (`PARAMETROS.md`, secciones 2, 7 y 8), uno por uno.** «Plan» quiere decir que el prompt lo pide y se mide en el render; ninguno está comprobado todavía.

| Pedido | Dónde está en este prompt | Estado |
|---|---|---|
| A1 pelea con los tiempos medidos | Coreografía de cada golpe (sección 11); gramática de Keter | Plan |
| A2 aceleración y desaceleración | Mapa de velocidad (sección 11) | Plan |
| A3 mundo con profundidad e interacción | Escenario (5), carriles y choques contra el mundo en cada toma | Plan |
| A4 fuego y humo | Tomas 12 a 23; efectos (11) | Plan |
| A5 choques | Tomas 5, 6, 8, 11, 15 | Plan |
| A6 explosión e implosión | Tomas 21 y 23, por fases y con tope de destellos | Plan |
| A7 sonidos de golpes | Sección 13: cada golpe en K −1 | Plan; nadie los ha oído |
| A8 daños que se quedan | Escenario (5) y toma 25 | Plan |
| A9 rival con cuerpo | Hoja v2 de `@duda`, en la hoja Noche | Plan; lila pendiente del dueño |
| A10 paleta por tema | Paleta B (tecnología), con su porqué en 3b | Plan; confirmada por fotografía |
| A11 entorno por tema y catálogo al día | `patio_tienda_de_computadoras`, entrada al catálogo | Por construir; producción anota el catálogo |
| A12 armas dibujadas con tinta, sin armas de fuego ni sangre | `regla_de_tinta` (Tin y Tan) y paquete (rival) | Plan |
| A13 universo conectado | Conexiones del universo (11): P-001 a P-007, 38 f activos | Plan |
| A14 escala: el Short es una página | Vertical 9:16; el rival sale «por el borde de la página» | Plan |
| Firma del lápiz bumerán | Tomas 1 y 25; sección 11 | Plan |
| Subtítulos en español dentro del video, sin pista `.srt` | Secciones 7, 8 y 12 | Plan |
| Portada que nombra al sujeto | Sección 8 y toma 1 | Plan |
| Cada dato con fuente y fecha | `hechos_short5_gta_6_on_pc.md`; fuentes en la descripción | Plan; el sello de fecha se escribe el 12-04 |
| Marcas solo nombradas; ninguna persona real golpeada | Sección 10 y 12 | Plan |
| Máximo 3 destellos por segundo | Tomas 21 y 23; `comprobar_destellos` | Plan |
| Ortografía con 0 errores | `revisar_texto.py` sobre este prompt y la dirección | Ver el informe de entrega |
| El sí del dueño para créditos, rehacer y publicar | Secciones 1, 7 y 14 | Pendiente |
