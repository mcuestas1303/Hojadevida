# Color de Tin & Tan por estadísticas y psicología — formato de acción

- **Fecha:** 2026-11-26
- **Pedido del dueño (textual):** «Replantear los colores con base a estadísticas y análisis psicológico».
- **Qué es este documento:** un estudio con tres paletas alternativas medidas. **No cambia nada:** `PARAMETROS.md`,
  `DESIGN.md`, `palitos.py` y las fichas siguen como estaban. Aplicar cualquiera pasa por `video-studio/cambios/`.
- **Muestras para ver:** `video-studio/estudios/2026-11-26_color_muestras.png` (la paleta actual y las tres
  alternativas, con sus hex y una mini escena en visión normal y en deuteranopía simulada).
- **Objetivo al que sirve:** entrar al Programa de socios de YouTube: que se queden a mirar, lleguen al final y se
  suscriban. Cada color se justifica por lo que comunica, la emoción que provoca y la métrica de Studio que lo
  comprobaría.

## 0. Cómo leer este documento

Los tres sellos son los de `manual/14_efectos_y_emocion.md`:

- **[investigación]**: hallazgo de psicología de la percepción o del color, con autores y año.
- **[oficio]**: práctica aceptada de la profesión o norma técnica.
- **[hipótesis del equipo]**: no se encontró respaldo; se dice y se indica con qué métrica se comprobará.

Cuatro advertencias que valen para todo:

1. **«Abierta» quiere decir que la página se descargó y se leyó el 2026-11-26. «(resumen)» quiere decir que solo se
   vio el resumen de un buscador.** La red de esta sesión no dejó abrir ningún artículo primario (lista en la
   sección 9). Casi todo lo abierto es Wikipedia en inglés y la ayuda oficial de YouTube. **De ningún estudio se leyó
   el texto completo.**
2. **Ningún estudio encontrado se hizo con Shorts verticales.** La investigación respalda el mecanismo (por ejemplo,
   que un color saturado y luminoso activa más); que ese mecanismo mejore una métrica de YouTube es siempre
   **[hipótesis del equipo]** hasta medirlo.
3. **Dos resultados encontrados dicen que el color solo puede no mover nada** (H8 y H9 de la tabla). Están en la
   tabla a propósito: el color es condición para que se lea la acción, no una palanca probada de retención.
4. Las cifras medidas (contraste, ΔE) son aproximadas, con un decimal. La simulación de daltonismo es aproximada
   (sección 3.1). Sin cifras de «sube la retención un X %»: no se abrió ninguna fuente que las dé.

## 1. Qué se sabe del público y qué implica para el color

Fuente: lectura de YouTube Studio del 2026-11-26, en `video-studio/estadisticas/datos/2026-11-26_studio_tin_y_tan.md`
(no se sube; aquí va en palabras). Son dos videos con datos: señal, no prueba.

| Lo que mide Studio (en palabras) | Qué implica para el color |
|---|---|
| Casi todo el público tiene menos de 45 años; no hay registro de 55 o más | Ya no hace falta diseñar para la vista de 45 a 70 (cristalino amarillento, 7:1). Vale el mínimo general: 4,5:1 en texto y 3:1 en figuras |
| Uno de los tramos mayores es el de 13 a 17; en el short de videojuegos es el mayor | Es justo el público que una restricción por edad deja fuera. El color no puede acercar el dibujo a «dibujo infantil con violencia» ni a sangre |
| Mayoría hombres | El daltonismo rojo–verde afecta a ≈ 8 % de los hombres de origen europeo (H16): con este público no es un caso raro. Los personajes, el rival, el fuego y el dato tienen que separarse también por claro y oscuro |
| Casi la mitad de las horas se ve en televisor y tableta, y en televisor se ve en compañía | Pantalla grande y a distancia: la figura tiene que leerse por masa de color y contorno, no por detalle fino. El resto sigue siendo celular |
| EE. UU. primero; luego Filipinas e India | Las preferencias medidas que se encontraron son de EE. UU., Reino Unido e India (H1, H4). **De Filipinas no se encontró ningún estudio útil** (sección 8) |
| Casi todo el tráfico llega del feed de Shorts; todo el público es nuevo; ninguna suscripción | El primer fotograma decide si se queda o desliza. Y como nadie conoce todavía el canal, **cambiar la identidad hoy cuesta menos que nunca**: no hay espectadores que regresen a quienes confundir |
| La mayor caída de retención está entre los segundos 5 y 10 | El color tiene que ayudar a que el golpe y el dato fuerte se entiendan antes del segundo 5: un solo punto de máxima saturación por plano |

## 2. Hallazgos

