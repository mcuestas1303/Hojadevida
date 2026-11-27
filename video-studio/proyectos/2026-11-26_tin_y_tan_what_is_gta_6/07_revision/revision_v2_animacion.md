# Revisión de animación · short 4 (TIN-EN-S-004) · versión 2

Revisor: director de animación. Fecha: 2026-11-26. Motivo: el dueño vio la v2 y dijo que «la animación pierde un poco de
sentido cuando quieren interactuar en el espacio 3D, por ejemplo intentan correr y casi no se mueven, entre otras cosas»
y que «hablamos de producir algo de alta calidad» (`cambios/2026-11-26_short4_v2_animacion_en_el_espacio.md`).

Esta revisión cubre **el movimiento**. El encuadre y la profundidad están en `revision_v2_fotografia.md` (B1–B6, A1–A9);
la identidad, el texto y los cruces entre personajes, en `revision_v2_continuidad.md` (C1–C18). Donde un defecto ya está
ahí, lo cito y doy solo la causa de animación y su corrección en el motor.

**Veredicto: NO FIRMO la v2. CORREGIR.** Detalle en la sección 5.

## 0. Qué vi y con qué límites

- **Video:** `entregas_temporales/tin_y_tan_short04_v2.mp4` (1080×1920, 30 f/s, 986 f). Extraje los 986 fotogramas a
  una carpeta temporal fuera del repositorio y miré **fotograma por fotograma, en tiras numeradas**, estos tramos:
  f46–f122, f122–f181, f296–f340, f566–f615, f668–f697; **1 de cada 2** en f616–f664 y f878–f916; **1 de cada 3 o 4** en
  f196–f253, f356–f432 y f740–f816. No miré en tiras f432–f565, f698–f739, f817–f877 ni f918–f985: de esos tramos solo
  hablo por el guion y por las medidas.
- **Guion y motor:** leí completos `motor_de_accion/escena.html`, `guiones/tin_en_s_004.js` y
  `guiones/tin_en_s_004.tiempos.json`. Para medir, ejecuté el guion fuera del navegador (objetos de relleno en lugar de
  la escena) con las mismas funciones `pista`, `mezcla`, `EASE` y `esqueleto` del motor, y saqué por fotograma la
  posición, la pose y los pies de cada personaje. El guion y el motor no se tocaron.
- **Límites:** no vi el video reproducido en tiempo real (juzgo el movimiento por fotogramas consecutivos) ni oí el
  audio. Las medidas en unidades del mundo (u) salen del guion y son exactas respecto al código; las medidas en píxeles
  usan la cámara de `tiempos.json` con la focal ≈ 2954 px que calculó fotografía, y sirven como orden de magnitud. El
  «deslizamiento del pie» es calculado (recorrido sobre el suelo del pie más bajo mientras sigue siendo el de apoyo),
  no medido sobre la imagen. No comparé contra las hojas de contacto de Keter (no están en el repositorio): uso los
  tiempos de `estudios/2026-11-26_referencias_de_pelea_estudio_de_keter.md`, sección 3.
- **Todo número de corrección o de criterio de este documento es un valor de partida a comprobar en la vista previa,
  no un valor final.**

Tamaños que uso (del motor): R = 0,36 u. Tin y Tan: pierna 0,59 u, alto ≈ 1,8 u. Rival a escala 1: pierna 0,74 u.

## 1. Diagnóstico de fondo

### 1.1 Por qué «corren y casi no se mueven»

**La pose y el desplazamiento son dos pistas que no se conocen.** `corre(q, f0, f1)` (guion, línea 37) alterna
`corre1`/`corre2` cada 4 f, siempre, y la posición va aparte en `pos(...)`. Nada liga la cadencia de las piernas a la
distancia recorrida. En `corre1` los pies quedan separados 0,78 u (pie adelantado +0,835 R, pie atrasado −1,343 R): a un
paso cada 4 f, ese ciclo «pide» ≈ 5,9 u/s. Lo que el guion recorre de verdad:

| Carrera | Fotogramas | Recorrido (u) | dx / dz (u) | Velocidad media (u/s) | Pasos | u por paso | En pantalla (px) | Hacia donde mira |
|---|---|---|---|---|---|---|---|---|
| Tin, entrada | f50–f66 | 0,75 | −0,22 / −0,72 | 1,41 | 3 (cada 6 f) | 0,25 | ≈ 66 | bien |
| Rival, embestida | f141–f156 | 4,78 | +1,60 / +4,50 | 9,55 | 4 | 1,19 | ≈ 375 | bien |
| Tin, tras la patada | f200–f253 | 2,21 | −0,70 / +2,10 | 1,25 | 13 | 0,17 | ≈ 233 | **al revés** |
| Tin, al mostrador | f284–f301 | 3,18 | +1,46 / −2,82 | 5,61 | 4 | 0,80 | ≈ 370 | bien |
| Tan, tras el gancho | f359–f387 | 0,43 | +0,19 / −0,39 | **0,46** | 7 | **0,06** | ≈ 59 | bien |
| Tin, vuelve del mostrador | f375–f426 | 1,48 | −1,45 / +0,30 | 0,87 | 13 | 0,11 | ≈ 369 | **al revés** |
| Tan, cruce | f570–f585 | 2,40 | +2,40 / 0 | 4,81 | 4 | 0,60 | ≈ 672 | bien |
| Tan, al fondo | f630–f656 | 2,10 | −0,90 / −1,90 | 2,43 | 7 | 0,30 | ≈ 245 | bien |
| Tin, al fondo | f649–f656 | 0,80 | −0,38 / −0,70 | 3,41 | 2 | 0,40 | ≈ 72 | **al revés** |
| Tin y Tan, remate | f671–f687 | 1,19 cada uno | ±0,05 / −1,19 | 2,23 | 4 | 0,30 | ≈ 125 | de perfil, uno frente al otro |
| Tin, tras la explosión | f770–f800 | 0,33 | +0,15 / +0,30 | **0,33** | 8 | **0,04** | ≈ 40 | bien |
| Tan, tras la explosión | f770–f800 | 0,60 | +0,35 / +0,49 | 0,60 | 8 | 0,08 | ≈ 117 | bien |
| Tin, final | f909–f916 | 0,77 | +0,05 / +0,77 | 3,29 | 2 | 0,38 | ≈ 70 | de perfil, hacia cámara |

