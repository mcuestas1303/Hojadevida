# Control automático de encuadre y movimiento — short 5, animática muda

Grabación: `s5_a5` · 930 fotogramas · hecho por `codigo/control_encuadre.py`.

**Resultado: PASA** · 0 fallos, 4 avisos.

Avisos (no bloquean; se miran en las hojas):
- E1: rival cortado en f91–f99, f137–f142, f228–f229, f343
- E3: Tan y rival encimadas en f116–f117
- E5: la madeja del rival contra Tan en f118
- E5: la madeja sobre el arma de Tin en f792


## G1 · Claves del guion

Ninguna clave cruzada ni repetida.

## E1 · Personajes cortados por un borde lateral (centro de la cabeza a menos de 70 px)

- rival: f91–f99, f137–f142, f228–f229, f343

## E2 · Fuera de la zona de acción (y 705–1376)

Nadie.

## E3 · Cabezas encimadas

- Tan y rival: f116–f117

## E4 · El cuerpo del rival sobre la cabeza de Tin o de Tan

Nunca.

## E5 · La madeja del rival contra la cabeza ampliada (visera, rodete) o el arma de Tin o de Tan

- contra Tan: f118
- la madeja sobre el arma de Tin (aviso): f792

## M1 · Carreras y caminatas

| Quién | Fotogramas | Modo | Recorre (u) | u/s | En pantalla (px) | f por paso | Pie de apoyo resbala (u, máx.) | |
|---|---|---|---|---|---|---|---|---|
| Tin | f100–f111 | corre | 1.77 | 4.4 | 527 | 5.7 | 0.05 | bien |
| Tin | f162–f172 | corre | 2.25 | 6.1 | 367 | 4.7 | 0.10 | bien |
| Tin | f272–f289 | camina | 1.33 | 2.2 | 204 | 6.1 | 0.00 | bien |
| Tin | f420–f433 | camina (diagonal) | 1.08 | 2.3 | 71 | 6.8 | 0.33 (no aplica) | bien |
| Tin | f446–f457 | corre | 2.46 | 6.2 | 803 | 4.4 | 0.06 | bien |
| Tin | f542–f573 | camina | 2.34 | 2.2 | 259 | 6.1 | 0.08 | bien |
| Tin | f640–f650 | corre_arma | 1.81 | 4.9 | 383 | 5.7 | 0.02 | bien |
| Tin | f840–f884 | camina (diagonal) | 1.76 | 1.2 | 78 | 13.5 | 0.33 (no aplica) | bien |
| Tan | f104–f115 | corre (diagonal) | 2.23 | 5.6 | 1539 | 6.0 | 0.19 (no aplica) | bien |
| Tan | f143–f162 | corre | 4.16 | 6.2 | 604 | 4.4 | 0.09 | bien |
| Tan | f438–f451 | camina | 0.99 | 2.1 | 364 | 6.4 | 0.00 | bien |
| Tan | f458–f469 | corre_arma (diagonal) | 1.89 | 4.7 | 419 | 7.1 | 0.06 (no aplica) | bien |
| Tan | f604–f617 | corre | 2.17 | 4.6 | 519 | 5.9 | 0.02 | bien |
| Tan | f840–f851 | corre | 2.01 | 5.0 | 310 | 5.7 | 0.02 | bien |
| rival | f50–f67 | camina (diagonal) | 1.88 | 3.1 | 70 | 7.4 | 0.46 (no aplica) | bien |
| rival | f268–f291 | camina | 2.06 | 2.6 | 263 | 6.3 | 0.05 | bien |
| rival | f450–f470 | corre | 4.81 | 6.9 | 1149 | 4.0 | 0.03 | bien |
| rival | f566–f594 | camina | 3.38 | 3.5 | 276 | 3.9 | 0.07 | bien |
| rival | f624–f639 | camina (diagonal) | 1.40 | 2.6 | 236 | 5.2 | 0.42 (no aplica) | bien |
| rival | f770–f797 | camina (diagonal) | 2.80 | 3.0 | 139 | 4.1 | 0.23 (no aplica) | bien |

## M2 · Saltos de posición de Tin y de Tan (> 0,36 u en un fotograma, fuera del contacto)

Ninguno.

