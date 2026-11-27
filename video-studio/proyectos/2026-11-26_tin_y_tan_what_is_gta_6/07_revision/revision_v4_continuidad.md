# Revisión de continuidad y calidad — short 4 de Tin & Tan, versión 4

- **Fecha:** 2026-11-26 · **Quién:** supervisor de continuidad · **Qué se revisó:** final v4
  (`06_final/tin_y_tan_short04_v4.mp4`, 1080×1920, 30 f/s, 986 f = 32,87 s).
- **sha256 (12 primeros):** `f4c8224b3707` (calculado por mí con `sha256sum`; coincide con el de producción).
- **Cómo:** los 986 fotogramas extraídos por mí a resolución completa en una carpeta temporal fuera del repositorio;
  20 de las 21 tiras de producción (todas menos la 18); montajes fotograma a fotograma y recortes a tamaño real
  (1 píxel = 1 píxel) de cada punto N1–N17, de los cuatro avisos E4, de los dos M5, de cada golpe y de los dos cortes de
  firma; tarjetas y subtítulos leídos a tamaño real; `revisar_texto.py` en los dos `.srt`; `postpro.py destellos`;
  lectura de `color_v4.txt` y `control_encuadre_v4.md`; líneas marcadas «v4» del guion.
- **Lo que NO pude comprobar:** no oí el audio (A7, el «it» que sobra según el reconocedor y «cada corte con su
  sonido» siguen sin firma de oído). No releí las fuentes de los datos ni audité `licencias.md`. No comparé plano por
  plano con la referencia (A1). El tramo f816–f862 (tira 18, respiro) lo vi solo por muestreo (f812, f830, f860). No
  volví a correr `revisar_color.py` ni a medir contraste: copio lo de `color_v4.txt`; la tarjeta y la tinta son las
  mismas que medí en la v3 (14,9:1). No reabrí las imágenes de `referencias/`; la identidad la comparé contra las
  listas de comprobación de las tres fichas. No toqué `controles.md` ni `firmas.md` (encargo: un solo archivo).
  Las medidas en píxeles son a ojo sobre los recortes (van con «≈»). Los fotogramas se citan como `fNNN`
  (segundo = f / 30).

**Resumen:** la v4 quita el defecto bloqueante de la v3 (ya no hay pies del rival sobre la cara de Tin ni cabeza
hundida en el mostrador) y resuelve de verdad N2, N3, N5, N8 y N13. No la firmo porque el rival todavía toca la
cabeza de Tin en tres momentos que se ven a velocidad normal: la madeja pegada a su visera 14 fotogramas tras el salto
desde el estante (N4, que cambió de forma), la madeja sobre su cara en la pausa de impacto del remate (nuevo, y es el
golpe más importante del video) y el puño sobre su gorra y su visera en el mostrador (resto de N1). La prueba E4 del
control automático no vio los dos primeros. Todo es render por código: corregir cuesta 0 créditos.

---

## 1. Identidad contra las fichas

| Personaje | Rasgo | ¿Está? | Evidencia |
|---|---|---|---|
| Tin | Cabeza naranja, contorno tinta, lentes con brillo, lápiz amarillo con goma roja | Sí | f30, f547, f693, f957 |
| Tin | Gorra con visera clara, botón y dos costuras | **A medias (igual que en v2 y v3)** | Botón sí. En la pelea la visera es una barra marrón oscura y no se ven costuras (f547, f693) |
| Tin | Cara legible | **No en f694–f696**; gorra tapada en f892–f905 | Ver V2 y V7 |
| Tan | Cabeza verde azulado, rodete con cinta, bufanda mostaza con dos puntas | Sí | f30, f484, f612, f957 |
| Tan | Cara legible | Sí | En el cruce (f582–f584) y en el mazo (f612–f640) se le ve entera |
| Rival | Madeja, dos huecos de papel, sin boca ni pupilas, rizo sin punto | Sí | f58, f164, f313, f547, f693, f812, f885 |
| Rival | Sin nombre en pantalla | Sí | Ninguna tarjeta ni subtítulo lo nombra |
| Rival | Cuerpo de palitos; escalones de tamaño | Sí | f58 grande → f547 → f693 pequeño → f812 |
| Rival | Solo tinta, sin color propio | Sí, con el artificio visible | Disco de papel detrás de la madeja (N7) |
| Rival | «Se borra empezando por la cabeza» | **No (igual)** | f898–f902: el cuerpo se va en gotas y la madeja es lo último |

## 2. Estado de N1–N17 de la v3

