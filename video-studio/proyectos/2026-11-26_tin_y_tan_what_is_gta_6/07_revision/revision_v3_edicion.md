# Revisión de edición · short 4 (TIN-EN-S-004) · versión 3

Revisor: editor de video. Fecha: 2026-11-27.

## 1. Pieza revisada y límites

- **Pieza:** `06_final/tin_y_tan_short04_v3.mp4`, sha256 `511571dd5f4d` (12 primeros caracteres; calculado aquí con `sha256sum`, coincide con el de producción).
- **Formato (ffprobe):** 1080×1920, 30/1 f/s, 986 fotogramas, 32,867 s; H.264 High, yuv420p, 6,8 Mb/s; AAC LC 48 kHz **mono**, 32,866 s. Etiqueta `color_range` sin declarar. Sonoridad medida con ebur128: **−14,1 LUFS** integrados, LRA 2,9 LU, pico real **−1,1 dBFS** (tope −1: pasa por 0,1).
- **Qué miré:** las 21 tiras de todo el video (1 de cada 2 fotogramas, f0–f985), la detección de cortes por diferencia de fotogramas (sobre `_sin_audio.mp4`, numpy), fotogramas a resolución completa extraídos del mp4 final (f0, f30, f304, f718, f725, f954, f955, f956, f985) y los pares f985|f0, f718|f725, f955|f956, f304|f30. `revisar_fotogramas.py` sobre el video (salida en mi carpeta del scratchpad `…/ed/rf/`). Medí con el propio `componer.py` (importado, sin tocarlo) las cajas de cada panel de subtítulo y de cada tarjeta de dato. Leí `tiempos.py`, `componer.py`, los dos `.srt`, `medidas_composicion.json`, `direccion.md` (secciones 6 y D22–D33) y `revision_v2_fotografia.md`.
- **No pude comprobar:** el video en movimiento ni el audio (no oigo; la sonoridad y el pico sí están medidos); el aspecto real bajo la interfaz de Shorts (uso las zonas escritas en `ENTREGA_YOUTUBE.md` y `manual/07`, que vienen de vidIQ y no de una captura); la ortografía por máquina (`revisar_texto.py` devuelve «SIN COMPROBAR: falta Hunspell»; leí a mano los 12 subtítulos y los textos de la capa de datos: sin faltas, nombres propios con mayúscula); los fotogramas intermedios que las tiras no muestran (1 de cada 2), así que un defecto de un solo fotograma impar puede escapárseme. `entrega.py` sobre el proyecto: **1 error, «falta ficha.json»** (no es de edición; lo anoto en la sección 3).
- **Controles automáticos:** `revisar_fotogramas.py`: sin marcas (16 planos detectados, el más corto 0,3 s, sin imagen congelada, vacíos ni destellos). Destellos (`medidas_composicion.json`): PASA, 8 cambios bruscos (f100, 102, 336, 338, 430, 442, 564, 728), máximo 2 en 1 s (s 3,33), mayor salto 37,8 de 255 (tope 40; cerca del tope, en f102).

## 2. Defectos de edición de la v2: estado en la v3

| Defecto v2 | Estado | Prueba |
|---|---|---|
| T1: subtítulos que se pisaban 67 ms (dos textos encimados) | **Resuelto** | Los 12 subtítulos son consecutivos: cada uno termina en el fotograma donde entra el siguiente (`.srt` y quemados). En todas las tiras nunca hay dos paneles a la vez; cambio limpio en f171, f249, f316, f430, f483, f550, f614, f738, f838, f888. |
| T2 / M8: el borrón de 3 f emborronaba el subtítulo y el texto de portada | **Resuelto** | f955: escena borrosa, panel «Rockstar no ha anunciado ninguno. A hoy.» nítido; f956: «GTA 7? / Facts, Checked» nítido sobre escena borrosa. El panel sale en f956, no antes (srt 00:00:31,867). |
| B3 / A5 (franja de subtítulo sobre el televisor y el fuego con velo) | **Resuelto** | Subtítulo abajo (y 1377–1551), panel opaco 100 %; en f612–f670 el fuego rojo está por encima y no toca el texto. |
| B5 (humo sobre el dato) | **Resuelto** | Tarjeta opaca de papel con borde de tinta: en f752–f870 el humo queda detrás y el dato se lee igual. |
| M1 (líneas radiales cruzan el dato) | **Resuelto** | f100, f336, f562: las líneas van debajo de la tarjeta y del subtítulo. |
| M7 (letra de apoyo pequeña) | **Resuelto** | Líneas de apoyo 54–62 px, sello 50 px, dato principal 60–132 px (v2: 30–44 px). |
| M5 (disco de color fuera de paleta en los cuadros invertidos) | **No resuelto** | f718 (el segundo de los dos cuadros invertidos, f717–f718): disco gris azulado semitransparente con llama roja y puntos amarillos desaturados, color que no está en la paleta C. Ver M-1. El claro f724–f727 sí quedó plano (`#FFF4B8` con borde de tinta, ≈ 17 % del cuadro). |
| M6 (anillo amarillo en la explosión) | **Resuelto** | f728–f736: el anillo es de tinta (D29). |
| Cierre: borrón, empalme de bucle | **Resuelto** (con la excepción D6 declarada) | Ver 3.5. |

