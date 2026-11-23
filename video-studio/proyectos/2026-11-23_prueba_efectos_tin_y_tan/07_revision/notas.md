# Notas de la prueba de efectos y profundidad — Tin & Tan

- **Fecha:** 2026-11-23 · **Video:** `06_final/prueba_efectos_v1.mp4` (22,0 s, 1080x1920, 30 fps, 660 fotogramas; no se
  sube) · **Comparación:** `06_final/prueba_efectos_antes_despues.png`
- **Código:** `codigo/render.py` + `video-studio/herramientas/efectos.py` 1.0. `palitos.py` 1.3 **no se tocó**
  (mismo blob de git, `3ed0a0f`; los shorts 1 y 2 no cambian porque ni su código ni el de los personajes cambió).
- **Costo:** 0 créditos. Sin voz ni música: 37 golpes hechos con código.
- **Qué es:** comprobación técnica (se puede hacer, se lee, no molesta). No es un catálogo para que el dueño escoja:
  la selección de cada video la hace el equipo con `manual/14_efectos_y_emocion.md` (regla del dueño, 2026-11-23).
  Lo de abajo dice qué **funciona técnicamente** con este estilo; qué comunica cada efecto lo decide ese manual.

## Técnica por técnica

Costo de render = segundos de reloj que tardó ese tramo con 4 procesos, y lo mismo por segundo de video. Referencia:
el plano sin efectos (bloque 0) cuesta ≈ 5,8 s por segundo de video.

| N.º | Técnica (función) | Qué hace | Segundos | Costo de render | Riesgo |
|---|---|---|---|---|---|
| 0 | plano de comparación | El mismo plano como en los shorts 1 y 2: papel liso, línea de suelo, todo nítido y sin sombra | 0,0–1,2 | 7,0 s (≈ 5,8 s/s) | Ninguno |
| 1 | capas con paralaje (`Capa`, `Camara`, `componer`) | 7 capas con profundidad; la cámara barre y empuja y cada capa se mueve y crece según su distancia; lo lejano se funde con el papel (niebla) | 1,2–3,0 | 13,8 s (≈ 7,7 s/s) | Bajo. Con todo nítido, el lápiz del primer plano compite con los personajes: necesita el desenfoque (técnica 2) |
| 2 | cambio de foco (`Camara.foco`, `apertura`, `campo`) | El foco va de los personajes al televisor, al lápiz del primer plano, y vuelve | 3,0–4,8 | ≈ 14,5 s (≈ 8 s/s) | Medio: mientras el foco está en otra capa, las caras quedan borrosas. Nunca durante una línea de diálogo |
| 3 | sombras y papel (`sombra_contacto`, `sombra_de_suelo`, `sombra_proyectada`, `papel`) | Sombra de contacto bajo los pies y los muebles, sombra tumbada en el suelo, sombra del casete sobre el fondo; grano y viñeta | 4,8–6,2 | ≈ 15,4 s (≈ 11 s/s; incluye la luz que se mueve) | Bajo. La sombra tumbada de un muñeco de palitos es una mancha tenue: aporta poco. El grano casi no sobrevive a la compresión |
| 4 | revelado desde desenfoque (`revelar_desde_desenfoque`) | El plano entra borroso (42 px) y se aclara en 0,9 s | 6,2–7,7 | ≈ 8 s (≈ 5,4 s/s) | Bajo. Retrasa 0,3–0,4 s la lectura del objeto: no sirve para el primer fotograma (portada) |
| 5 | atravesar la escena (`atravesar`) | La cámara se mete por el hueco del carrete del casete y sale en el plano de los dos | 7,7–9,3 (el paso, 8,0–9,0) | ≈ 22 s (≈ 14 s/s: dibuja dos planos) | Medio: 3 cambios de luz en 0,15 s (justo en el límite); a pantalla llena el carrete es una mancha marrón grande |
| 6 | barrido de obturador (`barrido_obturador`) | Barrido con borde blando, borrón direccional y franja de tinta; uno horizontal y uno vertical | 9,3–10,9 (9,6 y 10,3) | ≈ 17,6 s (≈ 11 s/s) | Bajo |
| 7 | zoom de golpe y sacudida (`golpe_de_zoom`, `sacudida`) | Zoom ×1,75 con muelle a la cara de Tin, y salto a la de Tan; 8 fotogramas de sacudida | 10,9–12,4 (11,15 y 11,8) | ≈ 16,6 s (≈ 11 s/s) | Medio: a ×1,75 el casete tapa parte del rótulo y el otro personaje sale del cuadro; con texto en pantalla hay que comprobar la zona segura |
| 8 | destello y negativo (`destello`, `negativo_paleta`) | Destello de 3 fotogramas en el corte (blanco de papel al 45 %) y negativo tinta↔papel de 5 fotogramas en un círculo sobre el casete | 12,4–14,0 (12,4; 13,0; 13,6) | ≈ 11,4 s (≈ 7 s/s) | **Alto si se repite.** Es lo único que toca el límite de fotosensibilidad. Ver abajo |
| 9 | garabatos de tinta (`garabato`, `trazo_*`) | Círculo alrededor del casete, flecha al teléfono y subrayado de la palabra clave, dibujándose | 14,0–15,6 | ≈ 16,4 s (≈ 10 s/s; el costo es el plano, no el garabato) | Bajo. Hay que dejar aire: el círculo y el subrayado se pisaban y hubo que bajar el casete 40 px |
| 10 | texto: clave, vidrio, contador, cascada (`poner_texto`, `texto_vidrio`, `contador`, `titulares_en_cascada`) | Pregunta con palabra clave sobre panel translúcido, contador 0→60 que solo sube, tres titulares que caen | 15,6–17,4 | ≈ 18,7 s (≈ 10 s/s) | Medio: tres paneles a la vez tapan el objeto; la cascada a 48 px es pequeña para 45+ |
| 11 | cruce, congelado y salida (`cruce_por_delante`, `congelado_con_marco`, `salida_del_cuadro`) | El lápiz cruza y esconde el corte; el plano se congela, queda como foto con marco y cae; el siguiente entra de un latigazo | 17,4–19,4 (17,7; 18,45; 19,25) | ≈ 23,7 s (≈ 12 s/s) | Medio: el lápiz gigante oscurece el cuadro (2 cambios de luz). El congelado dura 0,75 s: caro para un short de 30 s |
| 12 | todo junto | Gancho de 4 planos en 0,6 s (19,4–20,0), zoom de golpe con sacudida, palabra clave con subrayado, cambio de foco, respiro de 2 s con empuje lento y el negativo como firma (21,3) | 19,4–22,0 | ≈ 25,7 s (≈ 10 s/s) | El gancho usa los 3 cambios de luz por segundo que hay: no admite un destello más |

