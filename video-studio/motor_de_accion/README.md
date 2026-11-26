# Motor de acción de Tin & Tan

> **Idea del dueño (2026-11-26), textual:** «El entorno idealmente se debe generar con base al prompt, es decir, el
> contexto y temática; aquí es donde lo pienso como un motor, o no sé cómo llamarlo, donde en la medida que vayamos
> generando videos todos los elementos los vayas almacenando, por si caben o se quieren reutilizar en algún otro video;
> pero el entorno debe cambiar dependiendo del contexto y temática del video». Sobre el color: «me gustan los A, B y C».

## Qué es

Una escena 3D por código (three.js, grabada con el Chromium de la sesión) donde Tin, Tan y el rival son dibujos 2D de
pie dentro del mundo. **Cada video elige, según su tema, una paleta y un entorno; lo que se crea para un video se queda
en la biblioteca** y se puede volver a usar. 0 créditos.

| Pieza | Dónde | Qué cambia por video |
|---|---|---|
| Paleta | `paletas/*.json` | Se elige por el tema (día, noche, competencia…). Las tres de partida salen del estudio de color |
| Entorno | `entornos/*.js` | **Uno por tema.** Se escribe a partir del prompt del video; si ya hay uno que sirve, se reutiliza |
| Personajes | `personajes/exportar_sprites.py` (cabezas oficiales) y el esqueleto de `escena.html` | No cambian; solo la línea de tinta se aclara en fondos oscuros |
| Poses, efectos, cámara | `escena.html` | Se reutilizan; lo nuevo se añade al catálogo |
| Sonidos | `sonidos/sonido.py` | Se reutilizan; lo nuevo se añade |
| Guion (quién hace qué y cuándo) | hoy dentro de `escena.html`; pasará a `guiones/` | Uno por video |
| Catálogo | `catalogo.json` | Una entrada por cada elemento, con sus temas y los videos donde se usó |

## Cómo se usa

```bash
npm install                                           # three.js (autorizado por el dueño el 2026-11-26)
python3 personajes/exportar_sprites.py sprites        # cabezas de los tres, una carpeta por paleta
node render.js salida 230 b_noche_de_tinta ciudad_de_carton      # carpeta, tope de fotogramas, paleta, entorno
python3 sonidos/sonido.py salida/eventos.json salida/sonido.wav
```

## Cómo se añade un entorno

1. El prompt del video dice el tema y el lugar. Se busca en `catalogo.json` un entorno con ese tema.
2. Si no hay, se escribe `entornos/<id>.js` con el mismo contrato que `ciudad_de_carton.js` (`construir` devuelve lo
   que se puede romper) y se anota en el catálogo con sus temas.
3. Al terminar el video se anota en «usada_en» qué paleta, entorno, efectos y sonidos llevó.

## Estado y límites (2026-11-26)

- Comprobado: corre con las tres paletas y el entorno de relleno. **No es una prueba para el dueño**: falta el entorno
  hecho para un tema real, los tiempos de golpe medidos por Keter, los defectos anotados en
  `canales/nostalgia-tin-y-tan/pruebas/2026-11-26_accion_mundo_3d/informe.md` y la voz con los datos.
- El guion de la pelea todavía está dentro de `escena.html`; hay que sacarlo para que cada video tenga el suyo.
- En la paleta C el estudio propone cambiar los colores de Tin y de Tan. No se aplica: está pendiente de que el dueño
  diga si los personajes cambian con el entorno o se quedan fijos.
- El dueño tiene otra conversación llamada «Motor generador de contenido» y avisó de que explicará ese motor
  (`CLAUDE.md`). Este motor es solo el de la acción en pantalla; cuando explique el otro se ve cómo se unen.
