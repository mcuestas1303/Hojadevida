# Revisión de animación — short 4, versión 2 (`tin_y_tan_short04_v2.mp4`)

- **Firma:** director de animación, 2026-11-26. Responde a `cambios/2026-11-26_short4_v2_animacion_en_el_espacio.md`.
- **Qué revisé:** las 9 hojas de contacto (`hoja_v2_00` a `08`, 1 de cada 6 fotogramas), `guiones/tin_en_s_004.js`,
  `guiones/tin_en_s_004.tiempos.json` (los K reales de la voz, que ya no son los de la dirección), las poses y el
  esqueleto de `escena.html`, la sección 4 de `direccion.md` y el estudio de referencias.
- **Límites de esta revisión (dichos de frente):** no pude reproducir el video ni sacar fotogramas sueltos (no tengo
  consola). Los contactos (K) caen casi siempre entre dos muestras de la hoja, así que los juzgo por la hoja más la
  aritmética de las claves del guion. Las distancias, zancadas y velocidades de este documento las calculé a mano desde
  `pos` y `pose` (margen ± 10 %). Donde algo se ve en la hoja pero no está probado en el código, lo marco «verificar».
- **Convenciones:** `f` = fotograma; `K*` = claves de `tiempos.json` (K1 = 82, K2 = 169, K3 = 314, KB = 548, K4 = 574,
  K5 = 612, KR = 694, K6 = 886); u = unidad del motor; un ciclo de carrera = `corre1` → `corre2` → `corre1` (2 pasos).

## 0. Veredicto en tres líneas

1. **La v2 no está al nivel profesional.** El dueño lo vio bien: los personajes «corren» sin avanzar, caminan de espaldas,
   patinan, se quedan clavados más de 3 s y, en el remate, parecen golpearse entre sí.
2. **No es un problema de detalle: es de método.** El guion pone movimiento donde la cámara no lo puede mostrar (en
   profundidad), pone el ciclo de carrera sin mirar la distancia y deja a Tin y Tan de estatuas mientras el rival hace todo.
3. **Se arregla con 0 créditos, en el guion y con 4 piezas nuevas del motor** (sección 3). Hay 10 defectos que bloquean
   la v3 (sección 1, B1 a B10) y una lista que puede esperar (sección 4).

## 0.1 La causa raíz (para quien programa)

| # | Causa | Qué provoca |
|---|---|---|
| C-A | **El mundo es 3D pero los personajes son láminas de frente a la cámara** (`Personaje.malla` es un plano que mira a +z; `mira` solo vale +1 o −1) y **todas las cámaras de `tiempos.json` miran por −z** (`camaraDe`: `cam.position.set(p.cx, p.h, p.z + D)`; no hay giro lateral). Lo que se mueve en z (profundidad) en esta cámara casi no se ve: solo cambia la escala unos % y los pies suben o bajan en pantalla | «Corre y casi no se mueve»; vuelos en profundidad que no se leen. La dirección prometía `C2` lateral, `C4` contrapicado y `C3` héroe «de espaldas»: **ninguno existe**, todos son frontales (P3, P6, P8, P14, P16 y P18 se llaman «lateral» pero no lo son) |
| C-B | **`corre()` pone una pose cada 4 f con `lin`, sin mirar la distancia**: ciclo fijo de 8 f (7,5 pasos/s) sea cual sea el recorrido | Zancada de 0,08 a 0,5 u cuando la pose pide ≈ 1,6 u: los pies resbalan 3 a 20 veces más rápido que el cuerpo |
| C-C | **`reloj` (LENTOS) solo frena la física** (`actualizar(v / FPS)` → polvo, cajas, partículas). `pos` y `pose` se evalúan en `S = cuadroN` | **No hay cámara lenta de personajes.** Las «carreras a 0,3» y los «vuelos a 0,25» de la dirección 4.5 no existen para Tin, Tan ni el rival |
| C-D | **Las poses se mantienen idénticas decenas de fotogramas** y el desplazamiento es una interpolación de `pos` (smoothstep por defecto) sin pasos ni derrape | Estatuas y patinaje |

## 1. Defectos por gravedad

Gravedad: **BLOQUEA** (no se presenta la v3 sin esto) · **ALTO** · **MEDIO** · **BAJO**. Dentro de cada nivel, de más a
menos grave. «Evidencia» dice dónde se ve (hoja) o dónde está la causa (guion).

### BLOQUEA

#### B1. Carreras que no avanzan, con el ciclo desacoplado de la distancia (lo que dijo el dueño)

- **Qué se ve:** piernas bombeando a 7,5 pasos/s mientras el cuerpo se mueve a 1 a 2 u/s. Tin en f375–425 y Tan en
  f359–386 son la peor muestra: en la hoja 03 (f360–f426) se ve el mismo pie de apoyo deslizándose hacia atrás.
- **Medida (todas las carreras del guion).** Zancada necesaria: **1,6 u por ciclo** para Tin y Tan (la pose `corre1` abre
  los pies 2,2 R = 0,79 u por paso; R = 0,36 u) y **2,3 u** para el rival a escala 1,15.

