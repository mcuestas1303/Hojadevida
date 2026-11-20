# Hojadevida

El sitio de la hoja de vida vive en `Evaluacion Fundamentos html/`.
`video-studio/` es un estudio de prompts para generación de video; su guía es `video-studio/README.md`.

## Línea editorial

- Decisión del dueño (2026-11-20), para todo lo que se produzca aquí: nada de identidad de género ni
  ideología de género en el contenido, en ningún idioma ni formato. Tiky es él y Lumi es ella.

## Trabajo con videos

- Para ver un video: `python3 video-studio/herramientas/analizar_video.py <video> <salida>` y luego
  lee las hojas de contacto (`hoja_NN.jpg`). No se puede reproducir video directamente.
- Un video nuevo empieza con `python3 video-studio/herramientas/nuevo_proyecto.py <nombre> [referencia]`.
- El análisis de una referencia lo hace el agente `analista-de-video`; el prompt lo escribe
  `director-de-prompts`. La conversación principal coordina y habla con el usuario.
- Todo prompt define su elenco con personajes de `video-studio/personajes/`. Si el usuario no ha
  dicho quién sale, se le pregunta; no se inventan personajes ni se elige por él.
- No se da por bueno un prompt hasta que `validar_prompt.py` termina sin errores.
- Los prompts son archivos `.md`. Una vez validado, cada prompt se archiva con `archivar_prompt.py` en
  `video-studio/personajes/<protagonista>/prompts/` dentro de `intro/`, `capitulos/`, `shorts/` u `otros/`.
  Ahí es donde el usuario los busca; `proyectos/` es solo la mesa de trabajo.

## Contenido infantil (series)

- Las series viven en `video-studio/series/<serie>/`. La primera es `granja`: Tiky y Lumi, 1 a 3 años.
- Un episodio se crea con `nuevo_proyecto.py <nombre> --serie granja` y pasa por el equipo en este orden:
  `pedagoga-montessori` (ficha pedagógica) → `guionista-interactivo` (guion) → `psicologa-infantil`
  (revisión) → `director-de-prompts` (prompt). Si la psicóloga pide cambios, vuelve al guionista.
- El `comercial-inteligencia-digital` trabaja después de la ficha pedagógica: entrega `publicacion.md` y su
  sección de la ficha técnica. Le habla al adulto que elige el video; no cambia el guion, y lo que proponga
  para dentro del video lo deciden la pedagoga y la psicóloga. Toda cifra lleva fuente y fecha.
- Idiomas: español (maestro), inglés y portugués de Brasil. El video es el mismo; cambian la voz
  (`voz_idiomas.md`) y el paquete de publicación (uno por idioma). Se adapta, no se traduce literal.
- Formatos en `video-studio/formatos.md`: capítulo e intro en 16:9 (1920x1080); short en 9:16 (1080x1920), 60 s o menos.
- Todos trabajan contra `video-studio/infantil/guia_1_a_3.md`.
- Cada prompt de serie lleva su `ficha_tecnica.md`: los objetivos de cada disciplina (pedagogía, Montessori,
  psicología infantil, aprendizaje interactivo, producción, comercial e inteligencia digital), escritos por su responsable antes de generar.
  Es la rúbrica del video: una vez generado se puntúa cada criterio y se calcula con `puntuar_ficha.py`.
- En la serie `granja` solo actúan `@tiky` y `@lumi` hasta que el dueño cargue los secundarios.
- El contenido infantil nunca se cruza con «M» ni con personajes para adultos.
- El resto de los personajes del dueño está en la rama `claude/focused-thompson-wojzu6` (`creador-personajes/`).
