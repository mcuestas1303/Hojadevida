# Firma del supervisor de continuidad — short 2 de Tin & Tan, vuelta 1

- **Fecha:** 2026-11-23.
- **Pieza revisada:** `06_final/tin_y_tan_short02_v1.mp4` (archivo del 2026-11-23 16:27; 1080×1920, 30 fps, 855 fotogramas, 28,5 s) y `06_final/portada_short02.png` (del 2026-11-21).
- **Cómo se revisó:** de cero, sin copiar `notas.md`. Hojas propias a 2 fotogramas por segundo (`vuelta_01/supervisor/hoja_01..03.jpg`, las tres vistas), 14 fotogramas a tamaño completo (0,3 · 1,5 · 3,5 · 6,0 · 10,0 · 12,5 · 14,5 · 16,5 · 19,0 · 20,5 · 22,8 · 24,5 · 26,5 · 28,3 s), la portada, 24 fotogramas de las transiciones (vueltas de hoja, llegada del contador, borrones), recortes ampliados de los textos y de la cara de Tin, y una medida de la caja de dibujo en los 855 fotogramas.
- **No revisado por mí:** control 3 (voz y audio: es del diseñador de sonido; no escuché nada) y la redacción de la sección 3b (es del director de fotografía). No pude comprobar en una fuente externa la fecha de salida de GTA VI: sigue siendo la de Wikipedia leída por el equipo el 2026-11-21.

## Veredicto general

**CAMBIOS.** Firmo 2 (Cifras), 7 (Marca, con salvedad) y 8 (Color, medición). No firmo 1 (Texto), 4 (Imagen y portada) ni 5 (Video). Todo lo que bloquea se arregla por código o editando texto: 0 créditos, un render de unos 90 s. La voz no se toca.

## Tabla por control