De 14 carreras, **solo 3 pasan de 4 u/s** (rival f141, Tin f284, Tan f570) y son las únicas que se leen como carrera.
En las demás el personaje hace el gesto de un sprint a 6 u/s y avanza entre 0,3 y 2,4 u/s. Las peores: **f770–f800
(un segundo entero de zancadas para avanzar 0,33 u, menos de un quinto de su altura)** y f359–f387. Visto en las tiras:
Tan en f360–f388 y los dos en f772–f800 pedalean en el sitio.

Las cinco causas, en orden de peso:

1. **Cadencia fija, sin relación con la distancia** (lo de arriba).
2. **Carreras hacia el fondo con un ciclo dibujado de perfil.** Los dibujos solo existen de lado (`mira` ±1 voltea en x).
   Cuando el recorrido es casi todo en z (remate: dz −1,19, dx 0,05), el personaje corre «de lado» y lo único que cambia
   es que se achica ≈ 12 % y sube ≈ 100 px. Con la cámara frontal y lejana (fotografía, sección 1) 1 u en profundidad son
   ≈ 100 px; 1 u lateral son ≈ 250–350 px. Una carrera de perfil **tiene que recorrer x**.
3. **Marcha atrás.** En tres carreras Tin mira a la derecha (`mira` = +1 desde f189) y se desplaza hacia la izquierda:
   f200–f253, f375–f426 y f632–f656. Visto en f202–f250 y f376–f424: corre hacia el rival y se aleja de él.
4. **La curva por defecto frena en cada clave.** `pista` usa `io` si la clave no trae curva (`EASE[e || 'io']`,
   `escena.html`). Las carreras f50–f66, f200–f253, f375–f426, f770–f800 y f909–f916 arrancan y terminan a velocidad
   cero: los primeros 8–10 f son zancadas completas con ≈ 0,1 u de avance. Las carreras `lin` hacen lo contrario: pasan
   de 0 a tope en 1 f y paran en seco, sin arranque ni frenada.
5. **No hay cuerpo en la carrera.** El torso va a 30° fijos corra a 0,3 o a 6 u/s; la cadera sube y baja 0,057 R
   (≈ 0,02 u, ≈ 6 px) entre `corre1` y el punto medio; no hay fase de vuelo, porque `colocar` pega siempre el punto más
   bajo de la pose al suelo (`caderaY = e.bajo · R · escala + y`). Sin rebote, sin inclinación que cambie y sin los dos
   pies en el aire, el ojo no cree el esfuerzo.

### 1.2 Pies que resbalan

- **Dentro de las carreras:** con 0,78 u de separación de pies y 0,04–0,40 u de avance por paso, el pie de apoyo patina
  entre 0,4 y 0,7 u por paso (≈ 100–200 px). Calculado sobre el pie más bajo: f200–f253 ≈ 8,4 u de patinazo acumulado
  en 13 pasos; f770–f800 ≈ 5,2 u; f375–f426 ≈ 8,4 u. Incluso la carrera buena de Tan (f570–f585) patina ≈ 0,5 u por paso.
- **Fuera de las carreras (se deslizan en pose de pie):** el guion mueve la posición mientras la pose es guardia,
  festejo o dibujo. Tramos con más de 0,25 u: Tin f574–f584 (0,94 u a 2,8 u/s sosteniendo el golpe), **Tin f632–f648
  (1,82 u a 3,4 u/s en pose `dibuja`, parado)**, Tin f591–f626 (0,66 u lanzando el mazo), Tin f69–f75 (0,45 u mientras
  carga el puño hacia atrás: avanza al tomar impulso), Tan f140–f155 (0,77 u en guardia), Tan f180–f195 (0,80 u con los
  brazos arriba festejando), Tan f309–f339 (0,58 u), Tan f550–f554 (0,41 u en 4 f = 3,1 u/s en guardia) y f555–f569
  (0,55 u), rival f811–f825 (0,49 u).

### 1.3 Saltos de posición y claves cruzadas

Los saltos de 1 f en el contacto (`'salto'`, 0,2–0,35 u del atacante) son intención y valen como embestida **si llevan
borrón**; hoy no lo llevan (1.5). Aparte hay saltos que son errores: al escribir las pistas con fotogramas calculados
(`K4 + 11`, `K.mazo − 2`…) varias claves quedaron **fuera de orden o en el mismo fotograma**, y el `sort` final las
reordena en silencio:

