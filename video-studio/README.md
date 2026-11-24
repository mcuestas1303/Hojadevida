# Video Studio

Carpeta de trabajo para pasar de una idea, o de un video de referencia, a un prompt de video
listo para generar, con el elenco definido y el costo calculado antes de gastar.

**Para montar un personaje nuevo, sigue `MANUAL.md`.** Este archivo es la referencia de la
carpeta; el manual es el procedimiento paso a paso y `casos/` guarda el ejemplo real.


## Canales

`canales/<canal>/` guarda las decisiones, pruebas y pendientes de cada canal. Hoy: `canales/nostalgia-tin-y-tan/`
(canal «Tin & Tan»: explican con hechos comprobados lo que la gente ya está mirando; dibujados con
`herramientas/palitos.py`. Su definición es `canales/nostalgia-tin-y-tan/PARAMETROS.md`; el nombre de la carpeta se
conserva solo para no romper rutas).

## Equipo de producción

El estudio tiene un equipo completo de producción de audio y video, entrenado con el manual de `manual/`
(objetivo y emoción, cámara, luz, animación, herramientas y costos, modos, edición, audio, prompts maestros,
algoritmo y monetización). Se pone en marcha con **`/producir <personaje> <idea o clip>`**.

## Quién hace qué

| Paso | Quién | Entrega |
|---|---|---|
| Ver el clip propio o de referencia | agente `analista-de-video` | `01_referencia/analisis.md` |
| Objetivo comercial, público, emoción, gancho, medición | agente `director-creativo` (creativo y comercial) | `02_prompt/direccion.md` §1, §2, §8 |
| Cámara, lente, luz y color por toma | agente `director-de-fotografia` | `direccion.md` §3 |
| Actuación y movimiento del personaje | agente `director-de-animacion` | `direccion.md` §4 |
| Voz, música, efectos, mezcla | agente `disenador-de-sonido` | `direccion.md` §5, `05_audio/` |
| Plan de montaje y salidas | agente `editor-de-video` | `direccion.md` §6, `06_final/` |
| Ruta más barata y presupuesto cotizado | agente `jefe-de-produccion` | `direccion.md` §7, `costos.md` |
| Escribir el prompt y fijar el elenco | agente `director-de-prompts` | `02_prompt/prompt.md` |
| Comprobar elenco, estructura y costo | `herramientas/validar_prompt.py` | pasa o no pasa |
| Generar keyframes y clips | la sesión principal, con aprobación del dueño | `03_keyframes/`, `04_clips/` |
| Revisar fidelidad y calidad | agente `supervisor-de-continuidad` | `revision_produccion.md` |
| Editar, unir, subtitular, mezclar (gratis) | `herramientas/postpro.py`, `ensamblar.py` | `06_final/` |
| Leer estadísticas y decidir qué repetir | `director-creativo` con `herramientas/estadisticas.py` | `estadisticas/informe_*.md` |

El prompt lo escribe un agente dedicado y no la conversación general por tres razones:
trabaja siempre con la misma estructura, lee las fichas de personaje en vez de recordarlas, y no
carga los fotogramas del video (eso lo hace el analista), así que cada prompt sale más barato.
La comprobación final es un script, no una opinión: si un personaje no existe o falta en una
toma, el prompt no pasa.

## Estructura

```
video-studio/
├── MANUAL.md                procedimiento para montar un personaje de cero a publicación
├── casos/                   registro de cada montaje real
├── personajes/              elenco: una carpeta por personaje
│   ├── REGISTRO.md          lista de quién existe
│   └── <id>/
│       ├── ficha.md         bloque de identidad, vestuario, voz, prohibidos
│       ├── referencias/     imágenes aprobadas del personaje
│       └── prompts/         prompts de video terminados, por tipo
│           ├── INDICE.md    lista de todo lo que tiene el personaje
│           ├── intro/
│           ├── capitulos/
│           ├── shorts/
│           └── otros/
├── series/<serie>/          biblia, entorno y temario de cada serie
├── infantil/                guía de 1 a 3 años y plantillas del equipo creativo
├── generador.md             herramienta y precios
├── formatos.md              formatos de salida para YouTube y redes
├── estudios/                informes de lo aprendido de material externo
├── referencias_externas.md  material de terceros para estudiar, no para copiar
├── generacion.md            reglas de créditos, definición cerrada y cambios
├── cambios/                 solicitudes de cambio revisadas por el equipo
├── datos/                   exportaciones del canal para el comercial
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
    ├── estado.py
    ├── nuevo_personaje.py
    ├── nueva_serie.py
    ├── nuevo_proyecto.py
    ├── analizar_video.py
    ├── validar_prompt.py
    ├── archivar_prompt.py
    ├── puntuar_ficha.py
    ├── revisar_fotogramas.py
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

5. **Archivar** el prompt en la carpeta del personaje

   ```bash
   python3 video-studio/herramientas/archivar_prompt.py video-studio/proyectos/<proyecto>
   ```

6. **Generar** en este orden: keyframes → clips en borrador → solo los aprobados en resolución final.
   Los aprobados van a `04_clips/seleccionados/` como `toma_01.mp4`, `toma_02.mp4`…
7. **Ensamblar**

   ```bash
   python3 video-studio/herramientas/ensamblar.py video-studio/proyectos/<proyecto> --formato largo --musica ruta/a/musica.mp3
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