| Control | Qué miré | Evidencia | Resultado | Firma |
|---|---|---|---|---|
| 1. Texto | `revisar_texto.py` sobre `subtitulos.srt`, `render.py` y `miniatura.py` (`--idioma en`); el mismo filtro sobre la descripción de §8 del prompt; lectura a mano de cada texto en la imagen; glifos; zona segura; nombres propios | Los tres archivos: 44 textos, 0 errores, 0 avisos. Descripción: **2 errores** («Xbox» y «Rockstar» no están en el glosario). En pantalla leí: «GTA 5?», «how many days?», «Sep 17, 2013», «Nov 19, 2026», «GTA 5», «17», «13 × 365», «… days» (contador), «+3 leap days», «+63 days», «Sep 17, 2026», «GTA 6», «4,811 days», «age 13»: sin faltas, sin cuadros, «×» presente, ningún nombre propio en minúscula. **Fallan:** el `.srt` mezcla «G T A five» / «G T A six» (líneas 1 y 2) con «GTA 5» (línea 3); los dígitos clave con trazo salen deformados (defecto 3) | **NO PASA** | **NO FIRMADO** |
| 2. Cifras | Recalculé con `datetime`; comparé pantalla, subtítulos, guion y descripción; valores intermedios de los cuatro contadores, fotograma a fotograma; fechas de las hojas; bloques bisiestos | 17-sep-2013 → 19-nov-2026 = 4.811 días; 13 × 365 = 4.745; bisiestos 2016, 2020 y 2024 dentro del tramo = 3 → 4.748; 17-sep → 19-nov-2026 = 13 + 31 + 19 = 63; 4.748 + 63 = 4.811. Los 29-feb caen en los bloques 3, 7 y 11, que son los marcados. Contadores: 395 → 4.745, 4.745 → 4.748, 9 → 63, 4.748 → 4.811; solo suben, nunca pasan del final, nunca se ve «0». Visto en hojas: 646, 3,339, 4,483, 4,688, 4,741, 4,745 / 4,747, 4,748 / 9, 44, 53, 62, 63 / 4,748, 4,790, 4,810, 4,811. Todo entero: no hace falta «≈». Coma de miles correcta para EE. UU. La misma cifra en voz (guion), pantalla, `.srt` y descripción | **PASA CON SALVEDAD** (defectos 9 y 16) | **FIRMADO** |
| 4. Imagen | Cada personaje contra su ficha y sus hojas de referencia; lados y `espejo`; objetos de mano contra la definición; zona segura medida en los 855 fotogramas; forma del mando; nada de terceros | Colores, rodete, bufanda con dos puntas, gorra con botón y dos costuras, lentes con brillo, manos de punto y dos zapatos: correctos en todas las tomas. Tan a la izquierda con el gesto hacia la izquierda y las puntas al otro lado; Tin a la derecha sin espejo. `control` y `calendario` según la ficha. Nada de Rockstar ni Take-Two: ni logotipo, ni letra, ni paleta. **Fallan:** defectos 2, 4, 5, 6 y 7 | **NO PASA** | **NO FIRMADO** |
| 4.5 Portada | `portada_short02.png` medida y vista; fotogramas 0 a 1 s del video contra `ENTREGA_YOUTUBE.md`, «Portada de los Shorts» | Archivo: 1080×1920, 103 kB, «GTA 5?» en x 114–850, y 484–686 (dentro de la zona útil y de la franja 400–700), 2 palabras, clave en mostaza, sin la respuesta, 95 % en paleta. **Fallan:** en el video el mismo texto está en y ≈ 288–380, fuera de la zona útil (defecto 2); no hay caras (defecto 8); el archivo no es el fotograma 0 | **NO PASA** | **NO FIRMADO** |
| 5. Video | `ffprobe`, `revisar_fotogramas.py`, `postpro.py destellos`, mis hojas, diferencia entre fotogramas, preguntas fijas | Formato correcto. «Sin marcas»: ni congelados, ni vacíos, ni destellos (0 cambios fuertes de brillo). Ningún tramo de 8 fotogramas o más sin cambio. Bucle: fotograma 854 contra 0, diferencia media 2,35 de 255 (igual que dos vecinos de la toma 13): empalma. Los tiempos del `.srt` coinciden uno a uno con `linea_de_tiempo_voz.md` y con los silencios medidos hoy en `dialogo_110.mp3` (±0,03 s). Lo técnico pasa; **no firmo** porque el punto 5.4 exige los controles 1 y 3 sobre el archivo final, y los defectos 1 a 3 obligan a renderizar otra vez | **PASA CON SALVEDAD en lo técnico; pendiente del nuevo render** | **NO FIRMADO** |
| 7. Marca del canal | Paleta, tipografía, capitalización, lados y motivos contra `DESIGN.md`. Alcance: este Short y su portada; no volví a revisar banner, perfil ni marca de agua | Solo colores de la paleta más el blanco `#FFF8EC` de la hoja (declarado en el prompt). Inter Display Medium, minúsculas y a la izquierda, con «GTA», «Sep» y «Nov» en mayúscula por ser sigla y nombres. Portada con mayúscula inicial y 2 palabras. Tan izquierda con `espejo`, Tin derecha. Sin degradados. El nombre del canal no aparece en el video (no se exige) | **PASA CON SALVEDAD** (defecto 10) | **FIRMADO** |
| 8. Color (medición) | `revisar_color.py` sobre el video, la portada y, como pidió el director de fotografía, el tramo 21,0–27,5 s por separado; `--contraste` de cada par; acento plano por plano | Video: ≈ 93 % en paleta, saturación ≈ 17 %, luminosidad ≈ 89 %, entre segundos ±2 % y ±2 %. Portada: ≈ 95 %. Tramo 21,0–27,5 s: ≈ 94 %, ±2 %; el tomate no llega a dominante (los seis primeros son papel, verde azulado, marrón y grises de borde). Contrastes: tinta/papel 12,6:1; tinta/blanco 14,5:1; tinta/mostaza 8,0:1; tinta/tomate 3,5:1; mostaza/papel 1,6:1; tomate/papel 3,6:1. Toda clave en mostaza o tomate lleva contorno de tinta. Acento por plano: coincide con la tabla del prompt en las 13 tomas; mostaza y tomate no comparten plano como acento. Sección 3b completa, con veredicto APROBADO | **PASA CON SALVEDAD** (tinta/tomate 3,5:1, aceptado por escrito en 3b, juicio 3; `ficha.json` todavía no existe para copiar lo medido) | **FIRMADO** |

## Preguntas fijas (cap. 11, regla 20)

| Pregunta | Respuesta | Evidencia |
|---|---|---|
| ¿Movimiento y corte antes del segundo 1? | Movimiento **sí**; corte **no** | El mando retumba con estela desde el fotograma 0. El primer corte cae en 1,0 s justo, no antes |
| ¿Plano héroe cerca de la mitad? | **No** | El héroe principal es la toma 10 (21,0–23,5 s, ≈ 75 % del video). Hacia la mitad (≈ 14 s) hay un detalle. Está declarado y razonado en la sección 3 de la dirección |
| ¿Picos y respiros? | **Sí** | Respiros en 2,0–5,0 y 5,0–9,0; pico en 21,0–23,5; cierre en 27,5–28,5 |
| ¿Final que empalma con el inicio? | **Sí** | Diferencia media 2,35 de 255 entre el último fotograma y el primero |
| ¿Cada corte con su sonido? | **Sin comprobar por mí** | La tabla de §13 del prompt tiene un golpe por corte y `audio.py --verificar` da 47 de 47; oírlo es del diseñador de sonido |
| ¿Algo genérico? | **No** | Todo es dibujo propio |
| ¿Más de 3 destellos por segundo? | **No** | 0 destellos |
| ¿Todo con licencia? | **Sí** | `licencias.md` cubre voces, efectos, música, imagen, tipografía (OFL 1.1) y la mención nominativa. Ver defecto 17 |

