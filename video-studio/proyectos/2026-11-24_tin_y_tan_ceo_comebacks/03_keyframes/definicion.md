# Definición de generación — 2026-11-24_tin_y_tan_ceo_comebacks

- **Estado:** PENDIENTE
- **Costo total cotizado:** voz por cotizar con `estimate_audio_cost` (referencia por analogía con el short 3: 3,7 créditos; con la prueba de voces de 2026-11-21, 5 líneas de Tin = 2,2 y 3 líneas de Tan = 0,8: ≈ 3,5 créditos; **no es una cotización**); imagen y video: 0
- **Autorizado por el dueño:** no

<!--
Estado: PENDIENTE → REVISADA POR EL EQUIPO → AUTORIZADA. Solo con AUTORIZADA se genera.
Este video no tiene keyframes ni clips generados: todas las tomas son dibujo por código. Lo único que se genera es la voz (2 piezas, una sola generación cada una).
Versión 1 (2026-11-24).
-->

## Piezas

### Pieza por código: el video (31,0 s)

- **Tipo:** pieza por código (no se genera con IA)
- **Modelo y ajustes:** `palitos.py` 1.4 y `efectos.py` 1.1, Pillow, numpy y ffmpeg; 1080x1920 a 30 fps, 930 fotogramas, H.264, yuv420p; render de unos minutos con varios procesos (el del short 3 tardó ≈ 160 s)
- **Costo cotizado:** 0 créditos
- **Referencias que se suben:** ninguna; las referencias son el código y las hojas de `personajes/tin/referencias/` y `personajes/tan/referencias/`, solo para comparar
- **Personajes:** Tan y Tin, con la proporción de sus fichas (mismo `alto` en un plano de los dos: 505 px, 26,3 % del alto del cuadro; 487 px en la portada)
- **Lugar:** papel_crema (sección 5 de `prompt.md`); no hay lugar definido en `entorno.md` porque el proyecto no es de serie
- **Composición:** rótulo en inglés arriba (x = 10 %, y de 13,2 % a 24 %, cifras al 7 %); **ranking de seis filas de 68 px en y 480–888** (nombres a 56 px desde x = 100; barras de 40 px de x = 320 a 980, 660 px = 4.382 días); **banda de subtítulos en español de y 905 a 1085**; personajes con pies a 86 % (y = 1651) y cabeza desde y ≈ 1146; portada: texto de tres renglones a 92 px en y 400–700, silla de director y 720–1100, caras en x 60–960 e y 380–1440
- **Debe verse:** la silla de director vacía (marrón y papel sombra, sin letras); el ranking con las filas Altman, Huang, Iger, Dell, Dorsey y Jobs, cada una con su nombre y su barra a escala (Iger 150 px, Dell 160 px, Dorsey 369 px, Jobs 660 px) y las marcas mínimas de 8 px con borde de 2 px en Huang y Altman; el lápiz girando con estela (llega en la toma 1 y sale en la toma 12); los rótulos de la tabla de la sección 12 y las 12 tarjetas en español; Tan con rodete y bufanda mostaza con dos puntas, pestañas cortas; Tin con gorra marrón con visera, botón y dos costuras, lentes con brillo y cejas visibles bajo la visera
- **No debe verse:** logotipos, letras o colores de marca de Nvidia, Disney, Dell, Twitter, Apple u OpenAI; a ninguna persona real dibujada o imitada; texto fuera de las tablas; destellos o negativo; sombra tumbada de los muñecos; la silla tachada o señalada; expresiones `pensando`, `concentrado`, `celebra`, `eureka` o la cara `neutra`; sonrisa en un dato de una salida; subtítulo sobre la portada (0,0–1,0 s y 29,97–31,0 s); una barra o marca sin nombre; marca de menos de 8 px; las tres fallas de las fichas, ya corregidas en el código y que no deben volver: en Tan, la bufanda tapando el brazo (se usa `espejo`) y las pestañas largas que se leen como enojo; en Tin, la visera tapando las cejas y la mano escondida detrás de la cabeza en `saluda`; un segundo acento en el mismo plano
- **Prompt:** no aplica (la especificación de dibujo de cada toma está en `02_prompt/prompt.md`, sección 6)

### Voz de Tan (Zelda)