| # | Qué era | Estado en la v4 | Fotograma que lo prueba |
|---|---|---|---|
| N1 (B) | Rival sobre la cara de Tin y cabeza de Tin hundida en el mostrador, f289–f313 | **Resuelto como bloqueante.** Tin frena antes del mostrador y su cara se ve entera todo el tramo. **Queda un resto de gravedad A (V3)** | f296–f313: Tin de pie delante del mostrador, cabeza completa. Resto: f292–f301 |
| N2 (A) | Salto de 216 px en la patada, f166–f171 | **Resuelto** | f168→f169: el rival no cambia de sitio; f170–f171: la madeja lejos del rodete de Tan. Nota b: f172–f173 las piernas del rival despedido cruzan las canillas de Tin justo antes de que Tin salte |
| N3 (A) | Giro de 180° con salto, f212→f213 | **Resuelto** | f206–f217 sin giro ni salto; se levanta dentro del cuadro f216–f230 |
| N4 (A) | Rival por encima de Tin, f644–f660 | **No resuelto: cambió de forma (V1)** | Ya no pasa por encima de Tin, pero cae con la madeja contra su visera f648–f661 y antes roza la cabeza de Tan f644–f645 |
| N5 (A) | Gotas sobre la cara de Tin en el bloqueo, f548–f561 | **Resuelto en lo principal** | f552–f561: las gotas van hacia el rival y hacia abajo; ninguna sobre la cara. Nota b: la estrella roza la mejilla de Tin en f549–f551 |
| N6 (A) | Puño sobre la gorra de Tin, f66–f69 | **A medias (V4, baja a M)** | f66: la gorra de Tin contra el antebrazo del rival; f67–f69: el puño toca la punta de la visera |
| N7 (M) | Disco de papel detrás de la madeja | **No resuelto** | f704–f714 recorte redondo en la llama; halo claro también en f648–f662 y f694–f698 |
| N8 (M) | Cabeza de Tin cortada en la pausa del remate | **Resuelto el encuadre** | f684–f693: cabeza entera. El acercamiento que pedí en la v3 produjo V2 |
| N9 (M) | Cabeza de Tan sobre media cara de Tin en el cruce | **Mejor (b)** | f582–f584: Tin salta y su cara queda libre; las cabezas quedan apiladas 3 f |
| N10 (M) | Cambio de lado en el corte de cierre | **Igual, declarado (D26)** | f953→f957 |
| N11 (M) | El lápiz pasa de Tan a Tin en el corte sin entrega | **Igual** | f29 (lo tiene Tan) → f30 (lo tiene Tin) |
| N12 (M) | Madeja detrás de la tarjeta; cabeza de Tin en la tapa del mostrador | **No resuelto** | f372–f400: la madeja queda tapada por la tarjeta «GTA 6»; f376–f377: la tapa del mostrador le cruza el mentón a Tin |
| N13 (M) | El rival tendido tapa las piernas de Tin | **Resuelto** | f186–f214: las piernas del rival acaban a ≈ 40–80 px de los pies de Tin, cabeza lejos |
| N14 (M) | No se borra empezando por la cabeza | **No resuelto** | f898–f902 |
| N15 (b) | Cabezas del rival y de Tan apiladas | **A medias (b)** | f154–f156: la madeja toca y queda detrás de la cabeza de Tan 3 f |
| N16 (b) | Mango sobre la visera, gota en el lente, lámpara como ojo | Mango y gota: no los volví a encontrar (f594, f898, f902). La lámpara sigue | f719–f749 |
| N17 (b) | Marco de la tarjeta de respuesta en y ≈ 358 | **Resuelto en el límite** | f920: borde superior en y ≈ 380 |

## 3. Avisos del control automático, mirados en imagen

| Aviso | ¿Defecto? | Lo que se ve |
|---|---|---|
| E4 Tin f85 | No | La extremidad del rival queda a ≈ 100 px de la cabeza de Tin, a la izquierda |
| E4 Tin f295 | **Sí (V3)** | El puño del rival dibujado encima de la gorra de Tin |
| E4 Tan f106–f107 | Sí, M (V5) | La madeja del rival caído pegada al borde de la cabeza de Tan; dura hasta ≈ f120 |
| E4 Tan f631–f632 | Sí, M (V6) | Los pies del rival, que trepa el estante, tocan el rodete de Tan (f630–f633) |
| E1 rival f129–f145 | No | Sale por el borde derecho al levantarse |
| M2 Tan f303 | No | Fuera de cuadro |
| M5 Tin f648 | Sí: forma parte de V1 | Tin inmóvil mientras tiene la madeja en la visera |
| M5 Tin f805 | No | Respiro; Tin sonríe con el bastón, quietud breve |