| Pista | Fotograma | Qué pasa | Visto |
|---|---|---|---|
| Tin, posición | f584–f585 | `[K.mazo−2 = 584, (0,1; −2,2)]` cae **antes** de `[K4+11 = 585, (0,7; −2,6)]`: Tin se va 0,94 u en 10 f y **vuelve 0,72 u en 1 f (≈ 190 px)** | f584→f585→f586: tirón claro |
| Rival, pose | f602–f611 | `[K5−6 = 606, guardia]` cae en medio de `recogido` (602–608): **pose de guardia en pleno salto**; y `[K5−1 = 611, recibe]` comparte fotograma con `agachado`: la reacción previa al mazazo nunca se ve | f604–f609: cambia de forma en el aire |
| Tan, pose | f882–f887 | `[L.B.f1 = 886, pregunta]` y `[K6 = 886, recibe]` en el mismo fotograma: de f842 a f882 la pose se va deshaciendo en vez de sostenerse y en f887 cambia 290° en 1 f | no mirado en tira |
| Rival, pose | f514–f515 | `agachado` y `poder` en f514: cambio de 215° en 1 f justo al dibujar la espada | no mirado en tira |
| Rival, pose | f126–f129 | `[K1+44 = 126, agachado]` y `[K2−42 = 127, guardia]`: se pone de pie en 1 f | tapado por Tan |
| Tin y Tan, pose | f916–f919 | `quieto` (916/918) y `guardia` (918/919) cruzadas: un golpe de guardia de 1 f antes del cierre | f916: Tin pasa de zancada a firme en 1 f |
| Tin y Tan, pose | f681 | clave doble (fin de `corre` y arranque de `ataque`): sin efecto visible, pero es la misma familia |  |

### 1.4 Escala con la profundidad

La perspectiva es correcta (cámara de perspectiva real); el problema no es la fórmula sino lo poco que rinde: con la
cámara a 8–14 u, 1 u de fondo cambia el tamaño ≈ 10–12 %. Por eso un personaje que «corre al fondo» 1,2 u parece que
no se movió, y el rival, que además se achica por guion (1,15 → 0,62), se lee «más pequeño», no «más lejos»
(continuidad lo anota en f693). El espacio lo tienen que vender el desplazamiento lateral, la diagonal y el cruce por
delante o por detrás de la utilería; la cámara es de fotografía (su sección 3). Mi parte: **ninguna acción de carrera o
de golpe puede depender solo de z**.

### 1.5 Golpes: los tiempos están; el cuerpo y el contacto no

`ataque()` cumple en papel la gramática de Keter: 6 f de anticipación + 6 f de pausa, contacto de 1 f, 5 f sostenido y
6 f de recuperación. Lo que falla:

- **El contacto no cae en el cuerpo del rival.** Las posiciones del atacante, del rival y de la estrella son tres
  números escritos a mano. Calculado en el fotograma K (x; y en u):

| Golpe | Punto que golpea | Rival (eje x; cadera y) | Estrella del guion | Problema |
|---|---|---|---|---|
| K1 f82, puño de Tin | (−0,04; 0,93) | (−0,25; 0,95), escala 1,15 | (−0,02; 1,55) | La estrella está 0,62 u por encima del puño y a 0,36 u del centro de la cabeza de Tin (0,26; 1,33): **le tapa la cara** (C1) |
| K2 f169, patada de Tan | pie (−0,61; 0,45) | (−0,15; 0,85) | (−0,50; 1,20) | El pie queda 0,46 u corto y a la altura de la rodilla; la estrella, 0,75 u más arriba, en el aire (C2). El rival está en la columna de Tin |
| K3 f314, gancho de Tin | puño (2,34; 1,97), z −2,9 | (2,85; 2,11), z −3,4 | (2,62; 2,85) | El puño queda 0,5 u corto en x y 0,5 u en z; la estrella, 0,88 u más arriba. Además, en la pose `gancho` **el puño cae sobre la propia cara de Tin** (mano 0,80 R; −2,57 R, cabeza 0,70 R; −2,43 R). Visto en f314–f335 |
| K4 f574, bastón de Tin | mano (1,71; 0,93), punta (2,60; 1,05) | (1,85; 0,73) | (1,70; 1,45) | El bastón sí cruza al rival, pero la mano ya pasó su eje; la estrella está a 0,31 u de la cabeza de Tin: le tapa la cara (C1) |
| K5 f612, mazo de Tan | mano (2,83; 0,64), cabeza del mazo (3,71; 0,45) | (2,90; 0,35) | (2,85; 0,85) | **Las manos de Tan están dentro del rival** y el mazo cae 0,8 u más allá; cabeza de Tan (2,64; 1,21) sobre la del rival (2,46; 1,11). Por eso «el mazo desaparece» (C9) |
| KR f694, remate doble | manos en x −0,19 y −0,01 | (−0,12; 0,73), z −6,4 | (−0,25; 1,35) y (0; 0,95) | Tin y Tan (z −6,0) chocan entre sí; el rival queda 0,4 u detrás y a escala 0,69 (C8). Visto en f694–f697: un nudo |
| K6 f886, bastón de Tin | mano (−0,04; 0,93), punta (0,85; 1,05) | (0; 0,46), escala 0,62 | (−0,10; 1,05) | La mano de Tin está en el eje del rival: Tin encima del rival. Visto en f886–f892 |