| # | f | Quién | Recorrido (eje) | Ciclos (8 f) | Zancada real | % de la necesaria | Observación |
|---|---|---|---|---|---|---|---|
| 1 | 46–66 | Tin | 0,84 u (casi todo z) | 1,7 | 0,49 | 31 % | en z: no se ve |
| 2 | 200–252 | Tin | 2,21 u (z +2,1) | 6,5 | 0,34 | 21 % | además aleja a Tin del rival y camina de espaldas (B2) |
| 3 | 284–296 | Tin | 3,38 u (x +1,55, z −3,0) | 2,1 | 1,6 | 100 % | **la única bien**; le faltan arranque y frenada |
| 4 | 375–425 | Tin | 1,48 u (x −1,45) | 6,5 | 0,23 | **14 %** | camina de espaldas (B2) |
| 5 | 632–656 | Tin | 2,73 u (x −1,3, z −2,4) | 2 poses de carrera (f649–656) | — | **0 %** | 17 f deslizándose en pose `dibuja`/`guardia` (B2, B3) |
| 6 | 671–682 | Tin y Tan | 1,1 u (solo z) | 1,1 | 1,0 | 63 % | «carrera lenta»: es en z y a velocidad normal |
| 7 | 770–800 | Tin | 0,33 u | 4 | 0,08 | **5 %** | corre en el sitio en pleno «respiro» |
| 8 | 909–915 | Tin | 0,8 u (z) | 1 | 0,8 | 50 % | en z |
| 9 | 359–386 | Tan | 0,45 u | 3,4 | 0,13 | **8 %** | corre en el sitio |
| 10 | 570–584 | Tan | 2,4 u (x) | 1,75 | 1,37 | 86 % | bien de zancada; cruza por detrás de Tin en pleno golpe 4 (A4) |
| 11 | 630–656 | Tan | 2,1 u (z 1,9) | 3,25 | 0,65 | 41 % | en z |
| 12 | 770–800 | Tan | 0,6 u | 4 | 0,15 | 9 % | corre en el sitio |
| 13 | 141–155 | Rival | 4,78 u (z 4,5) | 1,75 | 2,7 | 117 % | **correcta** (se ve porque crece al acercarse) |

- **Causa en el guion:** `const corre = (q, f0, f1, arma) => { for (let f = f0, i = 0; f < f1; f += 4, i++) pose(q, [f, … corre1/corre2, 'lin']); }`.
- **Corrección (por quien programa el motor):**
  1. Sustituir `corre` por `correDe(q, f0, x0, x1, z, mira, arma)`: `n = round(|x1 − x0| / 1,6)` ciclos (rival: 2,3);
     `f1 = f0 + 12·n`; la `pos` entre `f0 + 3` y `f1 − 3` es **`lin`** y constante (0,133 u/f); 4 poses por ciclo, una cada
     3 f (contacto, abajo, paso, arriba; sección 3, regla M1). Prohibido tocar `pos` en esos fotogramas con otra curva.
  2. Aplicar por carrera:
     - **#1 (Tin f46–66):** borrar las tres poses `corre`; Tin en z = −1,6 desde f30; **2 pasos de guardia de 0,13 u**
       (f52–f64) para pasar de x = 1,5 a 1,25. No es una carrera.
     - **#2 (Tin f200–252):** **borrar** `corre('tin', K2+31, K.cartel-5)` y las claves `pos` [K2+30] → [K.cartel-4].
       Tin se queda en (1,0; 0; −1,8) con reposo vivo (B5). El rival acaba su resbalón en z = −1,8 (hoy +0,15) y los
       `postes_de_fila` y el `cartel_de_pie` pasan a z = −1,8 ± 0,3 (hoy +0,3 y −0,5). Tin queda a 1,3 u del rival: ya
       está al alcance (brazo del rival 0,83 u + brazo de Tin 0,54 u) y la esquiva de f261–269 por fin tiene causa (A3).
     - **#3 (Tin f284–296):** conservar. Añadir arranque en f281–283 (torso 25°, cadera 0,1 u más baja) y frenada en
       f297–300 (pose `frena`: torso −8°, pie delantero extendido, polvo de 3 f).
     - **#4 (Tin f375–425):** Tin se queda en x = 2,0 con reposo vivo hasta f396; `mira = −1` en f396 con giro de 3 f
       (B9); **1 ciclo** de f398 a f410 (Δx = −1,6, de 2,0 a 0,4, z constante); frenada f410–413 con derrape de 0,15 u; `mira = +1`
       en f413 (giro de 3 f); reposo vivo hasta f426 (`dibuja`).
     - **#5, #6, #11 (remate):** rehacer según B4.
     - **#7 y #12 (f770–800):** **borrar** las dos carreras. Tin y Tan se quedan en (−1,1; −5,1) y (1,5; −4,9) con reposo
       vivo y cara de asombro (es el «respiro» de la dirección 4.4: «Boca abierta y quieta f703–f745»).
     - **#8 (f909–915):** borrar; el plano de portada (f956) lo hace la capa 2D. Tin queda quieto, con reposo vivo.
     - **#9 (Tan f359–386):** borrar. Tan en reposo vivo y, en f376–386, `festeja` corto sin desplazarse.
     - **#10 (Tan f570–584):** mover a **f584–f602** (1,5 ciclos = 18 f, Δx = 2,4), después de que Tin termine el golpe 4
       (K4 + 10), para que llegue a recibir el mazo en f598–603 sin cruzarse con él.
  3. **Contralateral:** en `P.corre1` el brazo delantero va con la pierna delantera (`aF [70,120]` con `lF [55,10]`; en
     `corre2`, `aF [−60,−10]` con `lF [−40,−95]`): es marcha de camello (ipsilateral). Cambiar los brazos:
     `corre1.aF = [−60,−10]`, `corre1.aB = [70,120]`; `corre2.aF = [70,120]`, `corre2.aB = [−60,−10]`.
  4. **Cadencia:** 12 f por ciclo (5 pasos/s). 8 f por ciclo solo en dos casos («sprint», zancada 2,2 u, máx. 14 f).

#### B2. Marcha atrás: la dirección de la mirada no coincide con el sentido del movimiento

