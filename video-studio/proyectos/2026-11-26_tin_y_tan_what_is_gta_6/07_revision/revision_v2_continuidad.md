# Revisión de continuidad y calidad — short 4 de Tin & Tan, versión 2

- **Fecha:** 2026-11-26 · **Quién:** supervisor de continuidad · **Qué se revisó:** final v2
  (`06_final/tin_y_tan_short04_v2.mp4`, 1080×1920, 30 f/s, 986 f = 32,87 s).
- **Cómo:** las nueve hojas `hoja_v2_00…08.jpg` completas, más los 986 fotogramas extraídos a una carpeta temporal
  fuera del repositorio; los tramos de golpe, fotograma por fotograma; posición de las cabezas de Tin y Tan medida en
  cada fotograma (centro de la mancha naranja y de la verde azulada); `postpro.py destellos`; `revisar_texto.py`.
- **Lo que no hice:** no oí el audio (no puedo); no releí las fuentes de los datos; no corrí `revisar_color.py` (copio
  la medida del constructor); no audité `licencias.md`. Los fotogramas se citan como `fNNN` (número de fotograma del
  video; segundo = f / 30).

**Veredicto: CORREGIR.** El texto está limpio y los rasgos de los tres personajes están; lo que falla es el espacio de
la pelea: los golpes no caen donde está el rival, las estrellas de impacto caen sobre la cara de Tin y de Tan, el rival
atraviesa a los protagonistas y las carreras no avanzan. Coincide con lo que vio el dueño. Todo es render por código:
corregir cuesta 0 créditos.

---

## 1. Identidad de cada personaje contra su ficha

| Personaje | Rasgo | ¿Está? | Evidencia |
|---|---|---|---|
| Tin | Cabeza naranja, contorno tinta | Sí | f0: `#E47C2E` medido (ficha `#E07A2E`) |
| Tin | Gorra marrón con visera clara, botón y dos costuras | **A medias** | En la firma (f0–f29, f957–f985) hay botón y visera clara. En la pelea (motor) la visera es un trazo oscuro, sin el marrón claro `#9C6A44`, y no se ven costuras (f300, f430, f676) |
| Tin | Lentes redondos con brillo | Sí | f430 (primer plano), f300 |
| Tin | Lápiz amarillo, goma roja, punta naranja | Sí, con dos defectos | f354–f360: el lápiz cruza la cara y tapa un lente (fallo conocido de la ficha). f29→f30: el lápiz pasa de la mano de Tan a la de Tin en el corte, sin verse la entrega |
| Tan | Cabeza verde azulado, rodete, cinta | Sí | f0: `#2E7E7A` medido (ficha `#2F7F7A`) |
| Tan | Bufanda mostaza con dos puntas | Sí en todos los planos | f0, f104, f300, f676, f985 |
| Tan | Cara legible | **No en dos tramos** | f612–f616: dos manchas negras por ojos y una estrella encima. f640 y f676: la cabeza del mazo le tapa la cara entera |
| Tin y Tan | Mismo dibujo en todo el video | **No** | Hay dos sistemas de dibujo: firma (`palitos.py`: tinta parda `#281E1D` medida, línea fina, piernas juntas) y pelea (motor: negro, línea más gruesa, visera distinta). Se nota en los dos cortes de firma (f29→f30 y f953→f957) |
| Tin y Tan | Tamaño entre planos | A medias | 487 px en la firma; ≈ 400 px en f30–f300; hasta ≈ 675 px en f486. Salto de tamaño y de posición en los dos cortes de firma |
| Rival | Madeja por cabeza, dos huecos de papel, sin boca ni pupilas | Sí | f56, f168, f257, f530 |
| Rival | Rizo de pregunta **sin punto** | Sí, en todos los fotogramas mirados | f40, f56, f168, f257, f530, f693, f884 |
| Rival | Sin nombre en pantalla | Sí | Ningún dato ni subtítulo lo nombra |
| Rival | Cuerpo de palitos, manos y pies | Sí | f56, f222, f530 |
| Rival | Escalones de tamaño | A medias | 1,5 (f56) → ≈ 1,25 (f257) → ≈ 1,0 (f530) bien. En f693 mide ≈ 0,7 de Tin a ojo (declarado 0,9) con los pies casi en la misma línea de suelo: se lee pequeño, no lejos |
| Rival | «Se borra empezando por la cabeza» | **No se lee** | f896: el cuerpo ya se deshace en gotas y la madeja sigue entera |
| Rival | Sin color propio | **No en f712–f714** | Ver sección 5 |

## 2. Continuidad entre planos

Ordenado por gravedad.

