# Revisión de continuidad y calidad — short 4 de Tin & Tan, versión 3

- **Fecha:** 2026-11-27 · **Quién:** supervisor de continuidad · **Qué se revisó:** final v3
  (`06_final/tin_y_tan_short04_v3.mp4`, 1080×1920, 30 f/s, 986 f = 32,87 s).
- **sha256 (12 primeros):** `511571dd5f4d` (calculado por mí con `sha256sum`; coincide con el de producción).
- **Cómo:** las 21 tiras de producción (1 de cada 2 fotogramas, todo el video) y los 986 fotogramas extraídos por mí a
  resolución completa en una carpeta temporal fuera del repositorio; montajes fotograma a fotograma de cada golpe, de
  cada cambio de subtítulo y de los dos cortes de firma; tarjetas de dato y subtítulos leídos a resolución completa;
  `revisar_texto.py` sobre los dos `.srt`; `revisar_color.py` sobre el video; `postpro.py destellos`.
- **Lo que NO pude comprobar:** no oí el audio (no puedo): A7, el «it» de más de la voz y «cada corte con su sonido»
  siguen sin firma de oído. No releí las fuentes de los datos ni audité `licencias.md`. No comparé plano por plano con
  la referencia (A1). Las medidas en píxeles de este informe son a ojo sobre los montajes (van con «≈»); las del motor
  las copio de `control_encuadre_v3.md`. Los fotogramas se citan como `fNNN` (segundo = f / 30).

**Resumen:** la v3 resuelve lo que más pesaba en la v2: las carreras recorren distancia, los golpes caen sobre el
rival, las estrellas ya no tapan la cara de quien pega, los subtítulos no se enciman, los datos se leen siempre y el
texto está limpio. Lo que no deja presentarla es un tramo de 25 fotogramas (f289–f313) en el que el rival queda
dibujado con los pies sobre la cara de Tin y la cabeza de Tin hundida en el mostrador, más cuatro momentos en los que
el rival se encima a Tin o a Tan o salta de sitio en un fotograma. El control automático los dejó pasar porque solo
compara centros de cabeza. Todo es render por código: corregir cuesta 0 créditos.

---

## 1. Identidad contra las fichas

| Personaje | Rasgo | ¿Está? | Evidencia |
|---|---|---|---|
| Tin | Cabeza naranja, contorno tinta, lentes con brillo, lápiz amarillo con goma roja | Sí | f30, f547, f958 |
| Tin | Gorra con visera clara, botón y dos costuras | **A medias (igual que en la v2)** | Botón sí. En la pelea la visera es una barra marrón oscura y no se ven costuras (f547, f692) |
| Tin | Cara legible | **No en f289–f313** | Los pies y las piernas del rival cruzan la cara; ver N1 |
| Tan | Cabeza verde azulado, rodete con cinta, bufanda mostaza con dos puntas | Sí en todos los planos | f30, f484, f612, f958 |
| Tan | Cara legible | Sí | El mazo ya no le tapa la cara (f606–f660); en el golpe 5 se le ve entera (f612–f618) |
| Tin y Tan | Mismo dibujo en firma y pelea | Mejor | La tinta ya es la misma (`componer.py`, línea 60). Queda el salto de tamaño y de lado en el corte de cierre (N10) |
| Rival | Madeja, dos huecos de papel, sin boca ni pupilas, rizo **sin punto** | Sí, en todo lo mirado | f46, f164, f262, f514, f692, f810, f884 |
| Rival | Sin nombre en pantalla | Sí | Ninguna tarjeta ni subtítulo lo nombra |
| Rival | Cuerpo de palitos; escalones de tamaño | Sí | 1,5 (f58) → 1,25 (f234) → ≈ 1,0 (f514) → pequeño (f692, f810) |
| Rival | Solo tinta, sin color propio | Sí, con un artificio visible | El disco de papel detrás de la madeja se sigue viendo (N7) |
| Rival | «Se borra empezando por la cabeza» | **No (igual que en la v2)** | f896–f900: se va el cuerpo en gotas y la madeja es lo último que queda |

## 2. Defectos bloqueantes de la v2: estado en la v3

