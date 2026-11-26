# Revisión de animación · Short 4 (TIN-EN-S-004) · versión 2

- **Fecha:** 2026-11-26. **Quién:** Equipo de producción audiovisual: director de animación, con fotografía y el
  supervisor de continuidad. **Motivo:** el dueño no aprobó la v2. Textual: «intentan correr y casi no se mueven».
  Solicitud: `cambios/2026-11-26_short4_v2_animacion_en_el_espacio.md` (rama del Generador).
- **Qué se revisó:** el guion del motor `motor_de_accion/guiones/tin_en_s_004.js`, `escena.html`, la tabla de cámaras
  `tin_en_s_004.tiempos.json` y las revisiones de la v2 que ya existían (`revision_v2_continuidad.md` y
  `revision_v2_fotografia.md`, rama `claude/laughing-dirac-s4pmig`). **No se repite lo que ya está en ellas**: aquí va
  lo que faltaba, la carrera.
- **Cómo se midió:** `video-studio/herramientas/medir_carrera.mjs` (nuevo, gratis). Evalúa el guion sin renderizar,
  reproduce la interpolación del motor (`pista`) y proyecta cada fotograma con la cámara de su plano. Lo previsto
  coincide con lo que midió continuidad sobre el video. Ejemplo: en f671–f681 la cabeza de Tin avanza ≈ 59 px según el
  guion y 44 px en su medición, y lo mismo pasa con el vaivén de f236–f282.
- **Límite:** esta sesión no vio el MP4. El archivo está solo en el PC del dueño y esta sesión corre en la nube. Se
  le pidieron a Keter el sha256 y las posiciones de las cabezas por fotograma, y ya llegaron: el archivo coincide y
  las medidas confirman lo calculado (sección 4). La voz (control 3) sigue sin firmar.

## 1. Diagnóstico: por qué «intentan correr y casi no se mueven»

Las piernas y el cuerpo van por **dos pistas que no se hablan**. `corre()` cambia de pose cada 4 fotogramas fijos,
sin mirar cuánto avanza el cuerpo, y la posición va por otra pista con sus propias claves. El resultado:

| Tramo (s) | Quién | Plano | Pasos/s | Avance real | Avance que piden las piernas | Avance / paso | Hacia dónde | En pantalla |
|---|---|---|---|---|---|---|---|---|
| 1,67–2,10 | Tin | P2 | ≈ 4,6 | 0,70 u | 1,6 u | **0,45** | adelante | 0,33 cuerpos/s |
| 6,67–8,30 | Tin | P7 | ≈ 7,3 | 2,18 u (casi todo hacia cámara) | 9,4 u | **0,23** | **de espaldas** en x | 0,35 cuerpos/s |
| 9,47–9,90 | Tin | P7 | ≈ 6,9 | 2,58 u | 2,3 u | 1,10 | adelante | 1,34 cuerpos/s (**el único que funciona**) |
| 11,97–12,80 | Tan | P10 | ≈ 7,2 | 0,40 u | 4,7 u | **0,08** | adelante | 0,12 cuerpos/s |
| 12,50–14,13 | Tin | P10 | ≈ 7,3 | 1,47 u | 9,4 u | **0,16** | **de espaldas** (avanza a la izquierda mirando a la derecha) | 0,48 cuerpos/s |
| 19,00–19,43 | Tan | P14 | ≈ 6,9 | 2,23 u | 2,3 u | 0,95 | adelante | 2,5 cuerpos/s (es el cruce B2 de fotografía) |
| 21,00–21,83 | Tan | P15 | ≈ 7,2 | 2,02 u | 4,7 u | **0,43** | adelante | 0,59 cuerpos/s |
| 22,37–22,73 | Tin y Tan | P16 remate | ≈ 5,5 | 1,10 u, **todo hacia el fondo** | 1,6 u | 0,70 | adelante | 0,45 cuerpos/s |
| 25,67–26,63 | Tin | P19 respiro | ≈ 7,2 | 0,33 u | 5,5 u | **0,06** | adelante | 0,09 cuerpos/s |
| 25,67–26,63 | Tan | P19 respiro | ≈ 7,2 | 0,60 u | 5,5 u | **0,11** | **de espaldas** | 0,25 cuerpos/s |
| 4,70–5,13 | rival | P5 | ≈ 6,9 | 4,43 u | 2,5 u | **1,75** (patina hacia adelante) | adelante | 1,88 cuerpos/s |

