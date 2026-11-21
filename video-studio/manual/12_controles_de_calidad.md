# 12 · Controles de calidad (bloqueantes)

> Regla del dueño (2026-11-21), textual: «un error ortográfico puede matar el video […] independiente del público
> no son cosas que tengan flexibilidad. […] estamos produciendo en alta calidad, no amateur».
> Origen: el banner salió «tin & tan» en minúscula y nadie del equipo lo vio.

## Cómo funcionan

- Cada control tiene **un responsable que lo firma**, una herramienta y un criterio de paso. No hay «casi»: o **PASA**
  o **NO PASA**, y una pieza que no pasa un control no avanza a la etapa siguiente ni sale del estudio.
- Quien hace la pieza se revisa primero; el **supervisor de continuidad** vuelve a revisar y firma. Dos pares de ojos
  siempre, aunque la pieza sea chica (un banner, una etiqueta, una línea de subtítulo).
- Cada control queda escrito en `<proyecto>/07_revision/controles.md` (o en la carpeta de la pieza, si no es de un
  proyecto): control, PASA o NO PASA, quién, fecha y la evidencia (salida de la herramienta, cálculo, hoja revisada).
- Un error que se encuentra en algo **ya entregado o subido** se le avisa al dueño enseguida: qué está mal, dónde,
  y qué cuesta arreglarlo. No se arregla en silencio ni se rehace sin su sí (`generacion.md`).
- Lo que un control no puede comprobar con herramienta se lee a mano y se deja escrito que se leyó a mano.

## 1. Texto: lo firma el supervisor de continuidad

Aplica a **todo texto** que vea el público: títulos en pantalla, subtítulos, miniatura, banner, foto de perfil,
marca de agua, título, descripción, etiquetas, hashtags, descripción del canal y textos de las hojas de personaje.

1. `python3 video-studio/herramientas/revisar_texto.py <archivos o carpeta> --idioma <en|es|pt>` con **0 errores**.
   Revisa nombres propios, ortografía (Hunspell con los diccionarios de LibreOffice de inglés, español y portugués
   de Brasil, más `video-studio/glosario.txt`; en una sesión nueva se instala con
   `bash video-studio/herramientas/instalar_corrector.sh`), espacios, palabras repetidas,
   comillas y paréntesis, ¿? y ¡! en español, oraciones en minúscula y separador decimal. `entrega.py` lo corre solo
   sobre la ficha y los subtítulos. El texto que se dibuja con código se revisa pasando los `.py` del render.
2. Cada **AVISO** se lee uno por uno y se resuelve o se explica por escrito.
3. **Lectura completa a mano**, palabra por palabra, del texto tal como sale en la imagen o el video (no del código):
   tildes y eñes (español y portugués), concordancia, mayúsculas, que el idioma no se mezcle.
4. **Nombres propios con mayúscula inicial, siempre**: «Tin & Tan», «Tin y Tan», «Tiky», «Lumi», «Spike», nombres de
   canal, también en hashtags (`#TinAndTan`). El estilo en minúsculas de un canal **no** alcanza a los nombres.
5. **Unidades y formato de números del público**: EE. UU. en pulgadas y pies, con punto decimal y coma de miles
   (`4.76`, `1,170`); público hispano en sistema métrico, con coma decimal (`4,76`).
6. **Glifos**: en la imagen ya renderizada no hay cuadros ni signos que la tipografía no tenga (lección de «≈» y «→»).
7. **Legibilidad**: el texto se lee con la pieza al tamaño en que la ve el público (miniatura a 25 %, perfil en
   círculo chico, short en un celular) y queda dentro de la zona segura.

## 2. Cifras y datos: los escribe el director creativo, los recalcula el supervisor

