# Video Studio

Carpeta de trabajo para pasar de una idea, o de un video de referencia, a un prompt de video
listo para generar, con el elenco definido y el costo calculado antes de gastar.

## Quién hace qué

| Paso | Quién | Entrega |
|---|---|---|
| Ver el video de referencia | agente `analista-de-video` | `01_referencia/analisis.md` |
| Escribir el prompt y fijar el elenco | agente `director-de-prompts` | `02_prompt/prompt.md` |
| Comprobar elenco, estructura y costo | `herramientas/validar_prompt.py` | pasa o no pasa |
| Generar keyframes y clips | tú, en tu generador | `03_keyframes/`, `04_clips/` |
| Unir los clips | `herramientas/ensamblar.py` | `06_final/final.mp4` |

El prompt lo escribe un agente dedicado y no la conversación general por tres razones:
trabaja siempre con la misma estructura, lee las fichas de personaje en vez de recordarlas, y no
carga los fotogramas del video (eso lo hace el analista), así que cada prompt sale más barato.
La comprobación final es un script, no una opinión: si un personaje no existe o falta en una
toma, el prompt no pasa.

## Estructura

```
video-studio/
├── personajes/              elenco: una carpeta por personaje
│   ├── REGISTRO.md          lista de quién existe
│   └── <id>/
│       ├── ficha.md         bloque de identidad, vestuario, voz, prohibidos
│       └── referencias/     hoja de personaje, frente, cuerpo completo
├── series/<serie>/          biblia, entorno y temario de cada serie
├── infantil/                guía de 1 a 3 años y plantillas del equipo creativo
├── generador.md             herramienta y precios
├── plantillas/
│   ├── prompt_video.md      estructura fija del prompt
│   ├── hoja_de_personaje.md prompt para crear la hoja de un personaje
│   └── proyecto/            esqueleto que se copia en cada video
├── proyectos/
│   └── AAAA-MM-DD_nombre/
│       ├── 00_brief.md      qué se quiere, quién sale, presupuesto
│       ├── 01_referencia/   video original y su análisis
│       ├── 02_prompt/       prompt.md
│       ├── 03_keyframes/    imagen inicial de cada toma
│       ├── 04_clips/        borradores/ y seleccionados/
│       ├── 05_audio/        voz, música, efectos
│       ├── 06_final/        video terminado
│       └── costos.md        registro de cada generación
└── herramientas/
    ├── nuevo_proyecto.py
    ├── analizar_video.py
    ├── validar_prompt.py
    └── ensamblar.py
```

## Flujo

1. **Crear el proyecto**

   ```bash
   python3 video-studio/herramientas/nuevo_proyecto.py "nombre del video" ruta/al/video_de_referencia.mp4
   ```

   El video de referencia es opcional. Si lo hay, queda analizado en `01_referencia/analisis/`.

2. **Llenar `00_brief.md`**, sobre todo la línea de personajes.
3. **Pedir el análisis** ("analiza la referencia del proyecto X") y luego **el prompt**
   ("escribe el prompt del proyecto X").
4. **Validar**

   ```bash
   python3 video-studio/herramientas/validar_prompt.py video-studio/proyectos/<proyecto>/02_prompt/prompt.md
   ```

5. **Generar** en este orden: keyframes → clips en borrador → solo los aprobados en resolución final.
   Los aprobados van a `04_clips/seleccionados/` como `toma_01.mp4`, `toma_02.mp4`…
6. **Ensamblar**

   ```bash
   python3 video-studio/herramientas/ensamblar.py video-studio/proyectos/<proyecto> --musica ruta/a/musica.mp3
   ```

## Personajes

Un personaje existe para el estudio cuando tiene `personajes/<id>/ficha.md` con su bloque de
identidad y al menos una imagen en `referencias/`. Para dar de alta uno, copia
`personajes/_plantilla/` con el id como nombre de carpeta y agrégalo a `REGISTRO.md`.

En el prompt, la sección **2. Elenco** dice quién sale en el video y cada toma repite quién
aparece en ella. El validador rechaza el prompt si:

- no hay elenco (ni personajes ni un "ninguno" explícito);
- se usa un `@id` que no tiene ficha, bloque de identidad o imagen de referencia;
- una toma no dice quién sale, o usa a alguien que no está en el elenco;
- alguien del elenco no aparece en ninguna toma.

## Cómo se mantiene bajo el costo

- **Primero la imagen.** Un keyframe cuesta una fracción de un clip. El personaje se acierta en
  imagen y después se anima; así no se pagan videos donde la cara salió mal.
- **Borrador antes que final.** Todo se prueba en la resolución y duración más bajas. Solo la
  toma aprobada se regenera o se escala a calidad final.
- **Tomas de 5 s o menos, una acción cada una.** Las tomas largas fallan más y cada fallo cuesta
  el doble.
- **Lo que se puede editar no se genera.** Títulos, texto, logos, zooms sobre foto, cámara
  lenta, repeticiones y transiciones se hacen en el montaje.
- **Mismo bloque de identidad, mismas referencias.** La consistencia viene de repetir
  exactamente lo mismo, no de describir mejor cada vez.
- **Se anota cada intento en `costos.md`.** Si una toma lleva tres fallos, se cambia el prompt
  o se divide la toma; no se sigue intentando.

## Series infantiles

Para contenido de 1 a 3 años hay un equipo creativo que trabaja antes del prompt:

| Orden | Agente | Formación | Entrega |
|---|---|---|---|
| 1 | `pedagoga-montessori` | Pedagogía de primera infancia y método Montessori | `ficha_pedagogica.md`: un objetivo, tramo de edad, material |
| 2 | `guionista-interactivo` | Aprendizaje interactivo | `guion.md`: planos, voz exacta, preguntas y pausas |
| 3 | `psicologa-infantil` | Psicología del desarrollo | `revision.md`: APROBADO o CAMBIOS |
| 4 | `director-de-prompts` | — | `prompt.md` validado |

Los cuatro leen `infantil/guia_1_a_3.md`. Cada serie tiene su carpeta en `series/`:
`serie.md` (público, elenco permitido, estructura del episodio, estilo), `entorno.md`
(lugares fijos con su bloque de escenario) y `temario.md`.

```bash
python3 video-studio/herramientas/nuevo_proyecto.py "Hola, granja" --serie granja
```

En un prompt de serie el validador además exige: solo personajes del elenco permitido,
objetivo de aprendizaje, ninguna toma por debajo de la duración mínima, cámara fija o lenta,
ningún término prohibido en los prompts y la revisión de la psicóloga en APROBADO.

## Requisitos

`ffmpeg` y Python 3. La transcripción del audio es opcional: si el comando `whisper` está
instalado, `analizar_video.py` la agrega; si no, deja el audio en `audio.wav`.
