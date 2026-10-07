# Hojadevida

Hoja de vida en HTML de Marvin Cuestas (`Evaluacion Fundamentos html/`).

## Motor generador de contenido

Las páginas de `Evaluacion Fundamentos html/html/` se generan a partir de un único
archivo de datos, así el encabezado, el menú y el pie de página se escriben una sola vez.

```
Evaluacion Fundamentos html/generador/
├── contenido.json        # datos personales, páginas y secciones
├── plantillas/logo.svg   # logo compartido del encabezado
└── motor.js              # genera html/*.html
```

Para actualizar la hoja de vida:

1. Edita `generador/contenido.json`.
2. Ejecuta (requiere Node.js, sin dependencias):

   ```sh
   node "Evaluacion Fundamentos html/generador/motor.js"
   ```

No edites los archivos de `html/` a mano: el motor los sobrescribe.

### Tipos de sección

Cada página tiene una lista de `secciones`; cada una indica su `tipo`:

| Tipo                  | Campos                         | Resultado                         |
| --------------------- | ------------------------------ | --------------------------------- |
| `titulo`              | `texto`                        | Encabezado `<h3>`                 |
| `foto`                | —                              | Foto de `persona.foto`            |
| `perfil`              | —                              | Párrafo con `persona.perfil`      |
| `lista`               | `items`                        | Lista con viñetas                 |
| `tabla`               | `columnas`, `filas`            | Tabla (p. ej. estudios)           |
| `video`               | `subtitulo`, `src`, `poster`   | Reproductor de video              |
| `audio`               | `subtitulo`, `src`             | Reproductor de audio              |
| `formulario-estudios` | `anios`                        | Formulario "Agregar Estudios"     |

Para agregar una página nueva, añade un objeto a `paginas` con `archivo`, `titulo`,
`menu` y `secciones`; el menú de navegación de todas las páginas se actualiza solo.