| # | Hallazgo | Fuente | Sello | Qué implica |
|---|---|---|---|---|
| H1 | El azul fue el color favorito en los 10 países de una encuesta de 2015 (entre ellos EE. UU. e Indonesia; no Filipinas ni India). En EE. UU. y Reino Unido lo eligen más los hombres que las mujeres, y sigue siendo el primero entre ellas | YouGov, 2015 (resumen): https://yougov.com/en-us/articles/12335-why-blue-worlds-favorite-color | [investigación], encuesta comercial | El azul es la apuesta de menor riesgo para lo que deba gustar (acento, o un personaje). Es preferencia declarada, no retención |
| H2 | En EE. UU., marrón y naranja aparecen como los colores que menos gustan | YouGov (resumen; solo se vio el titular): https://yougov.com/en-us/articles/10735-americas-favorite-color | [investigación], encuesta comercial, sin leer | Hoy el cuadro es crema, marrón, naranja y mostaza. No basta para tocar a Tin (su naranja es identidad y funciona por contraste), sí para no llenar el mundo de marrones |
| H3 | La preferencia por un color sigue lo que se siente por los objetos de ese color: gustan los azules (cielo, agua limpia) y disgustan los marrones (comida podrida). 48 adultos de California | Palmer y Schloss, 2010, *PNAS* 107 (resumen): https://pubmed.ncbi.nlm.nih.gov/20421475/ · Wikipedia, «Color psychology» (abierta) | [investigación] | El color se lee por lo que recuerda. El humo marrón se lee como humo o polvo (apropiado); un mundo marrón, como algo sucio o viejo |
| H4 | Hombres y mujeres prefieren en conjunto los tonos fríos (azul verdoso) a los cálidos; las mujeres suman una preferencia por rosa y morado. El patrón de los hombres es muy parecido entre británicos e indios (80 estudiantes británicos y 81 jóvenes indios) | Bonnardel y otros, 2018, *Color Research & Application* (resumen): https://zendy.io/title/10.1002/col.22188 · Hurlbert y Ling, 2007 (resumen) | [investigación] | El verde azulado de Tan ya está en la zona que gusta a los dos sexos y en India. No hay base para quitárselo por preferencia |
| H5 | Hay diferencias de preferencia por edad y sexo (niños de 8 a 12, jóvenes de 18 a 24, mayores de 61 a 88, Reino Unido). Los niños pequeños prefieren el amarillo, al contrario que los adultos | Ling y Hurlbert, 2011 (resumen; no se leyeron los resultados por edad): https://benjamins.com/catalog/z.167.40lin · Wikipedia, «Color psychology», citando a Aslam, 2006 (abierta) | [investigación], incompleta | **No encontré datos del tramo de 13 a 17.** No se puede afirmar qué color prefiere un adolescente frente a un adulto |
| H6 | Con el color a pantalla completa: más saturación y más luminosidad dan más activación; por tono, la activación sube del azul y el verde hacia el rojo. La valoración más alta es para los colores saturados y luminosos. 62 personas, 30 s por color, con medida de la piel y del pulso | Wilms y Oberfeld, 2018, *Psychological Research* 82 (resumen): https://link.springer.com/article/10.1007/s00426-017-0880-8 | [investigación] | Es el hallazgo central. La emoción que pide `PARAMETROS.md` es asombro o sorpresa, de alta activación: los golpes, el fuego y el dato van saturados, luminosos y cálidos. Un cuadro entero oscuro o apagado trabaja en contra |
| H7 | Sobre cualquier fondo, los colores de máxima saturación y luminosidad son los que más atraen la atención. 123 estudiantes, Turquía | Camgöz, Yener y Güvenç, 2004, *Color Research & Application* 29 (resumen): https://repository.bilkent.edu.tr/items/f71941a7-d7b2-4d57-ab51-92503ae069ea | [investigación] | El punto que hay que mirar (golpe, dato) es el más saturado y luminoso del plano; el mundo, no |
| H8 | **Resultado nulo.** En 21 adolescentes jugando en el celular, cambiar tono y saturación no cambió de forma significativa su estado emocional; los autores apuntan al tamaño de la pantalla | arXiv 2402.19064, 2024 (resumen): https://arxiv.org/abs/2402.19064 | [investigación], muestra pequeña | En un celular y con adolescentes, el color solo puede no mover la emoción. No se promete nada a cuenta del color |
| H9 | **Resultado nulo.** En miniaturas de video largo, luminosidad, saturación, contraste y proporción de cálidos fueron casi iguales entre los videos que rompieron la media de su canal y los que no | Eden, análisis de miniaturas (resumen; blog comercial, sin revisión): https://eden.so/blog/what-makes-a-good-youtube-thumbnail/ | [oficio], dato comercial | No hay prueba de que «más saturado» traiga más vistas. Miniaturas de video largo, no el primer fotograma de un Short |
| H10 | Un objeto que difiere de los que lo rodean en un solo rasgo, como el color, «salta» sin esfuerzo; los modelos de saliencia calculan el contraste de color por canales opuestos (rojo–verde, azul–amarillo) | Wikipedia, «Visual search», citando a Treisman y Gelade, 1980, y Wolfe, 1994 (abierta) · Itti, Koch y Niebur, 1998 (resumen) | [investigación] | Lo que salta es la diferencia con el entorno. Hoy ≈ 92 % del cuadro es cálido: Tin (naranja) y el fuego están en la misma familia que el fondo. Un fondo frío les da contraste azul–amarillo |
| H11 | El rojo se asocia con dominancia, agresividad y peligro: en deportes de combate, quien viste de rojo gana algo más y los árbitros lo puntúan más alto; las palabras de peligro se clasifican más rápido en rojo; en cinco países, entre ellos EE. UU., el rojo se liga al enfado | Wikipedia, «Color psychology» (abierta) · Hill y Barton, 2005, *Nature* 435 (resumen) · Pravossoudovitch y otros, 2014 (resumen) | [investigación], con réplicas discutidas | El rojo es el color de la amenaza y del golpe. Sirve para el borde del fuego y el impacto. En un personaje se acerca a «sangre» y la ficha del rival lo prohíbe |
| H12 | En la naturaleza, las señales de advertencia más comunes y eficaces son rojo, amarillo, negro y blanco, en patrones de alto contraste | Wikipedia, «Aposematism», citando a Stevens y Ruxton, 2012 (abierta) | [investigación] | Fuego amarillo y rojo junto a tinta negra es una señal de peligro que no depende de la cultura |
| H13 | Las asociaciones entre color y emoción se parecen mucho entre 30 países (similitud media r = 0,88), con diferencias locales | Jonauskaite y otros, 2020, *Psychological Science* 31 (resumen; no pude comprobar si Filipinas e India están en la muestra) | [investigación] | Una misma paleta emocional puede servir para EE. UU., Filipinas e India; no hay base para hacer versiones por país |
| H14 | Naranja y verde azulado son complementarios y se usan juntos en el cine de Hollywood desde ≈ 2010 | Wikipedia, «Color grading», citando a *The Guardian*, 2010 (abierta) | [oficio] | La pareja Tin–Tan ya es la pareja de color del cine comercial. Otro motivo para no tocarla |
| H15 | En el género: la serie de palitos más conocida distingue a cada luchador por un color plano (naranja, rojo, amarillo, verde lima, cian; un antagonista negro y otro rojo vivo). El clásico chino usa un muñeco negro sobre fondos mínimos. Los títulos con más vistas del listado nombran la pelea por colores («Orange vs Red», «Black vs Red», «Fire vs Ice») | Wikipedia, «Animator vs. Animation» y «Xiao Xiao» (abiertas) · listados de `estudios/2026-11-26_accion_stickman_y_tin_y_tan.md`, sección 2 (**ningún video visto**) | [oficio], solo lo verificable | Un color plano por luchador y un rival negro son la convención del género. **No pude verificar los fondos ni las paletas de los canales grandes** |
| H16 | Daltonismo rojo–verde: ≈ 8 % de los hombres y ≈ 0,5 % de las mujeres de origen norte-europeo (deutanes ≈ 6 %, protanes ≈ 2 % de los hombres). Confunden rojo, verde, naranja y marrón; los protanes ven el rojo mucho más oscuro | Wikipedia, «Color blindness» (abierta) | [investigación] | El naranja de Tin y un fuego naranja son el mismo color para ellos. Fuego y Tin se separan por luminosidad y por contorno. No sé la prevalencia en Filipinas e India |
| H17 | Texto: contraste mínimo 4,5:1 (3:1 en texto grande). Gráficos necesarios para entender: 3:1. No más de 3 destellos por segundo; hay un umbral aparte para destellos hacia rojo saturado. El contraste solo de color, sin cambio de luminosidad, rara vez dispara una crisis | WCAG 2.2 (resumen; w3.org no abrió): https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html · Wikipedia, «Photosensitive epilepsy» (abierta) | [oficio], norma | La palabra de dato tiene que dar 4,5:1 sin ayuda o llevar contorno. El borde rojo del fuego no parpadea; una explosión es un cambio de luminosidad y cuenta como destello |
| H18 | Para decidir si un video es «hecho para niños», YouTube mira, entre otros factores, si incluye «personajes… que atraen a los niños, incluidos personajes animados o figuras de dibujos». También dice que la animación «que atrae a todos» es contenido general. **La página no menciona el color.** El esquema del bebé (cara redonda, mejillas) es lo que hace que algo se vea tierno; tampoco menciona el color | Ayuda de YouTube (abierta): https://support.google.com/youtube/answer/9528076?hl=en · Wikipedia, «Cuteness» (abierta) · políticas ya citadas en `estudios/2026-11-26_accion_stickman_y_tin_y_tan.md`, 1.b y 1.d | [oficio] para la política; **[hipótesis del equipo]** para el color | Que un cuadro claro, cálido y poco saturado (hoy ≈ 21 % de saturación y ≈ 84 % de luminosidad) empuje a leerlo como infantil es una hipótesis razonable, no un dato. Lo que sí pesa son las formas redondas y las mejillas, que no se tocan aquí |
| H19 | Un color muy saturado se ve más luminoso de lo que mide; el efecto es mayor en ambientes oscuros | Wikipedia, «Helmholtz–Kohlrausch effect» (abierta) | [investigación] | Argumento a favor de un mundo oscuro con efectos saturados en televisor. No se midió con video |
| H20 | Sobre fondo negro, el rojo suele verse delante del azul; sobre fondo blanco el efecto puede invertirse | Wikipedia, «Chromostereopsis», citando a Verhoeff, 1928 (abierta) | [investigación] | No se puede contar con que «lo cálido avanza» sobre un mundo claro. La profundidad se apoya en la perspectiva aérea: lo lejano, más azulado y con menos contraste (`manual/14`, R7) |
| H21 | Para simular daltonismo se usa el modelo de Machado, Oliveira y Fernandes (2009). La pareja naranja–azul es la base de la paleta de Okabe e Ito, pensada para que la distingan todos | Machado y otros, 2009, *IEEE TVCG* 15 (resumen): https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html · Okabe e Ito (resumen) | [oficio] | Método de la sección 3.1. Naranja contra azul es la pareja más segura; naranja contra verde azulado también pasa |

