# Revisión de animación — short 4, versión 3 (`tin_y_tan_short04_v3.mp4`)

- **Pieza revisada:** `06_final/tin_y_tan_short04_v3.mp4`, sha256 `511571dd5f4d` (12 primeros caracteres). **No pude
  calcularlo yo** (en esta sesión no tengo consola): es el dato que dio producción el 2026-11-27.
- **Firma:** director de animación, 2026-11-27.
- **Convención de nombres:** Tin = el de la gorra naranja (el que atrapa el lápiz en f0); Tan = el verde de la bufanda;
  el rival = el garabato negro. Los fotogramas son los de la numeración de las tiras (f = fotograma).

## 1. Qué miré y con qué límites

- Miré **las 21 tiras completas** (`rev_v3/tira_01` a `tira_21`, 1 de cada 2 fotogramas, f0–f984), 13 fotogramas compuestos
  de `06_final/fotogramas/` (f312, f318, f396, f486, f504, f552, f582, f660, f702, f762, f846, f0, f984),
  `07_revision/control_encuadre_v3.md`, la sección D22–D33 de `direccion.md` y `revision_v2_animacion.md`.
- **No pude comprobar:** (a) el sha256 ni reproducir el video; (b) movimiento fotograma a fotograma: con 1 de cada 2 los
  contactos (K) y los giros de `mira` de 3 f se ven por la estrella y por la pose antes y después, no cuadro a cuadro;
  (c) el código (`tin_en_s_004.js`, `escena.html`): no lo abrí, así que los nombres de pistas y de poses de las
  correcciones son orientativos y quien programa los ajusta; (d) la sincronía con el sonido (no es mío).
- Dónde hay un defecto que no vi en las tiras pero el control automático dice «bien» (resbalón de pies), me fío del
  control y lo digo.

## 2. Defectos bloqueantes de la v2 (mi revisión): estado en la v3

| # | Defecto de la v2 | Estado | Prueba |
|---|---|---|---|
| B1 | Carreras que no avanzan | **Resuelto** | Control M1: 5 carreras de 2,1 a 4,5 u a 4,6–6,2 u/s, un paso cada 6,2–7,3 f. Se ve en f288–f292 (Tin cruza hacia el mostrador con zancada abierta y torso inclinado), f577–f594 (Tan cruza de borde a borde en 17 f) y f664–f676 (Tin y Tan cargan hacia el televisor). La carrera del rival f146–f166 se lee. Las cinco carreras falsas de la v2 ya no existen |
| B2 | Marcha atrás | **Resuelto** (una reserva en M1) | No hay carreras en sentido contrario a la mirada. El único tramo que se mueve hacia atrás es Tin en f376–f410 (ver M1) |
| B3 | Patinaje con la pose congelada | **A medias** | Los reposicionamientos de guardia ya no se ven deslizar; sigue habiendo un deslizamiento de cuerpo tumbado en f212–f216 (ver A3) |
| B4 | Remate que parece golpe entre ellos | **A medias** | Mejor: en f694–f702 el golpe llega a la base del pilar del televisor y el rival sale hacia arriba, con calcos, hasta el televisor (f702, f706–f716); las cabezas de Tin y Tan quedan a un tercio del ancho. Sigue siendo un sándwich (Tin a la izquierda, Tan a la derecha, rival en medio) y la reacción a la onda es un agachado quieto de unos 20 f (f728–f748), sin empuje (M3 y M4) |
| B5 | Estatuas | **No resuelto** | En la tabla de A1 de abajo: Tin y Tan quedan con el cuerpo clavado f752–f872 (f762 contra f846: misma pose, solo cambian las caras y el ángulo del bastón); Tin f190–f250; Tan f102–f156; Tan en primer plano f484–f511 |
| B6 | Cámara lenta de personajes | **Resuelto** (por D28) | Los vuelos «salen rápido, se cuelgan arriba y caen» (f318–f334: rival arriba, calcos, cae hacia el mostrador; f86–f96; f702–f716). No se promete cámara lenta falsa |
| B7 | Contactos sin peso ni lectura | **Resuelto** en 8 de 9 | Hay estrella en el punto en f82–f84 (K1), f170–f172, f314–f316, f576, f612–f614, f694–f696, f886–f888, con el golpeado ya reaccionando en f86, f174, f318, f578, f616, f698 y f890. Las distancias del control son 0,23–0,36 u (mi criterio de la v2 pedía ≤ 0,15 u con otra medida; se leen todas como contacto). El noveno, el bloqueo f548–f552, tiene la estrella sobre la cara de Tin (ver M2) |
| B8 | Gancho sin piernas y clave desordenada | **Resuelto** | Control G1: ninguna clave cruzada. En f314–f318 Tin sube con las piernas rectas y el rival vuela |
| B9 | Giros instantáneos | **Resuelto en lo que se ve** | No vi cuadro con lámina volteada a mitad de carrera. No pude mirar los giros de 3 f uno a uno |
| B10 | Decorado que tapa el contacto | **A medias** | Ya no hay carteles tapando las piernas; en f304–f312 el mostrador y la caja registradora tapan la carga del gancho de Tin (ver M5) |