| v2 | Qué era | Estado | Fotograma que lo prueba |
|---|---|---|---|
| C1 | Estrella sobre la cara de quien pega | **Resuelto** en golpes 1, 2, 4, 5, remate y 6 (f82–f84 entre puño y rival; f169–f171 en la pierna del rival; f574–f576; f612–f614; f694–f696; f886–f888). **A medias** en el golpe 3 (f314–f316: toca la copa de la gorra, no la cara) y en el bloqueo (N5) |
| C2 | La patada no conectaba | **Resuelto** en el contacto (f169–f171), pero con salto de posición (N2) |
| C3 | El rival se estrellaba donde estaba Tan | **Resuelto** | f86–f98 vuela sobre el estante; f100 impacto; f102–f126 Tan al lado, fuera de la trayectoria |
| C4 | Bloqueo con cuerpos encimados | **Resuelto** en los cuerpos (f546–f550, separados); queda N5 |
| C5 | Carrera del remate sin avance y salto | **A medias** | f661–f679 recorren de verdad (cambia el fondo; 383 y 313 px). Queda la pausa con Tin cortado por el borde y el salto al contacto (N8) |
| C6 | Carrera con vaivén (f236–f282) | **Resuelto** | Ya no hay carrera ahí; Tin en guardia, esquiva en f262–f270 |
| C7 | Carrera en el sitio ante el mostrador | **Resuelto** | f283–f295 corre 493 px hasta el mostrador |
| C8 | Golpe doble en otro plano que el rival | **Resuelto** | f694–f696: armas, estrella y rival en el mismo sitio |
| C9 | Mazo invisible, Tan cortada, golpe a un caído | **Resuelto** | f606–f611 el rival está de pie; f612 el mazo baja; Tan entera en cuadro. La cabeza del mazo queda medio tapada por estrella y humo (nota b) |
| C10 | Cabezas de Tin y Tan fundidas en el cruce | **A medias** | f583–f585: Tan pasa por delante y su cabeza tapa media cara de Tin 3 f (N9) |
| C11 | La llama desaparecía antes de estallar | **Resuelto** | f704–f716 la llama sigue hasta f716; f717 invertidos |
| C12 | El rival pasaba de tendido a de pie sin levantarse | **No resuelto, cambió de forma** | f212→f213 (N3). En el respiro sí se levanta bien (f786–f810) |
| C13 | Humo pegado a las cabezas | **Resuelto** | f750–f873: el humo está arriba, en la pared |
| C14 | Halo del disco de papel | **No resuelto** | f664–f716 (N7) |
| C15 | Bloque negro bajo la mano de Tan en el cierre | **Resuelto** | f958–f985 |
| C16 | Tan a medias por el borde en f56 | **Resuelto** | f30–f69 entera |
| C17 | Quietos 28 y 35 f | **Resuelto** según el control (M4: nadie) | f484–f511 Tan habla y gesticula |
| C18 | Bucle: fondo roto frente a fondo entero | **Igual (D6 declarada)** | f985→f0: lápiz, brazo, caras, texto y cámara empalman; el fondo no. Sigue faltando la firma de animación |
| T1 | Subtítulos encimados | **Resuelto** | f170→f171, f248→f249, f315→f316, f429→f430, f482→f483, f549→f550, f613→f614, f887→f888: un solo subtítulo en cada fotograma |
| T2 | Texto emborronado en el cierre | **Resuelto** | f954–f955: el subtítulo sale nítido sobre el barrido; f956 la portada entra nítida |
| T3 | Estrella bajo el panel del subtítulo | **Resuelto** | Subtítulo en y 1376–1552; ninguna acción detrás |
| T4 | «A hoy.» | **Igual** | f888–f955. Es de redacción; lo decide el director creativo («Hasta hoy.») |
| — | Datos tapados por el humo | **Resuelto** | Tarjeta opaca: f630–f668 y f750–f879 se leen enteros |
| — | Rojo sobre el rival (f712–f714) | **Resuelto en la letra** | f704–f716: ningún rojo por delante de la madeja; ver N7 |
| — | Grieta de salida invisible | **Resuelto** | f926–f934: el trazo va del asterisco a la grieta, en suelo despejado |

## 3. Defectos nuevos o que siguen, por fotograma

Gravedad: **B** bloquea presentar · **A** alta · **M** media · **b** baja. Todo número de corrección es un **valor de
partida**. Archivo salvo que se diga otro: `video-studio/motor_de_accion/guiones/tin_en_s_004.js`.

