# Control automático de encuadre y movimiento — short 4, versión 3

Grabación: `d` · 986 fotogramas · hecho por `codigo/control_encuadre.py`.

**Resultado: PASA** · 0 fallos, 5 avisos.

Avisos (no bloquean; se miran en las hojas):
- E1: rival cortado en f213–f218
- E2: rival alto en f70–f81, f286–f293, f323–f329, f591–f595
- E3: Tan y rival encimadas en f86
- E3: Tin y rival encimadas en f660
- M2: Tan salta 0.51 u en f303 (fuera de cuadro)


## G1 · Claves del guion

Ninguna clave cruzada ni repetida.

## E1 · Personajes cortados por un borde lateral (centro de la cabeza a menos de 70 px)

- rival: f213–f218

## E2 · Fuera de la zona de acción (y 705–1376)

- rival, cabeza por encima de la zona: f70–f81, f286–f293, f323–f329, f591–f595

## E3 · Cabezas encimadas

- Tan y rival: f86
- Tin y rival: f660

## M1 · Carreras y caminatas

| Quién | Fotogramas | Modo | Recorre (u) | u/s | En pantalla (px) | f por paso | Pie de apoyo resbala (u, máx.) | |
|---|---|---|---|---|---|---|---|---|
| Tin | f283–f295 | corre | 2.09 | 4.8 | 493 | 6.9 | 0.09 | bien |
| Tin | f661–f679 | corre_arma (diagonal) | 3.24 | 5.1 | 383 | 6.6 | 0.43 (no aplica) | bien |
| Tan | f577–f594 | corre (diagonal) | 2.76 | 4.6 | 506 | 6.6 | 0.11 (no aplica) | bien |
| Tan | f661–f679 | corre_arma (diagonal) | 3.41 | 5.4 | 313 | 6.2 | 0.54 (no aplica) | bien |
| rival | f146–f167 | corre (diagonal) | 4.53 | 6.2 | 413 | 7.3 | 0.34 (no aplica) | bien |

## M2 · Saltos de posición de Tin y de Tan (> 0,36 u en un fotograma, fuera del contacto)

- Tan: f303 (0.51 u, fuera de cuadro)

## M3 · Contactos

| Golpe | Con qué | Del punto de golpe al rival (u) | Diferencia de carril (u) | Estrella a la cabeza de quien pega (u) | |
|---|---|---|---|---|---|
| golpe 1 | mano | 0.27 | 0.00 | 0.56 | bien |
| golpe 2 | pie | 0.34 | 0.00 | 1.12 | bien |
| golpe 3 | mano | 0.33 | 0.15 | 0.53 | bien |
| bloqueo | espada contra bastón | — | — | 0.54 (a la cabeza de Tin) | bien |
| golpe 4 | arma | 0.23 | 0.00 | 1.19 | bien |
| golpe 5 | arma | 0.35 | 0.00 | 1.52 | bien |
| remate (Tin) | arma | 0.36 | 0.00 | 1.15 | bien |
| remate (Tan) | arma | 0.28 | 0.00 | 1.31 | bien |
| golpe 6 | arma | 0.29 | 0.00 | 1.40 | bien |

## M4 · Quietud (mano de Tin o de Tan sin moverse más de 8 f estando en cuadro)

Nadie.

## Encuadre por plano (px): dónde quedan las cabezas y los pies

| Plano | Fotogramas | Tin: x de la cabeza | Tan: x de la cabeza | Rival: x de la cabeza | Cabeza más alta (y) | Pies más bajos (y) | Alto de Tin o Tan (px) |
|---|---|---|---|---|---|---|---|
| P2 entra el rival | f30–f69 | 792–947 | 85–209 | 397–658 | 671 | 1339 | 427 |
| P3 golpe 1 | f70–f99 | 450–863 | -48–240 | -50–443 | 532 | 1360 | 474 |
| P4 impacto estante | f100–f101 | fuera | fuera | 24–31 | 359 | 1523 | — |
| P5 el rival vuelve | f102–f156 | fuera | 610–673 | 77–680 | 596 | 1328 | 446 |
| P6 golpe 2 | f157–f183 | 740–921 | 125–225 | 235–916 | 635 | 1371 | 472 |
| P7 general | f184–f282 | 179–428 | fuera | 403–1055 | 637 | 1363 | 443 |
| P8 gancho | f283–f335 | 330–669 | fuera | 467–1007 | 374 | 1393 | 446 |
| P9 impacto mostrador | f336–f337 | 2–2 | fuera | 1031–1033 | 603 | 1520 | 826 |
| P10 general | f338–f429 | 176–491 | fuera | 576–995 | 527 | 1337 | 478 |
| P11 detalle del lápiz | f430–f441 | 9–107 | fuera | fuera | 451 | 1893 | 1403 |
| P12 general | f442–f482 | 161–199 | fuera | 712–775 | 599 | 1351 | 488 |
| P12b Tan invita | f483–f511 | fuera | 489–512 | fuera | 698 | 1829 | 1107 |
| P12c espada y bloqueo | f512–f561 | 271–384 | fuera | 602–902 | 642 | 1345 | 518 |
| P13 impacto televisor | f562–f563 | 634–634 | fuera | fuera | 6889 | 13198 | 6309 |
| P14 golpe 4 y cruce de Tan | f564–f598 | 228–540 | -47–719 | 752–1067 | 370 | 1353 | 388 |
| P15 mazo, carga y remate | f599–f718 | -22–403 | 132–965 | 253–990 | 469 | 1371 | 395 |
| P18 héroe | f719–f749 | 121–308 | 759–958 | fuera | 911 | 1348 | 359 |
| P19 respiro | f750–f873 | 148–243 | 836–960 | 445–560 | 880 | 1364 | 423 |
| P20 golpe 6 | f874–f905 | 199–451 | fuera | 698–911 | 743 | 1344 | 559 |
| P21 final | f906–f955 | 129–290 | 859–919 | 515–516 | 877 | 1350 | 431 |
