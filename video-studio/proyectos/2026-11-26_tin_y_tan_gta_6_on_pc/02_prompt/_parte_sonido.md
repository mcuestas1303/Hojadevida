## 5. Sonido — disenador-de-sonido

> Escrita el 2026-11-27 por el diseñador de sonido sobre `00_brief.md`, `perfil_emocional.md` y 2.2 a 2.4 de esta dirección.
> Aquí solo se **diseña**: no se ha generado voz, música ni efectos, no hay cotización y no hay mezcla. **Nadie del equipo ha
> oído nada** (los efectos y la percusión son sintéticos, por código): los valida el oído de una persona antes de publicar.
> **Los fotogramas de los golpes son los de 2.2 y 2.3 (voz estimada). Se ajustan a los de animación (sección 4) y a la voz real;
> cada sonido va atado a su K de animación, no a un número escrito aquí.** Regla de atado: el pico del golpe cae en **K −1**.
> Sellos de `manual/14`: (investigación), (oficio), (hipótesis del equipo); lo que no lleva sello es norma de partida, o
> sea (hipótesis del equipo).

### 5.1 Lo que se aprendió del short 4 y se aplica aquí

| Defecto del short 4 (`revision_v3_sonido.md`, `revision_v4_sonido.md`) | Qué se hace en este video |
|---|---|
| S1: el mazazo cayó a −9,5 dBFS sobre la última sílaba de una frase (a −9 el reconocedor y el oído la pierden) | **Ningún efecto pasa de −24 dBFS de pico mientras suena una palabra**, y ninguno pasa de −32 dBFS sobre una cifra dicha (5.5). Los golpes de más de −12 dBFS solo caen donde no hay voz |
| `choque_pilar` sobre «GTA six» hizo oír un «it» de más (comentario en `audio.py`) | La grieta (f30–f45) cae **bajo «GTA 6»** de la línea 1 de Tan: sin transitorio de 300 Hz a 4 kHz, solo grave (5.4, nota A) |
| S3: la línea de suscripción de Tan salió 3 a 5 dB por debajo de Tin | La línea 7 de Tan es la que más importa: se iguala al RMS activo de Tin (±2 dB) **comprimiendo**, no subiendo ganancia (D1 abajo) |
| D1: la voz de Tan llegó a +4,4 dBFS antes del limitador (117 muestras sobre 0) y el limitador la raspó | Ganancia por línea con pico de voz ≤ −1,5 dBFS **antes** del limitador; si hace falta más cuerpo, compresión suave en Tan; el limitador no debe actuar sobre voz |
| S4: la cola de la explosión pisó el arranque de la voz siguiente | La voz de Tin entra en f728; la cola de la explosión llega a −40 dBFS en f727 (5.4, f706) |
| S5/S6: sin pausa limpia antes de un golpe (5 f en vez de 6) | Pausa de efectos y música de **8 f** antes del toque de f700 (no 6), y de 6 f antes de cada K |
| Percusión a 120 pulsos con un pulso cada 15 f y capas que suben tras cada golpe | **Otro patrón** (5.7): tic de regla a 90 pulsos, latido grave, aceleración en el suspenso, sin bombo de 4 por compás |
| Los 49 eventos tuvieron su pico en K −1 a ±0,1 f | Misma regla, y se comprueba igual (5.9) |

### 5.2 Voz: texto final por personaje, para el generador

**Una generación por personaje** (regla del canal y 7 de esta dirección). Modelo `seed_audio`, ajustes por defecto, como en
la prueba del 2026-11-21 (`canales/nostalgia-tin-y-tan/voces.md`). Cada línea va en **su propio párrafo**, con punto final;
las palabras son **exactamente** las de 2.2, sin añadir ni cambiar nada. En edición se cortan por las pausas **y se
escucha cada corte** (en el short 4 los cortes se hicieron sin oír). Después, `atempo=1.10` y −14 LUFS por personaje.

**Tin = Kevin** (`f1373f24-3b96-433f-9a68-e595810ef608`). Trato: seco, de hechos, sin adjetivos; las frases bajan al
final; ninguna sube como pregunta; energía despierta pero sin gritar.

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

**Tan = Zelda** (`b7aaea29-0c88-5925-90c0-8f66754cda53`). Trato: curiosa en las preguntas, simple en lo demás.

```text
Is GTA 6 coming to PC?

How long last time?

Subscribe for facts, checked.

Don't download them.
```

Cambios de **puntuación** (no de palabras) respecto de 2.2, y por qué:

- Línea 4: coma antes de «and Xbox» para separar las dos consolas y que «Xbox Series X and S» no se pegue a «PlayStation 5».
- Línea 9: se quitan las comillas simples (el generador a veces las dice como pausa rara o las ignora) y se ponen comas
  alrededor de «GTA 6 for PC» para que se oiga como nombre citado.
