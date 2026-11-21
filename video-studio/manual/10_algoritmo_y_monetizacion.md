# 10 · Algoritmo, público y monetización

El director es creativo **y comercial**: diseña para una emoción, pero también para un objetivo de negocio medible.
Este capítulo dice qué objetivos existen, qué número los mide, qué premia cada plataforma y cómo se leen las
estadísticas.

## 1. El objetivo comercial se define en cada proyecto

Va en `00_brief.md`, línea **Objetivo comercial**, y lo fija el dueño. Hay un objetivo principal por video; puede haber
uno secundario.

| Objetivo | Qué buscamos | Métrica principal (KPI) | Métricas de apoyo | Qué cambia en la creación |
|---|---|---|---|---|
| **Monetizar** | ingresos por anuncios o fondos de creador | horas de visualización (largo) / vistas aptas (Shorts) y RPM | retención, duración media, sesiones | videos que cumplen la duración mínima que paga cada plataforma; series que encadenan vistas |
| **Presencia / alcance** | que nos vea la mayor cantidad posible del público objetivo | vistas únicas e impresiones del público objetivo | % de vistas desde el feed, alcance a no seguidores | gancho fuerte en 1 s, formato corto, tendencias adaptadas |
| **Posicionamiento / recordación** | que nos recuerden por algo (el personaje, una frase, un color) | búsquedas del nombre, menciones, comentarios que nombran al personaje | vistas repetidas, guardados | rasgo icónico siempre visible, frase o gesto fijo, misma estructura en cada video |
| **Comunidad** | gente que vuelve y participa | seguidores ganados por cada 1 000 vistas | comentarios, respuestas, vistas de suscriptores | preguntas a cámara, llamados a comentar, personajes con opiniones |
| **Conversión / venta** | que alguien compre o haga clic (libros para colorear, productos) | clics en el enlace, ventas | CTR del enlace, guardados | producto visible y deseable, llamada a la acción clara al final |
| **Viralidad** | que se comparta fuera de la plataforma | compartidos por cada 1 000 vistas | vistas repetidas (loop), guardados | remate sorpresivo, «esto es tan tú» (identificación), loop perfecto |

Cuando el brief no tiene objetivo comercial, el director **lo pregunta**; no lo elige por el dueño.

## 2. Qué premian los algoritmos (lo común a todas)

Las plataformas no publican su fórmula; esto es lo que coinciden en decir sus propias guías para creadores y la
práctica de la industria (confianza media). Se revisa con los datos propios.

1. **Retención:** porcentaje del video que se ve. En Shorts/TikTok/Reels, ver hasta el final y **volver a verlo**
   (loop) pesa mucho.
2. **El primer segundo:** si la gente desliza en el segundo 1, el video no se reparte. Por eso el gancho (cap. 01).
3. **Interacción con intención:** compartir y guardar valen más que «me gusta».
4. **Satisfacción del público objetivo:** que el video le guste a *ese* público hace que se lo muestre a más gente
   parecida. Un video que gusta a gente equivocada confunde al algoritmo sobre a quién mostrarle la cuenta.
5. **Constancia y nicho claro:** publicar con frecuencia estable y sobre lo mismo ayuda a que la plataforma entienda
   a quién mostrar la cuenta.
6. **Originalidad:** contenido reciclado, resubido o con marca de agua de otra app reparte menos y puede quedar fuera
   de la monetización.

## 3. Requisitos para cobrar (verificar antes de planear)

Datos conocidos a mediados de 2025 (confianza media; **las condiciones cambian, revisarlas en la página oficial de
cada programa antes de decidir**):

| Programa | Requisito para entrar | Qué paga |
|---|---|---|
| YouTube Partner Program (nivel completo) | 1 000 suscriptores y 4 000 horas de vistas públicas de videos largos en 12 meses, **o** 1 000 suscriptores y 10 millones de vistas de Shorts en 90 días | anuncios en videos largos y parte de los ingresos de Shorts |
| YouTube (nivel inicial) | 500 suscriptores, 3 videos en 90 días y 3 000 horas en 12 meses o 3 millones de vistas de Shorts en 90 días | membresías, Super Thanks, compras; no anuncios |
| TikTok Creator Rewards | 18 años, 10 000 seguidores, 100 000 vistas en 30 días; solo videos de más de 1 minuto | por vistas aptas |
| Facebook / Instagram | programas por invitación o por país; ver el panel de monetización de la cuenta | variable |

