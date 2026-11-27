# Revisión de fotografía · short 4 (TIN-EN-S-004) · versión 3

Revisor: director de fotografía. Fecha: 2026-11-27.

## 1. Pieza revisada y límites

- **Pieza:** `06_final/tin_y_tan_short04_v3.mp4`. sha256 (12 primeros): **`511571dd5f4d`**, dato de producción. **No lo pude comprobar:** esta sesión no tiene consola, solo lectura de archivos.
- **Visto:** las 21 tiras completas (`rev_v3/tira_01` a `tira_21`, 1 de cada 2 fotogramas, f0–f984), cuatro fotogramas compuestos a media resolución (`f_0060`, `f_0306`, `f_0582`, `f_0588`, `f_0618`, `f_0642`, `f_0732`, `f_0762`), la dirección (3b y D22–D33), mi revisión de la v2, `control_encuadre_v3.md` y `color.txt`.
- **No pude comprobar:**
  - La pieza en movimiento: la velocidad de la cámara y la regla «un movimiento por toma» las juzgo por la deriva del decorado entre tiras, no por medición.
  - El audio y el sha.
  - El color de la v3: `07_revision/color.txt` es de la v1 y `color_v2.txt` es de la v2. No hay medición de `revisar_color.py` sobre la v3 y yo no puedo correrla. **Color medido: nada.** Lo de abajo es visual y está marcado como tal.
  - Los tamaños de letra: son estimados desde medias resoluciones, ± 4 px.
  - La interfaz de Shorts: sigue sin plantilla. Uso la hipótesis de ≈ 120 px a la derecha y y > 1600 abajo.
- Las cifras de corrección son valores de partida para probar en la vista previa.

## 2. Bloqueantes y altas de la v2: estado en la v3

| ID v2 | Estado | Prueba |
|---|---|---|
| B1 interacción 3D ilegible | **Resuelto.** Cámara alta, lente de 46°, carriles y diagonal: los golpes caen sobre el cuerpo y a una distancia que se lee | f60 (rival al frente, Tin y Tan a los lados, rejilla fugando), f582, f588, f642 |
| B2 cruce con cabezas fundidas | **Resuelto.** Tan cruza por delante de Tin con ≥ 90 px entre cabezas | f580–f592 (f588: Tin a la izquierda con el mazo, Tan en diagonal, sin solape). Eje roto solo en la portada (ver b1) |
| B3 televisor tapado por el subtítulo | **Resuelto en lo esencial**; **a medias** donde la tarjeta de 3 líneas lo tapa (ver M1) | f60, f642: televisor entre la tarjeta y la acción |
| B4 gag en el borde derecho | **Resuelto.** Tan, mostrador y bolas en el tercio central | f612–f636 (`f_0618`) |
| B5 humo sobre el dato | **Resuelto.** La tarjeta es opaca y el humo nace por encima o detrás | f642 (humo sobre la tarjeta, fuera de ella), f750–f770 (bolas tras la tarjeta, texto limpio) |
| B6 rival fuera de cuadro por arriba | **Resuelto.** La cámara lo acompaña | f320–f334: sube y baja dentro del cuadro |
| A1 Tan cortado a la izquierda (P6) | **Resuelto**, con margen justo (≈ 125 px; el control dice Tan 125–225) | f160 |
| A2 / A3 trío apretado, rival al borde | **Resuelto**, salvo f214–f218 (b2) | f338–f429, f204–f276 |
| A4 Tin y Tan pegados a los bordes (P19–P21) | **A medias.** Cabezas a ≈ 150 px y a ≈ 120 px del borde, con ≈ 700 px de escombro y rival pequeño en el centro | f750–f873 (ver M5) |
| A5 subtítulo con velo sobre el fuego | **Resuelto.** Panel opaco, el fuego no lo cruza | f618–f666, `f_0642` |
| A6 héroe abierto | **A medias** (ver A2 de abajo): ya no tapan al personaje con el estallido, pero siguen al ≈ 19 % del alto | f720–f748, `f_0732` |
| A7 detalle del lápiz | **Resuelto.** Primer plano real: cara de Tin, punta del lápiz que se vuelve bastón | f430–f440 |
| A8 cuadro vacío en el gancho | **Resuelto en f306–f336** (el rival se queda en cuadro); **sigue vacío** f32–f86 (M2) | f48, f60 |
| A9 tamaño al 21 % en f30–f85 | **No resuelto:** 427 px = 22 % (control P2) | f48–f68 |
| M1 cuadros de impacto | **Resuelto.** Un solo objeto legible (estante con bolas en f100, mostrador con grieta en f336) y el dato queda sobre las líneas | f100, f336, f562 |
| M5 disco de color fuera de paleta | **A medias:** en f718 queda un disco azul-gris translúcido con el fuego lavado | f718 (b3) |
| M6 anillo amarillo | **Resuelto** (D29): anillo de tinta, claro `#FFF4B8` con borde rojo oscuro | f728–f736 |
| M8 borrón sobre el subtítulo | **Resuelto.** En f954 el subtítulo sigue nítido bajo el borrón | f952–f956 |
| M10 zona segura | **Resuelto.** Pies en y ≈ 1340–1390 (control) y subtítulo en 1376–1552 | todas |