No están en la prueba (existen en la biblioteca): `transicion_zoom` (corte con zoom) y `sombra_proyectada` sobre los
personajes (con trazos de 15 px la sombra desplazada se lee como una línea doble: se descartó al mirarla).

## Tiempos de render

- **Total: 213 s (3 min 33 s)** para 660 fotogramas con 4 procesos: **0,32 s de reloj por fotograma** (≈ 1,2 s de
  procesador), ≈ 9,7 s por segundo de video. El plano sin capas cuesta ≈ 5,8 s por segundo de video: la profundidad
  lo sube a ≈ 8–11, y las transiciones a ≈ 12–14 porque dibujan dos planos a la vez.
- Un short de 30 s con profundidad en todos los planos: ≈ 5 min de render.
- Se hicieron 4 renders completos (≈ 14 min de máquina) y 2 hojas rápidas. Detalle: `tiempos_de_render.json`.

## Controles

| Control | Resultado |
|---|---|
| `analizar_video.py --cada 0.5` | 22,0 s, 1080x1920, 30 fps, con audio. 3 hojas en `analisis/`, miradas una por una |
| Mirada a tamaño completo | Un fotograma por técnica (12) más el último. Texto y rótulos dentro de x 100–980, y 250–1670 (lo comprueba `comprobaciones()` antes de dibujar). Fuera de la zona segura solo hay decorado (lápiz del primer plano, mesita del teléfono) |
| `revisar_fotogramas.py` | **Sin marcas**: 0 congelados, 0 vacíos, 0 destellos (umbral 40). 10 planos; el más corto, 0,5 s a su resolución de 10 fps |
| `efectos.comprobar_destellos` | **PASA, en el límite**: 8 cambios bruscos en 22 s, **máximo 3 en 1 s (límite 3)**; mayor salto de luminosidad media 33,8 de 255 (límite 40), en el corte de 12,4 s. `destellos.json` |
| `revisar_color.py` (paleta de `DESIGN.md`) | **≈ 82 % dentro de paleta: AVISO** (umbral 85 %). Saturación ≈ 20 %, cálidos 54 %, fríos 1 % |
| `revisar_texto.py --idioma es` | **PASA, 0 errores**, 23 textos |
| `palitos.py` | Sin cambios (`git diff` vacío); shorts 1 y 2 intactos |
| Audio | 37 golpes, −24,2 LUFS, pico −6,0 dBTP. **Nadie lo ha escuchado** |