- **No hay arco de borrón.** El motor apaga el calco de movimiento cuando el guion va por fotogramas
  (`GU.porFotogramas ? false : rapidez > 7`, en `actualizar`). Keter midió «1 o 2 f, con arco de borrón del color de
  quien golpea»: en la v2 el golpe pasa de `carga` a `golpe` en 1 f (hasta 165° de brazo, y la cabeza de Tan viaja
  ≈ 1,0 u en f611→f612) sin nada que una las dos poses. Se lee como un corte, no como un golpe.
- **La pausa es un congelado.** 6 f con pose y posición idénticas, y muchas veces con todo el cuadro quieto: f302–f313
  (Tin agachado y rival sentado, ≈ 11 f sin un píxel de cambio), f601–f611 (Tan con el mazo arriba), f683–f693 (remate).
  La referencia dice «casi quietos», no congelados.
- **La anticipación no se distingue.** `carga` (torso −14°, brazo atrás) se parece a la guardia vista de frente al
  dibujo (f76–f81). Y en K1 Tin avanza 0,45 u mientras «carga hacia atrás» (f69–f75).
- **Recuperación sin sobrepaso:** pose de golpe rígida 5–9 f y vuelta `io` a la guardia.

### 1.6 Remate (f671–f697), que resume todo

Tin y Tan pedalean 11 f de perfil, uno frente al otro, sin acercarse (el mazo de Tan le tapa la cara: f671–f681). En
f682 la pose pasa de torso +30° a `carga` (−14°) y las dos cabezas **retroceden ≈ 0,68 u**: después de «correr» quedan
más separados. Congelados 11 f (f683–f693). En f694 saltan 0,22 u, la pose de golpe adelanta la cabeza otros ≈ 0,68 u y
quedan uno sobre el otro, con el rival detrás. Coincide con C5 y C8.

### 1.7 Vuelos, caídas y levantadas

- **Los vuelos no son parábolas y cada uno tiene su gravedad.** El motor usa 22 u/s² para los trozos (`pasoTrozos`);
  los personajes van por claves con `out`/`in`:
  - K1 (f82–f108): sube sin parar 17 f hasta 1,4 u, choca y cae 1,25 u en 7 f (equivale a ≈ 46 u/s²).
  - K3 (f314–f337): sube 3,6 u en 11 f, flota 6 f en 5,0 u y **cae 3,3 u en 4 f** (hasta 1,91 u en un fotograma,
    ≈ 57 u/s). Con 22 u/s² esa caída duraría ≈ 16–18 f. Además está fuera de cuadro de f322 a f332 (B6 de fotografía):
    se ve subir 7 f, desaparece 11 f y vuelve 3 f antes del impacto.
  - K4 (f574–f596) y el salto f629–f648 (2,3 u de alto, 4,8 u de largo en 19 f): aceptables de ritmo, sin arco real.
- **Aterrizajes sin peso.** Ninguno tiene aplastamiento, polvo propio ni asentamiento: f108 (cae ya en `caido`), f186,
  f337, f596, f610, f648. En f596 aterriza y **2 f después (f598) vuelve a saltar 2,0 u**; aterriza en f610 y en f612
  ya recibe el mazo. No hay un solo fotograma de peso entre acción y acción.
- **Caídas y levantadas tapadas o sin transición.** f108–f127: el rival cae en x −1,95, la misma columna de Tan
  (x −1,95), 5 u detrás: la caída y la levantada ocurren **tapadas por Tan** (C3; visto en f102–f140). De `caido`
  (torso −88°) a `agachado` (+30°) se pasa girando el torso 118° como aguja de reloj en 10–12 f, sin apoyo de manos ni
  pose sentada (f116–f126, f215–f227 —C12—, f358–f370), y en f126–f127 hay 1 f hasta la guardia (1.3).
- **Reacciones.** La reacción del rival empieza en K (bien). Tin y Tan casi no reaccionan a nada: no se apartan cuando
  el rival les pasa por encima (f100–f120) y la bola de fuego de 5,6 u (f728) estalla a 1,4–1,6 u de ellos sin moverlos:
  se agachan en 1 f (tapado por el destello), sostienen `recibe` 16 f y luego «corren» 0,3–0,6 u (f770–f800).
- **Dos mazos.** Tin lanza el mazo en f598 y vuela hasta f603, pero Tan ya lo tiene en la mano desde f598
  (`K5 − 14`) y hace `atrapa` en f597: f598–f603 hay un mazo en el aire y otro en la mano (visto).
- **El reloj lento no es de todos.** `reloj` (A2) frena solo humo, polvo y trozos; los personajes van por número de
  fotograma. En los lanzamientos el rival vuela a velocidad normal dentro de un mundo al 25 %.

### 1.8 Lo que sí funciona

Los tiempos del golpe (6 + 6, 1, 6) y los calcos del lanzamiento; la desaceleración del rival en el aire (`out`); la
embestida del rival f141–f156 y el cruce de Tan f570–f585 como velocidad (4,8–9,6 u/s); el sobrepaso de la curva `back`
en festejos; el aplastado del mazazo (f612–f627) como idea.

## 2. Defectos por tramo y fotograma

Gravedad: **B** bloquea presentar · **A** alta · **M** media · **b** baja. Las correcciones están en términos del motor;
los valores son de partida.

### Bloqueantes

