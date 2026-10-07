#!/usr/bin/env node
// Motor generador de contenido de la hoja de vida.
// Lee generador/contenido.json y genera las páginas HTML en html/.
// Uso: node generador/motor.js

'use strict';

const fs = require('fs');
const path = require('path');

const RAIZ = path.join(__dirname, '..');
const DESTINO = path.join(RAIZ, 'html');
const contenido = JSON.parse(fs.readFileSync(path.join(__dirname, 'contenido.json'), 'utf8'));
const logo = fs.readFileSync(path.join(__dirname, 'plantillas', 'logo.svg'), 'utf8').trimEnd();

function esc(texto) {
  return String(texto)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function sangrar(html, espacios) {
  const pad = ' '.repeat(espacios);
  return html.split('\n').map((linea) => (linea ? pad + linea : linea)).join('\n');
}

// Un renderizador por cada tipo de sección del contenido.
const secciones = {
  titulo: (s) => `<h3>${esc(s.texto)}</h3>`,

  foto: (s, persona) => `<img src="${esc(persona.foto)}" alt="${esc(persona.nombre)}" width="10%">`,

  perfil: (s, persona) => `<p>${esc(persona.perfil)}</p>`,

  lista: (s) => [
    '<ul>',
    ...s.items.map((item) => `  <li type="square">${esc(item)}</li>`),
    '</ul>',
  ].join('\n'),

  tabla: (s) => [
    '<table border="1" cellpadding="10" cellspacing="0">',
    '  <thead>',
    '    <tr>',
    ...s.columnas.map((col) => `      <th>${esc(col)}</th>`),
    '    </tr>',
    '  </thead>',
    '  <tbody>',
    ...s.filas.flatMap((fila) => [
      '    <tr>',
      ...fila.map((celda) => `      <td>${esc(celda)}</td>`),
      '    </tr>',
    ]),
    '  </tbody>',
    '</table>',
  ].join('\n'),

  video: (s) => [
    `<h4>${esc(s.subtitulo)}</h4>`,
    `<video src="${esc(encodeURI(s.src))}" poster="${esc(encodeURI(s.poster))}" width="20%" preload="auto" controls></video>`,
  ].join('\n'),

  audio: (s) => [
    `<h4>${esc(s.subtitulo)}</h4>`,
    `<audio src="${esc(encodeURI(s.src))}" controls></audio>`,
  ].join('\n'),

  'formulario-estudios': (s) => [
    '<form autocomplete="on">',
    '  <fieldset>',
    '    <legend><strong>Agregar Estudios</strong></legend>',
    '    <p><label><strong>Año:</strong>',
    '      <select name="anio">',
    ...s.anios.map((anio) => `        <option value="${esc(anio)}">${esc(anio)}</option>`),
    '      </select></label>',
    '    </p>',
    '    <p><label><strong>Institución:</strong> <input type="text" name="institucion" placeholder="Ej. UJMD"></label></p>',
    '    <p><label><strong>Lugar:</strong> <input type="text" name="lugar" placeholder="Ej. San Salvador"></label></p>',
    '    <p><strong>Género:</strong><br>',
    '      <label><input type="radio" name="genero" value="Masculino" checked> Masculino</label><br>',
    '      <label><input type="radio" name="genero" value="Femenino"> Femenino</label>',
    '    </p>',
    '    <p><label><strong>Recomendado por:</strong>',
    '      <select name="recomendado">',
    '        <option>Google</option>',
    '        <option>Amigo</option>',
    '        <option>Redes Sociales</option>',
    '      </select></label>',
    '    </p>',
    '    <p><label><strong>Comentarios:</strong>',
    '      <textarea name="comentarios" rows="3" cols="30"></textarea></label>',
    '    </p>',
    '    <p><label><strong>Acepto Términos y Condiciones:</strong> <input type="checkbox" name="terminos" required></label></p>',
    '    <input type="submit" value="Registrar">',
    '  </fieldset>',
    '</form>',
  ].join('\n'),
};

function renderSeccion(seccion, persona) {
  const render = secciones[seccion.tipo];
  if (!render) {
    throw new Error(`Tipo de sección desconocido: "${seccion.tipo}"`);
  }
  return render(seccion, persona);
}

function renderNav(pagina, paginas) {
  const enlaces = paginas
    .filter((p) => p !== pagina)
    .map((p) => `<a href="${esc(p.archivo)}">${esc(p.menu)}</a>`)
    .join(' &vert; ');
  return [
    '<nav>',
    `  <h2>${esc(contenido.persona.nombre)}</h2>`,
    `  ${enlaces}`,
    '</nav>',
  ].join('\n');
}

function renderFooter(persona) {
  const enlaces = persona.contacto
    .map((c) => `<a href="${esc(c.url)}" title="${esc(c.titulo)}"><img src="${esc(c.icono)}" width="3%" alt="${esc(c.alt)}"></a>`)
    .join(' &vert; ');
  return [
    '<footer>',
    '  <h5>Contáctame</h5>',
    `  ${enlaces}`,
    '</footer>',
  ].join('\n');
}

function renderPagina(pagina) {
  const { persona, paginas } = contenido;
  const cuerpo = [
    '<header>',
    sangrar(logo, 2),
    '  <h1>Hoja de Vida</h1>',
    '</header>',
    renderNav(pagina, paginas),
    '<main>',
    ...pagina.secciones.map((s) => sangrar(renderSeccion(s, persona), 2)),
    '</main>',
    renderFooter(persona),
  ].join('\n');

  return [
    '<!DOCTYPE html>',
    '<!-- Archivo generado por generador/motor.js. Edita generador/contenido.json y vuelve a ejecutar el motor. -->',
    '<html lang="es">',
    '  <head>',
    '    <meta charset="utf-8">',
    '    <meta name="viewport" content="width=device-width, initial-scale=1">',
    `    <title>${esc(pagina.titulo)}</title>`,
    '  </head>',
    '  <body>',
    sangrar(cuerpo, 4),
    '  </body>',
    '</html>',
    '',
  ].join('\n');
}

for (const pagina of contenido.paginas) {
  const destino = path.join(DESTINO, pagina.archivo);
  fs.writeFileSync(destino, renderPagina(pagina));
  console.log(`Generado: ${path.relative(RAIZ, destino)}`);
}
