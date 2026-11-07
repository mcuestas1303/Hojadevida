# Dónde quedamos (2026-11-07)

Punto de entrada para retomar el proyecto de personajes, influencers y avatares con IA.

## Herramientas

- **Higgsfield MCP** (conector personalizado `https://mcp.higgsfield.ai/mcp`): genera imagen, video y audio con los
  créditos del plan Plus. El conector «Higgsfield AI» del directorio solo lee: no sirve para generar.
- **Red del entorno Default:** se permitieron `upload.higgsfield.ai`, `d8j0ntlcm91z4.cloudfront.net` y
  `d2ol7oe51mr4n9.cloudfront.net` para subir fotos y revisar resultados.
- **Vista previa sin costo:** `creador-personajes/index.html` dibuja un boceto del personaje y arma el prompt para Higgsfield.
- **Agente que decide herramientas:** `experto-influencers` del repo `motor-de-marketing`.

## Personajes

- `personajes/reserva.md`: **Spike** (en uso), **el científico** y **el afro verde** (en reserva), con IDs y prompts.
- `personajes/marvin.md`: el creador, con los IDs de sus dos fotos subidas a Higgsfield.
- `personajes/lumi-bravo.md`: Lumi Bravo (cómic 2D, todavía sin generar).

## Videos hechos

- `shorts/01-spike-y-marvin.md`: Short 01, 12 s, Seedance 2.0 (54 créditos). Al creador no le convenció.
- `shorts/02-cientifico-y-spike.md`: Short 02, 24 s, Seedance 2.0 Mini (24 créditos). Hay que corregir el fondo de la parte 2.
- Los videos están en el historial de Higgsfield (IDs en cada archivo). No se guardan en el repo porque es público.

## Decisiones

- No se usan videos de terceros como fuente para calcarlos (reel o «making of»). Para replicar un trend, el creador
  graba su propia versión y se le transfiere el movimiento con Genjutsu (unos 84 créditos por 12 s en 720p).
- Los personajes son originales: Spike no copia rasgos de personajes existentes.
- La música la pone el creador; los videos se generan sin audio.

## Pendiente

1. Que el creador grabe su clip si quiere una réplica del trend con transferencia de movimiento.
2. Corregir el fondo de la parte 2 del Short 02, si se regenera.
3. Publicar la vista previa como página con enlace, si el creador quiere usarla desde el celular.
4. Ponerle nombre al científico y al afro verde.