## 3. Medidas y defectos nuevos de la v3

### 3.1 Montaje: cortes, ritmo, planos

Cortes duros medidos (diferencia de fotograma > 40 sobre 255; los que siguen son cortes de plano o cuadros de impacto): f30, f70, f100–101 (impacto), f102, f157, f184, f283, f336–337 (impacto), f338, f430, f442, f483, f512, f562–563 (impacto), f564, f599, f719, f874, f906, f956. Más movimientos de cámara continuos en f82, f314, f574, f612, f662–f680.

Duración de cada plano (f / s): portada 0–29 (1,0) · 30–69 (1,3) · 70–99 (1,0) · impacto 100–101 · 102–156 (1,8) · 157–183 (0,9) · 184–282 (3,3) · 283–335 (1,8) · impacto 336–337 · 338–429 (3,1) · primer plano de Tin 430–441 (0,4) · 442–482 (1,4) · primer plano de Tan 483–511 (1,0) · 512–561 (1,7) · impacto 562–563 · 564–598 (1,2) · **599–718 (4,0; el plano largo del mazo al remate)** · 719–873 (5,2) · 874–905 (1,1) · 906–955 (1,7) · cierre 956–985 (1,0).

- **El plano largo del mazo al remate funciona.** f599–f718 son 120 f (4,0 s) con la cámara acompañando la carga de Tin y Tan (f612–f630 y f662–f680) y siempre algo que se mueve (mazo, carrera, caja, fuego); no se siente pulso plano. Es el plano más largo con acción continua y cae donde la dirección pide el pico.
- Los cortes de impacto de 2 f (f100–101, f336–337, f562–563) leen bien: cada uno lleva un solo elemento reconocible (estante inclinado, mostrador con grieta, televisor roto) y el golpe cae en el borde del cuadro. Pasan el límite de destellos.
- Cierre: el ritmo acelera hacia el final (plano de 3,1 s → 1,1 s → 1,7 s) y remata con el plano de portada, como pide el mapa de ritmo.
- **A-1 · Respiro demasiado largo, f750–f874 (125 f = 4,2 s, un solo plano fijo de 155 f desde f719).** La dirección (sección 2.2) pedía un respiro fijo de 80 f; la regla de ritmo del manual (respiros de 2–3 s) lo deja en 2–3 s. Aquí Tin y Tan casi no se mueven (f768–f870: balanceo mínimo, el rival se incorpora, brasas pequeñas); lo sostienen la voz («trece años y sesenta y tres días», f738–f836, y «¿Y GTA 7?», f838–f886) y la tarjeta de 130 f. Está en el tramo donde cae la retención antes de la respuesta. Corrección (valor de partida): en `motor_de_accion/guiones/tin_en_s_004.js`, tabla PLANOS, partir el plano en f≈800 con un corte a un medio de Tin y Tan (misma dirección de mirada) con un empuje de cámara de ≈ 5 % hasta f838, o dar movimiento a los dos personajes en f790–f838. Con esto el respiro queda en ≈ 2,5 s y el ritmo no cambia el momento del dato.
- **b-1 · Del plano de portada al primer plano de la pelea (f29 → f30) es un corte duro** (46 de 255): los personajes pasan de 487 px a ≈ 400 px y la cámara cambia. Está declarado por la firma (D20), igual que en la v2; lo anoto porque `ENTREGA_YOUTUBE.md` pide que el video siga desde la portada «sin corte brusco». No bloquea: es un plano de firma por regla del canal.

### 3.2 Capa de datos (tamaño, tiempos, tarjeta)

