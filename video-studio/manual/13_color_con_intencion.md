# 13 · Color con intención (psicología del color y colorimetría)

> Regla del dueño (2026-11-21): los videos llevan un filtro de color; el agente que corresponde se capacita, el
> color entra en las revisiones y decisiones, y **en la ficha queda por qué se eligió cada color y cómo ayuda a
> cumplir el objetivo**.
> Fuente del dueño: reel de andrea.eskailet (Instagram, 2026-11-20, https://www.instagram.com/p/DfcEl9Hj0Mg/),
> resumido por Keter en el Cerebro (nodo «consejos-de-los-videos»).

**Quién:** el **director de fotografía** decide el color y lo escribe en la dirección; el **director creativo**
comprueba que sirva al objetivo comercial; el **supervisor de continuidad** lo mide y lo firma (control 8 del
capítulo 12). El editor lo aplica e iguala en edición, gratis.

## 1. Lo que se sabe y lo que no

- El color sí cambia lo que la gente siente, piensa y hace, pero **su significado depende del contexto** (teoría del
  color en contexto). La propia revisión dice que el campo está en una etapa temprana y que faltan límites y
  pruebas en la vida real (Elliot y Maier, *Annual Review of Psychology* 65, 2014,
  https://pubmed.ncbi.nlm.nih.gov/23808916/). Por eso **no hay tabla de significados fijos**: cada color es una
  hipótesis que se escribe con su razón y se mide con los resultados del video.
- El tono, la saturación y la luminosidad del color de una marca cambian la personalidad que se le percibe y la
  intención de compra (Labrecque y Milne, *Journal of the Academy of Marketing Science* 40, 2012, cuatro estudios;
  https://link.springer.com/content/pdf/10.1007/s11747-010-0245-y.pdf). Se leyó el resumen, no el texto completo:
  no se citan sus asociaciones color-rasgo hasta leerlo.
- La cifra que circula de «62 a 90 % del juicio sobre un producto se basa solo en el color» viene de una revisión
  (Singh, *Management Decision* 44, 2006) que la toma de un instituto comercial. **No se usa como dato.**
- **Público de 45 años o más:** con la edad el cristalino amarillea, cuesta más distinguir azules, verdes y
  morados (GerontoVis 2024, https://arxiv.org/pdf/2403.13173), y dos pasteles que un joven separa se ven iguales; los
  azules oscuros se ven más oscuros (guía de diseño de Sherwin-Williams citando a una científica del color,
  https://www.sherwin-williams.com/architects-specifiers-designers/inspiration/stir/sw-art-stir-color-aging-eye;
  fuente de la industria, no un estudio controlado). Vistos en resumen de buscador el 2026-11-21. Para
  ese público se separa por **claro contra oscuro**, no solo por tono.
- **Daltonismo:** nunca se separa información solo por rojo contra verde; siempre hay también diferencia de
  luminosidad o de forma.

## 2. La regla de la paleta: 2 neutros + 1 acento (reel del dueño)

1. Cada pieza lleva **dos colores neutros y uno de acento**.
2. **Los neutros fijan el tono** de la pieza (fondo y texto/líneas).
3. **El acento va solo en el título y en un elemento**, y es el que cambia lo que transmite la pieza. Ejemplo del
   reel: negro medianoche `#030308` con blanco roto `#DECEC5` transmite elegancia; si se suma rojo carmesí `#C40D2E`,
   transmite impacto.
4. Los colores de identidad de los personajes (la cabeza naranja de Tin, la verde azulada de Tan) no cuentan como
   acento: son el personaje. El acento es lo que el equipo elige para **esa** pieza.
5. Un acento por plano (ya estaba en `DESIGN.md` de Tin & Tan). Si un plano necesita dos acentos, está mal
   planteado.

## 3. Color al servicio del objetivo comercial

Hipótesis de partida. Se escribe cuál se usa y se mide con el KPI del video.

| Objetivo | Qué hace el color | Cómo se mide |
|---|---|---|
| Recordación, presencia | la **misma** paleta y el mismo acento en todas las piezas del canal: se reconoce antes de leer el nombre | búsquedas del canal, regreso de espectadores |
| Retención, viralidad | el acento **salta** sobre neutros apagados desde el primer cuadro; el ojo va a un solo lugar | visto frente a deslizado, retención del segundo 1 al 3 |
| Conversión, monetización | el acento va **solo** en la palabra clave o el llamado a la acción; nada más compite | clics, suscripciones desde el video |
| Comunidad | neutros cálidos y familiares; el acento en el gesto del personaje, no en el texto | comentarios, compartidos |
| Infantil 1 a 3 años | colores claros y suaves, sin acentos estridentes ni destellos (`infantil/guia_1_a_3.md`) | lo decide la psicóloga; no se busca «enganchar» |

## 4. Color según la emoción

La tabla de luz y paletas del capítulo 03 es el punto de partida. En corto: los cálidos acercan (nostalgia,
ternura), los fríos alejan o calman, la saturación alta da energía, la baja da calma o melancolía, y la luminosidad
baja da tensión. Todo esto vale **en contexto**: se escribe la razón para este público y esta pieza.

## 5. Colorimetría: lo que se mide (gratis)

`python3 video-studio/herramientas/revisar_color.py <imagen|video> --paleta <DESIGN.md o "#hex,...">`

1. **Paleta:** al menos ≈ 85 % del cuadro dentro de la paleta declarada (ΔE < 12). Si baja, se explica qué color
   entró y por qué.
2. **Texto legible:** contraste de texto sobre fondo de 4,5:1 como mínimo (WCAG 2.x) y **7:1 para público de 45 o
   más** (`revisar_color.py --contraste "#texto" "#fondo"`). Un texto en color de acento claro (mostaza sobre papel
   da 1,6:1) **lleva contorno oscuro**, y lo que se mide es el contorno contra el fondo.
3. **Igualdad entre planos:** sin saltos de luminosidad de más de ≈ 15 % entre segundos, salvo que el salto sea el
   giro del video y esté escrito en la dirección.
4. **Fondo:** el color dominante no está más saturado que el personaje (cap. 03: el fondo no compite).
5. **Salida:** sRGB / Rec. 709, sin blancos ni negros quemados (`postpro.py info`).

## 6. Qué queda escrito en cada video

En `02_prompt/direccion.md`, sección **«Color con intención»** (la escribe el director de fotografía y la valida el
director creativo):

- **Neutros (2):** hex y para qué (fondo, texto/líneas).
- **Acento (1):** hex, dónde va (título + un elemento) y dónde no va.
- **Por qué esta paleta:** la emoción que busca, para este público.
- **Cómo ayuda al objetivo:** objetivo comercial del brief → qué hace el color → con qué métrica se va a ver.
- **Riesgos de lectura:** público mayor, daltonismo, pantalla chica.
- **Medido:** salida de `revisar_color.py` (paleta, contraste, saltos), firmado por el supervisor.

Y en `ficha.json` de la entrega, el campo `color` con lo mismo en corto (`entrega.py` lo exige):

```json
"color": {"neutros": ["#F3E9D2", "#2B2420"], "acento": "#E8B33B",
          "por_que": "…", "objetivo": "…", "medido": "…"}
```

## 7. Ejemplo: Tin & Tan (escrito después del primer Short)

- **Neutros:** papel `#F3E9D2` (fondo) y tinta `#2B2420` (líneas y texto), contraste 12,6:1.
- **Acento:** mostaza `#E8B33B`, solo en la palabra clave y en el lápiz; con contorno de tinta, porque sola sobre papel
  da 1,6:1.
- **Por qué:** papel crema y tinta marrón remiten a impresos y fotos de los 70 y 80. Son cálidos y de saturación
  baja (≈ 17 % medido), para la nostalgia de un público de 45 o más, y se leen bien con su vista.
- **Objetivo (retención y recordación):** el acento mostaza lleva el ojo a la cifra en el primer segundo, y la
  paleta fija hace que el canal se reconozca entre Shorts.
- **Medido en TIN-EN-S-001:** ≈ 94 % dentro de la paleta, saltos de luminosidad de ±3 %; pasa.
