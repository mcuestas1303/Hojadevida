# DESIGN · canal de nostalgia (Tin & Tan)

Las referencias reales del canal (regla 6 del cap. 11): sin esto cargado no se renderiza. Los valores de color y las
medidas viven en `video-studio/herramientas/palitos.py`; si se cambian allí, se cambian aquí.

## Paleta (años 70, papel crema)

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

Nada de degradados de fondo (cap. 11, regla 7). Un color de acento por plano.

## Tipografía

- Títulos y cifras: **Inter Display Medium** (en Windows, si no está instalada: Segoe UI Semibold).
- Siempre en **minúsculas**, alineadas a la **izquierda**; nunca mayúsculas centradas.
- **Excepción obligatoria: los nombres propios llevan mayúscula inicial** (regla del dueño, 2026-11-21): «Tin & Tan»,
  «Tin y Tan», «Tin», «Tan». El banner salió como «tin & tan» y el dueño lo rechazó; desde entonces el supervisor de
  continuidad revisa cada nombre letra por letra antes de entregar.
- La tipografía tiene que tener todos los símbolos que se usan (en la prueba, «≈» y «→» salieron como cuadrados):
  antes de renderizar, comprobar los glifos o escribir «about» y una flecha dibujada.
- Subtítulos: 1 a 3 palabras, la palabra clave en mostaza.

## Personajes

- **Tan** a la izquierda del cuadro cuando están juntos (abre con la pregunta); **Tin** a la derecha (responde).
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

- El objeto de la pregunta del video (en la prueba: el casete girando).
- El lápiz amarillo de Tin.

## Composición 16:9

- Zona de texto fija arriba a la izquierda; los personajes nunca debajo del texto (en la prueba hubo textos sobre
  Tiky). Margen de 90 px a los lados.
- Suelo a 86 % de la altura.

## Voz

- **Tin:** Kevin. **Tan:** Zelda. Las dos de Higgsfield (`seed_audio`), con los ajustes por defecto.
- En edición: **10 % más rápido** sin cambiar el tono (`atempo=1.10`) y normalizado a −14 LUFS. Decisión del dueño, 2026-11-21.
- La voz se genera una sola vez con el texto definitivo; la velocidad y el volumen se ajustan gratis. Detalle en `voces.md`.