| # | Fotogramas | Qué se ve | Arreglo (todo por código, 0 créditos) |
|---|---|---|---|
| C1 | f82–f84, f574–f576, f612–f616, f695–f697 | **La estrella de impacto se dibuja sobre la cabeza de quien golpea**, no sobre el rival. En f82–f84 y f574–f576 tapa la cara de Tin; en f612–f616, la de Tan; en f695, las de los dos. Sin sonido se lee «le pegaron a Tin» | Colocar la estrella en el punto de contacto proyectado (puño, pie o arma contra el cuerpo del rival) |
| C2 | f170–f173 | Patada de Tan: la estrella queda en el aire, a ≈ 100 px del rival, que está encima de Tin y le tapa la cara. El golpe no conecta | Rival en la trayectoria del pie; nunca en la misma columna que Tin |
| C3 | f100–f150 | Golpe 1: el rival se estrella contra el estante **justo donde está parada Tan**; sus piernas salen a través de ella y vuelve a salir por detrás de su cabeza. Tan no reacciona | Mover a Tan fuera de la trayectoria o cambiar el estante de destino |
| C4 | f546–f548 | Bloqueo: en f548 el rival queda **encima de Tin**, cuerpo sobre cuerpo; no se ve bastón contra espada | Separar los cuerpos; que se crucen solo las armas |
| C5 | f671–f697 | «Carrera» del remate: Tin avanza 44 px y Tan 35 px en 10 fotogramas (f671–f681); en f683 la cámara los deja **más separados** (x 117 y 897) y quietos 10 fotogramas; en f695 saltan al centro (234 y 261 px en 2 fotogramas). Corren y no se acercan; luego se teletransportan | Que la carrera recorra de verdad la distancia hasta el rival, sin corte en medio |
| C6 | f236–f282 | Tin en pose de carrera 46 fotogramas: avanza 113 px netos y con vaivén (x 478 → 416 → 474 → 405): tirón en f252 y f260 | Trayectoria continua y más larga, o acortar el tramo |
| C7 | f338–f380 | Tin en pose de carrera delante del mostrador ≈ 1,4 s sin desplazarse (x 750–850) mientras se lee la fecha | Otra pose (guardia) o desplazamiento real |
| C8 | f693–f697 | Remate: las dos armas se cruzan en primer término y el rival está detrás, delante de la isla. El golpe doble cae en el plano de Tin y Tan, no donde está el rival | Rival en el mismo plano de profundidad que las armas en el contacto |
| C9 | f609–f630 | Golpe 5: el mazo **desaparece** en el contacto (f612–f624) y reaparece en f630. Tan salta de x 733 a x 975 y queda cortada por el borde derecho. El golpe clave de la caja registradora ocurre en el borde del cuadro | Encuadrar el golpe; mazo visible en K y K+1 |
| C10 | f573–f584 | Tan pasa **detrás** de Tin: las dos cabezas se funden (f573 y f576, el verde asoma bajo la cara de Tin). En f584 un calco del rival cae sobre la cabeza de Tan | Separar en x o en tiempo |
| C11 | f714→f716 | La llama grande del televisor desaparece entera un fotograma antes de la explosión | Mantenerla hasta el estallido |
| C12 | f216→f222 | El rival pasa de tendido a de pie en 6 fotogramas, sin levantarse | Añadir la subida o cortar |
| C13 | f786–f912 | Bolas de humo gris pegadas a la altura de las cabezas durante ≈ 4 s; en f840–f876 una tapa la cara de Tin | Que el humo suba y se disipe |
| C14 | f654–f693, f706–f710 | El disco de papel detrás de la madeja se ve como un halo claro sobre la isla y sobre la llama | Recortarlo a la silueta de la madeja |
| C15 | f957–f985 | Plano final: un bloque negro (resto del televisor) queda justo bajo la mano de Tan: parece que carga una caja | Moverlo ≈ 150 px |
| C16 | f56 | Tan sale a medias por el borde izquierdo | Reencuadrar |
| C17 | f484–f511 y f839–f873 | Tin y Tan sin moverse 28 y 35 fotogramas (≈ 0,9 y ≈ 1,2 s); la herramienta no lo marca porque otras cosas se mueven | Acción secundaria (bufanda, parpadeo) |
| C18 | f985→f0 | El bucle empalma en personajes, lápiz, texto y cámara; el fondo salta de tienda rota a tienda entera (excepción D6) | Falta la firma de animación; no lo apruebo yo |

