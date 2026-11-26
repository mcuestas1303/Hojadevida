// Vista de comprobación del entorno «tienda_de_videojuegos»: no es un video. Coloca a Tin y a Tan en su marca de portada
// y enseña las cinco cámaras de la dirección del short 4 (sección 3), una cada 2 fotogramas.
export const FICHA = { id: 'vista_tienda', entorno: 'tienda_de_videojuegos', creado: '2026-11-26' };
export function guion({ P }) {
  const c = (i, p, m) => [[i / 15, p, 'salto'], [i / 15, m, 'salto']];
  const CAMS = [[[0, 2.4, 13.5], [0, 2.1, 0]], [[0, 5.2, 14], [0, 1.6, -3]], [[-1.6, 1.3, 8.5], [0, 1.5, 0]], [[1.6, 1.3, 8.5], [0, 1.5, 0]], [[0, 0.5, 6], [0, 4, -8]], [[3.0, 0.6, -0.4], [2.3, 4, -3.4]]];
  const CAM = { pos: CAMS.map((k, i) => [i / 15, k[0], 'salto']), mira: CAMS.map((k, i) => [i / 15, k[1], 'salto']) };
  CAM.pos[0].pop(); CAM.mira[0].pop();
  const G = {
    tin: { pos: [[0, [1.28, 0, 0]]], pose: [[0, P.quieto]], mira: [[0, -1]], cara: [[0, 'curiosidad']], escala: [[0, 1]] },
    tan: { pos: [[0, [-1.28, 0, 0]]], pose: [[0, P.quieto]], mira: [[0, 1]], cara: [[0, 'curiosidad']], escala: [[0, 1]] },
    duda: { pos: [[0, [0, 0, -2.5]]], pose: [[0, P.guardia]], mira: [[0, 1]], cara: [[0, 'duda']], escala: [[0, 1.5]] },
  };
  return { FIN: 99, velocidad: () => 2, G, CAM, HECHOS: [], caras: ['duda_0', 'duda_1', 'duda_2', 'duda_3', 'tin_curiosidad', 'tan_curiosidad'] };
}
