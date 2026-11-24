# Prompt de video para redes — [TÍTULO]

<!--
Plantilla para contenido dirigido a adultos o público general (redes, anuncios, piezas de marca).
NO se usa en series infantiles: el ritmo rápido, el gancho y el bucle van contra la guía de 1 a 3 años.
Estructura fija. No renombres los encabezados ni las etiquetas en negrita:
herramientas/validar_prompt.py las lee. Los textos entre corchetes se reemplazan.
-->

## 1. Ficha técnica

- **Proyecto:** [carpeta del proyecto]
- **Tipo:** [intro | capítulo | short | otro]
- **Número:** [número de capítulo o de short, o "—"]
- **Serie:** [nombre de la serie en video-studio/series/, o "ninguna"]
- **Objetivo de aprendizaje:** [solo en series infantiles: una sola cosa que el niño practica; si no, "no aplica"]
- **Generador:** [herramienta y modelo]
- **Aspecto:** [16:9 para capítulo e intro | 9:16 para short; ver formatos.md]
- **Duración total:** [N] s
- **Resolución de borrador:** [la más baja que ofrezca el generador]
- **Resolución final:** [solo para las tomas aprobadas]
- **Precio por segundo:** [costo de 1 s de video en tu plan, o "desconocido"]
- **Intentos estimados por toma:** 1

## 2. Elenco

<!--
OBLIGATORIO. Aquí queda definido quién sale en el video.
Solo personajes que existen en video-studio/personajes/. Una fila por personaje.
Si el video no lleva personajes, borra la tabla y escribe: Elenco: ninguno
-->

| Personaje | Papel en este video | Vestuario | Referencia que se sube |
|---|---|---|---|
| @[id] | [qué hace aquí] | [base u otra variación de su ficha] | personajes/[id]/referencias/[archivo] |

## 3. Idea en una línea

[Qué pasa y qué debe sentir quien lo ve.]

## 4. Estilo global

Bloque que se pega igual al final de todos los prompts de imagen y de video.

```text
[look, lighting, colour palette, lens and camera feel, texture — in English]
```

**Negativo global:**

```text
[lo que no debe aparecer: text, watermark, extra fingers, extra people, logo…]
```

## 5. Escenarios

- **[nombre_escenario]:** [descripción fija del lugar, hora y luz]

## 6. Tomas

<!--
Una toma = una acción + un movimiento de cámara. Si hay dos acciones, son dos tomas.
Método:
  imagen→video : se genera un keyframe y se anima (lo normal cuando hay personajes)
  texto→video  : solo para planos sin personajes
  edición      : se resuelve gratis en el montaje (texto, logo, foto con zoom, repetición)
-->

### Toma 1 — [nombre corto]

- **Duración:** [N] s
- **Personajes:** @[id] <!-- o: ninguno -->
- **Método:** imagen→video
- **Escenario:** [nombre_escenario]
- **Encuadre:** [plano general | medio | primer plano; ángulo]
- **Cámara:** [fija | paneo lento | travelling in…]
- **Acción:** [una sola acción, con principio y fin]
- **Audio:** [diálogo exacto entre comillas, o sonido ambiente, o "nada"]
- **Referencia:** [segundo del video de referencia que replica, o "—"]

**Prompt de keyframe:**

```text
[Bloque de identidad del personaje, pegado tal cual desde su ficha]
[pose inicial, encuadre, escenario]
[estilo global]
```

**Prompt de video:**

```text
[movimiento del personaje y de la cámara, en presente, una acción]
[estilo global]
```

## 7. Audio

- **Voz:** [TTS / grabada / la del generador; quién habla y en qué toma]
- **Música:** [archivo en 05_audio/ y su licencia, o "ninguna"]
- **Efectos:** [lista]

## 8. Montaje

- **Orden:** Toma 1 → Toma 2 → …
- **Transiciones:** [corte directo salvo que se indique]
- **Texto en pantalla:** [se pone en edición, nunca dentro del video generado]
- **Formato de salida:** [1920x1080 para capítulo e intro | 1080x1920 para short; fps del generador]

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | | |
| Keyframes | | |
| Remates en resolución final | | |
| **Total estimado** | | |