«Avance / paso» = lo que avanza el cuerpo ÷ lo que tendría que avanzar para que el pie apoyado no resbale (pasos ×
zancada; zancada de Tin y Tan ≈ 0,78 u, la distancia entre pies de `corre1`). 1 es correcto; por debajo de ≈ 0,8 los
pies patinan hacia atrás y se lee «corre en el sitio»; por encima, el cuerpo se desliza. Los tramos de 1 a 5 f no
están en la tabla.

Las causas, en orden de peso:

1. **Cadencia fija y demasiado alta.** Un paso cada 4 f es ≈ 7,5 pasos por segundo, más rápido que un velocista (≈ 4 a
   5 pasos/s; referencia de oficio, sin fuente consultada hoy). Con piernas a esa velocidad y un cuerpo que avanza
   0,3–1,5 u/s, el pie apoyado resbala 3 a 15 veces la distancia que avanza el cuerpo. **8 de los 11 tramos están por
   debajo de 0,5.**
2. **Corren hacia el fondo o hacia la cámara con un dibujo de perfil.** El dibujo dice «voy a la derecha» y el
   cuerpo va en profundidad (P7, remate P16). Con la cámara frontal fija y la lente larga (36° vertical, ≈ 21°
   horizontal), avanzar 1,1 u hacia el fondo a ≈ 9 u de la cámara cambia el tamaño ≈ 12 % y la posición unos 60 px. Es
   la misma causa que fotografía llama «el mundo es 3D pero se mira como una pantalla plana».
3. **Tres tramos corren de espaldas** (Tin f200–f248 y f375–f423, Tan f770–f798): el cuerpo va en sentido contrario
   al que miran las piernas, como un *moonwalk*.
4. **No hay fase de vuelo.** `colocar()` apoya siempre el punto más bajo del dibujo en el suelo, y el ciclo es solo
   `corre1` ↔ `corre2` con mezcla lineal: las piernas hacen tijera y los dos pies nunca despegan. Sin contacto, sin
   recogida y sin vuelo, una carrera se lee como trote nervioso en el lugar.
5. **La cámara lenta del remate frena el mundo, no a los personajes.** La dirección pide la carrera previa al remate
   «a 0,3». En el motor, `reloj` (LENTOS) solo frena humo, polvo y trozos: el cuerpo avanza poco, como en cámara
   lenta, pero las piernas siguen a ≈ 5,5 pasos/s. Es la versión más clara de la queja del dueño.
6. **El borrón de movimiento que pide la dirección para las carreras rápidas (1,3 con borrón) está apagado.** En
   modo por fotogramas, `dibujar` recibe `GU.porFotogramas ? false : …`, así que nunca se dibuja.
7. **Arranques y frenadas suavizados con las piernas a tope.** En f200–f248 y f375–f423 la posición usa la curva por
   defecto (`io`, lenta al principio y al final) y las piernas ya están a 7,5 pasos/s desde el primer fotograma:
   patinan más al arrancar y al frenar. No hay anticipación antes de arrancar ni resbalón al frenar.

## 2. Corrección para la versión 3

Todo es código: **0 créditos**. Se hace en el motor y en el guion; la voz, el guion hablado, los datos y la paleta no
cambian.

### Director de animación (el ciclo)

1. **El paso sale de la distancia, no del reloj.** La fase de la pierna = distancia recorrida en el suelo ÷ (2 ×
   zancada). Se calcula en `actualizar()` con `rapidez`, que ya se mide, y reemplaza a `corre()`. Así, si el cuerpo no
   avanza, las piernas no corren.
2. **Cadencia según la velocidad, con techo:** trote ≈ 3 pasos/s (10 f por paso) hasta ≈ 2,3 u/s; carrera ≈ 4 a 5
   pasos/s (6 a 7 f por paso) hasta ≈ 3,9 u/s. Más rápido no se pide con piernas: se pide con borrón. Si un tramo
   recorre menos de una zancada (≈ 0,8 u), **no es carrera**: son dos pasos cortos, un salto o un deslizamiento con la
   pose `resbala`.
