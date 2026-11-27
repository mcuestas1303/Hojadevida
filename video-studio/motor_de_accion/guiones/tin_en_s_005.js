// Guion del short 5 de Tin & Tan (TIN-EN-S-005, «Is GTA 6 Coming to PC? Here's What's Announced»).
// Fuente: proyectos/2026-11-26_tin_y_tan_gta_6_on_pc/02_prompt/direccion.md (2.2, 3.2, 4.2, 4.3, 4.10) y prompt.md.
// ANIMÁTICA MUDA, versión 0 (2026-11-27): coreografía, carriles, tamaños y cámaras, con los tiempos de la voz ESTIMADA
// (guiones/tin_en_s_005.tiempos.json). Sirve para medir con control_encuadre.py antes de generar la voz (método 2, sección 0).
// Lo que aquí es provisional y se termina antes del render: la regla de tinta (se dibuja con el arma «bastón»), el paquete,
// el telescopio, el fuego, la explosión por fases y las versiones rotas del entorno.
// Decisiones de producción de esta versión (van al brief, «Decisiones del equipo»):
//  1. Reparto del cuadro: el que pasó la puerta en el short 4 (acción y 705–1376, subtítulo abajo). La dirección (3.0) pone
//     el subtítulo en y 885–1105, en mitad del cuadro: es lo que el short 4 corrigió en su versión 3.
//  2. Cámara alta y en diagonal en los planos de pelea (4.2 de animación y lección del short 4); los ángulos `az` son los de
//     fotografía (3.2). Los planos a ras de suelo quedan para detalle, héroe y pico.
//  3. Plano 2: general desde el lado de Tan (la alternativa que deja fotografía al subjetivo).
// Las jugadas salen del banco (motor_de_accion/jugadas.js).
import { banco } from '../jugadas.js';
export const FICHA = { id: 'tin_en_s_005', entorno: 'patio_tienda_de_computadoras', paleta: 'b_noche_de_tinta', creado: '2026-11-27', estado: 'animática v0' };

