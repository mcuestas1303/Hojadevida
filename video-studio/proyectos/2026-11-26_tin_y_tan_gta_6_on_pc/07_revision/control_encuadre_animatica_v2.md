# Control automático de encuadre y movimiento — short 4, versión 3

Grabación: `s5_a2` · 930 fotogramas · hecho por `codigo/control_encuadre.py`.

**Resultado: NO PASA** · 22 fallos, 2 avisos.

Fallos:
- E2: Tin bajo en f644–f645
- E3: Tin y rival encimadas en f94–f99, f190–f200, f815
- E4: el rival sobre la cabeza de Tin en f90, f93–f99, f153–f161, f190–f201, f214–f216, f338, f542–f544, f814–f817
- E4: el rival sobre la cabeza de Tan en f138–f140, f142, f486–f489, f661
- E5: la madeja del rival contra Tin en f69–f70, f90–f99, f152–f163, f189–f211, f214–f217, f338, f649–f650, f812–f818
- E5: la madeja del rival contra Tan en f130–f131, f138–f143, f486–f489, f494–f496, f661
- M1: Tin f100–f112: resbala
- M1: Tin f272–f289: resbala
- M1: Tin f540–f561: resbala
- M1: Tin f640–f650: resbala
- M1: Tan f143–f162: resbala
- M1: Tan f312–f326: resbala
- M1: Tan f438–f451: resbala
- M1: Tan f632–f649: resbala
- M1: Tan f662–f675: poco en pantalla
- M1: rival f268–f291: resbala
- M1: rival f566–f594: resbala
- M1: rival f642–f661: resbala
- M1: rival f770–f797: resbala
- M3: golpe 2: no llega al rival, estrella sobre quien pega
- M3: golpe 6: no llega al rival
- M3: faltan contactos medidos

Avisos (no bloquean; se miran en las hojas):
- E2: rival alto en f76–f87
- E3: Tan y rival encimadas en f487–f488


## G1 · Claves del guion

Ninguna clave cruzada ni repetida.

## E1 · Personajes cortados por un borde lateral (centro de la cabeza a menos de 70 px)

Ninguno.

## E2 · Fuera de la zona de acción (y 705–1376)

- Tin, pies por debajo de la zona: f644–f645
- rival, cabeza por encima de la zona: f76–f87

## E3 · Cabezas encimadas

- Tin y rival: f94–f99, f190–f200, f815
- Tan y rival: f487–f488

## E4 · El cuerpo del rival sobre la cabeza de Tin o de Tan

- sobre Tin: f90, f93–f99, f153–f161, f190–f201, f214–f216, f338, f542–f544, f814–f817
- sobre Tan: f138–f140, f142, f486–f489, f661

## E5 · La madeja del rival contra la cabeza ampliada (visera, rodete) o el arma de Tin o de Tan

- contra Tin: f69–f70, f90–f99, f152–f163, f189–f211, f214–f217, f338, f649–f650, f812–f818
- contra Tan: f130–f131, f138–f143, f486–f489, f494–f496, f661

## M1 · Carreras y caminatas

| Quién | Fotogramas | Modo | Recorre (u) | u/s | En pantalla (px) | f por paso | Pie de apoyo resbala (u, máx.) | |
|---|---|---|---|---|---|---|---|---|
| Tin | f100–f112 | corre | 1.95 | 4.5 | 1062 | 7.4 | 0.13 | resbala |
| Tin | f146–f159 | corre (diagonal) | 2.23 | 4.8 | 327 | 7.0 | 0.06 (no aplica) | bien |
| Tin | f272–f289 | camina | 0.84 | 1.4 | 104 | 15.1 | 0.44 | resbala |
| Tin | f420–f433 | camina (diagonal) | 1.08 | 2.3 | 71 | 10.6 | 0.18 (no aplica) | bien |
| Tin | f446–f457 | corre | 2.46 | 6.2 | 803 | 4.6 | 0.04 | bien |
| Tin | f506–f521 | corre | 2.96 | 5.6 | 484 | 5.2 | 0.10 | bien |
| Tin | f540–f561 | corre_arma | 4.96 | 6.8 | 727 | 4.2 | 0.34 | resbala |
| Tin | f640–f650 | corre_arma | 1.88 | 5.1 | 374 | 5.8 | 0.74 | resbala |
| Tin | f840–f884 | camina (diagonal) | 1.76 | 1.2 | 63 | 21.0 | 0.27 (no aplica) | bien |
| Tan | f106–f122 | corre (diagonal) | 2.41 | 4.3 | 1465 | 7.9 | 0.17 (no aplica) | bien |
| Tan | f143–f162 | corre | 3.76 | 5.6 | 740 | 5.3 | 0.37 | resbala |
| Tan | f296–f310 | corre (diagonal) | 4.10 | 8.2 | 345239 | 4.1 | 0.15 (no aplica) | bien |
| Tan | f312–f326 | corre | 4.10 | 8.2 | 279956 | 4.0 | 0.22 | resbala |
| Tan | f438–f451 | camina | 1.06 | 2.3 | 384 | 10.9 | 0.38 | resbala |
| Tan | f458–f469 | corre_arma (diagonal) | 1.89 | 4.7 | 419 | 7.1 | 0.06 (no aplica) | bien |
| Tan | f632–f649 | camina | 2.13 | 3.5 | 554 | 6.2 | 0.79 | resbala |
| Tan | f662–f675 | corre (diagonal) | 2.64 | 5.7 | 251 | 5.9 | 0.25 (no aplica) | poco en pantalla |
| Tan | f840–f855 | corre | 2.68 | 5.0 | 407 | 5.7 | 0.10 | bien |
| rival | f50–f67 | camina (diagonal) | 1.88 | 3.1 | 73 | 11.6 | 0.35 (no aplica) | bien |
| rival | f156–f165 | camina (diagonal) | 2.21 | 6.6 | 315 | 4.3 | 0.32 (no aplica) | bien |
| rival | f268–f291 | camina | 2.06 | 2.6 | 221 | 9.8 | 0.68 | resbala |
| rival | f450–f470 | corre | 4.81 | 6.9 | 1149 | 4.2 | 0.06 | bien |
| rival | f566–f594 | camina | 3.62 | 3.7 | 326 | 5.6 | 0.83 | resbala |
| rival | f642–f661 | camina | 1.41 | 2.1 | 181 | 8.7 | 1.50 | resbala |
| rival | f770–f797 | camina | 3.05 | 3.3 | 360 | 5.4 | 0.63 | resbala |