## 3. Diagnóstico de la paleta actual

### 3.1 Cómo se midió

- **Contraste:** fórmula de WCAG 2.x, la misma de `herramientas/revisar_color.py --contraste`.
- **Diferencia de color:** ΔE76 en Lab (D65), la misma de `revisar_color.py`. Umbral de `DESIGN.md`: ΔE ≥ 25 para que
  dos colores no se confundan.
- **Daltonismo:** se transformó cada color con las matrices de Machado y otros (2009) para deuteranopía y protanopía
  totales, en RGB lineal, y se volvió a medir ΔE. **Es una aproximación:** las matrices se copiaron de la tabla
  publicada sin poder abrir la página de los autores en esta sesión, valen para un monitor sRGB típico y simulan el
  caso extremo (la mayoría de los daltónicos tiene una forma más leve). Umbral usado: ΔE ≥ 20 en la simulación
  **[hipótesis del equipo]**.
- **Cuadro real:** `revisar_color.py` sobre `pruebas/2026-11-26_accion_mundo_3d/salida/contacto.png`.
- Los colores de fuego y humo «actuales» son los que usa la escena de la prueba (mostaza, naranja y marrón de la
  paleta). El guion de medición quedó en el borrador de la sesión, no en el repositorio.

### 3.2 Lo medido

Hoja de contacto de la prueba: ≈ 92 % del cuadro cálido y ≈ 1 % frío; saturación media ≈ 21 %; luminosidad media
≈ 84 %; ≈ 80 % dentro de la paleta declarada (aviso de `revisar_color.py`: por debajo del 85 %).

| Elemento | Hex | S / V | ≈ con fondo | ≈ con suelo | ≈ con tinta | Deuteranopía | Protanopía |
|---|---|---|---|---|---|---|---|
| Fondo (papel) | `#F3E9D2` | 14 % / 95 % | — | 1,2:1 | 12,6:1 | `#F1EBD3` | `#EFE8D1` |
| Suelo (papel sombra) | `#E6D8B8` | 20 % / 90 % | 1,2:1 | — | 10,8:1 | `#E4DBB9` | `#E0D7B6` |
| Tinta / línea | `#2B2420` | 26 % / 17 % | 12,6:1 | 10,8:1 | — | `#282620` | `#262520` |
| Tin | `#E07A2E` | 79 % / 88 % | 2,5:1 | 2,1:1 | 5,1:1 | `#B09E2D` | `#988723` |
| Tan | `#2F7F7A` | 63 % / 50 % | 3,9:1 | 3,4:1 | 3,2:1 | `#6C6F7B` | `#78787A` |
| Rival | `#2B2420` | 26 % / 17 % | 12,6:1 | 10,8:1 | — | `#282620` | `#262520` |
| Fuego, núcleo (mostaza) | `#E8B33B` | 75 % / 91 % | 1,6:1 | 1,4:1 | 8,0:1 | `#D6C141` | `#CAB328` |
| Fuego, borde (naranja) | `#E07A2E` | 79 % / 88 % | 2,5:1 | 2,1:1 | 5,1:1 | `#B09E2D` | `#988723` |
| Acento de dato (mostaza) | `#E8B33B` | 75 % / 91 % | 1,6:1 | 1,4:1 | 8,0:1 | `#D6C141` | `#CAB328` |
| Humo (marrón) | `#7A4B2A` | 66 % / 48 % | 6,1:1 | 5,2:1 | 2,1:1 | `#645A2A` | `#595027` |
| Sombra | `#B9A98E` | 23 % / 73 % | 1,9:1 | 1,6:1 | 6,6:1 | `#B4AD8F` | `#B0A98C` |

### 3.3 Qué funciona

1. **Tin contra Tan:** ΔE ≈ 86 en visión normal, ≈ 67 en deuteranopía y ≈ 54 en protanopía. Se distinguen siempre. Es
   además la pareja complementaria del cine comercial (H14) y el verde azulado está en la zona que gusta a los dos
   sexos y en India (H4).
2. **Papel y tinta:** ≈ 12,6:1. Las líneas se leen en cualquier pantalla.
3. **El rival de tinta:** se separa de Tin (ΔE ≈ 77) y de Tan (≈ 44) por luminosidad, que es lo único que el
   daltonismo no toca, y coincide con la convención del género: un antagonista negro (H15).