export async function guion(m) {
  const { THREE, P, V, C, EASE, clamp, ra, pista, marca, grieta, mancha, onda, soltar, estrella, trozos, entorno, personajes, escena, caja } = m;
  window.MEDIDAS = window.MEDIDAS || {};
  const T = await (await fetch('guiones/tin_en_s_005.tiempos.json')).json();
  const K = T.K, N = T.N;
  const { tin, tan, duda } = personajes, Z = entorno.piezas, E = entorno.MEDIDAS;
  const { K1, K2, K3, K4, K5, KB, KR, K6 } = K;                    // KR = el toque al paquete (f700)
  const B = banco(m), { G, A, lerp, entre, pos, pose, trayecto, ataque, J } = B;
  const C1 = E.C1, C2 = E.C2, C3 = E.C3, CIERRE = K.cierre;

  // ------------------------------------------------------------ poses nuevas (provisionales: las afina animación)
  Object.assign(P, {
    cargaEmpuja: { t: -10, aF: [40, 140], aB: [36, 136], lF: [20, 0], lB: [-30, -10], c: -4 },
    empuja: { t: 18, aF: [88, 92], aB: [80, 88], lF: [40, 0], lB: [-40, -20], c: 2 },
    cargaHombro: { t: -8, aF: [-30, 60], aB: [40, 130], lF: [30, -10], lB: [-30, -20], c: -4 },
    cargaPatada: { t: 8, aF: [50, 140], aB: [20, 130], lF: [60, -70], lB: [-10, -20], c: 0 },
    patadaFrontal: { t: -14, aF: [-40, -80], aB: [40, 120], lF: [88, 86], lB: [-14, -30], c: -4 },
    batazoAtras: { t: 24, aF: [-30, 20], aB: [-20, 30], lF: [50, -30], lB: [-30, -60], c: 6, armaAng: 300 },
    batazo: { t: -12, aF: [130, 150], aB: [120, 140], lF: [30, 0], lB: [-36, -14], c: -10, armaAng: 120 },
    estocada: { t: 26, aF: [90, 90], aB: [-40, -20], lF: [60, -10], lB: [-50, -20], c: 4, armaAng: 90 },
    mide: { t: 0, aF: [70, 100], aB: [-12, -6], lF: [10, 4], lB: [-10, -4], c: 0, armaAng: 90 },
    manosAtras: { t: -4, aF: [-30, -70], aB: [-36, -80], lF: [8, 4], lB: [-8, -4], c: 8 },
    seCubre: { t: -14, aF: [120, 200], aB: [110, 190], lF: [20, 4], lB: [-24, -8], c: -12 },
    cruzaRegla: { t: 14, aF: [70, 80], aB: [30, 120], lF: [44, -10], lB: [-40, -20], c: 4, armaAng: 96 },
  });
  const Gd = A(P.guardia, 150), Cg = A(P.carga, 244), Gp = A(P.golpe, 98);

  // ------------------------------------------------------------ puesta en escena (v2 de la animática, por las mediciones de v0 y v1)
  // Reglas: (1) el plano de cada golpe encuadra a los dos que pelean y el tercero espera FUERA de cuadro, al lado contrario
  // de hacia donde sale despedido el rival; (2) nadie cruza por delante ni por detrás de otro dentro de un plano: las cabezas
  // miden ≈ 0,55 u y dos personajes necesitan ≈ 1,2 u de separación lateral aunque estén en carriles distintos; (3) el rival
  // no salta por encima de Tin: su contraataque se queda corto; (4) los golpes con la regla se dan a 1,4 u y el hombro a 0,25 u.
  const ARMA = { contacto: B.MEDIDAS.arma.contacto, recupera: B.MEDIDAS.arma.recupera, poses: { antes: Gd, carga: Cg, golpe: Gp, despues: Gd } };

  // ------------------------------------------------------------ Tin
  G.tin.visible.push([0, false], [30, true], [CIERRE, false]);
  G.tin.mira.push([0, -1], [100, 1], [114, -1], [434, 1], [446, -1], [506, 1], [540, -1], [563, 1]);
  G.tin.cara.push([0, 'curiosidad'], [80, 'concentrado'], [K1 + 2, 'curiosidad'], [170, 'sorpresa'], [192, 'concentrado'], [K3 + 2, 'curiosidad'], [296, 'concentrado'], [K4 + 2, 'eureka'], [380, 'curiosidad'], [640, 'sorpresa'], [660, 'concentrado'], [KR + 2, 'sorpresa'], [733, 'curiosidad'], [K6 - 13, 'concentrado'], [K6 + 2, 'curiosidad']);
  pos('tin', [30, [1.85, 0, C1]], [57, [1.85, 0, C1]]);
  J.saltito({ q: 'tin', f: 58, a: [1.85, C1], b: [2.4, -1.85] }); J.saltito({ q: 'tin', f: 66, a: [2.4, -1.85], b: [2.9, C2] });
  J.golpeDeFrente({ pega: 'tin', recibe: 'duda', k: K1, desde: [2.9, C2], rival: [1.2, C2], poses: { carga: P.cargaEmpuja, golpe: P.empuja } });
  trayecto('tin', 100, 113, [[2.3, 0, C2], [3.6, 0, -1.2]]);                                        // sale de cuadro por la derecha: el golpe 2 es de Tan
  pos('tin', [145, [3.6, 0, -1.2]]);
  trayecto('tin', 146, 160, [[3.6, 0, -1.2], [1.9, 0, C2]]);
  pos('tin', [177, [1.9, 0, C2]]);
  J.saltito({ q: 'tin', f: 178, a: [1.9, C2], b: [2.2, C2] }); J.saltito({ q: 'tin', f: 185, a: [2.2, C2], b: [2.5, C2] });   // lee el zarpazo y retrocede: el rival se queda corto
  J.saltito({ q: 'tin', f: 192, a: [2.5, C2], b: [2.35, C2] });
  J.golpeDeFrente({ pega: 'tin', recibe: 'duda', k: K3, desde: [2.35, C2], rival: [1.15, C2], contacto: 0.36, poses: { carga: P.cargaPatada, golpe: P.patadaFrontal } });
  pos('tin', [271, [2.25, 0, C2]]);
  trayecto('tin', 272, 290, [[2.25, 0, C2], [1.4, 0, C2]], 'camina');
  J.golpeDeFrente({ pega: 'tin', recibe: 'duda', k: K4, desde: [1.4, C2], rival: [-0.4, C2], ...ARMA });
  pos('tin', [419, [1.1, 0, C2]]);
  trayecto('tin', 420, 434, [[1.1, 0, C2], [1.1, 0, -1.6]], 'camina');
  pos('tin', [445, [1.1, 0, -1.6]]);
  trayecto('tin', 446, 458, [[1.1, 0, -1.6], [-1.4, 0, -1.4]]);                                     // deja el plano del golpe 5
  pos('tin', [505, [-1.4, 0, -1.4]]);
  trayecto('tin', 506, 522, [[-1.4, 0, -1.4], [1.6, 0, -1.5]]);
  pos('tin', [539, [1.6, 0, -1.5]]);
  trayecto('tin', 540, 562, [[1.6, 0, -1.5], [-3.4, 0, -1.4]], 'corre_arma');                       // se va al otro lado: bloqueará desde la izquierda del paquete
  pos('tin', [639, [-3.4, 0, -1.4]]);
  trayecto('tin', 640, 651, [[-3.4, 0, -1.4], [-1.9, 0, -2.6]], 'corre_arma');                      // el bloqueo
  pos('tin', [789, [-1.9, 0, -2.6]]);
  J.saltito({ q: 'tin', f: 790, a: [-1.9, -2.6], b: [-1.9, -2.9] });
  J.golpeDeFrente({ pega: 'tin', recibe: 'duda', k: K6, desde: [-1.9, -2.9], rival: [-0.4, -2.9], contacto: 1.15, recupera: 1.5, poses: ARMA.poses, recibePose: P.recogido });
  pos('tin', [839, [-1.9, 0, -2.9]]);
  trayecto('tin', 840, 885, [[-1.9, 0, -2.9], [-1.4, 0, -1.2]], 'camina');
  pos('tin', [N, [-1.4, 0, -1.2]]);
  pose('tin', [30, P.guardia], [56, P.guardia], [145, P.guardia], [170, P.guardia], [172, P.susto, 'out'], [176, P.susto], [177, P.guardia],
    [262, P.guardia], [271, P.guardia], [292, P.guardia], [296, P.dibuja], [322, P.dibuja], [372, Gd], [380, A(P.explica, 150), 'back'], [410, A(P.explica, 150)], [419, Gd], [436, Gd], [438, A(P.carga, 240)], [441, P.golpe, 'in'], [445, P.guardia],
    [523, P.guardia], [533, P.guardia], [537, P.atrapa, 'out'], [539, P.mide], [563, Gd], [639, Gd], [652, P.cruzaRegla, 'salto'], [659, P.cruzaRegla], [667, Gd],
    [686, Gd], [693, Cg, 'out'], [699, Cg], [KR, Gp, 'salto'], [KR + 3, Gp], [KR + 8, P.seCubre, 'out'], [KR + 18, P.seCubre], [KR + 30, Gd], [736, A(P.explica, 150), 'back'], [743, Gd], [789, Gd],
    [K6 + 24, A(P.quieto, 60)], [839, P.quieto], [886, P.quieto], [N, P.quieto]);

  // ------------------------------------------------------------ Tan
  G.tan.visible.push([0, false], [30, true], [CIERRE, false]);
  G.tan.mira.push([0, 1], [143, -1], [164, 1], [328, -1], [458, 1], [471, -1], [662, 1], [677, -1]);
  G.tan.cara.push([0, 'curiosidad'], [32, 'sorpresa'], [70, 'curiosidad'], [K2, 'sorpresa'], [K2 + 20, 'curiosidad'], [226, 'sorpresa'], [240, 'curiosidad'], [438, 'risa'], [472, 'concentrado'], [K5 + 2, 'curiosidad'], [532, 'risa'], [554, 'curiosidad'], [KR + 2, 'sorpresa'], [733, 'curiosidad']);
  pos('tan', [30, [-1.7, 0, C1]], [45, [-1.7, 0, C1]]);
  J.saltito({ q: 'tan', f: 46, a: [-1.7, C1], b: [-1.95, C1] }); J.saltito({ q: 'tan', f: 54, a: [-1.95, C1], b: [-2.2, C1] });
  pos('tan', [105, [-2.2, 0, C1]]);
  trayecto('tan', 106, 123, [[-2.2, 0, C1], [-0.45, 0, C2]]);                                       // carrera y frenada; espera a que el rival esté de pie
  pos('tan', [129, [-0.45, 0, C2]], [K2, [0.65, 0, C2], 'salto'], [141, [-0.2, 0, C2]], [142, [-0.2, 0, C2]]);
  B.contactos.push({ k: K2, pega: 'tan', recibe: 'duda', tipo: 'hombro' });
  trayecto('tan', 143, 163, [[-0.2, 0, C2], [-3.6, 0, C1]]);                                        // sale de cuadro por la izquierda
  pos('tan', [295, [-3.6, 0, C1]]);
  trayecto('tan', 296, 311, [[-3.6, 0, C1], [-0.2, 0, 1.4]]);                                       // cambia de lado por detrás de la cámara del plano de detalle
  trayecto('tan', 312, 327, [[-0.2, 0, 1.4], [3.2, 0, C1]]);
  pos('tan', [437, [3.2, 0, C1]]);
  trayecto('tan', 438, 452, [[3.2, 0, C1], [2.2, 0, -1.4]], 'camina');
  pos('tan', [457, [2.2, 0, -1.4]]);
  trayecto('tan', 458, 470, [[2.2, 0, -1.4], [3.4, 0, -2.9]], 'corre_arma');
  J.golpeDeFrente({ pega: 'tan', recibe: 'duda', k: K5, desde: [3.4, -2.9], rival: [1.9, -2.9], ...ARMA });
  pos('tan', [631, [3.4, 0, -2.9]]);
  trayecto('tan', 632, 650, [[3.4, 0, -2.9], [1.25, 0, -2.8]], 'camina');
  pos('tan', [661, [1.25, 0, -2.8]]);
  trayecto('tan', 662, 676, [[1.25, 0, -2.8], [3.6, 0, -1.5]]);
  pos('tan', [839, [3.6, 0, -1.5]]);
  trayecto('tan', 840, 856, [[3.6, 0, -1.5], [0.9, 0, -1.2]]);
  pos('tan', [N, [0.9, 0, -1.2]]);
  pose('tan', [30, P.pregunta], [44, P.pregunta], [62, P.guardia], [105, P.guardia], [124, P.guardia], [126, P.cargaHombro, 'out'], [129, P.cargaHombro], [K2, P.embiste, 'salto'], [K2 + 5, P.embiste], [K2 + 11, P.guardia],
    [164, P.guardia], [295, P.guardia], [328, P.guardia], [437, P.guardia], [440, P.atrapa, 'out'], [444, P.atrapa], [453, A(P.invita, 200), 'back'], [456, A(P.invita, 200)], [457, Gd],
    [528, Gd], [532, A(P.carga, 240)], [535, P.golpe, 'in'], [541, P.guardia], [631, P.guardia], [651, P.senala, 'out'], [652, P.susto, 'salto'], [659, P.susto], [661, P.guardia],
    [677, P.guardia], [KR + 2, P.guardia], [KR + 8, P.seCubre, 'out'], [KR + 18, P.seCubre], [KR + 30, P.guardia], [768, P.guardia], [774, P.senala, 'back'], [790, P.senala], [796, P.guardia], [839, P.guardia], [861, P.guardia], [864, P.atrapa, 'out'], [N, P.atrapa]);

  // ------------------------------------------------------------ el rival (@duda): nace de la grieta, baja un escalón con cada dato
  const D = G.duda, s = v => 0.77 * v;
  D.visible.push([0, false], [30, true], [870, false]);
  D.mira.push([0, 1], [K1 + 2, -1], [K2 + 2, 1], [K3 + 2, -1], [246, 1], [K4 + 2, -1], [450, 1], [K5 + 2, -1], [596, 1], [770, -1]);   // se da la vuelta al salir despedido
  D.cara.push([0, 'duda']);
  D.escala.push([30, s(1.25)], [45, s(1.25)], [69, s(1.5), 'back'], [98, s(1.5)], [106, s(1.35)], [132, s(1.35)], [140, s(1.2)], [214, s(1.2)], [222, s(1.1)], [338, s(1.1)], [346, s(1.0)], [553, s(1.0)], [565, s(0.9)], [719, s(0.9)], [726, s(0.8)], [K6 + 1, s(0.8)], [831, 0.1, 'in'], [N, 0.1]);
  pos('duda', [30, [E.grieta[0], 0, E.grieta[1]]], [49, [E.grieta[0], 0, E.grieta[1]]]);
  trayecto('duda', 50, 68, [[E.grieta[0], 0, E.grieta[1]], [1.2, 0, C2]], 'camina');
  J.despedido({ q: 'duda', k: K1, via: [[0.95, 0.45, -3.0], [0.85, 0, -3.3]], aterriza: 101, caida: false });           // golpe 1: contra la pila
  pos('duda', [118, [0.85, 0, -3.3]], [126, [0.9, 0, C2], 'out'], [K2 + 1, [0.9, 0, C2]]);
  J.despedido({ q: 'duda', k: K2, via: [[1.3, 1.4, -3.3], [1.8, 1.0, -4.0], [1.9, 0, -4.3]], aterriza: 147 });           // golpe 2: contra las cajas de la derecha
  pos('duda', [155, [1.9, 0, -4.3]]);
  trayecto('duda', 156, 166, [[1.9, 0, -4.3], [0.3, 0, C2]], 'camina');
  pos('duda', [167, [0.3, 0, C2]], [171, [0.15, 0, C2], 'out'], [177, [0.15, 0, C2]], [183, [0.7, 1.5, C2], 'out'], [190, [1.0, 0, C2], 'in'], [197, [1.15, 0, C2], 'out']);   // contraataque que se queda corto
  J.despedido({ q: 'duda', k: K3, via: [[0.2, 1.0, -3.0], [-1.2, 0.9, -3.4], [-2.1, 0, -3.9]], aterriza: 227, caida: false });   // golpe 3: contra los monitores
  pos('duda', [267, [-2.1, 0, -3.9]]);
  trayecto('duda', 268, 292, [[-2.1, 0, -3.9], [-0.4, 0, C2]], 'camina');
  pos('duda', [K4 + 2, [-0.6, 0.2, -2.8], 'salto'], [343, [-3.2, 1.3, -4.35], 'out'], [351, [-3.2, 1.3, -4.35]], [363, [-3.0, 0, -4.1], 'in'], [395, [-3.3, 0.6, -4.4], 'io'], [437, [-3.3, 0.6, -4.4]], [449, [-2.9, 0, -3.6], 'in']);   // golpe 4: contra el farol
  trayecto('duda', 450, 471, [[-2.9, 0, -3.6], [1.9, 0, -2.9]]);
  pos('duda', [K5 + 2, [1.8, 0.2, -3.1], 'salto'], [499, [1.3, 1.3, -6.25], 'out'], [502, [1.3, 1.3, -6.25]], [549, [1.3, 0, -6.2], 'in'], [553, [1.3, 0, -6.2]], [565, [1.3, 0, -5.6], 'out']);   // golpe 5: contra la persiana
  trayecto('duda', 566, 595, [[1.3, 0, -5.6], [-1.6, 0, -3.4]], 'camina');
  pos('duda', [641, [-1.6, 0, -3.4]]);
  trayecto('duda', 642, 662, [[-1.6, 0, -3.4], [-0.5, 0, -4.3]], 'camina');                                                  // se aparta hacia atrás, con las manos a la espalda
  pos('duda', [707, [-0.5, 0, -4.3]], [708, [-0.3, 0.3, -4.3], 'salto'], [714, [1.0, 1.3, -4.6], 'out'], [719, [2.0, 0, -3.9], 'in'], [726, [2.5, 0, -3.9], 'out'], [769, [2.5, 0, -3.9]]);   // el paquete revienta: despedido y rueda
  trayecto('duda', 770, 798, [[2.5, 0, -3.9], [-0.4, 0, -2.9]], 'camina');
  pos('duda', [855, [-0.4, 0, -2.9]], [869, [-4.7, 0, -2.9], 'in'], [N, [-4.7, 0, -2.9]]);                                   // el resto sale goteando por el borde izquierdo
  pose('duda', [30, P.quieto], [46, P.quieto], [56, P.poder, 'back'], [69, P.guardiaBaja], [K1 - 1, P.guardiaBaja], [102, P.sentado], [117, P.sentado], [124, P.quieto], [127, P.guardia], [K2 - 1, P.guardia], [K2, P.recibe, 'salto'],
    [151, P.sentado], [155, P.quieto], [167, P.guardia], [171, P.carga, 'out'], [175, P.carga], [178, P.acecha], [185, P.golpe], [189, P.golpe], [190, P.agachado, 'salto'], [197, P.agachado], [207, P.guardia], [K3 - 1, P.guardia],
    [228, P.sentado], [239, P.sentado], [246, P.quieto], [251, P.guardia], [293, P.guardia], [K4 - 1, P.guardia], [K4 + 3, P.vuela], [342, P.vuela], [344, P.recibe, 'salto'], [351, P.recibe], [363, P.agachado], [395, P.recogido], [437, P.recogido], [449, P.guardia],
    [472, P.guardia], [K5 - 1, P.guardia], [K5 + 3, P.vuela], [499, P.vuela], [500, P.recibe, 'salto'], [549, P.recibe], [557, P.agachado], [565, P.guardia], [596, P.dibuja], [611, P.dibuja], [614, P.empuja, 'out'], [640, P.empuja], [663, P.manosAtras], [699, P.manosAtras],
    [KR + 8, P.vuela, 'salto'], [719, P.vuela], [720, P.caido, 'salto'], [726, P.caido], [734, P.sentado], [761, P.sentado], [766, P.quieto], [769, P.guardia], [799, P.guardia], [K6 - 1, P.guardia], [K6 + 3, P.recogido], [N, P.recogido]);

  B.cerrar(['tin', 'tan']);
  window.MEDIDAS.banco = B.comprobar(N);
  if (window.MEDIDAS.banco.length) console.warn('BANCO: ' + window.MEDIDAS.banco.join(' | '));

  // ------------------------------------------------------------ extras: la regla (provisional: bastón), entrada del rival, giros
  const REGLA_TIN = [[300, K.regla_a_tan], [537, 848]], REGLA_TAN = [K.regla_a_tan + 6, 532];
  const vueltas = [[K2 + 6, K2 + 16, 6.28], [K4 + 2, K4 + 7, -3.1], [708, 719, 6.28]];
  function extra(id, f) {
    if (id === 'tin') { const x = { lapiz: f < 858 }; for (const [a, b] of REGLA_TIN) if (f >= a && f < b) x.arma = { tipo: 'baston', prog: a === 300 ? entre(f, 300, 322) : b === 848 && f >= 836 ? 1 - entre(f, 836, 847) : 1 }; return x; }
    if (id === 'tan') return f >= REGLA_TAN[0] && f < REGLA_TAN[1] ? { arma: { tipo: 'baston', prog: 1 } } : null;
    const x = {};
    if (f < 46) x.revela = entre(f, 30, 45);
    for (const [a, b, n] of vueltas) if (f >= a && f < b) x.giro = n * EASE.out(entre(f, a, b));
    for (const k of [98, 132, 214, 338, 486]) if (f >= k && f < k + 3) x.aplasta = 0.4;                // baja un escalón: se aplasta 3 f
    if (f >= K6 && f < K6 + 2) x.aplasta = 0.85;
    return x;
  }

  // ------------------------------------------------------------ piezas provisionales del guion
  const polvo = (x, y, z, n = 10, d = 1.6) => soltar('polvoC', V(x, y, z), V(0, 0.9, 0), d, n);
  const paquete = caja(0.55, 0.45, 0.5, C.bloque_cerca, 0.07); paquete.visible = false; escena.add(paquete);
  const telescopio = caja(0.55, 0.14, 0.14, C.utileria, 0.05); telescopio.visible = false; escena.add(telescopio);
  const CAJA_DE = [-1.0, -3.1], CAJA_A = [0.6, -2.8], TEL = E.telescopio;
  const CONTACTOS = [];
  function contacto(nombre, quien, parte, donde = 'pecho', tam = 0.6, n = 6, hacia = 0.75) {
    const a = personajes[quien], g = (parte === 'arma' ? a.armaMundo : parte === 'pie' ? a.pieMundo : parte === 'hombro' ? a.pechoMundo : a.manoMundo).clone();
    const blanco = (donde === 'cabeza' ? duda.cabezaMundo : donde === 'cadera' ? duda.caderaMundo : duda.pechoMundo).clone();
    const pr = (p) => window.proyecta(p.x, p.y, p.z), b0 = pr(blanco), pxU = Math.hypot(...window.proyecta(blanco.x, blanco.y + 1, blanco.z).map((v, i) => v - b0[i]));
    const d = Math.hypot(...pr(g).map((v, i) => v - b0[i])) / pxU, p = d > 0.45 ? g.clone().lerp(blanco, 1 - 0.3 / d) : g.clone().lerp(blanco, hacia);
    const cam = m.camara.position.clone().sub(p).setY(0).normalize(); p.addScaledVector(cam, 0.08);
    estrella(p, tam); soltar('gota', p, V(Math.sign(blanco.x - a.caderaMundo.x) * 2.6, 2.2, 0), 2.0, n);
    CONTACTOS.push({ nombre, f: null, quien, parte, golpe_a_rival_u: +d.toFixed(3), dz_u: +Math.abs(a.malla.position.z - duda.malla.position.z).toFixed(3), estrella_a_cabeza_de_quien_pega_u: +p.distanceTo(a.cabezaMundo).toFixed(3), vector: [+(blanco.x - g.x).toFixed(2), +(blanco.y - g.y).toFixed(2), +(blanco.z - g.z).toFixed(2)], estrella_px: pr(p).map(Math.round), cabeza_rival_px: pr(duda.cabezaMundo).map(Math.round) });
    window.MEDIDAS.contactos = CONTACTOS; return p;
  }
  const animados = [], anima = (f0, f1, fn) => animados.push([f0, f1, fn]);
  const HECHOS = [
    [30, () => { marca('grieta_abre'); grieta(E.grieta[0], E.grieta[1], 0.5, 6); }],
    [K1 - 1, () => marca('golpe')], [K1, () => contacto('golpe 1', 'tin', 'mano', 'pecho', 0.5, 4, 1.3)],
    [100, () => { marca('choque_madera'); polvo(0.5, 0.8, -3.4, 10); }],
    [K2 - 1, () => marca('golpe_grave')], [K2, () => contacto('golpe 2', 'tan', 'hombro', 'pecho', 0.55, 6, 1.3)],
    [146, () => { marca('cajas_caen'); polvo(2.0, 0.6, -4.4, 12, 2.0); for (const c of Z.cajas_der.cajas) { c.rotation.z = ra(-0.5, 0.5); c.position.y *= 0.6; c.scale.y = 0.6; } }],
    [182, () => marca('silbido')], [192, () => marca('roce_suelo')],
    [K3 - 1, () => marca('golpe_agudo')], [K3, () => contacto('golpe 3', 'tin', 'pie', 'pecho', 0.55, 6)],
    [226, () => { marca('vidrio_grieta'); marca('chispas'); soltar('chispaC', V(-2.3, 0.8, -4.2), V(0, 2.5, 1.2), 3, 8); Z.monitores.lista[1].rotation.x = -1.2; Z.monitores.lista[1].position.y = 0.2; }],
    [262, () => marca('caida_objeto')], [300, () => marca('trazo_de_tinta')],
    [K4 - 1, () => marca('regla_golpe')], [K4, () => contacto('golpe 4', 'tin', 'arma', 'pecho', 0.6, 7)],
    [344, () => { marca('farol_choque'); marca('chispas'); soltar('chispaC', V(E.farol[0], 1.5, E.farol[1] + 0.2), V(0.6, 2.5, 1.0), 3.5, 12); }],
    [356, () => marca('fuego_enciende')],
    [K.regla_a_tan, () => marca('silbido_corto')],
    [K5 - 1, () => marca('regla_golpe')], [K5, () => contacto('golpe 5', 'tan', 'arma', 'pecho', 0.55, 6)],
    [500, () => { marca('persiana_choque'); const g = Z.persiana.lienzo.getContext('2d'); g.strokeStyle = C.linea; g.lineWidth = 7; g.beginPath(); g.ellipse(300, 400, 70, 96, 0, 0, 7); g.stroke(); g.beginPath(); g.arc(300, 300, 46, 0, 7); g.stroke(); Z.persiana.tex.needsUpdate = true; Z.persiana.abollada = true; }],
    [573, () => marca('papel_rasga')], [588, () => { marca('caida_objeto'); polvo(TEL[0], 0.1, TEL[1], 4, 0.8); }],
    [596, () => { marca('trazo_de_tinta'); paquete.visible = true; }], [612, () => marca('paquete_desliza')],
    [KB, () => { marca('bloqueo_tinta'); const p = J.puntoDeBloqueo(tin.armaMundo.toArray(), tan.manoMundo.toArray()); estrella(V(...p), 0.4); CONTACTOS.push({ nombre: 'bloqueo', quien: 'tin', parte: 'regla sobre la muñeca de Tan', a_cabeza_u: +Math.min(V(...p).distanceTo(tin.cabezaMundo), V(...p).distanceTo(tan.cabezaMundo)).toFixed(3), estrella_px: window.proyecta(...p).map(Math.round) }); window.MEDIDAS.contactos = CONTACTOS; }],
    [KR, () => { marca('toque_regla'); estrella(V(CAJA_A[0], 0.5, CAJA_A[1]), 0.35); }],
    [702, () => { marca('explosion'); paquete.visible = false; onda(CAJA_A[0], CAJA_A[1], 0.4, 5.5, 0.5); mancha(CAJA_A[0], CAJA_A[1], 1.1, 0.5); polvo(CAJA_A[0], 0.4, CAJA_A[1], 16, 2.6); }],
    [726, () => marca('cola_explosion')],
    [K6 - 1, () => marca('regla_golpe')], [K6, () => { contacto('golpe 6', 'tin', 'arma', 'pecho', 0.55, 5); Z.pestana.marca(2); marca('asterisco_tic'); }],
    [814, () => { marca('implosion'); onda(-0.4, -2.9, 3.4, 0.15, 0.5); }], [819, () => onda(-0.4, -2.9, 2.6, 0.15, 0.42, 0.6)], [824, () => onda(-0.4, -2.9, 1.9, 0.15, 0.3, 1.1)],
    [836, () => marca('gotas')], [856, () => marca('escurre')], [858, () => marca('silbido_corto')], [864, () => marca('atrapa')],
    [1, () => { window.MEDIDAS.inicio = { pestana: window.proyecta(E.pestana[0], 3.2, E.pestana[1]), caja_registradora_rota: window.proyecta(E.caja_registradora_rota[0], 0.2, E.caja_registradora_rota[1]), grieta: window.proyecta(E.grieta[0], 0, E.grieta[1]), monitor: window.proyecta(E.pila[0], 2.0, E.pila[1]) }; }],
    [590, () => { window.MEDIDAS.telescopio_px = window.proyecta(TEL[0], 0.1, TEL[1]).map(Math.round); }],
    [K6 + 3, () => { window.MEDIDAS.pestana_px = window.proyecta(E.pestana[0], 3.2, E.pestana[1]).map(Math.round); }],
  ];
  HECHOS.sort((a, b) => a[0] - b[0]);
  anima(100, 106, u => { Z.pila.torres[2].rotation.z = 0.12 * EASE.out(u); Z.pila.monitor.rotation.z = 0.2 * EASE.out(u); });                 // golpe 1: la torre de arriba se descuadra; el monitor se inclina
  anima(262, 272, u => { const t = Z.pila.torres[2]; t.position.set(-0.9 * EASE.in(u), 1.25 - 1.0 * EASE.in(u), 0.35 * u); t.rotation.z = 0.12 + 1.45 * EASE.in(u); });   // la torre que cede
  anima(344, 352, u => { Z.farol.grupo.rotation.z = 0.14 * EASE.back(u); });                                                                    // farol torcido 8°
  let hechoAnim = new Set();
  function cadaCuadro(f) {
    for (const [i, [f0, f1, fn]] of animados.entries()) { if (f >= f0 && f <= f1) fn(entre(f, f0, f1)); else if (f > f1 && !hechoAnim.has(i)) { fn(1); hechoAnim.add(i); } }
    if (paquete.visible) { const u = EASE.out(entre(f, 612, 641)); paquete.position.set(lerp(CAJA_DE[0], CAJA_A[0], u), 0.23, lerp(CAJA_DE[1], CAJA_A[1], u)); }
    telescopio.visible = f >= 576;
    if (telescopio.visible) { const u = entre(f, 576, 587), r = entre(f, 588, 595); telescopio.position.set(TEL[0], f < 588 ? lerp(7.5, 0.08, EASE.in(u)) : 0.08 + 0.35 * Math.sin(Math.PI * r) * (1 - r), TEL[1]); telescopio.rotation.z = f < 595 ? (f - 576) * 0.5 : 0.2; }
  }

  // ------------------------------------------------------------ cámara: 25 planos, 24 cortes (3.2). c(a qué punto del suelo mira, distancia, {altura, diagonal…})
  const FOV = 46, BASE = { ty: 0, h: 3.2, az: 0, yP: 1330, fov: FOV };
  const c = (t, Dd, o = {}) => ({ ...BASE, t, D: Dd, ...o });
  const PL = (f0, nombre, ...claves) => ({ f0, nombre, claves });
  // encuadra: plano fijo que contiene a `quienes` durante [f0, f1]; mira al punto del suelo más cercano a la cámara (que cae en
  // y = 1340) y se aleja lo justo para que quepan con margen. Anota si un tercero visible queda dentro del ancho del cuadro.
  const TODOS = ['tin', 'tan', 'duda'], TERCEROS = [];
  const encuadra = (nombre, f0, f1, quienes, o = {}) => {
    const fov = o.fov || FOV, a = (o.az || 0) * Math.PI / 180, r = [Math.cos(a), -Math.sin(a)], w = [Math.sin(a), Math.cos(a)], foco = 960 / Math.tan(fov * Math.PI / 360);
    let lo = 1e9, hi = -1e9, fr = -1e9;
    for (let f = f0; f <= f1; f++) for (const q of quienes) { const p = B.posEn(q, f); if (!p) continue; const lat = p[0] * r[0] + p[2] * r[1], dep = p[0] * w[0] + p[2] * w[1]; lo = Math.min(lo, lat); hi = Math.max(hi, lat); if (p[1] < 0.3) fr = Math.max(fr, dep); }
    const cl = (lo + hi) / 2, Dd = Math.max(o.min || 7.4, (hi - lo + (o.margen || 1.7)) * foco / 1080), medio = Dd * 540 / foco;
    for (let f = f0; f <= f1; f += 2) for (const q of TODOS) if (!quienes.includes(q)) { const v = G[q].visible.filter(k => k[0] <= f).pop(), p = B.posEn(q, f); if (v && v[1] && p && Math.abs(p[0] * r[0] + p[2] * r[1] - cl) < medio + 0.45) { TERCEROS.push(`${nombre}: ${q} dentro del cuadro en f${f}`); break; } }
    return PL(f0, nombre, [f0, c([cl * r[0] + fr * w[0], cl * r[1] + fr * w[1]], Dd, { h: 3.2 + Math.max(0, Dd - 8) * 0.12, yP: 1340, ...o })]);
  };
  const PLANOS = [
    encuadra('P02 nace el rival', 30, 45, TODOS, { az: -20 }),
    encuadra('P03 el rival crece', 46, 75, TODOS, { az: -12 }),
    encuadra('P04 golpe 1', 76, 99, ['tin', 'duda'], { az: 16 }),
    PL(100, 'P05 impacto pila', [100, c([0.5, -3.4], 5.2, { az: -18, h: 2.2, ty: 1.0, yP: 1080 })]),
    encuadra('P06 golpe 2', 118, 143, ['tan', 'duda'], { az: -14 }),
    encuadra('P07 contraataque', 144, 185, ['tin', 'duda'], { az: 8 }),
    encuadra('P08 golpe 3', 186, 229, ['tin', 'duda'], { az: 20 }),
    encuadra('P09 general', 230, 295, TODOS, { az: -6 }),
    PL(296, 'P10 detalle del lápiz', [296, c([1.5, C2], 3.5, { az: 6, h: 1.6, ty: 1.2, yP: 1000, fov: 40 })], [329, c([1.55, C2], 3.4, { az: 5, h: 1.6, ty: 1.2, yP: 1000, fov: 40 })]),
    encuadra('P11 golpe 4', 330, 343, ['tin', 'duda'], { az: -12 }),
    PL(344, 'P12 chispas del farol', [344, c([-3.0, -4.2], 6.4, { az: 8, h: 2.6, ty: 1.4, yP: 1100, fov: 50 })]),
    encuadra('P13 general', 374, 437, ['tin', 'duda'], { az: -10 }),
    PL(438, 'P14 héroe de los dos', [438, c([1.65, -1.5], 6.2, { az: 10, h: 2.4, ty: 0.6, yP: 1250 })], [471, c([1.7, -1.5], 6.1, { az: 9, h: 2.4, ty: 0.6, yP: 1250 })]),
    encuadra('P15 golpe 5', 472, 499, ['tan', 'duda'], { az: 22 }),
    encuadra('P16 general', 500, 553, TODOS, { az: -6 }),
    encuadra('P17 respiro y objeto que cae', 554, 599, TODOS, { az: 6, fov: 52 }),
    PL(600, 'P18 el paquete', [600, c([-0.8, -3.1], 8.6, { az: 14, h: 3.2 })]),
    encuadra('P19 bloqueo', 646, 677, TODOS, { az: 30 }),
    PL(678, 'P20 detalle del paquete', [678, c([0.6, -2.8], 3.6, { az: 10, h: 1.2, ty: 0.4, yP: 1100, fov: 34 })]),
    PL(700, 'P21 pico', [700, c([0.4, -2.8], 12.6, { az: 0, h: 3.8, fov: 56 })]),
    encuadra('P22 revelado', 733, 799, TODOS, { az: -6, fov: 50 }),
    encuadra('P23 golpe 6', 800, 836, ['tin', 'duda'], { az: -16, fov: 52 }),
    encuadra('P24 remate', 837, 899, ['tin', 'tan'], { az: 8, fov: 50 }),
  ];
  window.MEDIDAS.terceros = TERCEROS; if (TERCEROS.length) console.warn('TERCEROS EN CUADRO: ' + TERCEROS.join(' | '));
  const PO = T.portada;
  function camaraDe(f, cam) {
    if (f < 30 || f >= CIERRE) { if (cam.fov !== 36) { cam.fov = 36; cam.updateProjectionMatrix(); } cam.position.set(PO.cx, PO.h, PO.z + PO.D); cam.lookAt(PO.cx, PO.h, PO.z); return; }
    let p = PLANOS[0]; for (const q of PLANOS) if (f >= q.f0) p = q;
    const v = pista(p.claves, f), a = v.az * Math.PI / 180, foco = (m.H / 2) / Math.tan(v.fov * Math.PI / 360);
    if (Math.abs(cam.fov - v.fov) > 1e-6) { cam.fov = v.fov; cam.updateProjectionMatrix(); }
    const baja = Math.atan2(v.h - v.ty, v.D) - Math.atan((v.yP - m.H / 2) / foco);
    cam.position.set(v.t[0] + Math.sin(a) * v.D, v.h, v.t[1] + Math.cos(a) * v.D);
    cam.lookAt(v.t[0], v.h - v.D * Math.tan(baja), v.t[1]);
  }
  window.MEDIDAS.planos = PLANOS.map(p => ({ f0: p.f0, nombre: p.nombre }));

  // control del guion: ninguna clave cruzada ni repetida
  const cruces = [];
  for (const q of ['tin', 'tan', 'duda']) for (const k of ['pos', 'pose', 'escala']) { const t = G[q][k]; for (let i = 1; i < t.length; i++) if (t[i][0] <= t[i - 1][0]) cruces.push(`${q}.${k}: f${t[i - 1][0]} y f${t[i][0]}`); }
  for (const p of PLANOS) for (let i = 1; i < p.claves.length; i++) if (p.claves[i][0] <= p.claves[i - 1][0]) cruces.push(`cámara ${p.nombre}: f${p.claves[i][0]}`);
  for (let i = 1; i < PLANOS.length; i++) if (PLANOS[i].f0 <= PLANOS[i - 1].f0) cruces.push(`planos ${PLANOS[i - 1].nombre} y ${PLANOS[i].nombre}`);
  window.MEDIDAS.claves_cruzadas = cruces;
  if (cruces.length) console.error('CLAVES CRUZADAS: ' + cruces.join(' | '));

  const vivo = B.reposoVivo([K1, K2, K3, K4, K5, KB, KR, K6]);
  const caras = ['duda_0', 'duda_1', 'duda_2', 'duda_3'];
  for (const p of ['tin', 'tan']) for (const e of ['curiosidad', 'sorpresa', 'eureka', 'risa', 'concentrado']) caras.push(`${p}_${e}`);
  return { porFotogramas: true, FIN: N, velocidad: () => 1, reloj: () => 1, G, CAM: null, camara: camaraDe, HECHOS, caras, cadaCuadro, extra, encara: true, pistas: true, borron: 6.5, respira: true, vivo };
}