3. **Ciclo de 4 poses** en vez de 2: contacto, recibe (cadera abajo, rodilla doblada), impulso y **vuelo** (los dos
   pies arriba, cadera ≈ 0,08–0,12 u más alta). El motor tiene que dejar despegar al dibujo durante el vuelo
   (`colocar()` con un `y` del ciclo, no siempre el punto más bajo en el suelo).
4. **Anticipación y frenada:** 2–3 f de carga hacia adelante antes del primer paso; los dos primeros pasos más
   cortos; al frenar, `resbala` 4–6 f con polvo. La posición va en `lin` mientras la velocidad es constante; las curvas
   solo en el arranque y la frenada, junto con el cambio de zancada.
5. **Nadie corre de espaldas:** `mira` = sentido del avance en pantalla. Retroceder es otro ciclo (pasos hacia atrás,
   torso hacia atrás), y solo si la acción lo pide.
6. **Cámara lenta de verdad en el remate:** el `reloj` también frena a Tin y a Tan (piernas y cuerpo a 0,3), o se
   quita el 0,3 de la carrera y la tensión se hace con la pausa de 6 f que ya existe. Recomiendo frenar a los dos:
   es lo que pide la dirección.
7. **Borrón en las carreras rápidas:** se enciende en modo por fotogramas cuando la cabeza se mueve más de ≈ 40 px por
   fotograma; el borrón ya existe (copia anterior al 22 %).

### Director de fotografía (la cámara en las carreras)

Se suma a la opción «media» que ya recomendó fotografía (`revision_v2_fotografia.md`, sección 3: lente de 48°,
horizonte desplazado y carriles):

1. **Toda carrera tiene al menos la mitad de su recorrido de lado** respecto de la cámara: diagonal de 35° a 45° como
   mínimo. Si la historia pide correr hacia el fondo (el remate contra el rival), se corta a un plano lateral para la
   carrera, o la cámara la acompaña con un giro suave de 12–16 f (el punto 5 de fotografía, que necesita su firma y la
   del jefe de producción).
2. **Una carrera dura lo que tarda en recorrerse.** Con ≈ 3,9 u/s, 1 s de carrera son ≈ 4 u; en el ancho útil de un
   general (≈ 3 u) no caben más de ≈ 0,8 s de carrera lateral sin acompañar.
3. **Respiro (P19, f770–f798):** ahí no hay carrera que contar. Se cambia a guardia con acción secundaria (bufanda,
   respiración) o a dos pasos para acomodarse.

### Supervisor de continuidad (cómo se comprueba)

1. **Control nuevo, bloqueante para la v3:** `node --no-warnings video-studio/herramientas/medir_carrera.mjs
   <motor_de_accion> tin_en_s_004`. Pasa si en todos los tramos de carrera de 6 f o más se cumple: avance / paso entre
   0,8 y 1,2, «adelante» en el sentido de avance y ≥ 0,6 cuerpos/s en pantalla, o el tramo está declarado como cámara
   lenta y el reloj frena también al personaje. Esto atiende el pedido de fotografía de «un control automático nuevo»
   para lo que hoy no se mide. Además, con `… tin_en_s_004 desliza`: ningún tramo de 0,3 u o más se desliza sin
   pasos, salvo el rebote de 0,2–0,3 u justo después de un contacto.
2. Después del render, en el video: posiciones de las cabezas por fotograma, como hizo continuidad en la v2.
   Comprobar que el pie apoyado no se mueve más de ≈ 10 px mientras está en el suelo (en las hojas a todos los
   fotogramas de cada carrera).
3. La v3 se ve **en movimiento** antes de presentarla, no solo en hojas (pedido de fotografía).

### Por tramo

