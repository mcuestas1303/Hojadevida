# Solicitud de cambio — profundidad y más efectos de video en Tin & Tan

- **Fecha:** 2026-11-23
- **Pedido del dueño, textual:** «Veamos el tercer video de Tin y Tan pero quiero que le demos profundidad y
  comencemos a usar más efectos de video. Te he pasado varios videos de ejemplo».
- **Estado:** EN REVISIÓN DEL EQUIPO · se prueba antes de aplicar al tercer video

## Qué toca de lo ya definido

| Definición | Archivo | Cómo está hoy | Cómo quedaría | ¿Choca con algo? |
|---|---|---|---|---|
| Estilo del canal | `canales/nostalgia-tin-y-tan/DESIGN.md` | Dibujo plano 2D sobre papel, sin degradados ni resplandores, cámara casi fija | Capas con paralaje, desenfoque por distancia, sombras, transiciones con efecto | No con la paleta; sí con «sin degradado ni textura» |
| Efectos de luz | perfiles emocionales de los shorts 1 y 2 | «Ninguno: calma y honestidad» | Destellos cortos y revelados desde desenfoque, con límite de frecuencia | Hay que reescribir esa fila en el perfil del short 3 |
| Ritmo | prompts de los shorts 1 y 2 | 12 a 16 cortes en ≈ 30 s | Ráfagas y respiros; gancho de varios cortes en el primer segundo | No |
| Personajes | fichas de Tin y Tan, `palitos.py` 1.3 | Sin sombra, de un solo grosor | Igual, con sombra de contacto y desenfoque cuando no están en foco | No cambia ningún rasgo |
| Herramientas | `palitos.py`, `codigo/render.py` de cada proyecto | Cada proyecto dibuja lo suyo | Una biblioteca común de efectos: `herramientas/efectos.py` | No |

## Qué deja de valer

| Pieza ya hecha | ¿Sigue sirviendo? | Qué habría que rehacer | Créditos |
|---|---|---|---|
| Shorts 1 y 2 | Sí, no se tocan | Nada | 0 |
| `DESIGN.md` | En parte | Añadir la sección de profundidad y efectos cuando el dueño elija | 0 |

**Costo total:** 0 créditos (todo es código). Costo en límite de uso: una prueba de ≈ 15 s y la biblioteca.

## Dudas

1. El dueño no dijo cuáles ejemplos son los de «profundidad» ni cuál le gusta; Keter se lo preguntó.
2. Cuánto efecto aguanta el público del canal sin que se sienta agresivo.

## Decisión del equipo

Antes de escribir el prompt del tercer video se hace una **prueba de efectos de ≈ 15 s** con Tin y Tan, por código y
sin créditos, que muestra cada técnica por separado y rotulada. El dueño elige con la prueba delante; lo elegido pasa
a `DESIGN.md` y al prompt del short 3.

## Decisión del dueño

Pendiente.