| # | Fotogramas | Gravedad | Qué se ve | Corrección (valor de partida) |
|---|---|---|---|---|
| N1 | f289–f313 (25 f, 0,83 s) y f314–f316 | **B** | El rival salta al mostrador y queda dibujado **encima de Tin**: en f289–f293 sus dos pies están sobre los ojos de Tin; en f294–f313 sus piernas cruzan la cara. En f300–f313 la cabeza de Tin está **hundida en el mostrador** (corte recto en f303 y f306). La estrella del gancho (f314–f316) cae sobre la gorra. Rompe la regla dura y D24, y es el plano que acompaña a «made today by Rockstar Games» | Línea 104: Tin termina la carrera en `[1.85, 0, -2.88]`, dentro del volumen del mostrador y a 0,35 u del rival, que cae en `[2.2, 1.0, -3.03]` (línea 129). Parar a Tin antes y delante: `[1.15, 0, -2.45]`; o llevar la caída del rival a x ≈ 2.9. Añadir a `codigo/control_encuadre.py` una prueba de solape de cajas (cuerpo del rival contra cabeza de Tin o de Tan), no solo centros de cabeza |
| N2 | f166–f171 | **A** | El rival carga contra Tin y su madeja tapa la gorra de Tin (f166–f168). En f168→f169 el rival **salta ≈ 216 px hacia la izquierda en un fotograma**, hacia el pie de Tan (el golpe lo atrae en vez de empujarlo), y en f170–f171 su madeja queda sobre el rodete de Tan | Pista de posición del rival antes de K2: que la carga termine en el carril de Tan y a ≥ 0,9 u de Tin en K2 − 1, de modo que la clave `[K2, …, 'salto']` no lo mueva más de 0,3 u; salida del golpe hacia +x desde K2 |
| N3 | f212→f213 | **A** | El rival, tendido junto a los pies de Tin con la cabeza a la izquierda, aparece en el fotograma siguiente **≈ 600 px a la derecha y girado 180°** (cabeza a la derecha), con cámara fija y Tin quieto. Luego se levanta cortado por el borde (f213–f220; aviso E1 del control) | Línea 121: `D.mira.push(…, [K2 + 44, -1])` voltea el dibujo mientras la pose es `caido`. Mover el cambio de `mira` a cuando ya está `sentado` o `agachado` (K2 + 58) o darle una transición; levantarse 0,5 u más adentro del cuadro |
| N4 | f644–f660 | **A** | El rival salta desde lo alto del estante derecho y **pasa por encima de Tin** (f645–f647, las piernas rozan la gorra) para caer a su izquierda; se queda 12 f con la madeja escondida detrás de la cabeza de Tin (f648–f660; aviso E3 en f660). D24 dice que nunca pasa por encima | Línea 133: `[K5 + 26, [1.5, 2.4, -4.4]]` → `[K5 + 36, [0, 0, ZF]]`. Bajar por el pasillo del fondo sin cruzar la columna de Tin (punto alto x ≈ 0.6, y ≈ 1.6) y caer a ≥ 0,8 u de Tin en pantalla |
| N5 | f548–f561 | **A** | Bloqueo: la estrella queda pegada al mentón de Tin (f548–f551) y **gotas de tinta negras caen sobre su ojo y su mejilla** durante 13 f (f548, f551, f556, f560, f561). La espada casi no se ve. Sin sonido se puede leer «le dieron a Tin» | Línea 263: `puntoBloqueo` a 0.6 del camino hacia el rival (`lerp(…, 0.2)`) y gotas con velocidad hacia el rival y hacia el fondo (`V(1.6, 1.4, -0.6)`) para que no crucen la cara; espada más larga en K − 1 |
| N6 | f66–f69 | **A** | Tras el pisotón, el puño del rival queda sobre la gorra de Tin mientras Tin se agacha (f66) y se incorpora (f67–f69): se lee como un empujón en la cabeza | Separar 0,4 u al rival de Tin entre f62 y f69, o que el retroceso del pisotón lleve el brazo al otro lado |
| N7 | f664–f716 | M | Sigue el disco de papel detrás de la madeja (C14): halo claro sobre la isla (f664–f693) y recorte redondo en la llama (f704–f714). Cumple «ningún rojo sobre el rival», pero el truco se ve | Línea 168 (`x.papel`): activar solo de f704 a f716 y recortar el disco al contorno de la madeja; o bajar la llama para que el vuelo no la cruce |
| N8 | f682–f694 | M | Pausa antes del remate con **la cabeza de Tin cortada por el borde izquierdo** (f688–f693) y, en f693→f694, Tin y Tan avanzan ≈ 250 y ≈ 180 px en un fotograma. Es la gramática del golpe (pausa y contacto), pero el encuadre lo afea | Tabla PLANOS, P15: abrir 0,4 u a la izquierda entre KR − 12 y KR − 1; terminar la carga 0,3 u más cerca |
| N9 | f583–f585 | M | Cruce de Tan por delante de Tin: 3 f con la cabeza de Tan sobre media cara de Tin. Se lee como cruce, no como fusión | Adelantar el cruce 4 f o separar 0,3 u más en z |
| N10 | f953→f957 | M | Corte de cierre: Tin a la izquierda y Tan a la derecha (f952) pasan a Tan izquierda y Tin derecha (f957) **con el mismo fondo detrás**. El barrido lo disimula; está declarado en D26 | Declararlo también en la sección 9.1 de la dirección o filmar P21 desde el otro lado del eje |
| N11 | f29→f30 | M | El lápiz pasa de la mano de Tan (f29) a la de Tin (f30) en el corte, sin entrega (igual que en la v2). Al final sí se ve la devolución (f942–f950) | Que Tin empiece P2 sin lápiz y lo reciba en f30–f40, o que Tan lo lance en f26–f29 |
| N12 | f372–f380 | M | La madeja del rival queda detrás de la tarjeta del dato (f374–f377) y la cabeza de Tin se mete en la tapa del mostrador al agacharse (f376–f377) | Bajar la cámara de P10 o alejar a Tin 0,3 u del mostrador |
| N13 | f184–f212 | M | El rival tendido tapa las piernas de Tin 28 f (Tin de pie, lápiz en alto, sin golpear: la regla del caído se cumple) | Que resbale 0,5 u más allá de Tin |
| N14 | f896–f900 | M | El rival no «se borra empezando por la cabeza»: la madeja es lo último | Invertir el orden del borrado en la implosión |
| N15 | f150–f156 | b | El rival corre por detrás de Tan y las dos cabezas quedan apiladas ≈ 6 f | — |
| N16 | f596, f900, f719–f749 | b | Mango del mazo sobre la visera de Tin 1 f; una gota sobre el lente de Tin; la lámpara del techo parece un ojo | — |
| N17 | f890–f953 | b | El marco de la tarjeta de la respuesta empieza en y ≈ 358 (zona útil desde 380); el texto está dentro | Bajar la tarjeta ≈ 25 px en `componer.py` |