**Contenido infantil («hecho para niños» en YouTube, ley COPPA):** sin anuncios personalizados (RPM más bajo), sin
comentarios, sin notificaciones de la campanita y sin miniaplicaciones. Consecuencias comerciales:

- La comunidad no se mide con comentarios: se mide con **vistas repetidas, sesiones largas y suscriptores**.
- Rinde más el **video largo** (recopilaciones de 10–30 min, episodios) que el Short, porque suma horas de vista.
- Ingresos fuera de los anuncios: libros para colorear, productos físicos, licencias de los personajes.
- Tiky y Lumi viven en su propio canal; «M» y Spike, en otro. Mezclar públicos arruina las recomendaciones de los dos.

## 4. Cómo leer las estadísticas (lo hace el director)

### Exportar los datos

- **YouTube Studio:** Estadísticas → Avanzado → Exportar → CSV («Contenido», con vistas, tiempo de visualización,
  duración media, porcentaje visto, impresiones, CTR, suscriptores).
- **TikTok:** Herramientas para creadores → Estadísticas → descargar datos (o copiar los números por video).
- **Instagram:** Panel profesional → Estadísticas; Meta Business Suite exporta CSV.

Los archivos van a `video-studio/estadisticas/datos/` (no se suben al repo: el repo es público).

### Analizarlas

```bash
python3 video-studio/herramientas/estadisticas.py video-studio/estadisticas/datos/*.csv \
    --etiquetas video-studio/estadisticas/etiquetas.csv --objetivo alcance
```

El script acepta columnas en español o inglés de YouTube Studio, TikTok o Instagram, y calcula por video:

| Indicador | Fórmula | Bueno para |
|---|---|---|
| Retención media | duración media vista ÷ duración del video | todos |
| Compartidos por mil | compartidos ÷ vistas × 1 000 | viralidad |
| Guardados por mil | guardados ÷ vistas × 1 000 | recordación, utilidad |
| Seguidores por mil | seguidores ganados ÷ vistas × 1 000 | comunidad |
| Interacción | (likes + comentarios + compartidos + guardados) ÷ vistas | todos |
| CTR de miniatura | dato de YouTube | largo, monetización |
| Horas de vista | tiempo de visualización total | monetización |
| Créditos por mil vistas | créditos gastados ÷ vistas × 1 000 | eficiencia (cruza con `costos.md`) |

Con `etiquetas.csv` (una fila por video: personaje, modo, tipo de gancho, emoción, duración, formato, hora de
publicación) compara **qué decisiones creativas rinden más** para el objetivo elegido, y propone qué repetir y qué
dejar.

### Reglas de lectura

- **No sacar conclusiones con menos de 5 videos por grupo** ni antes de 48–72 h de publicado un Short (7 días para
  videos largos). El script avisa cuando la muestra es chica.
- **Comparar contra la mediana de la propia cuenta**, no contra cuentas ajenas.
- **Cambiar una cosa por vez** entre videos parecidos (como en el afinado de personajes): si cambian el gancho, la
  hora y el personaje a la vez, no se sabe qué funcionó.
- **Curva de retención:** una caída fuerte en el segundo 1–2 = gancho débil; una caída a la mitad = parte lenta;
  subida al final = loop o remate que hace volver.
- **El costo cuenta:** un video que trae la mitad de vistas por un décimo de créditos puede ser el mejor negocio.

## 5. Ciclo semanal

1. Exportar datos y correr `estadisticas.py`.
2. El director escribe en `video-studio/estadisticas/informe_AAAA-MM-DD.md`: qué rindió, qué no, y 3 decisiones para
   la semana (qué repetir, qué probar, qué dejar).
3. Los briefs nuevos citan ese informe en la línea **Aprendizaje que aplicamos**.
