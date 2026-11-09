# Dónde quedamos (actualizado 2026-11-09)

Punto de entrada para retomar el proyecto de personajes, influencers y avatares con IA.

## Herramientas

- **Higgsfield MCP** (conector personalizado `https://mcp.higgsfield.ai/mcp`): genera imagen, video y audio con los
  créditos del plan Plus. El conector «Higgsfield AI» del directorio solo lee: no sirve para generar.
- **Red del entorno Default:** se permitieron `upload.higgsfield.ai`, `d8j0ntlcm91z4.cloudfront.net` y
  `d2ol7oe51mr4n9.cloudfront.net` para subir fotos y revisar resultados.
- **Vista previa sin costo:** `creador-personajes/index.html` dibuja un boceto del personaje y arma el prompt para Higgsfield.
  `herramientas/boceto.js` dibuja el boceto desde una ficha `fichas/<personaje>.json` para mostrarlo en el chat.
- **Método gratis fuera de Higgsfield (principal para definir):** `colab/bocetos_flux_schnell.ipynb`, FLUX.1 schnell
  en la GPU gratis de Google Colab. Sin probar todavía en una sesión real.
- **Agente que decide herramientas:** `experto-influencers` del repo `motor-de-marketing`.
- **Afinador de prompts:** agente `afinador-de-personajes` (`.claude/agents/`) y comando `/afinar-personaje <nombre>`.
  Lleva una bitácora por personaje en `afinado/` con lo que gusta (fijado), lo que no va y cada versión del prompt.
- **Revisor de atención:** agente `revisor-de-atencion`. Dice para qué público y nicho está diseñado el personaje,
  si coincide con el buscado y qué capta la atención en el feed. Se apoya en los expertos de `motor-de-marketing`.
- **Casos de estudio:** `casos/` con análisis de personajes ajenos como referencia (sin copiarlos). Primer caso:
  `casos/jean-philanthrope.md`, preliminar, a completar con capturas de su perfil.
- **Red:** también se permitió Instagram, pero sin iniciar sesión no muestra perfiles; las referencias van por capturas.

## Procedimiento de créditos

- `PROCEDIMIENTO.md`: precios verificados y la escalera para gastar lo mínimo (gratis → Z Image 0,15 → imagen
  oficial 1,5–2 → prueba de video 2,5 → video final 12–54). Saldo al 2026-11-07: 915,23 créditos.

## Producción híbrida

- Imágenes en la **web** de Higgsfield con modelos «Unlimited» del plan Plus (gratis); Claude recoge y revisa desde el
  historial. **La conexión de Claude es solo de lectura** (saldo, historial, catálogo); generar desde aquí solo en
  emergencia con aprobación. Reforzado en `.claude/settings.json`. Ver `PROCEDIMIENTO.md`.
- Pendiente: que el dueño confirme qué modelos aparecen como «Unlimited» en su cuenta.

## Personajes

- `personajes/reserva.md`: **Spike** (en uso), **el científico** y **el afro verde** (en reserva), con IDs y prompts.
- `personajes/marvin.md`: el creador, con los IDs de sus dos fotos subidas a Higgsfield.
- `personajes/lumi-bravo.md`: Lumi Bravo (cómic 2D, todavía sin generar).

## Universo

- `universo/README.md`: idea de un universo de personajes (el científico como papá de Spike, su esposa e hijos para
  contenido infantil). Ideas sin decidir; el dueño no quiere profundizar todavía.

## Contenido infantil

- **Tiky** (pollito) y **Lumi** (vaca, nombre provisional): versiones 3D (principal) y 2D (libros para colorear)
  aprobadas el 2026-11-08. IDs en `personajes/reserva.md`.

## Videos hechos

- `shorts/01-spike-y-marvin.md`: Short 01, 12 s, Seedance 2.0 (54 créditos). Al creador no le convenció.
- `shorts/02-cientifico-y-spike.md`: Short 02, 24 s, Seedance 2.0 Mini (24 créditos). Hay que corregir el fondo de la parte 2.
- Los videos están en el historial de Higgsfield (IDs en cada archivo). No se guardan en el repo porque es público.

## Decisiones

- No se usan videos de terceros como fuente para calcarlos (reel o «making of»). Para replicar un trend, el creador
  graba su propia versión y se le transfiere el movimiento con Genjutsu (unos 84 créditos por 12 s en 720p).
- Los personajes son originales: Spike no copia rasgos de personajes existentes.
- La música la pone el creador; los videos se generan sin audio.

## Última sesión (2026-11-09)

- **Tiky y Lumi** (contenido infantil): aprobados en 3D (principal) y 2D (libros para colorear). Lumi: la 3D con
  crayón y la 2D sin crayón. Nombre «Lumi» provisional (choca con Lumi Bravo).
- **«M»** (Marvin como héroe de acción, solo adultos): estilo cinematográfico realista, dos looks aprobados
  (`dac065d4-…` con bandana, `3c745e78-…` calvo). Arsenal en su perfil, escena propia cuando convenga. Faceta de papá
  pendiente. Detalle en `afinado/marvin-figura.md`.
- **Rostro oficial de Marvin:** retrato B `deb79874-05f4-48f1-af29-91871b4e58da` (look con pelo).
  Look calvo: barba de 5-6 cm recién arreglada; retrato por elegir entre `b5f6dc8c-…` (A) y `bc973d9b-…` (B).
  Ver `personajes/marvin.md`.
- **Generación:** el dueño pidió que Claude genere por la conexión (MCP) cuando se lo pide; se cotiza y se avisa el
  costo. Modelo habitual: Nano Banana 2 (1,5 créditos por imagen; el básico falló). Saldo ≈ 888 créditos.

## Pendiente

**Próximo paso con «M»:**
1. El dueño elige el retrato del look calvo (A o B).
2. Regenerar el look 2 de cuerpo entero con esa cara, tatuaje del antebrazo y **sin** tatuaje en el cuello (≈1,5).
3. Crear tres **Elementos** de Higgsfield (personajes guardados): rostro de Marvin, «M» look 1 y «M» look 2, y
   usarlos con `<<<id>>>` en los prompts para mantener la cara y los distintivos en cualquier escena.
4. Prueba de consistencia en 2-3 escenas (≈4-5 créditos). Si no alcanza: Soul ID con 5-20 fotos reales.
5. Más adelante: tatuajes definitivos, vestimentas y las facetas (deportes, emprendedor, arsenal, papá).

**Otros:**

1. Que el creador grabe su clip si quiere una réplica del trend con transferencia de movimiento.
2. Corregir el fondo de la parte 2 del Short 02, si se regenera.
3. Publicar la vista previa como página con enlace, si el creador quiere usarla desde el celular.
4. Ponerle nombre al científico y al afro verde.
