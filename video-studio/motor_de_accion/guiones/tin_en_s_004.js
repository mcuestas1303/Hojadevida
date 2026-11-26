// Guion del short 4 de Tin & Tan (TIN-EN-S-004, «What Is GTA 6, and Is a GTA 7 Coming?»).
// Fuente: proyectos/2026-11-26_tin_y_tan_what_is_gta_6/02_prompt/direccion.md y prompt.md.
// Los fotogramas salen de la voz real: guiones/tin_en_s_004.tiempos.json (lo escribe codigo/tiempos.py del proyecto).
// Reloj por fotogramas (S = fotograma). Sin temblor: cortes. Los planos de firma (portada) se graban sin personajes:
// Tin, Tan, el lápiz bumerán, los datos y los subtítulos los pone codigo/componer.py encima, con la firma del canal.
// Reglas que este guion respeta: el rival nunca alcanza a Tin ni a Tan; nada rojo sobre el rival (lo que salta es
// tinta); ningún rótulo ni marca en el mundo; fuego plano de dos tonos; humo con contorno; el daño se queda.
export const FICHA = { id: 'tin_en_s_004', entorno: 'tienda_de_videojuegos', paleta: 'c_alto_voltaje', creado: '2026-11-26' };

export async function guion(m) {
  const { THREE, P, V, C, EASE, clamp, ra, pista, marca, grieta, mancha, trazoSuelo, onda, soltar, estrella, trozos, entorno, personajes, escena, caja, lienzo, FPS } = m;
  const T = await (await fetch('guiones/tin_en_s_004.tiempos.json')).json();
  const K = T.K, N = T.N, L = {}; for (const l of T.lineas) L[l.id] = l;
  const { tin, tan, duda } = personajes, Z = entorno.piezas;
  const { K1, K2, K3, KB, K4, K5, KR, K6 } = K;
  const lerp = (a, b, u) => a + (b - a) * u, entre = (f, a, b) => clamp((f - a) / (b - a));

  // ------------------------------------------------------------ poses nuevas (entran al catálogo)
  const A = (pose, ang) => ({ ...pose, armaAng: ang });
  Object.assign(P, {
    gancho: { t: 16, aF: [150, 174], aB: [40, 120], lF: [30, 0], lB: [-36, -14], c: -12 },
    bloqueo: { t: -8, aF: [74, 150], aB: [44, 132], lF: [28, 4], lB: [-30, -10], c: 0, armaAng: 176 },
    dibuja: { t: 6, aF: [58, 112], aB: [84, 96], lF: [14, 4], lB: [-14, -4], c: 8, armaAng: 150 },
    pregunta: { t: 0, aF: [58, 152], aB: [-10, -5], lF: [8, 4], lB: [-8, -4], c: -10 },
    invita: { t: 2, aF: [104, 168], aB: [-22, -8], lF: [10, 4], lB: [-10, -4], c: -4 },
    mazoArriba: { t: -10, aF: [158, 184], aB: [150, 172], lF: [22, 0], lB: [-30, -10], c: -8, armaAng: 196 },
    mazoAbajo: { t: 40, aF: [62, 72], aB: [52, 62], lF: [52, -10], lB: [-40, -52], c: 12, armaAng: 78 },
    miraEspada: { t: -4, aF: [84, 166], aB: [20, 60], lF: [14, 4], lB: [-14, -4], c: 22, armaAng: 178 },
    atrapa: { t: 0, aF: [96, 150], aB: [-12, -6], lF: [10, 4], lB: [-10, -4], c: -6 },
  });
  const Gd = A(P.guardia, 150), Cg = A(P.carga, 244), Gp = A(P.golpe, 98);

  // ------------------------------------------------------------ pistas de cada personaje
  const nueva = () => ({ pos: [], pose: [], mira: [], cara: [], escala: [], visible: [] });
  const G = { tin: nueva(), tan: nueva(), duda: nueva() };
  const pos = (q, ...ks) => G[q].pos.push(...ks), pose = (q, ...ks) => G[q].pose.push(...ks);
  const corre = (q, f0, f1, arma) => { for (let f = f0, i = 0; f < f1; f += 4, i++) pose(q, [f, arma ? A(i % 2 ? P.corre2 : P.corre1, 150) : (i % 2 ? P.corre2 : P.corre1), 'lin']); };
  // golpe con la gramática medida: anticipación K−12 a K−7, pausa K−6 a K−1 (pose quieta), contacto K y K+1, recuperación
  const ataque = (q, k, antes, carga, golpe, despues, sostiene = 5) => pose(q, [k - 13, antes], [k - 7, carga, 'out'], [k - 1, carga], [k, golpe, 'salto'], [k + sostiene, golpe], [k + sostiene + 6, despues]);

  const CIERRE = K.cierre, RECOMPONE = KR + 86, ESC = { e15: 1.15, e14: 1.08, e125: 0.96, e11: 0.85, e10: 0.77, e09: 0.69, e08: 0.62 };

  // --- Tan
  G.tan.visible.push([0, false], [30, true], [CIERRE, false]);
  G.tan.mira.push([0, 1], [K5 + 16, -1], [RECOMPONE - 40, -1], [K.lapiz_a_tan - 6, -1]);
  G.tan.cara.push([0, 'sorpresa'], [K2 - 13, 'concentrado'], [K2, 'eureka'], [K2 + 26, 'curiosidad'], [L.C.f0, 'risa'], [L.C.f1 + 2, 'curiosidad'], [KB, 'sorpresa'], [K5 - 13, 'concentrado'], [K5, 'eureka'], [K5 + 20, 'concentrado'], [KR, 'eureka'], [K.invertidos, 'sorpresa'], [L.B.f0, 'curiosidad'], [K6, 'sorpresa'], [K.asterisco, 'curiosidad'], [K.lapiz_a_tan + 6, 'risa']);
  pos('tan', [30, [-1.5, 0, -0.6]], [46, [-1.5, 0, -0.6]], [66, [-1.95, 0, -0.4], 'out'], [K2 - 30, [-1.95, 0, -0.4]], [K2 - 13, [-1.45, 0, -1.0]], [K2 - 1, [-1.45, 0, -1.0]], [K2, [-1.2, 0, -1.0], 'salto'], [K2 + 11, [-1.4, 0, -1.0]], [K2 + 26, [-0.6, 0, -1.0]],
    [K3 - 10, [-0.6, 0, -1.0]], [K3 + 30, [-0.8, 0, -1.6]], [K4 - 4, [-0.8, 0, -1.6]], [K4 + 10, [1.8, 0, -2.3], 'lin'], [K5 - 14, [1.8, 0, -2.7]], [K5 - 1, [1.8, 0, -2.7]], [K5, [2.05, 0, -2.7], 'salto'], [K5 + 14, [1.9, 0, -2.7]],
    [K5 + 18, [1.9, 0, -2.7]], [K5 + 44, [1.0, 0, -4.6], 'lin'], [K.carrera, [1.0, 0, -4.6]], [K.carrera + 11, [0.95, 0, -5.7], 'lin'], [KR - 1, [0.95, 0, -5.9]], [KR, [0.75, 0, -6.0], 'salto'], [KR + 12, [0.95, 0, -5.8]],
    [K.radiales - 1, [0.95, 0, -5.8]], [K.radiales, [1.15, 0, -5.4], 'salto'], [L.T9.f0 + 30, [1.15, 0, -5.4]], [L.T9.f0 + 62, [1.5, 0, -4.9]], [N, [1.5, 0, -4.9]]);
  pose('tan', [30, P.guardia], [46, P.guardia], [54, P.recibe, 'out'], [66, P.guardia], [K2 - 30, P.guardia]);
  ataque('tan', K2, P.guardia, P.carga, P.patada, P.guardia);
  pose('tan', [K2 + 14, P.festeja, 'back'], [K2 + 20, P.festeja], [K2 + 28, P.guardia], [L.C.f0 - 6, P.guardia], [L.C.f0 + 2, P.invita, 'back'], [L.C.f1, P.invita], [L.C.f1 + 6, P.guardia], [K4 - 5, P.guardia]);
  corre('tan', K4 - 4, K4 + 10); pose('tan', [K4 + 11, P.guardia]);
  pose('tan', [K5 - 15, P.atrapa], [K5 - 14, A(P.atrapa, 170)]);
  ataque('tan', K5, A(P.atrapa, 170), P.mazoArriba, P.mazoAbajo, A(P.guardia, 150), 9);
  corre('tan', K5 + 18, K5 + 44, true);
  pose('tan', [K5 + 44, Gd], [K.carrera - 1, Gd], [K.carrera, A(P.corre1, 150)], [K.carrera + 5, A(P.corre2, 150), 'lin'], [K.carrera + 10, A(P.corre1, 150), 'lin']);
  ataque('tan', KR, A(P.corre1, 150), Cg, Gp, Gd);
  pose('tan', [K.radiales - 1, Gd], [K.radiales, A(P.agachado, 120), 'salto'], [L.T9.f0 + 4, A(P.agachado, 120)], [L.T9.f0 + 14, A(P.recibe, 150)], [L.T9.f0 + 30, A(P.recibe, 150)]);
  corre('tan', L.T9.f0 + 32, L.T9.f0 + 62, true);
  pose('tan', [L.T9.f0 + 62, Gd], [L.B.f0 - 4, Gd], [L.B.f0 + 4, A(P.pregunta, 150), 'back'], [L.B.f1, A(P.pregunta, 150)], [K6 - 4, Gd], [K6, A(P.recibe, 150), 'out'], [K6 + 20, Gd], [K.armas_gotas + 10, P.guardia], [K.asterisco, P.quieto],
    [K.lapiz_a_tan + 3, P.quieto], [K.lapiz_a_tan + 6, P.atrapa, 'out'], [N, P.atrapa]);

  // --- Tin
  G.tin.visible.push([0, false], [30, true], [CIERRE, false]);
  G.tin.mira.push([0, -1], [K2 + 20, 1], [K4 + 16, 1], [K5 + 18, 1], [L.T9.f0 + 40, 1]);
  G.tin.cara.push([0, 'curiosidad'], [K1 - 13, 'concentrado'], [K1 + 2, 'eureka'], [K1 + 40, 'curiosidad'], [K.rival_ataca - 6, 'sorpresa'], [K3 - 13, 'concentrado'], [K3 + 2, 'eureka'], [K3 + 60, 'curiosidad'], [K.dibuja_baston, 'concentrado'], [L.T5.f1, 'curiosidad'],
    [KB - 6, 'concentrado'], [K4 + 2, 'eureka'], [K4 + 30, 'concentrado'], [K5 + 2, 'curiosidad'], [K.carrera, 'concentrado'], [KR, 'eureka'], [K.invertidos, 'sorpresa'], [L.T9.f0 + 4, 'eureka'], [L.T9.f1, 'curiosidad'], [K6 - 13, 'concentrado'], [K6 + 2, 'curiosidad']);
  pos('tin', [30, [1.5, 0, -0.8]], [46, [1.5, 0, -0.8]], [66, [1.25, 0, -1.6]], [K1 - 13, [1.25, 0, -1.6]], [K1 - 7, [1.05, 0, -2.0]], [K1 - 1, [1.05, 0, -2.0]], [K1, [0.72, 0, -2.0], 'salto'], [K1 + 11, [1.0, 0, -2.0]],
    [K2 + 30, [1.0, 0, -2.0]], [K.cartel - 4, [0.45, 0, 0.1]], [K.salto_mostrador + 2, [0.45, 0, 0.1]], [K3 - 14, [1.85, 0, -2.9], 'lin'], [K3 - 1, [1.85, 0, -2.9]], [K3, [2.05, 0.45, -2.9], 'salto'], [K3 + 6, [2.0, 0, -2.9], 'in'],
    [K3 + 60, [2.0, 0, -2.9]], [K.dibuja_baston - 4, [0.55, 0, -2.6]], [KB - 1, [0.55, 0, -2.6]], [KB, [0.5, 0, -2.6], 'salto'], [K4 - 7, [0.6, 0, -2.6]], [K4 - 1, [0.6, 0, -2.6]], [K4, [0.95, 0, -2.6], 'salto'], [K4 + 11, [0.7, 0, -2.6]],
    [K.mazo - 2, [0.1, 0, -2.2]], [K5 + 20, [0.1, 0, -2.2]], [K5 + 44, [-1.2, 0, -4.6], 'lin'], [K.carrera, [-1.2, 0, -4.6]], [K.carrera + 11, [-1.15, 0, -5.7], 'lin'], [KR - 1, [-1.15, 0, -5.9]], [KR, [-0.95, 0, -6.0], 'salto'], [KR + 12, [-1.15, 0, -5.8]],
    [K.radiales - 1, [-1.15, 0, -5.8]], [K.radiales, [-1.25, 0, -5.4], 'salto'], [L.T9.f0 + 30, [-1.25, 0, -5.4]], [L.T9.f0 + 62, [-1.1, 0, -5.1]], [K6 - 1, [-1.1, 0, -5.1]], [K6, [-0.8, 0, -5.1], 'salto'], [K6 + 11, [-1.05, 0, -5.1]], [K.armas_gotas, [-1.05, 0, -5.1]], [K.asterisco - 2, [-1.0, 0, -4.3]], [N, [-1.0, 0, -4.3]]);
  pose('tin', [30, P.guardia], [46, P.guardia], [50, P.corre1], [56, P.corre2, 'lin'], [62, P.corre1, 'lin'], [66, P.guardia]);
  ataque('tin', K1, P.guardia, P.carga, P.golpe, P.guardia);
  pose('tin', [K2 + 30, P.guardia]);
  corre('tin', K2 + 31, K.cartel - 5);
  pose('tin', [K.cartel - 4, P.guardia], [K.rival_ataca - 5, P.guardia], [K.rival_ataca - 2, P.agachado, 'out'], [K.rival_ataca + 6, P.agachado], [K.rival_ataca + 12, P.guardia], [K.salto_mostrador + 2, P.guardia]);
  corre('tin', K.salto_mostrador + 3, K3 - 14);
  ataque('tin', K3, P.guardia, P.agachado, P.gancho, P.guardia, 8);
  pose('tin', [K3 + 60, P.guardia]);
  corre('tin', K3 + 61, K.dibuja_baston - 5);
  pose('tin', [K.dibuja_baston - 4, P.dibuja], [K.dibuja_baston + 14, P.dibuja], [K.dibuja_baston + 20, Gd], [KB - 10, Gd], [KB - 3, P.bloqueo, 'out'], [KB + 6, P.bloqueo], [K4 - 14, Gd]);
  ataque('tin', K4, Gd, Cg, Gp, Gd);
  pose('tin', [K.mazo - 2, Gd], [K.mazo, A(P.poder, 180)], [K.mazo + 8, A(P.poder, 180)], [K.mazo + 9, A(P.carga, 240)], [K.mazo + 12, P.golpe, 'in'], [K.mazo + 18, P.guardia], [K5 + 19, P.guardia], [K5 + 22, P.dibuja], [K5 + 34, P.dibuja], [K5 + 36, Gd]);
  corre('tin', K5 + 37, K5 + 44, true);
  pose('tin', [K5 + 44, Gd], [K.carrera - 1, Gd], [K.carrera, A(P.corre2, 150)], [K.carrera + 5, A(P.corre1, 150), 'lin'], [K.carrera + 10, A(P.corre2, 150), 'lin']);
  ataque('tin', KR, A(P.corre2, 150), Cg, Gp, Gd);
  pose('tin', [K.radiales - 1, Gd], [K.radiales, A(P.agachado, 120), 'salto'], [L.T9.f0 + 4, A(P.agachado, 120)], [L.T9.f0 + 14, A(P.recibe, 150)], [L.T9.f0 + 30, A(P.recibe, 150)]);
  corre('tin', L.T9.f0 + 32, L.T9.f0 + 62, true);
  pose('tin', [L.T9.f0 + 62, Gd], [K6 - 14, Gd]);
  ataque('tin', K6, Gd, Cg, Gp, Gd);
  pose('tin', [K6 + 30, A(P.quieto, 60)], [K.armas_gotas + 10, P.quieto], [K.armas_gotas + 11, P.guardia]);
  corre('tin', K.armas_gotas + 1, K.asterisco - 3);
  pose('tin', [K.asterisco - 2, P.quieto], [K.lapiz_a_tan - 3, P.quieto], [K.lapiz_a_tan - 1, P.carga], [K.lapiz_a_tan + 2, P.golpe, 'in'], [K.lapiz_a_tan + 8, P.quieto], [N, P.quieto]);

  // --- el rival (@duda): aparece con la pregunta, grande; baja un escalón de tamaño con cada dato; nunca muere
  const D = G.duda;
  D.visible.push([0, false], [30, true], [K.invertidos, false], [RECOMPONE, true], [K.asterisco + 6, false]);
  D.mira.push([0, 1], [K1 + 26, 1], [K2 - 14, -1], [K4 + 24, -1], [RECOMPONE, -1]);
  D.cara.push([0, 'duda']);
  D.escala.push([30, ESC.e125], [45, ESC.e125], [66, ESC.e15, 'back'], [K1 + 26, ESC.e15], [K1 + 42, ESC.e14], [K2 + 46, ESC.e14], [K2 + 66, ESC.e125], [K3 + 30, ESC.e125], [K3 + 50, ESC.e11], [K4 + 14, ESC.e11], [K4 + 24, ESC.e10],
    [K5, ESC.e10], [K5 + 14, ESC.e09], [KR + 20, ESC.e09], [RECOMPONE, ESC.e08], [K6 + 1, ESC.e08], [K.implosion_fin, 0.1, 'in'], [N, 0.1]);
  pos('duda', [30, [0, 0, -2.0]], [K1 - 1, [0, 0, -2.0]], [K1, [-0.25, 0.1, -2.1], 'salto'], [K1 + 5, [-0.9, 1.15, -3.0], 'out'], [K1 + 17, [-2.3, 1.4, -5.9], 'out'], [K1 + 19, [-2.35, 1.25, -6.0]], [K1 + 26, [-1.95, 0, -5.5], 'in'],
    [K2 - 28, [-1.95, 0, -5.5]], [K2 - 14, [-0.35, 0, -1.0], 'lin'], [K2 - 1, [-0.35, 0, -1.0]], [K2, [-0.15, 0.05, -0.95], 'salto'], [K2 + 5, [0.55, 0.2, -0.6], 'out'], [K2 + 17, [1.9, 0, 0.15], 'out'], [K.salto_mostrador, [1.9, 0, 0.15]],
    [K.salto_mostrador + 7, [2.4, 2.5, -1.8], 'out'], [K.salto_mostrador + 14, [2.85, 1.0, -3.4], 'in'], [K3 - 1, [2.85, 1.0, -3.4]], [K3, [2.85, 1.4, -3.4], 'salto'], [K3 + 5, [2.9, 3.5, -3.4], 'out'], [K3 + 11, [2.9, 4.9, -3.4], 'out'], [K3 + 17, [2.9, 5.0, -3.4]],
    [K3 + 21, [2.9, 1.7, -3.4], 'in'], [K3 + 23, [2.9, 1.0, -3.4]], [L.C.f0 + 18, [2.9, 1.0, -3.4]], [L.C.f0 + 24, [2.3, 1.5, -2.9], 'out'], [L.C.f0 + 30, [1.65, 0, -2.55], 'in'], [KB - 1, [1.65, 0, -2.55]], [KB, [1.42, 0, -2.55], 'salto'], [KB + 8, [1.6, 0, -2.55]],
    [K4 - 1, [1.6, 0, -2.55]], [K4, [1.85, 0.1, -2.6], 'salto'], [K4 + 5, [2.25, 1.3, -3.6], 'out'], [K4 + 13, [2.6, 1.5, -5.7], 'out'], [K4 + 15, [2.55, 1.4, -5.6]], [K4 + 22, [2.0, 0, -4.7], 'in'], [K4 + 24, [2.0, 0, -4.7]], [K4 + 30, [2.5, 2.0, -3.6], 'out'], [K4 + 36, [2.9, 0, -2.6], 'in'],
    [K5 + 16, [2.9, 0, -2.6]], [K5 + 26, [1.4, 2.3, -4.6], 'out'], [K5 + 36, [-0.15, 0, -6.3], 'in'], [KR - 1, [-0.15, 0, -6.3]], [KR, [-0.12, 0.2, -6.4], 'salto'], [KR + 5, [-0.1, 1.3, -6.7], 'out'], [KR + 20, [0, 2.3, -7.25], 'out'],
    [RECOMPONE, [0, 0, -5.6], 'salto'], [RECOMPONE + 30, [0, 0, -5.6]], [RECOMPONE + 46, [0, 0, -5.1]], [K6 + 2, [0, 0, -5.1]], [K.implosion_fin, [0, 0.35, -5.1]], [K.implosion_fin + 6, [0, 0, -5.1], 'in'], [N, [0, 0, -5.1]]);
  pose('duda', [30, P.quieto], [46, P.quieto], [54, P.poder, 'back'], [57, P.poder], [60, P.pisoton, 'in'], [66, P.guardia], [K1 - 1, P.guardia], [K1, P.recibe, 'salto'], [K1 + 3, P.vuela], [K1 + 19, P.vuela], [K1 + 26, P.caido], [K1 + 34, P.caido], [K1 + 44, P.agachado], [K2 - 42, P.guardia],
    [K2 - 36, P.poder, 'back'], [K2 - 29, P.poder]);
  corre('duda', K2 - 28, K2 - 14);
  pose('duda', [K2 - 13, P.guardia], [K2 - 7, P.carga], [K2 - 1, P.carga], [K2, P.recibe, 'salto'], [K2 + 5, P.resbala], [K2 + 17, P.resbala], [K2 + 22, P.caido], [K2 + 46, P.caido], [K2 + 58, P.agachado], [K2 + 70, P.guardia],
    [K.cartel - 8, P.guardia], [K.cartel, P.carga, 'in'], [K.rival_ataca - 1, P.carga], [K.rival_ataca, P.golpe, 'salto'], [K.rival_ataca + 6, P.golpe], [K.rival_ataca + 12, P.guardia], [K.salto_mostrador - 3, P.agachado], [K.salto_mostrador + 4, P.recogido], [K.salto_mostrador + 12, P.recogido], [K.salto_mostrador + 15, P.agachado], [K.salto_mostrador + 22, P.guardia],
    [K3 - 1, P.guardia], [K3, P.recibe, 'salto'], [K3 + 4, P.vuela], [K3 + 21, P.vuela], [K3 + 23, P.caido], [K3 + 44, P.caido], [K3 + 56, P.agachado], [L.C.f0 + 16, P.agachado], [L.C.f0 + 22, P.recogido], [L.C.f0 + 31, P.agachado], [K.dibuja_espada, A(P.poder, 185), 'back'], [K.dibuja_espada + 12, A(P.poder, 185)], [KB - 14, Gd]);
  ataque('duda', KB, Gd, Cg, Gp, P.miraEspada, 3);
  pose('duda', [K4 - 1, P.miraEspada], [K4, P.recibe, 'salto'], [K4 + 4, P.vuela], [K4 + 15, P.vuela], [K4 + 22, P.agachado], [K4 + 24, P.agachado], [K4 + 28, P.recogido], [K4 + 34, P.recogido], [K4 + 37, P.agachado], [K5 - 6, P.guardia], [K5 - 1, P.recibe],
    [K5, P.agachado, 'salto'], [K5 + 14, P.agachado], [K5 + 18, P.recogido], [K5 + 34, P.recogido], [K5 + 37, P.agachado], [K5 + 46, P.guardia], [KR - 8, P.guardia], [KR - 1, P.recibe], [KR + 3, P.vuela], [KR + 22, P.vuela],
    [RECOMPONE, P.agachado, 'salto'], [RECOMPONE + 22, P.agachado], [RECOMPONE + 32, P.guardia], [K6 - 3, P.guardia], [K6, P.recibe, 'salto'], [K6 + 3, P.recogido], [N, P.recogido]);

  for (const q of ['tin', 'tan', 'duda']) for (const k of ['pos', 'pose', 'mira', 'cara', 'escala', 'visible']) { G[q][k].sort((a, b) => a[0] - b[0]); if (!G[q][k].length) G[q][k].push([0, k === 'escala' ? 1 : k === 'visible' ? true : null]); }
  G.tin.escala = [[0, 1]]; G.tan.escala = [[0, 1]];

  // ------------------------------------------------------------ extras por personaje: armas de tinta, lápiz, giro en el aire
  const vueltas = [[K1 + 2, K1 + 18, -5.2], [K3 + 4, K3 + 21, 3.1], [K4 + 4, K4 + 15, 4.4], [KR + 3, KR + 21, 7.0]];
  function extra(id, f) {
    if (id === 'tin') {
      const x = { lapiz: f < K.lapiz_a_tan };
      if (f >= K.dibuja_baston && f < K.mazo) x.arma = { tipo: 'baston', prog: entre(f, K.dibuja_baston, K.dibuja_baston + 11) };
      else if (f >= K.mazo && f < K.mazo + 9) x.arma = { tipo: 'mazo', bloque: EASE.back(entre(f, K.mazo, K.mazo + 7)) };
      else if (f >= K5 + 22 && f < K.armas_gotas + 10) x.arma = { tipo: 'baston', prog: f < K.armas_gotas ? entre(f, K5 + 22, K5 + 33) : 1 - entre(f, K.armas_gotas, K.armas_gotas + 9) };
      return x;
    }
    if (id === 'tan') {
      if (f >= K5 - 14 && f < K.armas_gotas + 10) return { arma: { tipo: 'mazo', prog: 1 - entre(f, K.armas_gotas, K.armas_gotas + 9), bloque: 1 - entre(f, K.armas_gotas, K.armas_gotas + 6) } };
      return null;
    }
    const x = {};
    if (f < 46) x.revela = entre(f, 30, 45);
    if (f >= RECOMPONE && f < RECOMPONE + 22) x.revela = entre(f, RECOMPONE, RECOMPONE + 20);
    if (f >= K.dibuja_espada && f < K4) x.arma = { tipo: 'espada', prog: entre(f, K.dibuja_espada, K.dibuja_espada + 11), rota: f >= KB };
    for (const [a, b, n] of vueltas) if (f >= a && f < b) x.giro = n * EASE.out(entre(f, a, b));
    if (f >= K5 && f < K5 + 16) x.aplasta = f < K5 + 10 ? 0.85 : 0.85 * (1 - entre(f, K5 + 10, K5 + 16));
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
  const plano = (tex, w, h) => { const o = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ map: tex, transparent: true, alphaTest: 0.5, side: THREE.DoubleSide })); o.visible = false; escena.add(o); return o; };
  const llamas = [];                                              // {o, x, y, z, tam(f) → alto en u (0 = apagada)}
  const llama = (x, y, z, tam) => { const o = plano(texLlama[0], 1, 1.25); llamas.push({ o, x, y, z, tam }); };
  const TV = [0, 2.3, -7.44];
  const fase = f => f < K.tele_punta + 12 ? 0 : f < K5 + 2 ? 0.9 * EASE.back(entre(f, K.tele_punta + 12, K.tele_punta + 18)) : f < K.tele_choque ? lerp(0.9, 1.9, EASE.back(entre(f, K5 + 2, K5 + 9))) : 0;
  llama(TV[0] + 0.25, TV[1] + 0.35, TV[2] + 0.2, fase);
  const resto = (a) => f => (f >= K.enfria && f < K.implosion + a ? 0.55 * (1 - 0.5 * entre(f, K.enfria, K.implosion)) * (1 - entre(f, K.implosion + a - 6, K.implosion + a)) : 0);
  llama(-0.9, 0.0, -7.0, resto(8)); llama(0.75, 0.0, -6.7, resto(12)); llama(0.1, 0.0, -7.6, resto(10));
  const bola = plano(texEstallido[0], 1, 1); bola.renderOrder = 5;

  // objetos de tinta que vuelan: la punta de la espada, el mazo que Tin le lanza a Tan y el lápiz
  const punta = plano(texDibujo(96, 32, (g) => { g.fillStyle = C.linea; g.beginPath(); g.moveTo(4, 6); g.lineTo(92, 16); g.lineTo(4, 26); g.lineTo(16, 16); g.closePath(); g.fill(); }), 0.6, 0.2);
  const mazoV = plano(texDibujo(256, 96, (g) => { g.strokeStyle = C.linea; g.fillStyle = C.linea; g.lineCap = 'round'; g.lineWidth = 14; g.beginPath(); g.moveTo(14, 48); g.lineTo(190, 48); g.stroke(); g.fillRect(176, 6, 62, 84); }), 1.3, 0.5);
  const lapizV = plano(texDibujo(160, 40, (g) => { g.strokeStyle = C.linea; g.lineWidth = 26; g.beginPath(); g.moveTo(8, 20); g.lineTo(120, 20); g.stroke(); g.strokeStyle = '#E8B33B'; g.lineWidth = 16; g.beginPath(); g.moveTo(26, 20); g.lineTo(118, 20); g.stroke(); g.strokeStyle = '#D9583B'; g.beginPath(); g.moveTo(10, 20); g.lineTo(26, 20); g.stroke(); g.fillStyle = C.linea; g.beginPath(); g.moveTo(118, 6); g.lineTo(154, 20); g.lineTo(118, 34); g.fill(); }), 0.42, 0.105);
  const vuelo = (o, f, f0, f1, a, b, alto, giros) => { if (f < f0 || f > f1) return false; const u = entre(f, f0, f1); o.visible = true; o.position.set(lerp(a.x, b.x, u), lerp(a.y, b.y, u) + alto * Math.sin(Math.PI * u), lerp(a.z, b.z, u) + 0.05); o.rotation.z = giros * u * 6.2832; return true; };
  // calcos del rival en los lanzamientos (K+2 a K+5): tres copias que se quedan atrás
  const calcos = [0.34, 0.22, 0.12].map(op => { const o = new THREE.Mesh(new THREE.PlaneGeometry(1, 1), new THREE.MeshBasicMaterial({ map: duda.tex, transparent: true, opacity: op, depthWrite: false })); o.visible = false; escena.add(o); return o; });
  const historia = [], LANZA = [K1, K2, K3, K4, KR].map(k => [k + 2, k + 7]);
  // grieta del mostrador (golpe 3) y marca final
  const texGrieta = texDibujo(640, 190, (g) => { g.strokeStyle = C.linea; g.lineWidth = 9; g.lineJoin = 'round'; g.lineCap = 'round'; g.beginPath(); g.moveTo(300, 0); for (const [x, y] of [[322, 40], [296, 78], [330, 120], [306, 150], [318, 190]]) g.lineTo(x, y); g.stroke(); g.lineWidth = 5; g.beginPath(); g.moveTo(322, 40); g.lineTo(370, 58); g.moveTo(296, 78); g.lineTo(250, 96); g.stroke(); });
  const grietaMostrador = plano(texGrieta, 2.4, 0.95); grietaMostrador.position.set(3.0, 0.48, -2.98);
  const gotaSuelo = new THREE.Mesh(new THREE.PlaneGeometry(1, 0.07), new THREE.MeshBasicMaterial({ color: C.linea })); gotaSuelo.rotation.x = -Math.PI / 2; gotaSuelo.visible = false; escena.add(gotaSuelo);
  const AST = [0, -5.1], GRIETA_SALIDA = [1.8, -5.1], CAJA_ROTA = [-1.64, -4.24];

  // ------------------------------------------------------------ roturas con nombre (A8: el daño se queda)
  const suelta = (obj, v, w, piso) => { escena.attach(obj); obj.userData = { v: V(...v), w: V(...w), quieto: false, piso }; trozos.push(obj); };
  const tirarCajas = (lista, n, dir) => { let k = 0; for (const c of lista) { if (k >= n) break; if (c.userData.caida) continue; c.userData.caida = true; k++; suelta(c, [dir * ra(0.6, 2.4), ra(0.5, 2.5), ra(-0.6, 1.6)], [ra(-6, 6), ra(-6, 6), ra(-6, 6)], 0.05); } };
  const polvo = (x, y, z, n = 10, d = 1.6) => soltar('polvoC', V(x, y, z), V(0, 0.9, 0), d, n);
  const gotas = (x, y, z, vx, n = 6) => soltar('gota', V(x, y, z), V(vx, 2.2, 0), 2.0, n);
  const animados = [];                                             // [f0, f1, fn(u)]
  const anima = (f0, f1, fn) => animados.push([f0, f1, fn]);
  const reg = Z.caja_registradora, regDesde = V(2.55, 1.25, -3.4), regHasta = V(CAJA_ROTA[0], 0.02, CAJA_ROTA[1]);

  const HECHOS = [
    [30, () => marca('trazo_de_tinta')],
    [60, () => { marca('choque_suelo'); marca('cajas_caen'); onda(0, -2.0, 0.3, 2.6, 0.4); polvo(0.2, 0.15, -1.9, 8); grieta(0.1, -2.0, 0.9, 6); tirarCajas(Z.pila_de_cajas.slice().reverse(), 3, -1); }],
    // golpe 1 · Tin, puño · estante izquierdo
    [K1 - 3, () => marca('silbido')], [K1 - 1, () => marca('golpe')],
    [K1, () => { estrella(V(-0.02, 1.55, -1.95), 0.6); gotas(-0.1, 1.6, -2.0, -3.2, 6); }],
    [K1 + 18, () => { marca('choque_madera'); marca('cajas_caen'); polvo(-2.4, 1.2, -5.7, 14, 2.2); tirarCajas(Z.estante_izquierdo.cajas, 8, 1); }],
    // golpe 2 · Tan, patada · postes de fila
    [K2 - 1, () => marca('golpe_agudo')],
    [K2, () => { estrella(V(-0.5, 1.2, -0.95), 0.6); gotas(-0.4, 1.3, -1.0, 3.2, 6); }],
    [K2 + 6, () => marca('roce_suelo')],
    [K2 + 18, () => { marca('postes_caen'); polvo(2.1, 0.2, 0.3, 8); for (const c of Z.postes_de_fila.cintas) c.visible = false; }],
    [K.cartel, () => { marca('choque_madera_agudo'); polvo(2.75, 1.0, -0.5, 6); const a = Z.cartel_de_pie.arriba; suelta(a, [1.2, 2.6, 0.8], [0.4, 1.2, -4.5], 0.06);  }],
    [K.rival_ataca - 2, () => marca('silbido')],
    // golpe 3 · Tin, gancho · mostrador
    [K3 - 1, () => { marca('golpe_grave'); marca('silbido_sube'); }],
    [K3, () => { estrella(V(2.62, 2.85, -3.2), 0.6); gotas(2.7, 2.9, -3.3, 0.5, 6); }],
    [K3 + 18, () => marca('silbido_caida')],
    [K3 + 22, () => { marca('choque_pilar'); polvo(2.9, 1.2, -3.2, 12, 2.0); grietaMostrador.visible = true; Z.mostrador.mitades[0].rotation.z = -0.03; Z.mostrador.mitades[1].rotation.z = 0.03; }],
    [K.dibuja_baston, () => marca('trazo_de_tinta')],
    [K.dibuja_espada, () => marca('trazo_de_tinta')],
    // bloqueo · la punta rota vuela y enciende el televisor
    [KB - 1, () => marca('bloqueo_tinta')],
    [KB, () => { estrella(V(0.98, 2.05, -2.5), 0.5); gotas(1.0, 2.0, -2.5, 0.2, 5); }],
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
    [K4, () => { estrella(V(1.7, 1.45, -2.5), 0.6); gotas(1.8, 1.5, -2.6, 3.0, 6); }],
    [K4 + 14, () => { marca('choque_madera'); marca('cajas_caen'); polvo(2.5, 1.5, -5.4, 12, 2.0); tirarCajas(Z.estante_derecho.cajas.slice(12), 6, -1); const b = Z.estante_derecho.baldas[2]; b.rotation.x = 0.5; b.position.y -= 0.22; b.position.x -= 0.12; }],
    [K.mazo, () => marca('trazo_de_tinta')], [K.mazo + 12, () => marca('silbido')],
    // golpe 5 · Tan, mazo de tinta · el mostrador se parte y la caja registradora sale despedida
    [K5 - 1, () => { marca('mazo_golpe'); marca('choque_madera'); }],
    [K5, () => {
      estrella(V(2.85, 0.85, -2.5), 0.6); gotas(2.9, 0.9, -2.6, 0, 7); polvo(2.9, 0.8, -3.0, 14, 2.4); grieta(2.9, -2.6, 1.1, 7); grietaMostrador.visible = false;
      const [a, b] = Z.mostrador.mitades; a.rotation.z = -0.24; a.position.y = -0.1; a.position.x -= 0.12; b.rotation.z = 0.24; b.position.y = -0.1; b.position.x += 0.12;
      escena.attach(reg.grupo);
    }],
    [K5 + 2, () => marca('fuego_crece')],
    [K5 + 18, () => { marca('campanilla_caja'); reg.rota = true; reg.gaveta.position.z += 0.28; reg.pantalla.rotation.z = 1.05; reg.pantalla.position.y -= 0.06; reg.cinta.visible = true; reg.cinta.position.set(-0.15, 0.02, 0.5); polvo(regHasta.x, 0.15, regHasta.z, 6); }],
    [K5 + 22, () => marca('trazo_de_tinta')],
    // remate · golpe doble · explosión por fases
    [K.carrera, () => marca('subida')],
    [KR - 1, () => marca('golpe_doble')],
    [KR, () => { estrella(V(-0.25, 1.35, -5.9), 0.6); estrella(V(0.0, 0.95, -5.9), 0.5); gotas(-0.1, 1.4, -6.0, 0, 8); }],
    [K.tele_choque, () => { marca('vidrio_grieta'); soltar('chispaC', V(0, 2.3, -7.1), V(0, 3, 1), 5, 14); }],
    [K.claro, () => marca('explosion')],
    [K.invertidos, () => {
      const t = Z.isla_televisor; t.tele.visible = false;
      for (let i = 0; i < 12; i++) { const c = caja(ra(0.2, 0.55), ra(0.15, 0.4), 0.1, i % 3 ? C.linea : C.utileria, 0.02); c.position.set(ra(-0.9, 0.9), ra(1.8, 2.8), -7.3); c.visible = false; c.userData.resto = true; escena.add(c); restos.push(c); }
    }],
    [K.bola, () => {
      for (const c of restos) { c.visible = true; c.userData = { v: V(ra(-5, 5), ra(3, 9), ra(0.5, 6)), w: V(ra(-9, 9), ra(-9, 9), ra(-9, 9)), quieto: false, piso: 0.1 }; trozos.push(c); }
      mancha(0, -7.4, 1.5, 0.5); mancha(0.2, -7.3, 0.85, 0.55, C.linea); grieta(0.1, -6.6, 1.6, 9); grieta(GRIETA_SALIDA[0], GRIETA_SALIDA[1], 0.45, 5); trazoSuelo([[1.55, -5.2], [1.72, -5.05], [1.86, -5.16], [2.05, -5.0]], 0.05);
      const g = Z.pared_fondo.lienzo.getContext('2d'); g.fillStyle = C.humo; g.globalAlpha = 0.5; g.beginPath(); const borron = (cx, cy, R0, n) => { g.beginPath(); for (let i = 0; i <= n; i++) { const a = i / n * 6.283, R = R0 * (0.62 + 0.38 * az()) * (1 + 0.5 * Math.max(0, -Math.sin(a))); g.lineTo(cx + Math.cos(a) * R * 1.25, cy + Math.sin(a) * R); } g.closePath(); g.fill(); }; borron(512, 560, 150, 40); g.globalAlpha = 0.55; borron(520, 590, 80, 30); Z.pared_fondo.tex.needsUpdate = true;
      for (const [i, b] of Z.banderines.lista.entries()) if (i > 3 && i < 9) for (const hijo of b.children) hijo.material = new THREE.MeshBasicMaterial({ color: hijo === b.children[0] ? C.linea : C.humo, side: THREE.DoubleSide });
      tirarCajas(Z.estante_izquierdo.cajas, 4, 1); tirarCajas(Z.estante_derecho.cajas, 4, -1); onda(0, -7.0, 0.5, 7.5, 0.55);
    }],
    [K.enfria, () => { marca('cola_explosion'); for (let i = 0; i < 26; i++) soltar('humoC', V(ra(-1.6, 1.6), ra(0.6, 3.6), ra(-7.2, -6.2)), V(0, 0.8, 0), 1.2, 1); }],
    // golpe 6 · Tin, bastón · implosión; queda un asterisco y lo último del trazo se escurre por la grieta
    [K6 - 1, () => marca('baston_golpe_grave')],
    [K6, () => { estrella(V(-0.1, 1.05, -5.05), 0.55); gotas(-0.05, 1.1, -5.1, 1.5, 5); }],
    [K.implosion, () => { marca('implosion'); onda(AST[0], AST[1], 3.6, 0.15, 0.5); }],
    [K.implosion + 5, () => onda(AST[0], AST[1], 2.8, 0.15, 0.42, 0.6)],
    [K.implosion + 10, () => onda(AST[0], AST[1], 2.0, 0.15, 0.3, 1.1)],
    [K.armas_gotas, () => { marca('gotas'); soltar('gota', tin.manoMundo.clone().add(V(0.4, 0.3, 0)), V(0, 0.5, 0), 1.0, 6); soltar('gota', tan.manoMundo.clone().add(V(-0.4, 0.5, 0)), V(0, 0.5, 0), 1.2, 7); despeja(); }],
    ...[0, 1, 2, 3, 4, 5].map(i => [K.asterisco + i, () => { marca('asterisco_tic'); const a = i * Math.PI / 3 + 0.26, r = 0.125; trazoSuelo([[AST[0], AST[1]], [AST[0] + Math.cos(a) * r, AST[1] + Math.sin(a) * r * 1.6]], 0.042); }]),
    [K.escurre, () => marca('escurre')],
    [K.lapiz_a_tan, () => marca('silbido_corto')],
    [K.lapiz_a_tan + 6, () => marca('atrapa')],
    [N - 1, () => { window.MEDIDAS.final = { mando_mostaza: window.proyecta(-2.36, 3.21, -9.72), caja_registradora_rota: window.proyecta(regHasta.x, 0.2, regHasta.z), asterisco: window.proyecta(AST[0], 0, AST[1]), grieta_salida: window.proyecta(GRIETA_SALIDA[0], 0, GRIETA_SALIDA[1]), televisor: window.proyecta(0, 2.3, -7.44), px_por_u_en_asterisco: Math.abs(window.proyecta(1, 0, AST[1])[0] - window.proyecta(0, 0, AST[1])[0]) }; }],
    [1, () => { window.MEDIDAS.inicio = { mando_mostaza: window.proyecta(-2.36, 3.21, -9.72), televisor_izq_arriba: window.proyecta(-1.2, 3.0, -7.44), televisor_der_abajo: window.proyecta(1.2, 1.6, -7.44), suelo_z0: window.proyecta(0, 0, 0), banderines_bajo: window.proyecta(0, 5.5, -9.5) }; }],
  ];
  HECHOS.sort((a, b) => a[0] - b[0]);
  const restos = [];
  // lo que se mueve a lo largo de varios fotogramas
  anima(K1 + 18, K1 + 24, u => { Z.estante_izquierdo.grupo.rotation.z = 0.21 * EASE.out(u); });
  anima(K2 + 18, K2 + 26, u => { Z.postes_de_fila.postes.forEach((p, i) => { p.rotation.z = -1.52 * EASE.in(clamp(u * 1.4 - i * 0.12)); p.rotation.y = 0.3 * i; }); });
  anima(K.invertidos, K.invertidos + 12, u => { const g = Z.isla_televisor.grupo; g.rotation.z = 1.42 * EASE.in(u); g.position.y = 0.25 * EASE.in(u); });
  anima(K.bola, K.bola + 16, u => { Z.banderines.grupo.rotation.z = -0.95 * EASE.back(u); });
  anima(K5 + 2, K5 + 18, u => { reg.grupo.position.set(lerp(regDesde.x, regHasta.x, u), lerp(regDesde.y, regHasta.y, u) + 2.6 * Math.sin(Math.PI * u), lerp(regDesde.z, regHasta.z, u)); reg.grupo.rotation.set(u * 5.2, 0.6 * u, u * 6.2832); if (u >= 1) { reg.grupo.rotation.set(0, 0.35, 0); reg.grupo.scale.setScalar(0.72); } });
  let corridos = null;
  anima(K.implosion, K.implosion_fin, u => {                        // la implosión arrastra cajas y papeles ≈ 0,5 u hacia el centro
    if (!corridos) corridos = trozos.filter(t => t.userData.quieto && Math.hypot(t.position.x - AST[0], t.position.z - AST[1]) < 4.5 && Math.hypot(t.position.x - AST[0], t.position.z - AST[1]) > 1.7).map(t => ({ t, de: t.position.clone() }));
    for (const c of corridos) { const d = V(AST[0] - c.de.x, 0, AST[1] - c.de.z); const l = d.length(); c.t.position.copy(c.de).addScaledVector(d.normalize(), Math.min(0.5, l - 1.2) * EASE.io(u)); }
  });

  // ------------------------------------------------------------ cada fotograma
  // zonas de conexión limpias: nada de escombros sobre la marca final, la salida por la grieta ni la caja registradora rota
  function despeja() {
    for (const t of trozos) {
      if (t === reg.grupo) continue; const p = t.position;
      const d = Math.hypot(p.x - AST[0], p.z - AST[1]); if (d < 1.0) { const a = d > 0.01 ? Math.atan2(p.z - AST[1], p.x - AST[0]) : 2.2; p.x = AST[0] + Math.cos(a) * 1.05; p.z = AST[1] + Math.sin(a) * 1.05; }
      if (p.x > -0.2 && p.x < 2.3 && Math.abs(p.z - AST[1]) < 0.4) p.z = AST[1] + (p.z < AST[1] ? -0.5 : 0.5);
      const c = Math.hypot(p.x - CAJA_ROTA[0], p.z - CAJA_ROTA[1]); if (c < 0.95) { p.x = CAJA_ROTA[0] + 1.05; p.z = CAJA_ROTA[1] - 0.5; }
    }
  }
  let hechoAnim = new Set();
  function cadaCuadro(f, dt) {
    for (const [i, [f0, f1, fn]] of animados.entries()) { if (f >= f0 && f <= f1) fn(entre(f, f0, f1)); else if (f > f1 && !hechoAnim.has(i)) { fn(1); hechoAnim.add(i); } }
    // llamas planas: 3 dibujos de 2 f; el borde cambia de forma, no parpadea
    for (const l of llamas) { const t = l.tam(f); l.o.visible = t > 0.02; if (!l.o.visible) continue; l.o.material.map = texLlama[Math.floor(f / 2) % 3]; l.o.scale.set(t, t, 1); l.o.position.set(l.x, l.y + t * 0.58, l.z); }
    if (f >= K.tele_punta + 22 && f < K.tele_choque && f % 5 === 0) soltar('humoC', V(TV[0] + ra(-0.2, 0.6), TV[1] + 1.0 + fase(f) * 0.9, TV[2] + 0.1), V(0, 1.0, 0), 0.5, 1);
    if (f >= K.enfria && f <= L.T9.f0 + 30 && f % 3 === 0) despeja();
    if (f >= K.enfria && f < K.implosion && f % 9 === 0) soltar('humoC', V(ra(-0.9, 0.9), 0.9, -6.9), V(0, 0.9, 0), 0.5, 1);
    // bola de fuego plana (f bola a enfría), 3 dibujos de 2 f; al enfriar se encoge
    const ub = entre(f, K.bola, K.enfria), ue = entre(f, K.enfria, K.enfria + 8);
    bola.visible = f >= K.bola && f < K.enfria + 8;
    if (bola.visible) { const t = lerp(2.2, 5.6, EASE.out(ub)) * (1 - 0.85 * EASE.in(ue)); bola.material.map = texEstallido[Math.floor(f / 2) % 3]; bola.scale.set(t, t, 1); bola.position.set(0, 3.1, -7.0); }
    // objetos que vuelan
    punta.visible = false; mazoV.visible = false; lapizV.visible = false;
    if (!vuelo(punta, f, KB + 2, KB + 13, V(0.98, 2.05, -2.5), V(TV[0] + 0.28, TV[1] + 0.25, TV[2] + 0.1), 0.9, 2.5) && f > KB + 13 && f < K.invertidos) { punta.visible = true; punta.position.set(TV[0] + 0.28, TV[1] + 0.25, TV[2] + 0.13); punta.rotation.z = 2.4; }
    vuelo(mazoV, f, K.mazo + 12, K.mazo + 17, V(0.5, 1.9, -2.3), V(lerp(-1.2, 1.2, entre(K.mazo + 17, K4 - 4, K5 - 14)) - 0.1, 1.9, -2.6), 0.7, 1);
    vuelo(lapizV, f, K.lapiz_a_tan, K.lapiz_a_tan + 6, V(-0.75, 1.5, -4.3), V(1.22, 1.55, -4.9), 0.8, 1.5);
    // calcos del rival
    historia.unshift({ p: duda.malla.position.clone(), s: duda.malla.scale.clone(), r: duda.malla.rotation.z }); historia.length = Math.min(historia.length, 8);
    const lanza = LANZA.some(([a, b]) => f >= a && f <= b);
    calcos.forEach((o, i) => { const h = historia[(i + 1) * 2]; o.visible = lanza && !!h && duda.malla.visible; if (o.visible) { o.position.copy(h.p); o.position.z -= 0.02 * (i + 1); o.scale.copy(h.s); o.rotation.z = h.r; } });
    // implosión: tinta que se recoge hacia el centro; se lleva el humo
    if (f >= K.implosion && f < K.implosion_fin) soltar('gota', V(AST[0] + ra(-2.0, 2.0), ra(0.2, 2.6), AST[1] + ra(-0.8, 0.8)), V(0, 0, 0), 0.1, 3, V(AST[0], 0.5, AST[1]));
    // lo último del trazo se escurre por la grieta del suelo (16 f)
    gotaSuelo.visible = f >= K.escurre && f <= K.escurre_fin;
    if (gotaSuelo.visible) { const u = entre(f, K.escurre, K.escurre_fin), x = lerp(AST[0] + 0.2, GRIETA_SALIDA[0], EASE.io(u)), largo = 0.5 * Math.sin(Math.PI * Math.min(1, u * 1.15)) + 0.04; gotaSuelo.scale.set(largo, 1, 1); gotaSuelo.position.set(x - largo / 2 * (u > 0.8 ? 1 : 0.4), 0.02, AST[1]); }
  }

  // ------------------------------------------------------------ cámara: sin inclinación, sin temblor; se corta
  function camaraDe(f, cam) {
    let p = T.planos[0]; for (const q of T.planos) if (f >= q.f0) p = q;
    const D = lerp(p.D, p.D1, entre(f, p.f0, p.f1 - 1));
    cam.position.set(p.cx, p.h, p.z + D); cam.lookAt(p.cx, p.h + (p.sube || 0), p.z);
  }
  // reloj de la escena (A2): solo frena o acelera la física (humo, polvo, trozos); la voz nunca cambia
  const LENTOS = [[K1 + 6, K1 + 17, 0.25], [K2 + 6, K2 + 17, 0.25], [K3 + 6, K3 + 17, 0.25], [KB + 2, KB + 13, 0.3], [K4 + 6, K4 + 13, 0.25], [K5 + 6, K5 + 17, 0.25], [K.carrera, K.carrera + 10, 0.3], [KR + 6, KR + 20, 0.25], [K2 - 28, K2 - 14, 1.3], [K.salto_mostrador + 3, K3 - 14, 1.3]];
  const reloj = f => { for (const [a, b, v] of LENTOS) if (f >= a && f <= b) return v; return 1; };

  const caras = ['duda_0', 'duda_1', 'duda_2', 'duda_3'];
  for (const p of ['tin', 'tan']) for (const e of ['curiosidad', 'sorpresa', 'eureka', 'risa', 'concentrado']) caras.push(`${p}_${e}`);
  return { porFotogramas: true, FIN: N, velocidad: () => 1, reloj, G, CAM: null, camara: camaraDe, HECHOS, caras, cadaCuadro, extra };
}
