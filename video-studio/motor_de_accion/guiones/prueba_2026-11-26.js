// Guion de la prueba técnica del 2026-11-26 (sin tema): quién hace qué y cuándo. Salió de escena.html sin cambios.
// Contrato de todo guion: guion(m) → { FIN, velocidad(S), G, CAM, HECHOS, caras, cadaCuadro(S, dS) }.
// «m» trae lo que ofrece el motor: poses, efectos, daños, sonidos (marca) y las piezas del entorno.
export const FICHA = { id: 'prueba_2026-11-26', entorno: 'ciudad_de_carton', creado: '2026-11-26' };

export function guion(m) {
  const { THREE, P, V, EASE, clamp, ra, marca, grieta, quemadura, garabatoResto, onda, soltar, estrella, focos, romperCajones, empujarTrozos, estado, entorno, personajes } = m;
  const { tin, tan, duda } = personajes, { pilar } = entorno;
  const GOLPE = 1.35, CHOQUE = 1.62, EXPLO = 2.62, PATADA = 3.55, FINAL = 4.25, IMPLO = 4.45, FIN = 5.6;
  const LENTO = [[GOLPE - 0.02, GOLPE + 0.075, 0.2], [EXPLO - 0.01, EXPLO + 0.14, 0.45], [PATADA - 0.03, PATADA + 0.07, 0.2], [FINAL - 0.02, FINAL + 0.07, 0.22]];
  function velocidad(S) { for (const [a, b, v] of LENTO) if (S >= a && S < b) return v; return 1.18; }   // cámara lenta en cada impacto; el resto, algo acelerado
  
  const G = {
    tin: {
      pos: [[0, [3.2, 0, 0.8]], [1.12, [3.3, 0, 0.8]], [1.33, [1.05, 0, 0.3], 'in'], [1.75, [1.5, 0, 0.5]], [EXPLO, [1.6, 0, 0.6]], [2.72, [3.0, 0.5, 0.9], 'out'], [3.05, [4.3, 0, 1.0], 'out'], [3.9, [4.2, 0, 1.0]], [4.22, [1.0, 0, 0.1], 'in'], [4.7, [1.4, 0, 0.6]], [FIN, [1.6, 0, 0.9]]],
      pose: [[0, P.guardia], [0.45, P.guardia], [0.55, P.recibe, 'out'], [0.8, P.guardia], [0.95, P.guardia], [1.12, P.carga], [1.24, P.embiste, 'in'], [1.33, P.golpe, 'in'], [1.55, P.golpe], [1.8, P.guardia], [EXPLO, P.guardia], [2.7, P.vuela, 'out'], [3.0, P.resbala], [3.35, P.guardia], [3.88, P.carga], [4.05, P.embiste, 'in'], [4.22, P.golpe, 'in'], [4.5, P.golpe], [4.9, P.guardia], [5.2, P.festeja, 'back']],
      mira: [[0, -1]], cara: [[0, 'sorpresa'], [0.8, 'concentrado'], [1.3, 'eureka'], [1.8, 'curiosidad'], [EXPLO, 'sorpresa'], [3.35, 'concentrado'], [4.2, 'eureka'], [5.05, 'risa']], escala: [[0, 1]],
    },
    tan: {
      pos: [[0, [-3.5, 0, 1.2]], [EXPLO, [-3.5, 0, 1.2]], [2.72, [-4.3, 0.4, 1.4], 'out'], [2.98, [-4.9, 0, 1.5], 'out'], [3.34, [-2.6, 0, -0.5], 'lin'], [3.46, [-1.9, 1.5, -0.45], 'out'], [3.55, [-1.25, 1.25, -0.4], 'in'], [3.8, [-1.7, 0, -0.2], 'in'], [4.1, [-1.7, 0, -0.2]], [4.22, [-1.15, 0, -0.1], 'in'], [4.7, [-1.6, 0, 0.5]], [FIN, [-1.9, 0, 0.9]]],
      pose: [[0, P.guardia], [0.45, P.guardia], [0.55, P.recibe, 'out'], [0.85, P.guardia], [EXPLO, P.guardia], [2.7, P.vuela, 'out'], [2.98, P.resbala], [3.08, P.corre1], [3.17, P.corre2, 'lin'], [3.26, P.corre1, 'lin'], [3.34, P.agachado, 'lin'], [3.46, P.recogido, 'out'], [3.54, P.patada, 'in'], [3.7, P.patada], [3.85, P.agachado], [4.05, P.carga], [4.22, P.golpe, 'in'], [4.5, P.golpe], [4.9, P.guardia], [5.2, P.festeja, 'back']],
      mira: [[0, 1]], cara: [[0, 'sorpresa'], [0.85, 'curiosidad'], [EXPLO, 'sorpresa'], [3.05, 'concentrado'], [3.45, 'eureka'], [5.05, 'risa']], escala: [[0, 1]],
    },
    duda: {
      pos: [[0, [0, 10, 0]], [0.45, [0, 0, 0], 'in'], [GOLPE, [0, 0, 0]], [1.5, [-1.8, 1.3, -1.2], 'out'], [CHOQUE, [-3.0, 0.5, -1.9], 'lin'], [1.75, [-3.0, 0, -1.7], 'in'], [2.75, [-3.0, 0, -1.7]], [2.95, [-1.6, 2.3, -1.1], 'out'], [3.15, [-0.2, 0, -0.4], 'in'], [PATADA, [-0.2, 0, -0.4]], [3.8, [0.25, 0, -0.3], 'out'], [FINAL, [0.2, 0, -0.3]], [FIN, [0.1, 0, -0.3]]],
      pose: [[0, P.recogido], [0.4, P.recogido], [0.47, P.agachado, 'lin'], [0.8, P.guardia, 'back'], [GOLPE - 0.03, P.guardia], [GOLPE + 0.02, P.recibe, 'out'], [1.5, P.vuela], [CHOQUE, P.vuela], [1.75, P.caido], [1.95, P.caido], [2.2, P.agachado], [2.45, P.poder, 'back'], [2.56, P.poder], [EXPLO, P.pisoton, 'in'], [2.75, P.agachado], [2.95, P.recogido], [3.13, P.recogido], [3.2, P.agachado, 'lin'], [3.4, P.guardia], [PATADA - 0.02, P.guardia], [PATADA + 0.03, P.recibe, 'out'], [3.95, P.resbala], [FINAL - 0.02, P.guardia], [FINAL + 0.03, P.recibe, 'out'], [4.5, P.poder], [4.95, P.recogido, 'in']],
      mira: [[0, 1], [1.4, 1], [1.9, 1], [3.15, -1], [3.85, 1], [FINAL, -1]], cara: [[0, 'duda']],
      escala: [[0, 1.0], [2.15, 1.0], [2.5, 1.45, 'back'], [PATADA, 1.45], [3.75, 1.15, 'out'], [FINAL, 1.15], [IMPLO, 1.1], [4.98, 0.04, 'in'], [FIN, 0.04]],
    },
  };
  const CAM = {
    pos: [[0, [0.6, 6.2, 9.5]], [0.45, [0.4, 4.6, 10.5], 'in'], [0.9, [1.6, 2.3, 12.6]], [GOLPE, [2.0, 2.3, 11.8], 'in'], [1.75, [-1.9, 2.3, 11.6], 'out'], [2.45, [-2.6, 2.0, 10.6]], [2.9, [-0.6, 2.9, 14.2], 'out'], [PATADA, [-1.6, 2.2, 11.6], 'in'], [3.95, [0.2, 2.1, 11.0]], [FINAL, [0.5, 2.2, 11.4], 'in'], [4.6, [0.4, 2.2, 10.4]], [FIN, [3.2, 3.6, 12.8]]],
    mira: [[0, [0, 0.6, 0]], [0.45, [0, 0.9, 0]], [0.9, [0, 1.5, 0]], [GOLPE, [0.6, 1.7, 0]], [1.75, [-2.4, 1.2, -1.4]], [2.45, [-2.8, 1.8, -1.6]], [2.9, [-0.8, 1.6, -0.6]], [PATADA, [-0.5, 2.0, -0.4]], [3.95, [0.1, 1.5, -0.3]], [FINAL, [0.2, 1.7, -0.3]], [4.6, [0.1, 1.3, -0.3]], [FIN, [-0.5, 1.2, -0.7]]],
  };
  const HECHOS = [
    [0.02, () => marca('silbido_caida')],
    [0.45, () => { marca('choque_suelo'); grieta(0, 0, 2.2); onda(0, 0, 0.3, 4.2, 0.55); soltar('polvo', V(0, 0.2, 0), V(0, 1.5, 0), 3.2, 26); estado.temblor = 0.28; }],
    [1.14, () => marca('silbido')],
    [GOLPE, () => { marca('golpe'); estrella(V(0.25, 2.3, 0.4), 1.25); soltar('chispa', V(0.3, 2.0, 0.3), V(-3, 2, 0), 3, 12); soltar('tinta', V(0.2, 2.0, 0.2), V(-3.5, 2.5, 0), 2.2, 7); estado.temblor = 0.1; }],
    [CHOQUE, () => { marca('choque_madera'); romperCajones(-1); soltar('polvo', V(-3.0, 0.8, -1.8), V(0, 1.2, 0), 2.6, 22); soltar('humo', V(-3.0, 0.6, -1.8), V(0, 1, 0), 1.5, 6); grieta(-3.0, -1.7, 1.2, 6); estado.temblor = 0.2; }],
    [2.2, () => marca('fuego_enciende')],
    [EXPLO, () => {
      marca('explosion'); const p = V(-3.0, 0.3, -1.7);
      soltar('fuego', p.clone().setY(1.0), V(0, 3.5, 0), 5.5, 60); soltar('humo', p.clone().setY(1.2), V(0, 2.6, 0), 3.6, 22); soltar('chispa', p.clone().setY(1.0), V(0, 6, 0), 8, 40);
      onda(p.x, p.z, 0.4, 9.5, 0.6); onda(p.x, p.z, 0.2, 6.0, 0.75); quemadura(p.x, p.z, 2.3); grieta(p.x, p.z, 2.8, 12); empujarTrozos(p.x, p.z, 16); estado.temblor = 0.42;
      focos.push({ pos: V(-3.6, 0.2, -1.1), tipo: 'fuego', desde: EXPLO, hasta: 99, cada: 0.035, ancho: 0.35 }, { pos: V(-2.1, 0.2, -2.2), tipo: 'fuego', desde: EXPLO, hasta: 99, cada: 0.05, ancho: 0.3 },
        { pos: V(-3.0, 0.6, -1.7), tipo: 'humo', desde: EXPLO, hasta: 99, cada: 0.22, ancho: 0.5 });
    }],
    [3.16, () => { marca('choque_suelo'); soltar('polvo', V(-0.2, 0.2, -0.4), V(0, 1.2, 0), 2.6, 16); onda(-0.2, -0.4, 0.3, 3.2, 0.45); grieta(-0.2, -0.4, 1.4, 6); estado.temblor = 0.18; }],
    [3.2, () => { marca('choque_pilar'); soltar('polvo', V(5.6, 0.3, -2.3), V(0, 1.4, 0), 3, 20); grieta(5.4, -2.3, 1.6, 7); estado.temblor = Math.max(estado.temblor, 0.16); }],
    [3.3, () => marca('silbido')],
    [PATADA, () => { marca('golpe'); estrella(V(-0.55, 2.9, -0.2), 1.35); soltar('chispa', V(-0.6, 2.6, -0.3), V(3, 2, 0), 3, 14); soltar('tinta', V(-0.5, 2.6, -0.3), V(3.5, 2.5, 0), 2.2, 8); estado.temblor = 0.12; }],
    [4.05, () => marca('silbido')],
    [FINAL, () => { marca('golpe_doble'); estrella(V(0.6, 2.5, 0.1), 1.15); estrella(V(-0.35, 2.3, 0.1), 1.15); soltar('chispa', V(0.2, 2.1, 0), V(0, 4, 0), 5, 22); estado.temblor = 0.16; }],
    [IMPLO, () => { marca('implosion'); onda(0.15, -0.3, 6.5, 0.2, 0.5); onda(0.15, -0.3, 4.2, 0.2, 0.42, 1.4); }],
    [4.98, () => { marca('estallido_final'); soltar('humo', V(0.15, 1.2, -0.3), V(0, 1.6, 0), 2.4, 18); soltar('chispa', V(0.15, 1.2, -0.3), V(0, 3, 0), 5, 18); garabatoResto(0.15, -0.3); onda(0.15, -0.3, 0.2, 3.0, 0.4); estado.temblor = 0.12; }],
  ];
  focos.push({ seguir: () => duda.cabezaMundo && duda.cabezaMundo.clone().add(V(0, 0.5, 0.05)), tipo: 'fuego', desde: 2.2, hasta: IMPLO, cada: 0.022, ancho: 0.6 },
    { seguir: () => duda.cabezaMundo && duda.cabezaMundo.clone().add(V(0, 0.9, -0.05)), tipo: 'humo', desde: 2.3, hasta: IMPLO, cada: 0.07, ancho: 0.5 });
  
  const caras = ['duda_0', 'duda_1', 'duda_2', 'duda_3'];
  for (const p of ['tin', 'tan']) for (const e of ['curiosidad', 'sorpresa', 'eureka', 'risa', 'concentrado']) caras.push(`${p}_${e}`);
  function cadaCuadro(S, dS) {
    if (S > IMPLO && S < 4.98) soltar('tinta', duda.cabezaMundo.clone().add(V(ra(-2.4, 2.4), ra(-1.2, 2.2), ra(-1.4, 1.4))), V(0, 0, 0), 0.1, 3, duda.cabezaMundo.clone().setY(1.2));
    duda.malla.visible = S < 4.98;
    // el pilar cae con la explosión y se queda caído
    pilar.rotation.z = -EASE.in(clamp((S - (EXPLO + 0.05)) / 0.5)) * Math.PI / 2 * 0.985;
  }
  return { FIN, velocidad, G, CAM, HECHOS, caras, cadaCuadro };
}