- **Evidencia:** `G.tin.mira` = [[0,−1],[K2+20 = 189, +1], …] deja a Tin mirando a +x desde f189 hasta el final del cuerpo
  a cuerpo. Se mueve hacia −x con `mira = +1` en: f200–252 (−0,7 u y hacia cámara), **f375–425 (−1,45 u)** y **f632–656
  (−1,3 u en x)**. En la hoja 03 (f390–f426) la visera de Tin apunta al rival mientras Tin se aleja a toda leva.
- **Corrección:** regla M3 (la mirada es el signo de la velocidad en x, salvo «retroceso» con pasos cortos de 0,4 u).
  Casos concretos: f375–425 → B1 #4; f632–656 → B4. Comprobar por programa: para todo fotograma con |vx| > 0,03 u/f,
  `sign(vx) == mira`, o la pose es `retrocede`.

#### B3. Patinaje: desplazamientos con la pose congelada

- **Evidencia (guion):**

| f | Quién | Qué | Recorrido | Pose durante el recorrido |
|---|---|---|---|---|
| 46–69 | Tan | retrocede | 0,45 u | `recibe`/`guardia` |
| 139–156 | Tan | se acerca | 0,8 u (de −1,95 a −1,45; z −0,4 a −1,0) | `guardia` |
| 180–195 | Tan | `festeja` y se desliza | 0,8 u | `festeja` |
| 304–344 | Tan | | 0,63 u | `guardia`/`festeja` |
| K1+0 a K1+11 | Tin | vuelve a la guardia | −0,28 u | `golpe` → `guardia` |
| K4+0 a K4+11 | Tin | vuelve a la guardia | −0,25 u | idem |
| K6+0 a K6+11 | Tin | vuelve a la guardia | −0,25 u | idem |
| 632–648 | Tin | | 1,3 u en x y 2,4 en z | `dibuja`, luego `guardia` |

- **Corrección:** regla M2 (pies anclados): cualquier desplazamiento de más de 0,15 u necesita pasos. Un paso de
  guardia = 0,14 u y 4 a 6 f, con dos poses nuevas: `pasoA` = `{t:12, aF:[55,150], aB:[25,140], lF:[34,12], lB:[−20,−6], c:0}` y
  `pasoB` = `{t:12, aF:[55,150], aB:[25,140], lF:[14,0], lB:[−30,−14], c:0}`. Para volver a la guardia después del golpe
  (K1, K4, K6): **dos pasos** (`pasoA` en K+6, `pasoB` en K+10) en vez de deslizarse 11 f. Tan f139–156 y f180–195: los
  0,8 u se hacen con 6 pasos de guardia o se quita el desplazamiento (preferible: Tan en x = −1,45 desde f139).

#### B4. El remate se lee como si Tin y Tan se golpearan entre sí

- **Evidencia (hoja 05, f690–f714; guion):** en f696 las cabezas de Tin y Tan casi se tocan, las dos estrellas caen entre
  ellas, y el bastón y el mazo se cruzan en X delante de sus caras. Causa: `G.tin.mira` = +1 y `G.tan.mira` = −1 desde
  K5+16 (f628), con Tin en x = −0,95 y Tan en x = +0,75 en KR, y el rival (−0,12; z −6,4) **detrás**, 0,4 u más lejos.
  Es un sándwich lateral con el rival en el fondo, y de perfil el fondo no se ve. Rompe la regla 3 de la dirección 2.1 («nunca
  entre sí») **a los ojos del público**, aunque el código apunte al rival.
  Además: f717–f719 en `agachado` fijo 23 f (f719–f742), sin que la onda les haga nada; P18 «héroe de espaldas» es
  imposible con láminas de perfil (en la hoja 06, f720–f727, se ven de perfil y de frente el uno al otro).
- **Corrección (f632–f742):**
  1. **Los dos del mismo lado, mirando al rival:** `mira = −1` para ambos desde f640 (Tin gira con 3 f en f637–f640);
     posiciones en KR − 1: **Tin (1,0; 0; −2,6)**, **Tan (1,9; 0; −2,6)** con salto de 0,5 u y `mazoArriba` → `mazoAbajo`
     (apilados en altura: Tan golpea alto y Tin bajo, así que el pico se ve «doble» sin que se tapen); rival en (−0,1; 0; −2,6).
     La punta de `arma` (`armaMundo`) de cada uno debe quedar a ≤ 0,15 u del torso del rival en K.
  2. **Todo el remate en el mismo plano z = −2,6** (el del P15), no en z = −6 (P16): así el rival se ve volar «hacia el
     televisor» como un vuelo en altura (de y 0 a 2,3) y no como un achicamiento en profundidad. El televisor y la isla se
     ven al fondo, sin cambiar. Quien hace cámara (fotografía) fija P16 en z = −2,6 y `D` = 10,2.
  3. **Carrera previa:** en P15 (f632–f658) Tin y Tan corren hacia −x y salen del cuadro por la izquierda (2 ciclos = 24 f,
     Tin de x = 0,1 a −3,3; Tan de 1,9 a −1,3). En el corte a P16 (f671) **entran por el borde derecho ya corriendo hacia −x**
     (corte en el movimiento, respeta el sentido): Tin en x = +2,6 y Tan en +3,5, **1 ciclo** de f671 a f683 (1,6 u cada uno) hasta x = +1,0 y
     +1,9; el final del ciclo es la anticipación (K − 12 a K − 7 = f682–f687) y la pausa va en f688–f693. **No hay «carrera
     a cámara lenta» mientras no se resuelva B6**; no se simula con zancadas cortas.
  4. **Reacción a la onda:** en f719 (`radiales`) Tin y Tan pasan de `agachado` a `recibe` con empuje de 0,35 u hacia
     +x (el lado contrario al estallido: están a la derecha, el televisor al centro) con 4 pasos de retroceso o un
     derrape de 0,3 u con polvo; cara `sorpresa`. Quitar la `pos` [K.radiales: (1,15; −5,4) `salto`] de Tan.
  5. P18: o se hace con vista de frente (sprites `frente_tin` y `frente_tan` nuevos, 2 láminas) o se cambia por un
     contrapicado de perfil (`h` = 0,7, `sube` = 3,1, que es lo que ya hay) **sin llamarlo «de espaldas»**. Pasa a fotografía.

