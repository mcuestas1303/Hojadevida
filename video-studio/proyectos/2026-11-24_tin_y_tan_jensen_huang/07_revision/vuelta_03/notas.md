# Vuelta 3 — render 3 del short 3 (2026-11-24)

Único cambio respecto del render 2 (pedido por el supervisor en `vuelta_02/firma_supervisor.md`): la tarjeta en español
«4.382 días.» se veía 9 fotogramas nítidos.

- `codigo/tiempos.py`, `SUBTITULOS`: la tarjeta 8 («Steve Jobs, Apple: / 4.382 días.») sigue hasta el corte de 22,5 s y
  continúa después en un solo renglón, «4.382 días.», de 22,5 a 23,5 s (la de dos renglones tapaba la barra tras el
  corte: 3.670 px bajo el panel). «4.382 días.» queda en pantalla 1,43 s seguidos (22,07 a 23,5 s).
- La tarjeta 9, «¿Casi 12 años?», va de 23,5 a 24,5 s (30 fotogramas). Tan dice «twelve years?» de 22,71 a 24,49 s.
- Medido en todos los fotogramas (`subtitulos_medidos.txt`): mínimo 12 px a las cabezas y 16 px a los gráficos; PASA.
- Render con `--sin-audio`: la mezcla es la misma del render 2 (misma `05_audio/mezcla.wav`). 0 destellos; bucle 0,27 de 255.
- Entrega rehecha (CRF 26, 2,94 MB); `entrega.py`: lista para entregar. Lo que se oye en la entrega coincide con el guion.
- Evidencia: `par.jpg` (22,2 s y 22,9 s) y `tira_tarjeta8.jpg`.

Sin hacer en este render: la flecha del calendario sigue pasando sobre el 18, 24 y 25 (menor, anotado por el supervisor).
Los `.srt` no cambian: son la pista completa; las tarjetas quemadas son su versión corta.

Escucha: el dueño aprobó voz, pronunciación y mezcla sobre el render 1 (`../escucha_del_dueno.md`). Desde entonces solo
bajaron a −20 dBFS el chasquido y el silbido de ida de la firma del lápiz (pico de −1,0 a −1,7 dBTP); se le avisó.

## Verificación externa de Keter (2026-11-24, antes de publicar)

Keter abrió las fuentes que desde aquí estaban bloqueadas: renuncia el 12-nov (Al Jazeera y NBC; un punto de CNBC dice
13-nov, con lo que serían 10 días: se mantiene el 12 por tener dos fuentes); el 17-nov el presidente de la junta dijo
que no pensaban reponerlo (NBC y CNBC); reposición el 23-nov en el comunicado de Nvidia
(nvidianews.nvidia.com/news/nvidia-board-reinstates-jensen-huang-as-president-ceo-and-board-director). Sus cuentas dan
11, 6, 12.274, 5 y 4.382. La descripción deja de decir que el comunicado no se pudo abrir y lo cita. Desde esta
conversación el comunicado no se leyó: la lectura es de Keter.
