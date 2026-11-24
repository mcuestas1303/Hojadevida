# Definición de generación — 2026-11-24_tin_y_tan_jensen_huang

- **Estado:** PENDIENTE
- **Costo total cotizado:** ≈ 3,3 créditos, **estimados por analogía con el short 2 y sin cotizar**; hay que cotizar con `estimate_audio_cost` antes de pedir el sí. Imagen y video: 0.
- **Autorizado por el dueño:** no

<!--
Estado: PENDIENTE → REVISADA POR EL EQUIPO → AUTORIZADA. Solo con AUTORIZADA se genera.
Este video no tiene keyframes ni clips generados: todas las tomas son dibujo por código. Lo único que se genera es la voz (2 piezas).
-->

## Piezas

### Pieza por código: el video (30,5 s)

- **Tipo:** pieza por código (no se genera con IA)
- **Modelo y ajustes:** `palitos.py` 1.3 y `efectos.py` 1.0, Pillow, numpy y ffmpeg; 1080x1920 a 30 fps, 915 fotogramas, H.264, yuv420p; render ≈ 5 a 6 minutos con 4 procesos
- **Costo cotizado:** 0 créditos
- **Referencias que se suben:** ninguna; las referencias son el código y las hojas de `personajes/tin/referencias/` y `personajes/tan/referencias/`, solo para comparar
- **Personajes:** Tan y Tin, con la proporción de sus fichas (miden lo mismo: mismo `alto` en cada plano)
- **Lugar:** papel_crema (sección 5 de `prompt.md`); no hay lugar definido en `entorno.md` porque el proyecto no es de serie
- **Composición:** zonas de la sección 5 del prompt: texto arriba a la izquierda (x = 10 %, y de 13,2 % a 24 %), gráficos de 27 % a 51 %, personajes con pies a 86 % y `alto` 34 %; portada: texto y 415–690, tarjeta y 731–1089, caras en x 60–960 e y 380–1440
- **Debe verse:** las dos tarjetas genéricas (1999: placa marrón, escuadra, un ventilador, memorias, dedos dorados; actual: carcasa de tinta, tres ventiladores), el pedestal, la PC beige al fondo, el chip con 144 puntos, la pared de 4.000 minitarjetas, los textos de la tabla de la sección 12; Tan con rodete y bufanda mostaza con dos puntas; Tin con gorra marrón, lentes y lápiz (tomas 3 a 5)
- **No debe verse:** logotipos, letras o verde de Nvidia o de GeForce; a Jensen Huang; texto fuera de la tabla; destellos o negativo; sombra tumbada de los muñecos; expresiones `pensando` o `concentrado`; en Tan, la bufanda tapando el brazo (fallo conocido de su ficha: se usa `espejo`); en Tin, la visera tapando las cejas y la mano escondida detrás de la cabeza en `saluda` y `celebra` (fallos conocidos de su ficha, ya corregidos en el código: comprobar que no vuelvan)
- **Prompt:** no aplica (la especificación de dibujo de cada toma está en `02_prompt/prompt.md`, sección 6)

### Voz de Tan (Zelda)

- **Tipo:** audio
- **Modelo y ajustes:** Higgsfield `seed_audio`, voz predefinida de Zelda (`b7aaea29-0c88-5925-90c0-8f66754cda53`), ajustes por defecto; una sola generación; después `atempo=1.10` y −14 LUFS en edición
- **Costo cotizado:** ≈ 0,8 créditos (estimado; falta cotizar)
- **Referencias que se suben:** ninguna
- **Personajes:** Tan
- **Lugar:** no aplica
- **Composición:** no aplica (5 líneas separadas por una línea en blanco; la última es una coletilla que se descarta)
- **Debe verse:** no aplica. **Debe oírse:** las cuatro líneas útiles completas, sin comas (Zelda hace pausas de 0,7 a 0,8 s tras una coma), con «P C» leído letra por letra y la última línea útil terminada en «us»
- **No debe oírse:** frases cortadas al final del archivo (por eso la coletilla), un tono de súplica en «Subscribe and count with us.»
- **Prompt:**

```text
Remember putting one of these in your P C?

How many of those are in a new one?

Four thousand of these in one of those?

Subscribe and count with us.

That's all, folks.
```

### Voz de Tin (Kevin)

- **Tipo:** audio
- **Modelo y ajustes:** Higgsfield `seed_audio`, voz predefinida de Kevin (`f1373f24-3b96-433f-9a68-e595810ef608`), ajustes por defecto; una sola generación; después `atempo=1.10` y −14 LUFS en edición
- **Costo cotizado:** ≈ 2,5 créditos (estimado; falta cotizar)
- **Referencias que se suben:** ninguna
- **Personajes:** Tin
- **Lugar:** no aplica
- **Composición:** no aplica (9 líneas separadas por una línea en blanco; la última es una coletilla que se descarta)
- **Debe verse:** no aplica. **Debe oírse:** «G Force two fifty-six» como «jee force», «R T X fifty-ninety», «C E O», «Nvidia» y «Jensen Huang»; el número «twenty-three million» y «ninety-two billion» sin errores; la última línea útil terminada en «chip»
- **No debe oírse:** que diga «hundred» en «two fifty-six», que diga que la RTX es más rápida, ni nada que no esté en el texto (el generador no inventa frases)
- **Prompt:**

```text
That's the G Force two fifty-six, from nineteen ninety-nine.

Nvidia's board brought Jensen Huang back as C E O.

We're counting transistors, not speed.

That card had up to twenty-three million transistors.

The R T X fifty-ninety has about ninety-two billion.

Divide them.

More than four thousand.

That whole wall, in transistors, is one chip.

That's all, folks.
```

## Revisión del equipo

| Quién | Qué revisó | ¿Conforme? | Nota |
|---|---|---|---|
| director-de-prompts | Que cada dato venga de una ficha o del brief, sin suposiciones | Sí | Datos del brief y fichas de Tin y Tan; cada texto de voz es el de `prompt.md`, sección 7. Dos datos con fuente débil se dicen en la descripción: el comunicado de Nvidia no se abrió y los 23 millones de 1999 solo se vieron en un resumen de buscador |
| supervisor-de-continuidad | Texto, cifras y personajes contra las fichas | Pendiente | Se revisa sobre el video y la voz reales |
| director-creativo | Que la voz y el video cumplan el título y la línea editorial | Pendiente | Firma cuando exista el video |

## Resultado

| Pieza | ID | ¿Cumple la definición? | Qué falló | Costo |
|---|---|---|---|---|
| Voz de Tan | sin generar | — | — | — |
| Voz de Tin | sin generar | — | — | — |