**La prueba E4 no basta todavía:** no marcó f648–f661 ni f694–f698, que son los dos peores. Compara el cuerpo del rival
con la cabeza; hace falta comparar también **la madeja del rival** con la cabeza de Tin o de Tan **ampliada con la
visera, el rodete y el arma**, y que sea fallo, no aviso, cuando dura 3 fotogramas o más.

## 4. Defectos de la v4, por fotograma

Gravedad: **B** bloquea presentar · **A** alta · **M** media · **b** baja. Los números de corrección son **valores de
partida**. Archivo: `video-studio/motor_de_accion/guiones/tin_en_s_004.js`.

| # | Fotogramas | Gravedad | Qué se ve | Corrección (valor de partida) |
|---|---|---|---|---|
| V1 | f644–f661 (18 f) | **A** | El rival salta del estante: en f644–f645 sus piernas rozan el rodete y la frente de Tan; cae con **la madeja contra la visera y el bastón de Tin** de f648 a f661 (14 f, 0,47 s); en f650–f654 el rizo queda encima de la visera. Tin no se mueve (M5). Sin sonido se lee «le dio un cabezazo» | Línea 136: caída en `[K5 + 36, [0, 0, ZF]]` → x ≈ +0,6; punto alto `[K5 + 26, [1.9, 1.7, -4.9]]` → x ≈ 2,6 para no cruzar la columna de Tan. Línea 99–100: Tin 0,4 u más a la izquierda en K5 + 36. Meta en pantalla: ≥ 150 px entre el borde de la madeja y la visera. Que Tin reaccione (paso atrás) en K5 + 36 |
| V2 | f694–f698 (5 f) | **A** | Remate, el golpe principal: en la pausa de impacto (f694–f696, tres fotogramas casi iguales) **la madeja del rival tapa la visera y toca la mejilla de Tin**; en f697–f698 sale despedida rozando la copa de su gorra. Nuevo en la v4 | Línea 101: `[KR, [-1.42, 0, ZF], 'salto']` → x ≈ −1,8 (Tan, línea 72, puede quedarse en 1,42: su cabeza queda libre). Línea 136: salida `[KR + 6, [0, 1.3, -6.4]]` → x ≈ +0,3 para que suba entre los dos y no sobre Tin |
| V3 | f292–f301 (10 f) | **A** | Resto de N1: la pierna del rival cruza el borde de la gorra de Tin (f292–f293); **el puño del rival sobre la gorra** (f294–f295) y en la punta de la visera (f296–f301). Además la madeja queda detrás de la tarjeta del dato de f291 a f303 | Caída del rival en el mostrador 0,4 u más a la derecha (x ≈ 2,6) o Tin en `[K3 - 7, [0.9, 0, -2.8]]`; pose del rival sobre el mostrador con el brazo hacia atrás, no extendido hacia Tin |
| V4 | f65–f69 | M | Resto de N6: en f65→f66 el rival cambia de lado y de pose y se corre ≈ 140 px en un fotograma; la gorra de Tin queda contra su antebrazo (f66) y el puño toca la punta de la visera (f67–f69) | Rival 0,3 u más lejos de Tin en f66–f69 o guardia con los puños más bajos; repartir el giro en 2–3 f |
| V5 | f106–f120 | M | El rival, despedido por Tin, cae al pie del estante con la madeja pegada a la cabeza de Tan ≈ 14 f. No la ataca, pero las dos cabezas se tocan | Tan 0,4 u más a la izquierda en P5 o el rival 0,4 u más adentro del estante |
| V6 | f630–f633 | M | El rival trepa el estante justo detrás de Tan y sus pies tocan el rodete | Que trepe 0,5 u más a la derecha |
| V7 | f892–f905 | M | La tarjeta «GTA 7: not announced» tapa media gorra de Tin (en f874–f878 la tarjeta anterior ya le toca la copa) | Bajar la cámara de P20 o encuadrar a Tin ≈ 60 px más abajo |
| V8 | f82–f85 | M | Golpe 1: la estrella queda pegada a la mejilla y al mentón de Tin 4 f; en f82 la madeja roza su gorra | Punto de la estrella a 0,6 del camino hacia el rival |
| V9 | f100–f101 | b | Mancha marrón grande y desenfocada (un trozo de la gorra de Tin, gigante) en la esquina inferior derecha del plano de impacto | Ocultar a Tin en P4 |
| V10 | f314–f316 | b | Golpe 3: el brazo de Tin cruza su propia cara 2 f y la estrella toca su gorra (igual que en la v3) | — |
| V11 | f262; f618–f624 | b | La cabeza de Tin toca el borde izquierdo al esquivar; entra cortado por el borde en el golpe 5 | — |
| V12 | f157–f158; f626–f628; f874 | b | El pie del rival toca las manos de Tan tras el corte; un bloque gris pasa por delante del cuerpo de Tin; el bastón cruza la cara de Tin 1 f | — |

