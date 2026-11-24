# DESIGN · canal Tin & Tan

> **Actualizado el 2026-11-24** por el cambio de parámetros (`PARAMETROS.md`, que manda sobre este archivo). El canal
> dejó de ser «dibujo plano sin degradados sobre papel de los años 70»: la profundidad y los efectos se eligen por lo
> que comunican (`manual/14_efectos_y_emocion.md`) y se hacen con `herramientas/efectos.py`.
>
> **Sigue fijo:** los colores de Tin y de Tan, el contorno de tinta, la tipografía, los dígitos `ss01`, la zona
> segura, los nombres propios con mayúscula y los límites de seguridad. **Cambia por video, con su porqué:** el
> acento, la profundidad, los efectos, el ritmo y la cantidad de texto.

Las referencias reales del canal (regla 6 del cap. 11): sin esto cargado no se renderiza. Los valores de color y las
medidas viven en `video-studio/herramientas/palitos.py`; si se cambian allí, se cambian aquí.

## Paleta (papel y tinta)

| Nombre | Hex | Uso |
|---|---|---|
| papel | `#F3E9D2` | fondo de todos los planos |
| papel_sombra | `#E6D8B8` | suelo, sombras, separadores |
| tinta | `#2B2420` | líneas de los cuerpos, contornos, texto principal |
| naranja | `#E07A2E` | cabeza de Tin; acento de cifras |
| marrón | `#7A4B2A` | gorra de Tin; texto secundario |
| verde azulado | `#2F7F7A` | cabeza de Tan; acento secundario |
| mostaza | `#E8B33B` | bufanda de Tan, lápiz; **color de la palabra clave en subtítulos** |
| tomate | `#C8553D` | alertas, la goma del lápiz, la cifra final |
| rubor | `#E9967A` | mejillas |

Un color de acento por plano. Los degradados, desenfoques, sombras y texturas ya no están prohibidos: se usan cuando
un efecto de `manual/14` los pide y se justifican en el perfil emocional del video (ver «Profundidad y efectos»). Lo
que sigue sin hacerse es el degradado de fondo «por defecto», sin nada que comunicar (cap. 11, regla 7).

**Por qué esta paleta** (manual, cap. 13; regla 2 neutros + 1 acento):
- **Neutros (fijos):** papel `#F3E9D2` (fondo) y tinta `#2B2420` (líneas y texto), con contraste 12,6:1. Se quedan
  porque son lo que hace reconocible el canal entre Shorts y porque el contraste alto se lee a cualquier edad (el
  público ya no tiene edad fija); saturación baja (≈ 17 % medido), para que el acento y los personajes manden.
- **Acento de partida:** mostaza `#E8B33B`, solo en la palabra clave o el dato y en un objeto (el lápiz). Sobre
  papel da 1,6:1, así que **siempre lleva contorno de tinta**. Tomate `#C8553D` (3,6:1) solo como alerta o dato
  final, con contorno, y nunca en el mismo plano que la mostaza.
- **El acento puede cambiar por video** si el tema lo pide (`PARAMETROS.md`, «Paleta»). Condiciones: uno solo por
  video; no puede ser ni parecerse al naranja de Tin ni al verde azulado de Tan (ΔE76 ≥ 25 con los dos); no es el
  color de una marca de terceros; con contorno de tinta si da menos de 4,5:1 sobre papel; y su porqué (qué comunica
  y cómo acerca al objetivo) va en la sección 3b de la dirección, en `ficha.json` y en el perfil emocional. Se mide
  con `revisar_color.py` pasándole la paleta con el acento de ese video.
- **Identidad, no acento (fijos):** naranja (Tin), verde azulado (Tan), marrón y rubor son los personajes. No cambian
  nunca, tampoco con efectos de color encima de ellos.
- **Objetivo:** retención (el acento lleva el ojo al dato en el primer segundo) y reconocimiento (los mismos neutros
  y los mismos personajes en todo el canal). Métrica: espectadores que regresan frente al rendimiento del video.

