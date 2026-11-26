# Prompt de video para redes — What Is GTA 6, and Is a GTA 7 Coming?

> **ESTADO (2026-11-26, versión 1):** especificación de producción del short 4 de Tin & Tan (`TIN-EN-S-004`), escrita por el director de prompts sobre `00_brief.md` (versión 2 del gancho), `02_prompt/direccion.md`, `ficha_tecnica.md` y `perfil_emocional.md`. **Manda la dirección**: cada toma de abajo es un plano (P1 a P22) de su sección 3, con los fotogramas, la coreografía, la voz y los textos de su sección 2.2, 4, 5 y 6. **La voz no está generada** (cotizada hoy en ≈ 3,4 créditos, sin aprobar) y **los fotogramas son un plan con la voz estimada**: se recalculan con la voz real, sin mover los desfases dentro de cada golpe ni las reglas de 2.1 de la dirección. El video no está renderizado.

> **Cómo se produce:** no hay generador de video ni de imágenes. El video se dibuja y se graba por código con el motor de acción (`video-studio/motor_de_accion/`: escena 3D con Tin, Tan y el rival como dibujos 2D de pie dentro del mundo) y se arma con la voz, los sonidos y la música. Por eso todas las tomas son «edición» y, en lugar de «Prompt de keyframe» y «Prompt de video», cada toma lleva su frase de cámara y su actuación en inglés, que son las que van al guion del motor. El bloque de identidad de cada ficha no se pega en tomas: el diseño oficial es el código (`palitos.py`, cabezas exportadas por `exportar_sprites.py` y la hoja v2 del rival) y se comprueba con la lista de comprobación de cada ficha.

> **Notas del director de prompts (contradicciones y huecos encontrados; ninguna cambia una frase de voz ni un dato):**
> 1. **Brief frente a dirección.** La dirección manda: «So, GTA 7?» lo dice Tan y no Tin (decisión D2, que ya lo declara); la duración es ≈ 31,5 s y no ≈ 30 s (D11); la línea 1 del brief se reparte en tres tiempos (D1) y la frase «From GTA 5 to GTA 6: thirteen years and sixty-three days.» en dos, con la pausa de voz de f629 a f696 entre ellas. Ninguna palabra cambia.
> 2. **Capa de datos: y 380–700 o y 400–700.** La sección 3 de la dirección dice 380–700 y las secciones 2, 6 y 9.2 dicen 400–700. Este prompt usa **400–700** (la que repiten tres secciones y la portada). Lo confirma fotografía.
> 3. **Amarillo en la explosión.** La sección 4.2 de la dirección pide una «bola de fuego plana con anillo amarillo» y la 3b dice que el acento `#FFD21F` **no** va en el fuego ni en el humo. **Sin resolver:** el prompt copia las dos y lo deja como pregunta abierta para fotografía (sección 11, «Efectos»). No se elige solo.
> 4. **Ficha de `@duda`.** Su «Bloque de identidad» todavía describe la versión 1 (madeja sin miembros) y la propia ficha dice que vale la versión 2 (cuerpo de palitos, madeja como cabeza). Este prompt describe la versión 2 y manda la hoja `hoja_v2_2026-11-26.png`; la ficha necesita que el creador de personajes actualice el bloque.
> 5. **Zelda y la coma.** En el short 3 se anotó que Zelda hace pausas de 0,7 a 0,8 s tras una coma; la frase de Tan «So, GTA 7?» lleva coma y no se cambia. Se escucha antes de aprobar y la pausa se comprime en edición si hace falta (la dirección deja f750–f788 para esa línea).
> 6. **Cifras y siglas en la voz.** Los números van como los escribió el brief («November 19, 2026», «GTA 7»): cómo los lea el generador («G T A», «twenty twenty-six») se comprueba al oído; no se regenera sin autorización del dueño.
> 7. **Plano P17.** La dirección no dice qué contiene la máscara circular de los dos cuadros invertidos (f664–f665). Este prompt los pone sobre el contacto lejano del rival contra el televisor, sin elementos nuevos; lo confirma fotografía.
> 8. **Subtítulo y voz de cierre.** La voz de «Subscribe. We check the facts.» llega hasta f928 y el subtítulo hasta f914: los últimos 14 fotogramas de voz van sin subtítulo porque el plano de portada no lo lleva (D20).

## 1. Ficha técnica

- **Proyecto:** 2026-11-26_tin_y_tan_what_is_gta_6
- **Tipo:** short
- **Número:** 4
- **Serie:** ninguna
- **Objetivo de aprendizaje:** no aplica
- **Generador:** ninguno: dibujo y grabación por código con el motor de acción (three.js grabado con Chromium, `palitos.py`, `efectos.py`, sonidos de `sonidos/sonido.py`) y armado con ffmpeg. Lo único que se genera es la voz (Higgsfield `seed_audio`: Kevin para Tin y Zelda para Tan)
- **Aspecto:** 9:16
- **Duración total:** 31,5 s (945 fotogramas a 30 f/s; tolerancia 30 a 33 s; se recalcula con la voz real)
- **Resolución de borrador:** 540x960 a 30 f/s; prueba corta de 5 s con un fotograma por pulso (render propio)
- **Resolución final:** 1080x1920 a 30 f/s, H.264, 945 fotogramas
- **Precio por segundo:** 0 (render propio; no hay servicio de pago de imagen ni de video)
- **Intentos estimados por toma:** 1
- **Código previsto:** TIN-EN-S-004 (hueco H01 de la tanda 01; primer video del formato de acción)
- **Objetivo comercial (dueño, 2026-11-23):** entrar al Programa de socios de YouTube lo antes posible. KPI: «se quedó a mirar» a 48 horas al menos 5 puntos por encima del short 2 a la misma edad.
- **Voz:** una generación por personaje, cotizada hoy con `estimate_audio_cost` en ≈ 3,4 créditos (Tin ≈ 2,6 y Tan ≈ 0,8). **Sin aprobar:** no se genera sin el sí del dueño.

## 2. Elenco

| Personaje | Papel en este video | Vestuario | Referencia que se sube |
|---|---|---|---|
| @tan | Pregunta («Will there be a GTA 7?» y «So, GTA 7?»), patea (golpe 2), da el mazazo (golpe 5) y el golpe doble con Tin; invita a suscribirse; atrapa el lápiz en f10, lo recibe de Tin en f874 y lo lanza en f930. Voz: Zelda al 110 % | Base de su ficha (rodete y bufanda mostaza); objeto de mano `lapiz` solo en los planos de firma y desde f874; `mazo_de_tinta` en las tomas 15 y 16 | personajes/tan/referencias/principal_tin_y_tan.png |
| @tin | Responde con las frases del brief; puño (golpe 1), gancho (golpe 3), bloqueo, bastón (golpes 4 y 6) y golpe doble; dibuja las armas con el lápiz y nunca golpea con él. Voz: Kevin al 110 % | Base de su ficha (gorra marrón, lentes, lápiz); **sin lápiz** en los planos de firma (f0–f29 y f915–f944); `baston_de_tinta` | personajes/tin/referencias/principal_tin_y_tan.png |
| @duda | El rival: la pregunta hecha cuerpo. Se dibuja sola en f30, crece a 1,5 veces, falla sus dos ataques, baja un escalón de tamaño con cada dato y no se borra del todo (queda un asterisco). Sin nombre en pantalla, sin voz, sin boca | Versión 2: cuerpo de palitos de tinta, madeja como cabeza con rizo de pregunta sin punto y dos huecos de papel por ojos; `espada_de_tinta` dibujada por ella; solo tinta `#1B1B22` | personajes/duda/referencias/hoja_v2_2026-11-26.png |

No se sube nada a un generador: las referencias son el diseño en código y solo sirven para comparar. **Ninguna persona real aparece ni se nombra.** Marcas solo nombradas (voz y capa de datos): GTA, Grand Theft Auto, Rockstar Games. «La Duda» es el nombre de trabajo del equipo: no se dice ni se escribe en el video, en la voz, en los subtítulos, en el título ni en la portada. Poses del motor usadas: `parado`, `guardia`, `carga`, `golpe`, `patada`, `agachado`, `corre1`, `corre2`, `poder`, `pisoton`, `festeja`, `resbala`, `recibe`, `vuela`, `caido`, `recogido`; poses de Tan de la ficha (`pregunta`); expresiones: `curiosidad`, `concentrado`, `eureka`, `sorpresa`, `feliz`. Tin y Tan miden ≈ 2,2 u; el rival entra a 1,25 veces su altura y crece a 1,5.

## 3. Idea en una línea

La pregunta «¿habrá GTA 7?» se dibuja sola, enorme, como un rival de tinta, y Tin y Tan la bajan a golpes de lo general a lo particular (qué es GTA, qué es GTA 6, cuánto se esperó) hasta la respuesta honesta, fechada: Rockstar no ha anunciado ninguno. Por eso el rival no se borra: queda un asterisco. Quien lo ve debe sentir curiosidad en el arranque, activación que sube con cada golpe, asombro en la cuenta de trece años y sesenta y tres días, y alivio con humor al final.

## 4. Estilo global

Bloque que se pega igual al final de toda descripción de plano que se pase al motor.

```text
Flat 2D ink drawing: 2D stick-figure characters standing inside a real 3D video game store seen with depth and parallax. Two neutrals plus one accent: cool light paper (#DCE6EE wall, #F4F1EA floor with a faint grid) and near-black ink (#1B1B22) for lines, bodies, the ink figure, drawn weapons and all text; ONE accent, highlighter yellow #FFD21F, only as a highlighter strip behind data text and as the 2 to 4 frame impact star. Tin keeps his orange head (#E07A2E), Tan her teal head (#2F7F7A), mustard scarf and pencil (#E8B33B): identity colors, not accents. Even bright store light, soft contact shadows (#A7B0BC, opacity 0.2 to 0.3), props in #666B76 and white (#FFFFFF near, #B9C6D2 far). Fire is flat, in two hard-edged tones (core #FFF4B8, edge #B81414), built in phases; smoke is #666B76 with an ink outline. Impacts are short 2-frame cuts, not camera shake. Hard cuts, fixed or slow push-in cameras, no gradients on shapes, no glow, no neon.
```

**Negativo global:**

```text
any text, logo, box art or typography inside the 3D world, any image, character, logo, typeface or music from the game, any real person, firearms or firearm silhouettes, blood, red on the ink figure, gradients on shapes, glow, neon, lens flare, camera shake, strobing, pure white over the whole frame, negative-color frames outside the two masked ones, yellow on characters, weapons, fire or smoke, blurry particle fire, extra characters, extra fingers, uppercase centered titles, photographs, a mouth or pupils on the ink figure
```