Siguen además N7, N10, N11, N12 y N14 (M) y N9, N15 y la lámpara de N16 (b), ver sección 2.

## 5. Texto y cifras (leídos a mano sobre los fotogramas, a tamaño real)

| Texto en pantalla | Fotograma leído | Resultado |
|---|---|---|
| «GTA 7?» / «Facts, Checked» | f20, f970, f985 | Correcto; 4 palabras; mayúsculas bien |
| «GTA = Grand Theft Auto» | f120 | Correcto |
| «a game series · since 1997» | f230 | Correcto |
| «made today by Rockstar Games» | f290 | Correcto |
| «GTA 6» / «out since Nov 19, 2026» | f400 | Correcto |
| «the sixth numbered game» | f460 | Correcto |
| «rated M · 17 and over» | f580 | Correcto |
| «from GTA 5 to GTA 6» | f640 | Correcto |
| «13 years, 63 days» / «GTA 5: Sep 17, 2013» / «GTA 6: Nov 19, 2026» | f800 | Correcto |
| «GTA 7:» / «not announced» / «as of Nov 26, 2026» | f920 | Correcto para hoy, 26. Se recompone el día de publicar |

- **Subtítulos grabados en español (12), leídos uno por uno** (f40, f100, f200, f280, f400, f450, f520, f580, f650,
  f780, f880, f920): «¿Habrá un GTA 7?» · «GTA es Grand Theft Auto:» · «una serie de juegos que empezó en 1997» ·
  «y que hoy hace Rockstar Games.» · «GTA 6 salió el 19 de noviembre de 2026.» · «Es el sexto juego numerado.» ·
  «Suscríbete. Aquí comprobamos los datos.» · «Clasificación M: mayores de 17.» · «De GTA 5 a GTA 6:» · «trece años y
  sesenta y tres días.» · «¿Y GTA 7?» · «Rockstar no ha anunciado ninguno. Hasta hoy.» Sin errores de ortografía,
  tildes ni signos. **T10 dice «Hasta hoy.»**, como aprobó el dueño. Todos los nombres propios con mayúscula. Un solo
  subtítulo por fotograma en los cambios que miré (f170→f171, f315→f316 y f888); los demás cambios no los repasé.
- **`.srt`:** los dos coinciden con lo grabado. No van en la entrega (regla del dueño de hoy); cuenta lo grabado.
- **Cifra recalculada:** 17 de septiembre de 2013 → 19 de noviembre de 2026 = 13 años + 13 + 31 + 19 = 63 días.
  Entera: no lleva «≈». Igual en tarjeta, subtítulo y `.srt`. «Sexto», «17» y «1997» coinciden.
- **`revisar_texto.py`** (corrido por mí): español PASA, 0 errores; inglés PASA, 0 errores; ningún aviso.
- **`postpro.py destellos`** (corrido por mí): ningún segundo pasa de 3 (2 cambios fuertes en total).
- **Color** (copiado de `color_v4.txt`, no medido por mí): ≈ 90 % dentro de la paleta; luminosidad ± 2 % y saturación
  ± 2 % entre segundos.
- **Miniatura** (`06_final/miniatura.png`): 1080×1920; «GTA 7?» / «Facts, Checked» dentro de la zona útil; 4 palabras;
  no da la respuesta; es el mismo cuadro que f0.
- **Nada del juego ni marcas como objeto:** cumplido (televisor en blanco, cajas lisas, mando genérico).

## 6. Reglas duras

| Regla | Estado | Evidencia |
|---|---|---|
| El rival nunca alcanza ni pasa por encima de Tin o de Tan | **No se cumple en lo que se ve** | V1 (f644–f661), V2 (f694–f698), V3 (f292–f301); en menor grado V4, V5 y V6. Mejor que en la v3: ya no hay cuerpo del rival sobre la cara de Tin fuera de V2 |
| Ningún rojo sobre el rival | Se cumple | f704–f716: el disco de papel lo impide (N7); f786–f873: las llamas del suelo quedan a los lados |
| Nadie golpea a un caído | Se cumple | f186–f214 Tin no golpea; f600–f611 el rival de pie antes del mazo; f885 de pie antes del golpe 6 |
| Tin y Tan no pelean entre sí | Se cumple | — |
| Sin armas de fuego ni sangre | Se cumple | Bastón, espada y mazo de tinta; gotas negras |
| Máximo 3 destellos por segundo | Se cumple | `postpro.py destellos` |