4. **El mundo menos saturado que los personajes** (14 a 20 % contra 63 a 79 %): cumple la regla de `manual/13`.
5. **El humo marrón:** es el tono que mejor se separa de Tan y de Tin con daltonismo (sección 4, nota del humo).

### 3.4 Qué no funciona

| # | Problema | Medida | Por qué importa |
|---|---|---|---|
| D1 | **El fuego tiene el color de Tin.** El borde del fuego es su mismo naranja | ΔE = 0 | Cuando Tin está junto a una llama, su cabeza se funde con ella. Se ve en la hoja de contacto, fila 3 |
| D2 | **El acento de dato es el color del fuego, de la estrella de impacto, de la bufanda de Tan y del lápiz** | ΔE = 0 con el núcleo del fuego | El dato deja de ser «lo único de ese color». El acento ya no señala nada (H10) |
| D3 | **Con daltonismo, mostaza y naranja casi se igualan** | ΔE ≈ 14 en deuteranopía | Para ≈ 6 % de los hombres, dato, fuego y Tin son un mismo color |
| D4 | **La mostaza sobre papel no se lee sola** | ≈ 1,6:1 | Necesita contorno de tinta siempre; en letra chica el contorno se come la letra (ya pasó con las cifras, `DESIGN.md`) |
| D5 | **Todo el cuadro es de una familia cálida** | ≈ 92 % cálido, ≈ 1 % frío | No hay contraste de tono entre figura y fondo: Tin es naranja sobre crema. Solo separa la saturación (H10) |
| D6 | **Cuadro claro y poco saturado** | saturación ≈ 21 %, luminosidad ≈ 84 % | Poca activación para un formato que busca asombro (H6); y es el aspecto «pastel» que el pedido señala como riesgo (H18, hipótesis) |
| D7 | **Mundo y humo en marrones** | cajones, grietas y humo en marrón y tinta | Es la familia que menos gusta en EE. UU. (H2, H3); además las grietas de tinta y el rival de tinta se confunden cuando el rival está en el suelo |
| D8 | **Cabezas con poco contraste contra el mundo** | Tin ≈ 2,5:1 y ≈ 2,1:1; Tan ≈ 3,9:1 y ≈ 3,4:1 | Tin no llega a 3:1 (H17). Hoy lo salva el contorno de tinta; en un televisor a distancia el contorno fino pesa menos |

## 4. Las tres alternativas

Todas cumplen lo que no se mueve: sin sangre roja, sin destellos hacia rojo saturado, sin blanco puro a pantalla
completa, sin colores tomados de una marca (ninguno se eligió por parecerse a una marca; el control por tema sigue
siendo por video: si el video trata de una marca cuyo color coincide con el acento, se cambia el acento).

Reglas comunes a las tres **[hipótesis del equipo]**, salvo donde se cita:

- **El fuego se pinta en dos tonos con escalón duro** (núcleo amarillo claro, borde rojo oscuro), sin degradado que
  pase por el naranja, porque ese tramo intermedio es el color de Tin (D1). El borde lleva la silueta y el núcleo la luz.
- **El rojo del fuego no parpadea** y nunca cubre más de un cuarto del cuadro en dos fotogramas seguidos; todo video
  sigue pasando `efectos.comprobar_destellos` (H17).
- **El dato y el pico de una explosión no comparten plano:** un solo punto de máxima saturación a la vez (H7, H10;
  `manual/14`, paso 3).
- **Nota del humo (medida):** se probaron grises fríos y neutros, y con daltonismo todos se confunden con el verde
  azulado de Tan (ΔE ≈ 7 a 19), porque para un daltónico ese verde azulado es un gris. El humo pardo oscuro es el que
  se separa de Tan, de Tin y del rival a la vez. Por eso A y B conservan un humo pardo aunque el marrón no guste
  (H2): aquí el marrón se lee como humo (H3). Su único aviso es contra el borde rojo del fuego en protanopía, que se
  acepta porque el fuego se vuelve humo.

Diferencias de color entre los pares que no deben confundirse (≈ ΔE en visión normal / deuteranopía / protanopía;
**negrita** = no pasa):

| Par | Actual | A | B | C |
|---|---|---|---|---|
| Tin – Tan | 86 / 67 / 54 | 86 / 67 / 54 | 86 / 67 / 54 | 132 / 135 / 119 |
| Tin – rival | 77 / 73 / 65 | 77 / 73 / 65 | 102 / 104 / 100 | 97 / 90 / 77 |
| Tan – rival | 44 / 34 / 36 | 44 / 34 / 36 | 73 / 45 / 49 | 70 / 71 / 67 |
| Tin – fuego, borde | **0 / 0 / 0** | 36 / 23 / 33 | 36 / 23 / 33 | 31 / 27 / 35 |
| Tin – fuego, núcleo | **31 / 14 / 23** | 51 / 28 / 38 | 51 / 28 / 38 | 72 / 48 / 49 |
| Rival – humo | 35 / 34 / 29 | 29 / 28 / 24 | 79 / 78 / 76 | 35 / 35 / 35 |
| Tin – humo | 42 / 39 / 35 | 49 / 46 / 40 | 36 / 32 / 28 | 87 / 76 / 65 |
| Tan – humo | 54 / 37 / 31 | 52 / 36 / 33 | 52 / 37 / 27 | 61 / 61 / 55 |
| Acento – Tin | **31 / 14 / 23** | 129 / 133 / 120 | 106 / 89 / 78 | 57 / 26 / 39 |
| Acento – Tan | 82 / 78 / 72 | 90 / 68 / 67 | 41 / 41 / 41 | 154 / 154 / 149 |
| Acento – rival | 87 / 87 / 87 | 83 / 80 / 75 | 66 / 20 / 32 | 116 / 115 / 115 |
| Acento – fuego, núcleo | **0 / 0 / 0** | 154 / 149 / 146 | 96 / 96 / 91 | 54 / 51 / 54 |
| Fuego, borde – humo | 42 / 39 / 35 | 52 / 26 / **9** | 50 / 21 / **18** | 80 / 57 / 42 |

### Alternativa A · «Papel con fondo frío»

**Identidad: conserva sin tocar el naranja de Tin, el verde azulado de Tan, la tinta y el rival de solo tinta.** No
cambia la foto de perfil ni el banner. Cambia el fondo lejano, el fuego, el humo y el acento de dato.