## 5. Escenarios

- **tienda_de_videojuegos** (entorno nuevo; entra al catálogo del motor con los temas juegos, compras y estrenos): una tienda de videojuegos la noche del lanzamiento, sin logotipos, sin texto, sin arte en las cajas y sin figuras humanas. Luz de tienda, pareja y alta, con sombra de contacto de cada personaje. La noche se ve solo por el `escaparate` (vidrio en tinta con 5 puntos claros). Hoja Voltaje, paleta C (`motor_de_accion/paletas/c_alto_voltaje.json`). Al inicio está entera; al final conserva todos los daños. Medidas aproximadas en u (Tin y Tan miden ≈ 2,2 u; las ajusta producción); suelo de 14 por 20 u.

| Pieza (nombre de catálogo) | Medidas ≈ (u) | Dónde | Qué le pasa | Queda así |
|---|---|---|---|---|
| `suelo_tienda` | 14 × 20 | — | Quemadura (f686); papeles corridos (f797) | Quemadura; cajas y papeles corridos al centro |
| `pared_fondo` | 14 × 7, lisa, `#DCE6EE` | z = −10 | Quemadura (f686). **No se agujerea** | Mancha de quemadura |
| `escaparate` | 3 × 2,2 | Pared izquierda, cerca de cámara | Nada | Intacto |
| `estante_izquierdo` | 4,5 × 3,2 × 0,6; 4 baldas; 24 `caja_de_juego` | x = −5,2 | Choque (f100) | Inclinado ≈ 12°, 8 cajas en el suelo |
| `estante_derecho` | igual | x = +5,2 | Rebote (f506) | Una balda caída, 6 cajas en el suelo |
| `caja_de_juego` | 0,32 × 0,42 × 0,06, blanca con una banda de tinta, lisa | Estantes y pila | Caen | En el suelo |
| `pila_de_cajas` | Pirámide de 10 | (−1,2; −5) | Pisotón (f60) | 3 caídas desde el principio |
| `cartel_de_pie` | 1,0 × 2,2, en blanco con marco de tinta | (−2,6; −3) | Lo parte el rival (f196) | Partido en dos, en zigzag |
| `postes_de_fila` (4, con cinta) | 1,0 de alto, `#666B76` | Derecha, delante | Los tumba el rival (f162) | Tumbados |
| `mostrador` | 3,2 × 1,0 × 0,8; `#666B76`, tapa blanca | (2,8; −4,5) | Grieta (f304); se parte (f570) | Partido en dos |
| `caja_registradora` → `caja_registradora_rota` | 0,6 × 0,5 × 0,45 | Sobre el mostrador | Sale despedida (f572) y cae (f588) | Gaveta afuera, pantalla doblada, cinta de papel desenrollada |
| `isla_televisor` con `televisor_de_exhibicion` | Columna de 1,6; pantalla de 2,4 × 1,4, en blanco | (0; −7,5) | Punta clavada (f484), fuego (f496), explosión (f662) | Reventado y volcado |
| `banderines` | Cuerda de 12 triángulos | De pared a pared, y ≈ 5,5 | Onda de la explosión | Chamuscados, colgando de un lado |
| `estante_fondo` con `mando_mostaza` | Repisa de 1,2; mando de 1,1 R × 0,6 R (`objeto="control"` de `palitos.py`), mostaza `#E8B33B` con contorno de tinta | Pared del fondo, izquierda | **Nada: no se toca** | Intacto |

**Cámaras del motor** (el `temblor` del catálogo no se usa): C0 «portada», posición (0; 2,4; 13,5) a la altura de los ojos, mira a (0; 2,1; 0), fija (Tan en x ≈ 259 px, Tin en x ≈ 821 px, pies en y ≈ 1651 px; se miden en el fotograma 0). C1 «lectura», (0; 5,2; 14) alta, mira a (0; 1,6; −3): general, donde se leen los datos y el daño; se coloca para que la base de la pared del fondo caiga en y ≈ 1110 (± 15 px). C2 «lateral», (± 7; 1,3; 1) baja, de perfil, mira a (0; 1,4; 0): golpes y vuelos en profundidad. C3 «héroe», (0; 0,5; 6) a ras de suelo detrás de Tin y Tan, mira a (0; 4; −8): la explosión. C4 «vertical», (3,4; 0,6; −1,5) contrapicado junto al mostrador, mira a (2,8; 4; −4,5); invertida (picado) para el mazazo.

**Reparto del cuadro (1080x1920):** y 400–700 capa de datos sobre la pared lisa del fondo; y 905–1085 franja de subtítulos; y 1105–1700 piso de acción. Ningún contacto ni choque ocurre detrás de la franja.

## 6. Tomas

<!--
Las 22 tomas son los 22 planos de la dirección, sección 3 (P1 a P22), sobre 945 fotogramas a 30 f/s. Todas son «edición»:
dibujo por código con el motor de acción. «f» es el fotograma desde el inicio. Los segundos de la duración son f/30.
Cada toma trae su frase de cámara en inglés (la de la dirección) y, donde la dirección la escribió, su frase de actuación.
-->

### Toma 1 — Firma y portada (P1)

- **Duración:** 1,00 s (30 f, f0–f29)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** tienda_de_videojuegos, entera, con el televisor en blanco al centro (y ≈ 744–1075) y los dos estantes fugando hacia él
- **Encuadre:** general frontal C0 a la altura de los ojos. Tan a la izquierda (x ≈ 259 px) y Tin a la derecha (x ≈ 821 px), de perfil, cabeza a 25°, caras de `curiosidad` dentro de la zona útil. El `mando_mostaza` sobre la repisa del fondo izquierdo
- **Cámara:** fija. Frase de cámara: static locked-off shot, eye level, store aisle in depth
- **Acción:** el lápiz ya viene girando en f0, entero y nítido, con estela plana de dos copias; vuelve en 10 f y Tan lo atrapa en f10 con el brazo de firma (95°, 108°); retroceso de brazo y cuerpo. Tin sin lápiz, con su saltito. El rival no aparece hasta f30
- **Audio:** Tan empieza en f14: «Will there be a GTA 7?» (termina en f64, dentro de la toma 2). Sonidos de la firma S3 y S4 (regreso y atrapada), sin cambios
- **Texto en pantalla:** portada «GTA 7?» (≈ 150 px, subrayado amarillo) y debajo «Facts, Checked» (≈ 92 px), y 400–700, quieta f0–f29. Sin subtítulo
- **Referencia:** firma del canal (`canales/nostalgia-tin-y-tan/FIRMA_LAPIZ_BUMERAN.md`) y portada del short 3

### Toma 2 — El rival se dibuja y crece (P2)

- **Duración:** 1,33 s (40 f, f30–f69)
- **Personajes:** @tan, @tin, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** subjetivo de Tan, contrapicado suave: el rival al fondo del pasillo
- **Cámara:** empuje lento +5 % en 40 f. Frase de cámara: low-angle POV, slow push-in as the ink figure draws itself and grows
- **Acción:** el rival se dibuja de un solo trazo (f30–f45), crece a 1,5 veces la altura de Tin (f46–f69) y da un pisotón en f60: caen 3 cajas de la pila. Tan retrocede en f46–f69 con `sorpresa`; Tin se adelanta
- **Audio:** Tan termina «Will there be a GTA 7?» en f64. `trazo_de_tinta` (rasgueo de lápiz, 16 f) en f30–f45; `choque_suelo` bajo y `cajas_caen` en f60
- **Texto en pantalla:** subtítulo f30–f64 «¿Habrá un GTA 7?»
- **Referencia:** entrada del rival «se dibuja de un trazo» de la biblia del universo

### Toma 3 — Golpe 1: el puño (P3)

- **Duración:** 1,00 s (30 f, f70–f99)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** lateral bajo C2 izquierda, siluetas de perfil; Tan en guardia al fondo
- **Cámara:** fija. Frase de cámara: side profile, low angle, static
- **Acción:** Tin puño derecho (el lápiz va en la otra mano): anticipación f70–f75, pausa f76–f81, **contacto f82–f83** (salto de posición, arco de borrón naranja, estrella ≤ 0,6 u, 5 a 7 gotas de tinta), lanzamiento f84–f87 con 3 calcos, el rival vuela en profundidad f88–f99 girando y achicándose, reloj de la escena a 0,25. Frase de actuación: Tin plants his feet, pulls his fist back and holds completely still for a beat, then strikes in a single frame
- **Audio:** silencio de efectos f76–f81; `silbido` corto y `golpe` en f81 (un fotograma antes del contacto). Tin en f84: «GTA is short for Grand Theft Auto:»
- **Texto en pantalla:** subtítulo f84–f140 «GTA es Grand Theft Auto:». Dato, renglón 1 de la tarjeta: «GTA = Grand Theft Auto», entra en f86 y queda quieto f91–f275
- **Referencia:** el golpe de la referencia medida por Keter (pausa, contacto de 2 f, desaceleración en el aire)

### Toma 4 — Impacto contra el estante izquierdo (P4)

- **Duración:** 0,07 s (2 f, f100–f101)
- **Personajes:** @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** cuadro de impacto: el estante de cerca, líneas de tinta
- **Cámara:** fija; corte de impacto de entrada. Frase de cámara: impact frame, close on the shelf
- **Acción:** el rival choca contra `estante_izquierdo`: el estante queda inclinado ≈ 12° y pierde 8 cajas; polvo con contorno
- **Audio:** `choque_madera` y `cajas_caen` en f100
- **Texto en pantalla:** ninguno (el dato de la toma 3 sigue quieto en el plano que viene)
- **Referencia:** impacto en cuadros cortos con corte de cámara (referencia medida)

### Toma 5 — El rival sale del estante y carga (P5)

- **Duración:** 1,00 s (30 f, f102–f131)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** general alto C1 de toda la tienda; el estante izquierdo inclinado
- **Cámara:** fija. Frase de cámara: high wide shot of the whole store, static
- **Acción:** Tin se recupera a la guardia (f102–f107). El rival sale del estante, baja a 1,4 veces y carga corriendo hacia ellos (f108–f137; reloj de la escena a 1,3 con borrón de movimiento)
- **Audio:** Tin sigue en «GTA is short for Grand Theft Auto:» (hasta f140)
- **Texto en pantalla:** subtítulo «GTA es Grand Theft Auto:» (hasta f140); el renglón 1 sigue quieto
- **Referencia:** el contraataque que abre la curiosidad siguiente: «no bastó un dato»

### Toma 6 — Golpe 2: la patada (P6)

