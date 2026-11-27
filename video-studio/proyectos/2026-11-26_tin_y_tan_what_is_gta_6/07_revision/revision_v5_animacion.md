# Revisión de animación — short 4, versión 5 (`tin_y_tan_short04_v5.mp4`)

- **Pieza revisada:** `06_final/tin_y_tan_short04_v5.mp4`, sha256 `df6b8a638e86` (12 primeros caracteres, dato de producción), 986 fotogramas a 30 f/s.
- **Firma:** director de animación, 2026-11-27.
- **Nombres:** Tin = gorra naranja (lápiz y bastón); Tan = verde de la bufanda (mazo); el rival = el garabato negro.

## 1. Qué miré y qué no pude comprobar

Miré:
- Las 21 tiras completas (`rev_v5/tira_01` a `tira_21`, 1 de cada 2 fotogramas).
- 25 fotogramas compuestos a resolución completa: f72, f84, f126, f150, f198, f300, f306, f366, f372, f378, f384, f558, f564, f570, f576, f588, f654, f666, f684, f690, f696, f822, f948 (y los citados en la tabla).
- `control_encuadre_v5.md` (PASA, 0 fallos, 11 avisos), mi `revision_v4_animacion.md` y los comentarios «v5» de `tin_en_s_004.js` (4 líneas: `GrTin`, rival cae a la derecha en el gancho, remate y salida del rival).

No pude comprobar:
- El sha256 ni el movimiento real (sin reproducir): los giros de 1–3 f y el balanceo del reposo se leen por diferencia entre poses en tiras de 1 de cada 2 fotogramas.
- Fotogramas impares de la tira y los que no abrí a resolución completa (p. ej. f102–f156 de Tan solo en tira y en f126/f150).
- La sincronía con el audio (no es mío).

## 2. Avisos del control

- **M2 «fuera de cuadro»** (Tin f102 y f156, Tan f184, f302, f303): en las tiras no se ve a Tin ni a Tan en el cuadro anterior ni en el posterior de esos saltos (tira_03/04, tira_06/07); son recolocaciones tapadas por el corte de impacto o por el borde. Bien.
- **M1 carreras:** las cuatro entradas están marcadas «bien»; no vi carrera hacia atrás ni patinaje en las tiras. El único movimiento que se aparta del rival es la inclinación y los dos pasos bajos de Tin f374–f396 (f378 y f384): son del v4, se leen como paso y vuelta, no como carrera atrás.
- **M3 contactos:** nueve contactos en «bien»; el remate de Tin (0.34 u) y el de Tan (0.28 u) llegan cada uno por su lado.
- **M5:** nadie clavado. **E1/E2/E4/E5:** vuelos y entradas del rival por el borde, sin bulto: f85 el rival ya no queda sobre la gorra de Tin (f84: se ve a su lado, a la izquierda).

## 3. Cambios declarados en la v5: comprobación

| Cambio | Cierto | Prueba |
|---|---|---|
| Más amplitud del reposo vivo | **Sí** | Tan f102–f156 (tira_03/04, f126, f150): cambia el peso entre cuadros, inclina el torso y gira la cabeza hacia el estante; ya no es el mismo dibujo. Tin f190–f250 (tira_05/06, f198): cambia el ángulo del lápiz y el apoyo |
| El rival espera con el brazo atrás (`acecha`) y cae más a la derecha | **Sí** | f72 (tira_02): el rival está de pie con el brazo atrás frente a Tin; f84: golpe y caída sin pasar sobre Tin |
| Baja del estante por la derecha; Tin se aparta con un paso | **Sí** | tira_06/07 y f306: el rival baja del estante a la derecha del mostrador; Tin da un paso y queda a la izquierda, con claro |
| Tin llega al remate con dos saltos desde el pasillo y pega erguido (`GrTin`) | **Sí** | tira_14/15 (f654–f690): Tin a la izquierda, el bastón recto, la cabeza fuera de la madeja del rival |
| Caída con la cabeza a la derecha y vuelta al levantarse | **Sí** | tira_06 y tira_17: cabeza a la derecha del cuerpo; se da la vuelta al levantarse sin giro de un solo fotograma |
| Guardia baja del rival tras el pisotón | **Sí** | tira_19 (f874–f900) |
| Tan retrocede antes de la patada y entra con paso largo | **Sí** | tira_04 (f157–f183): Tan se echa atrás y entra con paso largo |
| Tin y Tan se recolocan fuera de cuadro | **Sí** | ver avisos M2: ninguno se ve saltar |

## 4. Mis notas de la v4: estado

| Nota v4 | Estado en la v5 | Prueba |
|---|---|---|
| M1 reposos Tan f102–f156, Tin f190–f250 | **Resuelta** | ver tabla 3; el balanceo ahora es de peso, no de píxeles |
| M2 reposo Tin/Tan f786–f870 | **Resuelta, aceptable** | tira_17/18 y f822: el bastón de Tin y el mazo de Tan cambian de ángulo; cambian las caras |
| M3 bastón y mazo cruzados en el remate | **Resuelta** | f696 y tira_15: el bastón llega desde la izquierda y el mazo desde la derecha; el rival queda entre las puntas y las armas no se cruzan |
| M6 / b2 rival pegado al hombro de Tin f646–f656 | **Resuelta** | f654 y f666: el rival queda en el centro, a más de una cabeza de Tin |
| b2 lápiz pequeño al caer | **Mejorada** | f948: el lápiz mide unos 30 px de alto y se lee como lápiz; sigue pequeño frente al cuadro pero ya no es un punto |
| b4 cuerpo tendido casi negro | **Sin cambio (baja)** | f180–f216 en tira_04/05 |

## 5. Defectos nuevos

No encontré saltos de posición visibles, carreras hacia atrás, patinaje ni giros de un solo fotograma en lo nuevo de la v5.

Solo notas **bajas** (no bloquean):
- **b1. Lápiz que cae, f944–f950.** Mide unos 30 px; si se vuelve a tocar, subir 1,3 veces para que lea en el teléfono.
- **b2. Inclinación de Tin en f376–f386.** Con el cuerpo muy tumbado (f378, f384) se lee como un deslizamiento corto en lugar de un paso. Es una vuelta de v4 que sigue legible; si se toca, reducir la inclinación a la mitad.
- **b3. Cuerpo tendido del rival, f176–f216.** Sigue casi todo negro. Es el b4 de la v4; decisión de arte.

## 6. Qué está bien (no tocar)

- Reposo vivo con cambio de peso y de ángulo del arma en Tan f102–f156, Tin f190–f250 y los dos de f786–f870.
- Anticipación del gancho (f312) y entrada del rival con el brazo atrás (f72).
- Remate de Tin y Tan por lados opuestos, sin cruce de armas (f696–f714).
- Recolocaciones fuera de cuadro sin saltos visibles.
- Dos pasos bajos y vuelta de Tin f374–f396, pausas antes de cada golpe y cortes de impacto.

## 7. Veredicto

Los ocho cambios de la v5 son ciertos y funcionan. Las notas M1, M2, M3 y M6 de la v4 quedan resueltas, b2 mejora y no entra ningún defecto nuevo de gravedad media, alta o bloqueante. Solo quedan tres notas bajas.

Veredicto: APROBADO

Firma: director de animación, 2026-11-27.
