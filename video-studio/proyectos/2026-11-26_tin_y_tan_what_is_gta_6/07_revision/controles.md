# Controles del short 4 (TIN-EN-S-004) — 2026-11-26

Video: `06_final/tin_y_tan_short04_v1.mp4` (1080×1920, 30 f/s, H.264 + AAC, 986 f = 32.87 s). Hojas de contacto de todo
el video (1 de cada 6 fotogramas): `07_revision/hoja_final_00.jpg` a `hoja_final_08.jpg`. **Ninguna persona ha visto ni
oído el video: esto son medidas y la revisión de las hojas por quien lo construyó.** Falta la firma del supervisor de
continuidad y de cada oficio.

## 1. Medidas

| Control | Herramienta | Resultado |
|---|---|---|
| Voz del diálogo armado | `revisar_voz.py` sobre `05_audio/dialogo_110.wav` | **COINCIDE: 74 palabras, 0 diferencias** (`voz_dialogo_solo.md`) |
| Voz en el video final (con efectos y percusión) | `revisar_voz.py` sobre el mp4 | **0 palabras perdidas; 1 palabra de más («it», entre «GTA 6» y «came out»)** que no está en la voz sola: el reconocedor la saca del sonido de fondo (ahí cae el choque contra el mostrador). No es «0 diferencias»: lo juzga un oído (`voz_video_final.md`) |
| Fotogramas muertos | `revisar_fotogramas.py` | Sin marcas: ni imagen congelada, ni fotogramas vacíos, ni destellos de más (`fotogramas/revision.md`). Detecta 9 planos; el guion tiene 23 (los cortes entre generales no cambian la luz) |
| Destellos | `efectos.comprobar_destellos` sobre los 986 fotogramas | **PASA**: 13 cambios bruscos en todo el video, máximo 3 en 1 s (tope 3) hacia 23.97 s; mayor salto de luminosidad 30.9 de 255 (tope 40); ningún salto a pantalla completa. La primera pasada dio 4 en 1 s: se retrasó el corte al plano del respiro (f750) |
| Firma del lápiz bumerán | `efectos.comprobar_firma` con la geometría de este fotograma 0 | **PASA**: despeje al texto 451.1 px, al televisor 112.1 px, a la cabeza de Tan 27.1 px y a la de Tin 45.7 px; giro 330.0°; velocidad máxima 58.9 px/f; centro dentro de la zona útil. Voz termina en f969 (c −17; tope c −17) y entra en f14. **Excepción declarada (D6):** el fondo del cierre es la tienda rota |
| Color | `revisar_color.py` con la paleta declarada (14 colores) | ≈ 92 % del cuadro dentro de la paleta (umbral 85 %); saturación media ≈ 11 %; luminosidad entre segundos ±2 % (`color.txt`). Contraste del dato: tinta sobre amarillo 11,8:1; tinta sobre fondo 13,5:1 |
| Sonido | `codigo/audio.py` (`05_audio/medidas_audio.json`) | Mezcla -14.0 LUFS, pico -1.3 dBTP; percusión -30.2 LUFS; efectos -31.0 LUFS (pico -8.0 dBFS, la explosión); silencio total en f688–f693: pico 0.0. 53 sonidos colocados por fotograma. **Nadie los ha oído** |
| Duración | `ffprobe` | 32.87 s (tolerancia de la dirección: 30 a 33 s) |
| Texto | `revisar_texto.py` | **No corrido en esta vuelta**; la ortografía sigue sin comprobar por máquina (falta Hunspell) |
| Rúbrica de la ficha | `puntuar_ficha.py` | **No corrido**: la herramienta no acepta las secciones de este canal |

## 2. Capa de datos (cada dato quieto 30 f o más)

| Dato | Entra (f) | Quieto (f) | Caja (px) |
|---|---|---|---|
| tarjeta 1 | 86 | 212 | [100, 421, 782, 494] |
| tarjeta 2 | 218 | 80 | [100, 511, 764, 577] |
| tarjeta 3 | 251 | 47 | [100, 593, 919, 659] |
| GTA 6 | 338 | 82 | [100, 446, 717, 685] |
| sexto | 432 | 41 | [100, 450, 938, 535] |
| rated M | 552 | 36 | [100, 453, 899, 554] |
| de 5 a 6 | 616 | 45 | [100, 456, 646, 525] |
| la cuenta | 750 | 122 | [100, 429, 904, 692] |
| respuesta | 890 | 56 | [100, 417, 833, 820] |

El primer dato queda quieto en f91 (3,0 s). **Fuera de zona:** el bloque de la respuesta baja hasta y = 820 (el sello «as of»
queda bajo la zona de datos 380–700, sobre la pared, sin tocar la franja de subtítulos 905–1085). El sello dice
«as of Nov 26, 2026»: **hay que volver a componer con la fecha del día de publicar**.

## 3. Conexiones del universo, medidas en el plano final (coordenadas en px)

| Pieza | Objetivo | Medido | ¿Cumple? |
|---|---|---|---|
| `mando_mostaza` | x 110–200, y 740–800 | centro (161; 770); 80 × 48 px | Sí |
| `caja_registradora_rota` | x 125–215, y 1362–1422 | centro (164; 1379) | En zona, **pero en el plano de cierre la tapa en parte la bufanda y el brazo de Tan** (no comprobé si en el plano anterior, P21, se ve entera) |
| Asterisco | x 516–564, y 1372–1420, ≈ 48 px | centro (540; 1396); ≈ 54 px de ancho | Sí; se dibuja en f918–f923 (6 f) |
| Salida por la grieta | de x 540 a x 890–960, y 1372–1420 | grieta en (926; 1396); f926–f941 (16 f) | Sí en coordenadas; **en el plano de cierre la grieta queda detrás de las piernas de Tin** |