**Lo que sí se sostiene:** grieta del pisotón desde f60 hasta f985; estante izquierdo inclinado; postes caídos; mostrador
agrietado (f336) y luego partido (f618); televisor agrietado (f562) y reventado; quemadura en la pared; banderines
colgando de un lado; `mando_mostaza` en su repisa de f0 a f985. Ningún objeto roto reaparece entero dentro de la pelea.
Bastón (lo dibuja Tin en f430–f440), espada del rival (f514–f530) y mazo tienen origen visible; bastón y mazo se deshacen
en gotas (f896–f920).

## 3. Texto y cifras

Leído a mano, palabra por palabra, sobre los fotogramas.

| Texto en pantalla | Fotogramas | Resultado |
|---|---|---|
| «GTA 7?» / «Facts, Checked» (portada y cierre) | f0–f29, f957–f985 | Correcto; 4 palabras; mayúsculas bien |
| «GTA = Grand Theft Auto» | f86–f305 | Correcto |
| «a game series · since 1997» | f218–f305 | Correcto |
| «made today by Rockstar Games» | f251–f305 | Correcto |
| «GTA 6» / «out since Nov 19, 2026» | f338–f427 | Correcto |
| «the sixth numbered game» | f432–f480 | Correcto |
| «rated M · 17 and over» | f552–f595 | Correcto |
| «from GTA 5 to GTA 6» | f616–f668 | Correcto, **pero tapado por la columna de humo** ≈ f636–f668 (más de la mitad de su tiempo) |
| «13 years, 63 days» / «GTA 5: Sep 17, 2013» / «GTA 6: Nov 19, 2026» | f750–f879 | Correcto. **El humo tapa el tercer renglón en ≈ f750–f768** |
| «GTA 7:» / «not announced» / «as of Nov 26, 2026» | f890–f953 | Correcto hoy. **El sello caduca: hay que recomponer con la fecha del día de publicar** |

- **Cifra recalculada:** del 17 de septiembre de 2013 al 19 de noviembre de 2026 = 13 años (hasta el 17 de septiembre de
  2026) + 13 + 31 + 19 = 63 días. En días: 13 × 365 + 3 bisiestos (2016, 2020, 2024) + 63 = 4.811. Coincide con la
  dirección. Son enteros: no llevan «≈». La cifra es la misma en voz, pantalla y los dos `.srt`.
- **Subtítulos en español (12):** sin errores de ortografía, tildes ni mayúsculas («Suscríbete», «Clasificación», «empezó»,
  «salió», «días», «¿Habrá…?», «¿Y GTA 7?»). GTA, Grand Theft Auto y Rockstar Games con su mayúscula en todos.
  `grep` de nombres en minúscula sobre los `.srt` y `publicacion.md`: sin coincidencias.
- **Hallazgo T1 (bloquea):** en los dos `.srt` los tiempos se pisan 67 ms entre líneas (2→3, 3→4, 4→5, 5→6, 6→7, 7→8,
  8→9, 10→11, 11→12). En el video son 2 o 3 fotogramas con dos subtítulos encimados e ilegibles: f172 («GTA es Grand
  Theft Auto:» bajo «una serie de juegos…»), f430, f614–f615 («Clasi De GTA 5 a GTA 6: de 17.»), f888. Arreglo en
  edición: que cada línea termine donde empieza la siguiente.
- **Hallazgo T2:** f954–f956, barrido borroso entre el último plano y el cierre: el subtítulo y luego la portada salen
  emborronados 3 fotogramas. Sacar el texto del borrón o cortar en seco, como pide la dirección.
- **Hallazgo T3:** f312–f314, la estrella del golpe 3 queda **debajo del panel del subtítulo**; el rival y el televisor
  siguen detrás del panel en los generales (f366–f426, f600–f690).
- **Hallazgo T4 (de redacción, no de ortografía):** «A hoy.» es poco natural; propongo «Hasta hoy.». Lo decide el
  director creativo.
- **Diferencias con la dirección, ya resueltas en el video:** la frase «Each numbered game tells a new story» no está en
  voz, datos ni subtítulos; el subtítulo 8 dice «Clasificación M: mayores de 17.» (la dirección decía «Para mayores de
  17.»); la suscripción va en 16,1 s. La dirección quedó desactualizada.
- **Nada del juego ni marcas como objeto:** cumplido. Televisor en blanco, cajas lisas, mando genérico sin logotipo,
  ningún rótulo en el mundo. Los nombres de marca solo están en la capa de datos y nada los golpea ni los quema.
- **`revisar_texto.py`:** NO PASA en español ni en inglés, por un solo error: falta Hunspell (instalarlo pide el sí del
  dueño). La lectura a mano de arriba lo suple por hoy, pero el control 1 no queda en «0 errores».