| Elemento | Hex | S / V | ≈ con fondo | ≈ con suelo | ≈ con tinta | Deuteranopía | Protanopía |
|---|---|---|---|---|---|---|---|
| Fondo (mundo lejano) | `#C9D6DE` | 9 % / 87 % | — | 1,2:1 | 10,3:1 | `#CFD3DE` | `#D2D5DE` |
| Suelo y primer término (papel) | `#F3E9D2` | 14 % / 95 % | 1,2:1 | — | 12,6:1 | `#F1EBD3` | `#EFE8D1` |
| Tinta / línea | `#2B2420` | 26 % / 17 % | 10,3:1 | 12,6:1 | — | `#282620` | `#262520` |
| Tin | `#E07A2E` | 79 % / 88 % | 2,0:1 | 2,5:1 | 5,1:1 | `#B09E2D` | `#988723` |
| Tan | `#2F7F7A` | 63 % / 50 % | 3,2:1 | 3,9:1 | 3,2:1 | `#6C6F7B` | `#78787A` |
| Rival (solo tinta) | `#2B2420` | 26 % / 17 % | 10,3:1 | 12,6:1 | — | `#282620` | `#262520` |
| Fuego, núcleo | `#FFE45C` | 64 % / 100 % | 1,2:1 | 1,1:1 | 12,0:1 | `#FFE863` | `#F9DF4C` |
| Fuego, borde | `#B81414` | 89 % / 72 % | 4,5:1 | 5,5:1 | 2,3:1 | `#766805` | `#4F4610` |
| Acento de dato | `#1B45C4` | 86 % / 77 % | 5,3:1 | 6,5:1 | 2,0:1 | `#004AC2` | `#005AC8` |
| Humo | `#664022` | 67 % / 40 % | 6,1:1 | 7,5:1 | 1,7:1 | `#544C22` | `#4B441F` |
| Sombra | `#A9A190` | 15 % / 66 % | 1,7:1 | 2,1:1 | 6,0:1 | `#A7A390` | `#A5A08F` |

| Color | Qué comunica y qué emoción busca | Respaldo | Métrica de Studio |
|---|---|---|---|
| Fondo frío poco saturado | «Esto está lejos»; deja a Tin, al fuego y a los golpes como lo único cálido del cuadro. Emoción: ninguna propia; es el escenario | Perspectiva aérea (`manual/14`, R7) [investigación]; contraste de tono figura–fondo (H10) [investigación]. Que mejore una métrica: [hipótesis del equipo] | «Se quedó a mirar» frente a «deslizó», comparado con los shorts 1 y 2 |
| Suelo de papel y tinta | «Es Tin & Tan»: lo único que se repite del canal | Reconocimiento por repetición (`manual/14`, R26) [investigación] | Espectadores que regresan, cuando los haya |
| Tin y Tan, sin cambio | Los protagonistas; pareja complementaria que se distingue con daltonismo | H4, H14 y medición de la sección 3.3 | Comentarios que los nombran; suscriptores por mil vistas |
| Rival de tinta | Amenaza por forma y por negro, no por color; sigue siendo «la pregunta» de la ficha | Antagonista negro del género (H15) [oficio]; negro como señal de advertencia (H12) [investigación] | Retención en el segundo en que aparece |
| Fuego amarillo claro y rojo oscuro | Peligro y golpe; alta activación en el pico | Rojo y amarillo como señal de peligro (H11, H12); saturación y calidez suben la activación (H6) [investigación] | Retención en el segundo de la explosión; compartidos por mil vistas |
| Acento azul saturado | «Este es el dato»: el único azul intenso del video, en la palabra clave y en un elemento. Emoción: alivio y certeza tras el golpe, el momento de menor activación del plano | Azul, el color que más gusta, sobre todo a hombres (H1); menor activación que los cálidos (H6); se lee solo, ≈ 5,3:1 y ≈ 6,5:1, sin contorno (H17); no cambia con daltonismo. Que señale «certeza»: [hipótesis del equipo] | Retención entre el golpe y el dato (segundos 3 a 8); porcentaje medio visto |
| Humo pardo oscuro | Daño que queda; no tapa a los personajes | Nota del humo (medida) | Ninguna propia: es condición de lectura |

- **Qué arregla del diagnóstico:** D1, D2, D3, D4 y D5 por completo; D7 en parte (el mundo deja de ser marrón, el humo
  no). D6 solo en los efectos: el cuadro sigue siendo claro. D8 no mejora (Tin baja a ≈ 2,0:1 contra el fondo frío):
  sigue dependiendo del contorno de tinta.
- **Riesgos:**
  - Rompe la letra de la regla «2 neutros + 1 acento» (`manual/13`): hay un tercer neutro (el fondo frío) y el fuego
    suma dos colores de efecto. La prueba actual ya la rompía con el fuego. Hay que decidir si los colores de efecto
    cuentan como acento; lo firma el director de fotografía.
  - El acento azul queda en la familia fría de Tan (ΔE ≈ 90, no se confunden), pero puede leerse como «color de Tan»
    cuando el dato lo dice Tin. [hipótesis del equipo]; se mira en comentarios.
  - El cuadro sigue siendo claro y de dibujo redondo: no reduce por sí solo el riesgo de «aspecto infantil» (H18).
  - Fuego contra humo en protanopía ≈ 9: aceptado (ver nota del humo).

### Alternativa B · «Noche de tinta»

**Identidad: conserva los hex de las cabezas de Tin y de Tan, pero cambia dos cosas que las fichas marcan como
fijas:** la línea del cuerpo y el contorno pasan de tinta a papel (`#F3E9D2`), y el rival deja de ser «solo tinta» y
pasa a tinta lila (su ficha prohíbe pintarlo «de cualquier color»). **Las dos cosas son decisión del dueño.** La foto
de perfil y el banner podrían quedarse en papel, pero entonces el canal y sus videos dejarían de parecerse.

| Elemento | Hex | S / V | ≈ con fondo | ≈ con suelo | ≈ con línea | Deuteranopía | Protanopía |
|---|---|---|---|---|---|---|---|
| Fondo (mundo lejano) | `#141B33` | 61 % / 20 % | — | 1,3:1 | 14,1:1 | `#0E1B32` | `#111E34` |
| Suelo | `#27304F` | 51 % / 31 % | 1,3:1 | — | 10,7:1 | `#21304E` | `#253350` |
| Línea y contorno (papel) | `#F3E9D2` | 14 % / 95 % | 14,1:1 | 10,7:1 | — | `#F1EBD3` | `#EFE8D1` |
| Tin | `#E07A2E` | 79 % / 88 % | 5,7:1 | 4,3:1 | 2,5:1 | `#B09E2D` | `#988723` |
| Tan | `#2F7F7A` | 63 % / 50 % | 3,6:1 | 2,7:1 | 3,9:1 | `#6C6F7B` | `#78787A` |
| Rival (tinta lila) | `#B79CFF` | 39 % / 100 % | 7,5:1 | 5,7:1 | 1,9:1 | `#84AAFC` | `#80ACFF` |
| Fuego, núcleo | `#FFE45C` | 64 % / 100 % | 13,4:1 | 10,2:1 | 1,1:1 | `#FFE863` | `#F9DF4C` |
| Fuego, borde | `#B81414` | 89 % / 72 % | 2,6:1 | 1,9:1 | 5,5:1 | `#766805` | `#4F4610` |
| Acento de dato | `#4FE3FF` | 69 % / 100 % | 11,2:1 | 8,5:1 | 1,3:1 | `#B5C9FF` | `#CEDCFF` |
| Humo | `#9A6A45` | 55 % / 60 % | 3,7:1 | 2,8:1 | 3,8:1 | `#847945` | `#786E42` |
| Sombra | `#0B0F1F` | 65 % / 12 % | 1,1:1 | 1,5:1 | 15,8:1 | `#070F1F` | `#091120` |