Tiempos medidos con `componer.py` (entrada → salida, fotogramas; «quieto» descuenta los 5 f de entrada y 3 de salida): tarjeta 1: f86–218 (124 quieta) · tarjeta 2: f218–251 (**33**, la más corta) · tarjeta 3: f251–306 (55) · «GTA 6»: f338–428 (82) · «sexto»: f432–481 (41) · «rated M»: f552–596 (36) · «de 5 a 6»: f616–669 (45) · «la cuenta»: f750–880 (122) · «la respuesta»: f890–954 (56). **Todo dato queda quieto 30 f o más** (regla cumplida; la tarjeta 2 pasa por 3 f y debe quedar como el mínimo).

- Tamaños: dato principal 60–132 px (renglón principal de la cuenta 106 px, de la respuesta 104 px), apoyo 54–62 px, sello 50 px. Pasa lo que pedía M7.
- Tarjeta opaca de papel `#F4F1EA` con borde de tinta y sombra dura: tinta sobre papel ≈ 15:1 en cualquier fondo (comprobado a la vista en f752–f870, f890–f954 con humo y escombros detrás).
- Entrada con golpe de 5 f y fundido de 3 f al salir: en f86, f304, f338, f426, f432, f480, f552, f594, f616, f668, f750, f878, f890 y f952 se ve un fotograma con la tarjeta translúcida (≈ 0,5 de opacidad) sobre la escena. Es el fundido de entrada o salida de 1 a 3 f; no se lee como error.
- **b-2 · Las tarjetas se salen de la zona útil de la portada/entrega (x 60–960, y 380–1440) en seis casos**, medidas incluyendo el borde de tinta y la sombra: tarjeta 3 hasta x 984; «sexto» hasta x 975; «la cuenta» y 384–727 (27 px dentro de la zona de acción, que empieza en 705); **«la respuesta» y 356–734** (24 px por encima de 380 y 29 px dentro de la acción; el texto llega hasta y 709, el medidor lo anota como `caja [100, 394, 793, 709]`). Los textos mismos caben salvo ese 709 contra 700. A y y 380 no hay botones de Shorts en la práctica (los botones del lateral derecho empiezan más abajo), y no se ve que tape caras ni acción en ninguno de los fotogramas revisados, pero **es una regla escrita** (D22: dato en y 380–700). Corrección (valor de partida): en `componer.py`, `datos()`, bajar la y inicial de «la respuesta» de 372 a 398 y el renglón del sello de 50 a 46 px (la tarjeta pasa a ≈ 382–712 y el texto a ≈ 414–690); en «la cuenta», y de 400 a 392 y apoyo de 54 a 50 px. Recortar a 940 el ancho máximo de las tarjetas con `partir()` o bajar el renglón a 56 px en «sexto» y la tarjeta 3.
- **b-3 · La tarjeta «rated M» sale en f596 y la voz de Tin termina en f612:** durante 16 f (0,5 s, f596–f612) se oye «mayores de 17» sin dato en pantalla. Corrección: `datos()`, cambiar `K["mazo"] + 10` por `L["T6"]["f1"]` (≈ f612).
- **b-4 · «GTA 6 out since Nov 19, 2026» entra en f338,** 22 f después del subtítulo y de la voz que lo dicen (f316). Está justificado por el cuadro de impacto (f336–f337) y por el vuelo del rival; si se quiere dato y voz a la vez, `K["K3"] + 24` → `L["T4"]["f0"] + 2` (≈ f318), pero tapa el vuelo del rival (se vería detrás de la tarjeta). Dejo la decisión a quien monta la pelea.

### 3.3 Subtítulos quemados

