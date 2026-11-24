# Revisión, vuelta 2 — short 3 de Tin & Tan (render 2, tras el rechazo del supervisor)

Fecha: 2026-11-24. Pieza: `06_final/tin_y_tan_short03_v1.mp4` (mismo nombre; se rehace con `python3 codigo/render.py`, ≈ 160 s),
`06_final/portada_short03.png` y `08_entrega/TIN-EN-S-003/`. 0 créditos. **La voz no se tocó.** Corrige lo pedido en
`07_revision/vuelta_01/firma_supervisor.md`. Miradas las cuatro hojas de `analisis/` y los fotogramas de la firma uno por uno
(`firma_apertura_f0_f14.jpg`, `firma_cierre_f900_f914.jpg`, `firma_cierre_f915_f929.jpg`). **Nadie ha escuchado el audio.**

## Tiempos reales

- 31,0 s, 930 fotogramas. Cortes: 1,0; 3,5; 6,5; 9,0; **11,5; 12,5**; 14,5; 16,0; 19,0; 22,5; 24,5; 27,0; 30,0.
- Voz: sin cambios (0,47 a 30,05 s). Tan atrapa el lápiz en el fotograma 10; la voz entra en el 14.
- Pico: 22,07 s = 71,2 %. Subida 19,43–20,23; silencio 20,23–20,63; contador 20,88–22,07.

## Qué cambió (por punto del encargo)

1. **Lápiz y cabezas** (`herramientas/efectos.py`): brazo de la firma (95°, 108°) en vez de `saluda`; punto de mano H en
   x de Tan + 1,51 R (el brazo mide 1,50 R: 1,6 R no se alcanza); salida del vuelo hacia delante; `_despejes` mide TODOS los
   fotogramas (c −30 a 30) contra las cabezas como círculos, sin la exclusión «junto a la mano». **Distancia mínima del lápiz:
   28,8 px a la cabeza de Tan (c = −14, f916) y 46,2 px a la de Tin con visera (f0)**; 61 px a la silla. Visto en f0–f14 y
   f900–f929: no toca ninguna cabeza. Obturador con hasta 16 subpasos (ya no se ve un abanico). `FIRMA_LAPIZ_BUMERAN.md`, sección 0b, actualizada.
2. **Subtítulos y cabezas:** `ALTO_PJ` = 505 px (26,3 %; con 520 quedaban a 9 px). Medido por código en los 762 fotogramas con
   tarjeta (`subtitulos_huecos.txt`, `render.py --medir-subtitulos`): **hueco mínimo panel–cabezas 12 px (tarjeta 8; las demás,
   25 px o más)**; panel–gráficos de arriba 16 px; 0 píxeles dibujados bajo ningún panel. Las letras van dentro del panel.
3. **Barras:** cada fila lleva su nombre en tinta encima («Huang 11», «Altman 5», «Jobs 4,382», 56 px) y su barra o marca
   debajo; filas separadas 124 px. «Jobs 4,382» entra cuando el contador llega. La barra de 12.274 va sin la marca mostaza.
   Filas añadidas a la tabla de rótulos de §12 del prompt.
4. **Portada:** Tan con `sorpresa` (también en todo el plano de firma). Tin en x = 75 % (la gorra ya no sale de x 960).
5. **Calendario:** círculo de tinta en el 17, flecha larga del 17 al 23 (≈ 300 px, 8 px de grosor, con punta), círculo del 12
   en tinta en las tomas 5 y 6; números arriba de la celda y cruces debajo (ya no tapan los números).
6. **Tarjetas:** «¿Jensen Huang volvió / rápido en 11 días?», «El 17, la junta dijo / que no lo repondría.», «Seis días
   después, / lo repuso como CEO.», «Sam Altman, OpenAI: / 5 días.», «Steve Jobs, Apple: / 4.382 días.», «¿Casi 12 años?».
   Renglón más ancho 854 px (máximo 856). El segundo renglón de la 7 entra con «five days» y el de la 8 cuando el contador
   llega (22,07 s: se ve 13 fotogramas antes del corte). `subtitulos_es.srt`: la entrada 9 pasa a «¿Casi 12 años?».
7. **Toma 6:** va de 11,5 a 12,5 s (antes 12,0–13,0): «11 days» sale sobre «…as C E O.» y «Before that:»; «more than
   thirty-three years» (desde ≈ 12,6 s) ya cae en la toma 7 con «12,274 days» (12,8 s) y la tarjeta 5 (12,5 s).