## 4. Texto y cifras (leídos a mano sobre los fotogramas, a resolución completa)

| Texto en pantalla | Fotogramas | Resultado |
|---|---|---|
| «GTA 7?» / «Facts, Checked» | f0–f29, f956–f985 | Correcto; 4 palabras; mayúsculas bien |
| «GTA = Grand Theft Auto» | f86–f305 | Correcto |
| «a game series · since 1997» | f218–f305 | Correcto |
| «made today by Rockstar Games» | f251–f305 | Correcto |
| «GTA 6» / «out since Nov 19, 2026» | f338–f428 | Correcto |
| «the sixth numbered game» | f432–f481 | Correcto |
| «rated M · 17 and over» | f552–f596 | Correcto |
| «from GTA 5 to GTA 6» | f616–f669 | Correcto; se lee entero todo su tiempo |
| «13 years, 63 days» / «GTA 5: Sep 17, 2013» / «GTA 6: Nov 19, 2026» | f750–f880 | Correcto; los tres renglones despejados |
| «GTA 7:» / «not announced» / «as of Nov 26, 2026» | f890–f953 | Correcto para el 26. **Hoy es 27: el sello caduca y se recompone el día de publicar** (D5) |

- **Subtítulos en español (12), leídos uno por uno en pantalla** (f40, f100, f200, f280, f400, f450, f520, f580, f650,
  f780, f860, f920): sin errores de ortografía, tildes ni signos («¿Habrá…?», «empezó», «salió», «Suscríbete»,
  «Clasificación», «años», «días», «¿Y GTA 7?»). GTA, Grand Theft Auto, Rockstar Games y Rockstar con mayúscula.
  Ningún nombre propio en minúscula. Sin subtítulo en los dos planos de portada (D20) ni en f684–f737 (no hay voz).