## Defectos (con segundo y gravedad)

### Bloquean

1. **Subtítulos, líneas 1 y 2 (0,00–5,12 s):** el `.srt` dice «Remember buying G T A five at midnight?» y «…wait for G T A six?». Es la grafía para el generador de voz, no texto para el público, y la línea 3 del mismo archivo ya dice «GTA 5». Corregir a «GTA 5» y «GTA 6». Cuesta 0: editar el archivo.
2. **Portada dentro del video, 0,0–0,9 s y 27,6–28,5 s:** «GTA 5?» va en y ≈ 288–380 px. La regla del dueño dice que los primeros 0,5 a 1 s **son** la portada (un canal fuera del Programa de Socios no puede subir imagen propia), con el texto entre y 400 y 700 y nada de texto fuera de la zona útil (y 380–1440). `portada_short02.png` sí cumple, pero no es el fotograma 0: tiene el texto más grande y más abajo. Hay que llevar el texto de las tomas 1 y 13 a la posición y el tamaño de `miniatura.py`, comprobar que no toca el mando con el balanceo y que el bucle sigue empalmando. Cuesta 0: código y render.
3. **Dígitos clave deformados por el trazo de tinta:** el contorno de 0,06 em invade el interior del número. Se ve en «5» (0,0–0,9; 5,1–8,9; 27,6–28,5 y en la portada), «13» (9,2–10,9), «3» (13,7–14,9), «63» (17,8–19,3), «6» de «GTA 6» (19,4–20,9), en los 6 y 8 del contador (11,2–13,4) y en el «13» tomate (25,7–27,4). El «6» de «GTA 6», que es el tema del video, queda con la abertura cerrada y una línea interior. Al tamaño de teléfono se sigue leyendo; a tamaño completo se ve sucio. Arreglo: dibujar primero el trazo y encima el relleno (o trazo solo hacia afuera). Cuesta 0.
4. **Descripción (§8 del prompt):** `revisar_texto.py` da 2 errores: «Xbox» y «Rockstar» no están en `video-studio/glosario.txt`. Son nombres correctos: se agregan al glosario con su porqué y se repite el filtro hasta 0 errores antes de armar `ficha.json`. Cuesta 0.

### Convienen

5. **15,0–21,0 s (tomas 8 y 9), Tan con `pensando`:** cejas inclinadas hacia el centro, boca recta y ojos chicos sin brillo durante 6 s seguidos. Es la expresión de la hoja aprobada, pero en plano se lee como molestia o desconfianza, el mismo problema por el que se quitó `concentrado` de la toma 5. Que lo juzgue el director de animación; alternativa sin dibujo nuevo: `curiosidad` en una de las dos tomas.
6. **0,0–1,0 s, 27,5–28,5 s y portada, mando:** la palanca derecha se sale del cuerpo por abajo y corta el contorno entre las empuñaduras. Viene de las medidas del prompt (centro en +0,14 W con radio 0,07 W, contra 0,20 W de media altura). Subirla ≈ 0,03 W. Cuesta 0.
7. **Forma del mando:** silueta de «hueso» con empuñaduras circulares, sin cruceta, sin botón central, sin gatillos y sin símbolos: no reproduce la silueta de ningún mando comercial. La disposición (palanca izquierda arriba, derecha abajo al centro, cuatro botones en rombo) es la de varias marcas a la vez. Lo doy por genérico; si se quiere más distancia, poner las dos palancas a la misma altura. No bloquea.
8. **Portada sin caras:** la regla de portada pide las caras de Tin y Tan en la zona útil mirando el objeto; aquí solo está el mando (decisión del prompt: objeto desde el fotograma 0). O se acepta por escrito en «Decisiones del equipo» o se cambia. Lo decide el director creativo.
9. **22,3–22,5 s, llegada de «4,811»:** por el redondeo, el contador llega al valor final y pasa a tomate en 22,3 s, pero el `pop` y el ding están en 22,5 s: 0,2 s de desfase. Lo mismo en la toma 8: el valor llega a 4,748 en 15,9 s y el `pop` es en 16,6 s. Atar `pop` y ding al fotograma en que el valor llega.
10. **El lápiz de Tin no aparece en todo el video:** Tin lleva el calendario (tomas 4 y 12) o la mano vacía (toma 10). `DESIGN.md` lo da como motivo que vuelve y la ficha como «lo que nunca cambia»; el prompt (§11) y la dirección (§3) dicen que el lápiz está, y no está. O entra en un plano o se corrigen esos dos textos.
11. **5,0–9,0 s (toma 4):** 4 s en los que solo cambian el rebote al pulso y un empuje de 3 %; en mis hojas, ocho fotogramas seguidos casi iguales. Es el tramo largo más temprano del video. Conviene un cambio a mitad de toma (por ejemplo, la mano de Tin con el calendario o la mirada de Tan en ≈ 7,0 s).
12. **`02_prompt/direccion.md`:** las secciones 1, 2, 4, 5, 6, 7 y 8 están con la plantilla vacía; solo están escritas la 3 y la 3b. No pude comparar emoción ni actuación por toma contra la dirección: comparé contra el prompt.

