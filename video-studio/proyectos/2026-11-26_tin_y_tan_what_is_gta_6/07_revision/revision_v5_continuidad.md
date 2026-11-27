# Revisión de continuidad y calidad — short 4 de Tin & Tan, versión 5

- **Fecha:** 2026-11-27 · **Quién:** supervisor de continuidad · **Qué se revisó:** final v5
  (`06_final/tin_y_tan_short04_v5.mp4`, 1080×1920, 30 f/s, 986 f = 32,87 s).
- **sha256 (12 primeros):** `df6b8a638e86` (calculado por mí con `sha256sum`; coincide con el del encargo).
- **Cómo:** las 21 tiras de producción, completas; los 986 fotogramas extraídos por mí a resolución completa en una
  carpeta temporal fuera del repositorio; montajes fotograma a fotograma (sin saltar ninguno) de f58–f69, f78–f89,
  f150–f161, f164–f175, f286–f320, f508–f519, f542–f553, f614–f663, f668–f679 y f686–f697, y de dos en dos de
  f698–f720 y f870–f906; recortes a tamaño real (1 píxel = 1 píxel) de V1, V2, V3, V4, de cada aviso E4 y E5, del
  golpe 2, del golpe 3, del rival ante la llama y de la cara de Tin en el golpe 6; las 10 tarjetas y los 12
  subtítulos leídos a tamaño real, y los 11 cambios de subtítulo con el fotograma anterior y el posterior;
  `revisar_texto.py` en los dos `.srt`, `postpro.py destellos` y `revisar_color.py` corridos por mí; líneas «v5»
  del guion.
- **Lo que NO pude comprobar:** no oí el audio (el «it» de más que marca el reconocedor en
  `voz_video_final_v5.md`, la mezcla y «cada corte con su sonido» siguen sin firma de oído; no medí los LUFS). No
  releí las fuentes de los datos ni audité `licencias.md`. No tuve el archivo de la v4 para comparar lado a lado:
  comparo contra mi revisión escrita. No reabrí las imágenes de `referencias/`; la identidad va contra las listas de
  las fichas, igual que en la v4. No medí contraste de texto (tarjeta y tinta son las de la v3, 14,9:1). El tramo
  f720–f869 (explosión y respiro) lo vi en las tiras (1 de cada 2 fotogramas), no fotograma a fotograma. Las
  distancias en píxeles son a ojo sobre recortes a tamaño real (van con «≈»). No toqué `controles.md` ni
  `firmas.md` (encargo: un solo archivo). Fotogramas como `fNNN` (segundo = f / 30).

**Resumen:** los tres defectos A de la v4 (V1, V2, V3) están resueltos: en ninguno de los tres tramos el rival toca
ya la cabeza, la visera ni la cara de Tin. No encontré defectos B ni A nuevos. Quedan cuatro roces breves, todos de
menos de 3 fotogramas de contacto (W1–W4), que anoto como M con su corrección de 0 créditos, y los M de arrastre
(N7, N11, N12, N14). La pieza puede presentarse al dueño diciéndole lo que queda.

---

## 1. Estado de V1–V12 de la v4