## Revisión de lo generado

Antes de puntuar la rúbrica, cada clip pasa por una revisión automática que no gasta créditos:

```bash
python3 video-studio/herramientas/revisar_fotogramas.py <clip> video-studio/proyectos/<proyecto>/07_revision/<toma> --serie granja
```

Marca imagen congelada, fotogramas vacíos, más de 3 destellos por segundo y planos más cortos
que el mínimo de la serie, y deja una hoja con los fotogramas marcados. Señala dónde mirar; no
autoriza a regenerar.

## Contenido para redes y adultos

Para piezas que le hablan al adulto (reels, anuncios, personajes no infantiles) hay una
plantilla aparte, `plantillas/prompt_video_redes.md`, con gancho, mapa de ritmo, texto en
pantalla y sonido. No se usa en series infantiles.

```bash
python3 video-studio/herramientas/nuevo_proyecto.py "nombre" --redes
```

## Créditos, definición y cambios

Tres reglas, detalladas en `generacion.md`: cada pieza se genera una sola vez; no se genera
nada sin definición cerrada (personaje, lugar y pieza) y sin autorización con el costo a la
vista; y todo cambio pasa primero por el equipo como una solicitud en `cambios/`, que dice
qué toca de lo ya definido y cuánto costaría.

## Dónde quedan los prompts

Todos los prompts son `.md`. `proyectos/` es la mesa de trabajo (brief, guion, revisión,
keyframes, clips); el prompt terminado se guarda en la carpeta del personaje, según el campo
`Tipo` de su ficha técnica:

| Tipo | Carpeta | Nombre del archivo |
|---|---|---|
| intro | `prompts/intro/` | `<serie>_intro_<título>.md` |
| capítulo | `prompts/capitulos/` | `<serie>_cap01_<título>.md` |
| short | `prompts/shorts/` | `<serie>_short01_<título>.md` |
| otro | `prompts/otros/` | `<serie>_otro_<título>.md` |

Un prompt se guarda una sola vez, en la carpeta del protagonista (el primer personaje del
elenco). Los demás personajes del video lo encuentran en su `prompts/INDICE.md`, que enlaza
al mismo archivo. Solo se archiva lo que pasa el validador.

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
| — | `comercial-inteligencia-digital` | Datos de YouTube y redes, inteligencia digital | `publicacion.md`: búsqueda, título, miniatura, shorts derivados, metas |

Los cuatro leen `infantil/guia_1_a_3.md`. Cada serie tiene su carpeta en `series/`:
`serie.md` (público, elenco permitido, estructura del episodio, estilo), `entorno.md`
(lugares fijos con su bloque de escenario) y `temario.md`.

```bash
python3 video-studio/herramientas/nuevo_proyecto.py "Hola, granja" --serie granja
```

En un prompt de serie el validador además exige: solo personajes del elenco permitido,
objetivo de aprendizaje, ninguna toma por debajo de la duración mínima, cámara fija o lenta,
ningún término prohibido en los prompts y la revisión de la psicóloga en APROBADO.

## Idiomas

El contenido sale en español, inglés y portugués de Brasil. Como los videos no llevan texto
en pantalla ni labios sincronizados, se genera un solo video y cambia la pista de voz: el
guionista escribe `voz_idiomas.md` (adaptada, no traducida, y ajustada a los mismos tiempos),
la psicóloga revisa los tres idiomas y el comercial prepara un paquete de publicación por mercado.

## Formatos

Capítulos e intro: 16:9, máster de 1920×1080. Shorts: 9:16, máster de 1080×1920, 60 s o
menos para reutilizarlos en Reels, TikTok y Facebook. Detalle y fuentes en `formatos.md`.

```bash
python3 video-studio/herramientas/ensamblar.py video-studio/proyectos/<proyecto> --formato largo
```

## Ficha técnica y rúbrica

Cada prompt de serie va acompañado de `ficha_tecnica.md`. Antes de generar, cada profesional
escribe lo que su disciplina se propone lograr en ese video:

| Sección | Responsable |
|---|---|
| Pedagogía | `pedagoga-montessori` |
| Método Montessori | `pedagoga-montessori` |
| Psicología infantil | `psicologa-infantil` |
| Aprendizaje interactivo | `guionista-interactivo` |
| Producción | `director-de-prompts` |
| Comercial e inteligencia digital | `comercial-inteligencia-digital` |

Cada criterio dice qué debe lograrse, cómo se comprueba en el video, en qué plano mirar, su
peso (1 a 3) y si es crítico. Con el video ya generado se puntúa cada uno (0 no se cumple,
1 a medias, 2 se cumple) con su evidencia, y se calcula:

```bash
python3 video-studio/herramientas/puntuar_ficha.py video-studio/proyectos/<proyecto>/02_prompt/ficha_tecnica.md
```

El resultado da el cumplimiento por disciplina y total. «CUMPLE» pide 80 % o más y todos los
críticos en 2; un crítico por debajo de 2 es «NO PUBLICAR» aunque el total sea alto. La ficha
se archiva junto al prompt en la carpeta del personaje, como `<nombre>_ficha.md`.

## Requisitos

`ffmpeg` y Python 3. La transcripción del audio es opcional: si el comando `whisper` está
instalado, `analizar_video.py` la agrega; si no, deja el audio en `audio.wav`.
