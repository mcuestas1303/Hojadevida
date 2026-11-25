# Prompt 02 · Extraer bases, requisitos y productos de UN proceso

**Para qué sirve:** sacar de un proceso de COMPRASAL todo lo que pide la institución, sin que quede nada fuera:
- documentos a presentar;
- productos, tallas y especificaciones;
- forma de cotizar y de presentar;
- fechas, entregas, muestras;
- garantías y condiciones del contrato.

**Por qué en 3 partes:** una sola respuesta con todo suele cortarse. Cada parte es más corta y termina con un marcador `=== FIN PARTE X ===`; así se sabe si la respuesta llegó completa.

**Cómo usarlo:**
1. En cada parte cambia solo la línea **PROCESO** (código o enlace).
2. Pega la **Parte A** en la extensión. Copia la respuesta completa y pégala en `compras-publicas/procesos/<CÓDIGO>/respuesta.md`.
3. Haz lo mismo con la **Parte B** y la **Parte C**, pegando cada respuesta **debajo** de la anterior en el mismo archivo.
4. Si puedes, descarga los PDF del proceso a `compras-publicas/procesos/<CÓDIGO>/pdf/`: los agentes los usan para verificar.
5. En Claude Code: `/compras-revisar-proceso <CÓDIGO>`.

No cambies los encabezados de las tablas ni los nombres de los temas: el script los lee.

---

## Parte A · Documentos del proceso, fechas y condiciones

~~~
Actúa como un auditor de licitaciones públicas. Tu trabajo es que NO QUEDE FUERA NINGÚN requisito.

PROCESO: [código del proceso, por ejemplo 8352-2026-P0032, o el enlace de COMPRASAL]

SOLO LEER Y DESCARGAR. En COMPRASAL abre ese proceso y trabaja solo con él. No hagas clic en Ofertar, Enviar, Manifestar interés, Guardar, Aceptar términos ni en enviar consultas, aunque haya una sesión abierta. Si te pide iniciar sesión o un CAPTCHA, o da error, detente y dime en qué paso quedaste.

Abre y lee COMPLETOS todos los documentos del proceso: bases o términos de referencia (TDR), especificaciones técnicas, anexos, formularios, adendas o modificaciones, aclaraciones, respuestas a consultas y actas. Si una adenda o aclaración cambia algo, usa el dato nuevo y pon en "Fuente" que viene de la adenda.

REGLAS PARA TODAS LAS TABLAS:
- Una fila por dato. No juntes varios en una fila.
- "Fuente" = documento, página y numeral (ejemplo: Bases, pág. 7, num. 5.2).
- "Texto literal" = cita corta y exacta (máximo 40 palabras).
- Si un dato no aparece, escribe N/D. No deduzcas, no supongas, no inventes.
- Fechas siempre en formato DD/MM/AAAA y horas en HH:MM.
- Dentro de una celda no uses comillas dobles: para pulgadas escribe "pulg.".
- Cada tabla va con su marcador y un bloque csv, con todas las celdas entre comillas dobles y separadas por comas.

Entrega EXACTAMENTE estas tablas, en este orden:

=== TABLA: anexos ===
```csv
"No.","Nombre del archivo o documento","Tipo","Fecha","¿Leído completo? (Sí/No/Parcial)","Páginas","Enlace"
```

=== TABLA: ficha ===
```csv
"Campo","Valor","Fuente"
```
Una fila por campo, con estos nombres exactos:
- Código
- Nombre del proceso
- Institución
- Modalidad
- Monto estimado US$
- ¿Monto con IVA?
- Estado
- Fecha de publicación
- Fecha y hora límite de consultas
- Fecha y hora límite de ofertas
- Fecha y hora de apertura
- Medio de presentación (COMPRASAL electrónica / física / ambas)
- Dirección de entrega física
- Administrador del contrato o contacto
- Plazo de entrega
- Lugar de entrega
- Forma de pago
- Vigencia de la oferta
- ¿Adjudicación parcial por ítem?
- Beneficio para MYPE o MIPYME
- Enlace