- El resto, igual a 2.2. Los subtítulos y los datos en pantalla no cambian.

**Indicaciones de entonación y pausas** (se pasan como nota de dirección a producción; el generador solo recibe el texto de
arriba, así que la entonación se consigue con la puntuación y se **comprueba al oír**; si no sale, es una regeneración de
esa línea, que cotiza producción):

| Línea | Quién | Cómo suena | Pausa que debe tener |
|---|---|---|---|
| 1 «Is GTA 6 coming to PC?» | Tan | Curiosa, pregunta que sube al final; «PC» claro | Termina limpia: Tin entra 8 f después |
| 2 «Not announced.» | Tin | La más corta y seca; baja al final; «announced» completa | Sin respiración antes ni «eh» |
| 3 «Rockstar hasn't announced a PC version.» | Tin | Plana, informativa | Va seguida de la 4 con 8 f de aire |
| 4 «It's on PlayStation 5, and Xbox Series X and S.» | Tin | Más lenta en «Xbox Series X and S» (cinco sílabas, con «X» y «S» marcadas) | Breve pausa en la coma |
| 5 «How long last time?» | Tan | Pregunta corta, sube | — |
| 6 «GTA 5 took about a year and a half to reach PC.» | Tin | Cifra clara: «about a year and a half» sin apuro, es el dato más importante | — |
| 7 «Subscribe for facts, checked.» | Tan | Amable, normal, sin súplica ni grito; «checked» cierra | Pausa de coma en «facts, checked» |
| 8 «Red Dead Redemption 2: about a year.» | Tin | «Red Dead Redemption 2» seguido, sin saltos; luego una pausa corta y «about a year» | Pausa en los dos puntos |
| 9 «Files that say, GTA 6 for PC, are not from Rockstar.» | Tin | Firme; «not from Rockstar» con el peso | Pausas de coma cortas |
| 10 «Some carry malware.» | Tin | Cara de póquer: lo dice sin dramatismo, plano | — |
| 11 «Don't download them.» | Tan | **Baja y seca, no regaño**; no sube ni grita (perfil emocional, fila Voces) | — |
| 12 «No official PC date. As of today.» | Tin | Tranquila, cierra; baja en «today» | Punto entre las dos frases |

### 5.3 Riesgos de pronunciación y cómo escribirlos

