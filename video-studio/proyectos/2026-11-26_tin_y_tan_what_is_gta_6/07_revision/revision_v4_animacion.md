# Revisión de animación — short 4, versión 4 (`tin_y_tan_short04_v4.mp4`)

- **Pieza revisada:** `06_final/tin_y_tan_short04_v4.mp4`, sha256 `f4c8224b3707` (12 primeros caracteres), 986 fotogramas a 30 f/s.
  **No pude calcularlo ni reproducir el video** (no tengo consola en esta sesión): el sha es el dato que dio producción.
- **Firma:** director de animación, 2026-11-26.
- **Convención de nombres:** Tin = el de la gorra naranja (atrapa el lápiz en f0); Tan = el verde de la bufanda; el rival = el
  garabato negro. f = fotograma de la numeración de las tiras.

## 1. Qué miré y qué no pude comprobar

Miré:
- Las 21 tiras completas (`rev_v4/tira_01` a `tira_21`, 1 de cada 2 fotogramas, f0–f984).
- 31 fotogramas compuestos a resolución completa de `06_final/fotogramas/`: f120, f138, f180, f198, f210, f216, f240, f264,
  f294, f312, f318, f324, f366, f390, f450, f474, f486, f504, f546, f552, f588, f618, f630, f636, f648, f654, f660, f702, f738,
  f762, f786, f804, f822, f846, f888, f948, f972.
- `07_revision/control_encuadre_v4.md` (PASA, 6 avisos), mi `revision_v3_animacion.md` y los comentarios «v4» y la función
  `vivo` de `tin_en_s_004.js` (solo las líneas citadas; no ejecuté nada).

No pude comprobar:
- (a) El sha256 ni el movimiento real: con 1 de cada 2 fotogramas los giros de 3 f y el balanceo del reposo vivo se ven por
  la diferencia entre poses, no cuadro a cuadro. Lo que llamo «reposo casi quieto» es una medida visual en reposo, no del
  video en movimiento.
- (b) La sincronía con el audio (no es mío).
- (c) Los fotogramas intermedios de 6 en 6 que no abrí (por ejemplo f696 exacto del remate): lo leo en la tira.

Sobre los avisos del control. **E4:** el rival sobre la cabeza de Tin en f85 y f295 y sobre la de Tan en f106–f107 y f631–f632 son
vuelos y trepadas del rival, los miré y no se leen como bulto (ver b1). **M5:** Tin «clavado» en f648 y f805: f805 sí es un
reposo muy poco marcado (ver M1 nueva); f648 es el tramo del rival junto a Tin (ver M6). Los demás avisos (E1 f129–f145, E2, M2
de Tan fuera de cuadro f303) son entradas por el borde y vuelos: bien.

## 2. Cambios que declaró producción: comprobación

| Cambio declarado | Cierto | Prueba |
|---|---|---|
| Tin se detiene antes del mostrador y el rival se le lanza desde arriba antes del gancho | **Sí** | f288–f296: Tin corre y frena a la izquierda del mostrador; el rival cae del borde superior sobre el mostrador. f312: Tin a cielo abierto, con el lápiz adelantado y el rival sentado en la caja: la anticipación se lee. f314–f316 estrella, f318 el rival sale volando |
| La patada ya no atrae al rival hacia Tan | **Sí** | f172–f180: el rival sale despedido hacia el mostrador de Tin y queda tendido a la derecha; Tan queda en su sitio, de pie, con cara de risa (f180) |
| El rival cae con la cabeza lejos de Tin y no gira tendido | **Sí** | f180–f216: cuerpo tendido en horizontal, sin giro, con la cabeza a la derecha bajo el mostrador |
| Tin espera el remate en el pasillo del fondo | **Sí** | f624–f700: Tin a la izquierda en el pasillo del fondo, Tan a la derecha, el rival entre los dos |
| Tan gesticula y cambia de cara al invitar a suscribirse | **Sí** | f484–f510: mano a la barbilla con risa, brazo extendido con cara neutra y ojos abiertos (f492–f502), de vuelta a risa con mano a la barbilla (f504–f510) |
| Dos pasos bajos en vez de tres rebotes tras el gancho | **Sí** | f376–f410: pasos con subida baja y un solo apoyo por paso; ya no es el rebote nervioso de la v3 |

## 3. Defectos de la v3: estado en la v4

