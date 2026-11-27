// Guion del short 4 de Tin & Tan (TIN-EN-S-004, «What Is GTA 6, and Is a GTA 7 Coming?»).
// Fuente: proyectos/2026-11-26_tin_y_tan_what_is_gta_6/02_prompt/direccion.md y prompt.md.
// Los fotogramas salen de la voz real: guiones/tin_en_s_004.tiempos.json (lo escribe codigo/tiempos.py del proyecto).
// Versión 3 (2026-11-26): coreografía, contactos y cámaras rehechos por las revisiones de animación, fotografía y
// continuidad de la v2 (07_revision/revision_v2_*.md). Reloj por fotogramas (S = fotograma). Sin temblor: cortes. Los planos de firma (portada) se graban sin personajes:
// Tin, Tan, el lápiz bumerán, los datos y los subtítulos los pone codigo/componer.py encima, con la firma del canal.
// Reglas que este guion respeta: el rival nunca alcanza a Tin ni a Tan; nada rojo sobre el rival (lo que salta es
// tinta); ningún rótulo ni marca en el mundo; fuego plano de dos tonos; humo con contorno; el daño se queda.
export const FICHA = { id: 'tin_en_s_004', entorno: 'tienda_de_videojuegos', paleta: 'c_alto_voltaje', creado: '2026-11-26' };

