# Vuelta 2 — notas de revisión

Video revisado: `06_final/tin_y_tan_short01_v1.mp4` después de los tres cambios de la vuelta 1. Es la versión que queda.
Miradas las tres hojas de `analisis/` (60 fotogramas, uno cada 0,5 s), `revision.md` y `comprobacion_propia.txt`.

## Qué fallaba en la vuelta 1 y cómo quedó

| Fallo de la vuelta 1 | Cambio | Resultado |
|---|---|---|
| Imagen idéntica 0,7 s en la toma 10 (17,57–18,27) | Empuje de cámara: 70 % con muelle `sello`, 30 % con ease-out cúbico hasta el final de la toma (tomas 4, 10 y 12) | `comprobar_video.py`: ningún tramo de 0,5 s o más sin cambio. Quedan pausas de 0,1 a 0,25 s (finales de las tomas 10, 11 y 14), que son los asentamientos de cada muelle |
| Toma 6 casi quieta (carretes detenidos por el prompt) | Movimiento secundario del lápiz de Tin (±3 grados, una sacudida por pulso) y más bufanda | Hay cambio en todos los fotogramas del tramo, pero pequeño |
| La bufanda de Tan se apagaba en la toma 3 | Oscilación sostenida de ±0,3 | Bien |

## Lo que sigue marcado y no se resuelve con código sin salirse del prompt

- `revisar_fotogramas.py` sigue marcando «imagen congelada» en 2,0–3,2; 7,3–9,2; 9,8–11,7; 15,4–16,8 y 18,8–20,1 s, y solo
  detecta los cortes de 1,0 y 5,0. Mide a 96x54 px y 10 fps: a ese tamaño no ve los carretes, las marcas de la cinta
  (que corre a 617 px/s), el arco de 3 px ni los cortes de 3 px de la barra, y todos los planos comparten el papel
  crema. A resolución completa los 15 cortes están en su fotograma y hay movimiento en esos tramos. Aun así es una
  señal válida: **en esos tramos el movimiento es pequeño en pantalla** (sobre todo la toma 6, de 3 s, y la toma 7, que
  es una tira de 77 px). Darles más vida pide cambiar la especificación (carretes girando en la 6, gráficos más
  grandes en la 7, 9 y 11), y eso lo decide el equipo.
- Toma 9 (plano héroe): el arco y el segmento de 11 cm tienen 3 px, como dice el prompt. Se ven, pero en un teléfono
  son un hilo. Recomendación: 8 px o más y un carrete más grande que 160 px.
- Toma 2: a 135 % el borde derecho del casete sale del cuadro (consecuencia del empuje centrado en el carrete izquierdo).
- Toma 3: el rodete de Tan queda a 15 px del casete; no se tapan, pero casi se tocan.
- El sonido no se pudo escuchar: solo está medido (ver `../decisiones_de_render.md` y `05_audio/medidas_audio.json`).

## Comprobado en esta vuelta (sin fallos)

Texto dentro de la zona segura y nunca sobre personaje, casete ni reloj · sin cuadrados ni símbolos prohibidos ·
contadores 6.3 → 77.8 → 114.0 → 126.9 → 128.5 y 192 → 725 → 1,017 → 1,142 → 1,170 (solo suben; el 1,170 en tomate) ·
Tan a la izquierda con espejo y Tin a la derecha, mismo tamaño · visera de perfil legible (toma 5) · casete sin letras ·
lápiz dentro de la ventana, nunca sobre la etiqueta · ningún fotograma vacío · 900 fotogramas, 30,000 s ·
el fotograma 900 se dibuja con la misma función que el 0 y da los mismos bytes (lo comprueba `render.py` al terminar);
el último fotograma del archivo (899) difiere del 0 en 1,4/255 de media, que es un treintavo de segundo de movimiento ·
dos ejecuciones seguidas de `render.py` dan el mismo archivo (mismo MD5 del MP4 y de `mezcla.wav`).