- Tiempos y encimado: ver sección 2 (T1 resuelto). Cada subtítulo empieza con su línea de voz (por construcción en `tiempos.py`/`componer.py`: `max(f0, 30)` a `min(f1 + 4, siguiente, cierre)`).
- Franja medida: paneles de **1 renglón** y 1412–1516; de **2 renglones** y 1377–1551; ancho máximo 808 px (T6: x 136–944), así que no pasan del borde derecho (≤ 944 contra 960). La franja pedida es 1376–1552: **cumplida** (sección «Sin resolver» 5 de la dirección: lo confirmo).
- Contra la zona segura de la interfaz de Shorts (15 % de arriba = y < 288; 20 % de abajo = y > 1536): arriba no hay texto (la «lámpara con ojo» del techo en f720–f750 es fondo). **b-5:** los paneles de 2 renglones llegan a y 1551, 15 px dentro del 20 % de abajo. La interfaz real empieza más abajo (título y canal hacia y ≈ 1600 en la práctica), así que no se ve un choque; solo contra la regla escrita. Corrección (valor de partida): `BANDA = (1362, 1536)` en `componer.py`.
- **M-2 · Tamaño de letra y largo del subtítulo.** Letra de 54 px (≈ 2,8 % del alto); en la vista del teléfono el panel se lee pequeño dentro de un cuadro grande (f30, f304: «¿Habrá un GTA 7?» ocupa 4,7 % del ancho del cuadro). El manual (`07_edicion.md`) pide «subtítulos grandes, 2 a 4 palabras por línea» y mi regla de oficio pide 1 a 3 palabras con la palabra clave en acento; los de este canal son la traducción completa de cada frase (hasta 8 palabras en 2 renglones), por pedido del dueño (2026-11-24), y esa traducción manda. Entre las dos, lo que sí puedo ajustar: **subir la letra a 64–68 px** (hoy hay holgura en el ancho: el panel más ancho mide 808 de los 960 útiles; la altura de dos renglones a 64 px es 200 px y habría que ampliar la franja a ≈ 1360–1560 o partir en tres renglones las frases largas). Valor de partida, a probar con la vista previa. No bloquea: se lee, con contraste 15:1.
- **b-6 · Cobertura del gancho:** la voz de Tan dice «¿Habrá un GTA 7?» en f14–f60, pero el subtítulo recién sale en f30 (D20: sin subtítulo en el plano de portada): 16 f (0,5 s) de la primera frase sin texto. La portada ya muestra «GTA 7?», así que un espectador sin sonido no pierde la idea. No lo toco.
- Silencios de subtítulo: f64–f84 (voz de Tan acabada, entrada de Tin), f684–f737 (carrera y explosión, 1,8 s sin voz): son silencios de voz reales, no huecos.

### 3.4 Los `.srt`

- `02_prompt/subtitulos_es.srt` y `02_prompt/subtitulos.srt` (inglés): 12 entradas cada uno, mismos tiempos, sin encimar y en orden, primera entrada 00:00:01,000 (= f30), última termina 00:00:31,867 (= f956, el cierre). Coinciden con lo quemado en cada fotograma que comprobé (f30, f172, f250, f316, f430, f483, f550, f614, f738, f838, f888).
- **A-2 · Los `.srt` no están en `06_final/`.** Mi regla pide `06_final/subtitulos.srt` y el CLAUDE.md pide la pista `subtitulos_es.srt` con el video. En `06_final/` hay solo mp4, `_sin_audio.mp4`, `miniatura.png` y `fotogramas/`. Corrección: que `hacer.sh` copie ambos a `06_final/` (o que se copien a mano) antes de pedir el sí para publicar.
- **A-3 · La sección 6 de `direccion.md` (Montaje y salida) quedó con los datos de la v2.** Dice franja de subtítulos y 905–1085, datos y 400–700 con x hasta 980, panel con opacidad 0,82, «Respiro 697–776, plano fijo de 80 f», tabla de densidad con f hasta 944 y bucle sobre 945 f; nada de la D22 ni del mapa real de la v3 (los tiempos medidos de arriba). Mi entrega pedida es esa sección y hoy contradice lo que muestra el video. Corrección: reescribirla con el mapa de la sección 3.1 (ritmo medido), la franja 1376–1552, los datos y 380–700, y cerrar el punto 5 de «Sin resolver». No toco `direccion.md` en esta revisión, por instrucción.
- Pistas ajenas a mi oficio pero que veo: `entrega.py` falla por `ficha.json` ausente; `controles.md` no tiene sección de la v3 (empieza en «versión 2»).

### 3.5 Cierre, borrón y bucle (fotograma 985 → 0)

- Borrón de 3 f en f954, f955, f956: dirección horizontal, solo sobre la escena; el panel de subtítulo (f954–f955) y el texto de portada (f956) quedan nítidos. T2 resuelto.
- **Empalme f985 → f0 (comparados a resolución completa):** lápiz en el mismo punto y ángulo (≈ x 325–445, y 810–835 en la mitad del par), Tan y Tin en la misma pose, la misma cabeza y expresión de curiosidad, el texto «GTA 7? / Facts, Checked» en el mismo sitio y tamaño, cámara idéntica. **Lo único que cambia es el fondo** (f985: tienda rota con la marca de explosión en la pared; f0: tienda entera con el televisor): es la excepción D6, declarada, que firma animación. Para un espectador es el momento «el lápiz salta a otra página»; coherente con D6.
- **Eje:** Tan queda a la izquierda y Tin a la derecha en el plano de cierre y en f0, pero en el último plano de pelea (f906–f955) Tin está a la izquierda y Tan a la derecha: **los dos personajes cambian de lado dentro de los 3 f de borrón** (f954–f956). Es la excepción de eje de la v2 (b3), que la firma impone; la dejo anotada para continuidad.
- **b-7 · Los dos planos de firma duran 30 f cada uno (1,0 s):** la voz de Tin termina en f969 (c −17) y el lápiz sale en f986−15 = f971 aprox.; el cierre queda corto pero cumple la firma (`comprobar_firma` PASA en `medidas_composicion.json`).