- **`subtitulos.srt` (inglés):** las 12 líneas coinciden con el guion de `tiempos.py`; sin errores.
- **Cifra recalculada:** 17 de septiembre de 2013 → 19 de noviembre de 2026 = 13 años + 13 + 31 + 19 = 63 días. Entera:
  no lleva «≈». Es la misma en la tarjeta, en los dos `.srt` y en el guion de voz. «Sexto», «17» y «1997» coinciden
  entre tarjeta y subtítulo.
- **`revisar_texto.py`:** NO PASA en español ni en inglés por un solo error, el mismo de la v2: falta Hunspell
  (instalarlo pide el sí del dueño). 12 textos por idioma, ningún otro error ni aviso. La lectura a mano lo suple, pero
  el control 1 no queda en «0 errores».
- **`revisar_color.py`** (paleta C, 11 colores de `c_alto_voltaje.json`): ≈ 90 % dentro de la paleta; luminosidad
  ± 2 % y saturación ± 2 % entre segundos; dominantes `#E9E4D6` 42,3 %, `#D9E4EB` 30,8 %, `#999E9B` 14,4 %. Texto tinta
  `#1B1B22` sobre tarjeta `#F2EFE8` (medido en f760): 14,9:1, pasa 7:1. La regla «un acento por plano» y la sección 3b
  las firma fotografía.
- **`postpro.py destellos`:** pasa (ningún segundo con más de 3).
- **Nada del juego ni marcas como objeto:** cumplido. Televisor en blanco, cajas lisas, mando genérico sin logotipo.

## 5. Lista A1–A14

| # | Pedido | Estado | Fotograma de prueba |
|---|---|---|---|
| A1 | Pelea «casi idéntica» a la referencia | **A medias** | La gramática está y los golpes conectan (f82, f169, f574, f612, f694, f886). Fallan N1 a N6. Sin comparar con la referencia |
| A2 | Aceleración y desaceleración | Se cumple | Calcos en los vuelos (f88–f94, f172–f180, f318–f322, f698–f708); pausas antes del contacto |
| A3 | 2D en mundo con profundidad | **Se cumple, con N1** | Cámara alta y en diagonal; carreras en profundidad (f283–f295, f577–f594, f661–f679); sombras. Rompe la coherencia f300–f313 |
| A4 | Fuego y humo | Se cumple | f576–f716 llama del televisor; f740; humo f600–f660 y f750–f873 |
| A5 | Choques | Se cumple | f100 (estante), f190 (postes), f336 (mostrador), f562 (televisor) |
| A6 | Explosión e implosión | Se cumple | f724–f740; f890–f904 |
| A7 | Sonidos de golpes | **Sin comprobar** | Nadie los ha oído |
| A8 | Daños que se quedan | Se cumple | f985: grieta, estante inclinado, mostrador volcado, quemadura, banderines caídos |
| A9 | Rival con cuerpo | Se cumple | f58, f514 |
| A10 | Paleta por tema | Se cumple por medida | ≈ 90 % (medido por mí) |
| A11 | Entorno por tema | Se cumple en pantalla | f0. No revisé el catálogo |
| A12 | Armas de tinta | Se cumple | f440 (bastón), f514–f546 (espada), f590–f606 (mazo). Sin armas de fuego ni sangre |
| A13 | Universo conectado | Se cumple en pantalla | Mando en su repisa (f30, f692, f985); caja registradora rota abajo a la izquierda (f918–f952); asterisco ≈ 65 px (f926–f985); trazo que se escurre a la grieta (f926–f934); rizo sin punto; Tin sin lápiz en la firma |
| A14 | Escalas | No aplica | — |
| — | Firma del lápiz bumerán | Se cumple, con D6 | f0–f10 y f972–f985 |
| — | Subtítulos en español quemados | Se cumple | Sección 4 |

## 6. Reglas duras

| Regla | Estado | Evidencia |
|---|---|---|
| El rival nunca alcanza a Tin ni a Tan | **No se cumple en lo que se ve** | f289–f313 (N1); f166–f168 y f170–f171 (N2); f645–f660 (N4); f66–f69 (N6); f548–f561 (N5). Mucho mejor que en la v2: en los golpes de Tin y Tan ya no hay cuerpos encimados |
| Ningún rojo sobre el rival | Se cumple | f704–f716; f786–f873 las llamas del suelo quedan a los lados |
| Nadie golpea a un caído | Se cumple | f184–f212 Tin no golpea; f606–f611 el rival está de pie antes del mazo; f884 de pie antes del golpe 6 |
| Tin y Tan no pelean entre sí | Se cumple | — |
| Sin armas de fuego ni sangre | Se cumple | — |
| Máximo 3 destellos por segundo | Se cumple | `postpro.py destellos` |

