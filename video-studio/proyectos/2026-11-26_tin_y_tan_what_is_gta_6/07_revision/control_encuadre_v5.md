# Control automático de encuadre y movimiento — short 4, versión 5

Grabación: `trabajo` · 986 fotogramas · hecho por `codigo/control_encuadre.py`.

**Resultado: PASA** · 0 fallos, 11 avisos.

Avisos (no bloquean; se miran en las hojas):
- E1: rival cortado en f109–f121, f632
- E2: rival alto en f70–f81, f87–f88, f285–f293, f305–f312, f316, f322–f329, f591–f594
- E4: el rival sobre la cabeza de Tin en f85
- E5: la madeja del rival contra Tin en f313, f513–f514
- E5: la madeja del rival contra Tan en f60–f61, f155–f156, f674, f678
- E5: la madeja sobre el arma de Tin en f512–f514
- M2: Tin salta 1.40 u en f102 (fuera de cuadro)
- M2: Tin salta 1.20 u en f156 (fuera de cuadro)
- M2: Tan salta 1.20 u en f184 (fuera de cuadro)
- M2: Tan salta 1.20 u en f302 (fuera de cuadro)
- M2: Tan salta 0.51 u en f303 (fuera de cuadro)


## G1 · Claves del guion

Ninguna clave cruzada ni repetida.

## E1 · Personajes cortados por un borde lateral (centro de la cabeza a menos de 70 px)

- rival: f109–f121, f632

## E2 · Fuera de la zona de acción (y 705–1376)

- rival, cabeza por encima de la zona: f70–f81, f87–f88, f285–f293, f305–f312, f316, f322–f329, f591–f594

## E3 · Cabezas encimadas

Ninguna.

## E4 · El cuerpo del rival sobre la cabeza de Tin o de Tan

- sobre Tin: f85

## E5 · La madeja del rival contra la cabeza ampliada (visera, rodete) o el arma de Tin o de Tan

- contra Tin: f313, f513–f514
- contra Tan: f60–f61, f155–f156, f674, f678
- la madeja sobre el arma de Tin (aviso): f512–f514

## M1 · Carreras y caminatas

| Quién | Fotogramas | Modo | Recorre (u) | u/s | En pantalla (px) | f por paso | Pie de apoyo resbala (u, máx.) | |
|---|---|---|---|---|---|---|---|---|
| Tin | f283–f295 | corre | 2.00 | 4.6 | 471 | 7.3 | 0.11 | bien |
| Tan | f577–f594 | corre (diagonal) | 2.95 | 4.9 | 504 | 6.4 | 0.14 (no aplica) | bien |
| Tan | f661–f679 | corre_arma (diagonal) | 3.41 | 5.4 | 301 | 6.2 | 0.55 (no aplica) | bien |
| rival | f146–f167 | corre (diagonal) | 4.22 | 5.8 | 270 | 7.8 | 0.53 (no aplica) | bien |

## M2 · Saltos de posición de Tin y de Tan (> 0,36 u en un fotograma, fuera del contacto)

- Tin: f102 (1.40 u, fuera de cuadro), f156 (1.20 u, fuera de cuadro)
- Tan: f184 (1.20 u, fuera de cuadro), f302 (1.20 u, fuera de cuadro), f303 (0.51 u, fuera de cuadro)

## M3 · Contactos

| Golpe | Con qué | Del punto de golpe al rival (u) | Diferencia de carril (u) | Estrella a la cabeza de quien pega (u) | |
|---|---|---|---|---|---|
| golpe 1 | mano | 0.31 | 0.00 | 0.68 | bien |
| golpe 2 | pie | 0.33 | 0.00 | 1.12 | bien |
| golpe 3 | mano | 0.43 | 0.05 | 1.00 | bien |
| bloqueo | espada contra bastón | — | — | 0.68 (a la cabeza de Tin) | bien |
| golpe 4 | arma | 0.23 | 0.00 | 1.19 | bien |
| golpe 5 | arma | 0.36 | 0.00 | 1.52 | bien |
| remate (Tin) | arma | 0.34 | 0.00 | 1.38 | bien |
| remate (Tan) | arma | 0.28 | 0.00 | 1.32 | bien |
| golpe 6 | arma | 0.28 | 0.00 | 1.40 | bien |

## M4 · Quietud (mano de Tin o de Tan sin moverse más de 8 f estando en cuadro)

Nadie.

## M5 · Cuerpos clavados (mano y cabeza de Tin o de Tan se mueven menos de 14 px en 24 f estando en cuadro)

Nadie.

## Encuadre por plano (px): dónde quedan las cabezas y los pies

| Plano | Fotogramas | Tin: x de la cabeza | Tan: x de la cabeza | Rival: x de la cabeza | Cabeza más alta (y) | Pies más bajos (y) | Alto de Tin o Tan (px) |
|---|---|---|---|---|---|---|---|
| P2 entra el rival | f30–f69 | 874–973 | 87–225 | 397–647 | 671 | 1339 | 426 |
| P3 golpe 1 | f70–f99 | 479–958 | -48–226 | -50–672 | 430 | 1364 | 477 |
| P4 impacto estante | f100–f101 | fuera | fuera | 959–960 | 506 | 1443 | — |
| P5 el rival vuelve | f102–f156 | fuera | 403–468 | 636–1074 | 594 | 1316 | 440 |
| P6 golpe 2 | f157–f183 | 725–930 | 106–244 | 475–1109 | 678 | 1323 | 443 |
| P7 general | f184–f282 | 119–349 | fuera | 528–980 | 662 | 1354 | 416 |
| P8 gancho | f283–f335 | 207–542 | fuera | 501–1019 | 303 | 1422 | 456 |
| P9 impacto mostrador | f336–f337 | fuera | fuera | 1031–1033 | 603 | 1483 | — |
| P10 general | f338–f429 | 135–341 | fuera | 576–995 | 527 | 1337 | 476 |
| P11 detalle del lápiz | f430–f441 | -29–84 | fuera | fuera | 452 | 1893 | 1381 |
| P12 general | f442–f482 | 152–212 | fuera | 712–775 | 599 | 1351 | 491 |
| P12b Tan invita | f483–f511 | fuera | 424–612 | fuera | 696 | 1829 | 1105 |
| P12c espada y bloqueo | f512–f561 | 271–413 | fuera | 602–902 | 642 | 1345 | 519 |
| P13 impacto televisor | f562–f563 | 634–634 | fuera | fuera | 6889 | 13198 | 6309 |
| P14 golpe 4 y cruce de Tan | f564–f598 | 160–553 | -43–760 | 752–1074 | 377 | 1363 | 394 |
| P15 mazo, carga y remate | f599–f718 | -30–289 | 118–983 | 307–1015 | 503 | 1375 | 387 |
| P18 héroe | f719–f749 | 16–293 | 802–1051 | fuera | 910 | 1463 | 454 |
| P19 respiro | f750–f873 | 164–266 | 832–978 | 445–560 | 876 | 1364 | 424 |
| P20 golpe 6 | f874–f905 | 233–460 | fuera | 682–874 | 798 | 1341 | 509 |
| P21 final | f906–f955 | 105–283 | 840–940 | 515–516 | 876 | 1350 | 431 |