| ID | Fotogramas | Defecto | Corrección en el motor |
|---|---|---|---|
| AN1 | f50–f66, f200–f253, f359–f387, f375–f426, f770–f800 (tabla 1.1) | Carrera sin desplazamiento: 0,3–1,4 u/s con gesto de sprint; 0,04–0,25 u por paso | Sustituir `corre()` + claves de `pos` por **una sola función de locomoción** en el guion, `locomocion(q, f0, f1, puntos, modo)`, que genere a la vez posición y pose (sección 3.1). Regla de reparto: recorrido < 0,3 u → sin ciclo (cambio de peso); 0,3–1,5 u → 1–3 pasos de caminar (zancada 0,45 u, 10–12 f por paso) o derrape; ≥ 1,6 u → carrera a ≥ 3,0 u/s (objetivo 4–6). En concreto: f359–f387 y f770–f800 **dejan de ser carreras** (pasos cortos o empuje de la explosión, AN14); f200–f253 y f375–f426 se acortan a 14–20 f con el recorrido real o se parten en «carrera corta + guardia» |
| AN2 | f671–f687, f630–f656, f649–f656, f909–f916 | Carrera hacia el fondo o hacia cámara con ciclo de perfil: no se lee | Regla de puesta en escena: en toda carrera **\|dx\| ≥ 1,5 · \|dz\|**. Remate: Tin y Tan parten abiertos (x ≈ ±2,2, z −5,4) y convergen en diagonal al rival (x ≈ ±0,95, z −6,2): ≈ 1,5 u en 10–12 f ≈ 4 u/s; el plano P16 debe abrir para que quepan (lo fija fotografía). f630–f656: repartir el trayecto como x primero (carrera) y z después dentro del corte a P16 |
| AN3 | f200–f253, f375–f426, f632–f656 | Tin corre mirando al lado contrario del desplazamiento | `locomocion` fija `mira` = signo de dx mientras dure; al llegar, giro de 2 f a la mira de combate. Si se quiere retroceder de cara al rival, modo `retrocede` (pasos atrás, torso −8°, ≤ 1,5 u/s), nunca el ciclo de carrera |
| AN4 | Todas las carreras y los tramos de 1.2 | Pies que patinan: 0,4–0,7 u por paso en carrera; hasta 1,82 u deslizándose en pose de pie (f632–f648) | En carrera, fase ligada a la distancia (3.1) con zancada = separación real de pies de la pose. Fuera de carrera, prohibido mover `pos` más de 0,10 u con una pose de pie: o va por `locomocion`, o es `derrape` declarado (pose `resbala`, polvo `polvoC` en los pies, ≤ 0,6 u, frenando con `out`) |
| AN5 | f671–f697 | Remate: no se acercan, retroceden ≈ 0,68 u al cargar, congelado de 11 f, nudo sobre nudo | AN2 + contacto resuelto por alcance (AN6): golpes a dos alturas y desde dos lados sin cruzar armas (Tin bastón alto desde la izquierda, Tan mazo bajo desde la derecha), rival **en el mismo z** que ellos (\|Δz\| ≤ 0,15) y cabezas separadas ≥ 0,6 u. La carga se hace **en carrera** (últimos 2 pasos con el arma atrás), sin clave `carga` de torso −14° |
| AN6 | K1 f82, K2 f169, K3 f314, K4 f574, K5 f612, KR f694, K6 f886 (tabla 1.5) | El golpe no cae sobre el rival; la estrella cae sobre la cara de quien golpea (C1, C2, C8, C9) | (a) Estrella y gotas en el punto real: el motor ya calcula `manoMundo`, `pieMundo` y `armaMundo` en `colocar`; los `HECHOS` de K deben usar ese vector (+0,05 en z), no coordenadas escritas. Para el arma, el punto a 2/3 del mango. (b) Colocar al atacante por alcance: `x_atacante = x_rival − mira · alcance(pose)`, con alcance de partida: puño `golpe` 0,76 u, patada 0,59 u, bastón 1,35 u, cabeza del mazo 1,66 u. Ejemplos: K5 → Tan en x ≈ 1,25 (hoy 2,05); K6 → Tin se queda en x ≈ −1,10 sin el salto de 0,3 u; K2 → pose `patada` con el muslo a ≈ 120° para subir el pie a ≈ 0,85 u y rival en x ≈ −0,60; K3 → rival en el mismo z que Tin y en x ≈ 2,35, o Tin sube al mostrador. (c) Rehacer `gancho` para que el puño quede delante y por encima de la cabeza (`aF` de partida [125, 165]) |
| AN7 | f584–f585, f602–f611, f882–f887, f514–f515, f126–f129, f916–f919 (tabla 1.3) | Claves fuera de orden o duplicadas: teletransporte de 0,72 u, poses que parpadean, reacción que no se ve | Corregir cada caso (p. ej. `K.mazo − 2` → `K4 + 12`; `K5 − 6`/`K5 − 1` del rival después de `K4 + 37`, o quitar el segundo salto, AN11). Y que el guion **falle al construir** si, tras escribir una pista, dos claves comparten fotograma o el orden de escritura no es creciente (en vez del `sort` silencioso de la línea 125) |
| AN8 | f597–f603 | Dos mazos a la vez; Tan «atrapa» antes de que llegue | `extra('tan')`: el mazo en la mano desde `K.mazo + 17` (cuando termina `vuelo(mazoV…)`), no desde `K5 − 14`. Pose `atrapa` de Tan en `K.mazo + 15` a `+17`, con 2 f de retroceso del brazo al recibir el peso. Alargar el vuelo de 5 a 8 f |