## M2 · Saltos de posición de Tin y de Tan (> 0,36 u en un fotograma, fuera del contacto)

Ninguno.

## M3 · Contactos

| Golpe | Con qué | Del punto de golpe al rival (u) | Diferencia de carril (u) | Estrella a la cabeza de quien pega (u) | |
|---|---|---|---|---|---|
| golpe 1 | mano | 0.30 | 0.00 | 0.59 | bien |
| golpe 2 | hombro | 0.50 | 0.00 | 0.44 | no llega al rival; estrella sobre quien pega |
| golpe 3 | pie | 0.45 | 0.00 | 0.96 | bien |
| golpe 4 | arma | 0.28 | 0.00 | 1.20 | bien |
| golpe 5 | arma | 0.29 | 0.00 | 1.17 | bien |
| bloqueo | regla sobre la muñeca de Tan | — | — | 1.29 (a la cabeza más cercana de Tin o de Tan) | bien |
| golpe 6 | arma | 0.83 | 0.00 | 0.99 | no llega al rival |

## M4 · Quietud (mano de Tin o de Tan sin moverse más de 8 f estando en cuadro)

Nadie.

## M5 · Cuerpos clavados (mano y cabeza de Tin o de Tan se mueven menos de 14 px en 24 f estando en cuadro)

Nadie.

## Encuadre por plano (px): dónde quedan las cabezas y los pies

| Plano | Fotogramas | Tin: x de la cabeza | Tan: x de la cabeza | Rival: x de la cabeza | Cabeza más alta (y) | Pies más bajos (y) | Alto de Tin o Tan (px) |
|---|---|---|---|---|---|---|---|
| P02 nace el rival | f30–f45 | 804–837 | 169–261 | 528–528 | 789 | 1340 | 346 |
| P03 el rival crece | f46–f75 | 742–838 | 171–307 | 565–667 | 835 | 1340 | 287 |
| P04 golpe 1 | f76–f99 | 406–870 | fuera | 72–665 | 557 | 1340 | 515 |
| P05 impacto pila | f100–f117 | fuera | -26–159 | 999–1117 | 582 | 1978 | 1042 |
| P06 golpe 2 | f118–f143 | fuera | 305–758 | 399–870 | 609 | 1340 | 437 |
| P07 contraataque | f144–f185 | 471–862 | -45–105 | 200–604 | 594 | 1340 | 334 |
| P08 golpe 3 | f186–f229 | 768–879 | fuera | 326–846 | 705 | 1340 | 339 |
| P09 general | f230–f295 | 756–889 | 139–176 | 341–590 | 999 | 1340 | 262 |
| P10 detalle del lápiz | f296–f329 | 284–666 | 14–14 | fuera | 47 | 7644 | 1395 |
| P11 golpe 4 | f330–f343 | 778–960 | fuera | 299–740 | 950 | 1340 | 269 |
| P12 chispas del farol | f344–f373 | fuera | fuera | 386–632 | 583 | 1538 | — |
| P13 general | f374–f437 | 843–949 | fuera | 147–169 | 955 | 1340 | 282 |
| P14 héroe de los dos | f438–f471 | -44–518 | 622–1108 | -12–790 | 777 | 1557 | 672 |
| P15 golpe 5 | f472–f499 | fuera | 573–826 | 176–701 | 589 | 1340 | 519 |
| P16 general | f500–f553 | 72–723 | 825–920 | 528–583 | 805 | 1340 | 269 |
| P17 respiro y objeto que cae | f554–f599 | 63–269 | 908–939 | 370–693 | 1066 | 1340 | 218 |
| P18 el paquete | f600–f645 | -17–60 | fuera | 389–428 | 900 | 1394 | 478 |
| P19 bloqueo | f646–f677 | 280–378 | 667–1006 | 449–593 | 981 | 1340 | 232 |
| P20 detalle del paquete | f678–f699 | fuera | fuera | 6–6 | 115 | 1117 | — |
| P21 pico | f700–f732 | 164–277 | 1016–1094 | 357–749 | 995 | 1390 | 262 |
| P22 revelado | f733–f799 | 156–212 | 903–949 | 344–742 | 1045 | 1340 | 263 |
| P23 golpe 6 | f800–f836 | 281–572 | fuera | 661–711 | 874 | 1340 | 454 |
| P24 remate | f837–f899 | 169–211 | 458–916 | -53–383 | 1013 | 1340 | 273 |