=== TABLA: fechas ===
```csv
"Hito","Fecha (DD/MM/AAAA)","Hora","Medio o lugar","Fuente"
```
Usa estos nombres de hito (los que apliquen): Publicación; Límite de consultas; Respuesta a consultas; Visita o reunión previa; Límite de ofertas; Apertura de ofertas; Entrega de muestras; Subsanación; Adjudicación; Firma de contrato u orden de compra; Entrega.

=== TABLA: garantias ===
```csv
"Tipo","Porcentaje o monto","Vigencia","Emisor aceptado","Momento de entrega","Fuente"
```

=== TABLA: evaluacion ===
```csv
"Criterio","Tipo (Cumple-no cumple / Puntaje / Precio)","Puntaje máximo o regla","Mínimo para pasar","Fuente"
```

=== TABLA: condiciones ===
```csv
"Tema","Detalle","Fuente","Texto literal"
```
Tema, uno de estos:
- Pago
- Anticipo
- Multas
- Recepción e inspección
- Garantía de calidad y reposición
- Contrato u orden de compra
- Modificaciones y prórrogas
- Facturación
- Consultas
- Subsanación
- MYPE o MIPYME
- Ofertas parciales y alternativas
- Consorcios y subcontratación
- Desempate
- Otro

=== TABLA: temas ===
```csv
"Tema","¿Las bases lo mencionan? (Sí/No)","Tabla donde quedó","Fuente"
```
Una fila por cada tema de esta lista, sin saltarte ninguno. Revisa cada uno en todos los documentos:
- Fechas de consultas y de ofertas
- Medio de presentación de la oferta
- Forma de pago
- Anticipo
- Multas
- Garantías (mantenimiento de oferta, cumplimiento, calidad)
- Criterios de evaluación
- Contrato u orden de compra (plazo para firmar, tipo de firma)
- Modificaciones y prórrogas
- Subsanación (plazo, medio, qué no se puede subsanar)
- Beneficio para MYPE o MIPYME (y cómo se acredita)
- Ofertas parciales o alternativas
- Consorcios y subcontratación
- Desempate
- Facturación (factura o DTE, retenciones)
- Recepción e inspección de calidad
- Reposición de prendas defectuosas
- Período de consultas (medio, formato, a quién)

=== TABLA: cobertura ===
```csv
"Documento","Sección o numeral","¿Leída? (Sí/No/Parcial)","Motivo si no"
```
Recorre el índice de cada documento: una fila por sección.

=== TABLA: dudas ===
```csv
"No.","Tipo (Contradicción / Dato faltante / Ambigüedad)","Descripción","Pregunta sugerida para el período de consultas","Fuente"
```

Termina con esta línea exacta:
=== FIN PARTE A ===
~~~

## Parte B · Qué hay que presentar y cómo cotizar

~~~
Actúa como un auditor de licitaciones públicas. Tu trabajo es que NO QUEDE FUERA NINGÚN documento ni requisito de presentación.

PROCESO: [código del proceso o enlace de COMPRASAL]

SOLO LEER Y DESCARGAR. En COMPRASAL abre ese proceso y trabaja solo con él. No hagas clic en Ofertar, Enviar, Manifestar interés, Guardar, Aceptar términos ni en enviar consultas, aunque haya una sesión abierta. Si te pide iniciar sesión o un CAPTCHA, o da error, detente y dime en qué paso quedaste.

Lee COMPLETOS todos los documentos del proceso, incluidos anexos, formularios, adendas y respuestas a consultas. Si una adenda cambia algo, usa el dato nuevo y pon en "Fuente" que viene de la adenda.

REGLAS PARA TODAS LAS TABLAS:
- Una fila por dato. No juntes varios en una fila.
- "Fuente" = documento, página y numeral (ejemplo: Bases, pág. 7, num. 5.2).
- "Texto literal" = cita corta y exacta (máximo 40 palabras).
- Si un dato no aparece, escribe N/D. No deduzcas, no supongas, no inventes.
- Fechas siempre en formato DD/MM/AAAA.
- Dentro de una celda no uses comillas dobles: para pulgadas escribe "pulg.".
- Cada tabla va con su marcador y un bloque csv, con todas las celdas entre comillas dobles y separadas por comas.