### 3.6 Color y destellos

- Destellos: PASA (ver sección 1).
- **M-1 · f717–f718, cuadros invertidos (2 f):** `fx.negativo_paleta(img, mascara, mezcla=0.55)` produce un disco gris azulado de ≈ 400 px con llama roja desaturada y puntos amarillo oliva, color que no está en la paleta C (el claro `#FFF4B8` y el rojo de la llama sí). Se ve en f718 de la tira y a resolución completa. Dura 2 f (0,07 s), pero es un fotograma con ≈ 12 % del cuadro en un tono sucio justo antes del claro. Corrección (valor de partida): en `componer.py`, `efectos_post`, rama `P["invertidos"]`: `mezcla=1.0` con borde de tinta de 8 px y relleno de paleta (tinta o `#FFF4B8`), sin transparencia; o quitar los dos cuadros (el claro de f724–f727 ya hace de golpe) y pasar sus 2 f al claro. Resta un cambio brusco al conteo de destellos.
- **b-8 · Lámpara de techo con forma de ojo en f720–f750:** la cámara baja del remate deja ver el techo (banda gris con un óvalo blanco centrado, y 0–70). Parece un ojo mirando a cámara durante 1 s. Es fondo dentro del 15 % de arriba; no bloquea, pero llama la atención entre la explosión y la cuenta. Corrección: en `tienda_de_videojuegos.js`, bajar la lámpara del centro a un lado o quitarla.

### 3.7 Formato y entrega

- 1080×1920, 30 fps, 986 f, 32,87 s (tolerancia de 30 a 33 s de la dirección): **cumple**.
- H.264 + AAC: **cumple**. Audio −14,1 LUFS y pico −1,1 dBFS: **cumple**.
- **b-9 · Audio mono.** Sin problema para YouTube, que lo duplica a dos canales; lo anoto por si se compara con el short 3.
- **b-10 · Falta etiquetar el espacio de color** (`color_range`/primarios sin declarar en el contenedor). Un reproductor puede interpretarlo como BT.601 y virar el amarillo y el azul claro; con la paleta decidida conviene `-colorspace bt709 -color_primaries bt709 -color_trc bt709 -color_range tv` al codificar en `componer.py`. No lo comprobé en un reproductor.
- **b-11 · `tin_y_tan_short04_v3_sin_audio.mp4` queda en `06_final/`:** es un intermedio; no debe subirse (la regla pide no guardar borradores).
- `miniatura.png`: se exporta desde el fotograma 0 (el código lo hace en `componer.py`); no la revisé aquí a 1080×1920 (la dimensión la da el mismo lienzo).

## 4. Resumen de defectos de edición

| ID | Gravedad | Dónde | Corrección (valor de partida) |
|---|---|---|---|
| A-1 | A | f750–f874 respiro de 4,2 s en un plano fijo | Partir en f≈800 con un medio y empuje de 5 % (`tin_en_s_004.js`, PLANOS) |
| A-2 | A | `.srt` fuera de `06_final/` | Copiar `subtitulos.srt` y `subtitulos_es.srt` a `06_final/` (`hacer.sh`) |
| A-3 | A | Sección 6 de `direccion.md` con datos de la v2 | Reescribirla con el mapa medido de arriba |
| M-1 | M | f717–f718 disco de color sucio | `mezcla=1.0` con borde de tinta, o quitar los dos cuadros |
| M-2 | M | Letra de subtítulo de 54 px | 64–68 px y ampliar la franja a ≈ 1360–1560 |
| b-2 … b-11 | b | Ver arriba | Ver arriba |

## 5. Veredicto

Ningún defecto B de edición: los defectos de edición que bloqueaban la v2 (subtítulos encimados, borrón sobre el texto, dato sobre humo, panel translúcido, tamaños) quedaron resueltos y medidos; el empalme del bucle es limpio; el plano largo del mazo al remate sostiene el pico; el formato, la duración y el audio cumplen. Los tres A son de ritmo (un respiro largo) y de entrega (los `.srt` y la sección 6), corregibles sin regenerar nada, y deben cerrarse antes de publicar: A-2 y A-3 antes de firmar la puerta de presentación, A-1 recomendado antes de publicar.

Veredicto: APROBADO

Firma: editor de video · 2026-11-27 (sobre sha256 `511571dd5f4d`).