## 3. Defectos nuevos y los que quedan de la v3

Gravedad: B bloquea presentar · A alta · M media · b baja.

### A (alta)

- **A1. Cuerpos clavados (la regla de la v2: ninguna pose idéntica más de 12 f).** Es lo que más le queda a la pieza, y el
  total pasa de 250 f (25 % del video) con alguno de los dos protagonistas en pose fija:

  | f | Quién | Qué se ve | Corrección (valores de partida) |
  |---|---|---|---|
  | **f752–f872 (121 f = 4,0 s)** | Tin y Tan | Tin con el bastón apoyado, Tan con el mazo al hombro; f762 y f846 son la misma pose. Cambian las caras y el bastón se inclina un poco. Mientras tanto el rival revive y camina (f786–f870) y **ninguno de los dos lo mira ni reacciona** | En el guion de `tin_en_s_004.js`, pistas `pose` de `tin` y `tan`: dos poses de reposo que se alternan cada 18–24 f, desfasadas 9 f entre los dos; `c` (cabeza) siguiendo al rival ±8°; en f786 (el rival se levanta) cara `sorpresa` 8 f en los dos y un paso atrás de 0,14 u de Tan; Tan baja el mazo de a poco de f800 a f850 |
  | f190–f250 (60 f) | Tin | Guardia con el lápiz, idéntica mientras el rival se levanta y camina | Mismo reposo vivo; en f214–f224 que gire la cabeza hacia donde se levanta el rival |
  | f442–f482 (40 f) | Tin | Bastón fijo mientras el rival se mueve en el mostrador | Cambio de apoyo cada 18–24 f y respiración ±2° |
  | f102–f156 (54 f) | Tan | De pie en primer plano; solo gira un poco la cabeza | Cambio de apoyo y un paso corto de guardia (0,14 u) en f130 |
  | f516–f546 (30 f) | Tin | Bastón en guardia, casi sin cambio | Hervor de ±2° cada 2 f en f538–f546 (pausa antes del bloqueo) |

- **A2. Tan en primer plano, f484–f511 (28 f): cuerpo, cara y boca fijos.** f486 y f504 son el mismo dibujo (boca abierta
  con la lengua, ojos cerrados, mano en la barbilla); solo se mueve la cámara en un deslizamiento corto. Es justo el defecto
  «boca abierta fija» de la v2 (B5) y la invitación («Suscríbete») va sin gesto de invitar. **Corrección:** alternar la cara
  (`risa` ↔ `curiosidad`) cada 10–12 f, y un gesto de la mano de f490 a f500 (mano de la barbilla a señalar a cámara);
  si el motor no tiene ese gesto en Tan, que sea un cabeceo de ±6° en `c` con ciclo de 14 f. Valores de partida.

- **A3. Rival tumbado que se desliza, f212–f216.** En f212 el cuerpo tumbado está a los pies de Tin y en f214 su cabeza
  ya está en el borde derecho (unos 160 px en 2 f; el control lo avisa como E1, «rival cortado en f213–f218»); en f218
  reaparece incorporándose junto al mostrador. Un cuerpo rígido que patina fuera de cuadro y vuelve se lee como tirón, no
  como el rival que se arrastra. **Corrección:** en el guion, pista `pos` del rival, repartir f205–f218 en 3 tramos con
  gateo (pose de manos y rodillas, un paso cada 6 f) o dejar que ya esté en el mostrador desde el corte f184. Si no se
  quiere tocar, bajar la velocidad a ≤ 0,3 u/f y que no se salga del cuadro.

### M (media)