### Menores

13. **25,5–27,5 s (toma 12):** el dibujo llega a x = 989 px (zona segura hasta 980): el calendario de Tin y el bloque 13 cuando late. Son 9 px, no 6. El calendario además queda pegado a la visera.
14. **9,0–11,0 s (toma 5):** Tan «señala la tira» con el brazo horizontal hacia la izquierda; la tira está arriba.
15. **13,5–15,0 y 17,5–21,0 s:** en `explica` y `piensa` el brazo del lado de las puntas pasa por detrás de la bufanda (fallo conocido de la ficha de Tan).
16. **Descripción:** «13 x 365» con letra x; en pantalla es «13 × 365». Unificar.
17. **`licencias.md`:** en las filas de voz, «(ID …)» es el ID del trabajo de generación, no el de la voz (los de las fichas son otros). Escribir «ID del trabajo».
18. **Fichas contra dibujo (no es de este video):** la ficha de Tan pide «rodete con cinta mostaza» y la cinta no se ve en ningún fotograma ni en la hoja de referencia (queda tapada por la cabeza). La ficha de Tin pide «cejas visibles bajo la visera» y en `eureka` (21,0–23,5 s) no hay cejas, igual que en su hoja de expresiones. Corregir el dibujo o las fichas.
19. **Salidas de texto:** en los 3 fotogramas de salida el texto sube hasta y = 239 px (zona segura desde 250), ya desvaneciéndose. Sin efecto visible.

## Rúbrica

**No existe.** En `07_revision/` solo están `controles.md` y `vuelta_01/`; el proyecto no es de serie y no tiene `ficha_tecnica.md`. En el prompt, §10 son las restricciones críticas y §14 la lista de qué se marca; no hay criterios con puntaje. Las repasé como lista:

| Punto de §10 y §14 | Resultado |
|---|---|
| Sin texto, logos ni marcas de agua fuera de la tabla de §12 | cumple |
| Personaje idéntico en todas las tomas | cumple |
| Solo cortes secos, sin transformaciones entre tomas | cumple (más el borrón de 2 fotogramas) |
| Cada cifra sale del archivo de datos | cumple |
| Contadores que solo suben y no pasan del final | cumple |
| Ningún texto sobre un personaje | cumple |
| Nada de Rockstar ni Take-Two; mando genérico y sin logos | cumple (defecto 7) |
| Imagen congelada o fotograma vacío | no hay |
| Texto cortado, tapado o que sigue sobre el plano siguiente | no hay («4,811 days» sigue en la toma 11 a propósito) |
| Elemento fuera de cuadro | no hay; 9 px fuera de la zona segura en la toma 12 |
| Glifos cuadrados | no hay |
| Bucle | empalma |
| Una reacción distinta de Tan por dato | cumple (defecto 5 sobre cómo se lee una de ellas) |

## Filtro de títulos

`revisar_titulo.py "How Many Days Did We Wait for GTA 6?" --canal tin-y-tan --idioma en --formato short --frase … --marca "GTA 6" --respuesta 4811`:

- Tal como se pidió: **NO PASA**, 1 error (M13, «casi igual a un título ya usado», parecido 1,00) y 1 aviso (M11, falta comprobar el descargo). El M13 es el propio título, ya anotado en `comercial/titulos_usados.json` para este mismo proyecto.
- Con `--proyecto 2026-11-21_tin_y_tan_gta6 --descripcion <descripción de §8>`: **PASA, 0 errores, 0 avisos.** El descargo está en la descripción. Queda la revisión humana del director creativo.

## Firmas

| Control | Firma |
|---|---|
| 1. Texto | **NO FIRMADO** |
| 2. Cifras | **FIRMADO** (con salvedad) |
| 4. Imagen y portada | **NO FIRMADO** |
| 5. Video | **NO FIRMADO** (lo técnico pasa; pendiente del nuevo render) |
| 7. Marca del canal | **FIRMADO** (con salvedad) |
| 8. Color (medición) | **FIRMADO** (con salvedad) |

Supervisor de continuidad, 2026-11-23. Veredicto general: `CAMBIOS`.
