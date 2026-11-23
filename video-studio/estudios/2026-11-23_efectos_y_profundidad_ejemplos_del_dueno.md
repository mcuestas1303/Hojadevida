# Estudio — efectos de video y profundidad: los ejemplos del dueño

- **Fecha:** 2026-11-23
- **Pedido del dueño (textual):** «Veamos el tercer video de Tin y Tan pero quiero que le demos profundidad y
  comencemos a usar más efectos de video. Te he pasado varios videos de ejemplo».
- **De dónde sale esto:** los ejemplos son reels de Instagram que el dueño le mandó a Keter hasta el 2026-11-21.
  **Este equipo no vio ninguno**: lo de abajo es el resumen que pasó Keter de sus fichas (Cerebro, `nodos/`). No hay
  segundos exactos salvo donde se indica, y el dueño no dijo de ninguno «este me gusta»; ninguno trae la palabra
  «profundidad». Keter le preguntó cuáles son los de profundidad.
- **Uso:** se toma la técnica. No se usa metraje, música ni marca de nadie.

## Los ejemplos

| N.º | Cuenta y enlace | Qué enseña | Nota del dueño |
|---|---|---|---|
| 1 | willrvail, «Viral Video Breakdown», https://www.instagram.com/p/Df2NAP3R7KC/ (39,7 s) | ≈ 52 cambios visuales en 30 s, con ráfagas y respiros de 2–3 s; gancho de 4 cortes en los primeros 0,6 s; planos macro, héroe abierto hacia la mitad, subjetivo y **revelado desde desenfoque**; transiciones de barrido de obturador, desenfoque y destello; un destello en negativo que vuelve como firma; final en bucle | Aplicarlo al equipo creativo y al generador |
| 2 | silvesttre.ai, https://www.instagram.com/p/Df-FD2sMnGa/ (89 s) | Motion graphics por código: física de muelles, tipografía y paleta de referencias reales, sonido atado a cada corte, revisión fotograma por fotograma | La misma |
| 3 | lmksilv, https://www.instagram.com/p/Df1VfeVAbWO/ | Reel de marca en 20 planos (ya estudiado en `2026-11-21_reel_de_marca_20_planos_bn.md`) | «Para replicar» |
| 4 | justyn.ai, https://www.instagram.com/p/Df7oScSsQ9p/ | Rehacer un efecto ajeno con material propio; biblioteca de efectos | «Esto puede servir para replicar…» |
| 5 | godofprompt, https://www.instagram.com/p/Df0B76nCNsY/ | Escena 3D (océano) hecha por código en un solo archivo: lo más cercano a profundidad real | «Necesito que entiendas esta forma barata de producir» |
| 6 | willrvail, desglose de un video de música, https://www.instagram.com/p/DfCmMZ7RBz4/ (2:11) | Lista de 14 efectos: destello de entrada de 2–4 fotogramas; zoom de salida de 150 a 100 %; texto de vidrio; plano en blanco y negro antes del color; plano de respiro; corte escondido en el movimiento; negativo; destellos en los golpes; texturas y garabatos; congelado como transición; clon en espejo; **barrido del fondo con el personaje fijo (paralaje)**; texto en modo Exclusion; rotoscopia con fondo en blanco y negro | Sin nota |
| 7 | annderrey, https://www.instagram.com/p/DfDOvols8DU/ | 10 efectos: salir del cuadro; **atravesar la escena**; letras de cristal; órbita; interfaces flotantes; muro de titulares; celular animado; gráfico que crece; garabatos; zoom de golpe | Sin nota |
| 8 | taki.gpt, https://www.instagram.com/p/Det_44sBsPY/ | 20 efectos: zoom, titulares en cascada, curva de crecimiento, pantalla verde | Sin nota |
| 9 | artzenmedia, https://www.instagram.com/p/DetwKJlBPu0/ | Abrir el cuadro con las manos; saltos con dos keyframes (recorte y transformación) | Sin nota |
| 10 | rourke, https://www.instagram.com/p/DfXaQcyoaJ5/ | 34 estilos de luz para nombrar en el prompt | Sin nota |

## Qué de esto da profundidad en un dibujo por código

| Técnica | Cómo se hace sin gastar créditos | De qué ejemplo sale |
|---|---|---|
| Capas con paralaje | Fondo, plano medio y primer plano que se mueven a distinta velocidad cuando la cámara empuja o barre | 6 |
| Desenfoque por distancia | La capa lejana y la muy cercana van borrosas; el foco cambia de una a otra | 1 |
| Revelado desde desenfoque | El plano entra borroso y se aclara sobre el objeto | 1 |
| Sombras | Sombra de contacto bajo personajes y objetos, y sombra proyectada sobre el papel | propio |
| Atravesar la escena | La cámara pasa por un hueco (el agujero de un carrete, una ventana) hacia el plano siguiente | 7 |
| Algo cruza por delante | Un objeto pasa entre la cámara y los personajes y esconde el corte | 6 |
| Escala con la distancia | Lo que se acerca crece y se oscurece el fondo | propio |
| Órbita falsa | Giro simulado alrededor de un objeto con dos o tres vistas | 7 |

## Efectos de video que caben en Tin & Tan

Zoom de golpe en el pulso; barrido de obturador; destello corto de entrada; congelado como transición; salir del
cuadro; garabatos y texturas de papel; gráfico que crece; contador; titulares en cascada; plano de respiro tras una
ráfaga; gancho de varios cortes en el primer segundo.

## Lo que hay que cuidar

- **Destellos y negativos.** Un destello repetido puede molestar o afectar a personas fotosensibles. Límite del
  estudio: como máximo 3 destellos por segundo, nunca a pantalla completa en blanco puro, y `revisar_fotogramas.py`
  sigue marcándolos. El «negativo que vuelve» se usa como acento, no como parpadeo.
- **La regla de color** (dos neutros y un acento) y la legibilidad a los 45 o más siguen mandando: los efectos van
  sobre la paleta del canal.
- **El perfil emocional** de los dos primeros videos decía «sin efectos de luz: calma». Esto lo cambia a propósito;
  hay que decir qué emoción busca cada efecto nuevo y medirlo.
- **Contenido repetitivo.** Variar el lenguaje visual entre videos ayuda frente a esa política de YouTube.