| Color | Qué comunica y qué emoción busca | Respaldo | Métrica de Studio |
|---|---|---|---|
| Mundo azul noche | Tensión y peligro; quita de golpe el aspecto claro y pastel | Luminosidad baja da tensión (`manual/13`, sección 4) [oficio]; lo saturado se ve más luminoso en ambiente oscuro (H19) [investigación]. **En contra:** más luminosidad da más activación (H6), y un cuadro oscuro baja la luminosidad media | «Se quedó a mirar»; reparto por dispositivo (¿sube el televisor?) |
| Línea de papel | Los personajes pasan a ser trazo claro sobre noche: máxima lectura de la silueta (≈ 14:1) | H17 [oficio] | Porcentaje medio visto |
| Tin y Tan (mismos hex) | Los mismos protagonistas. Tin gana contraste (≈ 5,7:1); Tan queda justo (≈ 3,6:1 y ≈ 2,7:1 contra el suelo): depende del contorno de papel | Medición | Comentarios que los nombran |
| Rival lila claro | En un mundo oscuro la tinta negra no se ve: el rival necesita luz propia. El lila fue el tono que se separó de todos (de Tin ≈ 102, de Tan ≈ 73, del humo ≈ 79, de la línea ≈ 70) | **Elegido por medición de distinguibilidad, no por emoción: no encontré respaldo para una emoción del lila.** [hipótesis del equipo] | Retención cuando aparece |
| Fuego amarillo y rojo | Lo mismo que en A, con más fuerza: el núcleo da ≈ 13:1 contra la noche | H6, H11, H12, H19 | Retención en la explosión |
| Acento cian luminoso | «Este es el dato»: el punto más luminoso y frío del plano | Azul como familia preferida (H1, H4); máxima saturación y luminosidad atraen la atención (H7) | Retención entre golpe y dato |
| Humo pardo claro | Humo iluminado por el fuego | Nota del humo | — |

- **Qué arregla del diagnóstico:** D1 a D8, todos. Es la única que ataca D6 y D8 de lleno.
- **Riesgos:**
  - **Fotosensibilidad: es la más delicada.** Un destello se define por cambio de luminosidad (H17): fuego a ≈ 13:1
    sobre fondo oscuro da saltos mucho mayores que sobre papel. Las explosiones tendrían que ser más lentas o más
    pequeñas, y `comprobar_destellos` pasa a ser el control crítico.
  - **Evidencia en contra (H6):** el cuadro oscuro puede activar menos que uno claro. No se sabe cuál efecto gana.
  - **Rompe «papel y tinta»,** lo único del canal que hoy se repite, y la premisa del rival («tinta sobre papel»).
  - El acento cian y el rival lila se acercan en deuteranopía (ΔE ≈ 20, en el límite): se separan por forma (letra
    contra personaje), no por color.
  - Tan contra el suelo ≈ 2,7:1: no pasa 3:1 sin contorno.
  - En un celular a pleno sol, una escena oscura se ve peor que una clara: **[hipótesis del equipo]**; el tramo de
    13 a 17 y la mitad de las horas son de celular.
  - Los subtítulos en español y la portada hay que rediseñarlos para fondo oscuro.

### Alternativa C · «Alto voltaje»

**Identidad: cambia los dos colores que las fichas marcan como «nunca cambian».** Tin pasa a un naranja más saturado
(`#F26A1B`; cambio pequeño, ΔE ≈ 16 respecto al actual) y **Tan pasa de verde azulado a azul** (`#1560D0`; cambio
grande, ΔE ≈ 76). También se enfrían el papel y la tinta. **Es decisión del dueño e implica rehacer foto de perfil,
banner, hojas de personaje y `palitos.py`.** El rival sigue siendo solo tinta.

| Elemento | Hex | S / V | ≈ con fondo | ≈ con suelo | ≈ con tinta | Deuteranopía | Protanopía |
|---|---|---|---|---|---|---|---|
| Fondo (mundo lejano) | `#DCE6EE` | 8 % / 93 % | — | 1,1:1 | 13,5:1 | `#E0E4EE` | `#E3E6EE` |
| Suelo | `#F4F1EA` | 4 % / 96 % | 1,1:1 | — | 15,2:1 | `#F4F2EA` | `#F3F1EA` |
| Tinta / línea | `#1B1B22` | 21 % / 13 % | 13,5:1 | 15,2:1 | — | `#191B22` | `#191C22` |
| Tin | `#F26A1B` | 89 % / 95 % | 2,4:1 | 2,7:1 | 5,6:1 | `#B29F13` | `#918004` |
| Tan | `#1560D0` | 90 % / 82 % | 4,6:1 | 5,1:1 | 2,9:1 | `#005DCE` | `#006ED4` |
| Rival (solo tinta) | `#1B1B22` | 21 % / 13 % | 13,5:1 | 15,2:1 | — | `#191B22` | `#191C22` |
| Fuego, núcleo | `#FFF4B8` | 28 % / 100 % | 1,1:1 | 1,0:1 | 15,4:1 | `#FFF5BA` | `#FFF0B4` |
| Fuego, borde | `#B81414` | 89 % / 72 % | 5,3:1 | 5,9:1 | 2,6:1 | `#766805` | `#4F4610` |
| Acento de dato (franja de resaltador; el texto va en tinta) | `#FFD21F` | 88 % / 100 % | 1,1:1 | 1,3:1 | 11,8:1 | `#F6DC30` | `#EBCF00` |
| Humo | `#666B76` | 14 % / 46 % | 4,2:1 | 4,7:1 | 3,2:1 | `#666A76` | `#686C77` |
| Sombra | `#A7B0BC` | 11 % / 74 % | 1,7:1 | 1,9:1 | 7,8:1 | `#AAAEBC` | `#ACB0BD` |

