'use strict';

/* ============================================================
   Creador de personajes · vista previa sin costo
   Dibuja un boceto SVG del personaje y arma el prompt para Higgsfield.
   Todo corre en el navegador: no llama a ninguna API ni gasta créditos.
   ============================================================ */

const $ = (id) => document.getElementById(id);
const CLAVE = 'creador-personajes:v1';

/* ---------- Paletas: [hex, nombre en español, nombre en inglés] ---------- */
const PAL = {
  piel: [
    ['#f8d9c4', 'clara', 'fair'], ['#eebb99', 'clara cálida', 'light warm'], ['#d9a07a', 'trigueña', 'tan'],
    ['#b97a53', 'morena', 'medium brown'], ['#8d5a3b', 'morena oscura', 'brown'], ['#5c3a24', 'oscura', 'deep brown'],
    ['#9fd8a0', 'verde fantasía', 'fantasy green'], ['#a9c6f0', 'azul fantasía', 'fantasy pale blue']
  ],
  colorCabello: [
    ['#1d1a1a', 'negro', 'black'], ['#3b2a20', 'castaño oscuro', 'dark brown'], ['#7a4b2a', 'castaño', 'brown'],
    ['#d9b26b', 'rubio', 'blonde'], ['#f2efe6', 'desteñido casi blanco', 'bleached almost-white'],
    ['#f28c28', 'naranja', 'orange'], ['#ff6a00', 'naranja neón', 'glowing neon orange'],
    ['#ff2fa0', 'rosa neón', 'neon pink'], ['#7dff3a', 'verde lima', 'lime green'], ['#8a4dff', 'violeta', 'violet'],
    ['#2fd4ff', 'cian', 'cyan'], ['#c8102e', 'rojo', 'red'], ['#8c8c8c', 'gris', 'grey']
  ],
  ojos: [
    ['#4a2c17', 'cafés', 'brown'], ['#b7852f', 'miel', 'honey'], ['#3f8f3a', 'verdes', 'bright green'],
    ['#3a77c2', 'azules', 'blue'], ['#6b6b6b', 'grises', 'grey'], ['#8a4dff', 'violetas', 'violet']
  ],
  labios: [
    [null, 'natural', ''], ['#c2185b', 'frambuesa', 'raspberry lipstick'], ['#e53935', 'rojo', 'red lipstick'],
    ['#ad6f5a', 'nude', 'nude lipstick'], ['#222222', 'negro', 'black lipstick']
  ],
  colorRopa: [
    ['#6c4cf1', 'violeta', 'violet'], ['#5b2a86', 'morado', 'purple'], ['#5b6b3a', 'verde oliva', 'olive green'],
    ['#d9a21b', 'mostaza', 'mustard'], ['#1b1b1f', 'negro', 'black'], ['#c8102e', 'rojo', 'red'],
    ['#2f6db5', 'azul', 'blue'], ['#f4efe6', 'blanco roto', 'off-white'], ['#c0c4cc', 'plateado', 'shiny metallic silver'],
    ['#7a5c43', 'café', 'brown']
  ],
  fondo: [
    ['#ffffff', 'blanco', 'white'], ['#ffd6e0', 'rosa', 'pink'], ['#d6f5ff', 'celeste', 'light blue'],
    ['#fff3c4', 'crema', 'cream'], ['#1e1c2a', 'noche', 'dark night'], ['#e9ffd6', 'menta', 'mint']
  ]
};
const NEON = ['#ff6a00', '#ff2fa0', '#7dff3a', '#2fd4ff'];

/* ---------- Opciones: valor → [etiqueta en español, frase en inglés para el prompt] ---------- */
const OP = {
  genero: { femenino: ['Femenino', 'woman'], masculino: ['Masculino', 'man'], nobinario: ['No binario', 'non-binary person'] },
  estiloImagen: {
    realista: ['Foto realista', 'Realistic photo'],
    comic: ['Cómic 2D', '2D comic book illustration with thick ink lines, flat colors and hard shadows']
  },
  proporciones: {
    normal: ['Normales', ''],
    alto: ['Altísimo y flaco', 'absurdly tall and stick-thin with extra-long arms'],
    bajito: ['Bajito y robusto', 'short and stocky'],
    caricatura: ['Caricatura (cabeza grande)', 'cartoonishly oversized head on a small body']
  },
  cabello: {
    corto: ['Corto', 'short hair'],
    largo: ['Largo', 'long flowing hair'],
    afro: ['Afro / rizado', 'a big perfectly round curly afro'],
    mono: ['Moño', 'hair tied in a bun'],
    coleta: ['Coleta', 'hair in a ponytail'],
    mullet: ['Mullet', 'a messy mullet'],
    puas: ['Púas punk', 'a giant crown of rigid punk liberty spikes, about a dozen spikes each as long as a forearm, perfectly stiff and glossy'],
    cresta: ['Cresta', 'a tall mohawk'],
    cono: ['Cono eléctrico', 'hair standing straight up in a perfect tall cone as if electrified'],
    rapado: ['Rapado', 'a buzzcut'],
    calvo: ['Calvo', 'a bald head']
  },
  estiloOjos: {
    normales: ['Normales', 'expressive'], grandes: ['Grandes', 'big round'],
    entrecerrados: ['Entrecerrados', 'half-closed sleepy'], felices: ['Felices (^ ^)', 'happy squinting']
  },
  expresion: {
    sonrisa: ['Sonrisa', 'a gentle smile'], carcajada: ['Gran sonrisa', 'a wide cheeky full-toothed grin'],
    seria: ['Seria', 'a deadpan serious expression'], sorpresa: ['Sorpresa', 'a surprised open mouth'],
    picara: ['Pícara', 'a mischievous smirk'], chicle: ['Chicle', 'blowing a big pink bubblegum bubble']
  },
  orejas: { normales: ['Normales', ''], puntiagudas: ['Puntiagudas', 'pointed elf-like ears'] },
  barba: { ninguna: ['Ninguna', ''], bigote: ['Bigote', 'a mustache'], corta: ['Corta', 'a short beard'], completa: ['Completa', 'a full thick beard'] },
  ropa: {
    camiseta: ['Camiseta', 't-shirt'],
    chandal: ['Chándal de terciopelo', 'oversized shiny velvet tracksuit with enormous padded shoulders'],
    cardigan: ['Cárdigan', 'oversized cardigan over a striped t-shirt'],
    blazer: ['Blazer', 'tailored blazer over a white shirt'],
    deportiva: ['Chaqueta deportiva', 'sport jacket with red piping'],
    bata: ['Bata de laboratorio', 'oversized white lab coat covered in colorful stickers and dangling audio cables'],
    puffer: ['Chaqueta puffer', 'gigantic puffer jacket three sizes too big'],
    bomber: ['Bomber', 'bomber jacket with a lightning patch on the sleeve']
  },
  accesorio: {
    ninguno: ['Ninguno', ''], lentes: ['Lentes redondos', 'round glasses'],
    sol: ['Lentes de sol naranjas', 'round orange-tinted sunglasses'], corazon: ['Lentes de corazón', 'heart-shaped red sunglasses'],
    steampunk: ['Gafas steampunk', 'huge brass steampunk goggles on the forehead'],
    audifonos: ['Audífonos gigantes', 'headphones the size of dinner plates around the neck'],
    boa: ['Boa de plumas', 'a fluffy neon-yellow feather boa'], cadenas: ['Cadenas de oro', 'chunky gold chains'],
    bandana: ['Bandana azul', 'a blue patterned tube headband on the forehead'], gorra: ['Gorra', 'a baseball cap']
  },
  nicho: {
    musica: ['Música', 'music'], comedia: ['Comedia', 'comedy'], moda: ['Moda', 'fashion'], gaming: ['Gaming', 'gaming'],
    fitness: ['Fitness', 'fitness'], viajes: ['Viajes', 'travel'], tecnologia: ['Tecnología', 'tech'], cocina: ['Cocina', 'cooking']
  },
  tono: {
    cercano: ['Cercano y amigable', 'warm and friendly'], humor: ['Humor absurdo', 'absurd deadpan humor'],
    inspirador: ['Inspirador', 'inspiring'], misterioso: ['Misterioso', 'mysterious'],
    educativo: ['Educativo', 'educational'], dramatico: ['Dramático', 'over-the-top dramatic']
  }
};