### Altas

| ID | Fotogramas | Defecto | Corrección en el motor |
|---|---|---|---|
| AN9 | Los 7 contactos | Sin arco de borrón ni intermedio: el golpe es un corte de pose | (a) En `actualizar` de `escena.html`, dejar que el guion por fotogramas pida el calco: `borron = GU.borron ? GU.borron(id, S) : (!GU.porFotogramas && rapidez > 7)`; el guion lo activa en K y K+1. (b) Arco de golpe: plano con un arco de tinta entre la posición de la mano o del arma en K−1 y en K, 2 f (K y K+1), del color de quien golpea, grosor ≈ 0,12 u. (c) Opcional: 1 f intermedio en K−1 con la pose a 70 % (`in`) |
| AN10 | f314–f337 (K3), f82–f108 (K1) | Vuelos sin parábola; caída de 3,3 u en 4 f; cada vuelo con su gravedad | Función `vueloDe(q, f0, desde, hasta, apice)` en el guion que escriba las claves por fotograma: x y z con `out` suave, y = parábola con **una sola gravedad** (partida: 22 u/s², la de los trozos; si queda lento, 30). K3: ápice 3,4 u (acorde con B6), subida ≈ 12 f, 4–6 f de flotación, caída ≈ 10–12 f; si no cabe antes de la voz, bajar el ápice, no acelerar la caída. Tope: ≤ 0,6 u de caída por fotograma |
| AN11 | f108, f186, f337, f596–f612, f648 | Aterrizajes sin amortiguación; del aterrizaje f596 al salto f598 y del aterrizaje f610 al mazazo f612 hay 2 f | Pose nueva `aterriza` (agachado profundo, manos al suelo) + `extra.aplasta` 0,30–0,40 durante 2–3 f + `polvoC` (6–8) en los pies + 4–6 f de asentamiento antes de cualquier otra acción. Quitar el segundo salto del rival (f598–f610): tras K4 cae junto al mostrador (x ≈ 2,9) rodando, y de ahí recibe el mazo |
| AN12 | f108–f140, f204–f239, f337–f370 | Caídas y levantadas tapadas o sin transición | (a) Que el rival **no aterrice en la columna de un protagonista**: tras K1, x ≈ −0,9 (no −1,95) o Tan desplazada (lo cruza continuidad, C3). (b) Levantada en 3 poses: `caido` → `sentado` (nueva: torso −35°, manos atrás apoyadas) → `agachado` → guardia, ≥ 14 f en total, con la cadera como pivote fijo en el suelo. (c) Si no hay tiempo, cortar a otro plano en vez de levantarlo en 1–6 f |
| AN13 | f69–f81, f302–f313, f601–f611, f683–f693 | Anticipación poco legible y pausa congelada; Tin avanza mientras carga | Anticipación: el cuerpo se va **al lado contrario** del golpe 0,10–0,15 u (hoy avanza 0,45 u). Pose `carga` con más silueta (torso −22°, codo fuera del cuerpo). Pausa viva: en los 6 f de pausa, deriva de 2–3° de torso y 0,02 u de cadera hacia atrás (curva `out`), nunca dos fotogramas idénticos. Recuperación: `golpe` 3 f, sobrepaso con `back` y guardia en 6–8 f |
| AN14 | f719–f800 | La explosión no mueve a Tin ni a Tan; luego «corren» 0,3–0,6 u | En `K.bola` (f728): empuje de 0,6–0,8 u hacia cámara en 8 f con `out`, pose `resbala` (derrape con polvo), brazo cubriendo la cara; 6 f de asentamiento; y el tramo f770–f800 pasa a 2 pasos de caminar hacia el rival que se recompone, o a nada |
| AN15 | Todas las carreras | Torso a 30° fijo, sin rebote, sin fase de vuelo | Ciclo de 4 poses por paso (3.1) con rebote de cadera de partida 0,08–0,10 u (bajada −0,05 u en el apoyo, +0,04 u en el vuelo) e inclinación = 8° + 5,5° por u/s (tope 34°), +8° en los 3 f de arranque y −15° con pose `resbala` en los 3–4 f de frenada |
| AN16 | Toda pista de `pos` sin curva | `io` por defecto: cada clave es una parada | En `locomocion` y `vueloDe`, posiciones por fotograma (clave por fotograma con `'lin'`) siguiendo un perfil de velocidad: 3–4 f de arranque, crucero constante, 3–4 f de frenada. No hace falta tocar `pista`. Añadir a `EASE` del motor, si se quiere, `arranca: u => u*u` y `frena: u => 1-(1-u)*(1-u)` |

### Medias y bajas