8. **Línea editorial:** Tin con cara `neutra` (ojos de punto, cejas en reposo, boca suave, sin rubor; definida en `render.py`
   con piezas de las fichas) en las tomas 3, 4, 5, 7, 9 y 10; en la reposición Tan señala con `sorpresa` (sin `celebra`); en
   el pico Tan abre las manos y Tin levanta la mano, los dos con `sorpresa` (sin `eureka`). Risa solo en la toma 12; sonrisa de Tin en la 13.
9. **Silla de la toma 3:** al centro, entre los dos (x 452–628): dentro de la zona segura.
10. **Documentos:** prompt (nota de tiempos, duración de las tomas, tablas de rótulos y de tarjetas), `ficha_tecnica.md`,
    `perfil_emocional.md` (22,07 s, 71,2 %, 31,0 s, Tan atrapa en f10), `licencias.md`, `ficha.json`.

Además: la toma 10 se movía poco antes del contador y `revisar_fotogramas.py` la marcó (19,1–20,8 s): ahora hay cambio de
pose y un empuje lento; sin marcas. El zoom de golpe se ancla en la banda de subtítulos para que ni las barras ni las cabezas
la pisen. Sonido de la firma: chasquido −20,0 dBFS, whoosh de ida −20,8, de vuelta −18,0, atrapada −12,0; empalme −34,0 / −33,5.

## Controles (render 2)

| Control | Resultado |
|---|---|
| `revisar_voz.py` sobre el video final | 87 palabras. Con el guion «November twelfth»: **1 diferencia, del comparador** (oye «12th» y lo normaliza a «twelveth»). Con el guion escrito «November 12th»: **0 diferencias** (`voz_video_final_12th.md`) |
| `comprobar_destellos` (930 fotogramas, margen de 2 por segundo) | 0 cambios bruscos; mayor salto 6,1 de 255 |
| `postpro.py destellos` (final y entrega) | 0 |
| `comprobar_video.py` | formato pedido: sí; 13 cortes en la rejilla; sin tramos quietos ni fotogramas vacíos; sin tinta fuera de la zona segura por arriba ni por los lados (mitad de arriba); media máxima 229; **−14,0 LUFS, pico real −1,7 dBTP**; un silencio de 0,4 s en 20,24 (el buscado) |
| Bucle | fotograma 930 = 0; último frente al 0: 0,27 de 255 (render), 0,55 (archivo) |
| `revisar_fotogramas.py` | sin marcas |
| `revisar_color.py` | video ≈ 93 %, portada ≈ 93 %, entrega ≈ 93 % |
| `revisar_texto.py` | 0 errores en pantalla (inglés, con los nombres de las barras), tarjetas, los dos `.srt` y `ficha.json` |
| `entrega.py` | lista para entregar; `video.mp4` 2,93 MB (CRF 26, audio copiado) |
| `validar_prompt.py` | sin errores |
| Portada (`portada_medidas.txt`) | texto y 416–692; silla y 715–1104; lápiz entero x 486–672 (187 px, 17 %); caras dentro de la zona útil (Tin hasta x 945) |

## Lo que no quedó o no se comprobó

- **Oído humano:** todo lo de la vuelta 1 sigue pendiente (pronunciación de Nvidia, Huang, OpenAI y C E O; cola de «Altman»;
  pausa alargada tras «Apple:»; golpes, firma y música; cortes de 6,5, 9,0 y 16,0 s sobre la cola de la línea anterior).
- El punto de mano quedó en 1,51 R y no en 1,6 R (límite del brazo).
- El hueco de la tarjeta 8 es justo 12 px en los fotogramas previos al contador.
- «4.382 días.» en español se ve solo 13 fotogramas (0,43 s): mostrarla antes adelantaría el pico.
- En la toma 6 ninguna voz dice «eleven days»: el rótulo acompaña el final de la línea 4.
- Números del calendario ≈ 20 px: siguen sin leerse en un teléfono; la fecha la da el rótulo.
- Portada: mayúsculas de 98 px y 22 px entre «Days?» y la silla, sin cambios.
- «That is twelve years?» en la voz y en `subtitulos.srt` sigue sin palabra de aproximación (no se regenera).
- La cara `neutra` no está en las fichas de los personajes: falta que el director de animación la acepte o la lleve a `palitos.py`.
- Sin hacer: `direccion.md` (sección 3b), `07_revision/controles.md`, `registro_codigos.md`, `consumo.md`, `COORDINACION.md`; firmas del supervisor, de fotografía, de sonido y del director creativo.