| Color | Qué comunica y qué emoción busca | Respaldo | Métrica de Studio |
|---|---|---|---|
| Mundo blanco frío | Limpio y actual; quita toda la familia crema y marrón | Marrones entre lo que menos gusta (H2, H3). Que un mundo frío y blanco se lea menos infantil: [hipótesis del equipo] | «Se quedó a mirar» |
| Tin naranja vivo | Energía; el personaje cálido y activo | Más saturación y luminosidad, más activación (H6); naranja como luchador del género (H15). **En contra:** el naranja aparece entre lo que menos gusta en EE. UU. (H2, sin leer) | Retención en sus golpes |
| Tan azul | El color que más gusta, sobre todo a hombres; máxima separación de Tin | H1, H4; naranja contra azul es la pareja más segura con daltonismo (H21): ΔE ≈ 132 / 135 / 119 | Suscriptores por mil vistas; reparto por sexo |
| Rival de tinta | Igual que en A. Se probaron tres colores y ninguno pasó: morado se confunde con el azul de Tan en deuteranopía (ΔE ≈ 3), magenta con el humo (≈ 10 a 14) y carmesí con el borde del fuego (≈ 21 a 23), además de acercarse a «sangre» | Medición; H11, H15 | Retención cuando aparece |
| Fuego casi blanco y rojo oscuro | Como en A; el núcleo se aclara para no igualarse a la franja del dato | H6, H11, H12 | Retención en la explosión |
| Dato en tinta sobre franja amarilla | «Esto está subrayado»: la franja es el punto más luminoso y saturado; el texto da ≈ 11,8:1. Remite al lápiz amarillo de Tin | Máxima saturación y luminosidad atraen la atención (H7); 4,5:1 de sobra (H17); el amarillo no cambia con daltonismo | Retención entre golpe y dato |
| Humo gris | Humo neutro; con Tan azul ya no hay confusión con los grises | Medición | — |

- **Qué arregla del diagnóstico:** D1 a D5 y D7 por completo; D8 en Tan (≈ 4,6:1), no en Tin (≈ 2,4:1); D6 solo en
  personajes y efectos.
- **Riesgos:**
  - **Es la más cara y la de menor respaldo por lo que cuesta.** La mejora medible sobre A es la separación con
    daltonismo, que A ya pasa, y el contraste de Tan. El resto es preferencia declarada (H1), no retención.
  - Quita el verde azulado, que la evidencia sí respalda (H4, H14).
  - La franja amarilla y la bufanda mostaza de Tan quedan cerca (ΔE ≈ 21): la bufanda es identidad, pero la franja
    ya no es «lo único amarillo».
  - Naranja, azul, amarillo y rojo saturados sobre blanco es la combinación de los colores primarios: **puede
    leerse más infantil, no menos** [hipótesis del equipo]. Es el riesgo contrario al que se quería evitar.
  - Rehacer perfil, banner y hojas: trabajo y, si se generan imágenes, créditos (sin cotizar aquí).

## 5. Cómo se comprobaría en Studio

| Qué se quiere saber | Métrica | Cómo |
|---|---|---|
| ¿El primer fotograma detiene el dedo? | «Se quedó a mirar» frente a «deslizó» | Promedio de 5 videos con la paleta nueva contra los shorts 1 y 2 |
| ¿Se entiende el golpe y el dato? | Retención por segundo en el golpe, en la explosión y en el dato | Curva de cada video, en los segundos anotados en el perfil emocional |
| ¿Llegan al final? | Porcentaje medio visto | Igual |
| ¿Se suscriben? | Suscriptores por mil vistas | Igual |
| ¿Cambia quién mira? | Edad, sexo y dispositivo | Si baja el tramo de 13 a 17 o sube el televisor tras el cambio, se anota |
| ¿YouTube lo trata como infantil o violento? | Columna «Avisos»; distribución en el feed | Cualquier aviso se informa al dueño ese día |

**Límite de esta medición:** el formato de acción ya es «el cambio grande» del próximo video (`PARAMETROS.md`,
sección 4). El color llega junto con la pelea, el mundo y el sonido, así que **no se podrá decir cuánto se debe al
color**. La comparación limpia sería el mismo video en dos paletas, y eso choca con el riesgo anotado de resubir un
Short casi igual. Lo honesto es tratar el color como arreglo de lectura y medir el formato entero.

## 6. Recomendación del equipo

**Alternativa A, como paleta de partida del formato de acción.** Por qué:

1. **Arregla lo que está medido y es seguro:** el fuego deja de ser del color de Tin (ΔE de 0 a ≈ 36), el dato deja
   de ser del color del fuego (de 0 a ≈ 154) y se lee solo (de ≈ 1,6:1 a ≈ 5,3:1), y el cuadro deja de ser de una
   sola familia. Son defectos que se ven en la hoja de contacto, no opiniones.
2. **Va con la evidencia más firme encontrada:** efectos saturados, luminosos y cálidos para la activación (H6, H7),
   rojo y amarillo para el peligro (H11, H12), azul para lo que debe gustar y leerse (H1), fondo frío para la
   profundidad y el contraste de tono (H10, R7).
3. **No toca lo que la evidencia respalda:** naranja y verde azulado se distinguen con daltonismo, son la pareja
   complementaria del cine y el verde azulado gusta a los dos sexos y en India (H4, H14). No encontré ningún dato que
   justifique cambiarlos.
4. **No le pide al dueño cambiar identidad, perfil ni banner,** y no cuesta créditos: es código.
5. **Deja abiertas las otras dos.** B queda como la prueba siguiente, en un solo video, si después de 5 videos con A
   «se quedó a mirar» no mejora: es la única que cambia la luminosidad del cuadro (D6) y la que más aleja del aspecto
   pastel, pero tiene evidencia en contra (H6), el mayor riesgo de destellos y dos decisiones de identidad. C no se
   recomienda ahora: es la más cara y lo que añade sobre A tiene poco respaldo; si algún día se cambia la identidad,
   hoy es el momento más barato (nadie conoce aún el canal), y eso conviene que el dueño lo sepa.

**Lo que necesita el sí del dueño para aplicar A** (por `video-studio/cambios/`): cambiar en `DESIGN.md` el acento de
partida (de mostaza a azul), añadir el fondo frío y los colores de fuego y humo, y resolver si los colores de efecto
cuentan dentro de «2 neutros + 1 acento». Las fichas de Tin, Tan y el rival no cambian.

## 7. Qué decide el dueño

| Decisión | Alternativa a la que afecta |
|---|---|
| Aceptar A como paleta de partida del formato de acción | A |
| Cambiar la línea de tinta a papel y darle color al rival (su ficha lo prohíbe) | B |
| Cambiar los colores de identidad de Tin y de Tan, con perfil y banner | C |
| Si el fuego y el humo cuentan como «acento» en la regla de 2 neutros + 1 acento | Todas |

## 8. Lo que no sé