## 10. Restricciones críticas

Van al inicio de cada prompt de video, antes de la descripción. Son las que no se negocian.

```text
CRITICAL: no text, captions, subtitles, logos or watermarks unless listed in section 12.
CRITICAL: the character looks identical in every shot (same design, colors, proportions).
CRITICAL: hard cuts only, no morphing between shots.
CRITICAL: every figure, name or claim on screen comes from the project's facts file, with source and date.
```

## 11. Gancho, ritmo y cierre

- **Regla formal de la pieza:** [la idea única que la sostiene, en una frase: «una sola forma que nunca se corta»]
- **Rejilla de tiempo:** [pulsos (BPM y compases) o intervalos fijos de N s; la rejilla suma la duración total]
- **Gancho (0 a 1 s):** [tipo: movimiento | contraste | cifra] — [qué se ve y qué texto lleva, si lleva]
- **Empieza en movimiento:** [sí: sin intro ni logo | no, y por qué]
- **Motivo visual que vuelve:** [objeto, gesto o transición que firma el video]
- **Cierre:** [plano final; si repite el plano inicial para que el video encadene en bucle]
- **Llamado a la acción:** [uno solo, o "ninguno"]

Mapa de ritmo (los tiempos al décimo de segundo):

| Tramo | Segundos | Pulso o intervalo | Cortes por segundo | Qué pasa (una acción) | Respiro |
|---|---|---|---|---|---|
| [inicio] | [0,0–0,6] | [1] | [n] | [ráfaga de planos] | [no] |

Lo que sale se va antes de que entre lo siguiente. El movimiento se describe como mecánica
(qué parte se mueve, con qué curva, en qué orden entra y sale), no con adjetivos.

Tipos de plano disponibles: detalle o macro, héroe abierto, subjetivo, revelado desde desenfoque,
objeto que salta sobre el mismo fondo. Transiciones siempre motivadas (obturador lento,
desenfoque, destello). **No más de 3 destellos por segundo.**

## 12. Texto en pantalla y sistema de diseño

- **Tipografías:** [nombre y licencia]
- **Paleta:** [colores con HEX]
- **Referencias de movimiento:** [archivos en 01_referencia/]
- **Prohibido** (de 5 a 10 vicios concretos del generador o motor que se usa, no frases generales): mayúsculas centradas sobre degradado, tarjetas con degradado, animaciones lineales, [otros]
- **Márgenes seguros y escenario:** [margen en % por lado; qué proporción del cuadro ocupa el contenido]
- **Texto exacto:** todo texto en pantalla es el de la tabla de abajo, letra por letra
- **No afirmar:** [cifras, promesas o nombres que no deben aparecer]
- **Subtítulos:** [de 1 a 3 palabras, con la palabra clave resaltada | no lleva]

| Texto | Entra (s) | Sale (s) | Posición (% del cuadro) | Tamaño (% del alto) |
|---|---|---|---|---|
| [texto] | [0,0] | [0,0] | [x, y] | [n] |

En un short, todo texto queda dentro de la zona segura de `formatos.md`.

## 13. Sonido

| Golpe o efecto | Segundo | A qué corte va atado | Origen y licencia |
|---|---|---|---|
| [efecto] | [0,0] | [corte n] | [ver licencias.md] |

- **Música:** [archivo y licencia]
- **Voz:** [sí | no]

## 14. Motor y revisión

- **Cómo se hace:** [generador de video | gráficos por código (fotograma a fotograma) | mezcla]
- **Punto de control:** antes de generar o renderizar se presenta la lista de tomas sobre la rejilla y se espera el visto bueno.
- **Revisión:** `herramientas/revisar_fotogramas.py` sobre cada clip; se anota en `07_revision/`. En piezas por código: prueba corta de 5 s, un fotograma por pulso, hoja de contacto y comprobación de medidas.
- **Qué se marca:** imagen congelada, fotograma vacío, texto cortado o tapado, elemento fuera de cuadro, tirones, demasiado tiempo sin cambio.
- **Vueltas:** las correcciones por código son gratis (salvo servicios de pago, que van a `costos.md`); **las de generador no se repiten sin autorización del dueño** (`generacion.md`).