| Palabra | Riesgo | Cómo va escrita | Si sale mal (regenerar solo esa línea; cotiza producción) |
|---|---|---|---|
| **GTA 6** | Que diga «G T A sicks» o «GTA vi»; en el short 4 salió bien con esta misma escritura (el reconocedor oyó «GTA VI»; no hubo palabras perdidas) | `GTA 6` | `G T A 6`, luego `G T A six` |
| **GTA 5** | Que diga «GTA five» bien y la «5» como «cinco» o «V»; o que se lea «GTA cinquenta»; es el mismo riesgo que «6» | `GTA 5` | `G T A 5`, luego `G T A five` |
| **Red Dead Redemption 2** | Que lea «two» débil o la junte con «about» (el final de la línea 8 pesa); o «Redemption» atropellada | `Red Dead Redemption 2:` (con los dos puntos) | `Red Dead Redemption two.` y `About a year.` en frases separadas |
| **Xbox Series X and S** | Que diga «Series ten», que se coma «and» o que la «S» suene «ess» pegada | `Xbox Series X and S` precedida de coma | `Xbox Series X, and S.` y, última, `Xbox Series Ex and Ess` |
| **malware** | Que diga «mal-wear» o «mala-ware» | `malware` | `mal ware` (con espacio) |
| **PC** | Que diga «pick» | `PC` | `P C` |
| **Rockstar** | Sin riesgo conocido (salió bien en la prueba); mantener | `Rockstar` | — |
| **hasn't, It's, Don't** | Contracciones: bien en inglés | tal cual, con apóstrofo recto `'` | — |
| **PlayStation 5** | «5» leída «five»; sin riesgo grave | `PlayStation 5` | `PlayStation five` |

Se compara la voz **palabra por palabra** con el guion con `revisar_voz.py` y, **además**, la oye una persona (el control 3 lo
exige; en el short 4 el reconocedor inventó un «it» que solo el oído confirma).

### 5.4 Estimación de la voz (para que producción cotice; **no es cotización**)

Cálculo sobre los fotogramas de 2.2, que ya cuentan 110 %:

| Personaje | Líneas | Sílabas | Fotogramas de voz (plan, al 110 %) | Segundos al 110 % | **Segundos que genera el modelo** (÷ 1,10, + aire entre líneas) | ≈ créditos a 0,1 por segundo |
|---|---|---|---|---|---|---|
| Tin (Kevin) | 8 | 81 | 28 + 75 + 82 + 95 + 68 + 95 + 34 + 75 = 552 f | ≈ 18,4 s | **≈ 20 a 23 s** | ≈ 2,0 a 2,3 |
| Tan (Zelda) | 4 | 23 | 69 + 27 + 34 + 27 = 157 f | ≈ 5,2 s | **≈ 6 a 7 s** | ≈ 0,6 a 0,7 |
| **Total** | 12 | 104 | 709 f | ≈ 23,6 s | **≈ 26 a 30 s** | **≈ 2,6 a 3,0** |

- Fuente de la tarifa: `video-studio/consumo.md` («unos 0,1 créditos por segundo de voz»). En la prueba de voces el precio
  dependió del largo del texto, no de la cantidad de frases (`voces.md`). El short 4 costó ≈ 3,1 (81 palabras de voz).
  Los textos de arriba tienen una cuenta parecida; **el número real lo da la cotización de producción**.
- La línea 1 de Tan está estimada con aire (69 f para 10 sílabas): la voz real puede salir más corta.
- Si la voz real pide más tiempo, se recorta en el orden de 2.1 (línea 4, respiros, línea 11). Con la línea 4 fuera de la
  voz se ahorran ≈ 3 s de voz de Tin (≈ 0,3 créditos).
- Posible **prueba corta** si producción quiere cubrir los riesgos de 5.3 antes de generar todo: las líneas 4, 6 y 8 de Tin
  (≈ 8 a 9 s, ≈ 0,9 créditos) cuestan casi lo mismo que regenerar una vez. Recomendación: generar completo y regenerar una
  sola línea si falla; se decide con el sí del dueño.

### 5.5 Niveles objetivo

| Medida | Objetivo | Cómo se comprueba |
|---|---|---|
| Mezcla final | **−14 LUFS integrado (±1)** y pico real **≤ −1 dBTP** (apuntar a −1,5) | `postpro.py info` |
| Voz activa (cada línea, en la mezcla) | −12,5 a −13,5 dBFS RMS activo; Tan dentro de ±2 dB de Tin (también la línea 7) | RMS de cada línea en la mezcla |
| Voz antes del limitador | Pico ≤ −1,5 dBFS (nada de la voz sobre 0, defecto D1 del short 4) | pico de `dialogo_110.wav` por línea |
| Efectos **con voz encima** | Pico **≤ −24 dBFS** (≥ 11 dB bajo la voz). Cola cortada antes de K+2 | pico por ventana de 100 ms |
| Efectos sobre una **cifra dicha** («about a year and a half» f372–f412; «about a year» f527–f553) | **Ninguno por encima de −32 dBFS; lo mejor es ninguno** | ventana de f372–f412 y f527–f553 |
| Efectos **sin voz** | Golpes de contacto −12 a −9 dBFS (el golpe 1, el más seco, a −10); explosión hasta −8 dBFS solo en la pausa de voz f695–f727 | por evento |
| Música | ≈ −30 LUFS a corto plazo; **≥ 14 dB bajo la voz**; agachada 6 dB más bajo cada línea de voz (envolvente de 60 ms) | contra `dialogo_110.wav` |
| Los dos pedidos hablados (invitación f438–f471 y consejo f768–f794) | **Nada por encima de la voz**: efectos en silencio, música agachada a su mínimo (5.7) | escucha y medida |
| Silencio antes del toque de f700 | **8 f (f692–f699) sin efectos ni música**, medido por debajo de −90 dBFS | medida por fotograma |

**Regla central: un golpe nunca tapa una cifra ni una palabra de un dato.** Si un golpe de animación se mueve y cae sobre una
palabra, **se mueve el sonido del efecto un fotograma o se acorta su cola**, nunca se sube la voz ni se regenera.

### 5.6 Sonidos: qué existe y qué hay que hacer por código

`motor_de_accion/catalogo.json` lista 27 sonidos y «percusión a 120 pulsos» (todos del short 4; nadie los ha oído). El
código vive en `proyectos/2026-11-26_tin_y_tan_what_is_gta_6/codigo/audio.py` (tabla `SONIDOS`, con su nivel por defecto) y,
más simple, en `motor_de_accion/sonidos/sonido.py`.

**Existen y se reutilizan:** `golpe`, `golpe_agudo`, `golpe_grave`, `silbido`, `silbido_corto`, `silbido_sube`,
`silbido_caida`, `choque_suelo`, `choque_madera` (y `_bajo`, `_agudo`), `choque_pilar`, `cajas_caen`, `roce_suelo`,
`vidrio_grieta`, `chispas`, `fuego_enciende`, `fuego_crece`, `bloqueo_tinta`, `trazo_de_tinta`, `explosion`,
`cola_explosion`, `implosion`, `gotas`, `escurre`, `asterisco_tic`, y los de la firma (`atrapa`, `firma_whoosh_regreso`,
`firma_atrapada`, `firma_chasquido`, `firma_whoosh_ida`). **No se usan:** `campanilla_caja` (es un «ding» agudo y
amable: sonaría a dato o a aviso, y a este video le toca un solo sonido tonal, el de la firma), `mazo_golpe`,
`baston_golpe`, `baston_golpe_grave`, `postes_caen`, `golpe_doble`, `estallido_final`, `subida` (armas y golpes que este
video no tiene; el patrón del suspenso es otro, 5.7).

**Hay que hacerlos por código (nuevos; 0 créditos).** Todos van con ruido filtrado y barridos de tono, sin ningún tono
puro agudo (que no suene a notificación), y se añaden a la tabla `SONIDOS` con su nivel:

| Nombre | Qué suena | Material | Duración | Intensidad (pico sin voz / con voz encima) |
|---|---|---|---|---|
| **`papel_rasga`** | Un papel grueso que se rasga de una vez, de un lado al otro | Ruido de 600 a 5 000 Hz con modulación rápida (≈ 28 Hz) y un barrido de 1 500 a 700 Hz; sin tono | ≈ 7 f (230 ms) | −26 dBFS (no hay voz: va bajo, que no se lea como dato) |
| **`caida_objeto`** | El telescopio de cartón que cae, rebota y queda: dos golpes sordos de cartón, el segundo más corto y bajo, y un roce corto | Golpe de 95 → 60 Hz con cuerpo de cartón (ruido de 200 a 1 800 Hz que cae rápido); sin campana ni metal | 12 f de caída, impacto en f587 (≈ 130 ms), rebote en f595 (≈ 90 ms, −8 dB), roce de ≈ 120 ms | −22 dBFS el impacto; −30 el rebote |
| **`grieta_abre`** | El suelo se abre: un crujido grave que se alarga | Ruido de 40 a 220 Hz con crujidos lentos, barrido 70 → 40 Hz; **sin energía arriba de 400 Hz** salvo un clic de −38 dBFS | 16 f (f30–f45) más 24 f de resto bajo (f46–f69, crece) | −26 dBFS (cae bajo «GTA 6», 5.4 nota A) |
| **`regla_marcas`** | La regla de tinta se dibuja con tres marcas rápidas (dibujo) | Variante de `trazo_de_tinta` (ruido de 1 500 a 7 000 Hz) con 3 «tic» de lápiz sobre una vara | 10 f | −26 dBFS |
| **`regla_golpe`** | La regla de tinta pega: vara flexible de madera, golpe plano con un temblor corto | Golpe de 130 → 90 Hz + chasquido de 2 000 Hz y vibración de 1 200 Hz que decae en 120 ms | ≈ 200 ms | −10 dBFS sin voz (su cola va bajo −26 en K+2) |
| **`farol_choque`** | Choque contra el poste del farol: metal hueco y vidrio chico que se rompe | Metal (resonancia de 380 y 640 Hz, decae en 0,35 s) + `vidrio_grieta` bajo | ≈ 350 ms | −11 dBFS sin voz; cola bajo −26 en K+2 |
| **`persiana_choque`** | Choque contra la persiana metálica: lámina ondulada que vibra y queda abollada | Ruido de 500 a 4 000 Hz con vibración de 18 Hz, resonancia a 900 Hz, decae en 0,5 s | ≈ 450 ms | −11 dBFS sin voz; cola bajo −26 en K+2 |
| **`paquete_desliza`** | Una caja lisa de cartón que se desliza por el suelo, despacio | `roce_suelo` más lento y grave (200 a 1 400 Hz) | 22 f | −30 dBFS (suspenso: casi nada) |
| **`toque_regla`** | La punta de la regla toca el paquete: un «tic» seco | Un solo golpecito de ruido de 1 800 a 6 000 Hz, 15 ms | 15 ms | −22 dBFS (es lo único que se oye en f700; antes, 8 f de silencio) |
| **`tinta_sube`** | La tinta del paquete se hincha un instante antes de reventar | Barrido ascendente de 120 a 380 Hz con ruido de 200 a 2 000 Hz, sube de nivel | 6 f (f702–f707) | de −34 a −16 dBFS (no hay voz) |
| **`fuego_crepita`** | Fuego pequeño al fondo: crepitar bajo continuo | Ruido de 80 a 900 Hz, muchas chispas de 3 a 8 ms; no se repite igual (semilla distinta cada 2 s) | continuo f344–f690 y f733–f811 | −40 dBFS (≥ 25 dB bajo la voz); se corta f690 a f699 y en f372–f412 y f527–f553 baja a −46 |
| **`ticks_regla` (música)** | Ver 5.7 | — | — | — |

`papel_rasga` y `caida_objeto` son los dos que pide el brief. Para que el objeto que cae **no suene a dato ni a error**:
sin tono definido, sin campana, sin barrido que suba (el oído lee un barrido ascendente como aviso); un golpe de cartón,
sordo, que cae en vez de subir; y lo bastante bajo (−22) para que no se oiga como un golpe de pelea. Cae en pleno respiro 2,
con la voz en silencio, así que **se oye, y por eso va tan bajo**: el sentido es que Tan lo mira 6 f y nadie lo comenta; si el
sonido fuera fuerte, el oído lo trataría como el pico del video.

### 5.7 Música: solo percusión por código, otro patrón que el del short 4

- **Qué es.** No hay melodía ni armonía (nada que pueda parecerse a la música del juego ni a la de nadie). Dos capas:
  1. **`tic_de_regla`**: un «tic» seco de ruido filtrado (2 000 a 7 000 Hz, 12 ms), **sin tono**, a **90 pulsos por minuto =
     un tic cada 20 f** (30 f/s: 90 BPM caen en 20 f exactos, igual de limpio que 120 en 15 f). Suena como una regla que mide
     o un reloj que espera.
  2. **`latido`**: un golpe doble grave (lub-dub: 55 Hz y 48 Hz, 90 ms y 70 ms, separados 8 f) cada **40 f**, solo en los
     tramos de tensión.
- **Por qué es distinta de la del short 4** (política de contenido repetitivo; F6 del brief). El short 4 tiene un bombo
  regular a 120 con capas que suben tras cada golpe: se siente como baile. Aquí no hay bombo: hay un reloj y un latido que
  se **aceleran** y se **cortan**. Es una música que espera, no que empuja.
- **Por qué esa emoción.** El video **mide** (dos precedentes con regla) y **espera** una respuesta que no llega: «no hay
  fecha». El tic es la regla y el reloj; el latido es la tensión que sube (perfil emocional, arco). En el suspenso el tic
  se acelera (suspenso: R5 de `manual/14`, «looming» auditivo, investigación); al revés del short 4, **la música no sube
  tras cada golpe**: cae en cada contacto. El corte total antes de f700 y la vuelta al latido lento después sostienen el
  alivio con humor seco (R39, oficio; el silencio agranda el pico: hipótesis del equipo).
- **Fuera de la música:** nada de sintetizador, de bajo con notas, de arpegio ni de loop grabado. Por código con `numpy`,
  como `pista_musica()` del short 4, **0 créditos**.
- **Prompt para el generador de música solo si el dueño lo pide** (la música la pone el dueño salvo que pida generarla): género
  percusión minimalista tipo reloj, sin melodía; 90 BPM; sin tonalidad (solo golpes secos y un latido grave de 55 Hz);
  instrumentos: clics de regla de madera, latido de bombo bajo; emoción: espera y suspenso contenido; estructura: 0:00 a 0:23
  tic constante que acelera de 90 a 150 BPM, 0:23 a 0:24 corte total, 0:24 a 0:31 un latido lento; duración 31 s; sin
  voz. No se genera sin sí del dueño y cotización de producción.

**Mapa por fotogramas** (la música se detiene alrededor de cada K: 6 f antes y 2 f después, como la pausa de los golpes):

| f | Qué suena | Nivel (corto plazo) |
|---|---|---|
| 0–29 | Nada (firma; sus sonidos, los de siempre) | — |
| 30–87 | `tic` cada 20 f desde f30; sin latido | ≈ −34 LUFS |
| 82–89 | **Pausa antes de K = f88** | silencio |
| 90–300 | `tic` + `latido` cada 40 f; pausa 6 f antes y 2 f después de f130 y f212; bajo agachado 6 dB bajo cada línea | ≈ −31 LUFS |
| 296–329 | Respiro 1: solo `tic`, más suave | ≈ −36 LUFS |
| 330–437 | `tic` + `latido`; pausa alrededor de f336; sin `latido` en f372–f412 (cifra) | ≈ −31 LUFS |
| **438–471** | **Invitación: solo un `tic` por 20 f, agachado al mínimo (≥ 20 dB bajo la voz). Nada más** | ≈ −40 LUFS |
| 472–553 | `tic` + `latido`; pausa alrededor de f484; sin `latido` en f527–f553 | ≈ −31 LUFS |
| 554–599 | Respiro 2: solo `latido` cada 40 f, muy bajo; **sin `tic`** (que el objeto que cae se oiga sin competir) | ≈ −38 LUFS |
| 600–691 | `tic` que **acelera**: cada 20 f hasta f640, cada 15 f hasta f670, cada 10 f hasta f691; el último tic en f689; pausa 6 f antes del bloqueo de f652 | de −33 a −29 LUFS |
| **692–699** | **Silencio total: 8 f, sin música ni efectos** | −∞ |
| 700–732 | Nada de música (la explosión es el sonido) | — |
| 733–799 | Respiro 3: un `latido` cada 40 f desde f741, muy bajo; **cero en f764–f796** (consejo) | ≈ −40 LUFS |
| 800–899 | Pausa en f806 a f813 (K = f812); desde f832 un `tic` cada 30 f, cada vez más espaciado; el último en f869 (cuando termina el goteo); luego nada | ≈ −36 LUFS |
| 900–929 | Nada. La firma, con los sonidos de siempre; la música ya está a cero, así que la regla «−6 dB desde c −24» se cumple sin cambiar nada | — |

### 5.8 Lista de golpes: efecto por fotograma (voz y efectos, tal como se pegarán)

«K» es el de 2.2 y 2.3; **se ajusta a los K de la sección 4**. Pico en K −1 salvo que se diga. Toda cola que cruce el
arranque de una línea de Tin (K+2) se **corta con fundido de ≤ 80 ms** y queda bajo −26 dBFS en K+2, porque Tin empieza
exactamente 2 f después del contacto.

| f | Qué pasa en imagen | Sonido | Pico sin voz | Voz que suena |
|---|---|---|---|---|
| 0–10 | La firma: lápiz de regreso y atrapado | Los de siempre: `firma_whoosh_regreso`, `firma_atrapada` en f10, `firma_chasquido` | de la firma | — |
| 14–82 | Tan pregunta | (sin efectos arriba de −26: ver siguiente fila) | — | **Línea 1, Tan** |
| 30–45 | El rival sale de la grieta (derecha) | **`grieta_abre`**: solo grave, **bajo «GTA 6»** (cae en f ≈ 20–55 de la voz: nota A) | **−26** | Línea 1 encima |
| 46–69 | Crece a 1,5 veces | Resto bajo de `grieta_abre`, subiendo 3 dB hasta f69; `roce_suelo` muy bajo (−34) en f58–f69 | −30 | Línea 1 hasta f82 |
| 82–87 | **Pausa de efectos y música** | Silencio (6 f) | — | Tan termina en f82 |
| **87 (K −1; K = 88)** | **Golpe 1: Tin, sin arma; el más corto y seco.** El rival choca con la pila de torres | `golpe` seco (tono alto, cuerpo corto, cola ≤ 90 ms) + `silbido_corto` en f85 | **−10** | Tin entra en f90 (K+2): cola bajo −26 |
| 100–101 | Una torre se rompe y se queda rota | `choque_madera_agudo` + `vidrio_grieta` bajo | −24 (hay voz) | **Línea 2, «Not announced.»** (f90–f117): efectos ≤ −24 |
| 118–129 | El rival se levanta | `roce_suelo` muy bajo | −34 | — |
| **129 (K = 130)** | **Golpe 2: Tan, de cuerpo.** Choca con cajas de cartón | `golpe_agudo` (un tono arriba del golpe 1) + `cajas_caen` | **−10** | Tin entra en f132 (K+2) |
| 150–300 | Cuatro acciones; el rival contraataca y falla | `silbido` en cada esquive; `choque_madera_bajo` y `cajas_caen` bajos en roturas | −24 (hay voz casi siempre) | **Líneas 3 y 4** |
| ≈ 245 (el que fije animación) | **Contraataque del rival que falla** | `silbido_sube` más largo; sin golpe (falla) | −24 | Línea 4 (f214–f295) |
| **211 (K = 212)** | **Golpe 3: Tin, de cuerpo.** Choca contra un monitor | `golpe_grave` + `vidrio_grieta` (el monitor) | **−10** | Tin entra en f214 |
| 296–329 | Respiro 1: el lápiz dibuja la regla | **`regla_marcas`** (3 marcas) | −26 | — |
| **335 (K = 336)** | **Medida 1: Tin, regla.** El rival sube y choca con el farol; la barra de «574 days» se dibuja | **`regla_golpe`** (f335) + **`farol_choque`** (f336) | **−10** | Tin entra en f338: cola bajo −26 |
| 344 | Chispas del farol: fuego pequeño en las cajas | `chispas` corto + `fuego_enciende` | −26 (hay voz) | Línea 6 (f338–f432) |
| 344–690 | Fuego pequeño al fondo | **`fuego_crepita`** continuo | −40 | (baja a −46 en f372–f412 y f527–f553) |
| **372–412** | **«about a year and a half»** | **Ningún efecto nuevo**; el trazo de la barra (f374–f379) queda en `regla_marcas` a **−34** o se quita | **≤ −32** | **Cifra** |
| 438–471 | Invitación: Tan recibe la regla, el rival baja del farol | **Silencio de efectos** (ni el pase de la regla ni el rival se oyen) | — | **Línea 7, Tan** |
| **483 (K = 484)** | **Medida 2: Tan, regla.** El rival choca con la persiana: abolladura | **`regla_golpe`** (f483) + **`persiana_choque`** (f484) | **−10** | Tin entra en f486 |
| 529–569 | Renglón 2: la barra más corta | Ningún efecto arriba de −34 | **≤ −32** | **Cifra** («about a year», f527–f553) |
| 554–569 | El rival se despega de la persiana | `roce_suelo` muy bajo | −34 | — |
| 570–576 | **Rasgadura del papel** (de donde cae el objeto) | **`papel_rasga`** (≈ 7 f, que termine en f576; si animación la mueve, se mueve) | **−26** | Sin voz |
| 576–587 | Cae el telescopio (12 f) | **`caida_objeto`**: fase de caída (roce que baja) | −28 | Sin voz |
| **587** | Impacto | **`caida_objeto`**: golpe sordo de cartón | **−22** | Sin voz |
| 588–595 | Rebote (8 f); Tan lo mira 6 f (f588–f593) | **`caida_objeto`**: rebote en f595 (−8 dB) y roce; **nadie reacciona con sonido** | −30 | Sin voz |
| 596–611 | El rival dibuja el paquete | `trazo_de_tinta` | −26 | — |
| 596–651 | Lo desliza hacia ellos | **`paquete_desliza`** | −30 | Línea 9 empieza en f600 |
| 600–694 | Suspenso | La música acelera (5.7); no hay golpe | — | **Línea 9, Tin** |
| 646–651 | **Pausa de 6 f antes del bloqueo** | Música callada | — | (la voz sigue) |
| **652** | **Bloqueo: Tin frena la mano de Tan con la regla** | `bloqueo_tinta` (suave: corte seco, sin tono largo, cola ≤ 120 ms) | −24 (hay voz) | Línea 9 (el dato entra en f654) |
| **692–699** | **Silencio total: sin efectos ni música (8 f)** | — | **−∞** | Voz callada f695–f727 (la línea 9 acaba en f694) |
| **700** | Tin toca el paquete con la regla, de lejos | **`toque_regla`** (único sonido) | −22 | — |
| 702–707 | El paquete se hincha | **`tinta_sube`** (6 f) | −34 → −16 | — |
| **≈ 706 (expansión; la fija animación)** | **EXPLOSIÓN por fases (f702–f726); cuadros invertidos f702–f712** | **`explosion` en la expansión, no en la ignición** (como en el short 4) + `chispas` | **−8** | — |
| 708–727 | Humo y fuego | `cola_explosion`, **llega a −40 dBFS en f727** | de −23 a −40 | — |
| 728–761 | Tin dice el dato | `fuego_crepita` bajo y nada más; sin cola de explosión | **≤ −40** | **Línea 10, Tin** |
| 735–799 | El humo despeja | Silencio de efectos salvo el crepitar | — | — |
| 768–794 | Consejo | **Nada por encima de la voz**: solo el crepitar a −46; música a cero | — | **Línea 11, Tan** |
| 796–811 | El rival se planta; el rizo en alto | Nada (humor seco) | — | — |
| 806–813 | **Pausa antes del golpe final** | Silencio de efectos y música | — | — |
| **811 (K = 812)** | **Golpe 5: Tin, regla** | **`regla_golpe`** (grave) + `golpe_grave` | **−10** | Tin entra en f814 |
| 812–815 | P-004: la segunda marca (asterisco) en la pestaña | `asterisco_tic` (6 golpecitos de lápiz) | −30 | — |
| 814–831 | **Implosión** (apaga el fuego, se lleva el humo) | **`implosion`**, **con la banda de voz (300 Hz a 4 kHz) recortada a −32 dBFS; el grave (30 a 150 Hz) entra a −24 dBFS** (si no, tapa «No official»); **corte seco en f831**; el `fuego_crepita` se corta en f831 | −24 con voz | **Línea 12, Tin** (f814–f888) |
| 831–855 | Nada se mueve | Silencio | — | Línea 12 |
| 856–869 | El resto del rival gotea por el borde izquierdo (P-005, 14 f) | **`escurre`** (f856) + **`gotas`** (f860–f869); la regla se deshace en `gotas` más agudas en f866 | −28 | Línea 12 hasta f888 |
| 869 | Último tic de la música | `tic_de_regla`, solo | −36 LUFS | Línea 12 |
| 890–899 | Salida | Silencio | — | Voz terminó en f888 |
| 900–929 | La firma: plano de portada y lanzamiento | Los de siempre: `firma_chasquido` y `firma_whoosh_ida` en c −15 | de la firma | — |

**Nota A (la grieta bajo «GTA 6»).** En el short 4 un choque cayó sobre «GTA six» y el reconocedor oyó un «it» de más. Aquí
la grieta (f30–f45) cae bajo la voz de Tan, que dice «Is GTA 6 coming to PC?» entre f14 y f82. Por eso la grieta se escribe
sin energía arriba de 400 Hz (el habla pesa de 300 Hz a 4 kHz) y a −26 dBFS. Con la voz real se mide: si una sílaba de «GTA 6»
cae en f30 a f45, se baja la grieta a −30 y se comprueba con `revisar_voz.py`.

**Nota B (implosión sobre «No official PC date»).** La voz de Tin entra en f814, el mismo fotograma en que arranca la
implosión (f814–f831), y «No official PC date» es el titular del video. Es el tramo más peligroso de la mezcla: el sonido es
casi solo grave. **Si al oír la mezcla «No official» se pierde, se pide al director creativo mover la línea 12 a f818 o más**
(no se regenera nada, la voz se recorta en edición), nunca bajar la voz.

### 5.9 Lista de comprobación de escucha humana (nadie del equipo ha oído nada)

Antes de la prueba y de publicar, **una persona oye la mezcla completa con auriculares y con el altavoz del teléfono**, y
marca:

1. **Voz:** cada línea de 5.2 se oye completa y con el sentido del guion: «Not announced», «Xbox Series X and S» (sin
   «ten»), «Red Dead Redemption 2» (sin trabarse), «malware», «GTA 5» y «GTA 6». No sobra ninguna palabra (el «it» del
   short 4).
2. **Línea 7** («Subscribe for facts, checked.») tan fuerte como la de Tin y sin aspereza (defecto D1 del short 4).
3. **Línea 11** («Don't download them.»): seca y baja, **no regaño**.
4. **Invitación (f438–f471) y consejo (f768–f794):** limpios, **ni un efecto** ni una nota de música por encima.
5. **Cifras:** se oyen «about a year and a half» y «about a year» sin nada encima.
6. **Golpes:** cada contacto suena **en el fotograma de la estrella o uno antes**; ninguno pesa más que la voz; el más corto y
   seco es el 1.
7. **Grieta (f30–f45):** se siente, no se oye como una palabra más; no cambia «GTA 6».
8. **Objeto que cae (f570–f595):** se oye **bajo y breve**, no se lee como aviso, error ni dato; no hay una campanilla ni un
   «ding».
9. **Silencio de 8 f (f692–f699):** se nota como pausa, no como falla de audio; después del `toque_regla` el pico no sorprende
   por clipping.
10. **Explosión:** sube en la expansión, cae a casi nada en f727; no pisa «Some carry malware».
11. **Implosión (f814–f831):** «No official PC date» se oye entero (nota B).
12. **Música:** se oye como reloj y latido, no como baile; no se parece a la del short 4; no tapa nada.
13. **Goteo de salida (f856–f869):** suena a tinta que se va, sin sonar triste ni gracioso de más.
14. **Sin clics, saturación ni cortes** en las uniones de las líneas ni al final.

**Medidas que sí hace el diseñador de sonido sin oír** (como en `revision_v4_sonido.md`): `postpro.py info` (−14 ±1 LUFS,
≤ −1 dBTP); pico de cada efecto por fotograma frente a su K; voz menos efectos por ventana de 100 ms (≥ 11 dB); silencio de
f692–f699; `revisar_voz.py` contra el guion. **Eso no sustituye la escucha**: el control 3 no se firma como PASA de
publicación sin ella.

### 5.10 Pedidos a otros oficios

- **Animación:** confirmar los K reales de 4 y el fotograma de la expansión de la explosión; confirmar que la rasgadura termina
  en f576 y el impacto del telescopio cae en f587.
- **Producción:** cotizar la voz (5.4, «no es cotización»); añadir a `audio.py` los sonidos nuevos de 5.6 y la percusión de 5.7;
  el nombre de los eventos del motor sigue el catálogo.
- **Director creativo:** si la nota B se confirma, mover la línea 12 a f818 o más.

- **Voz en off o labios:** voz en off (los personajes no tienen boca animada); sin costo extra de animación. La voz es el
  único gasto (5.4).