Eventos activos: 22 f (tope 1,5 s). Nada del universo lleva voz ni texto.

## 4. Lista de pedidos (PARAMETROS.md, secciones 7 y 8)

| # | Pedido | ¿Está? | Evidencia / lo que falta |
|---|---|---|---|
| A1 | Pelea de acción con la gramática de las referencias | **Sí, con reserva** | 7 golpes con anticipación (K−12 a −7), pausa (K−6 a −1), contacto de 2 f, lanzamiento, vuelo y choque. **No se comparó plano por plano con la referencia** (lo pide el control); las poses son de esqueleto simple y se ven más rígidas que las de Alan Becker o Hyun's Dojo |
| A2 | Aceleración y desaceleración | **A medias** | Pausa antes de cada golpe, vuelos de 12 a 15 f, carrera lenta de 11 f antes del remate. El «reloj a 0,25» solo frena humo, polvo y escombros: los vuelos van a tiempo de animación, **sin borrón de movimiento** en lo rápido |
| A3 | Personajes 2D en un mundo con profundidad | Sí | Tienda 3D; se alejan y se acercan (del pasillo al televisor), pasan por delante y por detrás del mostrador, rompen estantes, proyectan sombra. **La cámara corta, no se mueve dentro del mundo** (solo empujes lentos): decisión de la dirección (sin temblor) |
| A4 | Fuego y humo | Sí | Llama plana de dos tonos en dos fases sobre el televisor (f574 y f614), humo con contorno, llamas pequeñas tras la explosión |
| A5 | Choques | Sí | Estante izquierdo (f100), postes (f187), mostrador (f336), estante derecho (f588), televisor (f715) |
| A6 | Explosión e implosión | Sí | Explosión por fases f717–f747; implosión f888–f905. Destellos: pasa |
| A7 | Sonidos de golpes | Sí, **sin oír** | 53 sonidos pegados al fotograma; sintéticos; los valida una persona |
| A8 | Daños que se quedan | Sí | El plano final muestra estante inclinado, postes y cartel caídos, mostrador partido, televisor reventado e isla volcada, quemadura en suelo y pared, banderines colgando |
| A9 | Rival con cuerpo | Sí | `@duda` v2; baja de tamaño con cada dato |
| A10 | Color: paleta por tema | Sí | Paleta C; 92 % dentro de lo declarado. **Cambio de producción:** el mostrador va en gris claro `#B9C6D2` (no `#666B76`) para que los personajes se lean delante. Pendiente de fotografía: comparar el amarillo con el de la editora |
| A11 | Entorno por tema y biblioteca | Sí | `entornos/tienda_de_videojuegos.js`, guion, poses, efectos y sonidos en `motor_de_accion/catalogo.json` |
| A12 | Armas dibujadas con tinta | Sí | Bastón, mazo y espada; ninguna arma de fuego; nada rojo sale del rival (cuando vuela delante de la llama se ve el rojo del fuego **a través** de la madeja, f708–f715: lo juzga un ojo) |
| A13 | Universo conectado | Sí, con dos reservas | Sección 3: caja rota y grieta, medio tapadas en el plano de cierre |
| A14 | Escalas (Short = una página) | No aplica a este video | — |
| — | Firma del lápiz bumerán | Sí | `comprobar_firma` pasa; los planos de firma son 2D (`palitos.py`) sobre la tienda del motor: **Tin y Tan miden distinto en la firma (487 px) que en la pelea (≈ 400 px)**; hay corte entre ambos |
| — | Subtítulos en español quemados | Sí | Franja 905–1085; `02_prompt/subtitulos_es.srt` |
| — | Suscripción antes del final (a prueba) | Sí | Tan, f483–f548 (16.1 s; 49 % del video) |
| — | Ningún prompt sin estadísticas | Sí | Brief, sección «Estadísticas en que se basa» |

## 5. Defectos vistos en las hojas y no corregidos

1. **Media pantalla vacía en los planos generales**: la acción ocupa el 45 % inferior; arriba queda la pared lisa para el dato. Entre f30 y f85 no hay dato y el tercio alto está vacío.
2. **Tramos quietos**: f338–f430 (el rival tendido sobre el mostrador mientras se lee la fecha) y f442–f483: poco movimiento durante ≈ 3 s y ≈ 1,3 s.
3. **Rival pequeño al final** (0,8 veces, entre escombros): en el respiro y en el golpe 6 cuesta verlo en un teléfono.
4. **Tan cruza por delante de Tin** en f570–f584 para ir a recibir el mazo.
5. **El subtítulo tapa el televisor y a veces la cabeza del rival** en los planos generales (la franja cae sobre el fondo de la tienda).
6. El «POV de Tan» (P2), la cámara cenital del mazazo (P15) y Tin y Tan «de espaldas» (P18) de la dirección **no se hicieron**: los personajes son dibujos planos de perfil; se resolvió con planos frontales.
7. La explosión no lleva el anillo amarillo (el acento no va en el fuego, sección 3b) y la percusión es más simple que la descrita (capas por golpe, sin «subir» tras cada dato de forma audible comprobada).
8. Tin dibuja el segundo bastón (f634) sin plano de detalle ni dato; es para el golpe doble.