- **M1. Tin f376–f410:** sube y baja unos 0,2 u cada ~6 f (f376, f384, f388, f396, f400, f406) mientras se desplaza solo
  unos 0,3 u hacia el lado contrario del rival (cabeza de x 90 a 40). Es un «retroceso» (permitido), pero con tanta
  amplitud parece un rebote nervioso, no pasos. No lo pude ver cuadro a cuadro. **Corrección:** amplitud a 0,06 u, un
  paso de 0,4 u cada 8 f (como M3 de la v2), o dejarlo quieto en reposo vivo.
- **M2. Bloqueo, f548–f552:** la estrella y las gotas de tinta caen sobre la cara de Tin (f552: bastón vertical delante
  de la cara, gotas junto a las gafas). Se lee como que el rival le da en la cara, aunque es el choque de espada y bastón;
  el control lo mide a 0,54 u de la cabeza de Tin. **Corrección:** estrella 0,3 u por encima del cruce (en la punta del
  bastón) y el bastón girado 20° hacia fuera para que no tape el rostro.
- **M3. Remate f694–f716:** Tin y Tan siguen a ambos lados del rival; las armas se juntan en el pilar y se lee como
  doble golpe, pero la regla 2.1.3 («nunca entre sí») solo se cumple por la altura del rival (sube al televisor). Aviso,
  no bloqueo: si se rehace algo, apilarlos del mismo lado (M9 de la v2).
- **M4. Onda de f728–f748:** Tin y Tan se quedan agachados e iguales durante ~20 f. **Corrección:** empuje de 0,2–0,35 u
  hacia fuera y vuelta con dos pasos en f736–f748; cara `sorpresa`.
- **M5. Gancho, f304–f312:** Tin está detrás del mostrador y de la caja registradora, con la cabeza asomando, y el rival
  encima de su cabeza (f312). La anticipación del gancho no se lee; el golpe (f314–f318) sí. **Corrección:** subir la
  cámara 0,3 u o mover a Tin 0,4 u a la izquierda del mostrador en f302–f312.
- **M6. Rival junto a Tin, f646–f664 (E3 en f660):** la cabeza pequeña del rival queda pegada detrás del cuello de Tin y
  se lee como un bulto en su hombro. **Corrección:** `pos` del rival 0,8 u a la izquierda (o 0,6 u más cerca de la cámara)
  en f644–f668.
- **M7. Tan fuera de cuadro f184–f482 (≈ 10 s, salvo f303, avisado en D32) y f512–f576:** es un protagonista y no hace nada
  en la mitad del video. No es un defecto del movimiento; se lo paso al director creativo como decisión de reparto.
- **M8. Cruce de Tan, f584–f588:** la cabeza de Tan queda justo delante del torso de Tin con la de Tin encima; el control
  no lo avisa. Separar 0,3 u en z en f583–f588.

### b (baja)

- **b1.** Los calcos del rival en f320–f334 son anchos y se pegan al mostrador; leerlos mejor con menos opacidad.
- **b2.** El lápiz que cae en f944–f950 se ve como un punto naranja; agrandarlo 1,5 veces.
- **b3 (aviso a continuidad, no mío).** El empalme del bucle: en f984 el lápiz está en la misma posición que en f0 (muy
  bien: el bumerán entra con el mismo trazo), pero el cuarto está destrozado en f984 y entero en f0. Es el punto D6.

## 4. Qué está bien (no tocar)

- El bucle del lápiz: Tan lanza en f968–f974 y la posición del lápiz en f984 casa con f0 a 2 o 3 px.
- Carreras y vuelos: se ven, tienen peso y recorren distancia; el espectador sabe quién va adónde.
- La estrella nace en el punto de contacto y el golpeado reacciona (K1, K2, K3, K4, K5, remate y K6).
- La pausa antes de cada golpe (f564–f572, f874–f884) y el corte de impacto (f100, f336, f562).
- El gancho y su vuelo (f314–f334) y el último golpe (f886–f898, con onda en el suelo).

## 5. Veredicto

Ningún defecto bloqueante de la queja del dueño (carreras, vuelos, golpes) sigue vivo: la v3 resolvió B1, B2, B6, B7, B8
y B9. Lo que no cumple es el criterio que dejé escrito para firmar (que no haya cuerpos clavados): **A1 (4 s con los
dos protagonistas en pose fija, y otros 150 f de uno de los dos), A2 (la invitación sin gesto ni cara) y A3 (el rival que
patina fuera de cuadro)** juntos no se pueden presentar como trabajo de alta calidad. Se arreglan en el guion, sin créditos.

Veredicto: CAMBIOS

Firma: director de animación, 2026-11-27.
