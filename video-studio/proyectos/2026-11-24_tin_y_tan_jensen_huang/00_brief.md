# Brief — Tin & Tan, short 3: Jensen Huang volvió a Nvidia en 11 días

> Sustituye al brief anterior (`00_brief_anterior_tarjeta_1999.md`), que convertía la noticia en un video de
> nostalgia sobre una tarjeta de 1999. El dueño lo corrigió: la nostalgia era una limitante y quedó eliminada
> (`canales/nostalgia-tin-y-tan/PARAMETROS.md`). Este video trata de **la noticia**, que es lo que la gente busca.

- **Título provisional:** Jensen Huang Is Back as Nvidia CEO After 11 Days
- **Pedido del dueño (textual):** «Te propuse un video de Jensen porque este día retornó como CEO de Nvidia después del
  escándalo; revisa las noticias y filtra las propuestas bajo esa perspectiva» · «Filtra todo vos con base a tu
  investigación» · «Haz los cambios con respecto a la investigación» · «quiero que le demos profundidad y comencemos a
  usar más efectos de video».
- **Modo:** C desde cero, dibujado por código con `palitos.py` 1.3 y `herramientas/efectos.py`.
- **Objetivo comercial (dueño, 2026-11-23):** entrar al Programa de socios de YouTube lo antes posible.
- **Cómo se mide en este video:** se quedó a mirar frente a deslizó (el short 1 dio 20,7 %), retención por segundo,
  compartidos y suscriptores por cada mil vistas, y tráfico desde búsqueda. Es el primer video de actualidad del canal.
- **Público:** quien está siguiendo la noticia en EE. UU.; sin edad fija (parámetro flexible: manda el dato de Studio).
- **Para qué es el video:** que quien vio el titular entienda en 30 segundos qué pasó, con las fechas y los números, y
  se quede con un dato que no traía.
- **Emoción:** curiosidad en el gancho → tensión → asombro en el pico (alta activación: lo que la investigación
  asocia con compartir, `manual/14`).
- **Plataforma y formato:** YouTube Shorts 9:16, 25 a 35 s; se reutiliza en TikTok e Instagram.
- **Personajes:** `@tan` pregunta lo que el público se pregunta; `@tin` responde con datos. Jensen Huang **no aparece
  dibujado ni imitado**: se le nombra.
- **Presupuesto:** 0 créditos en imagen y video; la voz se cotiza y necesita el sí del dueño.
- **Idioma:** inglés de EE. UU.

## Datos del video (los únicos que se pueden afirmar)

| Dato | Valor | Fuente y fecha |
|---|---|---|
| Fundación y cargo | Nvidia se constituyó el 5 de abril de 1993; Huang la dirige desde entonces | Wikipedia en inglés, «Nvidia» y «Jensen Huang», leídas el 2026-11-24 |
| Investigación | El 8 de noviembre de 2026 la junta abrió una investigación independiente | Wikipedia, «Jensen Huang», leída el 2026-11-24 |
| Renuncia | El 12 de noviembre de 2026 renunció como presidente, director ejecutivo y miembro de la junta; Colette Kress quedó como directora ejecutiva interina | Wikipedia, leída el 2026-11-24; títulos de cadenas en YouTube |
| «No lo repondremos» | El 17 de noviembre la junta dijo que no pensaba reponerlo | Wikipedia, leída el 2026-11-24 |
| Regreso | El 23 de noviembre de 2026 la junta lo repuso como presidente y director ejecutivo, con efecto inmediato | Wikipedia y videos de CNN, BBC, NBC, CBS, ABC y Fox News, leídos el 2026-11-24. **El comunicado de Nvidia no se pudo abrir** |
| Días fuera | 12 → 23 de noviembre: **11 días** | cálculo |
| Días al mando antes de renunciar | 5-abr-1993 → 12-nov-2026: **12.274 días** (≈ 33,6 años) | cálculo con `datetime` |
| Proporción | 12.274 ÷ 11 ≈ **1.116**: un día fuera por cada ≈ 1.116 al mando | cálculo |
| Otros regresos | Sam Altman volvió a OpenAI en 5 días (noviembre de 2023); Steve Jobs estuvo fuera de Apple ≈ 12 años (1985–1997) | Wikipedia; **las fechas exactas se comprueban antes de escribir el guion** |

## Decisiones del equipo (2026-11-24), tomadas con la investigación

| Decisión | Porqué |
|---|---|
| El tema es la noticia del regreso, no un objeto de época | Es donde está la demanda: los videos sobre el regreso sumaron cientos de miles de vistas en horas (lectura del 2026-11-24); el tema lo pone la demanda (`PARAMETROS.md`) |
| Forma: los hechos en orden con sus fechas y tres números (11 días fuera, 12.274 al mando, la comparación con otros regresos) | Responde lo que el público se pregunta («¿qué pasó?», «¿cuánto estuvo fuera?»); la cuenta es una herramienta, no una obligación |
| Se nombra el hecho con las palabras que se buscan: «resigned», «scandal», «returned» | Evitar toda palabra de la polémica era una limitante: quita del título lo que la gente busca. Se nombra el hecho público; **no** se cuentan detalles de la vida privada, no se nombra a terceros y no se juzga |
| La cifra puede ir en el título («11 Days») | Es el gancho; ocultarla era una regla por opinión |
| Emoción de alta activación (tensión y asombro), sin burla | Lo que más se comparte es lo que activa (`manual/14`); la burla y la parodia son lo que ya hacen otros y cruzan el límite con una persona real |
| Profundidad y efectos según `manual/14` | Cada efecto se elige por lo que comunica y queda justificado en el perfil emocional |
| Tan pide la suscripción una vez | Los suscriptores son la mitad del umbral del Programa |
| Publicar cuanto antes | La noticia es de ayer; cada día pierde demanda |

## Lo que no se cruza (fijo, `PARAMETROS.md` sección 2)

Hechos públicos con fuente; sin detalles íntimos ni terceros; sin burla ni juicio moral; sin su cara ni su voz; sin
frases puestas en su boca; sin cifras de bolsa ni fortuna como consejo; marcas solo nombradas, con descargo.

## Lo que necesita el sí del dueño

- Los créditos de la voz.
- Publicar.

### Decisiones del equipo durante el render (2026-11-24)

- **«That is twelve years?» se deja sin palabra de aproximación en la voz.** Son 12 años menos un día (4.382 días);
  cambiarlo obligaría a regenerar la voz de Tan, que el dueño ya escuchó y aprobó. La tarjeta en español dice «¿Casi 12
  años?» y la descripción «≈ 12 years». Lo decide la coordinación, como dirección creativa.
- **Caras neutras en la renuncia y en la reposición.** Nadie sonríe ni festeja sobre un hecho polémico de una persona
  real (`PARAMETROS.md`, sección 2: sin burla). La cara `neutra` de Tin se armó en `codigo/render.py` con piezas de su
  ficha; queda pendiente llevarla a `palitos.py` y a su ficha para los siguientes videos.
- **Tan lanza y Tan atrapa el lápiz** (`FIRMA_LAPIZ_BUMERAN.md`); se le dijo al dueño que la variante «atrapa Tin»
  está prevista si la prefiere.
- **Tarjetas en español cortas, con las cifras**, en lugar del texto literal del `.srt`: a 86 px el texto completo no
  cabe en dos renglones; el `.srt` completo se sube como pista.

