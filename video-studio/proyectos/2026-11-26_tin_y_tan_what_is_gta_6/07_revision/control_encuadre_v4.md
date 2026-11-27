# Control automático de encuadre y movimiento — short 4, versión 4

Grabación: `trabajo` · 986 fotogramas · hecho por `codigo/control_encuadre.py`.

**Resultado: PASA** · 0 fallos, 6 avisos.

Avisos (no bloquean; se miran en las hojas):
- E1: rival cortado en f129–f145
- E2: rival alto en f70–f81, f87–f88, f285–f293, f306–f312, f316, f322–f329, f591–f594
- E4: el rival sobre la cabeza de Tin en f85, f295
- E4: el rival sobre la cabeza de Tan en f106–f107, f631–f632
- M2: Tan salta 0.51 u en f303 (fuera de cuadro)
- M5: Tin clavado en f648, f805


## G1 · Claves del guion

Ninguna clave cruzada ni repetida.

## E1 · Personajes cortados por un borde lateral (centro de la cabeza a menos de 70 px)

- rival: f129–f145

## E2 · Fuera de la zona de acción (y 705–1376)

- rival, cabeza por encima de la zona: f70–f81, f87–f88, f285–f293, f306–f312, f316, f322–f329, f591–f594

## E3 · Cabezas encimadas

Ninguna.

## E4 · El cuerpo del rival sobre la cabeza de Tin o de Tan

- sobre Tin: f85, f295
- sobre Tan: f106–f107, f631–f632

## M1 · Carreras y caminatas

| Quién | Fotogramas | Modo | Recorre (u) | u/s | En pantalla (px) | f por paso | Pie de apoyo resbala (u, máx.) | |
|---|---|---|---|---|---|---|---|---|
| Tin | f283–f295 | corre | 1.98 | 4.6 | 461 | 7.3 | 0.11 | bien |
| Tan | f577–f594 | corre (diagonal) | 2.95 | 4.9 | 504 | 6.4 | 0.14 (no aplica) | bien |
| Tan | f661–f679 | corre_arma (diagonal) | 3.41 | 5.4 | 310 | 6.2 | 0.54 (no aplica) | bien |
| rival | f146–f167 | corre (diagonal) | 4.13 | 5.6 | 264 | 8.0 | 0.79 (no aplica) | bien |

## M2 · Saltos de posición de Tin y de Tan (> 0,36 u en un fotograma, fuera del contacto)

- Tan: f303 (0.51 u, fuera de cuadro)

## M3 · Contactos

| Golpe | Con qué | Del punto de golpe al rival (u) | Diferencia de carril (u) | Estrella a la cabeza de quien pega (u) | |
|---|---|---|---|---|---|
| golpe 1 | mano | 0.29 | 0.00 | 0.59 | bien |
| golpe 2 | pie | 0.33 | 0.00 | 1.07 | bien |
| golpe 3 | mano | 0.43 | 0.05 | 1.00 | bien |
| bloqueo | espada contra bastón | — | — | 0.68 (a la cabeza de Tin) | bien |
| golpe 4 | arma | 0.23 | 0.00 | 1.19 | bien |
| golpe 5 | arma | 0.35 | 0.00 | 1.52 | bien |
| remate (Tin) | arma | 0.36 | 0.00 | 1.15 | bien |
| remate (Tan) | arma | 0.28 | 0.00 | 1.31 | bien |
| golpe 6 | arma | 0.29 | 0.00 | 1.40 | bien |

## M4 · Quietud (mano de Tin o de Tan sin moverse más de 8 f estando en cuadro)

Nadie.

## M5 · Cuerpos clavados (mano y cabeza de Tin o de Tan se mueven menos de 14 px en 24 f estando en cuadro)

- Tin: f648, f805

## Encuadre por plano (px): dónde quedan las cabezas y los pies

| Plano | Fotogramas | Tin: x de la cabeza | Tan: x de la cabeza | Rival: x de la cabeza | Cabeza más alta (y) | Pies más bajos (y) | Alto de Tin o Tan (px) |
|---|---|---|---|---|---|---|---|
| P2 entra el rival | f30–f69 | 841–950 | 87–217 | 397–658 | 671 | 1339 | 427 |
| P3 golpe 1 | f70–f99 | 464–920 | -48–230 | -50–443 | 430 | 1364 | 476 |
| P4 impacto estante | f100–f101 | fuera | fuera | 135–144 | 507 | 1443 | — |
| P5 el rival vuelve | f102–f156 | fuera | 521–596 | 644–1103 | 595 | 1330 | 445 |
| P6 golpe 2 | f157–f183 | 713–890 | 140–236 | 427–1087 | 670 | 1323 | 448 |
| P7 general | f184–f282 | 89–356 | fuera | 476–941 | 661 | 1353 | 419 |
| P8 gancho | f283–f335 | 217–542 | fuera | 501–1019 | 358 | 1399 | 455 |
| P9 impacto mostrador | f336–f337 | fuera | fuera | 1031–1033 | 603 | 1483 | — |
| P10 general | f338–f429 | 144–337 | fuera | 576–995 | 527 | 1337 | 476 |
| P11 detalle del lápiz | f430–f441 | -9–90 | fuera | fuera | 451 | 1893 | 1390 |
| P12 general | f442–f482 | 161–207 | fuera | 712–775 | 599 | 1351 | 491 |
| P12b Tan invita | f483–f511 | fuera | 443–593 | fuera | 696 | 1829 | 1105 |
| P12c espada y bloqueo | f512–f561 | 271–404 | fuera | 602–902 | 642 | 1345 | 518 |
| P13 impacto televisor | f562–f563 | 634–634 | fuera | fuera | 6889 | 13198 | 6309 |
| P14 golpe 4 y cruce de Tan | f564–f598 | 169–553 | -43–760 | 752–1074 | 377 | 1363 | 394 |
| P15 mazo, carga y remate | f599–f718 | -45–340 | 132–971 | 253–990 | 503 | 1371 | 387 |
| P18 héroe | f719–f749 | 107–323 | 744–942 | fuera | 907 | 1348 | 362 |
| P19 respiro | f750–f873 | 163–258 | 836–972 | 445–560 | 877 | 1364 | 424 |
| P20 golpe 6 | f874–f905 | 199–451 | fuera | 698–911 | 744 | 1344 | 559 |
| P21 final | f906–f955 | 112–285 | 846–932 | 515–516 | 876 | 1350 | 432 |
