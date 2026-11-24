# Firma de fotografía (color) — short 3 de Tin & Tan, render 3

- **Fecha:** 2026-11-24. **Director de fotografía.**
- **Pieza:** `06_final/tin_y_tan_short03_v1.mp4` (render 3) y `06_final/portada_short03.png`.
- **Cómo lo revisé:** leí las hojas `vuelta_02/analisis/hoja_01.jpg` a `hoja_04.jpg` (un cuadro cada 0,5 s; el render 3 solo cambia 22,5–24,5 s, según el supervisor), `vuelta_03/par.jpg`, la portada, `vuelta_02/revisar_color.txt` y `revisar_color_portada.txt`, `vuelta_03/subtitulos_medidos.txt`, `vuelta_03/firma_supervisor.md`, `08_entrega/TIN-EN-S-003/ficha.json` y `palitos.py` (colores del lápiz). **No tengo Bash:** no corrí `revisar_color.py`; los porcentajes son los del equipo y los contrastes y ΔE los calculé a mano. No vi el video en movimiento; lo de las hojas es un cuadro cada 0,5 s.
- **Decisión escrita:** sección 3b de `02_prompt/direccion.md`.

## Veredicto: PASA CON SALVEDAD

No pido cambios de render. Las salvedades son de documentación y para el siguiente video.

## Evidencia punto por punto

| Qué se juzgó | Evidencia | Juicio |
|---|---|---|
| Paleta y medición | Video: ≈ 93 % en paleta (mínimo 85 %), saturación ≈ 16 %, luminosidad ≈ 90 %, entre segundos ±1 % (`revisar_color.txt`). Portada: ≈ 93 %, saturación ≈ 17 % (`revisar_color_portada.txt`). Las hojas muestran solo papel, tinta, marrón, mostaza, tomate y los colores de Tin y Tan; ningún verde de marca | PASA |
| Un acento por plano | Hojas 1 a 4: mostaza en la clave y un elemento en todas las tomas salvo la 8 (sin acento) y las 10–11 (tomate). En 24,5 s vuelve la mostaza («11 days» y marca de Huang). En las tomas 10–11 Tin no lleva lápiz | PASA |
| **Mostaza doble** (lápiz en vuelo + «11» de la portada) | El cuerpo del lápiz es `mostaza` en `palitos.py` (mismo `#E8B33B` que la clave). Son un solo acento usado en el título y en un elemento, que es la forma que pide el manual 13 §2.3, no dos acentos. En la portada el ojo va primero a «11» (≈ 105 px de alto, contorno de tinta, arriba a la izquierda); el lápiz (≈ 190 px de largo, leído en la imagen) queda entre las dos caras y lleva la mirada de Tan hacia Tin. La bufanda de Tan es identidad (manual 13 §2.4) | **PASA** |
| **Tinta sobre tomate 3,5:1** en «4,382» | Calculé: tinta/tomate 3,51:1, tomate/papel 3,61:1, tinta/papel 12,6:1. No pasa 4,5:1 ni 7:1 como relleno contra contorno. Pero el manual 13 §5.2 manda medir el contorno contra el fondo (12,6:1), y la cifra mide ≈ 134 px (7 % del alto) con trazo de 0,045 em. En `par.jpg` y en las hojas se lee de inmediato. La misma cifra va además en tinta: «days», «Jobs 4,382» y la tarjeta «4.382 días.»; no hay texto corrido en tomate. Con redundancia, el dato no depende del tomate | **PASA CON SALVEDAD** (no oscurecer el tomate: saldría de la paleta del canal sin ganancia) |
| Tomate frente al naranja de Tin | ΔE76 ≈ 24,7 (cálculo a mano; `DESIGN.md` pide ≥ 25 al acento de partida). Es el acento del pico, no el de partida; en 10–11 el tomate va arriba y el naranja abajo, con barra y contorno entre los dos | SALVEDAD: medir con herramienta la próxima vez |
| Goma del lápiz en tomate | `palitos.py` pinta la goma con `tomate`; aparece como franja pequeña en todo plano con lápiz, incluida la portada. El negativo del prompt dice «tomato red outside the reveal shots» | Es identidad del objeto, no acento. Aclarar el negativo (ver correcciones) |
| **Legibilidad de la banda de subtítulos** | Tinta `#2B2420` sobre panel de papel translúcido (0,82), 86 px (4,5 % del alto), 12,6:1; **0 píxeles dibujados bajo el panel** en las 12 tarjetas (`subtitulos_medidos.txt`), así que el fondo efectivo es papel puro. Hueco mínimo 12 px a cabezas (toma 10) y 16 px a gráficos; sin tapar nada. Sin acento en los subtítulos: se leen en tinta en las hojas 1 a 4 y en `par.jpg`. En los 3 fotogramas de entrada y salida de cada tarjeta el texto baja a gris (se ve en las hojas): 0,1 s | **PASA** (la duración de «¿Casi 12 años?», 0,9 s, la dejó el supervisor como salvedad; no es de color) |
| Rótulos pequeños de las barras (56 px) | Tinta sobre papel 12,6:1, sin acento; legibles en las hojas. Son el texto más pequeño del video (≈ 19 px a 360 px de ancho) | PASA, en el mínimo |
| Marcas mostaza de 4 px (toma 9 Altman, toma 12 Huang) | Mostaza sobre papel 1,6:1 y sin contorno posible: se ven como un hilo pálido en las hojas. Lo que informa son la clave y el nombre de la barra, en tinta | SALVEDAD menor (siguiente video: marca de 8 px con borde de 2 px) |
| Peso del tomate en el pico | En las hojas el tomate aparece de 22,07 a 24,4 s (≈ 2,3 s de 31). No aparece entre los dominantes del video completo (esperable) | Falta la medición de los cuadros de 21 a 24,5 s por separado (la pidió el director de fotografía en el short 2 y el supervisor no la hizo) |

