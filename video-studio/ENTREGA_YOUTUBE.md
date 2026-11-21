# Entrega de videos terminados al publicador de YouTube

> Protocolo acordado el 2026-11-21 entre el dueño y la conversación «Canal automatizado de YouTube», que corre en la
> PC del dueño y sube los videos. Esa conversación **no puede responder mensajes**: si algo del protocolo no sirve, se
> le dice al dueño.

## Regla vigente del dueño

**Todo se sube en PRIVADO.** Para hacerlo público o programarlo, el publicador le presenta al dueño qué se publica,
sus objetivos y el plan para alcanzarlos, y espera su sí a ese video. Más adelante el dueño puede autorizar que se
haga solo.

## Dónde se entrega

Google Drive del dueño → carpeta **«Canal YouTube - Entregas»** → una subcarpeta por video, con el **código de
trazabilidad** del video como nombre.

## Qué lleva cada subcarpeta

| Archivo | Requisito |
|---|---|
| `video.mp4` | el video terminado |
| `miniatura.png` o `.jpg` | 1280×720, menos de 2 MB, texto puesto en edición (no dentro de la imagen generada) |
| `subtitulos.srt` | opcional |
| `ficha.json` | campos de abajo; si el proyecto ya tiene otros campos, se mantienen y se agregan estos |

```json
{
  "codigo": "código de trazabilidad",
  "canal": "en | es",
  "titulo": "máximo 100 caracteres, sin < ni >",
  "descripcion": "texto público, máximo 5.000 bytes, sin < ni >",
  "etiquetas": ["...", "..."],
  "idioma": "en | es",
  "categoria_id": "22",
  "contenido_sintetico_realista": false,
  "para_ninos": false,
  "objetivos": [{"metrica": "vistas", "meta": 1000, "plazo_dias": 28}],
  "fecha_sugerida": "2026-12-01T18:00:00-06:00",
  "archivos": {"video": "video.mp4", "miniatura": "miniatura.png", "subtitulos": "subtitulos.srt"},
  "notas": "fuentes verificadas, música y su licencia, qué escenas son de IA, riesgos"
}
```

- `canal`: `en` (inglés, EE. UU.) o `es` (español, público hispano general).
- `etiquetas`: en total, máximo 500 caracteres.
- `contenido_sintetico_realista` y `para_ninos` **los decide una persona** (el dueño); el equipo propone.
- `objetivos`: medibles y con plazo; salen del KPI de `02_prompt/direccion.md` §1 y §8.
- `fecha_sugerida`: opcional, ISO con zona horaria.

## Controles del publicador

Rechaza la entrega si falta un campo, si el título pasa de 100 caracteres, si falta un archivo o si el código ya se
subió (no se sube dos veces). Antes de entregar, el equipo corre:

```bash
python3 video-studio/herramientas/entrega.py <carpeta_de_entrega>
```

que revisa todo eso (y la miniatura) sin subir nada.

## Lo que conviene cuidar (política de contenido «no auténtico» de YouTube)

La política evalúa el canal entero: dos videos seguidos no repiten la misma estructura, música ni estilo de
miniatura; el video cumple lo que promete el título; no se usa material ajeno sin licencia.

## En el flujo del equipo

Al terminar `/producir` (sección 3), con el video aprobado por el supervisor: el editor arma la carpeta de entrega en
`<proyecto>/08_entrega/<codigo>/`, el director llena `ficha.json`, se corre `entrega.py`, y la carpeta se sube a Drive
**solo con el visto bueno del dueño**. Los videos no se suben al repositorio (es público).
