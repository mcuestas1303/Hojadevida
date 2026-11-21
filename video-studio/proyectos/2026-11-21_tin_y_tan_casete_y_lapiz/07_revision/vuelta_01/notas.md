# Vuelta 1 — notas de revisión

Video revisado: `06_final/tin_y_tan_short01_v1.mp4` (primer render completo, 900 fotogramas, 30,000 s).
Herramientas: `revisar_fotogramas.py` (`revision.md`, `marcados.jpg`), `analizar_video.py --cada 0.5` (`analisis/hoja_01–03.jpg`,
miradas una por una) y `codigo/comprobar_video.py` (`comprobacion_propia.txt`, a 540x960 y fotograma a fotograma).

Antes del primer render completo se corrigió, sobre una hoja previa de 60 fotogramas, un fallo de texto: el trazo de
tinta de 0,05 em pegaba entre sí las letras de la palabra clave («cassette», «11», «1,100» parecían una mancha). Se
añadió entre las letras de la palabra con trazo un espacio igual al trazo. Por eso «how many turns?» queda en 5,70 %
y «rewinding a cassette» en 4,70 % (ver `../decisiones_de_render.md`).

## Qué se buscó y qué se encontró

| Qué | Resultado |
|---|---|
| Texto cortado o fuera de cuadro | No. Todos los textos empiezan en x = 108 px y terminan antes de x = 980 px (se comprueba en el código antes de dibujar). |
| Texto encima de un personaje, del casete o del reloj | No. El texto va de y = 15 % a 22 %; el casete empieza en 24,8 % y las cabezas en 44 %. |
| Cuadrados en lugar de letras | No. Los 33 caracteres usados están en Inter Display Medium (comprobado en el código); no hay «≈» ni «→». |
| Contador que retrocede | No. 6.3 → 77.8 → 114.0 → 126.9 → 128.5 y 192 → 725 → 1,017 → 1,142 → 1,170 (tomate). También se comprueba fotograma a fotograma en el código. |
| Personajes mal ubicados o de distinto tamaño | No. Tan a la izquierda con espejo, Tin a la derecha sin espejo, mismo `alto` (34 %); Tin solo a 44 %. La visera de perfil (toma 5) se lee como gorra. |
| Fotogramas vacíos | Ninguno. |
| Lápiz sobre la etiqueta / letras en el casete | No. |
| Cortes fuera de la rejilla | No. Los 15 cortes caen en su fotograma (múltiplos de 15). `revisar_fotogramas.py` solo detecta 3 (1,0; 3,5; 5,0) porque mira a 96x54 px y todos los planos comparten el papel crema; la comprobación propia los ve todos. Los cortes de 0,5 y 25,5 son continuación del mismo plano, como pide el prompt. |
| **Tramos sin cambio** | **Sí, uno real: de 17,57 a 18,27 s (toma 10)** la imagen queda idéntica 0,7 s: el empuje con muelle `sello` se asienta en 0,4 s y Tin no se mueve. |
| «Imagen congelada» de `revisar_fotogramas.py` (2,0–3,2; 7,3–9,2; 9,8–11,7; 15,4–16,8; 18,8–20,1) | A resolución completa sí hay cambio en todos esos tramos (carretes, cinta que corre, arco, cortes de la barra), pero es pequeño: la herramienta trabaja a 96x54 px. El de 7,3–9,2 (toma 6) es el más quieto: el prompt pide carretes detenidos («respiro») y solo quedaban el empuje de 3 % y la bufanda. |

## Qué se cambió para la vuelta 2

1. Empujes de cámara de las tomas 4, 10 y 12: 70 % del recorrido con muelle `sello` y 30 % con ease-out cúbico hasta
   el final de la toma, para que no quede ningún tramo congelado.
2. Toma 6: el lápiz de Tin tiene movimiento secundario (±3 grados, una sacudida de muelle por pulso) y la bufanda de
   Tan se mueve más (viento de ±0,22). Los carretes siguen quietos, como pide el prompt.
3. Toma 3: la bufanda de Tan mantiene la oscilación de ±0,3 hasta el final (antes se apagaba).

## Observaciones que no se corrigen (son la especificación)

- Toma 2: con el empuje a 135 % centrado en el carrete izquierdo, el borde derecho del casete sale del cuadro.
- Toma 3: el rodete de Tan queda a 15 px del borde inferior del casete (casi se tocan).
- Toma 9: el arco y el segmento de 11 cm miden 3 px, como pide el prompt; se ven, pero son finos para un teléfono.
- Toma 7: el plano es una tira de 77 px sobre papel vacío.