| Tramo | Corrección |
|---|---|
| Tin f50–f62 (P2) | Dos pasos de acomodo, no carrera: recorre 0,7 u |
| Tin f200–f248 (P7) | Trayectoria en diagonal hacia el cartel, `mira` hacia el avance; ≈ 1,5 s de trote con ciclo por distancia; o acortar a 0,8 s y cortar |
| Tin f284–f296 (P7) | Bien de velocidad; agregar vuelo y anticipación |
| Tan f359–f383 y Tin f375–f423 (P10) | Tan: dos pasos (recorre 0,4 u). Tin: corre hacia la izquierda mirando a la izquierda, o cambia de lugar con un corte; hoy retrocede «corriendo» 1,4 u |
| Tan f570–f582 (P14) | Velocidad correcta, pero es el cruce que rompe el eje (B2 de fotografía): se mueve al plano general P12c, como propone fotografía |
| Tan f630–f654 (P15) | Ciclo por distancia; con mazo, trote (3 pasos/s) |
| Remate f671–f681 (P16) | Cámara lenta real (piernas y cuerpo a 0,3) **y** recorrido en diagonal o plano lateral; el corte al contacto no salta al centro (C5 de continuidad) |
| Respiro f770–f798 (P19) | Sin carrera: guardia con acción secundaria |
| Rival f141–f153 (P5) | Pasos más largos o más pasos: hoy el cuerpo va 1,75 veces más rápido que las piernas |

## 3. Controles del capítulo 12 sobre la v2 (lo que se pudo comprobar desde aquí)

| Control | Estado | Evidencia |
|---|---|---|
| 1 · Texto | **NO PASA (por poco)** | `revisar_texto.py` con el glosario del Generador: subtítulos en inglés y `componer.py` → 0 errores. Subtítulos en español → 2 errores, «Theft» y «Games» (parte de «Grand Theft Auto» y «Rockstar Games»): van al glosario con su porqué. Siguen los tiempos encimados de los `.srt` (T1 de continuidad: p. ej., la línea 2 termina en 5,767 s y la 3 empieza en 5,700 s). En la rama del equipo el glosario no tiene GTA ni Rockstar: se resuelve al sincronizar ramas. |
| 2 · Cifras | PASA | Recalculado: del 17-09-2013 al 19-11-2026 = 4.811 días = 13 años y 63 días. Son enteros: no llevan «≈». |
| 3 · Voz | **Sin firmar** | Nadie la ha oído (el reconocedor oye un «it» de más). Necesita una escucha humana |
| 4 · Imagen / portada | PASA, con nota | `miniatura.png` de 1080×1920 y 339 KB. «GTA 7?» y «Facts, Checked» (3 palabras con mayúscula inicial y sin la respuesta) entre y ≈ 440 y ≈ 700; caras de Tin y Tan en x ≈ 220 y ≈ 860, y ≈ 1280, dentro de la zona útil; televisor en el centro (y ≈ 780–1040). Nota: Tin y Tan se miran entre ellos, no al objeto (regla 29.5). |
| 5 · Video | **NO PASA** | Las carreras de la sección 1 y los deslizamientos de la sección 4, confirmados en el MP4, más lo que ya marcaron continuidad (CORREGIR) y fotografía (B1–B6) |
| 8 · Color | PASA la medida; queda una decisión | Miniatura ≈ 91 % dentro de la paleta del motor (`c_alto_voltaje`); el video, ≈ 91 % (`color_v2.txt`). Contrastes: tinta sobre amarillo 11,8:1, sobre fondo 13,5:1 y sobre suelo 15,2:1; todo ≥ 7:1. Pendiente M6 de fotografía: el anillo amarillo de la explosión contradice la sección 3b (lo decide el director creativo) |

## 4. Confirmado con el video (medidas de Keter, 2026-11-26)

Keter midió el MP4 en el PC del dueño, en solo lectura y sin subirlo a ningún lado. **Archivo verificado:** 20.794.162
bytes, sha256 `9d6d9048…5c35e7dc` (coincide), 1080×1920, 30 f/s, 986 f. Midió el centro de la cabeza de Tin y de Tan
en 356 fotogramas de los tramos de carrera (copia en el PC: `Canal YouTube/mediciones/2026-11-26_short04_v2_cabezas.json`;
no va al repositorio).