**Sobre el color.** El plano de comparación mide 91 % (no 100: los tonos de identidad de los personajes), el de
paralaje 85 %, con sombras 84 % y con paneles de vidrio 79 %. La profundidad cuesta entre 6 y 12 puntos porque el
desenfoque y la niebla crean mezclas de tinta, marrón y papel (`#C6BBA5`, `#8D8976`) que no están en la lista. No entró
ningún tono nuevo: fríos 1 %, igual que antes. Importa por una razón práctica: **`revisar_color.py` va a avisar en
todo video con profundidad**. O se baja su umbral para videos con desenfoque (≈ 75 %) o se mide además el fotograma
nítido. Decisión del director de fotografía; no se tocó la herramienta.

**Sobre los destellos.** La primera versión no pasaba (9 cambios en 1 s según una primera regla, que contaba cada
fotograma de una rampa; 5 reales en el bloque 8). Se corrigió: el negativo entra y sale a media fuerza en un fotograma
(deja de contar como cambio brusco), se quitó el segundo negativo del bloque 8 y el destello del congelado. Queda en
3 por segundo en tres sitios: al atravesar (8,5 s), en el cruce del lápiz (17,9–18,0) y en el gancho (19,6–19,8).

## Errores encontrados y corregidos

1. Desenfoque excesivo: con apertura 0,032 el televisor no se reconocía y el casete (el objeto del video) salía
   borroso. Quedó en 0,018 con una profundidad de campo de 150 (`Camara.campo`).
2. El paralaje sacaba a Tin del cuadro: barrido de ±190 px a ±95 px.
3. La cascada de titulares tapaba la cara de Tan: se subió y se redujo.
4. El negativo volvía azul marino la etiqueta blanca: ahora nada queda más oscuro que la tinta.
5. Franja negra al atravesar (el borde de la imagen ampliada): se rellena con papel.
6. En «todo junto» el empuje subía el casete sobre el texto: empuje de 150 a 75 y cámara 45 px más alta.
7. Texto: «shorts», «zoom» y «min» no están en el diccionario español (se cambiaron por «videos», «acercamiento» y
   «minutos»); «¿» y «?» en literales separados daban error (ahora la frase va entera, con la clave entre asteriscos).

## Opinión: qué funciona con este estilo y qué no

**Funcionan y las usaría en el short 3**
- **Capas con paralaje + desenfoque del fondo y del primer plano + sombra de contacto.** Es el cambio grande: en la
  hoja de antes y después el plano deja de ser una ficha y pasa a ser un lugar, y los personajes se separan del fondo
  (en plano, el televisor se confunde con las cabezas). El trazo de los personajes no cambia.
- **Empuje lento de cámara** en los respiros: con capas se nota mucho más que el «100 a 103 %» de los shorts 1 y 2.
- **Barrido de obturador** y **zoom de golpe con sacudida**: limpios, baratos y sin riesgo de luz.
- **Garabatos de tinta**: lo que mejor casa con el canal (es el lápiz de Tin). Uno por plano.
- **Revelado desde desenfoque**, una vez por video y nunca en el primer fotograma.
- **Sombra proyectada del objeto** (el casete flotando sobre el fondo).

**Con cuidado**
- **Cambio de foco**: bonito, pero deja las caras borrosas ≈ 0,5 s. Solo entre líneas de diálogo.
- **Atravesar la escena**: es el efecto más vistoso y el más caro en luz y en render. Uno por video como mucho, y con
  un hueco más grande que este (37 px de radio obligan a ampliar ×33).
- **Destello**: al 45 % de blanco de papel casi no se ve sobre papel crema. Gasta presupuesto de fotosensibilidad para
  poco efecto. Lo dejaría solo en el corte del gancho.
- **Negativo de paleta**: como firma, una vez, en círculo sobre el objeto. Nunca a pantalla completa (lo rechaza el
  control) ni repetido.
- **Texto de vidrio**: se lee bien, pero un panel a la vez. Para el público de 45+ el texto con contorno sobre papel
  ya contrasta 12,6:1; el vidrio solo hace falta si el texto va encima de un dibujo.

**Descartaría**
- **Sombra tumbada de los personajes** (`sombra_de_suelo`): con muñecos de palitos es una mancha; basta la de contacto.
- **Grano del papel**: no molesta, pero el códec lo borra. La viñeta sí se nota y se queda.
- **Titulares en cascada** a este tamaño: demasiada letra pequeña a la vez para este público.
- **Congelado con marco**: 0,75 s de transición en un video de 30 s es mucho; guardarlo para un cierre.
- **Cruce por delante** con un objeto tan grande: oscurece todo el cuadro. Si se usa, con algo más estrecho o claro.

## Pendiente (no lo hice)

- Anotar el consumo en `video-studio/consumo.md` y la entrada en `COORDINACION.md` (lo lleva la conversación principal).
- `DESIGN.md` sigue diciendo «nada de degradados»; se actualiza cuando el equipo cierre la selección.
- `02_prompt/` quedó como sale de la plantilla (es una prueba; ver `00_brief.md`).