| ID | Gr. | Fotogramas | Defecto | Corrección |
|---|---|---|---|---|
| AN17 | M | K+6 a K+17 de cada lanzamiento, f671–f681 | El reloj lento frena la física y no a los personajes | O se quita `LENTOS` de los tramos con personajes en vuelo, o `locomocion`/`vueloDe` reparten sus fotogramas con el mismo factor. Decidir uno; hoy conviven dos tiempos |
| AN18 | M | f640–f664, f671–f681, f772–f800 | El mazo cruza la cara de Tan mientras corre o espera (`A(pose, 150)`) | Ángulo del arma en carrera y espera: 200–215° (al hombro, por detrás de la cabeza) en vez de 150°. Coordinar con continuidad (cara legible) |
| AN19 | M | f586, f595, f181 | Brazos que dan la vuelta larga (cambios de 300° o más al mezclar ángulos de `poder` con otras poses) | Normalizar los ángulos al mezclar (camino corto) o reescribir `poder`/`festeja` con ángulos del mismo signo que la pose vecina |
| AN20 | M | f314 | Tin sube 0,45 u en 1 f en el gancho | Con AN9 (borrón) vale; añadir 1 f intermedio a 0,2 u |
| AN21 | M | f484–f511, f839–f873 | Tin y Tan inmóviles 28 y 35 f (C17) | Pausa viva general: respiración de ±1,5° de torso en ciclo de 40 f y un parpadeo o gesto propio cada ≈ 45 f. Ningún personaje visible más de 8 f idéntico |
| AN22 | b | f141–f156 | El rival corre a 1,19 u por paso con pierna de 0,80 u (zancada de 1,5 piernas) y pasa por encima de Tin (C2) | Con `locomocion`, zancada 1,0 u × escala → ≈ 5 pasos; trayectoria que no cruce la columna de Tin |
| AN23 | b | f46–f59 | Tan retrocede 0,47 u en guardia tras el pisotón | Declararlo `derrape` con polvo (AN4): la idea es buena |

## 3. La corrección de fondo, en términos del motor

### 3.1 Locomoción ligada a la distancia (sustituye a `corre`)

Se puede hacer **solo en el guion**, sin tocar `escena.html`, escribiendo una clave de `pos` y una de `pose` por
fotograma. Valores de partida:

- **Zancada (un paso):** Tin y Tan 0,80 u × escala (la separación real de pies de la pose, 0,78 u); rival 1,0 u × escala.
  Caminar: 0,45 u.
- **Fase = distancia acumulada / zancada.** La pose sale de la fase, no del fotograma. La cadencia resulta sola:
  a 4 u/s, 6 f por paso; a 6 u/s, 4 f; a 3 u/s, 8 f. Si sale más de 8 f por paso, no es carrera: se camina.
- **Ciclo de 4 poses por paso** (espejo para la otra pierna): `corre_contacto` (pie adelantado en el suelo, pierna casi
  recta), `corre_baja` (rodilla de apoyo flexionada, cadera −0,05 u), `corre_pase` (pie de apoyo bajo la cadera, la
  otra rodilla adelante), `corre_vuelo` (los dos pies en el aire, +0,04 u). Hoy solo existen los dos extremos.
- **Fase de vuelo:** `colocar` pega el punto más bajo al suelo; para despegar, sumar el rebote a la `y` de `pos` en
  `corre_vuelo` (ya se usa `y` para los saltos).
- **Pie de apoyo fijo:** entre `corre_contacto` y `corre_pase`, la x de la cadera se calcula desde el pie plantado
  (`x_cadera = x_pie_fijo − desplazamiento del pie en la pose`), no al revés. Para comprobarlo hace falta que el motor
  publique también el pie de atrás (hoy solo `pieMundo` = `lF`).
- **Perfil de velocidad:** 3–4 f de arranque, crucero, 3–4 f de frenada con derrape de 0,15–0,25 u y polvo.
- **Carrera mínima:** 1,6 u de recorrido (2 zancadas) y ≥ 3,0 u/s de crucero; objetivo 4–6 u/s (2–3 alturas por segundo).

### 3.2 Poses nuevas para el catálogo

`corre_contacto`, `corre_baja`, `corre_pase`, `corre_vuelo`, `paso1`, `paso2` (caminar), `retrocede`, `aterriza`,
`sentado`, y los ajustes de `carga`, `gancho` y `patada`. Todas pasan por la hoja de poses antes de usarse.

### 3.3 Contactos por alcance, no por coordenadas

Tabla de alcances por pose (se calcula una vez con `esqueleto`) y dos ayudas en el guion: `colocaAtacante(q, rival, pose)`
y `puntoDeGolpe(q)` (lee `manoMundo`/`pieMundo`/`armaMundo`). La estrella, las gotas y el arco salen de ahí.

### 3.4 Lo que sí pide tocar `escena.html` (poco)

1. Permitir el calco de movimiento con guion por fotogramas (AN9a): una línea en `actualizar`.
2. Publicar el pie de atrás (`pieBMundo`) y el pie de apoyo para el control automático.
3. Opcional: `EASE.arranca`, `EASE.frena`.

## 4. Criterios medibles para firmar la v3

Para un control automático que lea las pistas del guion y las posiciones proyectadas (como hace
`eventos_y_medidas_del_motor.json`). **Todos son valores de partida: se ajustan una vez tras la primera vista previa y
se dejan escritos.**

