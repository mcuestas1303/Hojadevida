# Ficha de personaje

> Copia la carpeta `_plantilla` como `personajes/<id>/` y llena esta ficha.
> El `<id>` es el nombre de la carpeta: minúsculas, sin espacios ni acentos (ej. `don_chepe`).
> En los prompts el personaje se cita como `@<id>`.

- **ID:** `@id_del_personaje`
- **Nombre:**
- **Rol / arquetipo:**
- **Edad aparente:**
- **Personalidad en una línea:**
- **Voz:** (tono, acento, velocidad; o ID de voz si usas TTS)

## Bloque de identidad

Un solo párrafo en inglés, de 40 a 70 palabras, que describe SOLO lo que se ve y nunca cambia:
edad aparente, complexión, piel, rostro, pelo, rasgo distintivo y vestuario base.
Este párrafo se pega **tal cual** en cada prompt donde salga el personaje; no se parafrasea.

```text
PENDIENTE
```

## Lo que nunca cambia

- (rasgo, prenda o accesorio que lo hace reconocible)

## Variaciones permitidas

- (vestuarios alternos, con nombre: `base`, `trabajo`, `fiesta`…)

## Prohibido

- (cosas que el generador suele inventar y hay que negar: barba, lentes, tatuajes…)

## Referencias (carpeta `referencias/`)

| Archivo | Qué es | Cuándo usarla |
|---|---|---|
| `hoja_personaje.png` | Hoja de personaje completa | Referencia maestra; no se sube al generador de video |
| `frente.png` | Retrato frontal, fondo neutro | Referencia de rostro para keyframes |
| `cuerpo_completo.png` | Cuerpo entero, vestuario base | Referencia de vestuario y proporción |

La hoja de personaje se genera una sola vez con `plantillas/hoja_de_personaje.md`.