const RASGOS = [
  ['alegre', 'cheerful'], ['inteligente', 'smart'], ['rebelde', 'rebellious'], ['optimista', 'optimistic'],
  ['audaz', 'bold'], ['amable', 'kind'], ['elegante', 'elegant'], ['sensible', 'sensitive'],
  ['irreverente', 'irreverent'], ['sociable', 'outgoing'], ['perseverante', 'determined'], ['humilde', 'humble']
];
const PLATAFORMAS = ['YouTube Shorts', 'TikTok', 'Instagram', 'Facebook'];

const IDEAS = {
  musica: ['Explico un beat absurdo en 15 segundos', 'Convierto un sonido cotidiano en canción', 'Duelo de teclados con un invitado', 'Así nace una canción en un minuto'],
  comedia: ['Sketch de 15 segundos con remate', 'Un personaje histórico descubre algo moderno', 'Expectativa contra realidad', 'Reacción exagerada a una noticia rara'],
  moda: ['Outfit del día en 3 cambios', 'Una prenda, cinco formas de usarla', 'Reacciono a las tendencias de la semana', 'Armario cápsula para 7 días'],
  gaming: ['El momento más absurdo de la partida', 'Ranking de personajes en 30 segundos', 'Reto: ganar sin usar el botón principal', 'Reacciono al tráiler de la semana'],
  fitness: ['Rutina de 5 minutos sin equipo', 'Mito o verdad del gimnasio', 'Lo que como en un día', 'Reto de 7 días con seguidores'],
  viajes: ['Un lugar en 15 segundos', 'Cuánto gasté en un día', 'Errores que no cometería otra vez', 'La comida más rara del viaje'],
  tecnologia: ['Una app útil que nadie conoce', 'Explico la noticia tech en 30 segundos', 'Pruebo un truco viral', 'Antes y después con IA'],
  cocina: ['Receta en 30 segundos', 'Arreglo una receta que salió mal', 'Pruebo una receta viral', 'Cocino con lo que quedó en la refri']
};

/* ---------- Personajes de partida (originales de este proyecto) ---------- */
const BASE = {
  nombre: '', handle: '', edad: 25, genero: 'masculino', ciudad: '', virtual: true,
  estiloImagen: 'realista', proporciones: 'normal', piel: '#eebb99', cabello: 'corto', colorCabello: '#3b2a20',
  estiloOjos: 'normales', ojos: '#4a2c17', expresion: 'sonrisa', orejas: 'normales', barba: 'ninguna', labios: null,
  pecas: false, ojeras: false, ropa: 'camiseta', colorRopa: '#6c4cf1', accesorio: 'ninguno', fondo: '#ffffff', extras: '',
  nicho: 'comedia', rasgos: [], tono: 'humor', plataformas: ['YouTube Shorts'], publico: '', frase: '', historia: ''
};

const PRESETS = {
  vacio: ['Personaje nuevo (en blanco)', {}],
  spike: ['Spike', {
    nombre: 'Spike', handle: 'spike.beats', edad: 25, genero: 'masculino', proporciones: 'alto', piel: '#f8d9c4',
    cabello: 'puas', colorCabello: '#ff6a00', estiloOjos: 'grandes', ojos: '#3f8f3a', expresion: 'chicle', pecas: false,
    ropa: 'chandal', colorRopa: '#5b2a86', accesorio: 'boa', fondo: '#ffffff',
    extras: 'thick bleached eyebrows, chunky rings on every finger, huge white platform sneakers, dramatic rock-star pose',
    nicho: 'musica', rasgos: ['irreverente', 'audaz', 'sociable'], tono: 'humor', plataformas: ['YouTube Shorts', 'TikTok', 'Instagram'],
    publico: 'jóvenes de 18 a 30 que aman la música electrónica y el humor absurdo', frase: 'Esto no es un beat, es una emoción.',
    historia: 'Tecladista excéntrico que explica cosas absurdas con total seriedad.'
  }],
  cientifico: ['El científico (en reserva)', {
    nombre: 'El científico', handle: 'dr.voltaje', edad: 35, genero: 'masculino', proporciones: 'alto', piel: '#f8d9c4',
    cabello: 'cono', colorCabello: '#ff6a00', estiloOjos: 'grandes', ojos: '#4a2c17', expresion: 'seria',
    ropa: 'bata', colorRopa: '#f4efe6', accesorio: 'steampunk', fondo: '#ffffff',
    extras: 'giant headphones around his neck, very long legs in shiny red tights and pointy black boots, one eyebrow raised impossibly high, intense mad-genius stare',
    nicho: 'musica', rasgos: ['inteligente', 'irreverente'], tono: 'dramatico', plataformas: ['YouTube Shorts', 'TikTok'],
    frase: 'Si explota, es que funciona.', historia: 'Inventor que trata cada beat como un experimento peligroso.'
  }],
  afro: ['El afro verde (en reserva)', {
    nombre: 'El afro verde', handle: 'afro.lima', edad: 24, genero: 'masculino', proporciones: 'alto', piel: '#b97a53',
    cabello: 'afro', colorCabello: '#7dff3a', estiloOjos: 'normales', ojos: '#4a2c17', expresion: 'carcajada', pecas: true,
    ropa: 'puffer', colorRopa: '#c0c4cc', accesorio: 'corazon', fondo: '#ffffff',
    extras: 'star-shaped painted freckles, tiny red shorts, knee-high rainbow striped socks, chunky gold chains, holding a mini keyboard like a guitar',
    nicho: 'musica', rasgos: ['alegre', 'audaz'], tono: 'humor', plataformas: ['YouTube Shorts', 'TikTok']
  }],
  lumi: ['Lumi Bravo', {
    nombre: 'Lumi Bravo', handle: 'lumi.bravo', edad: 20, genero: 'femenino', estiloImagen: 'comic', proporciones: 'caricatura',
    piel: '#eebb99', cabello: 'rapado', colorCabello: '#f28c28', estiloOjos: 'grandes', ojos: '#b7852f', expresion: 'sonrisa',
    pecas: true, ropa: 'bomber', colorRopa: '#5b6b3a', accesorio: 'ninguno', fondo: '#1e1c2a',
    extras: 'a small rectangle of grey-and-white TV static on her left cheek, a broken transparent cassette tape hanging from a cord around her neck',
    nicho: 'musica', rasgos: ['sensible', 'alegre'], tono: 'cercano', plataformas: ['YouTube Shorts'],
    frase: 'Este no es mío… pero me lo quedo un ratito.', historia: 'Cantante que escucha recuerdos ajenos en un casete roto.'
  }],
  marvin: ['Marvin (el creador)', {
    nombre: 'Marvin', handle: 'm_cuestas03', edad: 33, genero: 'masculino', virtual: false, proporciones: 'normal', piel: '#d9a07a',
    cabello: 'corto', colorCabello: '#1d1a1a', estiloOjos: 'normales', ojos: '#4a2c17', expresion: 'carcajada', barba: 'corta',
    ropa: 'deportiva', colorRopa: '#1b1b1f', accesorio: 'bandana', fondo: '#d6f5ff',
    extras: 'dark messy windswept hair, slightly slimmer build',
    nicho: 'viajes', rasgos: ['alegre', 'perseverante'], tono: 'cercano', plataformas: ['Instagram', 'YouTube Shorts']
  }]
};