## Umbral de color para videos con profundidad (`DESIGN.md`, «pendiente de firma»)

**Lo que se mide aquí:** con profundidad real (desenfoque `apertura` 0,018, niebla 0,30, sombras de contacto 0,25–0,30), el video da ≈ 93 % y la portada ≈ 93 %. No se repite el ≈ 82 % de la prueba del 2026-11-23 (la que describe `DESIGN.md`; no la vi). Mi hipótesis: aquella prueba tenía fondos con más capas desenfocadas; aquí las capas lejanas son una silla, un calendario y una mesa sobre papel liso.

**Lo que firmo desde hoy** (queda como criterio vigente; el editor debe copiarlo a `DESIGN.md`, yo no lo toqué):

1. **Piso para el video final: 85 % en paleta, el mismo de siempre.** Este video lo pasa con 8 puntos de margen; la profundidad por sí sola no justifica rebajarlo.
2. **Franja de excepción: de 75 % a menos de 85 %** solo si se entrega a la vista **la medida del fotograma de control** (mismas capas, sin desenfoque, sin sombras y sin grano) y esa da **≥ 85 %**, y el director de fotografía lo firma caso por caso. Bajo 75 % no pasa nunca. Si el control da menos de 85 %, hay un color nuevo de verdad: se corrige.
3. **Saltos de luminosidad entre segundos:** los del manual 13 (≈ 15 %), sin relajar. Este video: ±1 %.
4. **Lo que NO firmo todavía:** el punto 2 del borrador («ningún dominante con más del 3 % del cuadro a ΔE76 ≥ 12 de la recta entre dos colores de la paleta»). Falta un dato: la salida de `revisar_color.py` con los ΔE de cada dominante. En este video hay un dominante `#545F54` con 3,8 % (verde grisáceo) que no está en la paleta. Por su valor no cae en la recta tinta–papel ni en la teal–tinta; parece una mezcla de tres (cabeza de Tan, contorno de tinta y papel), no un color nuevo, y la regla de «recta entre dos colores» la daría por mala. Para fijar el criterio necesito: (a) esa salida con ΔE de ese dominante contra la paleta, (b) la medición del fotograma de control de este video. Con eso decido si el criterio se amplía a mezclas de tres colores de la paleta (mi inclinación) o se descarta. Hasta entonces el punto 2 del borrador es solo aviso, no bloqueo.

## Correcciones (ninguna cambia el render)

1. `DESIGN.md` (sección «Paleta», «Un color de acento por plano» y la línea «tomate … nunca en el mismo plano que la mostaza») y `prompt.md` (§5 «mostaza y tomate nunca comparten plano»; negativo global): reescribir como **«nunca comparten plano como acento (la bufanda de Tan y el cuerpo del lápiz son identidad; la goma del lápiz es tomate de identidad y no cuenta)»**. Es la misma corrección que pedí en el short 2 y sigue sin hacerse. Responsable: editor / director de prompts.
2. `ficha.json`, campo `color`: `medido` cita el render 2 y «falta la firma del supervisor». Poner: «render 3: color firmado por el supervisor (solo medición) y por el director de fotografía con salvedad; `direccion.md` §3b». Dejar `acento` en `#E8B33B` y el tomate nombrado como excepción del pico (ya lo está en `por_que`). Responsable: editor.
3. Siguiente video: (a) marcas mostaza de 8 px con borde de tinta de 2 px o dejarlas en tinta; (b) pasar `revisar_color.py` también a los cuadros de 21 a 24,5 s y al fotograma de control con efectos apagados; (c) medir ΔE tomate–naranja con la herramienta.

## Salvedades que acepto (no bloquean)

1. Tinta/tomate 3,5:1 en la cifra del pico (se lee por contorno, tamaño y redundancia).
2. Tomate–naranja ≈ 24,7, apenas bajo el 25 del acento de partida (cálculo a mano).
3. Marcas mostaza de 4 px casi invisibles sobre papel; la información no depende de ellas.
4. Rótulos de barras en el mínimo de tamaño.
5. Dos tonos de acento en 31 s (mostaza y tomate): cumple «un acento por plano», no «uno por pieza»; hipótesis a prueba, no separable del efecto de la cifra y el sonido.

Director de fotografía, 2026-11-24. **Veredicto: PASA CON SALVEDAD.** Falta la firma del control 8 completo, que es del supervisor y ya la dio sobre la medición.
