# Elenco

Lista de personajes disponibles. Un personaje existe para el estudio solo si tiene
`personajes/<id>/ficha.md` con su bloque de identidad y al menos una imagen en `referencias/`.
Ningún prompt puede usar un personaje que no esté aquí.

| ID | Nombre | Rol | Público / canal | Ficha | Carpeta terminada en Drive |
|---|---|---|---|---|---|
| `@tiky` | Tiky | Pollito curioso | Infantil (1–3 años) | `tiky/ficha.md` | `Personajes/Universo juguetes/Tiky (pollito)` |
| `@lumi` | Lumi | Vaca de las buenas ideas | Infantil (1–3 años) | `lumi/ficha.md` | `Personajes/Universo juguetes/Lumi (vaca)` |
| `@spike` | Spike | Tecladista excéntrico, humor absurdo | Jóvenes y adultos | `spike/ficha.md` | `Personajes/Spike` |
| `@tan` | Tan | Muñeca de palitos que recuerda y pregunta (v1, por aprobar) | Adultos, canal de nostalgia | `tan/ficha.md` | `Personajes/Tin & Tan (palitos)` |
| `@tin` | Tin | Muñeco de palitos que hace la cuenta (v1, por aprobar) | Adultos, canal de nostalgia | `tin/ficha.md` | `Personajes/Tin & Tan (palitos)` |

Cada carpeta de Drive tiene `01 Diseño aprobado` (referencia principal), `02 Hojas de personaje` (vueltas y
emociones, cuando existen), `03 Pruebas descartadas` (no se usa nunca) y `bitacora.md`.

## Todavía no cargados

| Personaje | Por qué no | Qué falta |
|---|---|---|
| «M» (Marvin como héroe de acción, solo adultos) | diseño sin cerrar | elegir el retrato del look calvo y regenerar el look 2 (ver `creador-personajes/ESTADO.md`) |
| Marvin (el creador) | es una persona real; sus fotos no van al repo público | el dueño decide si se carga con referencias guardadas solo en Higgsfield |
| El científico, el afro verde | en reserva | nombre y aprobación del dueño |
| Lumi Bravo | sin generar | diseño |

**Tin y Tan no se generan con IA:** se dibujan con código (`herramientas/palitos.py`), que es su diseño oficial.

**Separación de públicos:** el contenido infantil (`@tiky`, `@lumi`) nunca se cruza con `@spike`, `@tin`, `@tan`, «M»
ni humor para adultos, y se publica en un canal propio.