const NOMBRES = {
  femenino: ['Lumi', 'Nara', 'Vera', 'Kiara', 'Sol', 'Mia', 'Ada', 'Iris', 'Zoe', 'Luna'],
  masculino: ['Spike', 'Teo', 'Bruno', 'Iker', 'Nilo', 'Dante', 'Leo', 'Ciro', 'Max', 'Rafa'],
  nobinario: ['Ari', 'Noa', 'Kai', 'Sam', 'Alex', 'Rio', 'Eli', 'Indi']
};
const APELLIDOS = ['Bravo', 'Vega', 'Neón', 'Ceniza', 'Marea', 'Voltaje', 'Rayo', 'Luna', 'Brisa', 'Cometa'];

let estado = structuredClone(BASE);

/* ---------- Utilidades ---------- */
const pick = (arr) => arr[Math.floor(Math.random() * arr.length)];
const esc = (t) => String(t ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

function oscurecer(hex, f) {
  if (!hex) return '#000';
  const n = parseInt(hex.slice(1), 16);
  const r = Math.round(((n >> 16) & 255) * f), g = Math.round(((n >> 8) & 255) * f), b = Math.round((n & 255) * f);
  return '#' + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}
const nombreColor = (lista, hex, idioma) => {
  const fila = PAL[lista].find((c) => c[0] === hex);
  return fila ? fila[idioma === 'es' ? 1 : 2] : '';
};

function aviso(texto) {
  const a = $('aviso');
  a.textContent = texto;
  a.classList.add('visible');
  clearTimeout(aviso.t);
  aviso.t = setTimeout(() => a.classList.remove('visible'), 1800);
}

function leerGuardados() {
  try { return JSON.parse(localStorage.getItem(CLAVE)) || []; } catch { return []; }
}
function escribirGuardados(lista) {
  try { localStorage.setItem(CLAVE, JSON.stringify(lista)); return true; } catch { return false; }
}

/* ============================================================
   Dibujo SVG
   ============================================================ */
const PROP = {
  normal: { rx: 36, ry: 44, hy: 104, s0: 32, s1: 168, cuello: 22 },
  alto: { rx: 32, ry: 42, hy: 100, s0: 50, s1: 150, cuello: 16 },
  bajito: { rx: 38, ry: 42, hy: 110, s0: 20, s1: 180, cuello: 28 },
  caricatura: { rx: 46, ry: 52, hy: 100, s0: 50, s1: 150, cuello: 16 }
};

function dibujar(s) {
  const P = PROP[s.proporciones] || PROP.normal;
  const { rx, ry, hy } = P;
  const top = hy - ry;
  const piel = s.piel, pelo = s.colorCabello, ropa = s.ropa === 'bata' ? '#f7f7f5' : s.colorRopa;
  const linea = oscurecer(piel, 0.62);
  const brilla = NEON.includes(pelo) ? ' filter="url(#brillo)"' : '';
  const out = [];

  out.push(`<defs>
    <filter id="brillo" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <pattern id="rayas" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#fff"/><rect width="6" height="3" fill="#24324f"/></pattern>
  </defs>`);
  out.push(`<rect width="200" height="200" fill="${s.fondo}"/>`);

  // Cabello de atrás
  const cap = (op = 1) => `<path d="M${100 - rx - 1} ${hy - 2} Q${100 - rx - 3} ${top - 8} 100 ${top - 8} Q${100 + rx + 3} ${top - 8} ${100 + rx + 1} ${hy - 2} Q${100 + rx - 6} ${top + 16} 100 ${top + 14} Q${100 - rx + 6} ${top + 16} ${100 - rx - 1} ${hy - 2} Z" fill="${pelo}" opacity="${op}"${brilla}/>`;
  if (s.cabello === 'largo') out.push(`<path d="M${100 - rx - 4} ${hy - 10} Q${100 - rx - 6} ${top - 8} 100 ${top - 8} Q${100 + rx + 6} ${top - 8} ${100 + rx + 4} ${hy - 10} L${100 + rx + 10} ${hy + 62} Q100 ${hy + 56} ${100 - rx - 10} ${hy + 62} Z" fill="${pelo}"${brilla}/>`);
  if (s.cabello === 'afro') {
    const R = rx + 20, cy = top + 14;
    let g = `<g fill="${pelo}"${brilla}><circle cx="100" cy="${cy}" r="${R}"/>`;
    for (let i = 0; i < 14; i++) { const a = (i / 14) * Math.PI * 2; g += `<circle cx="${(100 + Math.cos(a) * R).toFixed(1)}" cy="${(cy + Math.sin(a) * R).toFixed(1)}" r="9"/>`; }
    out.push(g + '</g>');
  }
  if (s.cabello === 'mono') out.push(`<circle cx="100" cy="${top - 10}" r="15" fill="${pelo}"${brilla}/>`);
  if (s.cabello === 'coleta') out.push(`<path d="M${100 + rx - 6} ${top + 10} Q${100 + rx + 30} ${top + 20} ${100 + rx + 22} ${hy + 50} Q${100 + rx + 10} ${hy + 20} ${100 + rx - 2} ${top + 24} Z" fill="${pelo}"${brilla}/>`);
  if (s.cabello === 'mullet') out.push(`<path d="M${100 - rx - 2} ${hy - 6} L${100 - rx - 7} ${hy + 42} Q100 ${hy + 52} ${100 + rx + 7} ${hy + 42} L${100 + rx + 2} ${hy - 6} Z" fill="${pelo}"${brilla}/>`);

  // Cuerpo y ropa
  const s0 = s.ropa === 'puffer' ? P.s0 - 12 : P.s0, s1 = s.ropa === 'puffer' ? P.s1 + 12 : P.s1;
  out.push(`<path d="M${s0} 200 Q${s0 + 2} 174 100 168 Q${s1 - 2} 174 ${s1} 200 Z" fill="${ropa}" stroke="${oscurecer(ropa, 0.7)}" stroke-width="1.5"/>`);
  const w = P.cuello / 2;
  out.push(`<rect x="${100 - w}" y="${hy + ry - 14}" width="${w * 2}" height="${172 - (hy + ry - 14)}" fill="${piel}"/>`);
  out.push(`<path d="M${100 - w} ${hy + ry - 10} Q100 ${hy + ry + 2} ${100 + w} ${hy + ry - 10} L${100 + w} ${hy + ry - 4} Q100 ${hy + ry + 8} ${100 - w} ${hy + ry - 4} Z" fill="${linea}" opacity=".25"/>`);
  out.push(detallesRopa(s.ropa, ropa, piel, s0, s1));

  // Accesorios del cuello
  if (s.accesorio === 'boa') {
    let g = '<g>';
    for (let i = 0; i <= 12; i++) {
      const t = i / 12, x = (s0 + 22) + t * ((s1 - 22) - (s0 + 22)), y = 178 + Math.sin(t * Math.PI) * 8;
      g += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="8" fill="#e8f000"/><circle cx="${(x - 2).toFixed(1)}" cy="${(y - 2).toFixed(1)}" r="4" fill="#f7ff66"/>`;
    }
    out.push(g + '</g>');
  }
  if (s.accesorio === 'cadenas') out.push(`<path d="M86 170 Q100 192 114 170" fill="none" stroke="#d4af37" stroke-width="3"/><path d="M82 172 Q100 200 118 172" fill="none" stroke="#d4af37" stroke-width="3"/>`);
  if (s.accesorio === 'audifonos') out.push(`<path d="M78 178 Q100 196 122 178" fill="none" stroke="#222" stroke-width="5"/><circle cx="76" cy="176" r="13" fill="#222"/><circle cx="76" cy="176" r="7" fill="${s.colorRopa}"/><circle cx="124" cy="176" r="13" fill="#222"/><circle cx="124" cy="176" r="7" fill="${s.colorRopa}"/>`);

  // Orejas y cabeza
  if (s.orejas === 'puntiagudas') {
    out.push(`<path d="M${100 - rx + 2} ${hy - 8} L${100 - rx - 22} ${hy - 26} L${100 - rx + 2} ${hy + 12} Z" fill="${piel}" stroke="${linea}" stroke-width="1"/>`);
    out.push(`<path d="M${100 + rx - 2} ${hy - 8} L${100 + rx + 22} ${hy - 26} L${100 + rx - 2} ${hy + 12} Z" fill="${piel}" stroke="${linea}" stroke-width="1"/>`);
  } else {
    out.push(`<ellipse cx="${100 - rx}" cy="${hy + 2}" rx="7" ry="10" fill="${piel}" stroke="${linea}" stroke-width="1"/><ellipse cx="${100 + rx}" cy="${hy + 2}" rx="7" ry="10" fill="${piel}" stroke="${linea}" stroke-width="1"/>`);
  }
  out.push(`<ellipse cx="100" cy="${hy}" rx="${rx}" ry="${ry}" fill="${piel}" stroke="${linea}" stroke-width="1.2"/>`);

  // Cara
  const ex = rx * 0.42, ey = hy - 2, my = hy + Math.round(ry * 0.6);
  if (s.ojeras) out.push(`<path d="M${100 - ex - 7} ${ey + 8} Q${100 - ex} ${ey + 12} ${100 - ex + 7} ${ey + 8}" stroke="#7b4f86" stroke-width="2" fill="none" opacity=".6"/><path d="M${100 + ex - 7} ${ey + 8} Q${100 + ex} ${ey + 12} ${100 + ex + 7} ${ey + 8}" stroke="#7b4f86" stroke-width="2" fill="none" opacity=".6"/>`);
  if (['sonrisa', 'carcajada', 'chicle'].includes(s.expresion)) out.push(`<circle cx="${100 - ex - 6}" cy="${ey + 16}" r="6" fill="#ff6f6f" opacity=".22"/><circle cx="${100 + ex + 6}" cy="${ey + 16}" r="6" fill="#ff6f6f" opacity=".22"/>`);
  if (s.pecas) {
    let g = `<g fill="${oscurecer(piel, 0.65)}" opacity=".7">`;
    [[-14, 10], [-10, 14], [-18, 15], [14, 10], [10, 14], [18, 15], [-6, 12], [6, 12]].forEach(([dx, dy]) => { g += `<circle cx="${100 + dx}" cy="${ey + dy}" r="1.2"/>`; });
    out.push(g + '</g>');
  }
  out.push(ojos(s, ex, ey));
  out.push(cejas(s, ex, ey, pelo));
  out.push(`<path d="M100 ${hy + 4} Q96 ${hy + 16} 100 ${hy + 18} Q103 ${hy + 18} 105 ${hy + 16}" stroke="${linea}" stroke-width="1.6" fill="none" stroke-linecap="round"/>`);
  out.push(barba(s, rx, ry, hy, my, pelo));
  out.push(boca(s, my, piel));

  // Cabello de adelante
  out.push(peloFrente(s, rx, ry, hy, top, pelo, cap, brilla));

  // Accesorios de la cabeza
  out.push(accesorioCabeza(s, ex, ey, rx, top));

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="400" height="400">${out.join('')}</svg>`;
}

function detallesRopa(tipo, c, piel, s0, s1) {
  const d = oscurecer(c, 0.72);
  switch (tipo) {
    case 'camiseta': return `<path d="M88 168 Q100 180 112 168" stroke="${d}" stroke-width="2" fill="none"/>`;
    case 'chandal': return `<ellipse cx="${s0 + 16}" cy="182" rx="22" ry="14" fill="${oscurecer(c, 1.12 > 1 ? 1 : 1)}" stroke="${d}" stroke-width="1.5"/><ellipse cx="${s1 - 16}" cy="182" rx="22" ry="14" fill="${c}" stroke="${d}" stroke-width="1.5"/><path d="M100 172 L100 200" stroke="#d8d8d8" stroke-width="2"/><path d="M90 168 L100 176 L110 168" stroke="${d}" stroke-width="3" fill="none"/>`;
    case 'cardigan': return `<path d="M88 168 L100 200 L112 168 Z" fill="url(#rayas)"/><path d="M88 168 L100 200 M112 168 L100 200" stroke="${d}" stroke-width="2"/><circle cx="95" cy="184" r="1.8" fill="${d}"/><circle cx="97" cy="192" r="1.8" fill="${d}"/>`;
    case 'blazer': return `<path d="M88 168 L100 200 L112 168 Z" fill="#ffffff"/><path d="M88 168 L82 186 L100 200 Z" fill="${d}"/><path d="M112 168 L118 186 L100 200 Z" fill="${d}"/>`;
    case 'deportiva': return `<path d="M100 172 L100 200" stroke="#d0d0d0" stroke-width="2"/><path d="M${s0 + 12} 192 Q72 178 93 172" stroke="#c8102e" stroke-width="2.5" fill="none"/><path d="M${s1 - 12} 192 Q128 178 107 172" stroke="#c8102e" stroke-width="2.5" fill="none"/><path d="M${s0 + 18} 198 Q74 186 96 182" stroke="#e8e8e8" stroke-width="1.5" fill="none"/><rect x="118" y="182" width="7" height="8" rx="1.5" fill="#c8102e"/>`;
    case 'bata': return `<path d="M88 168 L96 200 M112 168 L104 200" stroke="#cfcfcf" stroke-width="2"/><rect x="66" y="184" width="8" height="6" rx="1" fill="#ff2fa0"/><circle cx="130" cy="188" r="4" fill="#2fd4ff"/><rect x="120" y="178" width="7" height="7" rx="1" fill="#7dff3a"/><path d="M76 196 Q84 178 92 190" stroke="#333" stroke-width="1.5" fill="none"/>`;
    case 'puffer': return `<path d="M${s0 + 6} 184 Q100 176 ${s1 - 6} 184" stroke="${d}" stroke-width="2" fill="none"/><path d="M${s0 + 2} 194 Q100 186 ${s1 - 2} 194" stroke="${d}" stroke-width="2" fill="none"/><path d="M88 168 Q100 176 112 168" stroke="${d}" stroke-width="6" fill="none"/>`;
    case 'bomber': return `<path d="M86 168 Q100 177 114 168" stroke="${d}" stroke-width="5" fill="none"/><path d="M100 174 L100 200" stroke="${d}" stroke-width="1.5"/><circle cx="${s1 - 22}" cy="184" r="6" fill="#d9a21b"/><path d="M${s1 - 23} 179 L${s1 - 25} 185 L${s1 - 21} 184 L${s1 - 23} 190" stroke="#1b1b1f" stroke-width="1.3" fill="none"/>`;
    default: return '';
  }
}

function ojos(s, ex, ey) {
  const iris = s.ojos;
  const uno = (x) => {
    switch (s.estiloOjos) {
      case 'grandes': return `<ellipse cx="${x}" cy="${ey}" rx="8" ry="7" fill="#fff" stroke="#3a2a2a" stroke-width=".8"/><circle cx="${x}" cy="${ey + .5}" r="4.8" fill="${iris}"/><circle cx="${x}" cy="${ey + .5}" r="2.3" fill="#141414"/><circle cx="${x + 1.6}" cy="${ey - 1.4}" r="1.3" fill="#fff"/>`;
      case 'entrecerrados': return `<ellipse cx="${x}" cy="${ey + 1}" rx="6" ry="3.2" fill="#fff"/><circle cx="${x}" cy="${ey + 1}" r="2.8" fill="${iris}"/><circle cx="${x}" cy="${ey + 1}" r="1.3" fill="#141414"/><path d="M${x - 7} ${ey - 1} Q${x} ${ey - 3} ${x + 7} ${ey - 1}" stroke="#3a2a2a" stroke-width="1.8" fill="none"/>`;
      case 'felices': return `<path d="M${x - 6} ${ey + 2} Q${x} ${ey - 6} ${x + 6} ${ey + 2}" stroke="#2b1d1d" stroke-width="2.4" fill="none" stroke-linecap="round"/>`;
      default: return `<ellipse cx="${x}" cy="${ey}" rx="6" ry="5" fill="#fff" stroke="#3a2a2a" stroke-width=".8"/><circle cx="${x}" cy="${ey + .5}" r="3.4" fill="${iris}"/><circle cx="${x}" cy="${ey + .5}" r="1.7" fill="#141414"/><circle cx="${x + 1.2}" cy="${ey - 1}" r="1" fill="#fff"/>`;
    }
  };
  return uno(100 - ex) + uno(100 + ex);
}

function cejas(s, ex, ey, pelo) {
  const c = pelo === '#f2efe6' ? '#d8cfb8' : oscurecer(pelo, 0.85);
  const y = ey - 10;
  let l = `M${100 - ex - 7} ${y + 1} Q${100 - ex} ${y - 3} ${100 - ex + 7} ${y}`;
  let r = `M${100 + ex - 7} ${y} Q${100 + ex} ${y - 3} ${100 + ex + 7} ${y + 1}`;
  if (s.expresion === 'sorpresa') { l = `M${100 - ex - 7} ${y - 2} Q${100 - ex} ${y - 7} ${100 - ex + 7} ${y - 3}`; r = `M${100 + ex - 7} ${y - 3} Q${100 + ex} ${y - 7} ${100 + ex + 7} ${y - 2}`; }
  if (s.expresion === 'seria') { l = `M${100 - ex - 7} ${y} L${100 - ex + 7} ${y + 1}`; r = `M${100 + ex - 7} ${y + 1} L${100 + ex + 7} ${y}`; }
  if (s.expresion === 'picara') { r = `M${100 + ex - 7} ${y - 3} Q${100 + ex} ${y - 8} ${100 + ex + 7} ${y - 4}`; }
  return `<path d="${l}" stroke="${c}" stroke-width="3" fill="none" stroke-linecap="round"/><path d="${r}" stroke="${c}" stroke-width="3" fill="none" stroke-linecap="round"/>`;
}

function barba(s, rx, ry, hy, my, pelo) {
  const bigote = `<path d="M88 ${my - 6} Q100 ${my - 12} 112 ${my - 6} Q100 ${my - 3} 88 ${my - 6} Z" fill="${pelo}"/>`;
  const mandibula = (extra, op) => `<path d="M${100 - rx + 2} ${hy + 4} Q${100 - rx + 4} ${hy + ry + 4 + extra} 100 ${hy + ry + 3 + extra} Q${100 + rx - 4} ${hy + ry + 4 + extra} ${100 + rx - 2} ${hy + 4} Q${100 + rx - 8} ${my + 2} 100 ${my + 4} Q${100 - rx + 8} ${my + 2} ${100 - rx + 2} ${hy + 4} Z" fill="${pelo}" opacity="${op}"/>`;
  switch (s.barba) {
    case 'bigote': return bigote;
    case 'corta': return mandibula(0, 0.55) + bigote;
    case 'completa': return mandibula(10, 1) + bigote;
    default: return '';
  }
}

function boca(s, my, piel) {
  const col = s.labios || oscurecer(piel, 0.5);
  const sw = s.labios ? 3 : 2.4;
  switch (s.expresion) {
    case 'carcajada': return `<path d="M86 ${my - 2} Q100 ${my + 16} 114 ${my - 2} Z" fill="#5a1a22" stroke="${col}" stroke-width="1.5"/><path d="M87.5 ${my - 1} L112.5 ${my - 1} Q100 ${my + 5} 87.5 ${my - 1} Z" fill="#fff"/>`;
    case 'seria': return `<path d="M90 ${my + 2} L110 ${my + 2}" stroke="${col}" stroke-width="${sw}" stroke-linecap="round"/>`;
    case 'sorpresa': return `<ellipse cx="100" cy="${my + 3}" rx="5" ry="7" fill="#5a1a22" stroke="${col}" stroke-width="1.5"/>`;
    case 'picara': return `<path d="M90 ${my + 2} Q102 ${my + 6} 112 ${my - 3}" stroke="${col}" stroke-width="${sw}" fill="none" stroke-linecap="round"/>`;
    case 'chicle': return `<path d="M92 ${my} Q100 ${my + 6} 108 ${my}" stroke="${col}" stroke-width="${sw}" fill="none" stroke-linecap="round"/><circle cx="111" cy="${my + 3}" r="12" fill="#ff7ac8" opacity=".92"/><circle cx="107" cy="${my - 1}" r="3" fill="#fff" opacity=".7"/>`;
    default: return `<path d="M88 ${my} Q100 ${my + 9} 112 ${my}" stroke="${col}" stroke-width="${sw}" fill="none" stroke-linecap="round"/>`;
  }
}

function peloFrente(s, rx, ry, hy, top, pelo, cap, brilla) {
  const borde = oscurecer(pelo, 0.7);
  switch (s.cabello) {
    case 'calvo': return '';
    case 'rapado': return cap(0.5);
    case 'puas': {
      const n = 11, L = rx * 1.25;
      let g = `<g fill="${pelo}" stroke="${borde}" stroke-width="1"${brilla}>`;
      for (let i = 0; i < n; i++) {
        const t = (-165 + i * (150 / (n - 1))) * Math.PI / 180, d = 7.5 * Math.PI / 180;
        const p = (a, kx, ky) => `${(100 + kx * Math.cos(a)).toFixed(1)} ${(hy + ky * Math.sin(a)).toFixed(1)}`;
        g += `<path d="M${p(t - d, rx, ry)} L${p(t, rx + L, ry + L)} L${p(t + d, rx, ry)} Z"/>`;
      }
      return g + '</g>' + cap();
    }
    case 'cresta': return cap(0.35) + `<path d="M93 ${top + 12} L90 ${top - 40} Q100 ${top - 54} 110 ${top - 40} L107 ${top + 12} Z" fill="${pelo}" stroke="${borde}" stroke-width="1"${brilla}/>`;
    case 'cono': return `<path d="M${100 - rx + 2} ${top + 16} Q${100 - rx * 0.5} ${top - 20} 100 ${top - 64} Q${100 + rx * 0.5} ${top - 20} ${100 + rx - 2} ${top + 16} Z" fill="${pelo}" stroke="${borde}" stroke-width="1"${brilla}/>` + cap();
    default: return cap();
  }
}

function accesorioCabeza(s, ex, ey, rx, top) {
  const L = 100 - ex, R = 100 + ex;
  switch (s.accesorio) {
    case 'lentes': return `<g fill="none" stroke="#222" stroke-width="2.2"><circle cx="${L}" cy="${ey}" r="10"/><circle cx="${R}" cy="${ey}" r="10"/><path d="M${L + 10} ${ey} Q100 ${ey - 4} ${R - 10} ${ey}"/></g>`;
    case 'sol': return `<g stroke="#222" stroke-width="2"><circle cx="${L}" cy="${ey}" r="10" fill="#ff8c1a" fill-opacity=".8"/><circle cx="${R}" cy="${ey}" r="10" fill="#ff8c1a" fill-opacity=".8"/><path d="M${L + 10} ${ey} Q100 ${ey - 4} ${R - 10} ${ey}" fill="none"/></g>`;
    case 'corazon': {
      const h = (x, y) => `<path d="M${x} ${y + 8} C${x - 14} ${y - 2} ${x - 8} ${y - 12} ${x} ${y - 5} C${x + 8} ${y - 12} ${x + 14} ${y - 2} ${x} ${y + 8} Z" fill="#e53935" stroke="#222" stroke-width="1.5"/>`;
      return h(L, top + 14) + h(R, top + 14) + `<path d="M${L + 8} ${top + 12} L${R - 8} ${top + 12}" stroke="#222" stroke-width="2"/>`;
    }
    case 'steampunk': return `<path d="M${100 - rx} ${top + 18} L${100 + rx} ${top + 18}" stroke="#4a3520" stroke-width="5"/><circle cx="${L}" cy="${top + 18}" r="10" fill="#b5863b" stroke="#6b4a1f" stroke-width="2"/><circle cx="${L}" cy="${top + 18}" r="6" fill="#2b3b4a"/><circle cx="${R}" cy="${top + 18}" r="10" fill="#b5863b" stroke="#6b4a1f" stroke-width="2"/><circle cx="${R}" cy="${top + 18}" r="6" fill="#2b3b4a"/>`;
    case 'bandana': {
      let g = `<rect x="${100 - rx - 1}" y="${top + 12}" width="${rx * 2 + 2}" height="12" rx="5" fill="#2f6db5"/>`;
      for (let i = 0; i < 8; i++) g += `<circle cx="${100 - rx + 6 + i * (rx * 2 - 8) / 7}" cy="${top + 18}" r="2" fill="#3fb6b2"/>`;
      return g;
    }
    case 'gorra': return `<path d="M${100 - rx - 2} ${top + 18} Q${100 - rx} ${top - 12} 100 ${top - 12} Q${100 + rx} ${top - 12} ${100 + rx + 2} ${top + 18} Z" fill="${s.colorRopa}" stroke="${oscurecer(s.colorRopa, 0.7)}" stroke-width="1.5"/><path d="M${100 - rx - 4} ${top + 18} Q100 ${top + 10} ${100 + rx + 18} ${top + 20} Q100 ${top + 27} ${100 - rx - 4} ${top + 18} Z" fill="${oscurecer(s.colorRopa, 0.8)}"/>`;
    default: return '';
  }
}

/* ============================================================
   Textos: prompt para Higgsfield, bio, ideas y prompt de chat
   ============================================================ */
function promptHiggsfield(s) {
  const estilo = OP.estiloImagen[s.estiloImagen][1];
  const partes = [];
  const prop = OP.proporciones[s.proporciones][1];
  partes.push(`${estilo} of an original, exaggerated eccentric character named ${s.nombre || 'the character'}: a ${OP.genero[s.genero][1]} around ${s.edad || 25} years old`);
  if (prop) partes.push(prop);
  partes.push(`${nombreColor('piel', s.piel, 'en')} skin`);
  partes.push(s.cabello === 'calvo' ? 'a bald head' : `hair: ${OP.cabello[s.cabello][1]}, ${nombreColor('colorCabello', s.colorCabello, 'en')}`);
  partes.push(`${OP.estiloOjos[s.estiloOjos][1]} ${nombreColor('ojos', s.ojos, 'en')} eyes`);
  partes.push(OP.expresion[s.expresion][1]);
  if (OP.orejas[s.orejas][1]) partes.push(OP.orejas[s.orejas][1]);
  if (OP.barba[s.barba][1]) partes.push(OP.barba[s.barba][1]);
  const lab = PAL.labios.find((l) => l[0] === s.labios);
  if (lab && lab[2]) partes.push(lab[2]);
  if (s.pecas) partes.push('freckles');
  if (s.ojeras) partes.push('dark under-eye circles');
  const ropa = s.ropa === 'bata' ? OP.ropa.bata[1] : `${nombreColor('colorRopa', s.colorRopa, 'en')} ${OP.ropa[s.ropa][1]}`;
  partes.push(`wearing an ${ropa}`.replace('an a', 'a').replace(/^wearing an ([^aeiou])/i, 'wearing a $1'));
  if (OP.accesorio[s.accesorio][1]) partes.push(OP.accesorio[s.accesorio][1]);
  if (s.extras.trim()) partes.push(s.extras.trim());
  const fondo = nombreColor('fondo', s.fondo, 'en');
  const cierre = s.estiloImagen === 'realista'
    ? `Seamless ${fondo} studio background, soft even light, full body, vertical 9:16.`
    : `Plain ${fondo} background, full body, vertical 9:16.`;
  return partes.join(', ') + '. ' + cierre;
}

function textoBio(s) {
  const nicho = OP.nicho[s.nicho][0];
  const creador = s.genero === 'femenino' ? 'Creadora' : s.genero === 'masculino' ? 'Creador' : 'Persona creadora';
  const lineas = [`${creador} de contenido de ${nicho.toLowerCase()}${s.rasgos.length ? ' · ' + s.rasgos.join(', ') : ''}`];
  if (s.frase) lineas.push(`«${s.frase}»`);
  if (s.publico) lineas.push(`Para ${s.publico}`);
  if (s.ciudad) lineas.push(`📍 ${s.ciudad}`);
  if (s.virtual) lineas.push('🤖 Personaje virtual creado con IA');
  return lineas.join('\n');
}

function textoIdeas(s) {
  return (IDEAS[s.nicho] || []).map((t, i) => `${i + 1}. ${t}`).join('\n') +
    `\n\nFormato: vertical 9:16, menos de 60 s · Plataformas: ${s.plataformas.join(', ') || 'por definir'}`;
}

function textoChat(s) {
  const rasgos = s.rasgos.length ? s.rasgos.join(', ') : 'por definir';
  return [
    `Eres ${s.nombre || 'el personaje'}, ${s.edad || ''} años, creador de contenido de ${OP.nicho[s.nicho][0].toLowerCase()}.`,
    `Personalidad: ${rasgos}. Tono: ${OP.tono[s.tono][0].toLowerCase()}.`,
    s.historia ? `Historia: ${s.historia}` : '',
    s.frase ? `Frase característica: «${s.frase}»` : '',
    s.publico ? `Hablas para: ${s.publico}.` : '',
    'Reglas: mantente en personaje; respuestas cortas; nunca digas que eres una persona real; si te preguntan, explica que eres un personaje virtual creado con IA.'
  ].filter(Boolean).join('\n');
}

/* ============================================================
   Interfaz
   ============================================================ */
function llenarSelect(id, opciones) {
  $(id).innerHTML = Object.entries(opciones).map(([v, [et]]) => `<option value="${v}">${esc(et)}</option>`).join('');
}

function llenarSwatches(clave) {
  const cont = $('sw-' + clave);
  const lista = clave === 'labios' ? PAL.labios : PAL[clave];
  cont.innerHTML = lista.map(([hex, es]) =>
    `<button type="button" class="swatch${hex ? '' : ' ninguno'}" data-clave="${clave}" data-valor="${hex ?? ''}" title="${esc(es)}" aria-label="${esc(es)}" style="${hex ? 'background:' + hex : ''}"></button>`
  ).join('');
}

function llenarChips(id, items, clave) {
  $(id).innerHTML = items.map((t) => `<button type="button" class="chip" data-clave="${clave}" data-valor="${esc(t)}">${esc(t)}</button>`).join('');
}

const CAMPOS_TEXTO = ['nombre', 'handle', 'edad', 'ciudad', 'publico', 'frase', 'historia', 'extras'];
const CAMPOS_SELECT = ['genero', 'estiloImagen', 'proporciones', 'cabello', 'estiloOjos', 'expresion', 'orejas', 'barba', 'ropa', 'accesorio', 'nicho', 'tono'];
const CAMPOS_CHECK = ['virtual', 'pecas', 'ojeras'];
const CLAVES_COLOR = ['piel', 'colorCabello', 'ojos', 'labios', 'colorRopa', 'fondo'];

function aFormulario() {
  CAMPOS_TEXTO.forEach((k) => { $(k).value = estado[k] ?? ''; });
  CAMPOS_SELECT.forEach((k) => { $(k).value = estado[k]; });
  CAMPOS_CHECK.forEach((k) => { $(k).checked = !!estado[k]; });
  document.querySelectorAll('.swatch').forEach((b) => {
    const v = b.dataset.valor || null;
    b.setAttribute('aria-pressed', String(estado[b.dataset.clave] === v));
  });
  document.querySelectorAll('.chip').forEach((b) => {
    const lista = estado[b.dataset.clave] || [];
    b.setAttribute('aria-pressed', String(lista.includes(b.dataset.valor)));
  });
}

function render() {
  $('avatar').innerHTML = dibujar(estado);
  $('pNombre').textContent = estado.nombre || 'Sin nombre';
  $('pHandle').textContent = estado.handle ? '@' + estado.handle.replace(/^@/, '') : '';
  $('pBio').textContent = textoBio(estado);
  $('pTags').textContent = `#${OP.nicho[estado.nicho][1]} #personajeIA`;
  $('oBio').textContent = textoBio(estado);
  $('oIdeas').textContent = textoIdeas(estado);
  $('oImagen').textContent = promptHiggsfield(estado);
  $('oChat').textContent = textoChat(estado);
}

function cargar(datos) {
  estado = { ...structuredClone(BASE), ...structuredClone(datos) };
  aFormulario();
  render();
}

function aleatorio() {
  const g = pick(Object.keys(OP.genero));
  const r = (o) => pick(Object.keys(o));
  const color = (k) => pick(PAL[k])[0];
  cargar({
    nombre: `${pick(NOMBRES[g])} ${pick(APELLIDOS)}`, genero: g, edad: 18 + Math.floor(Math.random() * 30),
    estiloImagen: estado.estiloImagen, proporciones: r(OP.proporciones), piel: color('piel'), cabello: r(OP.cabello),
    colorCabello: color('colorCabello'), estiloOjos: r(OP.estiloOjos), ojos: color('ojos'), expresion: r(OP.expresion),
    orejas: Math.random() < 0.15 ? 'puntiagudas' : 'normales', barba: g === 'femenino' ? 'ninguna' : r(OP.barba),
    labios: pick(PAL.labios)[0], pecas: Math.random() < 0.3, ropa: r(OP.ropa), colorRopa: color('colorRopa'),
    accesorio: r(OP.accesorio), fondo: color('fondo'), nicho: r(OP.nicho), tono: r(OP.tono),
    rasgos: [...RASGOS].sort(() => Math.random() - 0.5).slice(0, 2).map((x) => x[0]), plataformas: ['YouTube Shorts']
  });
}

function descargar(nombre, blob) {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = nombre;
  document.body.appendChild(a);
  a.click();
  setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500);
}
const archivo = () => (estado.nombre || 'personaje').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'personaje';

function descargarPng() {
  const svg = dibujar(estado).replace('width="400" height="400"', 'width="1024" height="1024"');
  const img = new Image();
  img.onload = () => {
    const c = document.createElement('canvas');
    c.width = c.height = 1024;
    c.getContext('2d').drawImage(img, 0, 0, 1024, 1024);
    c.toBlob((b) => b && descargar(archivo() + '.png', b), 'image/png');
  };
  img.onerror = () => aviso('No se pudo crear el PNG');
  img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
}

function renderGaleria() {
  const lista = leerGuardados();
  const g = $('galeria');
  if (!lista.length) { g.innerHTML = '<p class="vacia">Todavía no guardaste personajes en este navegador.</p>'; return; }
  g.innerHTML = lista.map((p, i) => `<div class="mini">
      <div data-cargar="${i}" title="Abrir">${dibujar({ ...BASE, ...p }).replace('width="400" height="400"', '')}</div>
      <p>${esc(p.nombre || 'Sin nombre')}</p>
      <button type="button" data-borrar="${i}">Borrar</button>
    </div>`).join('');
}

function guardar() {
  const lista = leerGuardados();
  const i = lista.findIndex((p) => p.nombre && p.nombre === estado.nombre);
  if (i >= 0) lista[i] = structuredClone(estado); else lista.unshift(structuredClone(estado));
  aviso(escribirGuardados(lista) ? 'Guardado en este navegador' : 'Este navegador no permite guardar');
  renderGaleria();
}

async function copiar(id) {
  const texto = $(id).textContent;
  try { await navigator.clipboard.writeText(texto); aviso('Copiado'); }
  catch {
    const t = document.createElement('textarea');
    t.value = texto; document.body.appendChild(t); t.select();
    try { document.execCommand('copy'); aviso('Copiado'); } catch { aviso('No se pudo copiar'); }
    t.remove();
  }
}

function iniciar() {
  $('preset').innerHTML = Object.entries(PRESETS).map(([k, [et]]) => `<option value="${k}">${esc(et)}</option>`).join('');
  ['genero', 'estiloImagen', 'proporciones', 'cabello', 'estiloOjos', 'expresion', 'orejas', 'barba', 'ropa', 'accesorio', 'nicho', 'tono']
    .forEach((k) => llenarSelect(k, OP[k]));
  CLAVES_COLOR.forEach(llenarSwatches);
  llenarChips('rasgos', RASGOS.map((r) => r[0]), 'rasgos');
  llenarChips('plataformas', PLATAFORMAS, 'plataformas');

  CAMPOS_TEXTO.forEach((k) => $(k).addEventListener('input', () => {
    estado[k] = k === 'edad' ? Number($(k).value) || '' : $(k).value;
    render();
  }));
  CAMPOS_SELECT.forEach((k) => $(k).addEventListener('change', () => { estado[k] = $(k).value; render(); }));
  CAMPOS_CHECK.forEach((k) => $(k).addEventListener('change', () => { estado[k] = $(k).checked; render(); }));

  document.addEventListener('click', (e) => {
    const sw = e.target.closest('.swatch');
    if (sw) { estado[sw.dataset.clave] = sw.dataset.valor || null; aFormulario(); render(); return; }
    const chip = e.target.closest('.chip');
    if (chip) {
      const k = chip.dataset.clave, v = chip.dataset.valor, lista = new Set(estado[k] || []);
      if (lista.has(v)) lista.delete(v);
      else if (k === 'rasgos' && lista.size >= 3) { aviso('Máximo 3 rasgos'); return; }
      else lista.add(v);
      estado[k] = [...lista]; aFormulario(); render(); return;
    }
    const cp = e.target.closest('[data-copiar]');
    if (cp) { copiar(cp.dataset.copiar); return; }
    const ab = e.target.closest('[data-cargar]');
    if (ab) { const p = leerGuardados()[Number(ab.dataset.cargar)]; if (p) { cargar(p); window.scrollTo({ top: 0, behavior: 'smooth' }); } return; }
    const br = e.target.closest('[data-borrar]');
    if (br) { const l = leerGuardados(); l.splice(Number(br.dataset.borrar), 1); escribirGuardados(l); renderGaleria(); }
  });

  $('preset').addEventListener('change', () => cargar(PRESETS[$('preset').value][1]));
  $('btnAleatorio').addEventListener('click', aleatorio);
  $('btnNuevo').addEventListener('click', () => { $('preset').value = 'vacio'; cargar({}); });
  $('btnGuardar').addEventListener('click', guardar);
  $('btnNombre').addEventListener('click', () => { estado.nombre = `${pick(NOMBRES[estado.genero])} ${pick(APELLIDOS)}`; aFormulario(); render(); });
  $('btnPng').addEventListener('click', descargarPng);
  $('btnSvg').addEventListener('click', () => descargar(archivo() + '.svg', new Blob([dibujar(estado)], { type: 'image/svg+xml' })));
  $('btnJson').addEventListener('click', () => descargar(archivo() + '.json', new Blob([JSON.stringify(estado, null, 2)], { type: 'application/json' })));
  $('importar').addEventListener('change', async (e) => {
    const f = e.target.files[0];
    if (!f) return;
    try { cargar(JSON.parse(await f.text())); aviso('Ficha importada'); } catch { aviso('Ese archivo no es una ficha válida'); }
    e.target.value = '';
  });

  $('preset').value = 'spike';
  cargar(PRESETS.spike[1]);
  renderGaleria();
}

document.addEventListener('DOMContentLoaded', iniciar);
