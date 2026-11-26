# Traspaso a sesión de escritorio (2026-11-26)

> **Decisión del dueño (2026-11-26), textual:** «Por el momento pásalo a Keter y haz los cambios necesarios para que
> Keter no siga como intermediario; pasa las conversaciones involucradas a sesión de desktop, entonces, si no tienes
> más alternativas».

## Por qué

Las conversaciones «Generador de prompts y carpetas para videos» y «Equipo de producción audiovisual» corren en la nube.
Desde ahí no hay navegador con la sesión del dueño (Studio, Trends), ni sus archivos, ni su tarjeta gráfica, y el
conector de Drive no acepta más de ≈ 3 MB por envío. Todo eso pasaba por Keter (sesión del PC) como intermediario: lecturas
de Studio copiadas a mano, videos que no llegaban al otro equipo. El 2026-11-26 el short 4 se presentó sin que
producción lo viera, entre otras cosas porque el archivo no podía salir de la nube.

## Alternativas vistas

| Alternativa | Qué resuelve | Qué no |
|---|---|---|
| Conectar una carpeta del PC a la sesión de la nube (Claude de escritorio → Ajustes → Claude Code → Remote Control) | Archivos y comandos en el PC | El 2026-11-26 la lista de carpetas disponibles salió vacía; no da navegador con la sesión del dueño |
| Dejar el archivo en la rama y que Keter lo baje | Pasa un archivo grande hoy | Sigue habiendo intermediario; el repositorio es público |
| **Trabajar en sesiones de escritorio (elegida)** | Navegador con Studio y Trends, Drive local, archivos grandes, tarjeta gráfica, sin copiar a mano | El PC tiene que estar encendido; el historial de la nube no viaja: viaja este traspaso y el repositorio |

## Cómo arranca la sesión de escritorio (una por conversación)

1. En el PC, abrir Claude de escritorio (o `claude` en la carpeta del clon) sobre el repositorio `Hojadevida`, rama
   `claude/laughing-dirac-s4pmig` (`git fetch origin claude/laughing-dirac-s4pmig && git checkout claude/laughing-dirac-s4pmig && git pull`).
2. Primer mensaje: «Lee `CLAUDE.md`, `video-studio/TRASPASO_A_ESCRITORIO.md`, `video-studio/COORDINACION.md` y
   `video-studio/mapa/MAPA.md` y continúa como <Generador de prompts | Equipo de producción audiovisual>. Habla en español.»
3. Una vez por máquina: `npm install` en `video-studio/motor_de_accion/` y `bash video-studio/herramientas/instalar_oido.sh`
   (ya aprobados por el dueño); ffmpeg y Python con Pillow y numpy. Cualquier otra instalación pide su sí.
4. Lo que no está en el repositorio (porque es público) hay que traerlo del Drive del dueño, carpeta «Canal YouTube -
   Entregas»: `canales/nostalgia-tin-y-tan/universo/` (los cuatro archivos «Tin & Tan - Universo - …», el registro de
   pistas en su versión «actualizado 2026-11-26, short 4») y las lecturas de `estadisticas/datos/`.

## Estado al traspasar

- **Short 4 (`TIN-EN-S-004`, `proyectos/2026-11-26_tin_y_tan_what_is_gta_6/`):** voz generada (3,1 créditos; no se
  regenera). Versión 2 renderizada (32,9 s) y **no aprobada**: el dueño dijo «intentan correr y casi no se mueven […]
  hablamos de producir algo de alta calidad». Solicitud: `cambios/2026-11-26_short4_v2_animacion_en_el_espacio.md`.
  Revisiones de animación, fotografía y continuidad en `07_revision/revision_v2_*.md` (pedidas el 2026-11-26). Sigue:
  versión 3 con esas correcciones, firmas de los cinco oficios y **puerta de presentación** en PASA antes de enseñarla.
  El video se regenera con `codigo/` y `motor_de_accion/` (0 créditos); una copia de la v2 está en
  `entregas_temporales/` hasta que llegue al Drive.
- **Reglas que no cambian:** créditos, instalar, rehacer una pieza generada y publicar piden el sí del dueño; una sola
  generación por pieza; nada de datos personales del dueño a servicios externos; Studio solo se lee.
- **Pendientes generales:** lista completa en `COORDINACION.md` y en el brief del short 4; calendario de diciembre en
  `canales/nostalgia-tin-y-tan/calendario_de_publicacion_2026-12.md` (ya está en el Google Calendar del dueño).

## Qué pasa con Keter

Con las dos conversaciones en el escritorio, Keter deja de ser intermediario: cada sesión lee Studio y Trends y mueve sus
archivos. Keter queda, si el dueño quiere, solo para estudios largos en paralelo.