| # | Qué era en la v4 | Estado en la v5 | Fotograma que lo prueba |
|---|---|---|---|
| V1 (A) | Madeja contra la visera y el bastón de Tin, f648–f661 (14 f); piernas sobre el rodete de Tan f644–f645 | **Resuelto como A.** La madeja cae a la derecha del bastón: ≈ 50 px entre la madeja y la punta de la visera en f648–f652, más de 100 px desde f653; la cara de Tin entera todo el tramo; Tin ya está apartado y en guardia. **Queda un resto M (W1)** en el lado de Tan, y nota b: el rizo roza el bastón de Tin f648–f650 | Recortes f647–f652; montaje f640–f663 |
| V2 (A) | Madeja sobre la visera y la mejilla de Tin en la pausa del remate, f694–f698 | **Resuelto.** Tin pega erguido; cara, lentes y visera enteras. La madeja queda a ≈ 15–20 px de la punta de la visera en f694–f695 y ≈ 10 px en f696, sin tocar; sale hacia arriba entre los dos (f697–f698, rizo a ≈ 30 px de la gorra). Nota b: sigue muy justo | Recortes f693–f698 |
| V3 (A) | Pierna y puño del rival sobre la gorra de Tin en el mostrador, f292–f301 | **Resuelto.** El rival cae a la derecha de la caja registradora; lo más cerca es f293–f294 (pierna a ≈ 40 px de la punta de la visera, sin cruzar); f296–f303 a más de 100 px, brazo atrás | Montaje f286–f309 |
| V4 (M) | Puño en la punta de la visera f66–f69; cambio de lado en un fotograma | **A medias (W2, M).** El puño toca la punta de la visera solo en f66–f67; f68–f69 a ≈ 50 px. Sigue el cambio de pose del rival en un fotograma (f65→f66) y la cabeza de Tin baja ≈ 100 px y vuelve en f66–f68 | Recorte f65–f70 |
| V5 (M) | Madeja pegada a la cabeza de Tan al pie del estante | **Resuelto.** El rival cae a más de 250 px de Tan | f102–f120 |
| V6 (M) | Pies del rival en el rodete de Tan al trepar | **Resuelto en la subida** (trepa lejos, f629–f637). Reaparece en la bajada: W1 | Montaje f626–f637 |
| V7 (M) | La tarjeta «GTA 7» tapa media gorra de Tin | **Resuelto (b).** Gorra entera; queda tangente al borde inferior de la tarjeta en f896–f904 | Montaje f890–f906 |
| V8 (M) | Estrella pegada a la mejilla de Tin en el golpe 1 | **Mejor (b).** La estrella está sobre el rival; roza el borde de la cabeza de Tin en f83 | Montaje f78–f89 |
| V9 (b) | Mancha marrón en el plano de impacto | **Resuelto** | f100–f101 |
| V10 (b) | El brazo de Tin cruza su propia cara en el golpe 3 | Igual (f314–f315) | Recorte f312–f317 |
| V11 (b) | Tin cortado por el borde izquierdo | Igual (f619–f624) | Montaje f614–f625 |
| V12 (b) | Bloque gris delante de Tin; bastón sobre su cara 1 f | Igual: la caja registradora en vuelo cruza la gorra y la cara de Tin en f627–f628; el bastón le cruza la cara en f874 | f626–f629; f874 |

## 2. Pendientes N

| # | Estado en la v5 | Fotograma |
|---|---|---|
| N7 (M) | **No resuelto.** El disco de papel detrás de la madeja se ve como un círculo claro recortado en la llama | f703–f705, f713–f716 |
| N11 (M) | **No resuelto.** El lápiz está en la mano de Tan y, tras el corte, en la de Tin, sin entrega | f29 → f30 |
| N12 (M) | **No resuelto.** La madeja del rival queda tapada por la tarjeta (f289–f303 y f372–f400) y la tapa del mostrador cruza la cabeza de Tin en f376–f377 | f296, f376, f390 |
| N14 (M) | **No resuelto.** El rival se encoge entero; no se borra empezando por la cabeza | f898–f904 |
| N10, N9, N15, N16 | N10 igual y declarado (f953→f957). N15 mejor: la madeja pasa a ≈ 35–55 px de la cabeza de Tan sin tocarla (f154–f156) | — |

## 3. Avisos E4 y E5 del control, mirados en imagen