| Tramo | Guion (px/s en pantalla) | Video (px/s, cabeza) | Lectura |
|---|---|---|---|
| Tin f50–f62 | ≈ 137 | ≈ 125 (774 → 724) | Coincide |
| Tin f200–f248 | ≈ 137 | ≈ 110 (x 634 → 482, y 1314 → 1397) | Coincide: ≈ 0,25 cuerpos/s |
| Tin f284–f296 | ≈ 673 | ≈ 628 (499 → 750) | Coincide: la única carrera que avanza |
| Tan f359–f383 | ≈ 64 | ≈ 64 (146 → 197) | Coincide: corre en el lugar |
| Tin f375–f423 | ≈ 224 | ≈ 222 (861 → 505) | Coincide: retrocede hacia la izquierda |
| Tan f630–f654 | ≈ 274 | ≈ 250 (700 → 500) | Coincide |
| Remate f671–f681 | — | Tin ≈ 132 (263 → 307), Tan ≈ 102 (732 → 698), cabezas que se achican ≈ 20 % | Peor de lo previsto: ≈ 0,2 cuerpos/s |
| Tin f770–f798 (respiro) | ≈ 41 | ≈ 31 (306 → 335 en 28 f) | Coincide: corre en el lugar |

- **La cadencia se ve en el video:** la altura de la cabeza oscila con un ciclo de 4 fotogramas, de ≈ 15–20 px (por
  ejemplo, Tin en f200, f204, f208, f212: y 1314, 1317, 1321, 1326 en los picos). Son los ≈ 7,5 pasos/s del motor.
- **Lo que pasa en el remate (C5 de continuidad), explicado:** después de 10 f de carrera que casi no avanza, en
  f682–f686 las cabezas se **alejan** ≈ 200 px cada una (Tin 307 → 113 y Tan 698 → 901). No es la cámara: es la pose
  `carga`, que echa el torso ≈ 44° hacia atrás justo después de la carrera (torso de +30° a −14°; la cabeza retrocede
  ≈ 0,67 u, ≈ 200 px a esa distancia). Quedan quietos 7 f y en f694 vuelven de golpe ≈ 240 px en 1 fotograma (Tin
  118 → 354, Tan 897 → 633). Corrección: después de una carrera, la anticipación es **recogerse** (cadera abajo y
  torso adelante), no echarse atrás; el contacto lleva 1–2 f intermedios o borrón, no un salto de 240 px.
- **Deslizamientos sin pasos** (control nuevo `medir_carrera.mjs … desliza`, confirmado en el video donde se midió):
  - **Tin, f632–f649 (P15): 1,93 u «patinando» de pie mientras dibuja el bastón.** En el video, la cabeza va de x 394 a
    221 a ≈ 11 px por fotograma con la pose quieta.
  - **Tin, f573–f584 (P14): 1,29 u tras el golpe 4 sin dar un paso.** En el video, de x 548 a 220.
  - Tan se desliza en guardia ≈ 0,8 u en f140–f155 (P5) y en f181–f194 (P6), y ≈ 1 u en f550–f569 (P12c).
  - El rival, ≈ 0,5 u en guardia en f812–f824 (P19).

  Corrección: todo cambio de lugar de 0,3 u o más lleva pasos (ciclo por distancia), o se hace fuera de cuadro y se
  corta. Los retrocesos de 0,2–0,3 u justo después de un golpe pueden quedarse (son el rebote del contacto).
- **Medidas no confiables:** donde Keter avisó (f562–f563, f650, f676, f682 de Tan, saltos de área), la mancha más
  grande no era la cabeza. La cabeza de Tan en P19 (f765–f805, área 20–43 mil px en y ≈ 1130) tampoco cuadra con el
  guion: no se usó.

Con esto se firma el diagnóstico de la sección 1 contra el video. El control 5 sigue en **NO PASA**, y el 3 (voz) sigue
sin firmar hasta que alguien oiga el audio.

**Veredicto: CAMBIOS.** La v3 se arma con la sección 2 de este documento más la opción «media» de fotografía y la
lista de continuidad. Costo: 0 créditos. No se generó ni se gastó nada.

Firmas: director de animación (diagnóstico y ciclo), director de fotografía (cámara en las carreras) y supervisor de
continuidad (control nuevo). Confirmado con el MP4 el 2026-11-26 (sección 4).
