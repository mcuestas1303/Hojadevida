# Reglas de generación

Regla del dueño (2026-11-20): **los créditos se cuidan. No se generan segundos intentos.**
Todo lo que se genera debe estar definido antes, y todo cambio pasa primero por el equipo.

## 1. Un intento por pieza

- Cada imagen, clip o audio se genera **una sola vez**.
- Si el resultado sale mal, **no se repite**: se informa al dueño qué falló, por qué, y cuánto
  costaría rehacerlo. Solo él autoriza otra generación, pieza por pieza.
- Lo que falló se anota en la ficha del personaje o del lugar («Fallos conocidos»), para que
  la definición lo prevenga la próxima vez.
- Ningún generador garantiza el resultado al primer intento. Lo que sí se controla es llegar
  con todo definido y no gastar de nuevo sin permiso.

## 2. Definición cerrada antes de generar

No se genera nada hasta que exista y esté completo:

| Qué | Dónde | Qué debe decir |
|---|---|---|
| Personaje | `personajes/<id>/ficha.md`, sección «Definición para generar» | Proporciones medibles, lista de rasgos a comprobar, fallos conocidos, imagen de referencia |
| Lugar | `series/<serie>/entorno.md` | Cada elemento del lugar descrito sin ambigüedad, lo que no debe haber, imagen de referencia del lugar |
| Pieza | `<proyecto>/03_keyframes/definicion.md` | Por cada imagen o clip: referencias que se suben, composición con medidas, qué debe verse, qué no, modelo, ajustes y costo cotizado |
| Aprobación | La misma `definicion.md` | Visto bueno del equipo y **autorización del dueño** con el costo total a la vista |

Si falta un dato (una proporción, un color, la forma de un objeto), no se supone: se pregunta
al dueño o se define con el equipo, y se escribe.

Antes de enviar una pieza al generador se cotiza y se compara con lo autorizado. Si el costo
es mayor, no se genera.

## 3. Cuando el dueño pide un cambio

Ningún cambio se aplica ni se genera directamente. Primero pasa por el equipo:

1. Se abre `cambios/AAAA-MM-DD_<tema>.md` con la plantilla `plantillas/solicitud_cambio.md`.
2. Se revisa qué toca de lo ya definido: fichas de personaje, entorno, biblia de la serie,
   frases fijas, guiones aprobados, prompts archivados, rúbricas y piezas ya generadas.
3. Opina quien corresponda: pedagoga, psicóloga, guionista, director de prompts, comercial.
4. Se le presenta al dueño: qué cambia, qué deja de valer, qué hay que rehacer y cuánto
   cuesta en créditos, con las dudas que haya que aclarar.
5. Con su respuesta se actualizan primero las definiciones. Solo después se genera, una vez.

## 4. Registro

Cada generación se anota en `costos.md` del proyecto, también las fallidas.
