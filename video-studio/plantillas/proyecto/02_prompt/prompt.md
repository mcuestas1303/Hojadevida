# Prompt de video — [TÍTULO]

<!--
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
- **Aspecto:** [9:16 | 16:9 | 1:1]
- **Duración total:** [N] s
- **Resolución de borrador:** [la más baja que ofrezca el generador]
- **Resolución final:** [solo para las tomas aprobadas]
- **Precio por segundo:** [costo de 1 s de video en tu plan, o "desconocido"]
- **Intentos estimados por toma:** 2

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
- **Formato de salida:** [resolución, fps]

## 9. Presupuesto

| Concepto | Cantidad | Costo |
|---|---|---|
| Segundos generados (tomas × intentos) | | |
| Keyframes | | |
| Remates en resolución final | | |
| **Total estimado** | | |