Veredicto sobre lo heredado: no queda B de la v2 sin resolver.

## 3. Defectos nuevos de la v3

Gravedad: B bloquea · A alta · M media · b baja.

### Altas

| ID | Fotogramas | Defecto | Corrección (valor de partida) |
|---|---|---|---|
| A1 | f298–f312 (P8, `f_0306`) | **La cara de Tin queda tapada** casi 0,5 s: el rival, el cuerpo del mostrador y la caja registradora le cubren la cabeza justo antes del golpe de f314. Se ve un casquete naranja detrás de la caja, sin ojos ni cara. El control no lo detecta porque el solape es con utilería y con el rival | En la tabla de cámaras (`tiempos.py`, P8): mover `cx` ≈ −0,4 a −0,6 u o bajar `h` para que la cabeza de Tin asome sobre la caja, o adelantar a Tin ≈ 0,3 u hacia la cámara (guion `tin_en_s_004.js`, su posición en K4). El rival debe quedar a la derecha de la cabeza de Tin, no delante de ella |
| A2 | f719–f749 (P18 héroe) | **Los personajes miden ≈ 19 % del alto** (359 px, control P18) en el plano que la dirección llama «héroe abierto». Son el momento clave y no se les ve la cara (puntos de ≈ 25 px). Además el héroe cae al 73 % del video, y el manual (cap. 11, regla 12) lo pide cerca de la mitad. En f728–f746 los pares de bolas con contorno, en los pies de Tin y Tan, se leen como ruedas de bicicleta | Dos caminos, decide producción:<br>1. Acercar P18 de `D` actual a ≈ 70 % de `D` y `h` +0,3, para llegar a ≈ 26–28 %. El estallido va detrás (ya está).<br>2. Si el clímax tiene que quedarse al 73 %, anotar en `direccion.md` §3 la excepción a la regla 12 con su porqué.<br>Quitar el contorno de tinta a las bolas de polvo que están en los pies (`escena.html`, polvo), o ponerlas detrás de las piernas |

### Medias

