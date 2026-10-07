# Pendientes del indicador ZonasEventosNY

## Para ver en el móvil
- [ ] **Telegram**: al publicarse una noticia (y en la apertura de NY de días con noticia), tomar una captura del gráfico con las zonas y enviarla a un bot de Telegram junto con el dato real, la previsión y la sorpresa. Requiere MT5 encendido (PC o VPS) y permitir `https://api.telegram.org` en Herramientas → Opciones → Asesores expertos.
- [ ] **TradingView**: pasar el indicador a Pine Script para verlo en la app móvil de TradingView. La vela de apertura de NY se replica bien; las noticias no tienen hora exacta desde código (habría que cargar fechas a mano o usar `request.economic`, que es menos preciso).

## Ajustes menores
- [x] Quitar las 2 advertencias del compilador ("expression not boolean" en `LeerCalendario`).
- [ ] Reintentar cada 10 s (en vez de 60 s) cuando faltan velas M1 por cargar.
- [ ] Buscar las noticias también por su código interno en inglés (`event_code`), por si el terminal muestra los nombres en otro idioma.

## Opcionales (si se necesitan)
- [ ] Transparencia real del relleno de las zonas (dibujo con CCanvas).
- [ ] Movimiento del precio 15, 30 y 60 minutos después de la noticia.
- [ ] Estadísticas separadas según el dato salga por encima o por debajo de la previsión.
- [ ] Alerta al romper el máximo o mínimo de la zona de apertura o de noticia.
- [ ] Mover el indicador a un repositorio propio (ahora está en `Hojadevida`).