## 7. Preguntas fijas (cap. 11, regla 20)

- ¿Movimiento y corte antes del segundo 1? Movimiento sí (f0–f10, el lápiz vuela); el primer corte cae en 1,0 s (f30).
- ¿Plano héroe cerca de la mitad? No: en la mitad está la suscripción (f483–f511); la explosión, en ≈ 24 s.
- ¿Picos y respiros? Sí (respiro f750–f873).
- ¿Final que empalma con el inicio? Personajes, lápiz, texto y cámara sí (f985 → f0); el fondo no (D6 declarada).
- ¿Cada corte con su sonido? Sin comprobar.
- ¿Algo genérico? No.
- ¿Más de 3 destellos por segundo? No.
- ¿Todo con licencia? No lo audité en esta vuelta.

## 8. Veredicto por tramo

| Tramo | Personaje fiel | Emoción se lee | Cámara | Actuación | Continuidad | Defectos | Veredicto |
|---|---|---|---|---|---|---|---|
| Firma y portada (f0–f29) | Sí | Sí | Bien | Bien | N11 | — | APROBADA |
| Entrada y pisotón (f30–f69) | Sí | Sí | Bien | Puño en la visera | V4 | — | CORREGIR EN CÓDIGO |
| Golpe 1 y estante (f70–f156) | Sí | Sí | Bien | Conecta | V5, N15 | V8, V9 | APROBADA con nota |
| Golpe 2 y postes (f157–f235) | Sí | Sí | Bien | Conecta | Bien | — | APROBADA |
| Esquiva, carrera y golpe 3 (f236–f337) | Sí | Sí | Bien | Puño sobre la gorra | V3 | V10 | CORREGIR EN CÓDIGO |
| Fecha y bastón (f338–f482) | Sí | Sí | Bien | Bien | N12 | — | APROBADA con nota |
| Suscripción (f483–f511) | Sí | Sí | Bien | Bien | Bien | — | APROBADA |
| Bloqueo y golpe 4 (f512–f598) | Sí | Sí | Bien | Bien | N9 | — | APROBADA |
| Golpe 5 (f599–f640) | Sí | Sí | Bien | Bien | V6 | V11 | APROBADA con nota |
| Salto del rival, carga y remate (f641–f718) | Cara de Tin tapada en el remate | Confusa en f648–f661 | Bien | Rival contra Tin | V1, V2, N7 | — | CORREGIR EN CÓDIGO |
| Explosión y respiro (f719–f873) | Sí | Sí | Bien | Bien | Bien | — | APROBADA |
| Golpe 6 e implosión (f874–f905) | Gorra tapada por la tarjeta | Sí | Tin muy arriba | Bien | N14 | V7 | APROBADA con nota |
| Final y cierre (f906–f985) | Sí | Sí | Bien | Bien | N10 | Sello de fecha | APROBADA con nota |

## 9. Lo que impide firmar y lo que queda antes de publicar

1. **No hay defectos B.** El de la v3 quedó resuelto.
2. **V1, V2 y V3 (A):** tres momentos, ≈ 33 fotogramas en total, en los que el rival toca la cabeza de Tin. Es la
   regla dura y es lo que el dueño señaló en la v2. V2 cae en la pausa de impacto del golpe principal.
3. **Control automático:** ampliar E4 como se dice en la sección 3 antes de la siguiente vuelta; con la prueba actual
   una v5 puede volver a dar PASA con el mismo defecto.
4. **Antes de publicar, aunque se corrija lo anterior:** sello «as of» con la fecha del día; escucha humana del audio
   (incluido el «it» que marca el reconocedor); firma de animación para D6; firmar `controles.md` con esta vuelta.

Costo de corregir: 0 créditos (código). Sería la quinta versión de una pieza que el dueño ya vio; tiene que saberlo.
Si la conversación principal decide presentarla así, que sea diciéndole al dueño estos tres puntos con su segundo
(≈ 9,8 s, ≈ 21,6 s y ≈ 23,1 s).

Veredicto: CAMBIOS

Firma: supervisor de continuidad, 2026-11-26. Pieza `f4c8224b3707`. Esta revisión no cubre el sonido, las fuentes de
los datos ni las licencias.