| ID | Fotogramas | Defecto | Corrección |
|---|---|---|---|
| M1 | f250–f306 | **La tarjeta de 3 líneas (hasta y ≈ 690) tapa el televisor** por completo y, en f288–f304, la parte alta del vuelo del rival (E2 del control: f286–f293). El televisor es el motivo central y queda oculto ≈ 1,9 s | Bajar el televisor `TV[1]` 0,3 u o subir la tarjeta a y ≈ 360. Mejor: partir a 2 líneas la tarjeta de f250–f304 |
| M2 | f32–f86 | **Tercio superior vacío ≈ 1,9 s** (cielo liso, y ≈ 0–560) entre el título y el primer dato. Es lo que pasaba en la v2 (A8, A9) y la tarjeta nueva no lo resuelve | Adelantar la tarjeta «GTA = Grand Theft Auto» a f60 (lo decide el editor) o subir el rótulo del título hasta f70 |
| M3 | f616–f622 | **Tin cortado por el borde izquierdo** (f618: la mitad de la cabeza fuera) y, a la derecha, las bolas y el mostrador cortados. Dura ≈ 8 f. El control marca Tin x −22 (P15) pero no lo lista en E1 | P15: `cx` −0,3 u o `D` +4 % |
| M4 | f624–f670 | **La grieta del suelo coincide con el borde derecho del subtítulo** y parece una raya que sale del panel: «De GTA 5 a GTA 6:» con trazos pegados al «:». No tapa texto, pero parece un fallo | Mover el decal de grieta del guion (suelo) ≈ 0,8 u más hacia el centro o a x < 0, o dejar el subtítulo sin grieta detrás |
| M5 | f750–f873 (P19) y f906–f948 | **Tin y Tan quedan en los extremos** (cabezas a ≈ 150 y ≈ 120 px) con el rival pequeño y el estallido gris en el centro. Funciona como duelo, pero la acción se aprieta en las esquinas, igual que A4 de la v2 | Acercar a Tin −0,2 u y a Tan +0,2 u hacia el centro, o `D` −5 % |
| M6 | f184–f482 y f512–f561 | **Tan fuera de cuadro 10 s** (≈ 30 % del video): P7, P8, P10 y P12 se encuadran con Tin y el rival. Es la animación (D32), pero el espectador no ve a «Tan» hasta f484 | Declarar la ausencia en la dirección. Si se quiere corregir: un fotograma de Tan al borde izquierdo en P10 (`cx` −0,6 u) |
| M7 | f82–f84 y f548–f552 | **Estrella amarilla a la vez que entra un dato nuevo** (la 3b prohíbe «nunca a la vez que un dato nuevo»). f550: estrella; f552: «rated M · 17 and over» entra. f84 → f86: «GTA = Grand Theft Auto» | Quitar la estrella 2–3 f antes del dato (en `componer.py`, la estrella a ≤ f547 y ≤ f81) o adelantar el dato 4 f |
| M8 | f648–f670 (E3 del control, f660) | Cabeza del rival pequeña y de sombra, **detrás de la cabeza de Tin** (≈ 40 % de solape): se lee como un adorno en el casco. El rival aquí es más pequeño que los dos personajes | Alejar al rival `x` ≈ 0,6 u de Tin en esos 20 f o subirlo a z de Tan |
| M9 | Líneas pequeñas del dato y subtítulo | Estimo la línea de apoyo («GTA 5: Sep 17, 2013») en ≈ 40–44 px y el subtítulo en ≈ 44–48 px, frente a los 48 px que pide la 3b. Se leen bien (tinta sobre papel ≈ 15:1), pero la regla escrita no se cumple por unos pocos píxeles. **No medido con herramienta** | `componer.py`: apoyo ≥ 48 px, sello «as of Nov 26, 2026» ≥ 44 px. Hay espacio en 380–700 |

### Bajas

- **b1 Eje en la portada:** Tan a la izquierda y Tin a la derecha en f0–f46 y f956–f984. En P21 (f906–f948) Tin va a la izquierda. El cambio cae en el borrón f954–f956. Excepción de eje que la dirección ya declara (D26 y la firma). Se queda.
- **b2 Rival cortado f214–f218** (E1 del control): 3 f en el borde derecho, tras el mostrador. No se nota.
- **b3 Disco del iris en f718:** translúcido, gris azulado, con el fuego lavado. Una vez, 1–2 f. Hacerlo sólido `#FFF4B8` con borde de tinta, como el resto de efectos.
- **b4 Tarjetas translúcidas al entrar y salir** (f86, f304, f338, f428, f480, f594): dos o tres fotogramas con el dato transparente sobre la acción. Es el fundido; si se quiere más limpio, entrada en 2 f.
- **b5 Utilería en primer término** (herramientas tiradas, cartel caído) en la franja de abajo (y > 1552), en f288–f470: da profundidad (paralaje) y no tapa nada. Se queda.
- **b6 Mando mostaza** recortado en la esquina de la tarjeta (f192–f216): decorado; ruido menor.

## 4. Cámara (D23)

- Cámara alta, diagonal, lente de 46° y acompañamiento de carreras y vuelos: **cumplido**. Se ve la deriva del decorado en P7 (f184–f282), P15 (f660–f690) y el seguimiento del rival (f284–f334). No vi temblor en ninguna tira.
- El rival cae «desde arriba» en el corte f336 y la cámara lo sigue: bien.
- Verticales con convergencia fuerte (estantes que se inclinan hacia dentro en f720–f748): es la lente abierta y el picado. Se lee como estilo, no como error. Lo marco por si el director creativo lo ve como deformación en caras (no las toca).
- **No comprobado:** velocidad real (≤ 8 % del ancho por segundo) y la regla de un movimiento por toma. Hace falta verlo en movimiento.

## 5. Color con intención (3b)

