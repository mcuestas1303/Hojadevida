# 11 · Retención, motion graphics y revisión fotograma a fotograma

> Pedido del dueño (2026-11-20), textual: *«Lo que dice en los ultimos 2 videos necesito que se implemente en el
> equipo creativo de producción y en generador de prompts lo que aplique»*.
>
> Fuentes: el desglose de un video viral de **willrvail** (instagram.com/p/Df2NAP3R7KC) y el estudio de motion
> graphics con Claude Code de **silvesttre.ai** (instagram.com/p/Df-FD2sMnGa), más tres videos del mismo lote
> (adley, ashharrisprod y uno sobre el director de fotografía Robby Müller). Los vio un ayudante desde otra
> conversación; esto es un resumen, **no está probado con datos propios**. Se trata como hipótesis: se aplica y se mide
> con `estadisticas.py` (cap. 10).
>
> Las pantallas del video del estudio de motion graphics son recreaciones: el método no está demostrado.

## Excepción infantil

En la serie `granja` (1–3 años) **mandan `infantil/guia_1_a_3.md` y `series/granja/serie.md`**. De este capítulo
no aplican ahí: afirmaciones de contraste o cifras en el gancho, capítulos «1/5», curiosidades sin resolver,
el ritmo de ~50 cambios en 30 s, la aceleración final, los destellos y los subtítulos. Sí aplican: la revisión
fotograma a fotograma (18–20), los motivos visuales que vuelven (8), el fondo constante (8), el sonido atado a
la línea de tiempo (17, en versión suave) y el final que empalma con el inicio (3, como saludo y despedida iguales).

## Reglas por rol

### Guion — `director-creativo` (y `guionista-interactivo` solo en lo que permita la guía infantil)

1. **El segundo 0–1 se resuelve con movimiento** y una afirmación de contraste o una cifra concreta. Nada de intro
   ni logo.
2. **Capítulos numerados visibles** («1/5») o una lista que crece en pantalla, cuando el video enumera cosas.
3. **El cierre empalma con el inicio** para que se vuelva a ver (loop). Se escribe a la vez que el gancho.
4. **Toda cifra con fuente**; un solo llamado a la acción; no se promete lo que el video no da.
5. **Dos ganchos** escritos para probar (A/B en publicaciones distintas o en la miniatura), y **curiosidades
   encadenadas sin resolver**, yendo un paso por delante del espectador (adley).

### Diseño — `director-de-fotografia` y `director-de-prompts`

6. **Sin referencias reales cargadas no se renderiza:** tipografías, paleta, recursos, ejemplos de movimiento. En el
   estudio eso es la carpeta del personaje (imagen aprobada, hojas de emociones) y, para gráficos, un `DESIGN.md`
   del proyecto con tipografía, colores y ejemplos.
7. **Prohibido lo genérico de IA:** mayúsculas centradas sobre degradado, cuadrícula de tarjetas con degradado,
   animaciones lineales, «cinematic masterpiece, 8k», luz azul y naranja por defecto sin motivo.
8. **1 o 2 motivos visuales que vuelven** (el crayón lila de Lumi, la tecla de Spike, el copete de Tiky que rebota)
   y **el mismo fondo entre planos de objeto** para dar continuidad.
9. **Subtítulos de 1 a 3 palabras** con la palabra clave en el color de acento del personaje
   (`postpro.py subtitulos` + `.ass` con color si hace falta; nunca en infantil 1–3).

### Animación y gráficos con código — `director-de-animacion`

10. Para gráficos (textos animados, listas, números, transiciones), **Claude escribe el código que pinta cada
    fotograma**; todo depende del **número de fotograma**, no del reloj, para que cada render salga igual.
11. **Movimiento con física de muelles** (masa, rigidez, amortiguación) declarada por elemento; nada de
    interpolación lineal.
12. En videos de **más de 20 s**, al menos un plano de cada tipo: **detalle, héroe abierto, subjetivo (POV),
    revelado**. El plano héroe va cerca de la mitad.
