# Prompt 02 · Extraer bases, requisitos y productos de UN proceso

**Para qué sirve:** sacar de un proceso de COMPRASAL todo lo que pide la institución (documentos, productos, especificaciones, forma de presentar, fechas, garantías), sin que quede nada fuera.

**Cómo usarlo:**
1. Cambia solo la línea **PROCESO** (código o enlace).
2. Pega el prompt en la extensión de Chrome.
3. Guarda la respuesta completa, tal cual, en `compras-publicas/procesos/<CÓDIGO>/respuesta.md`.
4. Si puedes, descarga también los PDF del proceso en `compras-publicas/procesos/<CÓDIGO>/pdf/`: los agentes los usan para verificar.
5. En Claude Code: `/compras-revisar-proceso <CÓDIGO>`.

No cambies los encabezados de las tablas: el script los lee tal cual.

---

```
Actúa como un auditor de licitaciones públicas. Tu trabajo es que NO QUEDE FUERA NINGÚN requisito de este proceso.

PROCESO: [código del proceso, por ejemplo 8352-2026-P0032, o el enlace de COMPRASAL]

Ve a https://www.comprasal.gob.sv, abre ese proceso y trabaja solo con él. No inicies sesión ni envíes formularios (solo búsqueda y descarga). Si algo exige inicio de sesión, CAPTCHA o da error, detente y dime en qué paso quedaste.

PASO 1 – Inventario de documentos.
Lista TODOS los documentos del proceso: bases o términos de referencia (TDR), especificaciones técnicas, anexos, formularios, adendas o modificaciones, aclaraciones, respuestas a consultas, actas. Ábrelos todos.

PASO 2 – Lectura completa.
Lee cada documento COMPLETO, todas las páginas y anexos. No resumas.
Reglas:
- Si una adenda o aclaración cambia algo, usa el dato nuevo y anota en "Fuente" que viene de la adenda.
- Si un documento está escaneado como imagen y no puedes leerlo, dilo en la tabla "cobertura".

PASO 3 – Extrae la información en las tablas de abajo.
Reglas:
- Una fila por cada requisito, documento, ítem o característica. No agrupes varios en una fila.
- "Fuente" = documento, página y numeral (ejemplo: "Bases, pág. 7, num. 5.2").
- "Texto literal" = cita corta y exacta del documento (máximo 40 palabras).
- Si un dato no aparece, escribe N/D. No inventes ni supongas nada.
- Copia las cantidades, medidas, colores, códigos Pantone, gramajes y tallas exactamente como están escritos.
- En especificaciones, haz una fila por cada característica (tela, composición, gramaje, color, corte, costuras, botones, cierres, bolsas, etiquetas, empaque, tallas). Para el logo: técnica (bordado, DTF, serigrafía, sublimado), tamaño, ubicación, número de colores y quién entrega el arte.

PASO 4 – Revisión final de cobertura.
Recorre el índice de cada documento y confirma que leíste cada sección. Después revisa, uno por uno, si el proceso dice algo de estos temas:
- Carta o formulario de oferta y oferta económica.
- Documentos legales (DUI, NIT, NRC, escritura, credencial o poder del representante).
- Solvencias (Hacienda, municipal, ISSS, AFP).
- Declaraciones juradas.
- Inscripción como proveedor.
- Experiencia y referencias.
- Estados financieros.
- Muestras.
- Fichas técnicas y catálogos.
- Garantías (mantenimiento de oferta, cumplimiento, calidad).
- Plazo y lugar de entrega.
- Forma de pago.
- Multas.
- Vigencia de la oferta.
- Idioma y moneda.
- Firma y sello.
- Foliado.
- Orden y formato de presentación.
- Carga electrónica.
- Criterios de evaluación.
- Período de consultas.
Si un tema aparece, debe estar en alguna tabla. Si no aparece, no lo agregues.

ENTREGA – Usa EXACTAMENTE este formato. Cada tabla va con su marcador "=== TABLA: nombre ===" y debajo un bloque csv con estos encabezados (todas las celdas entre comillas dobles). Si una tabla no tiene filas, deja solo los encabezados.

=== TABLA: ficha ===
"Campo","Valor","Fuente"
(Una fila por campo, en este orden: Código; Nombre del proceso; Institución; Modalidad; Monto estimado US$; Estado; Fecha de publicación; Fecha y hora límite de consultas; Fecha y hora límite de ofertas; Fecha de apertura; Medio de presentación (COMPRASAL electrónica / física / ambas); Dirección de entrega física; Administrador del contrato o contacto; Plazo de entrega; Lugar de entrega; Forma de pago; Vigencia de la oferta; ¿Adjudicación parcial por ítem?; ¿Reservado o con beneficio para MYPE?; Enlace)

=== TABLA: anexos ===
"Nº","Nombre del archivo o documento","Tipo","Fecha","¿Leído completo? (Sí/No/Parcial)","Páginas","Enlace"

=== TABLA: documentos ===
"Nº","Documento requerido","Categoría","Aplica a","Formato exigido","Vigencia máxima","¿Firma y sello?","¿Subsanable?","¿Causa descalificación?","Momento","Formulario o anexo modelo","Fuente","Texto literal"
(Categoría: Legal / Financiero / Técnico / Económico / Garantía / Muestra / Formulario / Otro. Aplica a: Persona natural / Persona jurídica / Ambas. Momento: Con la oferta / Al adjudicar / Al firmar contrato / Al entregar.)

=== TABLA: items ===
"Ítem/Lote","Descripción","Cantidad","Unidad","Precio de referencia US$","¿Se adjudica por ítem?","Tallas / colores / distribución","Plazo de entrega","Lugar de entrega","¿Muestra?","Fuente"

=== TABLA: especificaciones ===
"Ítem/Lote","Atributo","Valor exigido","Obligatorio o deseable","¿Admite equivalente?","Fuente","Texto literal"

=== TABLA: presentacion ===
"Nº","Requisito de presentación","Detalle exigido","Fuente","Texto literal"
(Orden de los documentos, sobres, número de copias, foliado, firma y sello en cada página, índice, formato de archivos, tamaño máximo, nombres de archivo, idioma, moneda, cómo cargar en COMPRASAL, cómo y dónde entregar la muestra.)

=== TABLA: fechas ===
"Hito","Fecha (DD/MM/AAAA)","Hora","Medio o lugar","Fuente"

=== TABLA: evaluacion ===
"Criterio","Tipo","Puntaje máximo o regla","Mínimo para pasar","Fuente"
(Tipo: Cumple-no cumple / Puntaje / Precio.)

=== TABLA: garantias ===
"Tipo","Porcentaje o monto","Vigencia","Emisor aceptado","Momento de entrega","Fuente"

=== TABLA: condiciones ===
"Tema","Detalle","Fuente"
(Tema: Pago / Anticipo / Multas / Plazo de entrega / Recepción / Garantía de calidad / Otro.)

=== TABLA: cobertura ===
"Documento","Sección o numeral","¿Leída? (Sí/No/Parcial)","Motivo si no"

=== TABLA: dudas ===
"Nº","Tipo","Descripción","Pregunta sugerida para el período de consultas","Fuente"
(Tipo: Contradicción / Dato faltante / Ambigüedad.)

Al final escribe 3 líneas:
- cuántos documentos leíste completos y cuántos no;
- qué no pudiste leer y por qué;
- los 3 requisitos que más riesgo tienen de descalificar una oferta.
```