- **Medido:** nada de la v3 (ver sección 1).
- **Visual, contra la 3b:**
  - Dos neutros (papel frío `#DCE6EE` y suelo `#F4F1EA`, tinta casi negra): se mantienen en todo el video.
  - Acento amarillo: solo en dato, estrella y resaltador; no está en el fuego, el humo, el rival ni el subtítulo. **Incumplimiento puntual: M7.**
  - Marca: subrayado, no placa, en «GTA 7?», «GTA», «Grand Theft Auto», «Rockstar Games» y «GTA 6» (f248–f300, f340). Cumplido.
  - Efectos declarados: fuego `#FFF4B8` con borde `#B81414` y humo gris. El estallido rojo cubre ≈ 40 % del cuadro en f724–f746 (≈ 0,8 s). Está declarado aparte, y por mi lectura acompaña la emoción; la métrica la da la retención en f702 (3b).
  - Naranja de Tin y verde azulado de Tan: intactos. El humo gris junto a Tan sigue siendo el riesgo de daltonismo que anotó la 3b (riesgo 2); en f618–f640 la bola gris queda pegada a la cabeza de Tan y no se confunden por forma.
  - Riesgo 1 (amarillo y negro de la editora): **sigue pendiente la comparación con el amarillo de la marca**; no la hice y no tengo fuente cargada.
- **Legibilidad del dato:** tinta sobre papel opaco ≈ 15:1 (cifra de la dirección, no medida por mí); el amarillo con tinta ≈ 11,8:1. Ningún humo, fuego ni utilería queda detrás del texto del dato. Bien.
- **Legibilidad del subtítulo:** panel opaco, centrado, 140–400 px de 540 en la media resolución → x ≈ 300–860, y ≈ 1376–1552. Dentro de la zona segura que supongo. M4 y M9 son lo único.

## 6. Reparto del cuadro (D22) y tamaño de los personajes

| Zona | Medida | Estado |
|---|---|---|
| Dato (380–700) | Tarjeta opaca de 1–3 líneas, y ≈ 390–690 | Bien. Excepciones: M1 y M2 |
| Acción (705–1376) | Cabeza más alta 370–911; pies 1328–1393 (control) | Bien. Rival alto en f70–f81, f286–f293, f323–f329, f591–f595 (E2): son vuelos, lo toleré |
| Subtítulo (1376–1552) | Panel opaco | Bien |
| Banda y > 1552 | Suelo con rejilla y utilería | Libre, 19 % del cuadro, para la interfaz |

- **Tamaño** (control, alto de Tin o Tan): P2 22 %, P3 25 %, P6 25 %, P7 23 %, P12c 27 %, P14 20 %, P15 21 %, P18 19 %, P19 22 %, P20 29 %, P21 22 %. Cierres cercanos: P11 (73 %) y P12b (58 %). Reconocimiento: por color, claro. Pero los planos largos (P7–P10, P19–P21) quedan en 22–25 %, que es general, y el manual los pide cortos: P19 dura 124 f (4,1 s). Lo dejo como M6 y M5; no lo hago bloquear porque el color del personaje se reconoce.
- **Eje:** Tan a la izquierda y Tin a la derecha hasta el corte de P7; después Tin a la izquierda y el mostrador a la derecha, que es el mismo eje con la cámara desplazada (no hay giro de 180°). El único cambio de lado es el cruce de Tan en f580–f592 (D26) y la portada final (b1).

## 7. Tipos de plano

- Detalle: P11, f430–f440. Cumple.
- Subjetivo: la dirección dice P2, pero P2 es un plano de tercera persona; no hay POV real. M, para que el director creativo lo declare o lo rehaga.
- Héroe abierto: P18 (A2).
- Revelado: P19, 124 f con el rival entre los escombros. Funciona.

## 8. Veredicto

Veredicto: APROBADO

Ningún defecto B de fotografía: B1–B6 de la v2 están resueltos y probados arriba. Quedan 2 altas (A1: cara de Tin tapada f298–f312; A2: héroe al 19 % y al 73 % del video) y 9 medias, que **recomiendo corregir antes de publicar** pero que no impiden presentar la pieza como trabajo de alta calidad. Dos condiciones de mi firma:
1. El sha `511571dd5f4d` lo compruebo en `07_revision/firmas.md` contra la firma que se anote; yo no pude calcularlo.
2. La firma vale para el encuadre y la profundidad de las tiras. La cámara en movimiento y el color medido siguen sin comprobar; las hace quien tenga consola (`revisar_color.py`, vista en movimiento).

Firma: director de fotografía · 2026-11-27