1. Cada número lleva su cálculo escrito y su fuente con fecha. El supervisor **lo recalcula** desde cero; no se copia.
2. **Decimales y fracciones se aproximan, siempre con «≈»** (regla del dueño, 2026-11-21, textual: «cuando tengas
   decimales, centésimas o milésimas, incluso millonésimas, solo aproxima y usa el símbolo de aproximación»).
   En pantalla, miniatura, subtítulos y descripción: «≈ 422 ft», no «421.9 ft»; «≈ 1.9 in/s», no «1⅞ in/s»; «≈ 4.8
   cm/s», no «4.76 cm/s». Se aproxima al entero cuando se entiende igual, y a lo sumo a un decimal. En la voz, la
   aproximación se dice con palabras: «about», «almost», «unos», «cerca de», «casi». La única excepción es una cita
   textual de una fuente entre comillas, que se copia tal cual. `revisar_texto.py` lo marca como error.
   «≈» está en Inter Display Medium (comprobado el 2026-11-21); en otra tipografía se comprueba el glifo antes.
3. **Redondeo, no truncado**: 421,9 se aproxima a ≈ 422, nunca a 421.
4. **Una sola versión de cada número** en voz, pantalla, subtítulos, descripción y miniatura; nunca dos números
   distintos para lo mismo.
5. Los supuestos (diámetro promedio, velocidad) se dicen en la descripción como supuestos.

## 3. Voz y audio: lo firma el diseñador de sonido

1. **Transcripción contra guion**: se escucha la pieza completa y se compara lo que dice la voz palabra por palabra
   con el guion. Palabra cambiada, cortada, mal pronunciada o con acento de otro idioma = NO PASA (lección de la voz
   de Juan, que sonaba a italiano o portugués).
2. Volumen integrado **−14 LUFS ±1** y pico real **≤ −1 dBTP** (`postpro.py normalizar` y `postpro.py info`).
3. Sin clics, cortes de respiración, silencios muertos, saturación ni música que tape la voz.
4. Voz, idioma y velocidad según `voces.md` del canal.

## 4. Imagen: la arma el editor, la firma el supervisor

1. Medidas exactas de cada destino (perfil 800×800, banner 2560×1440 con zona segura 1546×423, marca de agua 150×150,
   miniatura 1280×720 menor de 2 MB, miniatura vertical 1080×1920) y peso dentro del límite.
2. Personajes contra su ficha: rasgos, colores, proporciones, lado y espejo (`DESIGN.md` del canal).
3. Nada tapado o cortado (lección del casete sobre el moño de Tan en la miniatura vertical).
4. Se revisa la imagen renderizada a tamaño real, no solo el código que la dibuja.
5. **Portada de un Short** (`ENTREGA_YOUTUBE.md`, «Portada de los Shorts»): está en los primeros 0,5 a 1 s del
   video y en `miniatura.png` de 1080×1920; texto y caras dentro de la zona útil x 60–960, y 380–1440; máximo 4
   palabras con mayúscula inicial; sin la respuesta; el video cumple lo que promete.

## 5. Video: lo arma el editor, lo firma el supervisor

1. Formato del destino (`formatos.md`): medidas, 30 fps, duración.
2. Hoja de contactos a 2 fotogramas por segundo y `revisar_fotogramas.py`: sin negros, congelados, tirones ni
   fotogramas muertos; no más de 3 destellos por segundo.
3. Las preguntas fijas del capítulo 11 (gancho antes del segundo 1, plano héroe, final que empalma).
4. Los controles 1, 2 y 3 sobre el video ya montado: el texto y la voz se revisan en el archivo final.

## 6. Entrega: la arma el editor, la firma el director creativo

1. `python3 video-studio/herramientas/entrega.py <carpeta>` con 0 errores (incluye el control de texto).
2. `controles.md` del proyecto con los controles 1 a 5 en PASA.
3. Solo entonces se le pide al dueño el visto bueno para subir (`ENTREGA_YOUTUBE.md`).

## 7. Marca del canal: la firma el supervisor

Nombre, colores, tipografía, lema y lados iguales en banner, perfil, marca de agua, miniaturas, hojas y videos
(`canales/<canal>/DESIGN.md`). Un cambio de marca se aplica en todas las piezas a la vez o no se aplica.