| Aviso | ¿Defecto? | Lo que se ve |
|---|---|---|
| E4 Tin f85 | No | El rival sale despedido a la izquierda; su estela pasa por debajo de la estrella, no sobre la cabeza de Tin |
| E5 Tin f313 | No | Rival agachado en el mostrador antes del gancho; madeja a ≈ 55 px de la gorra, 1 f |
| E5 Tin f513–f514 | **Sí, M (W3)** | f513: la madeja toca la mejilla de Tin y el rizo queda sobre su visera (1 f); f514: a ≈ 30 px |
| E5 arma de Tin f512–f514 | No | El bastón de Tin apunta al rival que cae; es su arma contra el rival |
| E5 Tan f60–f61 | No | Pisotón: el rival se inclina hacia la izquierda; madeja a ≈ 55 px de Tan, 2 f |
| E5 Tan f155–f156 | No (b) | El rival pasa por detrás de Tan a ≈ 35–55 px, sin tocar |
| E5 Tan f674, f678 | No | Es Tan quien se acerca con el mazo; madeja a ≈ 40–55 px de su cabeza |

**Lo que el control no vio:** W1 (pies del rival sobre la cabeza de Tan, f644–f645) y W2 (puño en la visera,
f66–f67). E4 y E5 deberían comparar también pies y puños del rival con la cabeza ampliada, aunque el rival esté más
al fondo.

## 4. Defectos de la v5

Gravedad: **B** bloquea · **A** alta · **M** media · **b** baja. No hay B ni A. Archivo de las correcciones:
`video-studio/motor_de_accion/guiones/tin_en_s_004.js`. Todo es código: 0 créditos.

| # | Fotogramas | Gravedad | Qué se ve | Corrección (valor de partida) |
|---|---|---|---|---|
| W1 | f643–f646 (≈ 21,5 s) | **M** | El rival salta del estante y cruza justo por encima de la cabeza de Tan: en f644–f645 sus pies quedan en el borde superior de la cabeza y del rodete (contacto 2 f); en f646 baja a ≈ 40 px a su izquierda. Está más al fondo, es pequeño, y la cara de Tan no se tapa. Es lo más cercano a la regla «no pasa por encima»; lo dejo en M por durar menos de 3 f y no leerse como golpe. Si el dueño lee la regla al pie de la letra, es el punto a mostrarle | Línea 138: punto alto `[K5 + 26, [2.6, 1.8, -4.9]]` → y ≈ 2,6 (que pase ≥ 120 px por encima) o Tan 0,5 u más a la derecha hasta K5 + 30 |
| W2 | f65–f69 (≈ 2,2 s) | M | Resto de V4: puño del rival en la punta de la visera de Tin en f66–f67; cambio de pose del rival en un fotograma | Rival 0,2 u más a la izquierda en f66–f69; repartir el giro en 2–3 f |
| W3 | f513 (≈ 17,1 s) | M | Un fotograma tras el corte: la madeja toca la mejilla de Tin y el rizo cruza su visera | Caída del rival 0,2 u más a la derecha en ese fotograma |
| W4 | f894–f897 (≈ 29,8 s) | M | Golpe 6: una gota de tinta cruza la cara de Tin; en f896 le tapa medio lente | Que las gotas salgan solo hacia el lado del rival, o bajar esa gota |
| W5 | f172–f174 | b | Golpe 2: la estela gris del rival queda encima y detrás de la cabeza de Tan 3 f; el rival sólido no la toca (rizo a ≈ 20 px en f173) | Acortar la estela de ese golpe |
| W6 | f109–f121 | b | Rival cortado por el borde derecho al pie del estante (aviso E1) | — |

## 5. Identidad

Tin (cabeza naranja, gorra con botón, lentes, lápiz amarillo con goma roja), Tan (verde azulado, rodete, bufanda
mostaza de dos puntas) y el rival (madeja, dos huecos, rizo, sin boca, solo tinta, sin nombre en pantalla) se
mantienen en todos los planos vistos. Igual que en la v4: en la pelea la visera de Tin es una barra oscura sin
costuras visibles (M de arrastre). Ningún personaje, texto, logo ni marca de agua ajenos.

## 6. Texto y cifras (leídos a mano, a tamaño real)