## Profundidad y efectos (desde el 2026-11-24)

- Se eligen con el procedimiento de `manual/14_efectos_y_emocion.md` (qué comunica, qué emoción provoca, con qué
  respaldo y con qué métrica se verá) y se justifican en `02_prompt/perfil_emocional.md`. Ninguno se elige por gusto
  ni se le pregunta al dueño cuál prefiere (regla del dueño, 2026-11-23).
- Se hacen con `herramientas/efectos.py`: capas con paralaje y cámara, foco animable, sombras de contacto y
  proyectadas, transiciones, garabatos, texto de vidrio, contador. Gratis.
- **Límites que no se mueven** (`PARAMETROS.md`, sección 2; `manual/14`, sección 6): máximo 3 destellos por segundo,
  nunca blanco puro a pantalla completa; todo video pasa `efectos.comprobar_destellos`.
- Un efecto no tapa la cara de Tin ni de Tan ni cambia sus colores.
- La marca del canal (banner) usa solo sombras de contacto: tiene que leerse a 320 px de ancho.

### Control de color en videos con profundidad · **pendiente de firma del director de fotografía**

El problema (COORDINACION, 2026-11-23): con desenfoques y sombras `revisar_color.py` da ≈ 82 % dentro de la paleta
(umbral: 85 %) sin que entre ningún tono nuevo, porque los bordes suaves crean mezclas entre papel y tinta.
**Criterio propuesto (no vigente hasta que lo firme el director de fotografía; el supervisor de continuidad lo
revisa):**

1. **Fotograma nítido de control: ≥ 85 %.** De cada plano con profundidad se mide además un fotograma renderizado
   sin desenfoque, sin sombras y sin grano (las mismas capas, efectos apagados). Ese pasa el umbral de siempre.
2. **Fotograma final: ≥ 75 %**, y lo que quede fuera tiene que ser mezcla de colores de la paleta: ningún color
   dominante (k-medias de `revisar_color.py`) con más del 3 % del cuadro a ΔE76 ≥ 12 de la recta entre dos colores
   de la paleta declarada.
3. **Saltos de luminosidad entre segundos:** los mismos de `manual/13`; no se relajan.
4. Si falla 1, hay un color nuevo de verdad: se corrige. Si pasa 1 y falla 2, el efecto es demasiado fuerte: se baja.

Hasta la firma, un video con profundidad que dé menos de 85 % se entrega con las dos medidas a la vista y la nota
«umbral pendiente de firma», y lo decide el director de fotografía caso por caso.

## Tipografía

- Títulos y cifras: **Inter Display Medium** (en Windows, si no está instalada: Segoe UI Semibold).
- Siempre en **minúsculas**, alineadas a la **izquierda**; nunca mayúsculas centradas.
- **Excepción obligatoria: los nombres propios llevan mayúscula inicial** (regla del dueño, 2026-11-21): «Tin & Tan»,
  «Tin y Tan», «Tin», «Tan». El banner salió como «tin & tan» y el dueño lo rechazó; desde entonces el supervisor de
  continuidad revisa cada nombre letra por letra antes de entregar.
- **Portada de los Shorts: mayúscula inicial en cada palabra** («How Many / Pencil Turns?»), máximo 4 palabras en
  2 líneas, con la palabra clave en el acento del video (de partida, mostaza) (regla del dueño, 2026-11-21; `ENTREGA_YOUTUBE.md`). Es la única pieza
  del canal con esa capitalización; el resto sigue en minúsculas, salvo los nombres.
- **Cifras con decimales o fracciones: aproximadas y con «≈»** («≈ 422 ft», «≈ 1.9 in/s»), regla del dueño del
  2026-11-21 (`manual/12_controles_de_calidad.md`). Inter Display Medium sí tiene «≈» (comprobado); el cuadro de
  la prueba de 30 s salió de otra tipografía.