| # | Defecto de la v3 | Estado | Prueba |
|---|---|---|---|
| A1 | Cuerpos clavados (Tin y Tan f752–f872; Tin f190–f250, f442–f482, f516–f546; Tan f102–f156) | **A medias (rebajado a M, ver M1 y M2 nuevas)** | **Resuelto** en f752–f872: f762 (Tin ríe, bastón en diagonal, Tan con el mazo bajo) frente a f786 (los dos con cara de sorpresa), f804, f822 y f846: el mazo de Tan sube de a poco, el bastón de Tin cambia de ángulo, las caras cambian, y el rival se levanta y camina entre los dos. **Resuelto** en f442–f482: f450 frente a f474, Tin cambia el ángulo del bastón y el apoyo. **No resuelto del todo** en Tan f102–f156 (f120 y f138: mismo dibujo, mismos pies, solo gira un poco la cabeza) y Tin f190–f250 (f198, f210, f216 y f240: mismos pies y mismo lápiz; solo un balanceo de pocos píxeles) |
| A2 | Tan en primer plano, f484–f511, cuerpo y cara fijos | **Resuelto** | f486 y f504 son el mismo dibujo, pero entre medias hay un gesto completo de 10 f (brazo extendido, cara neutra, ojos abiertos) y cambio de cara; la invitación ya lleva gesto |
| A3 | Rival tumbado que se desliza fuera de cuadro, f212–f216 | **Resuelto** | La cabeza del rival queda siempre dentro del cuadro (a la derecha, bajo el mostrador) y no hay salto de 160 px: f198 y f210, f216. El control ya no avisa E1 en ese tramo (solo f129–f145, que es la entrada por el borde) |
| M1 | Tin f376–f410 rebota con amplitud de más | **Resuelto** | f376–f410: dos pasos bajos; f390 muestra el apoyo y la zancada, sin salto |
| M2 | Bloqueo f548–f552, estrella sobre la cara de Tin | **Resuelto** | f546 y f552: el choque está entre el bastón y la espada del rival, del lado del rival; las gotas salen hacia él; la cara de Tin queda libre |
| M3 | Remate f694–f716: Tin y Tan a los lados del rival | **Sin cambio (aviso)** | f702: las armas de Tin y Tan se cruzan en el pilar y el rival sale hacia el televisor; se lee como doble golpe, pero con las armas casi tocándose (ver M3 nueva) |
| M4 | Onda f728–f748: agachados e iguales | **Resuelto** | f738: los dos se echan hacia atrás con cara de sorpresa y la tira f720–f750 muestra empuje y vuelta, no una pose quieta |
| M5 | Gancho f304–f312: Tin tapado por el mostrador | **Resuelto** | f312 y tira_07: Tin se ve entero, a la izquierda del mostrador, y la anticipación se lee |
| M6 | Rival pegado al hombro de Tin f646–f664 | **A medias (b)** | f660: el rival está separado de Tin, delante del pilar. f648 y f654: su cabeza queda una cabeza a la derecha de la de Tin y cruzada por la punta del bastón, se sigue leyendo cerca (ver b2) |
| M7 | Tan fuera de cuadro f184–f482 y f512–f576 | **Sin cambio (no es de animación)** | Sigue fuera. Decisión de reparto para el director creativo; Tan ahora sí actúa en su primer plano |
| M8 | Cruce de Tan f584–f588, cabeza delante del torso de Tin | **Resuelto** | f588: Tan cruza por delante con claro de separación entre los dos |
| b1 | Calcos del rival f320–f334 anchos y opacos | **Resuelto** | f324: calcos claros y más transparentes que en la v3 |
| b2 | Lápiz que cae f944–f950 como un punto naranja | **No resuelto** | f948: sigue siendo un palito fino de unos 10 px; hay que agrandarlo (ver b3 nueva) |
| b3 | Empalme del bucle: lápiz igual, cuarto destrozado en f984 y entero en f0 | **Sin cambio (continuidad, no mío)** | f0 y f984: el lápiz casa; el cuarto no. Es el punto D6 que lleva continuidad |

## 4. Defectos nuevos y los que quedan

Gravedad: B bloquea presentar · A alta · M media · b baja. **No hay B ni A.**

### M (media)