13. **Transiciones motivadas:** obturador lento, desenfoque de movimiento, destello; deformar solo en un golpe.

Herramientas de gráficos con código (ninguna instalada; **instalar pide el sí del dueño**):

| Herramienta | Licencia y costo | Para qué |
|---|---|---|
| **HyperFrames** (HeyGen, github.com/heygen-com/hyperframes) | Apache 2.0, gratis | motor de render fotograma por fotograma con skills para Claude Code, `DESIGN.md` y ciclo de revisión. **Probarlo antes de construir un motor propio.** |
| **Remotion** | gratis hasta 3 personas; desde 4, desde US$25 por puesto al mes | videos con React, fotograma a fotograma |
| **Earshot** (github.com/Leonxlnx/earshot) | MIT | efectos de sonido |

Mientras no estén instaladas, los gráficos simples se hacen con `postpro.py` (zoom, subtítulos, fundidos) o en
CapCut/DaVinci con el plan del editor.

### Edición — `editor-de-video`

14. **Mapa de ritmo antes de renderizar:** tramos densos y respiros de 2–3 s, nunca un pulso plano. Referencia del
    desglose viral: unos 52 cambios en 30 s, **no parejos**. Va en `direccion.md` §6.
15. **Acelerar hacia el final y rematar con el plano del inicio** (cierra el loop de la regla 3).
16. **Material grabado** (modo A): transcribir el crudo con tiempos (Claude no oye: hace falta una transcripción con
    tiempos, del dueño o de una herramienta que se instale con su permiso), **primer corte quitando muletillas y
    pausas** (`postpro.py pausas` y `quitar-pausas`), después color, tomas de apoyo, gráficos como código y audio
    (ashharrisprod).

### Sonido — `disenador-de-sonido`

17. **Cada corte, destello o salto con su golpe**, en una **lista de golpes atada a la línea de tiempo**
    (`direccion.md` §5). Sonidos generados (Mirelo en Higgsfield, código con Web Audio o Earshot si se instala),
    grabados aparte y unidos con ffmpeg (`postpro.py mezclar --efectos archivo@segundo`). Música solo con licencia.

### Revisión — `supervisor-de-continuidad`

18. **Después de cada render, hoja de contactos a 2 fotogramas por segundo**
    (`analizar_video.py <video> <carpeta> --cada 0.5`); en los tramos rápidos, todos los fotogramas.
19. **Marcar fotogramas muertos:** vacíos, congelados, elementos fuera de cuadro, texto cortado o tapado, tirones,
    demasiado tiempo sin cambio, algo genérico. **Rehacer solo esos tramos** y anotar cada vuelta en
    `revision_produccion.md`. Lo que es código o edición propia se rehace gratis; lo que hay que volver a generar con
    créditos necesita la autorización del dueño, pieza por pieza (`generacion.md`).
20. **Preguntas fijas** en cada revisión:
    - ¿Hay movimiento y corte antes del segundo 1?
    - ¿Hay plano héroe cerca de la mitad?
    - ¿Hay picos y respiros, o el pulso es plano?
    - ¿El final empalma con el inicio?
    - ¿Cada corte tiene su sonido?
    - ¿Hay algo genérico?
    - ¿Hay más de 3 destellos por segundo? (`postpro.py destellos`; límite de accesibilidad)
    - ¿Todo tiene licencia?

### Grabación propia — `director-de-fotografia`

21. Si el dueño graba con poco equipo, **usar la luz que ya está:** ventanas, sol, faroles, neón (lección atribuida
    al director de fotografía Robby Müller). Se le indica dónde pararse respecto a esa luz.

## Cuidados

- **No se reutiliza metraje ajeno sin permiso.** El desglose viral usa un video ajeno con crédito, y el crédito no da
  derechos. En el estudio: modo B copia la fórmula, nunca las imágenes (cap. 06).
- **Esfuerzo alto del modelo solo para componer y revisar**: gasta mucho más. El resto del equipo trabaja en el
  modelo y esfuerzo por defecto.