- **Duración:** 1,13 s (34 f, f132–f165)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** lateral bajo C2 derecha, a ras de suelo
- **Cámara:** fija. Frase de cámara: side profile, floor level, static
- **Acción:** Tan patada giratoria: anticipación f132–f137, pausa f138–f143, **contacto f144–f145**, lanzamiento f146–f149; el rival resbala f150–f161 (0,25) y tumba los 4 `postes_de_fila` en f162; recuperación f163–f168 (Tan `festeja` 4 f). Frase de actuación: Tan spins on one foot and kicks; the ink figure slides across the floor
- **Audio:** `golpe` un tono arriba en f143; `roce_suelo` y `postes_caen` (4 golpes metálicos escalonados) en f150–f162. Tin en f146: «a game series that started in 1997,»
- **Texto en pantalla:** subtítulo f146–f223 «una serie de juegos que empezó en 1997»
- **Referencia:** patada de la referencia medida

### Toma 7 — Contraataque y carrera al mostrador (P7)

- **Duración:** 3,67 s (110 f, f166–f275)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** general alto C1; los postes tumbados y el mostrador al fondo derecho
- **Cámara:** empuje lento +6 % hacia el mostrador. Frase de cámara: high wide, slow push-in toward the counter
- **Acción:** el rival se levanta solo (1,25 veces), lanza un golpe (f186–f195) y falla: Tin se agacha en f194 y el brazo del rival parte el `cartel_de_pie` en f196. El rival salta al mostrador (f236–f250). Tin corre (f252–f269; reloj a 1,3) y toma carrera: anticipación f270–f275
- **Audio:** Tin termina «a game series that started in 1997,» en f223 y dice en f229: «made today by Rockstar Games.» (hasta f268). `choque_madera` seco, más agudo, en f196
- **Texto en pantalla:** subtítulos f146–f223 y f229–f268 «y que hoy hace Rockstar Games.». Tarjeta: renglón 2 «a game series · since 1997» entra en f190 y queda quieto f195–f275; renglón 3 «made today by Rockstar Games» entra en f231 y queda quieto f236–f275
- **Referencia:** el rival que falla un golpe: regla «nadie golpea a un caído»

### Toma 8 — Golpe 3: el gancho (P8)

- **Duración:** 0,93 s (28 f, f276–f303)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** contrapicado vertical C4 junto al mostrador
- **Cámara:** fija; corte en el movimiento. Frase de cámara: worm's-eye view beside the counter, static
- **Acción:** Tin gancho ascendente: pausa f276–f281, **contacto f282–f283**, lanzamiento vertical f284–f287; el rival flota arriba, en la banda alta derecha, f288–f299 (0,25) y cae f300–f303
- **Audio:** `golpe` grave y `silbido` ascendente en f281–f282; f288–f299 casi silencio, solo la voz; `silbido_caida` desde f300. Tin en f284: «GTA 6 came out on November 19, 2026.» (hasta f376)
- **Texto en pantalla:** subtítulo f284–f376 «GTA 6 salió el 19 de noviembre de 2026.»
- **Referencia:** el golpe ascendente con flotación de la referencia medida

### Toma 9 — Impacto contra el mostrador (P9)

- **Duración:** 0,07 s (2 f, f304–f305)
- **Personajes:** @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** cuadro de impacto cenital del mostrador
- **Cámara:** fija; corte de impacto. Frase de cámara: top-down impact frame on the counter
- **Acción:** el rival choca contra el `mostrador`: grieta a lo largo de la tapa; polvo con contorno
- **Audio:** `choque_pilar` en f304–f305
- **Texto en pantalla:** ninguno
- **Referencia:** choque grande con corte a cuadro de impacto

### Toma 10 — El mostrador agrietado y el dato de la fecha (P10)

- **Duración:** 2,57 s (77 f, f306–f382)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** general alto C1; mostrador agrietado
- **Cámara:** fija; corte de impacto. Frase de cámara: high wide, static
- **Acción:** Tin se recupera (f306–f311). El rival se sacude (1,1 veces) sobre el mostrador. Los tres quedan casi quietos mientras se lee el dato
- **Audio:** Tin termina «GTA 6 came out on November 19, 2026.» en f376
- **Texto en pantalla:** dato «GTA 6» / «out since Nov 19, 2026»: entra en f306 y queda quieto f311–f380. Subtítulo «GTA 6 salió el 19 de noviembre de 2026.» hasta f376
- **Referencia:** respiro después del golpe 3

### Toma 11 — Detalle: el lápiz dibuja el bastón (P11)

- **Duración:** 0,40 s (12 f, f383–f394)
- **Personajes:** @tin
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** macro: la punta del lápiz de Tin dibujando el `baston_de_tinta` de un solo trazo
- **Cámara:** fija; corte seco. Frase de cámara: macro close-up of the pencil tip drawing an ink staff
- **Acción:** el lápiz dibuja el bastón (f383–f394); `poder`. Frase de actuación: Tin draws a staff in one stroke of the pencil
- **Audio:** `trazo_de_tinta` en f383–f394. Tin en f383: «It's the sixth numbered game.» (hasta f422)
- **Texto en pantalla:** subtítulo f383–f422 «Es el sexto juego numerado.». Dato «the sixth numbered game»: entra en f385 y queda quieto f390–f426
- **Referencia:** plano de detalle (tipo de plano del manual 11)

### Toma 12 — El bloqueo: la espada del rival (P12)

- **Duración:** 2,97 s (89 f, f395–f483)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos, con el televisor en blanco centrado al fondo
- **Encuadre:** general alto C1
- **Cámara:** fija; corte seco. Frase de cámara: high wide, static, the blank television centered in the back
- **Acción:** el rival baja del mostrador, dibuja su `espada_de_tinta` con un mechón (f440–f451) y ataca: anticipación f458–f463, pausa f464–f469; **Tin bloquea con el bastón en f470–f471**. La punta se parte y vuela (f472–f483, reloj a 0,3) hacia el televisor; Tan con `sorpresa`; el rival mira su espada rota. Tin: anticipación f480–f485. Frase de actuación: The ink figure looks at its broken sword, puzzled
- **Audio:** `trazo_de_tinta` en f440–f451; `bloqueo_tinta` (choque seco con cola corta) en f470. Tin en f429: «Rated M: seventeen and over.» (hasta f483)
- **Texto en pantalla:** subtítulo f429–f483 «Para mayores de 17.». Dato «rated M · 17 and over»: entra en f431 y queda quieto f436–f487
- **Referencia:** el bloqueo con arma de la referencia del dueño

### Toma 13 — Impacto: la punta clava el televisor (P13)

- **Duración:** 0,07 s (2 f, f484–f485)
- **Personajes:** ninguno
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** cuadro de impacto: la pantalla en blanco se agrieta en estrella
- **Cámara:** fija; corte de impacto. Frase de cámara: impact frame, close on the cracked blank screen
- **Acción:** la punta de la espada se clava en el `televisor_de_exhibicion`; la pantalla queda agrietada en estrella
- **Audio:** `vidrio_grieta` en f484
- **Texto en pantalla:** ninguno
- **Referencia:** motivo visual que vuelve: el televisor en blanco del centro

### Toma 14 — Golpe 4: el bastón y la mecha (P14)

- **Duración:** 2,20 s (66 f, f486–f551)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** lateral C2 izquierda; llama pequeña y plana al fondo, sobre el televisor
- **Cámara:** fija; corte de impacto. Frase de cámara: side profile, static, small flat fire in the back
- **Acción:** pausa de Tin f486–f491, **contacto f492–f493** (bastón, barrido horizontal), lanzamiento f494–f497, vuelo f498–f505 (0,25), rebote en `estante_derecho` f506–f507 (pierde una balda y 6 cajas) y el rival cae de pie (1,0 veces). Chispas del televisor f486–f495; **fuego, fase 1** desde f496 (llama pequeña, 3 dibujos de 2 f cada uno); humo con contorno desde f506. Tin añade un bloque al bastón: es un mazo (f540–f551)
- **Audio:** `chispas` f486–f495; `baston_golpe` (madera hueca) en f491–f492; `fuego_enciende` en f496; `choque_madera` en f506; `trazo_de_tinta` en f540–f551. Tin en f494: «Each numbered game tells a new story.» (hasta f550)
- **Texto en pantalla:** subtítulo f494–f550 «Cada juego numerado cuenta una historia nueva.». Dato «each numbered game:» / «a new story»: entra en f496 y queda quieto f501–f553
- **Referencia:** el bastón de la referencia que vio el dueño; fuego plano por fases de la referencia medida

### Toma 15 — Golpe 5: el mazo y la caja registradora (P15)

- **Duración:** 2,20 s (66 f, f552–f617)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** picado sobre el mostrador, C4 invertida; la caja viene hacia cámara
- **Cámara:** fija; corte en el movimiento. Frase de cámara: high-angle shot over the counter, the register flies toward camera
- **Acción:** Tin lanza el mazo a Tan (f552–f556); Tan lo levanta (f558–f563), pausa f564–f569 y **contacto f570–f571**: el rival aplastado contra el mostrador, que se parte en dos. La `caja_registradora` sale despedida (f572–f575), vuela hacia cámara (f576–f587, 0,25) y cae abierta (f588–f589): queda `caja_registradora_rota`. **Fuego, fase 2** desde f572 (la llama crece al doble; el borde cambia de forma, no parpadea). El rival (0,9 veces, con un mechón suelto) se sube a la isla del televisor. Tin y Tan se miran (f600–f606). Frase de actuación: Tan raises an ink mallet over her head, holds, and brings it straight down
- **Audio:** `silbido` f552–f557; `mazo_golpe` (el más grave hasta aquí) y `choque_madera` en f569–f570; `campanilla_caja` en f588 (el único sonido amable del video). Tin en f572: «From GTA 5 to GTA 6:» (hasta f628)
- **Texto en pantalla:** subtítulo f572–f628 «De GTA 5 a GTA 6:». Línea de apoyo, pequeña: «from GTA 5 to GTA 6», entra en f574 y queda quieta f579–f640
- **Referencia:** el mazo de cerrar una cuenta; la caja «marca» que empieza la suma

### Toma 16 — La carrera lenta y el golpe doble (P16)