- **M1 nueva. Reposos todavía muy poco marcados, Tan f102–f156 (54 f) y Tin f190–f250 (60 f).** En f120 y f138 Tan es el mismo
  dibujo con los mismos pies; en f198, f210, f216 y f240 Tin conserva los mismos apoyos y el mismo lápiz. El reposo vivo
  (ciclo de 22 f) está activo pero su amplitud es de pocos píxeles: se lee como respiración, no como cambio de peso. No son
  estatuas del todo, pero es la deuda de A1. **Corrección (valores de partida, en `vivo` del motor o por pistas):**
  - Amplitud de la inclinación del torso y de la cadera ×2.
  - Un cambio de apoyo visible cada 18–24 f (peso de una pierna a la otra, 0,1 u).
  - Tan en f130 gira la cabeza hacia el estante que cae y da un paso corto de 0,14 u.
  - Tin en f214–f224 gira la cabeza hacia donde se levanta el rival.
- **M2 nueva. Tin y Tan f786–f870, con la cara como único cambio claro.** f804, f822 y f846: Tin con el mismo cuerpo y Tan con el
  mazo ya arriba y quieto; se mueve el rival y cambian las caras. Está aceptable como «respiro» de unos 3 s, pero el
  control aún marca Tin clavado en f805. **Corrección:** el mismo cambio de apoyo cada 18–24 f; en f850–f862 Tan baja el
  mazo 6° y Tin gira la cabeza hacia el rival (anticipa el último golpe).
- **M3 nueva. Remate f694–f702: el bastón y el mazo se cruzan.** En f702 las dos armas se juntan en el pilar y forman una X antes
  de que el rival salga hacia arriba; a 1 de cada 2 fotogramas se puede leer como si Tin y Tan chocaran sus armas.
  Es el M3 de la v3, que sigue vivo. **Corrección:** abrir 0,3 u la distancia en el momento del contacto (que cada arma llegue por
  su lado y el rival esté entre las puntas), o hacer el remate de a uno con la estrella más clara.

### b (baja)

- **b1. E4 del rival sobre la cabeza de Tin en f295 y sobre la de Tan en f631–f632.** En f294 la pierna del rival pasa detrás del
  gorro de Tin; en f630 su cabeza cae sobre el mazo de Tan. Se leen como caída y trepada, no como bulto, pero si se
  toca, separar 0,2 u en z.
- **b2. Rival junto a Tin, f646–f656.** La cabeza del rival queda a una cabeza de la de Tin y cruzada por la punta del bastón.
  Mover el rival 0,5 u a la derecha en esos fotogramas.
- **b3. Lápiz que cae, f944–f950:** sigue siendo un palito de unos 10 px. Agrandar 1,5 veces (es el b2 de la v3).
- **b4. Cuerpo tendido, f176–f216.** El cuerpo del rival, tendido y casi todo negro, se lee en f180 y f216 casi como una sombra o un
  palo largo; la cabeza sale del cuadro en f180. Darle algo de contorno claro o un pie a la vista.
- **b5. Polvo de la onda, f738.** Los círculos grises del polvo en las piernas de Tin y Tan se leen como ruedas de bicicleta. Es
  una decisión de estilo, la dejo al director de arte.

## 5. Qué está bien (no tocar)

- Carreras, vuelos y estrellas en el punto de contacto: se leen, tienen peso y recorren distancia (control M1 y M3 en «bien»).
- Gancho: Tin frena, el rival cae del techo, anticipación en f312, golpe en f314–f316, vuelo con calcos claros f318–f334.
- Tan en primer plano f484–f510: tres tiempos (risa con mano en la barbilla, brazo extendido con cara neutra, vuelta a risa).
- El rival cae lejos de Tin (f180) y se levanta y camina entre los dos en f786–f870.
- Dos pasos bajos de Tin f376–f410; bloqueo f546–f552 con la cara de Tin libre; onda f720–f750 con empuje.
- Pausas antes de cada golpe (f564–f572, f874–f884) y cortes de impacto (f100, f336, f562).
- Cara del rival en f366 y f450–f474: actuación clara con cambio de expresión.

## 6. Veredicto

Los seis cambios que declaró producción son ciertos y se ven en las tiras. De la v3 quedan resueltos A2, A3, M1, M2, M4, M5, M8
y b1, y A1 queda rebajado de «alta» a «media» porque el tramo más largo (f752–f872) ya actúa y lo que queda son dos
reposos de unos 2 s con poca amplitud (M1 nueva), no estatuas de 4 s con los dos protagonistas. No hay defecto B ni A.
Dejo anotados M1, M2 y M3 nuevas y b1–b5 para la próxima vuelta, que no impiden presentar la pieza al dueño.

Veredicto: APROBADO

Firma: director de animación, 2026-11-26.