#### B5. Estatuas: Tin y Tan quedan clavados decenas de fotogramas

- **Evidencia (guion + hojas):**

| Quién | f | Frames | Qué queda quieto |
|---|---|---|---|
| Tin | 93–199 | **106** | `guardia` idéntica (hojas 01: f114–f192, siete celdas iguales) |
| Tan | 197–328 | **131** | `guardia` idéntica (hojas 01–02) |
| Tin | 444–545 | 101 | `Gd` / `bloqueo` (hoja 03–04) |
| Tan | 386–451 | 65 | `guardia` |
| Tin y Tan | 483–548 | 65 | Tan en `invita` con la boca abierta fija (cara `risa`), Tin en `Gd`, rival quieto en el mostrador (hoja 04: f486–f510, cinco celdas idénticas) |
| Tin y Tan | 822–875 | 53 | Tan con el mazo plantado; Tin con el bastón (hoja 07) |
| Tin y Tan | 918–942 | 25 | de pie, sin respirar |

  Total (sin contar dos veces lo que se cruza): **Tin ≈ 290 f quieto (≈ 9,6 s) y Tan ≈ 340 f (≈ 11,3 s) de 32,9 s**. La
  acción la hace casi siempre el rival.
- **Corrección (regla M3c, reposo vivo):** ninguna pose se mantiene idéntica más de 12 f. En cada espera:
  1. Alternar dos poses de reposo cada 18 a 24 f (desfasadas entre Tin y Tan por 9 f): `guardia` y
     `guardiaB` = `{t:10, aF:[50,146], aB:[30,136], lF:[26,4], lB:[−24,−6], c:3}`; entre ambas, cambio de apoyo: `lF`/`lB` ± 4° y
     cadera ± 0,03 u.
  2. «Respiración»: `t` ± 2° y brazos ± 3° con ciclo de 36 f (curva `io`).
  3. Cabeza: `c` ± 3° siguiendo lo que pasa (al rival cuando se mueve).
  4. Reacciones obligatorias (ver A1). En la pausa de cada golpe (K−6 a K−1) un «hervor» de ± 2° cada 2 f en el que
     golpea, para que se lea como carga y no como fotograma congelado.
  5. En la espera de la invitación de Tan (f483–548): sacar la cara `risa` de boca abierta fija (los personajes no tienen
     boca animada) y poner `concentrado`/`curiosidad`, con `invita` y brazo moviéndose en 2 gestos (f485, f512).

#### B6. No hay cámara lenta de personajes (la «desaceleración en el aire» no existe)

- **Evidencia:** `LENTOS` y `reloj` solo llegan a `pasoTrozos`/`pasoParticulas`; `S = cuadroN` (`escena.html`, `window.cuadro`).
  Se ven las cajas y el polvo en lento, pero el rival vuela a la velocidad de la clave (12 f con `out`) y Tin y Tan corren a
  1,0 aun en «f671–f682 a 0,3».
- **Corrección:** en `escena.html`, acumular `Sa += reloj(S)` y evaluar `pista(g.pos/pose/escala, Sa)` (no `S`); los tramos
  `LENTOS` (vuelos K1+6..K1+17, K3+6..K3+17, KR+6..KR+20 a 0,25 a 0,35) se reescriben con la duración en tiempo de
  animación (por ejemplo, un vuelo de 6 f de animación a 0,3 = 20 f de pantalla). Si no se hace, **se borra la promesa**
  de la dirección 4.5 y se dice que la desaceleración es de easing. Elegir antes de la v3.

#### B7. Contactos que no se leen y sin peso (los 8 golpes)