- La tipografía tiene que tener todos los símbolos que se usan (en la prueba, «≈» y «→» salieron como cuadrados):
  antes de renderizar, comprobar los glifos o escribir «about» y una flecha dibujada.
- Subtítulos: de partida 1 a 3 palabras, con la palabra clave en el acento; la cantidad de texto es un parámetro
  (de casi ninguno a subtítulo completo, `PARAMETROS.md`).
- **Lemas y textos de marca en minúsculas** («she asks. he brings the facts.»), como todo el canal; si un lema lleva
  un nombre propio, ese nombre va con mayúscula.
- **Cifras: dígitos abiertos de Inter (rasgo OpenType `ss01`) y contorno de 0,045 em** (norma del canal desde el
  short 2, «How Many Days Did We Wait for GTA 6?», 2026-11-23). Por qué: con los dígitos por defecto de Inter Display
  Medium y el contorno de 0,06 em, las aberturas del 6, el 9, el 3 y el 5 son más estrechas que el trazo, se llenaban
  de tinta y el número salía con una línea por dentro (lo marcó el supervisor de continuidad). `ss01` es de la misma
  fuente (3, 4, 6 y 9 alternativos) y se aplica a **todas** las cifras de la pieza, con o sin contorno, para que no se
  mezclen dos formas del mismo número. En Pillow: `features=["ss01"]` (necesita libraqm). El short 1 («pencil turns»)
  quedó con los dígitos por defecto y el contorno de 0,05 em: no se rehace; si se vuelve a renderizar, se pasa a esta norma.

## Personajes

- **Tan** a la izquierda del cuadro cuando están juntos (abre con la pregunta); **Tin** a la derecha (responde con
  datos).
- **Cada uno gesticula del lado contrario al otro:** Tan con `espejo=True`, Tin sin espejo.
- Plano héroe de los dos: `referencias/principal_tin_y_tan.png` de cada ficha.
- Expresiones y poses: solo las de `palitos.py` (`EXPRESIONES`, `POSES`).

## Movimiento

- Todo depende del **número de fotograma**, no del reloj (regla 10).
- Entradas y salidas con **muelle** (masa, rigidez, amortiguación por elemento); nunca interpolación lineal.
- Las puntas de la bufanda de Tan y el lápiz de Tin tienen movimiento secundario.
- Contadores que **solo suben** (en la prueba uno volvía atrás).
- Máximo 3 destellos por segundo (`postpro.py destellos`).

## Motivos que vuelven

- Lo que el video explica, dibujado de forma propia (nunca el logotipo, la tipografía ni los colores de una marca;
  nunca la cara de una persona real).
- El lápiz amarillo de Tin.
- En la marca del canal: la pregunta que se vuelve respuesta comprobada («?» → visto bueno). Ningún objeto de un
  tema concreto es símbolo del canal.

## Firma del canal: el lápiz bumerán (borrador del 2026-11-24, pendiente de firmas y de prueba técnica)

Pedido del dueño: en todos los videos, al final Tan lanza el lápiz y al principio vuelve a sus manos (bucle). Dura 34 f
(1,13 s); el lápiz es identidad, no acento; cámara fija, sin destellos. Valores, fotogramas, sonido, seguridad y
medición: `FIRMA_LAPIZ_BUMERAN.md`. Si algo de ese archivo contradice a este, manda ese para la firma.

## Composición 16:9

- Zona de texto fija arriba a la izquierda; los personajes nunca debajo del texto (en la prueba hubo textos sobre
  Tiky). Margen de 90 px a los lados.
- Suelo a 86 % de la altura.

## Voz

- **Tin:** Kevin. **Tan:** Zelda. Las dos de Higgsfield (`seed_audio`), con los ajustes por defecto.
- En edición: **10 % más rápido** sin cambiar el tono (`atempo=1.10`) y normalizado a −14 LUFS. Decisión del dueño, 2026-11-21.
- La voz se genera una sola vez con el texto definitivo; la velocidad y el volumen se ajustan gratis. Detalle en `voces.md`.