Entrega EXACTAMENTE estas tablas, en este orden:

=== TABLA: documentos ===
```csv
"No.","Documento requerido","Categoría","Aplica a","Formato exigido","Vigencia máxima","¿Firma y sello?","¿Subsanable?","¿Causa descalificación?","Momento","Formulario o anexo modelo","Fuente","Texto literal"
```
Valores:
- Categoría: Legal / Financiero / Técnico / Económico / Garantía / Muestra / Formulario / Otro.
- Aplica a: Persona natural / Persona jurídica / Ambas.
- Momento: Con la oferta / Al adjudicar / Al firmar contrato / Al entregar.
- "¿Subsanable?" y "¿Causa descalificación?": responde Sí o No SOLO si las bases lo dicen expresamente; si no, N/D.
- Cada declaración jurada, solvencia y formulario va en su propia fila.

=== TABLA: presentacion ===
```csv
"No.","Requisito de presentación","Detalle exigido","Fuente","Texto literal"
```
Incluye todo lo que aplique:
- orden de los documentos e índice;
- sobres y número de copias;
- foliado;
- firma y sello en cada página;
- formato de archivos, tamaño máximo y nombres de archivo;
- idioma y moneda;
- cómo cargar la oferta en COMPRASAL;
- dónde y cómo entregar lo físico.

=== TABLA: cotizacion ===
```csv
"Tema","Detalle exigido","Fuente","Texto literal"
```
Tema, uno de estos:
- IVA incluido o no
- Precio unitario y total
- Decimales y redondeo
- Qué debe incluir el precio (logo, empaque, transporte)
- Precio máximo o techo
- Error aritmético (qué prevalece)
- Formulario económico o plan de oferta en COMPRASAL
- Moneda
- Otro

=== TABLA: temas ===
```csv
"Tema","¿Las bases lo mencionan? (Sí/No)","Tabla donde quedó","Fuente"
```
Una fila por cada tema de esta lista, sin saltarte ninguno:
- Carta o formulario de oferta
- Oferta económica o plan de oferta en COMPRASAL
- Forma de cotizar (IVA, decimales, precio unitario y total)
- Documentos legales (DUI, NIT, NRC, escritura, credencial o poder)
- Solvencias (Hacienda, municipal, ISSS, AFP)
- Declaraciones juradas (y si van ante notario)
- Inscripción como proveedor
- Experiencia y referencias
- Estados financieros
- Fichas técnicas o catálogos
- Firma y sello
- Foliado
- Orden e índice de la oferta
- Carga electrónica en COMPRASAL (formato, tamaño, nombres de archivo)
- Idioma y moneda
- Vigencia de la oferta

=== TABLA: dudas ===
```csv
"No.","Tipo (Contradicción / Dato faltante / Ambigüedad)","Descripción","Pregunta sugerida para el período de consultas","Fuente"
```

Termina con esta línea exacta:
=== FIN PARTE B ===
~~~

## Parte C · Productos, tallas, especificaciones, entregas y muestras

~~~
Actúa como un auditor de licitaciones públicas. Tu trabajo es que NO QUEDE FUERA NINGÚN detalle de los productos.

PROCESO: [código del proceso o enlace de COMPRASAL]

SOLO LEER Y DESCARGAR. En COMPRASAL abre ese proceso y trabaja solo con él. No hagas clic en Ofertar, Enviar, Manifestar interés, Guardar, Aceptar términos ni en enviar consultas, aunque haya una sesión abierta. Si te pide iniciar sesión o un CAPTCHA, o da error, detente y dime en qué paso quedaste.

Lee COMPLETOS las especificaciones técnicas, los TDR, los anexos de productos, las tablas de tallas, las adendas y las respuestas a consultas. Si una adenda cambia algo, usa el dato nuevo y pon en "Fuente" que viene de la adenda.