- **Tipo:** audio
- **Modelo y ajustes:** Higgsfield `seed_audio`, voz predefinida de Zelda (`b7aaea29-0c88-5925-90c0-8f66754cda53`), ajustes por defecto; una sola generación; después `atempo=1.10` y −14 LUFS en edición
- **Costo cotizado:** por cotizar con `estimate_audio_cost` (4 líneas y coletilla; la prueba de 2026-11-21 dio 0,8 créditos por 3 líneas)
- **Referencias que se suben:** ninguna
- **Personajes:** Tan
- **Lugar:** no aplica
- **Composición:** no aplica (4 líneas útiles separadas por una línea en blanco; la última es una coletilla que se descarta)
- **Debe verse:** no aplica. **Debe oírse:** las cuatro líneas útiles completas, sin comas en Tan (Zelda hace pausas de 0,7 a 0,8 s tras una coma), con «Jensen Huang» bien dicho, «C E O» letra por letra, «Almost seven years?» y «Almost twelve years?» con la palabra «almost» y la entonación de pregunta, y la última línea útil terminada en «count»
- **No debe oírse:** frases cortadas al final del archivo (por eso la coletilla), un tono de súplica en «Subscribe for the next count.», burla en la pregunta de apertura, que «longer» suene a reproche
- **Prompt:**

```text
Jensen Huang came back as C E O in eleven days. Who took longer?

Almost seven years?

Almost twelve years?

How long did they stay after coming back? Subscribe for the next count.

That's all, folks.
```

### Voz de Tin (Kevin)

- **Tipo:** audio
- **Modelo y ajustes:** Higgsfield `seed_audio`, voz predefinida de Kevin (`f1373f24-3b96-433f-9a68-e595810ef608`), ajustes por defecto; una sola generación; después `atempo=1.10` y −14 LUFS en edición
- **Costo cotizado:** por cotizar con `estimate_audio_cost` (5 líneas y coletilla; la prueba de 2026-11-21 dio 2,2 créditos por 5 líneas)
- **Referencias que se suben:** ninguna
- **Personajes:** Tin
- **Lugar:** no aplica
- **Composición:** no aplica (5 líneas útiles separadas por una línea en blanco; la última es una coletilla que se descarta)
- **Debe verse:** no aplica. **Debe oírse:** «Iger» (EYE-ger), «Disney», «Dell», «Dorsey», «Twitter», «Sam Altman», «Steve Jobs»; los números «nine hundred ninety-nine», «one thousand, sixty-three», «two thousand, four hundred forty-nine» y «four thousand, three hundred eighty-two» sin errores, con una pausa de ≈ 0,45 s tras «Apple:»; la última línea útil terminada en «longer»
- **No debe oírse:** que diga «hundred» de más, que añada adjetivos, juicios o motivos de una salida, ni nada que no esté en el texto (el generador no inventa frases); que lea «Iger» con otra pronunciación (si pasa, se pide autorización para regenerar esa voz: no hay segundo intento por cuenta propia)
- **Prompt:**

```text
Bob Iger at Disney: nine hundred ninety-nine days.

Michael Dell at Dell: one thousand, sixty-three days.

Jack Dorsey at Twitter: two thousand, four hundred forty-nine days.

Steve Jobs at Apple: four thousand, three hundred eighty-two days.

Only Sam Altman was faster than Huang: five days. The other four took longer.

That's all, folks.
```

## Dudas que quedan abiertas (no se suponen)

- **Costo exacto de la voz:** falta correr `estimate_audio_cost` con los dos textos (la conversación principal tiene la herramienta; este agente no genera ni cotiza).
- **Pronunciación de «Iger» y «Dorsey»:** no se sabe cómo las leerá `seed_audio` hasta oír la voz; se decide al oído y, si falla, se pide autorización para regenerar esa pieza.
- **Tiempos reales de la voz:** los cortes, las tarjetas y los rótulos de `prompt.md` se reajustan con ellos; el pico (hoy 61,7 %) debe quedar por debajo del 75 %.

## Revisión del equipo

| Quién | Qué revisó | ¿Conforme? | Nota |
|---|---|---|---|
| director-de-prompts | Que cada dato venga de una ficha o del entorno, sin suposiciones | Sí | Las medidas salen de `prompt.md`, de la sección «Definición para generar» de las fichas de Tan y Tin y de las firmas del short 3; las dudas están arriba |
| supervisor-de-continuidad | Contra `direccion.md` y las firmas del short 3 | Pendiente | Revisa tras el render |

## Resultado

| Pieza | ID | ¿Cumple la definición? | Qué falló | Costo |
|---|---|---|---|---|
| Video por código | — | pendiente | — | 0 |
| Voz de Tan (Zelda) | — | pendiente | — | por cotizar |
| Voz de Tin (Kevin) | — | pendiente | — | por cotizar |