- **Voz:** el reconocedor sigue oyendo un «it» de más («GTA 6. It came out»). Nadie lo ha oído: sin firma.

## 4. Lista A1–A14

| # | Pedido | Estado | Fotograma de prueba |
|---|---|---|---|
| A1 | Pelea de acción «casi idéntica» a la referencia | **A medias** | Están las fases (pausa f76–f81, contacto f82–f83), pero los golpes no conectan en el espacio: f84, f171, f548, f695. Sin comparar plano por plano con la referencia |
| A2 | Aceleración y desaceleración | **A medias** | Calcos en los vuelos (f172, f318, f584, f700). Sin borrón de movimiento; las carreras no avanzan (f236–f282, f671–f693) |
| A3 | 2D en mundo con profundidad e interacción 3D | **A medias** | Hay profundidad y sombras (f262→f300, Tin se aleja hacia el mostrador). Falla la coherencia: f104 (rival a través de Tan), f548, f693 (golpe en otro plano que el rival). La cámara corta; no viaja |
| A4 | Fuego y humo | Se cumple | f576 (fase 1), f640 y f676 (fase 2), humo con contorno f600–f768. El humo tapa datos (sección 3) |
| A5 | Choques | Se cumple | f100 (estante), f196 (postes), f336 (mostrador), f562 (televisor) |
| A6 | Explosión e implosión | Se cumple | f728 (anillo amarillo y estrella), f896–f900 (anillos que se cierran). Destellos: `postpro.py destellos` pasa |
| A7 | Sonidos de golpes | **Sin comprobar** | 53 eventos en el motor; nadie los ha oído |
| A8 | Daños que se quedan | Se cumple | f985: grieta, estante, mostrador partido, isla volcada, quemadura, banderines |
| A9 | Rival con cuerpo | Se cumple | f56, f530 |
| A10 | Paleta por tema | Se cumple por medida ajena | ≈ 91 % en paleta (`color_v2.txt`, no lo corrí yo). Falta la sección 3b firmada por fotografía |
| A11 | Entorno por tema y biblioteca | Se cumple en pantalla | f0 (tienda de videojuegos). El catálogo no lo revisé |
| A12 | Armas dibujadas con tinta | Se cumple | f440 (bastón), f530 (espada), f608 (mazo). Ninguna arma de fuego ni sangre |
| A13 | Universo conectado | **A medias** | f985: mando, caja rota (a la izquierda de Tan) y asterisco (f920–f985) a la vista. **La grieta de salida no se distingue**: queda entre cajas junto a las piernas de Tin |
| A14 | Escalas (Short = una página) | No aplica | — |
| — | Firma del lápiz bumerán | Se cumple, con reserva | f0–f10 y f972–f985; fondo distinto en el empalme (D6) y cambio de dibujo en el corte |
| — | Subtítulos en español quemados | Se cumple, con T1 a T3 | f40, f172, f614 |

## 5. Reglas duras

| Regla | Estado | Evidencia |
|---|---|---|
| El rival nunca alcanza a Tin ni a Tan | **No se cumple en lo que se ve** | La intención del guion es que fallen o bloqueen, pero en pantalla: f60–f64 el rival pisa con el cuerpo sobre el de Tin; f82–f84 y f574–f576 estrella sobre la cara de Tin; f104–f150 el rival atraviesa a Tan; f170–f173 el rival sobre Tin; f548 el rival encima de Tin; f584 calco sobre la cabeza de Tan; f612–f616 estrella sobre Tan; f695 estrellas sobre los dos |
| Ningún rojo sobre el rival | **No se cumple** | f706–f710 el disco de papel lo protege; en **f712–f714 las puntas rojas de la llama se dibujan por delante de la madeja**. La v2 lo daba por resuelto |
| Nadie golpea a un caído | **A medias** | Golpes 1 a 4, remate y golpe 6: el rival está de pie o en guardia (f80, f168, f546, f693, f884). Golpe 5: en f609 está agachado sobre la caja registradora, en f610 cae y en f612–f616 queda aplastado en el suelo con Tan encima y una estrella: se lee como golpe a un caído |
| Tin y Tan no pelean entre sí | Se cumple | Ojo con f695: las estrellas entre sus cabezas se prestan a esa lectura (se va con C1) |
| Sin armas de fuego ni sangre | Se cumple | — |
| Máximo 3 destellos por segundo | Se cumple | `postpro.py destellos`: OK |

## 6. Preguntas fijas (cap. 11, regla 20)