## 7. Preguntas fijas (cap. 11, regla 20)

- ¿Movimiento y corte antes del segundo 1? Movimiento sí (f0–f10); el primer corte cae en 1,0 s (f30), no antes.
- ¿Plano héroe cerca de la mitad? No: en la mitad está la suscripción (f483–f548); la explosión, en 24 s.
- ¿Picos y respiros? Sí.
- ¿Final que empalma con el inicio? Personajes, lápiz, texto y cámara sí; el fondo no (D6).
- ¿Cada corte con su sonido? Sin comprobar.
- ¿Algo genérico? No.
- ¿Más de 3 destellos por segundo? No.
- ¿Todo con licencia? No lo audité en esta vuelta.

## 8. Veredicto por tramo

| Tramo | Personaje fiel | Emoción se lee | Cámara | Actuación | Continuidad | Defectos | Veredicto |
|---|---|---|---|---|---|---|---|
| Firma y portada (f0–f29) | Sí | Sí | Bien | Bien | N11 | — | APROBADA |
| Entrada y pisotón (f30–f69) | Sí | Sí | Bien | Puño sobre la gorra | N6 | — | CORREGIR EN CÓDIGO |
| Golpe 1 (f70–f156) | Sí | Sí | Bien | Conecta | Bien | N15 | APROBADA |
| Golpe 2 y postes (f157–f235) | Sí | A medias | Bien | Conecta con salto | N2, N3, N13 | — | CORREGIR EN CÓDIGO |
| Esquiva, carrera y golpe 3 (f236–f337) | Cara de Tin tapada | Confusa | Bien | Rival sobre Tin | N1 | — | CORREGIR EN CÓDIGO |
| Fecha y bastón (f338–f482) | Sí | Sí | Bien | Bien | N12 | — | APROBADA con nota |
| Suscripción (f483–f511) | Sí | Sí | Bien | Bien | Bien | — | APROBADA |
| Bloqueo y golpe 4 (f512–f598) | Gotas en la cara de Tin | A medias | Bien | Bien | N5, N9 | — | CORREGIR EN CÓDIGO |
| Golpe 5 (f599–f640) | Sí | Sí | Bien | Bien | Bien | — | APROBADA |
| Salto del rival, carga y remate (f641–f718) | Sí | Sí | Tin cortado en la pausa | Bien | N4, N7, N8 | — | CORREGIR EN CÓDIGO |
| Explosión y respiro (f719–f873) | Sí | Sí | Bien | Bien | Bien | — | APROBADA |
| Golpe 6 e implosión (f874–f905) | Sí | Sí | Bien | Bien | N14 | — | APROBADA con nota |
| Final y cierre (f906–f985) | Sí | Sí | Bien | Bien | N10 | Sello de fecha | APROBADA con nota |

## 9. Lo que bloquea y lo que queda antes de publicar

1. **N1 (B):** f289–f313, el rival sobre la cara de Tin y la cabeza de Tin dentro del mostrador.
2. **N2, N3, N4, N5 y N6 (A):** juntos repiten, en menor grado, lo que el dueño señaló en la v2 (la interacción en el
   espacio pierde sentido): un salto de 216 px al contacto, un giro de 180° con salto de 600 px, el rival por encima
   de Tin, gotas sobre la cara de Tin en el bloqueo y el puño sobre su gorra.
3. **Antes de publicar, aunque se corrija lo anterior:** sello «as of» con la fecha del día; `revisar_texto.py` con
   Hunspell (sí del dueño para instalar); escucha humana del audio; firma de animación para D6; «A hoy.» (T4).

Costo de corregir: 0 créditos (código). Es una versión más de una pieza que el dueño ya vio dos veces: tiene que
saberlo.

Veredicto: CAMBIOS

Firma: supervisor de continuidad, 2026-11-27. Pieza `511571dd5f4d`. Esta revisión no cubre el sonido ni las fuentes de
los datos.