- **Duración:** 1,53 s (46 f, f618–f663)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** lateral C2 derecha, cámara lenta
- **Cámara:** fija; corte en el movimiento. Frase de cámara: side profile, static, slow motion
- **Acción:** Tin y Tan corren juntos a cámara lenta (f618–f628, reloj a 0,3); anticipación f629–f634; pausa f635–f640 con silencio total; **golpe doble (bastón y mazo a la vez), contacto f641–f642**; lanzamiento f643–f646; vuelo lento f647–f661 hacia el televisor en llamas; contacto lejano f662–f663. Frase de actuación: Both run in, hold, and strike together
- **Audio:** subida de 11 f en f618–f628 (looming auditivo); **silencio total, también de música, en f635–f640**; `golpe_doble` en f640–f641; `vidrio_grieta` en f662. Pausa de voz de f629 a f696
- **Texto en pantalla:** ninguno (la línea de apoyo sale en f643; el dato no comparte plano con el pico)
- **Referencia:** la referencia frena 11 cuadros antes del contacto clave

### Toma 17 — Cuadros invertidos del contacto lejano (P17)

- **Duración:** 0,07 s (2 f, f664–f665)
- **Personajes:** @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** dos cuadros invertidos, solo dentro de una máscara circular, sobre el contacto del rival contra el televisor
- **Cámara:** fija; corte de impacto. Frase de cámara: two inverted impact frames inside a circular mask
- **Acción:** 2 cuadros con los colores invertidos y máscara; es la única vez en el video. Nunca blanco puro a pantalla completa
- **Audio:** sin efecto nuevo (la `explosion` entra en f671)
- **Texto en pantalla:** ninguno
- **Referencia:** corte triple sin temblor de la referencia de Alan Becker

### Toma 18 — La explosión (P18)

- **Duración:** 1,03 s (31 f, f666–f696)
- **Personajes:** @tin, @tan
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** héroe abierto: contrapicado a ras de suelo C3, Tin y Tan de espaldas y agachados, la bola de fuego plana en la banda alta
- **Cámara:** fija; corte de impacto. Frase de cámara: low-angle hero shot from behind the two figures, flat fireball above
- **Acción:** líneas radiales f666–f670; claro de paleta (`#FFF4B8`) con máscara circular (55 % del cuadro como máximo, opacidad 0,6) f671–f674; bola de fuego plana con anillo y restos f675–f685 (cada dibujo dura 2 f); enfriamiento f686–f696 con onda en el suelo. Queda el televisor reventado y la isla volcada; quemadura en el suelo y en la pared (sin agujero) desde f686; los banderines chamuscados, colgando de un lado
- **Audio:** `explosion` en f671 (la referencia la pone en la expansión, no en la ignición); cola grave que cae y crepitar bajo desde f686. Sin voz (pausa de voz hasta f696)
- **Texto en pantalla:** ninguno
- **Referencia:** explosión por fases de la referencia medida; el pico cae en una cifra comprobada, no en la respuesta

### Toma 19 — El respiro: la cuenta (P19)

- **Duración:** 2,67 s (80 f, f697–f776)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos, con el daño acumulado
- **Encuadre:** general alto C1; revelado: el humo despeja y deja ver la cifra
- **Cámara:** fija; corte seco. Frase de cámara: high wide, static, outlined smoke clears
- **Acción:** el humo con contorno despeja (f697–f720; nunca pasa por delante de la cabeza de Tan). Tin con `sorpresa`; Tan con la boca abierta y quieta (f703–f745) y `pregunta` en f750. El rival se recompone del hollín (0,8 veces; f740–f775)
- **Audio:** Tin en f697: «thirteen years and sixty-three days.» (hasta f746), solo la voz sobre la cola grave, sin golpe. Tan en f750: «So, GTA 7?» (hasta f788)
- **Texto en pantalla:** subtítulos f697–f746 «trece años y sesenta y tres días.» y f750–f788 «¿Y GTA 7?». Dato «13 years, 63 days» / «GTA 5: Sep 17, 2013 · GTA 6: Nov 19, 2026»: entra en f697 y queda quieto f702–f775
- **Referencia:** respiro de lectura tras el pico

### Toma 20 — Golpe 6: la implosión (P20)

- **Duración:** 1,27 s (38 f, f777–f814)
- **Personajes:** @tin, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos
- **Encuadre:** medio frontal del rival; el bastón de Tin entra por el borde del cuadro
- **Cámara:** fija; corte en el movimiento. Frase de cámara: medium frontal shot, static, the figure collapses inward
- **Acción:** Tin anticipación f783–f788, pausa f789–f794, **contacto f795–f796**; **implosión** f797–f814 (reloj de 0,6 a 1,4, acelera hacia adentro): 3 anillos de tinta que se cierran, la tinta se recoge, el rival se borra desde la cabeza, se lleva el humo y apaga las últimas llamas; queda un mechón de ≈ 1,5 R que tiembla. Los papeles y cajas del suelo se deslizan ≈ 0,5 u hacia el centro y ahí se quedan
- **Audio:** `baston_golpe` un tono más bajo que en el golpe 4, en f794–f795; `implosion` (barrido de agudo a grave, hacia adentro) en f797–f814, con corte seco en f814. Tan termina «So, GTA 7?» en f788; Tin en f797: «Rockstar hasn't announced one. As of today.» (hasta f865)
- **Texto en pantalla:** subtítulo f797–f865 «Rockstar no ha anunciado ninguno. A hoy.». Dato con placa «GTA 7:» / «not announced» y sello «as of» seguido de la fecha de la relectura del día de publicar: entra en f799 y queda quieto f804–f872
- **Referencia:** el mismo gesto del golpe 4 con resultado distinto: aquí no hay dato que alcance

### Toma 21 — El asterisco y la salida por la grieta (P21)

- **Duración:** 3,33 s (100 f, f815–f914)
- **Personajes:** @tin, @tan, @duda
- **Método:** edición
- **Escenario:** tienda_de_videojuegos, con todo el daño a la vista
- **Encuadre:** general alto C1
- **Cámara:** fija; corte seco. Frase de cámara: high wide, static, all the damage in view
- **Acción:** el bastón y el mazo se deshacen en gotas (f830–f841); Tin baja el arma con `curiosidad` ante el resto. El mechón se anuda en un **asterisco** de ≈ 48 px (f842–f847), que se queda; lo último del trazo se escurre por una grieta del suelo, a la derecha (f852–f867). Tin le lanza el lápiz a Tan (f868–f874); Tan lo atrapa y los dos caminan a su marca (f878–f914). Frase de actuación: Tin lowers the staff; what is left of the figure ties itself into a small asterisk and the last stroke slips into a crack in the floor
- **Audio:** `asterisco_tic` (6 golpecitos de lápiz, uno por trazo) en f842–f847; `escurre` (roce que baja de tono) en f852–f867. Tin termina la respuesta en f865. Tan en f878: «Subscribe. We check the facts.» (hasta f928). Música: un solo pulso suave
- **Texto en pantalla:** subtítulo f878–f914 «Suscríbete. Aquí comprobamos los datos.». El dato «GTA 7: not announced» queda quieto hasta f872 y sale
- **Referencia:** remate visual del universo: la marca final y la salida del rival (siembras P-001 y P-002)

### Toma 22 — Cierre de la firma (P22)

- **Duración:** 1,00 s (30 f, f915–f944)
- **Personajes:** @tan, @tin
- **Método:** edición
- **Escenario:** tienda_de_videojuegos, con los daños (excepción declarada del empalme)
- **Encuadre:** general frontal C0, el mismo cuadro de la portada: mismas poses, mismo texto, misma cámara
- **Cámara:** fija; borrón de 3 f de entrada (el de la firma). Frase de cámara: static locked-off shot, same framing as the first frame
- **Acción:** el texto de portada entra en f915; Tan: anticipación f921–f926, impulso f926–f930, suelta f930 y vuelo del lápiz f930–f944 (15 f). Tin sin lápiz, cabeza a 25°. Nada más se mueve: el fuego y el humo se acabaron en f814 y el rival salió en f867. El fotograma 945 sería el fotograma 0 salvo el fondo
- **Audio:** la voz de Tan termina en f928 (c −17); sonidos S1 y S2 de la firma; música 6 dB más baja desde c −24
- **Texto en pantalla:** portada «GTA 7?» / «Facts, Checked» (como en f0). Sin subtítulo
- **Referencia:** toma 1 de esta versión; el vuelo del lápiz cierra el bucle

## 7. Audio

- **Voz (por generar; una sola generación por voz, sin segundos intentos):** Tan con Zelda y Tin con Kevin, Higgsfield `seed_audio`, voces ya elegidas por el dueño; después `atempo=1.10` (voz siempre al 110 %, la cámara lenta no la toca), −14 LUFS y armado con los fotogramas de la sección 6. **Costo cotizado hoy con `estimate_audio_cost`: ≈ 3,4 créditos (Tin ≈ 2,6 y Tan ≈ 0,8); sin aprobar.** Nadie ha oído las voces: «Grand Theft Auto», «Rockstar», «GTA 7», «2026» y «sixty-three» se comprueban al oído; `revisar_voz.py` no debe perder ninguna palabra.

Guion de voz (inglés, exacto; los fotogramas son el plan con la voz estimada, Tan a ≈ 3,5 sílabas por segundo y Tin a ≈ 5,5):

| Quién | Texto exacto | Fotogramas | Plano |
|---|---|---|---|
| Tan | Will there be a GTA 7? | f14–f64 | P1 y P2 |
| Tin | GTA is short for Grand Theft Auto: | f84–f140 | P3 y P5 |
| Tin | a game series that started in 1997, | f146–f223 | P6 y P7 |
| Tin | made today by Rockstar Games. | f229–f268 | P7 |
| Tin | GTA 6 came out on November 19, 2026. | f284–f376 | P8 y P10 |
| Tin | It's the sixth numbered game. | f383–f422 | P11 |
| Tin | Rated M: seventeen and over. | f429–f483 | P12 |
| Tin | Each numbered game tells a new story. | f494–f550 | P14 |
| Tin | From GTA 5 to GTA 6: | f572–f628 | P15 |
| Tin | thirteen years and sixty-three days. | f697–f746 | P19 |
| Tan | So, GTA 7? | f750–f788 | P19 y P20 |
| Tin | Rockstar hasn't announced one. As of today. | f797–f865 | P20 y P21 |
| Tan | Subscribe. We check the facts. | f878–f928 | P21 y P22 |

**Texto para generar cada voz** (una pieza por personaje; las líneas son las del brief, separadas por una línea en blanco; el editor abre las pausas de los dos puntos y de la coma en los tiempos de la tabla; sin coletilla, porque la cotización es de este texto: si se añade una, hay que recotizar):

Voz de Tan (Zelda), una sola generación:

```text
Will there be a GTA 7?

So, GTA 7?

Subscribe. We check the facts.
```

Voz de Tin (Kevin), una sola generación:

```text
GTA is short for Grand Theft Auto: a game series that started in 1997, made today by Rockstar Games.

GTA 6 came out on November 19, 2026. It's the sixth numbered game. Rated M: seventeen and over.

Each numbered game tells a new story.

From GTA 5 to GTA 6: thirteen years and sixty-three days.

Rockstar hasn't announced one. As of today.
```

- **Subtítulos:** `02_prompt/subtitulos_es.srt` (pista para YouTube y texto quemado) y `subtitulos.srt` en inglés, igual que la voz. Tiempos estimados; los hace producción con la voz real. En la sección 12 está el texto exacto.
- **Música:** hecha por código, **solo percusión** (0 créditos, sin melodía: nada que pueda parecerse a la música del juego ni a la de nadie). 120 pulsos por minuto (un pulso cada 15 f), ≈ −26 LUFS, atenuada bajo la voz. Sube una capa después de cada golpe; calla en las pausas; calla del todo en f635–f640; vuelve en f697 en su capa más baja; en f815–f914 queda un solo pulso suave; se baja 6 dB desde c −24, como pide la firma. La confirma el diseñador de sonido.
- **Efectos:** los de la sección 13, hechos con código.

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → … → Toma 22 (y vuelve a la toma 1: el fotograma 945 es el fotograma 0, salvo el fondo).
- **Transiciones:** corte directo. Cortes en el movimiento: tomas 3, 6, 8, 15, 16 y 20. Cortes de impacto (cuadros de 2 f): tomas 4, 9, 13 y 17, más la entrada de las tomas 5, 10, 14 y 18, que cortan sobre el impacto. Cortes secos: el resto. Borrón de 3 f solo en la entrada de la toma 22 (el de la firma). Sin barridos, sin negativo (salvo los 2 cuadros con máscara de la toma 17), sin temblor de cámara.
- **Texto en pantalla:** se dibuja en el mismo render (capa de datos, subtítulos quemados y portada), nunca dentro del mundo 3D. Detalle en la sección 12. Un dato a la vez; el texto nunca contradice lo que se oye.
- **Portada:** el fotograma 0, en 1080x1920 (`miniatura.png`). Texto «GTA 7?» / «Facts, Checked» (4 palabras en 2 renglones, mayúscula inicial en cada una), entre y 400 y 700; el objeto del centro es el televisor en blanco; las caras de Tan y Tin, de perfil, dentro de la zona útil. No da la respuesta ni insinúa fecha o tráiler; no usa la tipografía ni los colores del juego.
- **Formato de salida:** 1080x1920, 30 f/s, H.264, audio AAC a 48 kHz; archivo `06_final/tin_y_tan_short04_v1.mp4`; pista `subtitulos_es.srt` aparte.

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | 0 s (las 22 tomas son edición; 31,5 s se resuelven en el motor y en edición) | 0 |
| Keyframes | 0 | 0 |
| Remates en resolución final | 0 | 0 |
| Voz (Kevin para Tin ≈ 2,6 y Zelda para Tan ≈ 0,8; una generación por voz) | 2 generaciones, sin generar | ≈ 3,4 créditos, cotizados hoy con `estimate_audio_cost`; **sin aprobar** |
| **Total estimado** | 0 créditos de imagen y de video; la voz, por autorizar | ≈ 3,4 créditos |

Lo que reporta `validar_prompt.py` (2026-11-26): 22 tomas, 31,51 s en pantalla, **0 s generados** (todo es edición), presupuesto de generación de video ~0 s con 1 intento por toma. El validador no ve la voz: por eso el gasto real de este video, ≈ 3,4 créditos, se declara aquí y en `costos.md` cuando el dueño lo autorice.

## 10. Restricciones críticas

Van al inicio de la especificación de cada plano que se pase al motor, antes de la descripción. Son las que no se negocian.

```text
CRITICAL: no text, captions, subtitles, logos or watermarks unless listed in section 12.
CRITICAL: the character looks identical in every shot (same design, colors, proportions).
CRITICAL: hard cuts only, no morphing between shots.
CRITICAL: every figure, name or claim on screen comes from the project's facts file, with source and date.
CRITICAL: nothing from the game on screen: no images, no logos, no typeface, no music, no character names, no plot; no trailer or fan concept of a next game; blank television, blank sign, plain boxes.
CRITICAL: no real person or brand is ever hit, broken or burned: brand names are text on the data layer only, never objects of the world.
CRITICAL: no firearms or firearm silhouettes, no blood; the ink figure never gets red on its body, never has teeth, claws or pupils, never dies, and nobody hits it while it is down.
CRITICAL: at most 3 flashes per second; never pure white over the whole frame; inverted frames only once, inside a mask.
CRITICAL: the answer is always «hasn't announced», never «won't be»; no date, year, window or projection for a next game.
```

### Lo que NO debe verse ni oírse

- Ninguna imagen, captura, logotipo, tipografía, música ni nombre de personaje del juego; nada de su trama; ningún tráiler ni «concepto» de aficionados de una entrega siguiente; ninguna cita de directivos. Cajas lisas, televisor en blanco, cartel sin figura.
- Ninguna persona real; ningún nombre de marca como objeto del mundo (nada rotulado se golpea, se rompe ni se quema).
- Armas de fuego y su silueta; sangre; rojo sobre el rival (lo que salta es tinta); ensañamiento; miedo.
- El nombre «la Duda» en voz, texto, título o portada; boca o pupilas en el rival.
- Agujero en la pared (el agujero es de otro video); temblor de cámara; partículas borrosas en el fuego.
- Amarillo `#FFD21F` en personajes, rival, armas, entorno, subtítulos, fuego o humo (el acento va solo detrás del dato y en la estrella de impacto).
- Placa amarilla llena detrás de un nombre de marca (en «GTA 7?», «GTA», «GTA 6», «Grand Theft Auto» y «Rockstar Games» el acento es solo subrayado).
- Texto, voz o subtítulo sobre el universo (mando, caja rota, asterisco, grieta): no llevan ninguno.
- Cualquier dato fuera de la sección 12: ninguna fecha ni cifra de una entrega siguiente; ninguna cifra de aficionados; ni capítulos, ni misiones, ni finales.

## 11. Gancho, ritmo y cierre

- **Regla formal de la pieza:** una pregunta que se dibuja sola y se paga por capas, un golpe por dato; el golpe que no borra es la respuesta.
- **Rejilla de tiempo:** pulso de 15 f (0,5 s, 120 por minuto); 63 pulsos suman los 31,5 s (945 f). La música cuenta los pulsos y sube una capa por golpe; **los cortes los fija la acción** (pausa, contacto, vuelo y choque, según la dirección) y no todos caen sobre un pulso.
- **Gancho (0 a 1 s):** movimiento y contraste — el lápiz ya girando en f0 y atrapado en f10, «GTA 7?» subrayado en amarillo sobre un mundo de papel frío y tinta, y la voz de Tan desde f14; el rival se dibuja en f30 y en f69 mide vez y media lo que ellos; el primer golpe con su dato cae en f82 (contacto) y f91 (dato quieto), en el segundo 3.
- **Empieza en movimiento:** sí: sin intro ni logo; el lápiz gira desde el fotograma 0.
- **Motivo visual que vuelve:** el lápiz (firma, y con él se dibujan las armas) y el televisor en blanco del centro (está en f0, recibe la punta en f484, estalla en f662 y queda reventado en el plano final). Se repiten con las mismas formas y colores.
- **Cierre:** el último plano es el plano de portada (misma cámara, mismo texto, mismas poses) con Tan lanzando el lápiz; el fotograma 0 es el paso siguiente de ese vuelo. **Excepción declarada (D6):** el fondo del cierre conserva los daños y el del inicio está entero. El bucle devuelve la pregunta: termina con «GTA 7?» en pantalla y vuelve a empezar con ella.
- **Llamado a la acción:** uno solo, de Tan: «Subscribe. We check the facts.» (f878–f928), sin promesa de tema futuro.

Mapa de ritmo (los tiempos al décimo de segundo; cortes por segundo = cortes que empiezan dentro del tramo, divididos por su duración):

| Tramo | Segundos | Pulso o intervalo | Cortes por segundo | Qué pasa (una acción) | Respiro |
|---|---|---|---|---|---|
| Gancho | 0,0–2,3 | 15 f | 0,4 (1 corte) | Firma, portada y entrada del rival | no |
| Ráfaga 1 | 2,3–5,5 | 15 f | 1,3 (4 cortes) | Golpes 1 y 2: puño y patada | no |
| Subida | 5,5–12,7 | 15 f | 0,6 (4 cortes) | Contraataque y golpe 3; la tarjeta de «qué es GTA» se completa | sí (f306–f382, plano de 77 f) |
| Ráfaga 2 | 12,8–20,6 | 15 f | 0,6 (5 cortes) | Detalle del lápiz, bloqueo, golpes 4 y 5; arranca el fuego | no |
| Pico | 20,6–23,2 | 15 f | 1,2 (3 cortes) | Carrera lenta, silencio total, golpe doble y explosión | no |
| Respiro | 23,2–25,9 | 15 f | 0,4 (1 corte) | Plano fijo de 80 f: la cuenta y el asombro | sí |
| Salida | 25,9–30,5 | 15 f | 0,4 (2 cortes) | Implosión, respuesta, asterisco, salida del rival, invitación | sí (resto y asterisco, f815–f914) |
| Firma | 30,5–31,5 | 15 f | 1,0 (1 corte) | Plano de portada y lanzamiento del lápiz | no |

Total: 22 planos y 21 cortes en 31,5 s, cinco de ellos de impacto (rango del canal: 8 a 25 cortes en 30 s). Lo que sale se va antes de que entre lo siguiente. El movimiento se describe como mecánica (qué parte se mueve, con qué curva, en qué orden entra y sale). Tipos de plano: detalle (toma 11, al 41 % del video), héroe abierto (toma 18), subjetivo (toma 2), revelado (toma 19). **No más de 3 destellos por segundo.**

### Coreografía de cada golpe (tiempos medidos por Keter a 30 f/s; se copian los tiempos, no los dibujos)

Gramática: anticipación K −12 a K −7 (6 f, movimiento contrario al golpe con frenada); **pausa** K −6 a K −1 (6 f, pose casi quieta, el trazo «hierve», sin efectos de sonido); **contacto** K y K +1 (2 f, salto de posición, arco de borrón del color de quien golpea, estrella ≤ 0,6 u, 5 a 7 gotas de tinta); lanzamiento K +2 a K +5 (3 calcos translúcidos); vuelo y desaceleración de 8 a 15 f con el reloj de la escena a 0,25; choque de 2 f (en los grandes, corte a cuadro de impacto); recuperación de 6 f; el golpe suena en K o K −1; Tin empieza el dato 2 f después del contacto.