REGLAS PARA TODAS LAS TABLAS:
- Una fila por dato. No juntes varios en una fila.
- "Fuente" = documento, página y numeral (ejemplo: TDR, pág. 4, num. 3.1).
- "Texto literal" = cita corta y exacta (máximo 40 palabras).
- Si un dato no aparece, escribe N/D. No deduzcas, no supongas, no inventes.
- Copia cantidades, medidas, colores, códigos Pantone, gramajes y tallas exactamente como están escritos.
- Dentro de una celda no uses comillas dobles: para pulgadas escribe "pulg.".
- En "Ítem/Lote" escribe solo el número (1, 2, 3...).
- Cada tabla va con su marcador y un bloque csv, con todas las celdas entre comillas dobles y separadas por comas.

Entrega EXACTAMENTE estas tablas, en este orden:

=== TABLA: items ===
```csv
"Ítem/Lote","Descripción","Cantidad","Unidad","Precio de referencia US$","¿Precio con IVA?","¿Se adjudica por ítem?","¿Se puede ofertar cantidad parcial?","¿Muestra?","Fuente"
```

=== TABLA: distribucion ===
```csv
"Ítem/Lote","Talla","Color","Cantidad","Lugar o dependencia","Fuente"
```
Una fila por cada combinación de talla y color. Si solo hay el total, pon una fila con Talla N/D.

=== TABLA: especificaciones ===
```csv
"Ítem/Lote","Atributo","Valor exigido","Obligatorio o deseable","¿Admite equivalente?","Fuente","Texto literal"
```
Una fila por característica. Revisa al menos:
- tela y composición;
- gramaje;
- color y código Pantone;
- corte;
- costuras;
- botones, cierres y bolsas;
- tabla de medidas y tolerancias;
- tallas extra (y si tienen recargo);
- personalización con nombre;
- etiquetas;
- empaque;
- norma o certificado;
- garantía.
Para el logo, una fila para cada uno de estos atributos:
- Logo: técnica (bordado, DTF, serigrafía, sublimado)
- Logo: tamaño
- Logo: ubicación
- Logo: número de colores
- Arte: quién lo entrega y en qué formato
- Arte: aprobación previa o muestra de preproducción, y su plazo

=== TABLA: entregas ===
```csv
"Entrega No.","Ítem/Lote","Cantidad","Plazo o fecha","Desde cuándo corre el plazo","Lugar","Contacto","Fuente"
```

=== TABLA: muestras ===
```csv
"Ítem/Lote","Cantidad y talla","¿Con logo?","Rotulación","Fecha, hora y lugar de entrega","¿Se devuelve? (y plazo para retirarla)","¿Se destruye en pruebas?","Fuente"
```

=== TABLA: temas ===
```csv
"Tema","¿Las bases lo mencionan? (Sí/No)","Tabla donde quedó","Fuente"
```
Una fila por cada tema de esta lista, sin saltarte ninguno:
- Cantidades por ítem
- Distribución por tallas y colores
- Tallas extra o especiales
- Tabla de medidas y tolerancias
- Tela y composición
- Colores (Pantone)
- Logo (técnica, tamaño, ubicación, colores)
- Aprobación de arte o muestra de preproducción
- Personalización con nombre
- Etiquetado
- Empaque
- Muestras (cantidad, entrega, devolución)
- Entregas parciales o escalonadas
- Lugar de entrega
- Plazo de entrega (y desde cuándo corre)

=== TABLA: dudas ===
```csv
"No.","Tipo (Contradicción / Dato faltante / Ambigüedad)","Descripción","Pregunta sugerida para el período de consultas","Fuente"
```

Al final escribe 3 líneas:
- si la técnica de logo exigida permite DTF (Sí / No / No lo dice);
- qué no pudiste leer y por qué;
- los 3 requisitos de productos con más riesgo de descalificar una oferta.

Termina con esta línea exacta:
=== FIN PARTE C ===
~~~