- **Evidencia (hojas):**
  - **K1 (f82–f84):** la estrella cae sobre la cara de Tin (hoja 00, f84: estrella amarilla encima de la visera) y el puño no se ve.
    El rival sale en K+1 sin quedarse un instante: `pos` [K1 `salto`] → [K1+5 `out`] ya lo mueve 0,3 u en K1+1.
  - **K4 (f576):** la estrella queda entre las cabezas de Tin y Tan (Tan cruza por detrás de Tin, B1 #10); el rival no se ve.
  - **KR (f696):** B4.
  - **K2, K3, KB, K5, K6:** hay estrella y el rival reacciona, pero **ninguno tiene borrón del que golpea** (porque
    `p.dibujar(…, GU.porFotogramas ? false : rapidez > 7, …)` apaga el `borron`) y la pose pasa de `carga` a `golpe`
    **en 1 f sin dibujo intermedio**: el puño aparece en su sitio (pop), no golpea.
  - **Sin parada de impacto:** el golpeado ya se mueve en K+1 (K1, K2, K3, K4, K6). La gramática de 4.1 pide contacto de
    2 f y lanzamiento desde K+2.
  - **Sin peso:** el que golpea hace un salto de `pos` de 0,2 a 0,35 u en 1 f y vuelve **deslizándose** 11 f (B3). No hay
    pasada de más (overshoot), ni estiramiento, ni cabeza que se retrasa, ni aplastamiento al aterrizar.
- **Corrección (para K1, K2, K3, KB, K4, K5, KR y K6, con los nombres del guion):**
  1. **Smear en K:** añadir una clave `pose` en K con `golpe` y `borron` activo en K y K+1 (reactivar el parámetro
     `borron` aunque `porFotogramas` sea verdadero), y una clave `pos` en el medio (50 % del salto) en K − 1 + 0,5, es decir,
     **dos fotogramas de dibujo**: K con el brazo estirado 1,35 veces (`extra.estira = 0,35`, igual que `aplasta` pero
     al revés) y K+1 con la pose `golpe` normal.
  2. **Hit-stop:** en el rival, una clave `pos` en K+1 **igual** a la de K (hoy el `out` ya avanza). El lanzamiento empieza
     en K+2 y las `pos` de vuelo se mueven a K+2 / K+14.
  3. **Peso:** overshoot: clave `pos` en K+3 a 125 % del salto (0,33 → 0,41 u), `t` del torso 30° → 38° en K+3 y
     vuelta con `EASE.back` en K+4 a K+9; `aplasta` = −0,15 en K y +0,10 en K+3 (aterrizar).
  4. **Estrella en el punto de contacto, no en coordenadas fijas:** `estrella(manoMundo + dir·0,15)` (la mano o la punta
     del arma ya existen: `tin.manoMundo`, `tin.pieMundo`, `armaMundo`), nunca sobre la cara del que golpea.
  5. **Comprobación automática en K:** distancia de `manoMundo`/`pieMundo`/`armaMundo` al torso del rival ≤ 0,15 u; si no,
     el fotograma falla.
  6. **Anticipación contraria** (K − 13 a K − 7): hoy el cuerpo avanza hacia el rival mientras carga (Tin 1,25 → 1,05 en f69–75).
     Pasar a un retroceso de 0,12 u en K − 10 (peso hacia atrás) y arrancar de ahí.

#### B8. Tin salta fuera del tiempo: dos errores de claves

- **K3 (f313–f314):** `[K3−1, (1,85; 0; −2,9)]` → `[K3, (2,05; 0,45; −2,9), 'salto']`: Tin se levanta 0,45 u y avanza 0,2 u en
  **1 f**, con las piernas en `agachado` → `gancho` (`lF [30,0]`): sin extensión de piernas, flota. **Corrección:** clave
  `pose` en K − 1 con `agachado`, K con `gancho` y piernas extendidas (`lF [8,0]`, `lB [−6,−4]`, `t` 16), subida de
  `y` de 0 a 0,45 en K − 1 a K + 2 con `out` y caída de 6 f con `in` desde K + 4 (hoy cae en K + 6, flota ≈ 5 f).
- **f584 → f585 (error de orden de claves):** `pos('tin', … [K4 + 11, (0,7; 0; −2,6)], [K.mazo − 2, (0,1; 0; −2,2)] …)` con
  K4 + 11 = 585 y K.mazo − 2 = 584. Ordenadas, Tin va de 0,95 a 0,1 entre f574 y f584 (patina 0,85 u), **salta 0,6 u en 1 f
  (584 → 585)** y vuelve a 0,1 patinando 47 f. **Corrección:** borrar `[K.mazo − 2, …]` o ponerlo en K4 + 12; Tin recupera
  a (0,7; −2,6) con 2 pasos y se queda ahí hasta f632. *(Verificar en f582–f588; en la hoja 04 se ve a Tin desplazarse unos
  20 px entre f582 y f588.)*

#### B9. Giros instantáneos de `mira` a mitad de carrera o de golpe

- **Evidencia:** `escalon(g.mira, S)` voltea la lámina en 1 f: Tin f189 (K2 + 20), Tan f628 (K5 + 16, a mitad de carrera), Tin y Tan en f637–f640.
- **Corrección (regla M3):** giro de 3 f con la lámina aplastada en x: escala x 1,0 → 0,35 → 1,0 con la mitad del giro
  en el fotograma central (a 0,35 de ancho); solo con el personaje quieto o frenando. Nunca en mitad de ciclo de carrera.

#### B10. Piezas del decorado que tapan la acción (afectan la lectura del contacto)

- **Evidencia:** en f306–f318 y f342–f372 el trozo blanco del `cartel_de_pie` (x 2,75; z −0,5) y el `mostrador` tapan las piernas
  de Tin en el gancho y en la celebración (hoja 02: f306, f312; hoja 03: f360–f372, bloque blanco a la derecha). *(Verificar en el render.)*
- **Corrección (animación + decorado):** con el cambio de B1 #2 (`cartel_de_pie` a z = −1,8 ± 0,3 y a x ≥ 3,6 después de partirse,
  con la mitad de abajo cayendo hacia **−z**, no hacia cámara) y Tin en z = −2,2 en f302–f372 (el frente del `mostrador` está
  en z ≈ −3,0), no se tapa nada.

### ALTO

#### A1. El rival no reacciona y los héroes tampoco reaccionan al rival

- **Evidencia:** el rival en el mostrador (f337–f548) se queda en `recogido`/`agachado` 211 f cambiando solo cuando hace
  algo él; Tin y Tan no se giran cuando el rival se tira al mostrador (f281–f295), ni cuando dibuja la espada (f514–f525),
  ni cuando ataca (f548); durante la invitación de Tan (f483–f548) el rival ni se asoma.
- **Corrección (guion):**
  - **Rival:** en f337–f358 (caído en el mostrador) 2 sacudidas de 4 f (`escala` 1,02 y 0,98, `giro` ± 0,08); en f360–f513
    mirar a Tin (`D.mira` a −1) y, cada 36 f, un gesto: `pisoton` (f390), `recogido` con el rizo agitándose (f444), asomarse
    en f486–f490 (el rizo de pregunta crece 10 % durante 6 f cuando Tan habla: `escala` 1,10 → 1,0).
  - **Héroes:** cara `sorpresa` 8 f en K+2 de cada golpe **del otro** (Tan en K1, K3, K4; Tin en K2, K5); cara `concentrado`
    + pose `guardia` en la anticipación del rival (`rival_ataca − 6`, `dibuja_espada`, `KB − 13`); cabeza hacia el rival
    (`c` ± 8°) mientras vuela (hoy el testigo mira al frente).

