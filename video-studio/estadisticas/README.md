# Estadísticas

Aquí vive lo que el director creativo y comercial aprende de cada video publicado.

| Archivo | Qué es |
|---|---|
| `datos/` | Exportaciones de YouTube Studio, TikTok e Instagram (CSV). **No se suben al repo** (es público): están en `.gitignore`. |
| `etiquetas.csv` | Una fila por video publicado: su `id` (o `titulo`) tal como sale en la exportación y las decisiones creativas que se quieren comparar (`personaje`, `modo`, `objetivo`, `gancho`, `emocion`, `duracion_s`, `formato`, `hora`) más los `creditos` que costó (de su `costos.md`). |
| `informe_AAAA-MM-DD.md` | Informe semanal: lo que calcula `estadisticas.py` más las 3 decisiones del director. |

```bash
python3 video-studio/herramientas/estadisticas.py video-studio/estadisticas/datos/*.csv \
    --etiquetas video-studio/estadisticas/etiquetas.csv --objetivo alcance \
    --salida video-studio/estadisticas/informe_$(date +%F).md
```

Objetivos: `monetizar`, `alcance`, `recordacion`, `comunidad`, `conversion`, `viralidad`. Cómo se leen los números:
`manual/10_algoritmo_y_monetizacion.md`.
