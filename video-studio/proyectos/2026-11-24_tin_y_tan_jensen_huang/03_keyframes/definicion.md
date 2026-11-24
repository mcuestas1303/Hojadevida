# Definición de generación — 2026-11-24_tin_y_tan_jensen_huang

- **Estado:** PENDIENTE
- **Costo total cotizado:** voz por cotizar con `estimate_audio_cost` (referencia del plan anterior: 3,7 créditos con un texto parecido); imagen y video: 0
- **Autorizado por el dueño:** no

<!--
Estado: PENDIENTE → REVISADA POR EL EQUIPO → AUTORIZADA. Solo con AUTORIZADA se genera.
Este video no tiene keyframes ni clips generados: todas las tomas son dibujo por código. Lo único que se genera es la voz (2 piezas).
Versión 2 (2026-11-24): sustituye a la definición de la tarjeta de 1999.
-->

## Piezas

### Pieza por código: el video (30,5 s)

- **Tipo:** pieza por código (no se genera con IA)
- **Modelo y ajustes:** `palitos.py` 1.3 y `efectos.py`, Pillow, numpy y ffmpeg; 1080x1920 a 30 fps, 915 fotogramas, H.264, yuv420p; render ≈ 5 a 6 minutos con 4 procesos
- **Costo cotizado:** 0 créditos
- **Referencias que se suben:** ninguna; las referencias son el código y las hojas de `personajes/tin/referencias/` y `personajes/tan/referencias/`, solo para comparar
- **Personajes:** Tan y Tin, con la proporción de sus fichas (mismo `alto`, 29 % del alto del cuadro, en cada plano; 487 px en la portada)
- **Lugar:** papel_crema (sección 5 de `prompt.md`); no hay lugar definido en `entorno.md` porque el proyecto no es de serie
- **Composición:** texto en inglés arriba (x = 10 %, y de 13,2 % a 24 %), gráficos de 27 % a 46,5 % (y 518–893), **banda de subtítulos en español de y 905 a 1085**, personajes con pies a 86 % y cabeza desde y 1094; portada: texto en y 492–682, silla de director y 754–1066, caras en x 60–960 e y 380–1440
- **Debe verse:** la silla de director vacía (marrón y papel sombra, sin letras), el calendario de noviembre de 2026 (el 12 jueves, el 17 martes y el 23 lunes), la mesa de junta con cinco sillas genéricas, las barras a escala con su marca mínima de 4 px, el lápiz de Tin girando con estela (llega en la toma 1 y sale en la toma 14), los rótulos de la tabla de la sección 12 y las 12 tarjetas en español; Tan con rodete y bufanda mostaza con dos puntas; Tin con gorra marrón, lentes y lápiz
- **No debe verse:** logotipos, letras o verde de Nvidia; a Jensen Huang, a Sam Altman o a Steve Jobs ni a ninguna persona real; texto fuera de las tablas; destellos o negativo; sombra tumbada de los muñecos; la silla tachada o señalada; expresiones `pensando` o `concentrado`; subtítulo sobre la portada (0,0–1,0 s y 29,6–30,5 s); en Tan, la bufanda tapando el brazo (se usa `espejo`); en Tin, la visera tapando las cejas y la mano escondida detrás de la cabeza en `saluda` y `celebra` (fallos conocidos de su ficha, ya corregidos en el código: comprobar que no vuelvan); un segundo acento en el mismo plano
- **Prompt:** no aplica (la especificación de dibujo de cada toma está en `02_prompt/prompt.md`, sección 6)

### Voz de Tan (Zelda)

- **Tipo:** audio
- **Modelo y ajustes:** Higgsfield `seed_audio`, voz predefinida de Zelda (`b7aaea29-0c88-5925-90c0-8f66754cda53`), ajustes por defecto; una sola generación; después `atempo=1.10` y −14 LUFS en edición
- **Costo cotizado:** por cotizar con `estimate_audio_cost` (4 líneas y coletilla)
- **Referencias que se suben:** ninguna
- **Personajes:** Tan
- **Lugar:** no aplica
- **Composición:** no aplica (4 líneas útiles separadas por una línea en blanco; la última es una coletilla que se descarta)
- **Debe verse:** no aplica. **Debe oírse:** las cuatro líneas útiles completas, sin comas en Tan (Zelda hace pausas de 0,7 a 0,8 s tras una coma), con «Jensen Huang» bien dicho, y la última línea útil terminada en «count»
- **No debe oírse:** frases cortadas al final del archivo (por eso la coletilla), un tono de súplica en «Subscribe for the next count.», burla en la pregunta de apertura
- **Prompt:**

```text
Was Jensen Huang's comeback in eleven days fast?

Fast compared to who?

That is twelve years?

Who else came back? Subscribe for the next count.

That's all, folks.
```

### Voz de Tin (Kevin)

- **Tipo:** audio
- **Modelo y ajustes:** Higgsfield `seed_audio`, voz predefinida de Kevin (`f1373f24-3b96-433f-9a68-e595810ef608`), ajustes por defecto; una sola generación; después `atempo=1.10` y −14 LUFS en edición
- **Costo cotizado:** por cotizar con `estimate_audio_cost` (7 líneas y coletilla)
- **Referencias que se suben:** ninguna
- **Personajes:** Tin
- **Lugar:** no aplica
- **Composición:** no aplica (7 líneas útiles separadas por una línea en blanco; la última es una coletilla que se descarta)
- **Debe verse:** no aplica. **Debe oírse:** «Nvidia», «C E O» (letra por letra), «OpenAI», «Sam Altman», «Steve Jobs»; el número «four thousand, three hundred eighty-two» sin errores y con una pausa de ≈ 0,45 s tras «Apple:»; las fechas como ordinales («twelfth», «seventeenth»); la última línea útil terminada en «Altman»
- **No debe oírse:** que diga «hundred» de más, que añada adjetivos o juicios, ni nada que no esté en el texto (el generador no inventa frases)
- **Prompt:**

```text
He resigned from Nvidia on November twelfth after a scandal.

On the seventeenth the board said it would not bring him back.

Six days later it reinstated him as C E O.

Before that: more than thirty-three years in charge.

Sam Altman at OpenAI: five days.

Steve Jobs at Apple: four thousand, three hundred eighty-two days.

Faster than Jobs. Slower than Altman.

That's all, folks.
```

## Revisión del equipo

| Quién | Qué revisó | ¿Conforme? | Nota |
|---|---|---|---|
| director-de-prompts | Que cada dato venga de una ficha o del brief, sin suposiciones | Sí | Fechas de Altman y Jobs verificadas en Wikipedia el 2026-11-24 y calculadas con `datetime`; cada texto de voz es el de `prompt.md`, sección 7. Dos datos con fuente débil se dicen en la descripción: el comunicado de Nvidia no se abrió y el nombramiento de Jobs tiene un día de diferencia entre Wikipedia (16) y el título del NYT (17) |
| supervisor-de-continuidad | Texto, cifras y personajes contra las fichas | Pendiente | Se revisa sobre el video y la voz reales |
| director-creativo | Que la voz y el video cumplan el título y la línea editorial (una sola mención neutra del motivo; cierre con pregunta nueva) | Pendiente | Firma cuando exista el video |

## Resultado

| Pieza | ID | ¿Cumple la definición? | Qué falló | Costo |
|---|---|---|---|---|
| Voz de Tan | sin generar | — | — | — |
| Voz de Tin | sin generar | — | — | — |
