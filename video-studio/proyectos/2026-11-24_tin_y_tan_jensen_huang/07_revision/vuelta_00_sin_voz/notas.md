# Vuelta 0 (sin voz) — montaje DETENIDO el 2026-11-24

**Estado:** detenido por cambio de rumbo del dueño (el canal deja de definirse por la nostalgia; este video ya no es
el tercer short). No se renderizó nada: ni un fotograma, ni hoja de contacto, ni video, ni audio. 0 créditos.
No hay commit. No se tocaron `herramientas/efectos.py` (sigue en 1.0) ni `herramientas/palitos.py` (1.3).

## Qué existe

Solo `codigo/render.py` (escrito entero, una sola pasada). **Importa sin error** (`import render`: N = 915; el
contador llegaría a 4,000 en el fotograma 665). **Ninguna función de dibujo se ha ejecutado ni visto**: todo lo de
abajo es código sin probar.

- `comprobaciones()` **falla** en una aserción: el signo «÷» de la ecuación queda en x 95–172 (zona segura desde
  100; hay que ponerlo en x ≥ 105). Es lo único que se llegó a ejecutar.
- `main()` tiene un resto sin limpiar en la comprobación del bucle (una línea `capas, cam = plano_portada(0.0)` que
  sobra). La opción `--medidas` que anuncia la cabecera **no está escrita**.

## Reutilizable para el nuevo guion (escrito, SIN probar)

- **Tablas de tiempo arriba del archivo:** `VOZ` (12 líneas), `CORTES` (14 tomas), `MARCAS`, y `C(n)`, `L(n)`, `F(t)`;
  todos los instantes (textos, foco, barrido, silencio, contador) se derivan de ellas.
- **Objetos genéricos (sin logotipo, letra ni verde):** `tarjeta_1999`, `tarjeta_actual`, `capa_tarjeta` (con recorte
  para entrar en una ranura), `capa_pc_beige` (mesa, torre y monitor), `capa_pedestal`, `capa_cable`,
  `capa_placa_base` (ranura, zócalo, memorias, chips), `capa_manos`, `capa_die`, `imagen_pared` / `capa_pared`
  (80 × 50 = 4.000 minitarjetas).
- **Utilidades:** `pj()` (personaje por capas con sombra de contacto), `mezcla()` y `cambio()` (intercalado de 6
  fotogramas entre dos poses existentes), `cam_hacia`, `en_pantalla`, `en_reposo`, `golpe()`, `pegar()`,
  `geometria()`, `capa_texto()`, `texto_portada()`, `cajas_de_texto()`.
- **Tomas 1 a 14** y `fotograma()` (barrido 7→8, borrón 5→6, golpe de zoom, congelado con marco): escritas, sin ver.

## Lo que NO se hizo

- `audio.py`, `armar_dialogo.py`, `miniatura.py` y `comprobar_video.py`: **no existen** (no se llegó a escribirlos).
- Ningún control: ni `analizar_video.py`, ni `revisar_fotogramas.py`, `revisar_color.py`, `revisar_texto.py`,
  `comprobar_destellos`, tabla de portada ni bucle. `licencias.md` no se actualizó.

## Apartes del prompt ya decididos en el código (para revisar si se reutiliza)

- Tomas 3 y 4: Tin con `espejo=True` y pose `saluda` (no `senala`): hacia afuera, el brazo y el lápiz salían del
  cuadro (x ≈ 1090); personajes en x 26 % y 74 % y avance de cámara 0 → 100 (no 150), por la zona segura.
- El prompt se contradice en la toma 3: pide a Tin y Tan desenfocados 4–5 px «porque ninguno habla», pero Tin dice
  la línea 2 en esa toma. Se dejó el campo de foco más ancho (175) para que la cara se lea; sin ver.
- Chip de 320 px (no 400) para que el círculo de tinta no toque el texto ni las cabezas; tarjeta de la toma 8 de
  800 px (no 840); placa base más alta (y 660–1560) con ranuras y zócalo añadidos; la tarjeta «crece» redibujándola
  (en `efectos.py` cambiar `z` no cambia el tamaño de reposo).
- Golpes de «Back» y de zoom: suben y vuelven a 1,0 (no se quedan ampliados).