| # | Criterio | Umbral de partida |
|---|---|---|
| M1 | Velocidad de crucero en todo tramo marcado como carrera (sin contar arranque ni frenada) | ≥ 3,0 u/s; objetivo 4–6 u/s |
| M2 | Recorrido mínimo de una carrera | ≥ 1,6 u; por debajo, caminar o derrape |
| M3 | Largo de zancada (recorrido / pasos) | 0,80 u × escala ± 15 % (Tin, Tan); 1,0 u × escala ± 15 % (rival) |
| M4 | Cadencia | 4–8 f por paso en carrera; 9–12 f al caminar; nunca fija por fotograma |
| M5 | Dirección de la carrera | \|dx\| ≥ 1,5 · \|dz\|; `mira` = signo de dx en el 100 % de los fotogramas del tramo |
| M6 | Desplazamiento en pantalla de una carrera | ≥ 300 px a 1080×1920 |
| M7 | Deslizamiento del pie de apoyo | ≤ 4 px por fotograma y ≤ 12 px por apoyo (≈ 0,04 u) |
| M8 | Desplazamiento de cadera con pose de pie (fuera de locomoción y de derrape declarado) | ≤ 0,10 u por tramo |
| M9 | Rebote de cadera en carrera | 0,06–0,12 u pico a pico; ≥ 1 f con los dos pies en el aire por paso |
| M10 | Inclinación del torso | crece con la velocidad (≤ 12° por debajo de 1,5 u/s; 25–34° por encima de 4 u/s) |
| M11 | Claves | 0 claves duplicadas o fuera de orden en cualquier pista; el guion falla si las hay |
| M12 | Salto de posición de 1 f | ≤ 0,35 u y solo en K con borrón; fuera de K, ningún cambio > 0,25 u por fotograma que no sea carrera o vuelo declarado |
| M13 | Cambio de pose de 1 f | ≤ 60° en cualquier articulación fuera de K y K+1 |
| M14 | Golpe: anticipación | 10–12 f, con los últimos 5–6 en pausa viva (cambio por fotograma > 0 y ≤ 3° / 0,02 u) |
| M15 | Golpe: contacto | 1–2 f, con arco de borrón visible en K y K+1 |
| M16 | Golpe: punto de contacto | a ≤ 0,12 u del cuerpo del rival en x e y, entre su cadera y su cabeza; \|Δz\| ≤ 0,15 u |
| M17 | Golpe: estrella | a ≤ 0,10 u del punto de contacto y a ≥ 0,45 u del centro de la cabeza de quien golpea |
| M18 | Golpe: separación | centros de cabeza de atacante y rival a ≥ 0,6 u en K; entre Tin y Tan ≥ 0,6 u |
| M19 | Golpe: recuperación | 6–8 f, con sobrepaso |
| M20 | Vuelos | y(t) parabólica con una sola gravedad (22 u/s² ± 25 % en tiempo de caída); ≤ 0,6 u de caída por fotograma; 4–15 f de flotación o giro tras un lanzamiento |
| M21 | Aterrizajes | 2–3 f de aplastado, polvo en el fotograma de contacto y ≥ 4 f de asentamiento antes de la acción siguiente |
| M22 | Levantadas | de `caido` a de pie en ≥ 14 f con ≥ 2 poses intermedias, y a la vista (solape en pantalla con otro personaje < 30 %) |
| M23 | Congelados | ningún personaje visible con pose y posición idénticas más de 8 f; nunca todo el cuadro idéntico más de 2 f |
| M24 | Objetos | cada arma existe una sola vez por fotograma (en la mano o en el aire) |
| M25 | Reloj | personajes y física con el mismo factor de tiempo en cada fotograma |

Además de los números, **firmo solo después de ver la v3 en movimiento** (o, si no puedo, tiras consecutivas de todas
las carreras, golpes, vuelos y levantadas), porque M1–M25 detectan lo que se rompió en la v2, no garantizan que se sienta bien.

## 5. Veredicto

**No firmo la v2. Corregir y volver a pasar por animación antes de presentar.**

Bloquea la firma de la v3 (los ocho):

1. AN1–AN4: ninguna carrera con ciclo fijo; locomoción ligada a la distancia, sin marcha atrás, sin carreras en
   profundidad pura y con pies que no patinan (M1–M10).
2. AN5 y AN6: los siete contactos caen sobre el rival y la estrella sale del punto real de golpe (M16–M18).
3. AN7 y AN8: cero claves cruzadas y un solo mazo (M11, M24).

Deben ir en la v3 aunque no bloqueen por sí solos: AN9 (borrón y arco), AN10–AN12 (parábolas, aterrizajes, levantadas),
AN13 (pausa viva), AN14 (reacción a la explosión), AN15–AN16 (cuerpo y perfil de velocidad). El resto (AN17–AN23) puede
quedar anotado si el plazo aprieta.

Dependencias con los otros oficios:

- **Fotografía:** AN2 y AN5 necesitan planos que dejen ≥ 3 u de ancho útil en las carreras (su A2–A4 y la opción «media»
  de su sección 3); AN10 depende de su B6 (ápice dentro de cuadro); AN12 de que la caída no quede tras un protagonista.
- **Continuidad:** AN6 resuelve C1, C2, C8 y C9; AN5 resuelve C5; AN1 resuelve C6 y C7; AN12 resuelve C3 y C12.
- **Jefe de producción:** escribir el control de M1–M25 y añadirlo a la puerta de presentación.
- **Sonido:** si se mueven fotogramas de aterrizaje o se quita el segundo salto del rival, cambian los eventos.

Lo que no revisé y queda pendiente para la v3: el video en movimiento, el audio contra el contacto (la regla es sonido
en K o en K−1) y la comparación con las hojas de referencia de Keter.

No toqué código ni ningún otro archivo; no hice commit. Las tiras y el guion de medición quedaron en una carpeta
temporal fuera del repositorio.