| Golpe (dato) | Quién y con qué | Anticipación · pausa · contacto | Lanzamiento · vuelo · choque · recuperación | Qué se rompe (se queda) | Fuego, humo, explosión, implosión |
|---|---|---|---|---|---|
| 1 («GTA is short for Grand Theft Auto») | Tin, puño derecho | f70–f75 · f76–f81 · **f82–f83** | f84–f87 · f88–f99 en profundidad · f100–f101 contra `estante_izquierdo` · f102–f107 | Estante inclinado ≈ 12°, pierde 8 cajas | Polvo con contorno; sin fuego |
| 2 («a game series that started in 1997») | Tan, patada giratoria | f132–f137 · f138–f143 · **f144–f145** | f146–f149 · resbala f150–f161 · f162 contra los `postes_de_fila` · f163–f168 | Los 4 postes tumbados; en f196 el rival parte el `cartel_de_pie` | Polvo |
| 3 («GTA 6 came out on November 19, 2026») | Tin, gancho ascendente | f270–f275 · f276–f281 · **f282–f283** | f284–f287 hacia arriba · flota f288–f299 · cae f300–f303 · f304–f305 contra el `mostrador` · f306–f311 | Grieta a lo largo del mostrador | Polvo |
| Bloqueo («Rated M: seventeen and over») | El rival ataca con su `espada_de_tinta`; Tin bloquea con el `baston_de_tinta` | Del rival: f458–f463 · f464–f469 · **bloqueo f470–f471** | La punta vuela f472–f483 (0,3) · se clava en el televisor f484–f485 | Pantalla agrietada en estrella | Chispas f486–f495; fuego fase 1 desde f496; humo con contorno desde f506 |
| 4 («Each numbered game tells a new story») | Tin, bastón, barrido horizontal | f480–f485 · f486–f491 · **f492–f493** | f494–f497 · f498–f505 · rebote en `estante_derecho` f506–f507 · el rival cae de pie | El estante derecho pierde una balda y 6 cajas | Fuego fase 1 y humo, al fondo |
| 5 («From GTA 5 to GTA 6:») | Tan, `mazo_de_tinta` (Tin añade un bloque al bastón, f540–f551, y se lo lanza) | f558–f563 · f564–f569 · **f570–f571** | La caja sale f572–f575 · vuela a cámara f576–f587 · cae abierta f588–f589 · f590–f595 | El mostrador se parte en dos; `caja_registradora_rota` | Fuego fase 2 desde f572 |
| Remate («thirteen years and sixty-three days») | Tin y Tan, golpe doble: bastón y mazo a la vez | Carrera lenta f618–f628 · f629–f634 · f635–f640 con silencio total · **f641–f642** | f643–f646 · f647–f661 · contacto lejano f662–f663 | Televisor reventado, isla volcada, quemadura en suelo y pared (sin agujero), banderines chamuscados | Explosión por fases (ver «Efectos») |
| 6 («Rockstar hasn't announced one. As of today.») | Tin, bastón, un solo golpe | f783–f788 · f789–f794 · **f795–f796** | Sin lanzamiento: el rival se hunde en sí mismo | Papeles y cajas se deslizan ≈ 0,5 u al centro y ahí se quedan | Implosión f797–f814 |

**El rival (versión 2):** entra a 1,25 veces la altura de Tin y Tan y crece a 1,5 (f46–f69). **Marcador de avance**, un escalón por dato: 1,4 → 1,25 → 1,1 → 1,0 → 0,9 (con un mechón suelto) → 0,8 (chamuscado) → resto de ≈ 1,5 R. Nunca da miedo (crecido se infla como un gato erizado); sus dos ataques fallan o se bloquean; se levanta solo; nadie lo golpea caído; sin dientes, garras ni pupilas; **nunca muere**.

**Tin y Tan por tramo:** f0–f29 Tin `parado` sin lápiz, cara de la portada, cabeza 25°; Tan con el brazo de firma. f30–f131 Tin `guardia`, `carga`, `golpe`, `concentrado` en la pausa y `eureka` al decir el dato; Tan `guardia` y `sorpresa` al retroceder. f132–f275 Tin `guardia`, `agachado` en f194, `corre1`/`corre2`; Tan `carga`, `patada`, `festeja` 4 f. f276–f551 Tin `golpe` hacia arriba, `poder` al dibujar, bloqueo en `guardia`, bastón; Tan `guardia`, `sorpresa` con la punta. f552–f696 Tin lanza el mazo, se miran (f600–f606), `corre1`/`corre2`, `golpe` doble y `agachado` de espaldas; Tan atrapa el mazo, `carga`, `pisoton` en el contacto. f697–f914 Tin `sorpresa` con la cifra, `golpe` en f795, `curiosidad` ante el resto, lanza el lápiz; Tan boca abierta y quieta f703–f745, `pregunta` en f750, atrapa el lápiz, `feliz` al invitar. f915–f944 los dos como en f0. Acción secundaria: bufanda de Tan con muelle; el trazo del rival hierve cada 3 f; ninguna encima de un dato.

### Mapa de velocidad (el reloj de la escena cambia; la voz nunca)

| Tramo (f) | Reloj de la escena | Qué se siente |
|---|---|---|
| Anticipaciones (6 f antes de cada pausa) | 1,0 con frenada | Carga |
| Pausas (K −6 a K −1) | Pose quieta; el mundo sigue (humo, fuego) | Aire contenido |
| Contactos (K, K +1) | 1,0; salto de posición | Golpe seco |
| Lanzamientos (K +2 a K +5) | 1,3 con calcos | Violencia de dibujo |
| Vuelos: f88–f99, f150–f161, f288–f299, f472–f483, f498–f505, f576–f587, f647–f661 | 0,25 (0,3 en la punta de la espada) | Suspenso en el aire |
| Carreras: f108–f131 (el rival), f252–f269 (Tin) | 1,3 con borrón de movimiento | Urgencia |
| Carrera previa al remate: f618–f628 | 0,3 durante 11 f | Se sabe que viene el grande |
| Explosión: f675–f696 | 1,0; cada dibujo dura 2 f | Estallido legible |
| Respiro: f697–f776 | 1,0, casi nada se mueve | Asombro, lectura |
| Implosión: f797–f814 | De 0,6 a 1,4 (acelera hacia adentro) | Colapso |
| Resto y asterisco: f815–f914 | 1,0, movimientos pequeños | Humor seco |
| Firma: f0–f29 y f915–f944 | La de la firma, sin cambios | Reconocimiento |

### Efectos (fuego por fases, humo, impactos, explosión, implosión, daños)

| Efecto | Dónde y dosis | Qué comunica y qué emoción busca |
|---|---|---|
| Fuego plano por fases | Chispas f486–f495; fase 1 desde f496 (llama pequeña, 3 dibujos de 2 f); fase 2 desde f572 (el doble, el borde cambia de forma sin parpadear); se apaga con la implosión en f814. Dos tonos con escalón duro: núcleo `#FFF4B8`, borde `#B81414`; nunca toca el cuerpo del rival; nunca cubre más de un cuarto del cuadro en dos fotogramas seguidos | Peligro de dibujo, la mecha que se paga con la explosión: anticipación |
| Humo con contorno | Desde f506; `#666B76` con contorno de tinta; despeja en f697–f720 y deja ver la cifra; nunca pasa por delante de la cabeza de Tan | «Esto se quemó»; despeja para el dato |
| Impactos en cuadros cortos | Cinco cortes de impacto de 2 f (tomas 4, 9, 13, 17 y la entrada de 18); sin temblor | Golpe seco; euforia en cada contacto |
| Explosión | 2 cuadros invertidos con máscara f664–f665 · radiales f666–f670 · claro con máscara f671–f674 · bola de fuego plana f675–f685 · enfriamiento f686–f696 · humo f697–f720 | Asombro en un número comprobado |
| Implosión | f797–f814: 3 anillos de tinta que se cierran, la tinta se recoge, el rival se borra desde la cabeza; se lleva el humo y apaga las últimas llamas | Humor deadpan y alivio: la respuesta honesta no estalla |
| Daños que se quedan | Nueve: estante izquierdo inclinado, postes tumbados, cartel partido, mostrador partido, estante derecho sin balda, televisor reventado, `caja_registradora_rota`, banderines chamuscados, quemadura en suelo y pared | La pelea tuvo consecuencias; se ven en f900 y f944 |

**Pregunta abierta para fotografía (nota 3):** la dirección, sección 4.2, pone un «anillo amarillo» en la bola de fuego de f675–f685; la sección 3b excluye el acento `#FFD21F` del fuego y del humo. Hasta que fotografía lo decida, el anillo no se dibuja con el acento: queda como anillo en los tonos del fuego y se anota en la revisión de color.

### Firma del lápiz bumerán (no se toca)

- **Apertura (f0–f29, cámara C0 fija):** en f0 el lápiz está en el aire, entero y nítido, en el pasillo; vuelve en 10 f; Tan lo atrapa en f10 con el brazo de firma (95°, 108°); retroceso de brazo y cuerpo; Tin sin lápiz, con su saltito; la voz de Tan entra en f14. El rival no aparece hasta f30.
- **Cierre (f915–f944, misma cámara):** el texto de portada entra en c −30; anticipación c −24 a c −19 (f921–f926); impulso hasta c −15; suelta en c −15 (f930); vuelo de 15 f; la voz termina en c −17 (f928). Nada más se mueve.
- **Geometría y despejes:** se calculan con `geometria_firma` sobre el fotograma 0 de este video y pasan `comprobar_firma` sin cambios: 8 px o más a cualquier cabeza en todos los fotogramas, 30 px o más al texto y al objeto del centro (el televisor), centro del lápiz dentro de la zona útil, giro horario, velocidad y escala dentro de los topes. Los sonidos de la firma son los de siempre.
- **Empalme:** lápiz, brazo, cabeza y cuerpo de Tan, pose de Tin, caras, texto y cámara son los mismos en c −1 y f0. **El fondo no** (decisión D6: al final la tienda está rota y al inicio entera); la excepción necesita la firma del director de animación.

### Conexiones del universo (hueco H01; solo qué se ve, dónde y cuándo)

Ninguna lleva voz, subtítulo ni texto. Las coordenadas son el objetivo y se miden en el render (lado menor de 36 px o más, o no cuenta). Eventos activos: 22 f (≈ 0,73 s; tope 1,5 s); nada se mueve antes del segundo 10 salvo la entrada del rival; ninguna toca la franja de subtítulos, el pasillo de la firma ni sale de la zona útil.

| Qué se ve | Cuándo | Dónde (px, plano indicado) | Activo |
|---|---|---|---|
| El lápiz se atrapa dentro del mundo (la firma) | f0–f10 | Pasillo de la firma | No |
| `mando_mostaza` sobre la repisa del fondo, quieto todo el video | Desde f0 | Fondo izquierdo: x 110–200, y 740–800 (30 px o más bajo el texto de portada; fuera de la franja) | No |
| `caja_registradora_rota` | Se rompe en f570–f589 (después del segundo 10); queda hasta el final | Extremo izquierdo del piso de acción en el plano final: x 125–215, y 1362–1422 | No (es daño de la pelea) |
| Marca final: asterisco, ≈ 48 px | f842–f847 (6 f) y se queda | Centro, bajo el pasillo de la firma: x 516–564, y 1372–1420 | Sí: 6 f |
| El último trazo del rival se escurre por una grieta del suelo, lado derecho | f852–f867 (16 f), terminada 48 f antes de c −30 | Borde derecho del piso de acción: de x 540 a x 890–960, y 1372–1420 | Sí: 16 f |
| Tin sin lápiz en los planos de firma | f0–f29 y f915–f944 | — | No |
| El rizo del rival no tiene punto | Siempre que está en pantalla | — | No |

Control «se entiende solo»: quitando todo lo de esta tabla no se pierde ni una frase ni un dato. El asterisco es asterisco y no punto porque la pregunta del video queda sin respuesta comprobada: GTA 7 no está anunciado. Falta anotar `caja_registradora_rota` en la fila de pista P-003 del registro (privado, fuera de esta carpeta).

## 12. Texto en pantalla y sistema de diseño

- **Tipografías:** Inter Display Medium con dígitos abiertos (`ss01`), licencia SIL Open Font License 1.1 (`/usr/share/fonts/opentype/inter/InterDisplay-Medium.otf`). Minúsculas salvo los nombres propios y siglas, que llevan mayúscula («Tin & Tan», «GTA», «Rockstar Games», «Nov»); la portada con mayúscula inicial en cada palabra. Nunca la tipografía del juego.
- **Paleta:** neutros: papel claro frío `#DCE6EE` (fondo) y `#F4F1EA` (suelo, cuadrícula `rgba(27,27,34,0.20)`), apoyos `#FFFFFF`, `#B9C6D2`, `#C9D0D8`, `#A7B0BC`; tinta `#1B1B22` (líneas, cuerpos, rival, armas y todo el texto). Acento: amarillo `#FFD21F` (franja de resaltador detrás del dato y estrella de impacto de 2 a 4 f). Efectos: fuego `#FFF4B8` con borde `#B81414`; humo y utilería `#666B76`. Identidad (no cuenta como acento): naranja de Tin `#E07A2E`, verde azulado de Tan `#2F7F7A`, mostaza `#E8B33B` (bufanda, lápiz y mando). Contraste tinta sobre fondo ≈ 13,5:1; sobre suelo ≈ 15,2:1; tinta sobre el amarillo ≈ 11,8:1. Por qué cada color: sección 3b de la dirección. Se mide con `revisar_color.py` con esta paleta declarada.
- **Referencias de movimiento:** `01_referencia/` está vacía; las referencias de forma son `estudios/2026-11-26_referencias_de_pelea_estudio_de_keter.md` (solo tiempos), la hoja v2 del rival, `canales/nostalgia-tin-y-tan/DESIGN.md` y la paleta C.
- **Prohibido:**
  1. Mayúsculas centradas sobre degradado, y tarjetas con degradado.
  2. Animaciones lineales de posición o escala en lo vivo (solo muelle o ease-out; lineal solo en lo mecánico).
  3. Temblor de cámara (`temblor` del catálogo) y partículas borrosas en el fuego.
  4. Placa de amarillo lleno detrás de un nombre de marca (solo subrayado, el 40 % inferior de la altura de la letra, con extremos irregulares, inclinado ≈ 2°).
  5. El acento amarillo en personajes, rival, armas, entorno, subtítulos, fuego o humo.
  6. Texto sobre un personaje o sobre un contacto; un dato que se mueva con la cámara o cambie mientras se lee.
  7. Tres capas de texto a la vez (dato, subtítulo y portada nunca coinciden).
  8. Rótulos, carteles, cajas o televisores con texto, logotipo o arte dentro del mundo 3D.
  9. Sombras tumbadas de los muñecos, resplandor, confeti.
  10. Cambiar los colores o accesorios de Tin y Tan (solo cambia el objeto de la mano).
- **Márgenes seguros y escenario:** zona segura de `formatos.md` (centro de 880 × 1420 px: x 100–980, y 250–1670); la capa de datos entre y 400 y 700, alineada a la izquierda, x 100–980; subtítulos en la franja y 905–1085; piso de acción y 1105–1700. En la portada, caras dentro de la zona útil. Los personajes ocupan el piso de acción; ninguna acción importante detrás de la franja.
- **Texto exacto:** todo texto en pantalla es el de las tablas de abajo, letra por letra. Cada dato entra con un golpe de 5 f, se asienta y no se mueve ni cambia hasta salir (3 f); queda quieto 30 f o más. Un dato a la vez: la tarjeta de «qué es GTA» es un solo dato que crece en tres renglones (cada renglón nuevo entra en 5 f; los anteriores no se mueven). Dato de 86 px o más de alto de letra; líneas de apoyo y renglones de la tarjeta de 48 px o más; 3 renglones como máximo a la vista.
- **No afirmar:** que no vaya a haber GTA 7; ninguna fecha, año, ventana ni proyección para una entrega siguiente; ningún rumor ni tráiler de aficionados; nada de la trama ni de los personajes del juego; que el juego sea bueno o malo; que Rockstar hiciera la primera entrega (la serie empezó en 1997; «Rockstar la hace y la publica hoy»); en qué mundo de ficción está GTA 6; ningún número de capítulos, misiones o finales; ventas, ganancias ni la cifra de Take-Two; ninguna persona real.
- **Subtítulos:** en español, quemados, hasta 2 renglones, sin palabra clave resaltada; siguen a la voz. Sin subtítulo en los planos de portada (f0–f29 y f915–f944). Pista `subtitulos_es.srt`. Cada uno queda dentro de la franja y 905–1085, tinta sobre panel del color del suelo con opacidad 0,82; el tamaño de la letra lo fija el editor (en el short 3 fue de 86 px).

**Capa de datos y portada (inglés):**

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| GTA 7? (subrayado amarillo) / Facts, Checked | 0,00 | 1,00 | x 9,3; y 20,8–36,5 | 7,8 y 4,8 |
| GTA = Grand Theft Auto (renglón 1 de la tarjeta; subrayado en «GTA» y «Grand Theft Auto») | 2,87 | 9,27 | x 9,3; y 20,8–36,5 | 4,5 o más |
| a game series · since 1997 (renglón 2; placa en «since 1997») | 6,33 | 9,27 | x 9,3; y 20,8–36,5 | 2,5 o más |
| made today by Rockstar Games (renglón 3; subrayado en «Rockstar Games») | 7,70 | 9,27 | x 9,3; y 20,8–36,5 | 2,5 o más |
| GTA 6 / out since Nov 19, 2026 (subrayado en «GTA 6»; placa en «Nov 19, 2026») | 10,20 | 12,77 | x 9,3; y 20,8–36,5 | 4,5 o más |
| the sixth numbered game (placa en «sixth») | 12,83 | 14,30 | x 9,3; y 20,8–36,5 | 4,5 o más |
| rated M · 17 and over (placa en «17 and over») | 14,37 | 16,33 | x 9,3; y 20,8–36,5 | 4,5 o más |
| each numbered game: / a new story (placa en «a new story») | 16,53 | 18,53 | x 9,3; y 20,8–36,5 | 4,5 o más |
| from GTA 5 to GTA 6 (línea de apoyo, pequeña; subrayado en las marcas) | 19,13 | 21,43 | x 9,3; y 20,8–36,5 | 2,5 o más |
| 13 years, 63 days / GTA 5: Sep 17, 2013 · GTA 6: Nov 19, 2026 (placa en «13 years, 63 days») | 23,23 | 25,93 | x 9,3; y 20,8–36,5 | 4,5 o más y 2,5 o más |
| GTA 7: / not announced / as of y la fecha de la relectura del día de publicar (placa en «not announced»; subrayado en «GTA 7:») | 26,63 | 29,17 | x 9,3; y 20,8–36,5 | 4,5 o más y 2,5 o más |
| GTA 7? (subrayado amarillo) / Facts, Checked (portada de cierre) | 30,50 | 31,50 | x 9,3; y 20,8–36,5 | 7,8 y 4,8 |

Las entradas y las quietudes son las de la dirección (sección 2.2); las salidas se derivan de su regla («sale en 3 f» después del último fotograma quieto o antes de la entrada del dato siguiente) y las confirma el editor. **El sello de fecha («as of» más la fecha) se escribe el día de publicar con la fecha de la relectura del remate**; hasta entonces es el único texto sin fecha cerrada, y es código: se actualiza sin tocar la voz.

**Subtítulos en español (quemados y pista `.srt`):**

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| ¿Habrá un GTA 7? | 1,00 | 2,13 | franja y 47,1–56,5 | franja de 9,4 |
| GTA es Grand Theft Auto: | 2,80 | 4,67 | franja y 47,1–56,5 | franja de 9,4 |
| una serie de juegos que empezó en 1997 | 4,87 | 7,43 | franja y 47,1–56,5 | franja de 9,4 |
| y que hoy hace Rockstar Games. | 7,63 | 8,93 | franja y 47,1–56,5 | franja de 9,4 |
| GTA 6 salió el 19 de noviembre de 2026. | 9,47 | 12,53 | franja y 47,1–56,5 | franja de 9,4 |
| Es el sexto juego numerado. | 12,77 | 14,07 | franja y 47,1–56,5 | franja de 9,4 |
| Para mayores de 17. | 14,30 | 16,10 | franja y 47,1–56,5 | franja de 9,4 |
| Cada juego numerado cuenta una historia nueva. | 16,47 | 18,33 | franja y 47,1–56,5 | franja de 9,4 |
| De GTA 5 a GTA 6: | 19,07 | 20,93 | franja y 47,1–56,5 | franja de 9,4 |
| trece años y sesenta y tres días. | 23,23 | 24,87 | franja y 47,1–56,5 | franja de 9,4 |
| ¿Y GTA 7? | 25,00 | 26,27 | franja y 47,1–56,5 | franja de 9,4 |
| Rockstar no ha anunciado ninguno. A hoy. | 26,57 | 28,83 | franja y 47,1–56,5 | franja de 9,4 |
| Suscríbete. Aquí comprobamos los datos. | 29,27 | 30,47 | franja y 47,1–56,5 | franja de 9,4 |

Texto y subtítulos pasan `revisar_texto.py` (inglés para voz y datos, español para subtítulos) con 0 errores antes de dar el prompt por bueno.

### Color con intención

- **Neutros (2):** papel claro frío y tinta. **Acento (1):** amarillo `#FFD21F`, solo como franja de resaltador detrás del dato y en la estrella de impacto (2 a 4 f, nunca a la vez que un dato nuevo). Texto siempre en tinta.
- **Cómo ayuda al objetivo:** el primer cuadro se lee en menos de un segundo (fondo claro, siluetas de tinta y una sola mancha saturada); después el amarillo aparece solo donde hay un dato, y el ojo aprende dónde mirar. La placa de «not announced» es el punto de más contraste del final: que la respuesta honesta no pase inadvertida separa este video del clickbait.
- **Riesgos de lectura (por medir):** el amarillo con texto negro junto a «GTA» y «Rockstar Games» puede recordar al logotipo de la editora (por eso el subrayado en marcas; fotografía compara `#FFD21F` con el amarillo de esa marca); el humo gris y la cabeza verde azulada de Tan se confunden con daltonismo (por eso el humo lleva contorno y no pasa por delante de la cabeza de Tan); tres amarillos (acento, bufanda y lápiz, mando): el acento es el más luminoso y el único en la capa de datos; el rojo del borde del fuego no parpadea y no toca al rival; el claro de la explosión va con máscara de 55 % del cuadro como máximo y opacidad 0,6 durante 4 f; el dato de 86 px o más para pantalla chica y televisor.

## 13. Sonido

Nadie del equipo ha oído estos sonidos (son sintéticos, por código): los valida un oído humano antes de la prueba. Voz a −14 LUFS; efectos por debajo (picos de −20 a −12 dBFS con voz encima; la explosión puede llegar a −8 dBFS porque cae en la pausa de voz f629–f696). Cada golpe suena en K o un fotograma antes. «Catálogo» = existe en `motor_de_accion/sonidos/sonido.py`; «nuevo» = hay que construirlo y anotarlo en `catalogo.json`.

| Golpe o efecto | Segundo | A qué corte va atado | Origen y licencia |
|---|---|---|---|
| Firma: regreso del lápiz y atrapada (S3 y S4) | 0,00–0,33 (f0–f10) | Toma 1 | Los de la firma, código propio |
| `trazo_de_tinta` (rasgueo de lápiz, 16 f) | 1,00–1,50 (f30–f45) | Toma 2: el rival se dibuja | Nuevo, código propio |
| `choque_suelo` bajo y `cajas_caen` | 2,00 (f60) | Toma 2: pisotón | Catálogo y nuevo, código propio |
| Silencio de efectos (pausa del golpe 1) | 2,53–2,70 (f76–f81) | Toma 3 | — |
| `silbido` corto y `golpe` | 2,70 (f81) | Toma 3: contacto del golpe 1 | Catálogo, código propio |
| `choque_madera` y `cajas_caen` | 3,33 (f100) | Toma 4: estante | Catálogo y nuevo, código propio |
| `golpe` un tono arriba | 4,77 (f143) | Toma 6: patada | Catálogo, código propio |
| `roce_suelo` y `postes_caen` (4 golpes metálicos escalonados) | 5,00–5,40 (f150–f162) | Toma 6: resbalón y postes | Nuevo, código propio |
| `choque_madera` seco, más agudo | 6,53 (f196) | Toma 7: cartel partido | Catálogo, código propio |
| `golpe` grave y `silbido` ascendente | 9,37–9,40 (f281–f282) | Toma 8: gancho | Catálogo, código propio |
| Casi silencio: solo la voz | 9,60–9,97 (f288–f299) | Toma 8: flota | — |
| `silbido_caida` y `choque_pilar` | 10,00–10,13 (f300–f304) | Tomas 8 y 9: cae y choca | Catálogo, código propio |
| `trazo_de_tinta` | 12,77–13,13 (f383–f394) | Toma 11: dibuja el bastón | Nuevo, código propio |
| `trazo_de_tinta` y `bloqueo_tinta` (choque seco con cola corta) | 14,67–15,03 (f440–f451) y 15,67 (f470) | Toma 12: espada y bloqueo | Nuevo, código propio |
| `vidrio_grieta`, `chispas` y `fuego_enciende` | 16,13 (f484); 16,20–16,50 (f486–f495); 16,53 (f496) | Tomas 13 y 14: televisor, chispas, llama | Nuevo y catálogo, código propio |
| `baston_golpe` (madera hueca) y `choque_madera` | 16,37–16,40 (f491–f492) y 16,87 (f506) | Toma 14: golpe 4 y estante | Nuevo y catálogo, código propio |
| `trazo_de_tinta` | 18,00–18,37 (f540–f551) | Toma 14: el mazo | Nuevo, código propio |
| `silbido` | 18,40–18,57 (f552–f557) | Toma 15: lanzamiento del mazo | Catálogo, código propio |
| `mazo_golpe` (el más grave hasta aquí) y `choque_madera` | 18,97–19,00 (f569–f570) | Toma 15: mazazo | Nuevo y catálogo, código propio |
| `campanilla_caja` (el «ding» de gaveta, único sonido amable) | 19,60 (f588) | Toma 15: la caja cae abierta | Nuevo, código propio |
| Subida de 11 f (looming) | 20,60–20,93 (f618–f628) | Toma 16: carrera lenta | Código propio |
| **Silencio total, también de música (6 f)** | 21,17–21,33 (f635–f640) | Toma 16: pausa del golpe doble | — |
| `golpe_doble` | 21,33–21,37 (f640–f641) | Toma 16: golpe doble | Catálogo, código propio |
| `vidrio_grieta` | 22,07 (f662) | Toma 16: contacto lejano | Nuevo, código propio |
| `explosion` | 22,37 (f671) | Toma 18: expansión | Catálogo, código propio |
| Cola grave que cae y crepitar bajo | 22,87–24,00 (f686–f720) | Tomas 18 y 19 | Código propio |
| Entra la cifra: sin golpe, la voz sola sobre la cola | 23,23 (f697) | Toma 19 | — |
| `baston_golpe` un tono más bajo que en el golpe 4 | 26,47–26,50 (f794–f795) | Toma 20: golpe 6 | Nuevo, código propio |
| `implosion` (barrido de agudo a grave) y corte seco | 26,57–27,13 (f797–f814) | Toma 20: implosión | Catálogo, código propio |
| `asterisco_tic` (6 golpecitos de lápiz, uno por trazo) | 28,07–28,23 (f842–f847) | Toma 21: asterisco | Nuevo, código propio |
| `escurre` (roce que baja de tono) | 28,40–28,90 (f852–f867) | Toma 21: el trazo se escurre | Nuevo, código propio |
| Firma: lanzamiento del lápiz (S1 y S2) | 30,87–31,47 (c −17 a c −1) | Toma 22 | Los de la firma, código propio |

- **Música:** solo percusión, por código, ≈ −26 LUFS, 120 pulsos por minuto; ver la sección 7. Sin material de terceros. Licencias: `licencias.md` (hoy vacío: lo llena producción con cada recurso).
- **Voz:** sí (por generar con el sí del dueño); empieza en f14 y no tiene silencio inicial en el empalme del bucle.

## 14. Motor y revisión

- **Cómo se hace:** gráficos por código (fotograma a fotograma) con el motor de acción: `node render.js` sobre un guion propio de este video (el guion de la pelea todavía vive dentro de `escena.html` y hay que sacarlo a `guiones/`), la paleta `c_alto_voltaje`, el entorno `tienda_de_videojuegos` (por construir) y las cabezas oficiales de `exportar_sprites.py`; los sonidos con `sonidos/sonido.py`; el armado con ffmpeg y `postpro.py mezclar`. **Piezas nuevas que este video necesita** (brief y plan de la tanda 01): entorno con piezas que se rompen y sus versiones rotas con nombre propio; guion fuera de `escena.html`; fuego plano por fases; humo con contorno; cuadros de impacto con corte; armas de tinta (`baston_de_tinta`, `mazo_de_tinta`, `espada_de_tinta`); marca final (`asterisco`); salida del rival por grieta; capa de datos con tarjeta que crece, subtítulos y firma dentro del motor; los sonidos marcados «nuevo» de la sección 13; zonas de conexión y franja de subtítulos como constantes con comprobación.
- **Punto de control:** antes de renderizar se presenta la lista de tomas sobre los 945 fotogramas y se espera el visto bueno; **la voz no se genera sin el sí del dueño con el número a la vista.** Con la voz real se recalcula toda la tabla de fotogramas sin mover los desfases de cada golpe ni las reglas de 2.1 de la dirección.
- **Revisión:** `herramientas/revisar_fotogramas.py` sobre el render y su resultado en `07_revision/`. En piezas por código: prueba corta de 5 s con un fotograma por pulso, hoja de contacto a 2 por segundo y todos los fotogramas de los vuelos; comprobación de medidas en el render (zona segura, franja de subtítulos, coordenadas de la conexión del universo, pies a y ≈ 1651 en los planos de firma). Controles: `revisar_texto.py` con 0 errores; `comprobar_destellos` y `postpro.py destellos` sin avisos (máximo 3 por segundo, margen de 2); `comprobar_firma`; `revisar_color.py` con la paleta declarada (85 % o más, o la regla de `DESIGN.md` para videos con profundidad); `revisar_voz.py` sin palabras perdidas; control «se entiende solo» firmado por el supervisor de continuidad; el bucle (fotograma 945 igual al 0 salvo el fondo declarado); la escucha de una persona para los sonidos; los datos contra el archivo de hechos.
- **Qué se marca:** imagen congelada, fotograma vacío, texto cortado o tapado, texto que sigue sobre el plano siguiente, elemento fuera de cuadro, tirones, demasiado tiempo sin cambio, cualquier cosa del juego, un arma que parezca de fuego, rojo sobre el rival, el rival que dé miedo o muera, un golpe sin su pausa de 6 f, un contacto de más de 2 f, un daño que no se quede, y en el teléfono que datos, subtítulos y asterisco se lean.
- **Vueltas:** las correcciones por código son gratis (salvo servicios de pago, que van a `costos.md`); **las de generador no se repiten sin autorización del dueño** (`generacion.md`): aquí solo hay generador en la voz, una generación por voz y sin segundos intentos.