## M3 · Contactos

| Golpe | Con qué | Del punto de golpe al rival (u) | Diferencia de carril (u) | Estrella a la cabeza de quien pega (u) | |
|---|---|---|---|---|---|
| golpe 1 | mano | 0.24 | 0.00 | 0.66 | bien |
| golpe 2 | mano | 0.13 | 0.00 | 0.59 | bien |
| golpe 3 | pie | 0.40 | 0.00 | 0.96 | bien |
| golpe 4 | arma | 0.28 | 0.00 | 1.20 | bien |
| golpe 5 | arma | 0.26 | 0.00 | 1.20 | bien |
| bloqueo | regla sobre la muñeca de Tan | — | — | 1.23 (a la cabeza más cercana de Tin o de Tan) | bien |
| golpe 6 | arma | 0.07 | 0.00 | 1.26 | bien |

## M4 · Quietud (mano de Tin o de Tan sin moverse más de 8 f estando en cuadro)

Nadie.

## M5 · Cuerpos clavados (mano y cabeza de Tin o de Tan se mueven menos de 14 px en 24 f estando en cuadro)

Nadie.

## Encuadre por plano (px): dónde quedan las cabezas y los pies

| Plano | Fotogramas | Tin: x de la cabeza | Tan: x de la cabeza | Rival: x de la cabeza | Cabeza más alta (y) | Pies más bajos (y) | Alto de Tin o Tan (px) |
|---|---|---|---|---|---|---|---|
| P02 nace el rival | f30–f45 | 820–850 | 156–241 | 499–499 | 828 | 1340 | 319 |
| P03 el rival crece | f46–f75 | 787–843 | 166–298 | 552–650 | 848 | 1340 | 278 |
| P04 golpe 1 | f76–f99 | 465–884 | fuera | -57–444 | 686 | 1340 | 416 |
| P05 impacto pila | f100–f117 | fuera | 9–299 | 303–400 | 502 | 1934 | 926 |
| P06 golpe 2 | f118–f143 | fuera | 163–460 | 399–1052 | 847 | 1340 | 344 |
| P07 contraataque | f144–f185 | 476–919 | -50–42 | 125–750 | 762 | 1340 | 299 |
| P08 golpe 3 | f186–f229 | 729–916 | fuera | 58–728 | 839 | 1342 | 266 |
| P09 general | f230–f295 | 675–918 | fuera | 84–466 | 999 | 1340 | 287 |
| P10 detalle del lápiz | f296–f329 | 284–666 | fuera | fuera | 464 | 1885 | 1395 |
| P11 golpe 4 | f330–f343 | 778–960 | fuera | 37–671 | 954 | 1340 | 269 |
| P12 chispas del farol | f344–f373 | fuera | fuera | 335–676 | 583 | 1538 | — |
| P13 general | f374–f437 | 843–947 | fuera | 242–288 | 953 | 1340 | 282 |
| P14 héroe de los dos | f438–f471 | -45–518 | 622–1099 | -5–786 | 777 | 1501 | 671 |
| P15 golpe 5 | f472–f499 | fuera | 607–827 | 130–440 | 697 | 1340 | 453 |
| P16 general | f500–f540 | 142–191 | 836–927 | 411–412 | 832 | 1340 | 285 |
| P17 respiro y objeto que cae | f541–f599 | 77–385 | 921–949 | 382–704 | 1037 | 1340 | 200 |
| P18 el paquete | f600–f631 | fuera | 873–1125 | 271–371 | 900 | 1335 | 426 |
| P19 bloqueo | f632–f677 | -55–266 | 813–976 | 437–552 | 863 | 1338 | 411 |
| P20 detalle del paquete | f678–f699 | fuera | fuera | fuera | 9999 | 0 | — |
| P21 pico | f700–f732 | 164–277 | 832–899 | 323–484 | 976 | 1338 | 258 |
| P22 revelado | f733–f799 | 167–235 | 853–903 | 394–525 | 1005 | 1340 | 298 |
| P23 golpe 6 | f800–f836 | 281–511 | fuera | 690–817 | 874 | 1340 | 454 |
| P24 remate | f837–f899 | 177–226 | 507–866 | -57–435 | 983 | 1340 | 285 |