- ¿Movimiento y corte antes del segundo 1? Movimiento sí (lápiz, f0–f10); el primer corte cae justo en 1,0 s (f30), no antes.
- ¿Plano héroe cerca de la mitad? No: en la mitad (≈ 16 s) está el plano quieto de la suscripción; la explosión está en 24 s.
- ¿Picos y respiros? Sí.
- ¿Final que empalma con el inicio? En personajes y lápiz sí; el fondo no (D6).
- ¿Cada corte con su sonido? Sin comprobar: nadie ha oído el audio.
- ¿Algo genérico? No.
- ¿Más de 3 destellos por segundo? No.
- ¿Todo con licencia? No lo audité en esta vuelta.

## 7. Veredicto por tramo

| Tramo | Personaje fiel | Emoción se lee | Cámara | Actuación | Continuidad | Defectos | Veredicto |
|---|---|---|---|---|---|---|---|
| Firma y portada (f0–f29) | Sí | Sí | Bien | Bien | Lápiz cambia de mano en el corte | — | APROBADA |
| Entrada y pisotón (f30–f69) | Sí | Sí | Bien | Rival sobre Tin | C16 | f60–f64 | CORREGIR EN CÓDIGO |
| Golpe 1 (f70–f150) | Sí | Confusa | Bien | No conecta | C1, C3 | — | CORREGIR EN CÓDIGO |
| Golpe 2 y postes (f151–f235) | Sí | Confusa | Bien | No conecta | C2, C12 | T1 | CORREGIR EN CÓDIGO |
| Carrera y golpe 3 (f236–f337) | Sí | A medias | Bien | Carrera sin avance | C6 | T3 | CORREGIR EN CÓDIGO |
| Fecha y bastón (f338–f483) | Lápiz sobre la cara | Sí | Bien | Carrera en el sitio | C7 | — | CORREGIR EN CÓDIGO |
| Suscripción (f484–f545) | Sí | Sí | Bien | Quietos 28 f | C17 | — | APROBADA con nota |
| Bloqueo y golpe 4 (f546–f599) | Sí | Confusa | Bien | Cuerpos encimados | C1, C4, C10 | — | CORREGIR EN CÓDIGO |
| Golpe 5 (f600–f640) | Cara de Tan rota | Confusa | Golpe en el borde | Mazo desaparece | C9 | Regla del caído | CORREGIR EN CÓDIGO |
| Remate y explosión (f641–f749) | Mazo tapa a Tan | A medias | Corte en medio de la carrera | No avanza, luego salta | C5, C8, C11, C14 | Rojo sobre el rival; dato tapado | CORREGIR EN CÓDIGO |
| Respiro y golpe 6 (f750–f914) | Sí | Sí | Bien | Bien | C13 | Humo sobre el dato y sobre Tin | CORREGIR EN CÓDIGO |
| Asterisco y cierre (f915–f985) | Sí | Sí | Bien | Bien | C15, C18 | T2; grieta no se ve; sello de fecha | CORREGIR EN EDICIÓN |

## 8. Lo que bloquea, en orden

1. **Estrellas de impacto sobre la cara de Tin y de Tan** (C1): f82–f84, f574–f576, f612–f616, f695. Rompe la regla dura.
2. **El rival atraviesa o pisa a Tin y a Tan** (C3, C4, f60–f64, f170–f173, f584).
3. **Rojo de la llama sobre el rival** en f712–f714.
4. **Golpe 5 se lee como golpe a un caído**, con el mazo invisible y Tan cortada por el borde (C9).
5. **Carreras que no avanzan y salto al contacto** (C5, C6, C7): la queja del dueño.
6. **Golpes que no conectan en profundidad** (C2, C8).
7. **Subtítulos encimados** por tiempos que se pisan en los `.srt` (T1) y texto emborronado en f954–f956 (T2).
8. **Datos tapados por el humo**: «from GTA 5 to GTA 6» (f636–f668) y el tercer renglón de la cuenta (f750–f768).
9. **Caras tapadas**: mazo sobre Tan (f640, f676), humo sobre Tin (f840–f876), lápiz sobre Tin (f354–f360).
10. **Antes de publicar, aunque se corrija lo anterior:** sello «as of» con la fecha del día; `revisar_texto.py` con
    Hunspell; escucha humana del audio (el «it» de más y los 53 sonidos); firma de animación para D6; grieta de salida
    visible; unificar el dibujo de Tin y Tan entre firma y pelea (visera clara, grosor y color de tinta).

Costo de corregir: 0 créditos (todo es código y edición). Es una versión 3 de una pieza ya presentada: el dueño debe
saberlo antes de rehacerla.

**Veredicto general: CAMBIOS (CORREGIR).**

Firma: supervisor de continuidad, 2026-11-26. Esta revisión no cubre el sonido ni las fuentes de los datos.