| Texto en pantalla | Fotograma | Resultado |
|---|---|---|
| «GTA 7?» / «Facts, Checked» | f20, f958, f985 | Correcto |
| «GTA = Grand Theft Auto» | f120 | Correcto |
| «a game series · since 1997» | f230 | Correcto |
| «made today by Rockstar Games» | f290 | Correcto |
| «GTA 6» / «out since Nov 19, 2026» | f400 | Correcto |
| «the sixth numbered game» | f460 | Correcto |
| «rated M · 17 and over» | f580 | Correcto |
| «from GTA 5 to GTA 6» | f640 | Correcto |
| «13 years, 63 days» / «GTA 5: Sep 17, 2013» / «GTA 6: Nov 19, 2026» | f800, f870 | Correcto |
| «GTA 7:» / «not announced» / «as of Nov 26, 2026» | f892–f920 | Correcto para el 26. **Hoy es 27: el sello se recompone el día de publicar** (regla del dueño) |

- **Subtítulos grabados (12), uno por uno** (f40, f100, f200, f280, f400, f450, f500, f580, f650, f780, f860,
  f920): «¿Habrá un GTA 7?» · «GTA es Grand Theft Auto:» · «una serie de juegos que empezó en 1997» · «y que hoy
  hace Rockstar Games.» · «GTA 6 salió el 19 de noviembre de 2026.» · «Es el sexto juego numerado.» · «Suscríbete.
  Aquí comprobamos los datos.» · «Clasificación M: mayores de 17.» · «De GTA 5 a GTA 6:» · «trece años y sesenta y
  tres días.» · «¿Y GTA 7?» · «Rockstar no ha anunciado ninguno. Hasta hoy.» Sin errores de ortografía, tildes,
  signos ni mayúsculas de nombres. **T10 dice «Hasta hoy.»** Los 11 cambios (f84, f171, f249, f316, f430, f483,
  f550, f614, f738, f838, f888) muestran un solo subtítulo por fotograma.
- **`.srt`:** coinciden con lo grabado. No se suben a YouTube (regla del dueño).
- **Cifra recalculada:** 17 sep 2013 → 17 sep 2026 = 13 años; 17 sep → 19 nov 2026 = 63 días (13 + 31 + 19;
  confirmado con calendario). Entera: no lleva «≈». Igual en tarjeta, subtítulo y `.srt`.
- **`revisar_texto.py`** (corrido por mí): inglés PASA, 0 errores; español PASA, 0 errores; sin avisos.
- **`postpro.py destellos`** (corrido por mí): ningún segundo pasa de 3 (2 cambios fuertes en total).
- **Color** (corrido por mí con `--paleta 02_prompt/direccion.md`): ≈ 91 % en paleta, luminosidad ± 2 %,
  saturación ± 3 %; `color_v5.txt` dice ≈ 90 %. Contra `DESIGN.md` del canal a secas sale ≈ 44 % porque ese archivo
  declara 9 colores y no los del escenario: la paleta válida es la de la dirección.
- **Miniatura:** 1080×1920; mismo cuadro que f0; «GTA 7?» / «Facts, Checked» en y ≈ 480–700, dentro de la zona
  útil; 4 palabras; no da la respuesta.
- **Voz:** el reconocedor oye «GTA 6. It came out…» (un «it» de más). No lo oí; queda para la escucha del dueño.

## 7. Reglas duras

| Regla | Estado | Evidencia |
|---|---|---|
| El rival nunca alcanza ni pasa por encima de Tin o de Tan | **Se cumple en lo que se ve a velocidad normal; con cuatro roces de menos de 3 f** | V1, V2 y V3 resueltos. Quedan W1 (f644–f645), W2 (f66–f67), W3 (f513) y la gota W4 |
| Ningún rojo sobre el rival | Se cumple | f703–f716: la llama queda detrás; el disco de papel impide rojo dentro de la madeja (N7) |
| Nadie golpea a un caído | Se cumple | Rival de pie en f604–f611 antes del mazo; de pie en f668–f693 antes del remate; se levanta solo en el respiro y está de pie en f885 antes del golpe 6 |
| Tin y Tan no pelean entre sí | Se cumple | — |
| Sin armas de fuego ni sangre | Se cumple | Bastón, espada y mazo de tinta; gotas negras |
| Máximo 3 destellos por segundo | Se cumple | `postpro.py destellos` |