#### A2. Poses rígidas: sin curvas, sin arcos, sin acción secundaria

- **Evidencia:** las poses interpolan ángulos con `io` (suavizado simétrico) entre claves; no hay arco en la trayectoria del
  brazo (línea recta de `carga` a `golpe`), no hay arrastre de cabeza (`c` se mueve con `t * 0,6` igual que el torso) y la
  **bufanda de Tan con muelle**, que prometía la dirección (4.4, «Acción secundaria»), no existe (la bufanda va pintada en la
  lámina de la cabeza: en todas las hojas se ve inmóvil).
- **Corrección:** (a) en cada golpe, una clave intermedia en K − 0,5 con el codo a 40° del arco (`aF [20, 60]` en la pose de
  paso) para que el puño dibuje un arco; (b) el ángulo de cabeza `c` sigue al torso con 2 f de retraso (muelle: `c(f) +=
  (t·0,6 − c)·0,35`); (c) bufanda: 2 segmentos de muelle (k 180, amortiguación 14, masa 1) detrás de la cabeza de Tan, o se
  borra la promesa de la dirección 4.4. Rigidez y amortiguación a validar con la regla 11 del manual 11.

#### A3. «Esquiva» de Tin que no esquiva nada (f257–f275)

- **Evidencia:** Tin en x = 0,3, el rival en x = 2,3, brazo de 0,83 u: 1,2 u de aire. Tin se agacha (`K.rival_ataca − 2`) para evitar
  un golpe que no lo alcanza (hoja 02, f264–f270).
- **Corrección:** resuelta con B1 #2 (Tin en x = 1,0 y el rival en x = 2,3 → 1,3 u: al alcance). Si se prefiere que
  falle, la pose `agachado` empieza en `rival_ataca + 1` (cuando el brazo ya viene), no 4 f antes.

#### A4. Cabezas y cuerpos que se montan unos sobre otros

- **Evidencia (hojas):** f54 (rival sobre la cabeza de Tin), f564–f582 (Tan y Tin con las cabezas montadas; Tan cruza a Tin),
  f600–f606 (Tan delante del rival y del mazo, Tin pegado), f684–f714 (Tin, rival y Tan en 1 u de ancho).
- **Corrección:** regla M7: separación mínima en pantalla entre cabezas de personajes distintos ≥ 0,7 u (o 1,0 u si hay
  contacto de armas) salvo en K ± 3. Comprobación automática: caja de cada cabeza (`cabezaMundo` ± R) sin solaparse más del 20 %.

#### A5. El «respiro» (f750–874) no respira

- **Evidencia:** la dirección lo define como «plano fijo, casi nada se mueve»; en la hoja 06 (f780–f816) Tin y Tan corren en
  el sitio con las armas; en f792–f870 anillos de humo oscuro tapan la cara de Tin (hoja 06 f792–f798; hoja 07 f822–f858),
  justo cuando debe verse su asombro.
- **Corrección:** B1 #7 y #12 (se borran las carreras). El humo que pasa delante de las cabezas de los héroes
  (`soltar('humoC')` con `z` > −4,6 en f730–f870) se mueve a z ≤ −7 o se elimina; lo ve fotografía, pero es una condición
  de la actuación («nunca humo delante de la cara», dirección 3b).

#### A6. Salto del rival al mostrador (f281–f295): trayectoria plana y en profundidad

- **Evidencia:** `pos('duda', [K.salto_mostrador, (2,3; 0; 0,15)], [+7, (2,4; 1,3; −1,8), 'out'], [+14, (2,85; 1,0; −3,4), 'in'])`: pico de
  1,3 u cuando el mostrador está a 1,0 u: solo 0,3 u por encima de donde aterriza; 3,6 u en z, no en x. En pantalla es un
  achicamiento con un salto de 0,3 u.