1. **Qué pidió antes el dueño sobre los colores.** No está escrito en el repositorio (`PARAMETROS.md`, requisito A10).
   Este estudio responde al pedido de hoy; si el anterior decía otra cosa, hay que cruzarlos.
2. **Qué color prefieren los de 13 a 17.** No encontré ningún dato de ese tramo (H5).
3. **Nada de Filipinas.** Solo aparecieron tesis locales sobre ropa e interiores. Tampoco pude comprobar si Filipinas
   e India están entre los 30 países de H13. De India hay un solo estudio, con 81 jóvenes de una escuela de diseño.
4. **Los resultados completos de casi todos los estudios.** De H1 a H9, H11, H13, H17 y H21 solo vi resúmenes. No pude
   comprobar tamaños de efecto ni condiciones; en particular, no leí el orden de preferencia de Palmer y Schloss ni
   las diferencias por sexo de Wilms y Oberfeld.
5. **Qué paletas usan de verdad los canales grandes de peleas de palitos.** Nadie del equipo ha visto esos videos;
   solo hay títulos y dos artículos de Wikipedia (H15). El reel de referencia del dueño sigue sin verse plano por plano.
6. **Si el color influye en que YouTube lea un dibujo como infantil.** La política no menciona el color (H18); lo de
   «pastel y redondo» es hipótesis. Tampoco sé cómo decide el sistema automático.
7. **Si un mundo oscuro retiene más o menos que uno claro en Shorts,** en celular o en televisor. No abrí ningún
   estudio de lectura en claro sobre oscuro; la evidencia que tengo apunta en los dos sentidos (H6 contra H19).
8. **Si el color mueve alguna métrica** (H8, H9). No hay prueba; hay dos resultados nulos.
9. **La prevalencia de daltonismo en el público real** (H16 es de origen norte-europeo) y cómo se ven estos colores
   con daltonismo leve, que es lo más común: simulé solo el caso extremo y con matrices sin verificar contra la fuente.
10. **Cómo se ven las paletas en un televisor real.** Todo se midió en sRGB; un televisor en modo «vivo» satura más.
    Falta verlo en la pantalla del dueño.
11. **Las mejillas (rubor) y la forma redonda,** que según H18 pesan más que el color en el aspecto tierno, no se
    estudiaron aquí.

## 9. Fuentes

| Fuente | Enlace | Estado |
|---|---|---|
| Wikipedia, «Color psychology» | https://en.wikipedia.org/wiki/Color_psychology | Abierta (los primeros ≈ 100.000 caracteres) |
| Wikipedia, «Color preferences» | https://en.wikipedia.org/wiki/Color_preferences | Abierta; casi no trae datos por edad o sexo |
| Wikipedia, «Visual search» | https://en.wikipedia.org/wiki/Visual_search | Abierta |
| Wikipedia, «Color blindness» | https://en.wikipedia.org/wiki/Color_blindness | Abierta (primera mitad) |
| Wikipedia, «Photosensitive epilepsy» | https://en.wikipedia.org/wiki/Photosensitive_epilepsy | Abierta |
| Wikipedia, «Aposematism» | https://en.wikipedia.org/wiki/Aposematism | Abierta |
| Wikipedia, «Helmholtz–Kohlrausch effect» | https://en.wikipedia.org/wiki/Helmholtz%E2%80%93Kohlrausch_effect | Abierta |
| Wikipedia, «Chromostereopsis» | https://en.wikipedia.org/wiki/Chromostereopsis | Abierta |
| Wikipedia, «Color grading» | https://en.wikipedia.org/wiki/Color_grading | Abierta |
| Wikipedia, «Cuteness» | https://en.wikipedia.org/wiki/Cuteness | Abierta |
| Wikipedia, «Animator vs. Animation» y «Xiao Xiao» | https://en.wikipedia.org/wiki/Animator_vs._Animation · https://en.wikipedia.org/wiki/Xiao_Xiao | Abiertas |
| Wikipedia, «Elsagate» y «Light-on-dark color scheme» | https://en.wikipedia.org/wiki/Elsagate · https://en.wikipedia.org/wiki/Light-on-dark_color_scheme | Abiertas; no aportaron nada sobre color o lectura, no se citan |
| Ayuda de YouTube, «Determining if your content is "made for kids"» | https://support.google.com/youtube/answer/9528076?hl=en | Abierta |
| Wilms y Oberfeld, 2018 | https://link.springer.com/article/10.1007/s00426-017-0880-8 | (resumen); pubmed.ncbi.nlm.nih.gov y www.staff.uni-mainz.de no abrieron |
| Palmer y Schloss, 2010 | https://pubmed.ncbi.nlm.nih.gov/20421475/ | (resumen); pmc.ncbi.nlm.nih.gov y palmerlab.berkeley.edu no abrieron |
| Hurlbert y Ling, 2007; Ling y Hurlbert, 2011 | https://benjamins.com/catalog/z.167.40lin | (resumen) |
| Bonnardel y otros, 2018 | https://zendy.io/title/10.1002/col.22188 | (resumen) |
| Jonauskaite y otros, 2020 | https://www.psychologicalscience.org/journals/psychological-science/0956797620948810/ | (resumen); biopen.bi.no no abrió |
| Hill y Barton, 2005; Pravossoudovitch y otros, 2014; revisión de Elliot, 2015 | https://www.nature.com/articles/435293a · https://www.frontiersin.org/articles/10.3389/fpsyg.2015.00368/full | (resumen); www.frontiersin.org no abrió |
| YouGov, 2015 | https://yougov.com/en-us/articles/12335-why-blue-worlds-favorite-color · https://yougov.com/en-us/articles/10735-americas-favorite-color | (resumen); del segundo solo el titular |
| Camgöz, Yener y Güvenç, 2004 | https://repository.bilkent.edu.tr/items/f71941a7-d7b2-4d57-ab51-92503ae069ea | (resumen) |
| «The Influence of Color Stimuli on Adolescents' Emotion Playing Mobile Games», 2024 | https://arxiv.org/abs/2402.19064 | (resumen); arxiv.org no abrió |
| Eden, análisis de miniaturas | https://eden.so/blog/what-makes-a-good-youtube-thumbnail/ | (resumen) |
| Itti, Koch y Niebur, 1998 | https://sites.krieger.jhu.edu/cns/files/2021/08/Itti_etal98.pdf | (resumen) |
| WCAG 2.2 (1.4.3, 1.4.11, 2.3.1) | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html | (resumen); www.w3.org no abrió |
| Machado, Oliveira y Fernandes, 2009; Okabe e Ito | https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html | (resumen) |
| Estudios del propio repositorio | `estudios/2026-11-26_accion_stickman_y_tin_y_tan.md`, `manual/13`, `manual/14` | Leídos |