## 8. Preguntas fijas (cap. 11, regla 20)

- ¿Movimiento y corte antes del segundo 1? Movimiento sí (el lápiz vuela, f0–f10); el primer corte cae en 1,0 s (f30).
- ¿Plano héroe cerca de la mitad? No: en la mitad está la suscripción (f483–f511); el héroe, en ≈ 24 s (f719–f749).
- ¿Picos y respiros? Sí (respiro f750–f873).
- ¿Final que empalma con el inicio? Personajes, lápiz, texto y cámara sí (f985 → f0); el fondo no (D6 declarada).
- ¿Cada corte con su sonido? Sin comprobar.
- ¿Algo genérico? No.
- ¿Más de 3 destellos por segundo? No.
- ¿Todo con licencia? No lo audité.

## 9. Veredicto por tramo

| Tramo | Personaje fiel | Emoción se lee | Cámara | Actuación | Continuidad | Defectos | Veredicto |
|---|---|---|---|---|---|---|---|
| Firma y portada (f0–f29) | Sí | Sí | Bien | Bien | N11 | — | APROBADA |
| Entrada y pisotón (f30–f69) | Sí | Sí | Bien | Puño en la visera 2 f | W2 | — | APROBADA con nota |
| Golpe 1 y estante (f70–f156) | Sí | Sí | Bien | Conecta | Bien | W6 | APROBADA |
| Golpe 2 y postes (f157–f235) | Sí | Sí | Bien | Conecta | Bien | W5 | APROBADA |
| Esquiva, carrera y golpe 3 (f236–f337) | Sí | Sí | Bien | Bien | N12 | V10 | APROBADA |
| Fecha y bastón (f338–f482) | Sí | Sí | Bien | Bien | N12 | — | APROBADA con nota |
| Suscripción (f483–f511) | Sí | Sí | Bien | Bien | Bien | — | APROBADA |
| Bloqueo y golpe 4 (f512–f598) | Sí | Sí | Bien | Bien | W3 | — | APROBADA con nota |
| Golpe 5 (f599–f640) | Sí | Sí | Bien | Bien | Bien | V11, V12 | APROBADA |
| Salto del rival, carga y remate (f641–f718) | Sí | Sí | Bien | Bien | W1, N7 | — | APROBADA con nota |
| Explosión y respiro (f719–f873) | Sí | Sí | Bien | Bien | Bien | — | APROBADA |
| Golpe 6 e implosión (f874–f905) | Sí | Sí | Bien | Bien | N14 | W4 | APROBADA con nota |
| Final y cierre (f906–f985) | Sí | Sí | Bien | Bien | N10 | Sello de fecha | APROBADA con nota |

## 10. Antes de publicar (no frena la presentación)

1. Recomponer el sello «as of» con la fecha del día de publicación.
2. Escucha humana del audio, incluido el «it» de más.
3. Decirle al dueño W1 (≈ 21,5 s), W2 (≈ 2,2 s), W3 (≈ 17,1 s) y W4 (≈ 29,8 s) y los M de arrastre; corregirlos
   cuesta 0 créditos y sería una sexta versión: él decide.
4. Copiar esta vuelta en `controles.md` y `firmas.md`; ampliar E4/E5 a pies y puños.

Veredicto: APROBADO

Firma: supervisor de continuidad, 2026-11-27. Pieza `df6b8a638e86`. Esta revisión no cubre el sonido, las fuentes de
los datos ni las licencias.