export async function guion(m) {
  const { THREE, P, V, C, EASE, clamp, ra, pista, marca, grieta, mancha, trazoSuelo, onda, soltar, estrella, trozos, entorno, personajes, escena, caja, lienzo, FPS } = m;
  window.MEDIDAS = window.MEDIDAS || {};
  const T = await (await fetch('guiones/tin_en_s_004.tiempos.json')).json();
  const K = T.K, N = T.N, L = {}; for (const l of T.lineas) L[l.id] = l;
  const { tin, tan, duda } = personajes, Z = entorno.piezas;
  const { K1, K2, K3, KB, K4, K5, KR, K6 } = K;
  const lerp = (a, b, u) => a + (b - a) * u, entre = (f, a, b) => clamp((f - a) / (b - a));

  // ------------------------------------------------------------ poses nuevas (entran al catálogo)
  const A = (pose, ang) => ({ ...pose, armaAng: ang });
  Object.assign(P, {
    gancho: { t: 20, aF: [122, 148], aB: [40, 120], lF: [30, 0], lB: [-36, -14], c: -14 },
    bloqueo: { t: -8, aF: [74, 150], aB: [44, 132], lF: [28, 4], lB: [-30, -10], c: 0, armaAng: 176 },
    dibuja: { t: 6, aF: [58, 112], aB: [84, 96], lF: [14, 4], lB: [-14, -4], c: 8, armaAng: 150 },
    pregunta: { t: 0, aF: [58, 152], aB: [-10, -5], lF: [8, 4], lB: [-8, -4], c: -10 },
    invita: { t: 2, aF: [104, 168], aB: [-22, -8], lF: [10, 4], lB: [-10, -4], c: -4 },
    mazoArriba: { t: -10, aF: [158, 184], aB: [150, 172], lF: [22, 0], lB: [-30, -10], c: -8, armaAng: 196 },
    mazoAbajo: { t: 40, aF: [62, 72], aB: [52, 62], lF: [52, -10], lB: [-40, -52], c: 12, armaAng: 78 },
    miraEspada: { t: -4, aF: [84, 166], aB: [20, 60], lF: [14, 4], lB: [-14, -4], c: 22, armaAng: 178 },
    atrapa: { t: 0, aF: [96, 150], aB: [-12, -6], lF: [10, 4], lB: [-10, -4], c: -6 },
  });
  const Gd = A(P.guardia, 150), Cg = A(P.carga, 244), Gp = A(P.golpe, 98), Gr = A(P.golpe, 78);

  // ------------------------------------------------------------ pistas de cada personaje (versión 3: coreografía rehecha)
  // Reglas de puesta en escena de la v3 (revisiones de animación, fotografía y continuidad de la v2):
  //  1. Carriles: cada golpe ocurre con quien pega y quien recibe en el MISMO z; el tercero queda a ≥ 1,1 u en z o fuera de la línea.
  //  2. Las carreras recorren distancia de verdad (≥ 1,8 u, ≥ 4 u/s) y el ciclo de piernas sale de esa distancia (motor: `modo`).
  //     Los ajustes cortos son saltitos de guardia, nunca «correr en el sitio».
  //  3. El rival nunca pasa por encima ni a través de Tin o de Tan: lo esquivan (salto, agachada) o lo bloquean.
  //  4. Un solo cruce de Tan por delante de Tin, corriendo, en plano general (después del golpe 4).
  const nueva = () => ({ pos: [], pose: [], mira: [], cara: [], escala: [], visible: [], modo: [[0, null]] });
  const G = { tin: nueva(), tan: nueva(), duda: nueva() };
  const pos = (q, ...ks) => G[q].pos.push(...ks), pose = (q, ...ks) => G[q].pose.push(...ks);
  const corre = (q, f0, f1, modo = 'corre') => G[q].modo.push([f0, modo], [f1, null]);
  // trayecto: recorre una línea quebrada a velocidad pareja, con arranque y frenada de 3 f (una clave por fotograma), y marca el modo
  const trayecto = (q, f0, f1, puntos, modo = 'corre') => {
    const largos = puntos.slice(1).map((b, i) => Math.hypot(b[0] - puntos[i][0], b[2] - puntos[i][2])), total = largos.reduce((a, b) => a + b, 0), n = f1 - f0, r = Math.min(3, n / 3) / n;
    const avance = u => { const v = 1 / (1 - r); return u < r ? v * u * u / (2 * r) : u > 1 - r ? 1 - v * (1 - u) * (1 - u) / (2 * r) : v * (u - r / 2); };
    for (let f = f0; f <= f1; f++) { let d = avance((f - f0) / n) * total, i = 0; while (i < largos.length - 1 && d > largos[i]) { d -= largos[i]; i++; } const u = largos[i] ? Math.min(1, d / largos[i]) : 0, a = puntos[i], b = puntos[i + 1]; G[q].pos.push([f, [lerp(a[0], b[0], u), 0, lerp(a[2], b[2], u)], 'lin']); }
    if (modo) corre(q, f0, f1, modo);
  };
  // golpe con la gramática medida: anticipación K−12 a K−7, pausa K−6 a K−1 (pose quieta), contacto K y K+1, recuperación
  const ataque = (q, k, antes, carga, golpe, despues, sostiene = 5) => pose(q, [k - 13, antes], [k - 7, carga, 'out'], [k - 1, carga], [k, golpe, 'salto'], [k + sostiene, golpe], [k + sostiene + 6, despues]);
  Object.assign(P, { punio: { t: 14, aF: [90, 90], aB: [-25, 80], lF: [44, 0], lB: [-44, -24], c: 2 }, esquiva: { t: -22, aF: [60, 140], aB: [30, 120], lF: [52, -18], lB: [-28, -82], c: -10 }, susto: { t: -12, aF: [70, 150], aB: [40, 140], lF: [20, 4], lB: [-22, -6], c: -8 }, sentado: { t: -36, aF: [-40, 20], aB: [-70, -20], lF: [82, 22], lB: [70, 10], c: 10 }, explica: { t: 6, aF: [55, 150], aB: [70, 160], lF: [12, 4], lB: [-12, -4], c: -4, armaAng: 150 } });

  const CIERRE = K.cierre, RECOMPONE = KR + 86, ESC = { e15: 1.15, e14: 1.08, e125: 0.96, e11: 0.85, e10: 0.77, e09: 0.69, e08: 0.62 };
  const ZN = -1.0, ZM = -2.7, ZF = -5.9;                      // carriles: cerca, medio (delante del mostrador) y fondo (pasillo del televisor)
  const AST = [0, -5.1], GRIETA_SALIDA = [0.95, -5.1], CAJA_ROTA = [-1.79, -4.24];
  const CORRE_TAN = [K4 + 3, K4 + 21], CARGA = [K.carrera - 10, K.carrera + 9];     // el cruce de Tan y la carrera de los dos al remate

  // --- Tan
  G.tan.visible.push([0, false], [30, true], [CIERRE, false]);
  G.tan.mira.push([0, 1], [CARGA[1], -1]);
  G.tan.cara.push([0, 'sorpresa'], [K2 - 13, 'concentrado'], [K2, 'eureka'], [K2 + 26, 'curiosidad'], [L.C.f0, 'risa'], [L.C.f1 + 2, 'curiosidad'], [KB, 'sorpresa'], [K4 + 3, 'concentrado'], [K5, 'eureka'], [K5 + 20, 'concentrado'], [KR, 'eureka'], [K.invertidos, 'sorpresa'], [L.B.f0, 'curiosidad'], [K6, 'sorpresa'], [K.asterisco, 'curiosidad'], [K.lapiz_a_tan + 6, 'risa']);
  pos('tan', [30, [-1.7, 0, ZN]], [54, [-1.7, 0, ZN]], [60, [-1.8, 0.14, ZN], 'out'], [66, [-1.9, 0, ZN], 'in'], [K2 - 22, [-1.9, 0, ZN]], [K2 - 18, [-1.67, 0.12, ZN], 'out'], [K2 - 14, [-1.45, 0, ZN], 'in'], [K2 - 1, [-1.45, 0, ZN]], [K2, [-1.3, 0, ZN], 'salto'], [K2 + 11, [-1.4, 0, ZN]],
    [K3 - 12, [-1.4, 0, ZN]], [K3 - 11, [-1.3, 0, -1.5], 'salto'],                                  // fuera de cuadro (plano del mostrador): se acomoda
    [K5 - 7, [0.84, 0, -2.5], 'out'], [K5 - 1, [0.84, 0, -2.5]], [K5, [1.02, 0, -2.5], 'salto'], [K5 + 14, [0.9, 0, -2.5]],
    [KR - 7, [1.57, 0, ZF], 'out'], [KR - 1, [1.57, 0, ZF]], [KR, [1.42, 0, ZF], 'salto'], [KR + 12, [1.5, 0, ZF]],
    [K.radiales - 1, [1.5, 0, ZF]], [K.radiales + 12, [1.55, 0, -4.7], 'out'], [N, [1.55, 0, -4.7]]);
  trayecto('tan', CORRE_TAN[0], CORRE_TAN[1], [[-1.3, 0, -1.5], [0.4, 0, -1.5], [0.9, 0, -2.5]]);
  trayecto('tan', CARGA[0], CARGA[1], [[0.9, 0, -2.5], [1.45, 0, ZF]], 'corre_arma');
  pose('tan', [30, P.guardia], [52, P.guardia], [58, P.susto, 'out'], [70, P.guardia], [K2 - 30, P.guardia]);
  ataque('tan', K2, P.guardia, P.carga, P.patada, P.guardia);
  pose('tan', [K2 + 14, P.festeja, 'back'], [K2 + 22, P.festeja], [K2 + 30, P.guardia], [K3 + 26, P.guardia], [K3 + 34, P.festeja, 'back'], [K3 + 44, P.festeja], [K3 + 52, P.guardia],
    [K.dibuja_baston + 18, P.guardia], [K.dibuja_baston + 26, P.pregunta, 'back'], [K.dibuja_baston + 40, P.pregunta], [L.C.f0 - 6, P.guardia], [L.C.f0 + 2, P.invita, 'back'], [L.C.f1 - 8, P.invita], [L.C.f1 - 2, P.guardia], [KB + 2, P.susto, 'out'], [KB + 14, P.guardia], [CORRE_TAN[0], P.guardia]);
  pose('tan', [CORRE_TAN[1] + 1, P.guardia], [K5 - 14, P.atrapa, 'out']);
  ataque('tan', K5, A(P.atrapa, 170), P.mazoArriba, P.mazoAbajo, A(P.guardia, 150), 9);
  pose('tan', [K5 + 26, Gd], [K5 + 34, A(P.festeja, 170), 'back'], [K5 + 42, Gd], [CARGA[0], Gd]);
  ataque('tan', KR, Gd, Cg, Gr, Gd);
  pose('tan', [K.radiales - 1, Gd], [K.radiales, A(P.resbala, 150), 'salto'], [K.radiales + 12, A(P.agachado, 120)], [K.radiales + 26, A(P.agachado, 120)], [K.radiales + 38, A(P.susto, 150)], [K.radiales + 54, Gd], [L.T9.f0 + 60, Gd], [L.T9.f0 + 68, A(P.susto, 150), 'out'], [L.T9.f0 + 80, A(P.susto, 150)], [L.T9.f0 + 90, Gd],
    [L.B.f0 - 4, Gd], [L.B.f0 + 4, A(P.pregunta, 150), 'back'], [L.B.f1 - 8, A(P.pregunta, 150)], [K6 - 3, Gd], [K6 + 3, A(P.recibe, 150), 'out'], [K6 + 20, Gd], [K.armas_gotas + 9, P.guardia], [K.asterisco + 8, P.quieto],
    [K.lapiz_a_tan + 1, P.quieto], [K.lapiz_a_tan + 5, P.atrapa, 'out'], [N, P.atrapa]);

  // --- Tin
  G.tin.visible.push([0, false], [30, true], [CIERRE, false]);
  G.tin.mira.push([0, -1], [K2 + 10, 1], [CARGA[1], 1]);
  G.tin.cara.push([0, 'curiosidad'], [K1 - 13, 'concentrado'], [K1 + 2, 'eureka'], [K1 + 40, 'curiosidad'], [K2 + 2, 'sorpresa'], [K2 + 20, 'curiosidad'], [K.rival_ataca - 6, 'sorpresa'], [K3 - 13, 'concentrado'], [K3 + 2, 'eureka'], [K3 + 60, 'curiosidad'], [K.dibuja_baston, 'concentrado'], [L.T5.f1, 'curiosidad'],
    [KB - 6, 'concentrado'], [K4 + 2, 'eureka'], [K4 + 30, 'concentrado'], [K5 + 2, 'curiosidad'], [K5 + 6, 'sorpresa'], [K5 + 20, 'concentrado'], [KR, 'eureka'], [K.invertidos, 'sorpresa'], [L.T9.f0 + 4, 'eureka'], [L.T9.f1, 'curiosidad'], [K6 - 13, 'concentrado'], [K6 + 2, 'curiosidad']);
  pos('tin', [30, [1.75, 0, ZN]], [52, [1.75, 0, ZN]], [55, [1.66, 0.16, ZN], 'out'], [58, [1.57, 0, ZN], 'in'], [60, [1.57, 0, ZN]], [63, [1.48, 0.14, ZN], 'out'], [66, [1.4, 0, ZN], 'in'], [K1 - 13, [1.4, 0, ZN]], [K1 - 7, [1.52, 0, ZN], 'out'], [K1 - 1, [1.52, 0, ZN]], [K1, [0.6, 0, ZN], 'salto'], [K1 + 11, [1.05, 0, ZN]],
    [K2 + 4, [1.05, 0, ZN]], [K2 + 9, [1.0, 0.72, ZN], 'out'], [K2 + 14, [0.95, 0, ZN], 'in'],                                 // salta por encima del rival que resbala
    [K.cartel - 9, [0.95, 0, ZN]], [K.cartel - 5, [0.9, 0.1, ZN], 'out'], [K.cartel - 1, [0.85, 0, ZN], 'in'], [K.rival_ataca - 3, [0.85, 0, ZN]], [K.rival_ataca, [0.7, 0, ZN], 'out'], [K.rival_ataca + 12, [0.85, 0, ZN]], [K.salto_mostrador + 1, [0.85, 0, ZN]],
    [K3 - 7, [1.78, 0, -2.88], 'out'], [K3 - 1, [1.78, 0, -2.88]], [K3, [1.9, 0.3, -2.88], 'salto'], [K3 + 6, [1.9, 0, -2.88], 'in'],
    // tres saltitos hacia atrás, de guardia, para tomar distancia (antes: «corría» 50 f sin avanzar)
    [K3 + 62, [1.9, 0, -2.88]], [K3 + 66, [1.63, 0.3, -2.85], 'out'], [K3 + 70, [1.37, 0, -2.82], 'in'], [K3 + 73, [1.37, 0, -2.82]], [K3 + 77, [1.1, 0.3, -2.79], 'out'], [K3 + 81, [0.83, 0, -2.76], 'in'], [K3 + 84, [0.83, 0, -2.76]], [K3 + 88, [0.57, 0.3, -2.73], 'out'], [K3 + 92, [0.3, 0, ZM], 'in'],
    [KB - 1, [0.3, 0, ZM]], [KB, [0.22, 0, ZM], 'salto'], [K4 - 13, [0.25, 0, ZM]], [K4 - 7, [0.18, 0, ZM], 'out'], [K4 - 1, [0.18, 0, ZM]], [K4, [0.55, 0, ZM], 'salto'], [K4 + 6, [0.45, 0, ZM]], [K4 + 10, [-0.1, 0.22, ZM], 'lin'], [K4 + 14, [-0.75, 0, ZM], 'lin'],
    [KR - 7, [-1.57, 0, ZF], 'out'], [KR - 1, [-1.57, 0, ZF]], [KR, [-1.42, 0, ZF], 'salto'], [KR + 12, [-1.5, 0, ZF]],
    [K.radiales - 1, [-1.5, 0, ZF]], [K.radiales + 12, [-1.45, 0, AST[1]], 'out'], [K6 - 13, [-1.45, 0, AST[1]]], [K6 - 7, [-1.62, 0, AST[1]], 'out'], [K6 - 1, [-1.62, 0, AST[1]]], [K6, [-1.5, 0, AST[1]], 'salto'], [K6 + 11, [-1.45, 0, AST[1]]], [N, [-1.45, 0, AST[1]]]);
  pose('tin', [30, P.guardia], [53, P.guardia]);
  pose('tin', [54, P.agachado, 'out'], [57, P.guardia], [60, P.agachado, 'in'], [63, P.guardia], [66, P.agachado, 'in'], [68, P.guardia]);
  ataque('tin', K1, P.guardia, P.carga, P.punio, P.guardia);      // puño con el cuerpo más erguido: la cabeza de Tin queda lejos del impacto
  pose('tin', [K2 - 4, P.guardia], [K2 + 2, P.agachado, 'out'], [K2 + 4, P.agachado], [K2 + 7, P.recogido, 'out'], [K2 + 11, P.recogido], [K2 + 14, P.agachado, 'in'], [K2 + 17, P.agachado], [K2 + 24, P.guardia],
    [K.rival_ataca - 5, P.guardia], [K.rival_ataca - 2, P.esquiva, 'out'], [K.rival_ataca + 6, P.esquiva], [K.rival_ataca + 12, P.guardia], [K.salto_mostrador + 1, P.guardia]);
  trayecto('tin', K.salto_mostrador + 2, K.salto_mostrador + 15, [[0.85, 0, ZN], [1.85, 0, -2.88]]);
  pose('tin', [K.salto_mostrador + 16, P.guardia]);
  ataque('tin', K3, P.guardia, P.agachado, P.gancho, P.guardia, 8);
  pose('tin', [K3 + 30, P.guardia], [K3 + 38, P.festeja, 'back'], [K3 + 46, P.festeja], [K3 + 54, P.guardia], [K3 + 61, P.guardia]);
  for (const k of [K3 + 62, K3 + 73, K3 + 84]) pose('tin', [k + 1, P.agachado, 'out'], [k + 4, P.guardia], [k + 8, P.agachado, 'in'], [k + 10, P.guardia]);
  pose('tin', [K.dibuja_baston - 4, P.dibuja], [K.dibuja_baston + 14, P.dibuja], [K.dibuja_baston + 20, Gd], [K.dibuja_baston + 34, P.explica], [K.dibuja_baston + 48, Gd], [KB - 10, Gd], [KB - 3, P.bloqueo, 'out'], [KB + 6, P.bloqueo], [K4 - 14, Gd]);
  ataque('tin', K4, Gd, Cg, Gp, Gd);
  pose('tin', [K.mazo - 2, Gd], [K.mazo, A(P.poder, 180)], [K.mazo + 7, A(P.poder, 180)], [K.mazo + 8, A(P.carga, 240)], [K.mazo + 10, P.golpe, 'in'], [K.mazo + 16, P.guardia], [K5 + 3, P.guardia], [K5 + 6, P.agachado, 'out'], [K5 + 13, P.agachado], [K5 + 19, P.guardia], [K5 + 22, P.dibuja], [K5 + 34, P.dibuja], [K5 + 36, Gd], [CARGA[0], Gd]);
  trayecto('tin', CARGA[0], CARGA[1], [[-0.75, 0, ZM], [-1.45, 0, ZF]], 'corre_arma');
  ataque('tin', KR, Gd, Cg, Gr, Gd);
  pose('tin', [K.radiales - 1, Gd], [K.radiales, A(P.resbala, 150), 'salto'], [K.radiales + 12, A(P.agachado, 120)], [K.radiales + 26, A(P.agachado, 120)], [K.radiales + 36, A(P.susto, 150)], [K.radiales + 50, Gd], [L.T9.f0 + 36, Gd], [L.T9.f0 + 44, P.explica, 'back'], [L.T9.f1 - 8, P.explica], [L.T9.f1, Gd], [K6 - 14, Gd]);
  ataque('tin', K6, Gd, Cg, Gp, Gd);
  pose('tin', [K6 + 30, A(P.quieto, 60)], [K.armas_gotas + 10, P.quieto], [K.lapiz_a_tan - 3, P.quieto], [K.lapiz_a_tan - 1, P.carga], [K.lapiz_a_tan + 2, P.golpe, 'in'], [K.lapiz_a_tan + 8, P.quieto], [N, P.quieto]);

  // --- el rival (@duda): aparece con la pregunta, grande; baja un escalón de tamaño con cada dato; nunca muere
  const D = G.duda;
  D.visible.push([0, false], [30, true], [K.invertidos, false], [RECOMPONE, true], [K.asterisco + 6, false]);
  D.mira.push([0, -1], [66, 1], [K2 + 44, -1]);
  D.cara.push([0, 'duda']);
  D.escala.push([30, ESC.e125], [45, ESC.e125], [66, ESC.e15, 'back'], [K1 + 26, ESC.e15], [K1 + 42, ESC.e14], [K2 + 46, ESC.e14], [K2 + 66, ESC.e125], [K3 + 30, ESC.e125], [K3 + 50, ESC.e11], [K4 + 14, ESC.e11], [K4 + 24, ESC.e10],
    [K5, ESC.e10], [K5 + 14, ESC.e09], [KR + 20, ESC.e09], [RECOMPONE, ESC.e08], [K6 + 1, ESC.e08], [K.implosion_fin, 0.1, 'in'], [N, 0.1]);
  const CARGA_RIVAL = [K2 - 23, K2 - 1];
  pos('duda', [30, [0.1, 0, ZN]], [K1 + 1, [0.1, 0, ZN]], [K1 + 2, [-0.2, 0.15, ZN - 0.1], 'salto'], [K1 + 6, [-0.9, 1.3, -2.4], 'out'], [K1 + 17, [-2.3, 1.5, -5.9], 'out'], [K1 + 19, [-2.35, 1.3, -6.0]], [K1 + 26, [-1.9, 0, -5.4], 'in'],
    [K2 + 1, [-0.65, 0, ZN]], [K2 + 2, [-0.35, 0, ZN + 0.05], 'salto'], [K2 + 6, [0.75, 0, -0.8], 'out'], [K2 + 17, [2.6, 0, -0.4], 'out'],
    [K.rival_ataca - 1, [2.6, 0, -0.4]], [K.rival_ataca, [2.42, 0, -0.4], 'salto'], [K.rival_ataca + 8, [2.5, 0, -0.4]],
    [K.salto_mostrador, [2.5, 0, -0.4]], [K.salto_mostrador + 7, [2.3, 1.55, -1.9], 'out'], [K.salto_mostrador + 14, [2.2, 1.0, -3.03], 'in'], [K3 + 1, [2.2, 1.0, -3.03]], [K3 + 2, [2.25, 1.3, -3.03], 'salto'], [K3 + 12, [2.75, 2.4, -3.3], 'out'],
    [K3 + 22, [3.1, 1.0, -3.35], 'in'], [L.C.f0 + 17, [3.1, 1.0, -3.35]], [L.C.f0 + 23, [2.5, 2.0, -3.0], 'out'], [L.C.f0 + 30, [1.75, 0, ZM], 'in'],
    [KB - 13, [1.75, 0, ZM]], [KB - 7, [1.95, 0, ZM], 'out'], [KB - 1, [1.95, 0, ZM]], [KB, [1.7, 0, ZM], 'salto'], [KB + 8, [1.85, 0, ZM]], [K4 - 6, [1.95, 0, ZM]], [K4 + 1, [1.95, 0, ZM]],
    [K4 + 2, [2.1, 0.15, ZM], 'salto'], [K4 + 5, [2.35, 1.3, -3.9], 'out'], [K4 + 12, [2.5, 1.7, -5.7], 'out'], [K4 + 14, [2.45, 1.6, -5.5]], [K4 + 19, [2.75, 2.5, -3.9], 'out'], [K4 + 24, [2.9, 0, -2.5], 'in'],
    [K5 + 16, [2.9, 0, -2.5]], [K5 + 26, [1.5, 2.4, -4.4], 'out'], [K5 + 36, [0, 0, ZF], 'in'], [KR + 1, [0, 0, ZF]], [KR + 2, [0, 0.2, ZF - 0.1], 'salto'], [KR + 6, [0, 1.3, -6.4], 'out'], [KR + 20, [0, 2.2, -6.95], 'out'],
    [RECOMPONE, [AST[0], 0, AST[1]], 'salto'], [K6 + 2, [AST[0], 0, AST[1]]], [K.implosion_fin, [AST[0], 0.35, AST[1]]], [K.implosion_fin + 6, [AST[0], 0, AST[1]], 'in'], [N, [AST[0], 0, AST[1]]]);
  pose('duda', [30, P.quieto], [46, P.quieto], [54, P.poder, 'back'], [57, P.poder], [60, P.pisoton, 'in'], [66, P.guardia], [K1 - 1, P.guardia], [K1, P.recibe, 'salto'], [K1 + 3, P.vuela], [K1 + 19, P.vuela], [K1 + 26, P.caido], [K1 + 34, P.caido], [K1 + 42, P.sentado], [K1 + 50, P.agachado], [CARGA_RIVAL[0] - 1, P.guardia]);
  trayecto('duda', CARGA_RIVAL[0], CARGA_RIVAL[1], [[-1.9, 0, -5.4], [-0.65, 0, ZN]]);
  pose('duda', [K2 - 1, P.guardia], [K2, P.recibe, 'salto'], [K2 + 2, P.recibe], [K2 + 6, P.caido, 'out'], [K2 + 44, P.caido], [K2 + 54, P.sentado], [K2 + 64, P.agachado], [K2 + 72, P.guardia]);
  pose('duda', [K.cartel - 6, P.guardia], [K.cartel, P.carga, 'in'], [K.rival_ataca - 1, P.carga], [K.rival_ataca, P.golpe, 'salto'], [K.rival_ataca + 6, P.golpe], [K.rival_ataca + 12, P.guardia], [K.salto_mostrador - 3, P.agachado], [K.salto_mostrador + 4, P.recogido], [K.salto_mostrador + 11, P.recogido], [K.salto_mostrador + 14, P.agachado], [K.salto_mostrador + 22, P.agachado],
    [K3 - 1, P.agachado], [K3, P.recibe, 'salto'], [K3 + 4, P.vuela], [K3 + 21, P.vuela], [K3 + 23, P.caido], [K3 + 44, P.caido], [K3 + 54, P.sentado], [K3 + 64, P.agachado], [K3 + 74, P.pisoton, 'back'], [K3 + 84, P.pisoton], [K3 + 92, P.recogido], [K3 + 102, P.agachado], [K.dibuja_baston + 14, P.agachado], [K.dibuja_baston + 22, P.pisoton, 'back'], [K.dibuja_baston + 32, P.recogido], [K.dibuja_baston + 42, P.agachado], [L.C.f0 + 15, P.agachado], [L.C.f0 + 21, P.recogido], [L.C.f0 + 28, P.recogido], [L.C.f0 + 30, P.agachado], [K.dibuja_espada + 6, A(P.poder, 185), 'back'], [K.dibuja_espada + 14, A(P.poder, 185)], [KB - 14, Gd]);
  ataque('duda', KB, Gd, Cg, Gp, P.miraEspada, 3);
  pose('duda', [K4 - 1, P.miraEspada], [K4, P.recibe, 'salto'], [K4 + 4, P.vuela], [K4 + 14, P.vuela], [K4 + 19, P.recogido], [K4 + 23, P.recogido], [K4 + 25, P.agachado], [K4 + 29, P.guardia], [K4 + 33, P.poder, 'back'], [K5 - 1, P.poder],
    [K5, P.agachado, 'salto'], [K5 + 14, P.agachado], [K5 + 18, P.recogido], [K5 + 34, P.recogido], [K5 + 37, P.agachado], [K5 + 46, P.guardia], [K5 + 52, P.poder, 'back'], [K5 + 62, P.poder], [K5 + 70, P.guardia], [KR - 8, P.guardia], [KR - 1, P.guardia], [KR, P.recogido, 'salto'], [KR + 22, P.recogido],
    [RECOMPONE, P.agachado, 'salto'], [RECOMPONE + 22, P.agachado], [RECOMPONE + 32, P.guardia], [RECOMPONE + 40, P.guardia], [RECOMPONE + 48, P.poder, 'back'], [RECOMPONE + 56, P.poder], [RECOMPONE + 64, P.guardia], [K6 - 3, P.guardia], [K6, P.recibe, 'salto'], [K6 + 3, P.recogido], [N, P.recogido]);

  for (const q of ['tin', 'tan', 'duda']) for (const k of ['pos', 'pose', 'mira', 'cara', 'escala', 'visible', 'modo']) { G[q][k].sort((a, b) => a[0] - b[0]); if (!G[q][k].length) G[q][k].push([0, k === 'escala' ? 1 : k === 'visible' ? true : null]); }
  G.tin.escala = [[0, 1]]; G.tan.escala = [[0, 1]];

  // ------------------------------------------------------------ extras por personaje: armas de tinta, lápiz, giro en el aire
  const vueltas = [[K1 + 2, K1 + 18, -5.2], [K3 + 4, K3 + 21, 3.1], [K4 + 4, K4 + 13, 4.4], [KR + 3, KR + 21, 7.0]];
  const MAZO_LANZA = [K.mazo + 10, K.mazo + 14];              // Tin lo suelta y Tan lo atrapa: en esos fotogramas el mazo es solo el que vuela
  function extra(id, f) {
    if (id === 'tin') {
      const x = { lapiz: f < K.lapiz_a_tan };
      if (f >= K.dibuja_baston && f < K.mazo) x.arma = { tipo: 'baston', prog: entre(f, K.dibuja_baston, K.dibuja_baston + 11) };
      else if (f >= K.mazo && f < MAZO_LANZA[0]) x.arma = { tipo: 'mazo', bloque: EASE.back(entre(f, K.mazo, K.mazo + 7)) };
      else if (f >= K5 + 22 && f < K.armas_gotas + 10) x.arma = { tipo: 'baston', prog: f < K.armas_gotas ? entre(f, K5 + 22, K5 + 33) : 1 - entre(f, K.armas_gotas, K.armas_gotas + 9) };
      return x;
    }
    if (id === 'tan') {
      if (f > MAZO_LANZA[1] && f < K.armas_gotas + 10) return { arma: { tipo: 'mazo', prog: 1 - entre(f, K.armas_gotas, K.armas_gotas + 9), bloque: 1 - entre(f, K.armas_gotas, K.armas_gotas + 6) } };
      return null;
    }
    const x = {};
    if (f < 46) x.revela = entre(f, 30, 45);
    if (f >= RECOMPONE && f < RECOMPONE + 22) x.revela = entre(f, RECOMPONE, RECOMPONE + 20);
    if (f >= K.dibuja_espada && f < K4) x.arma = { tipo: 'espada', prog: entre(f, K.dibuja_espada, K.dibuja_espada + 11), rota: f >= KB };
    for (const [a, b, n] of vueltas) if (f >= a && f < b) x.giro = n * EASE.out(entre(f, a, b));
    if (f >= K5 + 30 && f < K.invertidos) x.papel = true;                                              // el rojo de la llama no se ve a través del rival
    if (f >= K5 && f < K5 + 16) x.aplasta = f < K5 + 10 ? 0.85 : 0.85 * (1 - entre(f, K5 + 10, K5 + 16));
    for (const k of [K1 + 26, K2 + 22, K3 + 23, K4 + 24, K5 + 36]) if (f >= k && f < k + 5) x.aplasta = 0.3 * (1 - entre(f, k, k + 5));   // aterriza y se asienta
    if (f > K.implosion_fin && f < K.asterisco) x.giro = Math.sin(f * 2.1) * 0.25;                     // el mechón tiembla
    return x;
  }

  // ------------------------------------------------------------ piezas propias del guion: llamas planas, objetos que vuelan, calcos
  function texDibujo(w, h, pinta) { const t = new THREE.CanvasTexture(lienzo(w, h, pinta)); t.colorSpace = THREE.SRGBColorSpace; return t; }
  let sem = 4004; const az = () => { sem = (sem * 1664525 + 1013904223) >>> 0; return sem / 4294967296; };
  // fuego plano: dos tonos con escalón duro (núcleo casi blanco, borde rojo oscuro); 3 dibujos de 2 f cada uno
  const texLlama = [0, 1, 2].map(() => texDibujo(256, 320, (g) => {
    const lenguas = 5, pts = []; for (let i = 0; i <= lenguas * 2; i++) { const u = i / (lenguas * 2), x = 20 + 216 * u, y = i % 2 ? 300 - (120 + 170 * az()) * Math.sin(Math.PI * (0.15 + 0.7 * u)) : 300 - 50 * Math.sin(Math.PI * u) - 20 * az(); pts.push([x, y]); }
    const forma = (k, col) => { g.fillStyle = col; g.beginPath(); g.moveTo(128 - 108 * k, 306); for (const [x, y] of pts) g.lineTo(128 + (x - 128) * k, 306 + (y - 306) * k); g.lineTo(128 + 108 * k, 306); g.quadraticCurveTo(128, 320, 128 - 108 * k, 306); g.fill(); };
    forma(1, C.fuego_borde); forma(0.6, C.fuego_nucleo);
  }));
  const texEstallido = [0, 1, 2].map(() => texDibujo(512, 512, (g) => {
    const n = 18, r = []; for (let i = 0; i < n; i++) r.push(i % 2 ? 150 + 50 * az() : 215 + 35 * az());
    const forma = (k, col) => { g.fillStyle = col; g.beginPath(); for (let i = 0; i < n; i++) { const a = i / n * 6.2832; g.lineTo(256 + Math.cos(a) * r[i] * k, 256 + Math.sin(a) * r[i] * k); } g.closePath(); g.fill(); };
    forma(1, C.fuego_borde); forma(0.7, C.fuego_nucleo);
  }));
  const deCara = [];                                              // planos sueltos que giran hacia la cámara, como los personajes
  const plano = (tex, w, h, gira = true) => { const o = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ map: tex, transparent: true, alphaTest: 0.5, side: THREE.DoubleSide })); o.visible = false; escena.add(o); if (gira) deCara.push(o); return o; };
  const llamas = [];                                              // {o, x, y, z, tam(f) → alto en u (0 = apagada)}
  const llama = (x, y, z, tam) => { const o = plano(texLlama[0], 1, 1.25); llamas.push({ o, x, y, z, tam }); };
  const TV = [0, 2.3, -7.44];
  // la llama del televisor no se apaga antes de estallar (antes desaparecía un fotograma antes): crece hasta el claro
  const fase = f => f < K.tele_punta + 12 ? 0 : f < K5 + 2 ? 0.9 * EASE.back(entre(f, K.tele_punta + 12, K.tele_punta + 18)) : f < K.tele_choque ? lerp(0.9, 1.9, EASE.back(entre(f, K5 + 2, K5 + 9))) : f < K.bola ? lerp(1.9, 2.6, entre(f, K.tele_choque, K.claro)) : 0;
  llama(TV[0] + 0.25, TV[1] + 0.35, TV[2] + 0.1, fase);
  const resto = (a) => f => (f >= K.enfria && f < K.implosion + a ? 0.55 * (1 - 0.5 * entre(f, K.enfria, K.implosion)) * (1 - entre(f, K.implosion + a - 6, K.implosion + a)) : 0);
  llama(-1.15, 0.0, -7.0, resto(8)); llama(0.95, 0.0, -6.8, resto(12)); llama(0.6, 0.0, -7.6, resto(10));
  const bola = plano(texEstallido[0], 1, 1); bola.renderOrder = 1;
  const anillo = plano(texDibujo(512, 512, (g) => { g.strokeStyle = C.linea; g.lineWidth = 30; g.beginPath(); g.arc(256, 256, 226, 0, 7); g.stroke(); }), 1, 1); anillo.renderOrder = 1;   // anillo de tinta (el acento amarillo no va en el fuego: dirección, 3b)

  // objetos de tinta que vuelan: la punta de la espada, el mazo que Tin le lanza a Tan y el lápiz
  const punta = plano(texDibujo(96, 32, (g) => { g.fillStyle = C.linea; g.beginPath(); g.moveTo(4, 6); g.lineTo(92, 16); g.lineTo(4, 26); g.lineTo(16, 16); g.closePath(); g.fill(); }), 0.6, 0.2);
  const mazoV = plano(texDibujo(256, 96, (g) => { g.strokeStyle = C.linea; g.fillStyle = C.linea; g.lineCap = 'round'; g.lineWidth = 14; g.beginPath(); g.moveTo(14, 48); g.lineTo(190, 48); g.stroke(); g.fillRect(176, 6, 62, 84); }), 1.3, 0.5);
  const lapizV = plano(texDibujo(160, 40, (g) => { g.strokeStyle = C.linea; g.lineWidth = 26; g.beginPath(); g.moveTo(8, 20); g.lineTo(120, 20); g.stroke(); g.strokeStyle = '#E8B33B'; g.lineWidth = 16; g.beginPath(); g.moveTo(26, 20); g.lineTo(118, 20); g.stroke(); g.strokeStyle = '#D9583B'; g.beginPath(); g.moveTo(10, 20); g.lineTo(26, 20); g.stroke(); g.fillStyle = C.linea; g.beginPath(); g.moveTo(118, 6); g.lineTo(154, 20); g.lineTo(118, 34); g.fill(); }), 0.42, 0.105);
  const vuelo = (o, f, f0, f1, a, b, alto, giros) => { if (f < f0 || f > f1 || !a || !b) return false; const u = entre(f, f0, f1); o.visible = true; o.position.set(lerp(a.x, b.x, u), lerp(a.y, b.y, u) + alto * Math.sin(Math.PI * u), lerp(a.z, b.z, u) + 0.05); o.rotation.z = giros * u * 6.2832; return true; };
  // calcos del rival en los lanzamientos (K+2 a K+15): tres copias que se quedan atrás
  const calcos = [0.34, 0.22, 0.12].map(op => { const o = new THREE.Mesh(new THREE.PlaneGeometry(1, 1), new THREE.MeshBasicMaterial({ map: duda.tex, transparent: true, opacity: op, depthWrite: false })); o.visible = false; escena.add(o); return o; });
  const historia = [], LANZA = [K1, K2, K3, K4, KR].map(k => [k + 2, k + 15]);
  // grieta del mostrador (golpe 3) y marca final
  const texGrieta = texDibujo(640, 190, (g) => { g.strokeStyle = C.linea; g.lineWidth = 9; g.lineJoin = 'round'; g.lineCap = 'round'; g.beginPath(); g.moveTo(300, 0); for (const [x, y] of [[322, 40], [296, 78], [330, 120], [306, 150], [318, 190]]) g.lineTo(x, y); g.stroke(); g.lineWidth = 5; g.beginPath(); g.moveTo(322, 40); g.lineTo(370, 58); g.moveTo(296, 78); g.lineTo(250, 96); g.stroke(); });
  const grietaMostrador = plano(texGrieta, 2.4, 0.95, false); grietaMostrador.position.set(3.0, 0.48, -2.98);
  const gotaSuelo = new THREE.Mesh(new THREE.PlaneGeometry(1, 0.07), new THREE.MeshBasicMaterial({ color: C.linea })); gotaSuelo.rotation.x = -Math.PI / 2; gotaSuelo.visible = false; escena.add(gotaSuelo);

  // ------------------------------------------------------------ roturas con nombre (A8: el daño se queda)
  const suelta = (obj, v, w, piso) => { escena.attach(obj); obj.userData = { v: V(...v), w: V(...w), quieto: false, piso }; trozos.push(obj); };
  const tirarCajas = (lista, n, dir) => { let k = 0; for (const c of lista) { if (k >= n) break; if (c.userData.caida) continue; c.userData.caida = true; k++; suelta(c, [dir * ra(0.6, 2.4), ra(0.5, 2.5), ra(-0.6, 1.6)], [ra(-6, 6), ra(-6, 6), ra(-6, 6)], 0.05); } };
  const polvo = (x, y, z, n = 10, d = 1.6) => soltar('polvoC', V(x, y, z), V(0, 0.9, 0), d, n);
  const animados = [];                                             // [f0, f1, fn(u)]
  const anima = (f0, f1, fn) => animados.push([f0, f1, fn]);
  const reg = Z.caja_registradora, regDesde = V(2.55, 1.25, -3.4), regHasta = V(CAJA_ROTA[0], 0.02, CAJA_ROTA[1]);
  // contacto: la estrella y las gotas salen del punto real del golpe (puño, pie o arma de quien pega, contra el cuerpo del rival)
  // en ESTE fotograma, nunca de una coordenada escrita a mano. Se anota la medida para el control.
  const CONTACTOS = [];
  function contacto(nombre, quien, parte, donde = 'pecho', tam = 0.6, n = 6, hacia = 0.75) {
    const a = personajes[quien], g = (parte === 'arma' ? a.armaMundo : parte === 'pie' ? a.pieMundo : a.manoMundo).clone();
    const blanco = (donde === 'cabeza' ? duda.cabezaMundo : donde === 'cadera' ? duda.caderaMundo : duda.pechoMundo).clone();
    const pxU = Math.hypot(...window.proyecta(blanco.x, blanco.y + 1, blanco.z).map((v, i) => v - window.proyecta(blanco.x, blanco.y, blanco.z)[i]));
    const d = Math.hypot(...window.proyecta(g.x, g.y, g.z).map((v, i) => v - window.proyecta(blanco.x, blanco.y, blanco.z)[i])) / pxU, p = d > 0.45 ? g.clone().lerp(blanco, 1 - 0.3 / d) : g.clone().lerp(blanco, hacia);       // sobre el cuerpo del rival
    const cam = m.camara.position.clone().sub(p).setY(0).normalize(); p.addScaledVector(cam, 0.08);
    estrella(p, tam); soltar('gota', p, V(Math.sign(blanco.x - a.caderaMundo.x) * 2.6, 2.2, 0), 2.0, n);
    CONTACTOS.push({ nombre, f: null, quien, parte, golpe_a_rival_u: +d.toFixed(3), dz_u: +Math.abs(G[quien].pos.length && a.malla.position.z - duda.malla.position.z).toFixed(3), estrella_a_cabeza_de_quien_pega_u: +p.distanceTo(a.cabezaMundo).toFixed(3), vector: [+(blanco.x - g.x).toFixed(2), +(blanco.y - g.y).toFixed(2), +(blanco.z - g.z).toFixed(2)],
      estrella_px: window.proyecta(p.x, p.y, p.z).map(Math.round), cabeza_rival_px: window.proyecta(duda.cabezaMundo.x, duda.cabezaMundo.y, duda.cabezaMundo.z).map(Math.round) });
    window.MEDIDAS.contactos = CONTACTOS; return p;
  }
  let puntoBloqueo = null;

  const HECHOS = [
    [30, () => marca('trazo_de_tinta')],
    [60, () => { marca('choque_suelo'); marca('cajas_caen'); onda(0.3, ZN, 0.3, 2.4, 0.4); polvo(0.4, 0.15, ZN + 0.1, 8); grieta(0.3, ZN, 0.9, 6); tirarCajas(Z.pila_de_cajas.slice().reverse(), 3, -1); }],
    // golpe 1 · Tin, puño · estante izquierdo
    [K1 - 3, () => marca('silbido')], [K1 - 1, () => marca('golpe')],
    [K1, () => contacto('golpe 1', 'tin', 'mano', 'pecho', 0.52)],
    [K1 + 18, () => { marca('choque_madera'); marca('cajas_caen'); polvo(-2.4, 1.2, -5.7, 14, 2.2); tirarCajas(Z.estante_izquierdo.cajas, 8, 1); }],
    [K1 + 26, () => polvo(-1.9, 0.15, -5.4, 5, 1.0)],
    // golpe 2 · Tan, patada · postes de fila
    [K2 - 1, () => marca('golpe_agudo')],
    [K2, () => contacto('golpe 2', 'tan', 'pie', 'cadera')],
    [K2 + 6, () => marca('roce_suelo')],
    [K2 + 14, () => polvo(1.0, 0.12, ZN, 4, 0.8)],                                                     // Tin cae del salto
    [K2 + 18, () => { marca('postes_caen'); polvo(2.2, 0.2, 0.2, 8); for (const c of Z.postes_de_fila.cintas) c.visible = false; }],
    [K.cartel, () => { marca('choque_madera_agudo'); polvo(3.0, 1.1, -0.6, 3, 0.8); const a = Z.cartel_de_pie.arriba; suelta(a, [1.2, 2.6, 0.8], [0.4, 1.2, -4.5], 0.06);  }],
    [K.rival_ataca - 2, () => marca('silbido')],
    // golpe 3 · Tin, gancho · mostrador
    [K3 - 1, () => { marca('golpe_grave'); marca('silbido_sube'); }],
    [K3, () => contacto('golpe 3', 'tin', 'mano', 'pecho', 0.6, 6, 1.6)],
    [K3 + 18, () => marca('silbido_caida')],
    [K3 + 22, () => { marca('choque_pilar'); polvo(3.1, 1.2, -3.2, 8, 1.6); grietaMostrador.visible = true; Z.mostrador.mitades[0].rotation.z = -0.03; Z.mostrador.mitades[1].rotation.z = 0.03; }],
    [K.dibuja_baston, () => marca('trazo_de_tinta')],
    [K.dibuja_espada, () => marca('trazo_de_tinta')],
    // bloqueo · la punta rota vuela y enciende el televisor
    [KB - 1, () => marca('bloqueo_tinta')],
    [KB, () => { const p = duda.armaMundo.clone().lerp(tin.manoMundo, 0.35); p.z += 0.08; puntoBloqueo = p; estrella(p, 0.5); soltar('gota', p, V(0.2, 2.2, 0), 2.0, 5);
      CONTACTOS.push({ nombre: 'bloqueo', quien: 'duda', parte: 'espada contra bastón', espada_a_cabeza_de_tin_u: +p.distanceTo(tin.cabezaMundo).toFixed(3), estrella_px: window.proyecta(p.x, p.y, p.z).map(Math.round) }); }],
    [K.tele_punta, () => {
      marca('vidrio_grieta'); const t = Z.isla_televisor, g = t.lienzo.getContext('2d'); g.strokeStyle = C.linea; g.lineCap = 'round'; const cx = 540, cy = 200;
      for (let i = 0; i < 11; i++) { let a = i / 11 * 6.283 + az() * 0.4, x = cx, y = cy; g.lineWidth = 3 + az() * 5; g.beginPath(); g.moveTo(x, y); for (let k = 0; k < 4; k++) { a += (az() - 0.5) * 0.7; x += Math.cos(a) * (40 + az() * 60); y += Math.sin(a) * (40 + az() * 60); g.lineTo(x, y); } g.stroke(); }
      t.tex.needsUpdate = true;
    }],
    [K.tele_punta + 2, () => { marca('chispas'); soltar('chispaC', V(TV[0] + 0.25, TV[1] + 0.1, TV[2] + 0.3), V(0, 2.5, 1.5), 3.5, 12); }],
    [K.tele_punta + 7, () => soltar('chispaC', V(TV[0] + 0.25, TV[1] + 0.1, TV[2] + 0.3), V(0, 2.5, 1.5), 3.5, 9)],
    [K.tele_punta + 12, () => marca('fuego_enciende')],
    // golpe 4 · Tin, bastón · estante derecho
    [K4 - 1, () => marca('baston_golpe')],
    [K4, () => contacto('golpe 4', 'tin', 'arma')],
    [K4 + 12, () => { marca('choque_madera'); marca('cajas_caen'); polvo(2.5, 1.5, -5.4, 12, 2.0); tirarCajas(Z.estante_derecho.cajas.slice(12), 6, -1); const b = Z.estante_derecho.baldas[2]; b.rotation.x = 0.5; b.position.y -= 0.22; b.position.x -= 0.12; }],
    [K4 + 24, () => polvo(2.9, 0.12, -2.5, 5, 0.9)],
    [K.mazo, () => marca('trazo_de_tinta')], [MAZO_LANZA[0], () => marca('silbido')],
    // golpe 5 · Tan, mazo de tinta · el mostrador se parte y la caja registradora sale despedida
    [K5 - 1, () => { marca('mazo_golpe'); marca('choque_madera'); }],
    [K5, () => {
      contacto('golpe 5', 'tan', 'arma', 'cadera', 0.6, 7); polvo(2.9, 0.5, -2.8, 14, 2.4); grieta(2.9, -2.6, 1.1, 7); onda(2.9, -2.5, 0.3, 2.2, 0.35); grietaMostrador.visible = false;
      const [a, b] = Z.mostrador.mitades; a.rotation.z = -0.24; a.position.y = -0.1; a.position.x -= 0.12; b.rotation.z = 0.24; b.position.y = -0.1; b.position.x += 0.12;
      escena.attach(reg.grupo);
    }],
    [K5 + 2, () => marca('fuego_crece')],
    [K5 + 18, () => { marca('campanilla_caja'); reg.rota = true; reg.gaveta.position.z += 0.28; reg.pantalla.rotation.z = 1.05; reg.pantalla.position.y -= 0.06; reg.cinta.visible = true; reg.cinta.position.set(-0.15, 0.02, 0.5); polvo(regHasta.x, 0.15, regHasta.z, 6); }],
    [K5 + 22, () => marca('trazo_de_tinta')],
    [K5 + 36, () => polvo(0, 0.12, ZF, 5, 0.9)],
    // remate · golpe doble · explosión por fases
    [K.carrera, () => marca('subida')],
    [KR - 1, () => marca('golpe_doble')],
    [KR, () => { contacto('remate (Tin)', 'tin', 'arma', 'pecho', 0.6, 5); contacto('remate (Tan)', 'tan', 'arma', 'pecho', 0.5, 5); }],
    [K.tele_choque, () => { marca('vidrio_grieta'); soltar('chispaC', V(0, 2.3, -7.1), V(0, 3, 1), 5, 14); }],
    [K.claro, () => marca('explosion')],
    [K.invertidos, () => {
      const t = Z.isla_televisor; t.tele.visible = false;
      for (let i = 0; i < 12; i++) { const c = caja(ra(0.16, 0.4), ra(0.12, 0.3), 0.1, i % 4 === 0 ? C.linea : i % 2 ? C.utileria : C.bloque_cerca, 0.02); c.position.set(ra(-0.9, 0.9), ra(1.8, 2.8), -7.3); c.visible = false; c.userData.resto = true; escena.add(c); restos.push(c); }
    }],
    [K.bola, () => {
      for (const c of restos) { c.visible = true; c.userData = { v: V(ra(-5, 5), ra(3, 9), ra(0.5, 4)), w: V(ra(-9, 9), ra(-9, 9), ra(-9, 9)), quieto: false, piso: 0.1 }; trozos.push(c); }
      mancha(0, -7.4, 1.5, 0.5); mancha(0.2, -7.3, 0.85, 0.55, C.linea); grieta(0.1, -6.6, 1.6, 9); grieta(GRIETA_SALIDA[0], GRIETA_SALIDA[1], 0.42, 5); trazoSuelo([[GRIETA_SALIDA[0] - 0.2, GRIETA_SALIDA[1] - 0.08], [GRIETA_SALIDA[0] - 0.06, GRIETA_SALIDA[1] + 0.05], [GRIETA_SALIDA[0] + 0.06, GRIETA_SALIDA[1] - 0.05], [GRIETA_SALIDA[0] + 0.22, GRIETA_SALIDA[1] + 0.08]], 0.06);
      const g = Z.pared_fondo.lienzo.getContext('2d'); g.fillStyle = C.humo; g.globalAlpha = 0.5; g.beginPath(); const borron = (cx, cy, R0, n) => { g.beginPath(); for (let i = 0; i <= n; i++) { const a = i / n * 6.283, R = R0 * (0.62 + 0.38 * az()) * (1 + 0.5 * Math.max(0, -Math.sin(a))); g.lineTo(cx + Math.cos(a) * R * 1.25, cy + Math.sin(a) * R); } g.closePath(); g.fill(); }; borron(512, 560, 150, 40); g.globalAlpha = 0.55; borron(520, 590, 80, 30); Z.pared_fondo.tex.needsUpdate = true;
      for (const [i, b] of Z.banderines.lista.entries()) if (i > 3 && i < 9) for (const hijo of b.children) hijo.material = new THREE.MeshBasicMaterial({ color: hijo === b.children[0] ? C.linea : C.humo, side: THREE.DoubleSide });
      tirarCajas(Z.estante_izquierdo.cajas, 4, 1); tirarCajas(Z.estante_derecho.cajas, 4, -1); onda(0, -7.0, 0.5, 7.5, 0.55);
      polvo(-1.4, 0.15, -5.6, 5, 0.8); polvo(1.6, 0.15, -5.3, 5, 0.8);                                   // Tin y Tan derrapan hacia atrás con la onda
    }],
    // humo de la explosión: sale del televisor reventado y SUBE por la pared (antes se quedaba a la altura de las cabezas)
    [K.enfria, () => { marca('cola_explosion'); for (let i = 0; i < 18; i++) soltar('humoC', V(ra(-1.2, 1.2), ra(1.6, 3.4), ra(-7.6, -7.1)), V(0, 1.6, 0), 1.0, 1); }],
    // golpe 6 · Tin, bastón · implosión; queda un asterisco y lo último del trazo se escurre por la grieta
    [K6 - 1, () => marca('baston_golpe_grave')],
    [K6, () => contacto('golpe 6', 'tin', 'arma', 'cabeza', 0.55, 5)],
    [K.implosion, () => { marca('implosion'); onda(AST[0], AST[1], 3.6, 0.15, 0.5); }],
    [K.implosion + 5, () => onda(AST[0], AST[1], 2.8, 0.15, 0.42, 0.6)],
    [K.implosion + 10, () => onda(AST[0], AST[1], 2.0, 0.15, 0.3, 1.1)],
    [K.armas_gotas, () => { marca('gotas'); soltar('gota', tin.manoMundo.clone().add(V(0.4, 0.3, 0)), V(0, 0.5, 0), 1.0, 6); soltar('gota', tan.manoMundo.clone().add(V(-0.4, 0.5, 0)), V(0, 0.5, 0), 1.2, 7); despeja(); }],
    ...[0, 1, 2, 3, 4, 5].map(i => [K.asterisco + i, () => { marca('asterisco_tic'); const a = i * Math.PI / 3 + 0.26, r = 0.16; trazoSuelo([[AST[0], AST[1]], [AST[0] + Math.cos(a) * r, AST[1] + Math.sin(a) * r * 1.6]], 0.05); }]),
    [K.escurre, () => marca('escurre')],
    [K.lapiz_a_tan, () => marca('silbido_corto')],
    [K.lapiz_a_tan + 6, () => marca('atrapa')],
    [K.invertidos, () => { window.MEDIDAS.explosion_px = window.proyecta(0, 2.6, -7.3).map(Math.round); }],
    [K.radiales, () => { window.MEDIDAS.radiales_px = window.proyecta(0, 2.8, -7.3).map(Math.round); }],
    [K.claro, () => { window.MEDIDAS.claro_px = window.proyecta(0, 3.0, -7.2).map(Math.round); }],
    [K1 + 18, () => { window.MEDIDAS.impacto_estante_px = window.proyecta(duda.caderaMundo.x, duda.caderaMundo.y, duda.caderaMundo.z).map(Math.round); }],
    [K3 + 22, () => { window.MEDIDAS.impacto_mostrador_px = window.proyecta(duda.caderaMundo.x, duda.caderaMundo.y, duda.caderaMundo.z).map(Math.round); }],
    [K.tele_punta, () => { window.MEDIDAS.impacto_tele_px = window.proyecta(TV[0] + 0.25, TV[1] + 0.2, TV[2]).map(Math.round); }],
    [N - 1, () => { window.MEDIDAS.final = { mando_mostaza: window.proyecta(-2.36, 3.21, -9.72), caja_registradora_rota: window.proyecta(regHasta.x, 0.2, regHasta.z), asterisco: window.proyecta(AST[0], 0, AST[1]), grieta_salida: window.proyecta(GRIETA_SALIDA[0], 0, GRIETA_SALIDA[1]), televisor: window.proyecta(0, 2.3, -7.44), px_por_u_en_asterisco: Math.abs(window.proyecta(1, 0, AST[1])[0] - window.proyecta(0, 0, AST[1])[0]) }; }],
    [K.cierre - 1, () => { window.MEDIDAS.plano_final = { caja_registradora_rota: window.proyecta(regHasta.x, 0.2, regHasta.z).map(Math.round), asterisco: window.proyecta(AST[0], 0, AST[1]).map(Math.round), grieta_salida: window.proyecta(GRIETA_SALIDA[0], 0, GRIETA_SALIDA[1]).map(Math.round), mando_mostaza: window.proyecta(-2.36, 3.21, -9.72).map(Math.round) }; }],
    [1, () => { window.MEDIDAS.inicio = { mando_mostaza: window.proyecta(-2.36, 3.21, -9.72), televisor_izq_arriba: window.proyecta(-1.2, 3.0, -7.44), televisor_der_abajo: window.proyecta(1.2, 1.6, -7.44), suelo_z0: window.proyecta(0, 0, 0), banderines_bajo: window.proyecta(0, 5.5, -9.5) }; }],
  ];
  HECHOS.sort((a, b) => a[0] - b[0]);
  const restos = [];
  // lo que se mueve a lo largo de varios fotogramas
  anima(K1 + 18, K1 + 24, u => { Z.estante_izquierdo.grupo.rotation.z = 0.21 * EASE.out(u); });
  anima(K.cartel + 1, K.cartel + 9, u => { Z.cartel_de_pie.abajo.rotation.x = -1.5 * EASE.in(u); Z.cartel_de_pie.abajo.position.set(0, 0.425 - 0.39 * EASE.in(u), -0.4 * EASE.in(u)); });
  anima(K2 + 18, K2 + 26, u => { Z.postes_de_fila.postes.forEach((p, i) => { p.rotation.z = -1.52 * EASE.in(clamp(u * 1.4 - i * 0.12)); p.rotation.y = 0.3 * i; }); });
  anima(K.invertidos, K.invertidos + 12, u => { const g = Z.isla_televisor.grupo; g.rotation.z = 1.42 * EASE.in(u); g.position.y = 0.25 * EASE.in(u); });
  anima(K.bola, K.bola + 16, u => { Z.banderines.grupo.rotation.z = -0.95 * EASE.back(u); });
  anima(K5 + 2, K5 + 18, u => { reg.grupo.position.set(lerp(regDesde.x, regHasta.x, u), lerp(regDesde.y, regHasta.y, u) + 2.6 * Math.sin(Math.PI * u), lerp(regDesde.z, regHasta.z, u)); reg.grupo.rotation.set(u * 5.2, 0.6 * u, u * 6.2832); if (u >= 1) { reg.grupo.rotation.set(0, 0.35, 0); reg.grupo.scale.setScalar(0.62); } });
  let corridos = null;
  anima(K.implosion, K.implosion_fin, u => {                        // la implosión arrastra cajas y papeles ≈ 0,5 u hacia el centro
    if (!corridos) corridos = trozos.filter(t => t.userData.quieto && Math.hypot(t.position.x - AST[0], t.position.z - AST[1]) < 4.5 && Math.hypot(t.position.x - AST[0], t.position.z - AST[1]) > 1.7).map(t => ({ t, de: t.position.clone() }));
    for (const c of corridos) { const d = V(AST[0] - c.de.x, 0, AST[1] - c.de.z); const l = d.length(); c.t.position.copy(c.de).addScaledVector(d.normalize(), Math.min(0.5, l - 1.2) * EASE.io(u)); }
  });

  // ------------------------------------------------------------ cada fotograma
  // zonas de conexión limpias: nada de escombros sobre la marca final, la salida por la grieta, la caja registradora rota
  // ni donde pisan Tin y Tan al final
  const PIES = [[-1.45, AST[1]], [1.55, -4.7]];
  function despeja() {
    for (const t of trozos) {
      if (t === reg.grupo) continue; const p = t.position;
      const d = Math.hypot(p.x - AST[0], p.z - AST[1]); if (d < 1.0) { const a = d > 0.01 ? Math.atan2(p.z - AST[1], p.x - AST[0]) : 2.2; p.x = AST[0] + Math.cos(a) * 1.05; p.z = AST[1] - Math.abs(Math.sin(a)) * 1.05 - 0.2; }
      if (p.x > -0.2 && p.x < 2.0 && Math.abs(p.z - AST[1]) < 0.45) p.z = AST[1] - 0.7;
      for (const [x, z] of PIES) if (Math.hypot(p.x - x, p.z - z) < 0.55) { p.z = z - 0.8; }
      const c = Math.hypot(p.x - CAJA_ROTA[0], p.z - CAJA_ROTA[1]); if (c < 0.95) { p.x = CAJA_ROTA[0] + 1.05; p.z = CAJA_ROTA[1] - 0.5; }
    }
  }
  let hechoAnim = new Set(), mazoDe = null, lapizDe = null;
  function cadaCuadro(f, dt) {
    for (const [i, [f0, f1, fn]] of animados.entries()) { if (f >= f0 && f <= f1) fn(entre(f, f0, f1)); else if (f > f1 && !hechoAnim.has(i)) { fn(1); hechoAnim.add(i); } }
    // llamas planas: 3 dibujos de 2 f; el borde cambia de forma, no parpadea
    for (const l of llamas) { const t = l.tam(f); l.o.visible = t > 0.02; if (!l.o.visible) continue; l.o.material.map = texLlama[Math.floor(f / 2) % 3]; l.o.scale.set(t, t, 1); l.o.position.set(l.x, l.y + t * 0.58, l.z); }
    if (f >= K.tele_punta + 22 && f < K.tele_choque && f % 5 === 0) soltar('humoC', V(TV[0] + ra(-0.2, 0.6), TV[1] + 0.9 + fase(f) * 0.9, TV[2] - 0.15), V(0, 1.5, 0), 0.4, 1);
    if (f >= K.enfria && f <= K.implosion && f % 3 === 0) despeja();
    if (f >= K.enfria && f < K.implosion && f % 8 === 0) soltar('humoC', V(ra(-0.7, 0.7), 1.7, -7.5), V(0, 1.7, 0), 0.4, 1);
    // bola de fuego plana (f bola a enfría), 3 dibujos de 2 f; al enfriar se encoge
    const ub = entre(f, K.bola, K.enfria), ue = entre(f, K.enfria, K.enfria + 8);
    bola.visible = f >= K.bola && f < K.enfria + 8;
    if (bola.visible) { const t = lerp(2.2, 5.6, EASE.out(ub)) * (1 - 0.85 * EASE.in(ue)); bola.material.map = texEstallido[Math.floor(f / 2) % 3]; bola.scale.set(t, t, 1); bola.position.set(0, 3.1, -7.3); }
    anillo.visible = f >= K.bola && f < K.bola + 9;
    if (anillo.visible) { const t = lerp(3.0, 9.5, EASE.out(entre(f, K.bola, K.bola + 9))); anillo.scale.set(t, t, 1); anillo.position.set(0, 3.1, -7.35); }
    // objetos que vuelan
    punta.visible = false; mazoV.visible = false; lapizV.visible = false;
    if (!vuelo(punta, f, KB + 2, KB + 13, puntoBloqueo, V(TV[0] + 0.28, TV[1] + 0.25, TV[2] + 0.1), 0.9, 2.5) && f > KB + 13 && f < K.invertidos) { punta.visible = true; punta.position.set(TV[0] + 0.28, TV[1] + 0.25, TV[2] + 0.13); punta.rotation.z = 2.4; }
    if (f === MAZO_LANZA[0]) mazoDe = tin.manoMundo.clone().add(V(0.3, 0.5, 0));
    vuelo(mazoV, f, MAZO_LANZA[0], MAZO_LANZA[1], mazoDe, tan.manoMundo.clone().add(V(0, 0.45, 0)), 0.55, 1);
    if (f === K.lapiz_a_tan) lapizDe = tin.manoAtrasMundo.clone();
    vuelo(lapizV, f, K.lapiz_a_tan, K.lapiz_a_tan + 6, lapizDe, tan.manoMundo, 0.9, 1.5);
    // los planos sueltos miran a la cámara
    for (const o of deCara) if (o.visible) o.rotation.y = Math.atan2(m.camara.position.x - o.position.x, m.camara.position.z - o.position.z);
    // calcos del rival
    historia.unshift({ p: duda.malla.position.clone(), s: duda.malla.scale.clone(), r: duda.malla.rotation.z, y: duda.malla.rotation.y }); historia.length = Math.min(historia.length, 8);
    const lanza = LANZA.some(([a, b]) => f >= a && f <= b);
    calcos.forEach((o, i) => { const h = historia[(i + 1) * 2]; o.visible = lanza && !!h && duda.malla.visible; if (o.visible) { o.position.copy(h.p); o.scale.copy(h.s); o.rotation.set(0, h.y, h.r); o.renderOrder = -1; } });
    // implosión: tinta que se recoge hacia el centro; se lleva el humo
    if (f >= K.implosion && f < K.implosion_fin) soltar('gota', V(AST[0] + ra(-2.0, 2.0), ra(0.2, 2.6), AST[1] + ra(-0.8, 0.8)), V(0, 0, 0), 0.1, 3, V(AST[0], 0.5, AST[1]));
    // lo último del trazo se escurre por la grieta del suelo (16 f)
    gotaSuelo.visible = f >= K.escurre && f <= K.escurre_fin;
    if (gotaSuelo.visible) { const u = entre(f, K.escurre, K.escurre_fin), x = lerp(AST[0] + 0.2, GRIETA_SALIDA[0], EASE.io(u)), largo = 0.5 * Math.sin(Math.PI * Math.min(1, u * 1.15)) + 0.04; gotaSuelo.scale.set(largo, 1.4, 1); gotaSuelo.position.set(x - largo / 2 * (u > 0.8 ? 1 : 0.4), 0.02, AST[1]); }
  }

  // ------------------------------------------------------------ cámara (v3): dentro del mundo, alta y con diagonal
  // Cada plano se define por a qué punto del suelo mira (t = [x, z]), desde qué distancia (D), altura (h) y diagonal (az, en
  // grados; + = la cámara se corre a la derecha), y en qué y del cuadro cae ese punto (yP). La cámara mira hacia abajo lo
  // justo para eso, así el suelo ocupa el cuadro y dos carriles separados 1,6 u se ven separados. Dentro de un plano puede
  // acompañar una carrera o un vuelo (claves); entre planos se corta. Sin temblor. Los dibujos giran hacia la cámara (motor).
  const FOV = 46, BASE = { ty: 0, h: 3.2, az: 0, yP: 1330, fov: FOV };
  const c = (t, D, o = {}) => ({ ...BASE, t, D, ...o });
  const PL = (f0, nombre, ...claves) => ({ f0, nombre, claves: claves.map(([f, v, e]) => [f, v, e]) });
  const PLANOS = [
    PL(30, 'P2 entra el rival', [30, c([-0.1, ZN], 9.4, { h: 3.3, az: -4 })], [69, c([-0.1, ZN], 9.0, { h: 3.3, az: 3 })]),
    PL(K1 - 12, 'P3 golpe 1', [K1 - 12, c([0.75, ZN], 7.4, { az: 12, h: 3.0 })], [K1 + 1, c([0.7, ZN], 7.3, { az: 12, h: 3.0 })], [K1 + 17, c([-0.3, ZN], 9.6, { az: 16, h: 3.5 }), 'io']),
    PL(K1 + 18, 'P4 impacto estante', [K1 + 18, c([-2.2, -5.7], 5.2, { az: 28, h: 2.4, ty: 1.3, yP: 1050 })]),
    // Tan y el rival: la diagonal separa al rival (al fondo) de Tan (cerca); Tin espera fuera de cuadro
    PL(K1 + 20, 'P5 el rival vuelve', [K1 + 20, c([-2.05, ZN], 8.8, { az: -14, h: 3.4 })], [CARGA_RIVAL[0], c([-2.0, ZN], 8.6, { az: -12, h: 3.4 })], [K2 - 13, c([-1.75, ZN], 8.2, { az: -8, h: 3.3 }), 'io']),
    PL(K2 - 12, 'P6 golpe 2', [K2 - 12, c([-0.2, ZN], 8.2, { h: 3.2, az: -4, yP: 1310 })], [K2 + 1, c([-0.2, ZN], 8.1, { h: 3.2, az: -4, yP: 1310 })], [K2 + 14, c([0.0, ZN], 8.2, { h: 3.2, az: 0, yP: 1310 }), 'io']),
    PL(K2 + 15, 'P7 general', [K2 + 15, c([1.9, -0.5], 8.5, { h: 3.2, az: 2 })], [K.salto_mostrador + 1, c([1.8, -0.6], 7.9, { h: 3.1, az: 10 })]),
    PL(K.salto_mostrador + 2, 'P8 gancho', [K.salto_mostrador + 2, c([1.9, -1.4], 8.4, { az: 30, h: 3.2 })], [K.salto_mostrador + 15, c([1.8, -2.88], 8.0, { az: 30, h: 3.1 }), 'io'], [K3, c([1.9, -2.88], 7.6, { az: 28, h: 3.0 })], [K3 + 12, c([2.3, -2.88], 8.6, { az: 26, h: 3.3, ty: 0.3, yP: 1285 }), 'out'], [K3 + 21, c([2.5, -2.88], 8.0, { az: 24, h: 3.0, ty: 0 }), 'in']),
    PL(K3 + 22, 'P9 impacto mostrador', [K3 + 22, c([3.15, -3.3], 4.6, { az: 14, h: 2.6, ty: 1.0, yP: 1080 })]),
    PL(K3 + 24, 'P10 general', [K3 + 24, c([2.5, -2.88], 8.2, { az: 8, h: 3.2 })], [K3 + 62, c([2.5, -2.88], 8.0, { az: 6, h: 3.2 })], [K3 + 92, c([1.78, -2.8], 8.6, { az: 3, h: 3.2 }), 'io'], [K.dibuja_baston - 1, c([1.78, -2.8], 8.4, { az: 1, h: 3.2 })]),
    PL(K.dibuja_baston, 'P11 detalle del lápiz', [K.dibuja_baston, c([1.0, ZM], 3.5, { az: 6, h: 1.6, ty: 1.2, yP: 1000, fov: 40 })], [K.dibuja_baston + 11, c([1.05, ZM], 3.3, { az: 4, h: 1.6, ty: 1.2, yP: 1000, fov: 40 })]),
    PL(K.dibuja_baston + 12, 'P12 general', [K.dibuja_baston + 12, c([1.78, -2.8], 8.5, { az: -5, h: 3.2 })], [L.C.f0 - 1, c([1.78, -2.8], 8.1, { az: -1, h: 3.2 })]),
    PL(L.C.f0, 'P12b Tan invita', [L.C.f0, c([-1.2, -1.5], 4.4, { az: 18, h: 2.0, ty: 1.2, yP: 1130, fov: 40 })], [K.dibuja_espada - 3, c([-1.2, -1.5], 4.2, { az: 14, h: 2.0, ty: 1.2, yP: 1130, fov: 40 })]),
    PL(K.dibuja_espada - 2, 'P12c espada y bloqueo', [K.dibuja_espada - 2, c([1.05, ZM], 7.6, { az: 4, h: 3.1 })], [KB + 13, c([1.0, ZM], 7.2, { az: 8, h: 3.1 })]),
    PL(K.tele_punta, 'P13 impacto televisor', [K.tele_punta, c([0.2, -7.4], 5.0, { h: 2.9, ty: 2.3, yP: 1050 })]),
    PL(K.tele_punta + 2, 'P14 golpe 4 y cruce de Tan', [K.tele_punta + 2, c([1.25, -2.0], 7.9, { az: 6, h: 3.2 })], [K4 + 2, c([1.25, -2.0], 7.8, { az: 6, h: 3.2 })], [K4 + 12, c([0.35, -1.5], 9.8, { az: -3, h: 3.5 }), 'io'], [K5 - 14, c([0.4, -1.5], 9.4, { az: -6, h: 3.5 }), 'io']),
    // un solo plano del mazazo al remate: acompaña a la caja registradora, descubre al rival ante el televisor y sigue la carrera
    PL(K5 - 13, 'P15 mazo, carga y remate', [K5 - 13, c([2.15, -2.5], 8.0, { az: 6, h: 3.2 })], [K5 + 1, c([2.15, -2.5], 7.9, { az: 6, h: 3.2 })], [K5 + 19, c([0.1, -2.6], 10.4, { az: -18, h: 3.7 }), 'io'], [CARGA[0], c([0.2, -2.6], 10.2, { az: -22, h: 3.6 })],
      [CARGA[1], c([0, ZF], 9.2, { az: -14, h: 3.4 }), 'io'], [KR + 1, c([0, ZF], 9.0, { az: -8, h: 3.4 })], [KR + 20, c([0, ZF], 9.2, { az: -4, h: 3.4 }), 'io']),
    PL(K.radiales, 'P18 héroe', [K.radiales, c([0.05, -6.0], 9.4, { az: -4, h: 1.0, ty: 2.0, yP: 900, fov: 52 })], [K.radiales + 30, c([0.05, -6.0], 9.9, { az: 4, h: 1.1, ty: 2.0, yP: 900, fov: 52 })]),
    PL(K.radiales + 31, 'P19 respiro', [K.radiales + 31, c([0.05, -4.9], 9.5, { az: -7, h: 3.5 })], [K6 - 13, c([0.05, -4.9], 9.0, { az: 7, h: 3.4 })]),
    PL(K6 - 12, 'P20 golpe 6', [K6 - 12, c([-0.8, AST[1]], 6.9, { az: 8, h: 2.9 })], [K6 + 19, c([-0.72, AST[1]], 6.7, { az: 5, h: 2.9 })]),
    PL(K6 + 20, 'P21 final', [K6 + 20, c([0.05, -4.9], 9.3, { az: -5, h: 3.5 })], [K.cierre - 1, c([0.05, -4.9], 9.0, { az: 1, h: 3.5 })]),
  ];
  const PO = T.portada;
  function camaraDe(f, cam) {
    if (f < 30 || f >= K.cierre) {                                  // planos de firma: la cámara de portada del canal, sin cambios
      if (cam.fov !== 36) { cam.fov = 36; cam.updateProjectionMatrix(); }
      cam.position.set(PO.cx, PO.h, PO.z + PO.D); cam.lookAt(PO.cx, PO.h, PO.z); return;
    }
    let p = PLANOS[0]; for (const q of PLANOS) if (f >= q.f0) p = q;
    const v = pista(p.claves, f), a = v.az * Math.PI / 180, foco = (m.H / 2) / Math.tan(v.fov * Math.PI / 360);
    if (Math.abs(cam.fov - v.fov) > 1e-6) { cam.fov = v.fov; cam.updateProjectionMatrix(); }
    const baja = Math.atan2(v.h - v.ty, v.D) - Math.atan((v.yP - m.H / 2) / foco);          // cuánto mira hacia abajo
    cam.position.set(v.t[0] + Math.sin(a) * v.D, v.h, v.t[1] + Math.cos(a) * v.D);
    cam.lookAt(v.t[0], v.h - v.D * Math.tan(baja), v.t[1]);
  }
  window.MEDIDAS.planos = PLANOS.map(p => ({ f0: p.f0, nombre: p.nombre }));

  // ------------------------------------------------------------ control del guion: ninguna clave cruzada ni repetida (revisión de animación, AN7)
  const cruces = [];
  for (const q of ['tin', 'tan', 'duda']) for (const k of ['pos', 'pose', 'escala']) { const t = G[q][k]; for (let i = 1; i < t.length; i++) if (t[i][0] <= t[i - 1][0]) cruces.push(`${q}.${k}: f${t[i - 1][0]} y f${t[i][0]}`); }
  for (const p of PLANOS) for (let i = 1; i < p.claves.length; i++) if (p.claves[i][0] <= p.claves[i - 1][0]) cruces.push(`cámara ${p.nombre}: f${p.claves[i][0]}`);
  for (let i = 1; i < PLANOS.length; i++) if (PLANOS[i].f0 <= PLANOS[i - 1].f0) cruces.push(`planos ${PLANOS[i - 1].nombre} y ${PLANOS[i].nombre}`);
  window.MEDIDAS.claves_cruzadas = cruces;
  if (cruces.length) console.error('CLAVES CRUZADAS: ' + cruces.join(' | '));

  const caras = ['duda_0', 'duda_1', 'duda_2', 'duda_3'];
  for (const p of ['tin', 'tan']) for (const e of ['curiosidad', 'sorpresa', 'eureka', 'risa', 'concentrado']) caras.push(`${p}_${e}`);
  // un solo reloj: personajes y física van al mismo paso (la cámara lenta está en las curvas de los vuelos)
  return { porFotogramas: true, FIN: N, velocidad: () => 1, reloj: () => 1, G, CAM: null, camara: camaraDe, HECHOS, caras, cadaCuadro, extra, encara: true, pistas: true, borron: 6.5, respira: true };
}