- **Corrección:** con el rival ya en z = −2,2 (B1 #2) y el mostrador en z = −2,6: `[281, (2,3; 0; −2,2)]`, `[284, (2,3; 0; −2,2)]` (agacha 3 f),
  `[288, (2,6; 1,9; −2,4), 'out']`, `[295, (2,85; 1,0; −2,6), 'in']`; poses `agachado` (f278–f283), `recogido` en f288 (pico),
  `agachado` en f295 con `aplasta` 0,2 durante 3 f al aterrizar.

### MEDIO

- **M-1. Lápiz de Tin atravesando la cara en `festeja`** (hoja 02 f354; hoja 03 f360, f366): el lápiz va en la mano `aB`, que
  en `festeja` sube a la cabeza. **Corrección:** `extra.lapiz = false` mientras `aB[0]` > 100° y mostrarlo en la mano
  `aF`/en la faja; o usar `festeja1` con los brazos a 120°.
- **M-2. Entrada del rival «se dibuja de un trazo» (f30–f45):** es un barrido de abajo hacia arriba (`revela`), no un trazo. Lo
  mismo en f780–f800 (`revela`). **Corrección:** dibujar el contorno con `trazoSuelo`-like en 16 f (cabeza → piernas) o decirlo
  en la dirección como «barrido».
- **M-3. Disco claro (`extra.papel`) visible alrededor de la cabeza del rival** sobre el televisor y el marco oscuro, f666–f696
  (hoja 05, f672, f684, f690). **Corrección:** el disco usa el color de lo que hay detrás (muestrear el fondo del televisor), o
  mover al rival a z más alejada del televisor.
- **M-4. P11 «macro de la punta del lápiz» (f430–f442)** muestra la cara de Tin ampliada, 4× la lámina de la cabeza (256 px), no la
  punta. **Corrección:** `D` = 5,6 → 3,2 y `cx` hacia la mano; la punta ≥ 40 px de largo; la mano en `dibuja` a escala 1,0.
- **M-5. El asterisco final (f918–f942) mide ≈ 16 px en la hoja (≈ 64 px reales), tapado por la pose de Tin.** Es el chiste de la
  respuesta. Fotografía debe agrandarlo (≥ 120 px) o acercar el plano; animación: Tin sale del cuadro de la marca (x ≥ −0,6).
- **M-6. Polvo y humo como discos blancos con contorno** (hojas 00, 02, 05) se leen como bolas de nieve y tapan caras
  (f102–f108 sobre Tan, f342–f354 sobre Tin). Pasa a fotografía/efectos con la condición de no tapar cabezas.
- **M-7. Cuadros invertidos con máscara (f717–f718)** se ven como un disco turbio azul-gris, no como cuadro invertido nítido.
  Pasa a fotografía.
- **M-8. Caras que no siguen la dirección:** Tan abre en f0 con `sorpresa` (la dirección dice `curiosidad`).
- **M-9. No hay cámaras laterales** (C2 y C4 de la dirección; P3, P6, P8, P14 y P16 «laterales» son frontales). **Corrección:**
  o se declara que el formato de acción es de **plano frontal** (y se corrigen las frases de cámara de la dirección), o el motor
  gira las láminas con el eje de la cámara (`malla.rotation.y = yaw`) y `camaraDe` acepta `yaw`. Decisión de fotografía con
  producción; **animación recomienda el plano frontal** hasta que haya láminas de frente/espalda.

### BAJO

- **L-1.** La pausa del golpe 1 llega en f76–f81 sin desplazamiento de hombros: añadir un parpadeo de cara (`concentrado` → `eureka`).
- **L-2.** Los calcos del rival solo en `LANZA`; el que golpea no deja calcos (la gramática de 4.1 lo pide solo para el golpeado: OK).
- **L-3.** `Tan` en f102–f126 queda recortada por el borde izquierdo en P6 (hoja 01, f162–f174): lo ve fotografía.
- **L-4.** `Tin` con la cabeza recortada por el borde en f948–f954 (hoja 08).

## 2. Qué está bien (se conserva)

- La **firma** (f0–f29 y f956–f985) tiene la geometría y los tiempos de la ficha; el empalme de pose y de lápiz casa.
- **La pausa antes del golpe** (`ataque()` con claves K−7 a K−1 quietas) y **los K sincronizados con la voz** (K + 2): es lo que pidió Keter.
- **Cortes de impacto** (f100–f101, f336–f337, f562–f563): se leen y no hay temblor.
- **El fuego plano por fases**, el humo con contorno y el **daño que se queda** (la tienda al final está rota de verdad).
- **El marcador de avance del rival** (baja un escalón de tamaño por dato) y la implosión con el asterisco.
- Los **vuelos del rival** de K1, K3 y K4 (`out` con arco de y y calcos) se leen bien; los de z largo (K1) pierden menos
  que los del resto porque llevan x e y.

## 3. Reglas nuevas para el motor (para que no vuelva a pasar)

> Para `motor_de_accion/README` y `REGLAS_CEREBRO.md`; el que programa el motor las convierte en comprobaciones automáticas
> (`comprobar_locomocion` y `comprobar_contactos`, que leen `G` del guion y fallan el render).

**Espacio**
- **M0. Plano de acción.** La acción (carreras, golpes, saltos) ocurre sobre x e y. En cada plano de cámara, los tres actores
  comparten z ± 0,3 u con la `z` de la cámara. Se mueve en z solo en entradas y salidas, o con cambio de escala ≥ 25 % y
  cambio de `y` en pantalla; **ninguna carrera con más del 25 % de su recorrido en z**.
- **M0b. Cámara y láminas.** Mientras `camaraDe` mire siempre por −z, no se llaman «laterales» las cámaras ni se promete
  «de espaldas»; si se quiere lateral, el motor gira las láminas con la cámara (`yaw`) o hay láminas de frente y de espalda.

**Locomoción**
- **M1. Zancada fija por ciclo.** Tin y Tan: **1,6 u por ciclo de 12 f** (0,133 u/f; paso de 6 f). Rival: 2,3 u (escala 1,15;
  se calcula como `2 × 2,7 R × 0,36 × escala`). Sprint: 2,2 u en 8 f, máx. 14 f. Ciclos = `round(Δx / zancada)`; la duración
  sale del número de ciclos, no al revés. Ciclo de **4 poses** (contacto, abajo, paso, arriba), brazos **contralaterales**.
- **M2. Pies anclados.** Cada fotograma de carrera: `pos.x` = ancla del pie de apoyo − desfase del pie en la pose; el ancla
  cambia al cambiar de pie. Tolerancia de resbalón: **≤ 5 %** de la velocidad del cuerpo. Todo desplazamiento > 0,15 u con
  pose no cíclica se hace con pasos (`pasoA`/`pasoB`, 0,14 u por paso) o no se hace.
- **M3. Mirada = sentido.** `mira == sign(vx)` cuando |vx| > 0,03 u/f; retroceder = `retrocede` (pasos de 0,4 u y 6 f, como
  máximo 2 pasos). Giro de **3 f** con la lámina aplastada (x 1,0 → 0,35 → 1,0) y solo con el personaje quieto o frenando.
- **M3b. Arranque y frenada.** Arranque: 3 f de anticipación (torso 25°, cadera −0,1 u, brazo atrás) y 3 f de aceleración con `in`.
  Frenada: 3 f con pose `frena` (torso −8°, pie delantero extendido) y 3 f de polvo con contorno (0,15 a 0,3 u de derrape).
  **Nunca de correr a quieto en 1 f.**
- **M3c. Reposo vivo.** Ninguna pose se repite idéntica más de 12 f (alternar 2 poses de reposo cada 18–24 f, respiración
  ± 2°, cambio de apoyo, cabeza que sigue); en pausas de golpe, hervor ± 2° cada 2 f.

**Golpes**
- **M4. Un golpe = 6 elementos:** (1) anticipación contraria de 0,12 u a K − 10; (2) pausa de 6 f con hervor; (3) contacto de
  2 f con **borrón del que golpea** y brazo elongado 1,35 veces; (4) **hit-stop** de 2 f en el golpeado; (5) lanzamiento desde
  K + 2; (6) peso: overshoot de 125 %, aplastamiento −0,15 / +0,10, recuperación con **pasos** y no deslizando.
- **M5. Contacto medible.** `manoMundo`/`pieMundo`/`armaMundo` a ≤ 0,15 u del torso del golpeado en K; la estrella nace en el
  punto de contacto (nunca sobre la cara del que golpea); el golpeado y el testigo reaccionan en K y K + 2 (cara y pose).
- **M6. Tiempo de animación.** `Sa = Σ reloj`; `pos`, `pose` y `escala` se evalúan en `Sa`. Sin esto, no se promete cámara lenta
  de personajes.
- **M7. Despeje.** Cabezas de personajes distintos separadas ≥ 0,7 u en pantalla (≥ 1,0 u si hay armas) salvo en K ± 3; el
  polvo y el humo no pasan delante de una cabeza de héroe.
- **M8. Orden de claves.** El guion no puede tener claves `pos` ni `pose` desordenadas: el motor falla si `sort` cambia el
  orden original (caso `K.mazo − 2` frente a `K4 + 11`).
- **M9. Diseño de remates.** Un golpe «doble» es de dos personajes **del mismo lado** (o apilados en altura), nunca enfrentados.

**Comprobaciones antes de presentar**
1. `comprobar_locomocion`: por carrera, zancada real ≥ 90 % de la de M1, mira = sentido, resbalón ≤ 5 %.
2. `comprobar_contactos`: distancia en K (M5) y hit-stop (M4).
3. Hoja de contacto **1 de cada 3 f** en los tramos de golpe y carrera (la de 1 de cada 6 se come los contactos).
4. Revisión de animación firmada **antes** de presentar al dueño (regla 4 de la solicitud).

## 4. Veredicto

### Bloquea la v3 (sin esto no se presenta)

| # | Qué | Quién lo hace | Esfuerzo |
|---|---|---|---|
| B1 | Carreras: `correDe`, 13 casos de la tabla, brazos contralaterales, ciclo de 12 f | guion + motor | medio |
| B2 | Marcha atrás (f375–425, f632–656, f200–252) | guion | bajo |
| B3 | Patinaje: pasos de guardia y recuperación con pasos | guion + 2 poses nuevas | bajo |
| B4 | Remate: mismo lado, mismo plano z, reacción a la onda, carrera de entrada | guion + fotografía (P16) | medio |
| B5 | Estatuas: reposo vivo, 580 f, y la boca fija de Tan en f483–548 | guion + 1 pose nueva | medio |
| B6 | Cámara lenta real (`Sa`) **o** borrar la promesa | motor (o dirección) | medio |
| B7 | Contactos: smear, hit-stop, peso, estrella en el punto, anticipación | guion + motor (`borron`, `estira`) | medio |
| B8 | Gancho sin piernas y la clave desordenada f584–585 | guion | bajo |
| B9 | Giro de `mira` en 3 f | motor | bajo |
| B10 | Decorado que tapa el contacto (cartel, mostrador) | guion + decorado | bajo |

**Orden de trabajo:** B8 y B2 (una tarde, arreglan lo más feo) → B1 con `correDe` y B9 → B3 y B5 → B7 → B4 → B6.
**Criterios para que firme animación la v3:** las 13 carreras ≥ 90 % de zancada y 0 marchas atrás; 0 estatuas de más de
12 f; cada K con smear, hit-stop y distancia ≤ 0,15 u; 0 cabezas montadas en un golpe; remate sin enfrentarse; B6 resuelto
en un sentido o en el otro; hoja de contacto a 1 de cada 3 f en los tramos corregidos.

### Puede esperar (v3.1 o el siguiente video)

- M-2 (entrada «de un trazo» real), M-3 (disco claro), M-4 (macro del lápiz), M-5 (tamaño del asterisco), M-6 y M-7 (efectos).
- A2 (arcos, muelle de la cabeza y de la bufanda): **lo mínimo en la v3** (los arcos de K) y el resto después.
- M-8 y las bajas (L-1 a L-4).
- Cámaras laterales verdaderas (M-9): decisión de formato, no de este video.

### Fuera de mi oficio, pero bloquea y lo dejo señalado

- **La invitación «Subscribe. We check the facts.» está dicha a mitad del video (f483–f548, `lineas` «C» en
  `tin_en_s_004.tiempos.json` y `05_audio/linea_de_tiempo.md`) y no al final (f878–f928, `direccion.md`: sección 2 y 2.2).** Por eso
  hay 65 f de Tan en primer plano con el rival congelado y el cierre no lleva llamado. Sonido y edición deben decidir si se
  reordena la voz (se recupera el tiempo de acción y se cumple la dirección) o se corrige la dirección. La animación de
  f483–f548 depende de eso (B5).
- **Revisar la dirección 4.5** (mapa de velocidad): hoy promete cámara lenta de personajes que el motor no hace.

### Notas para la memoria del equipo (no las guardo yo)

- Regla del dueño sobre calidad profesional: «hablamos de producir algo de alta calidad» (2026-11-26, vista de la v2).
- Ninguna pieza se presenta sin las firmas de los oficios (solicitud del 2026-11-26): ya está en `cambios/`.
