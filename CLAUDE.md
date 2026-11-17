# Hojadevida

El sitio de la hoja de vida vive en `Evaluacion Fundamentos html/`.
`video-studio/` es un estudio de prompts para generación de video; su guía es `video-studio/README.md`.

## Trabajo con videos

- Para ver un video: `python3 video-studio/herramientas/analizar_video.py <video> <salida>` y luego
  lee las hojas de contacto (`hoja_NN.jpg`). No se puede reproducir video directamente.
- Un video nuevo empieza con `python3 video-studio/herramientas/nuevo_proyecto.py <nombre> [referencia]`.
- El análisis de una referencia lo hace el agente `analista-de-video`; el prompt lo escribe
  `director-de-prompts`. La conversación principal coordina y habla con el usuario.
- Todo prompt define su elenco con personajes de `video-studio/personajes/`. Si el usuario no ha
  dicho quién sale, se le pregunta; no se inventan personajes ni se elige por él.
- No se da por bueno un prompt hasta que `validar_prompt.py` termina sin errores.
