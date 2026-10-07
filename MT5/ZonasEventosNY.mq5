//+------------------------------------------------------------------+
//|                                               ZonasEventosNY.mq5 |
//| Marca la vela de apertura de Nueva York (NYSE / Nasdaq, 9:30 NY) |
//| y las noticias del calendario económico de MT5, pasadas y nuevas.|
//| Las noticias nuevas se detectan solas cada pocos segundos.       |
//| Modo estudio: recorre una noticia (por ejemplo el IPC) en los    |
//| últimos años, con su vela, la apertura de ese día y promedios.   |
//+------------------------------------------------------------------+
#property copyright   "Marvin Cuestas"
#property version     "1.32"
#property description "Zonas de la vela de apertura de Nueva York y de las noticias del calendario económico."
#property indicator_chart_window
#property indicator_buffers 0
#property indicator_plots   0

#define PREFIJO       "ZENY_"
#define LINEAS_PANEL  14
#define ALTO_LINEA    16

enum ENUM_HORARIO_SERVIDOR
  {
   HORARIO_DST_EEUU,   // Cambia de horario con EE. UU. (GMT+2/+3, el más común)
   HORARIO_DST_EUROPA, // Cambia de horario con Europa
   HORARIO_SIN_DST     // No cambia de horario
  };

input group "Horario del bróker"
input ENUM_HORARIO_SERVIDOR InpHorarioServidor = HORARIO_DST_EEUU; // Cambio de horario del servidor
input int    InpDesfaseInvierno = 99;            // Desfase del servidor en invierno, horas (99 = automático)

input group "Apertura de Nueva York"
input bool            InpMostrarApertura = true;          // Marcar la vela de apertura
input int             InpHoraApertura    = 9;             // Hora de apertura (hora de Nueva York)
input int             InpMinutoApertura  = 30;            // Minuto de apertura
input int             InpHoraFinZona     = 16;            // Fin de las zonas de días anteriores (hora de Nueva York)
input ENUM_TIMEFRAMES InpTFVela          = PERIOD_M1;     // Vela que forma la zona (M1 = igual en todas las temporalidades)
input bool            InpAperturaSoloNoticias = true;     // Marcar la apertura solo en días con noticia
input int             InpDiasHistorial   = 30;            // Días hacia atrás (modo normal)
input color           InpColorApertura   = C'45,60,85';   // Color de la zona de apertura
input color           InpColorTexto      = clrWhite;      // Color de la etiqueta de apertura

input group "Recuadros"
input bool            InpRellenoZona     = true;          // Rellenar el recuadro (queda detrás de las velas)
input int             InpGrosorBorde     = 1;             // Grosor del borde
input ENUM_LINE_STYLE InpEstiloBorde     = STYLE_SOLID;   // Estilo del borde
input bool            InpExtenderTodas   = false;         // Extender también las zonas anteriores hasta la vela en curso

input group "Noticias (calendario económico de MT5)"
input bool   InpMostrarNoticias = true;                                          // Marcar noticias
input string InpMoneda          = "USD";                                         // Moneda (vacío = todas)
input ENUM_CALENDAR_EVENT_IMPORTANCE InpImportanciaMinima = CALENDAR_IMPORTANCE_MODERATE; // Importancia mínima para la línea
input ENUM_CALENDAR_EVENT_IMPORTANCE InpImportanciaAlta   = CALENDAR_IMPORTANCE_HIGH;     // Importancia mínima para zona y avisos
input string InpFiltroNombre    = "";                                            // Otras noticias que contengan (separar con ;)
input int    InpDiasFuturo      = 7;                                             // Días hacia adelante
input bool   InpZonaNoticia     = true;                                          // Marcar la vela de la noticia
input int    InpMinutosZonaNoticia = 1440;                                       // Extender la zona de la noticia (minutos)
input bool   InpLineasPasadas   = false;                                         // Líneas verticales en noticias pasadas
input bool   InpLineasFuturas   = true;                                          // Líneas punteadas en noticias próximas
input color  InpColorAlta       = C'233,30,99';                                  // Color importancia alta (línea y etiqueta)
input color  InpColorMedia      = clrOrange;                                     // Color importancia media
input color  InpColorBaja       = clrGold;                                       // Color importancia baja
input color  InpColorZonaNoticia = C'55,58,70';                                  // Color de la zona de la noticia

input group "Noticias a mostrar (true = activada)"
input bool   InpUsarLista     = true;   // Usar esta lista (false = todas las de la importancia mínima)
input bool   InpNotCPI        = true;   // CPI - IPC e IPC subyacente
input bool   InpNotPPI        = true;   // PPI - Precios al productor
input bool   InpNotNFP        = true;   // Nóminas no agrícolas, desempleo y salarios
input bool   InpNotADP        = false;  // ADP - Empleo privado
input bool   InpNotClaims     = false;  // Solicitudes de subsidio por desempleo (semanal)
input bool   InpNotJOLTS      = true;   // JOLTS - Ofertas de empleo
input bool   InpNotFedTasa    = true;   // Fed - Decisión de tipos de interés
input bool   InpNotFOMCActas  = true;   // Fed - Actas del FOMC
input bool   InpNotPowell     = true;   // Fed - Discursos y conferencia de Powell
input bool   InpNotPIB        = true;   // PIB (GDP)
input bool   InpNotPCE        = true;   // PCE - Inflación del gasto personal
input bool   InpNotVentas     = true;   // Ventas minoristas
input bool   InpNotISM        = true;   // ISM manufacturero y de servicios
input bool   InpNotConfianza  = false;  // Confianza del consumidor (Michigan, Conference Board)
input bool   InpNotDuraderos  = false;  // Pedidos de bienes duraderos
input bool   InpListarNombres = false;  // Escribir en Expertos todos los nombres de noticias de la moneda

input group "Estudio histórico de una noticia"
input bool   InpModoEstudio     = false;           // Activar el estudio histórico
input string InpEstudioNoticia  = "CPI";           // Noticia a estudiar (parte del nombre, separar con ;)
input int    InpEstudioAnios    = 5;               // Años hacia atrás
input color  InpColorPanel      = C'25,25,30';     // Fondo del panel

input group "Avisos"
input int    InpSegundosRevision  = 10;    // Revisar el calendario cada (segundos)
input bool   InpAvisoPublicacion  = true;  // Avisar cuando se publica el dato
input int    InpMinutosPreaviso   = 5;     // Avisar antes de la noticia (minutos, 0 = no)
input bool   InpNotificacionMovil = false; // Enviar también al móvil (MetaQuotes ID)

// Noticias que salen a la misma hora, agrupadas (por ejemplo IPC m/m, a/a y subyacente).
struct Ocurrencia
  {
   datetime          hora;        // hora del servidor
   int               importancia; // la mayor del grupo
   string            titulo;      // nombres unidos con " / "
   string            principal;   // nombre de la noticia más importante del grupo (para la etiqueta)
   string            detalle;     // una línea por noticia: previsión, anterior y actual
   string            tooltip;
  };

int        g_desfaseBase      = 0;  // desfase del servidor respecto a UTC en invierno, en segundos
ulong      g_cambioCalendario = 0;  // último cambio conocido del calendario
datetime   g_ultimoDibujo     = 0;
datetime   g_ultimaBarra      = 0;
bool       g_calendarioOk     = true;
ulong      g_avisados[];            // valores ya avisados al publicarse
ulong      g_preavisados[];         // valores ya avisados antes de publicarse
Ocurrencia g_noticias[];            // noticias cargadas, ordenadas por hora
int        g_indice           = -1; // noticia mostrada en el panel del modo estudio

//+------------------------------------------------------------------+
//| Fechas y horarios                                                |
//+------------------------------------------------------------------+
datetime Fecha(int anio, int mes, int dia)
  {
   MqlDateTime t;
   ZeroMemory(t);
   t.year = anio;
   t.mon  = mes;
   t.day  = dia;
   return StructToTime(t);
  }

int Anio(datetime t)
  {
   MqlDateTime s;
   TimeToStruct(t, s);
   return s.year;
  }

// Domingo número n del mes (1 = primero), o el último si n = 0, a la hora UTC indicada.
datetime Domingo(int anio, int mes, int n, int horaUtc)
  {
   MqlDateTime t;
   if(n > 0)
     {
      datetime primero = Fecha(anio, mes, 1);
      TimeToStruct(primero, t);
      return primero + ((7 - t.day_of_week) % 7 + 7 * (n - 1)) * 86400 + horaUtc * 3600;
     }
   datetime ultimo = (mes == 12 ? Fecha(anio + 1, 1, 1) : Fecha(anio, mes + 1, 1)) - 86400;
   TimeToStruct(ultimo, t);
   return ultimo - t.day_of_week * 86400 + horaUtc * 3600;
  }

// Horario de verano de EE. UU.: segundo domingo de marzo a primer domingo de noviembre, 2:00 hora local.
bool VeranoEEUU(datetime utc)
  {
   int anio = Anio(utc);
   return utc >= Domingo(anio, 3, 2, 7) && utc < Domingo(anio, 11, 1, 6);
  }

bool VeranoServidor(datetime utc)
  {
   if(InpHorarioServidor == HORARIO_DST_EEUU)
      return VeranoEEUU(utc);
   if(InpHorarioServidor == HORARIO_DST_EUROPA)
     {
      int anio = Anio(utc);
      return utc >= Domingo(anio, 3, 0, 1) && utc < Domingo(anio, 10, 0, 1);
     }
   return false;
  }

void CalcularDesfase()
  {
   if(InpDesfaseInvierno != 99)
     {
      g_desfaseBase = InpDesfaseInvierno * 3600;
      return;
     }
   int actual = (int)MathRound((double)(TimeTradeServer() - TimeGMT()) / 1800.0) * 1800;
   g_desfaseBase = actual - (VeranoServidor(TimeGMT()) ? 3600 : 0);
  }

datetime UtcAServidor(datetime utc)
  {
   return utc + g_desfaseBase + (VeranoServidor(utc) ? 3600 : 0);
  }

datetime ServidorAUtc(datetime servidor)
  {
   datetime aprox = servidor - g_desfaseBase;
   return aprox - (VeranoServidor(aprox) ? 3600 : 0);
  }

datetime UtcANy(datetime utc)
  {
   return utc - 5 * 3600 + (VeranoEEUU(utc) ? 3600 : 0);
  }

datetime NyAUtc(datetime ny)
  {
   datetime aprox = ny + 5 * 3600;
   return aprox - (VeranoEEUU(aprox) ? 3600 : 0);
  }

// Medianoche (hora de Nueva York) del día en que cae una hora del servidor.
datetime DiaNy(datetime servidor)
  {
   datetime ny = UtcANy(ServidorAUtc(servidor));
   return ny - (datetime)((long)ny % 86400);
  }

datetime AperturaServidor(datetime diaNy)
  {
   return UtcAServidor(NyAUtc(diaNy + InpHoraApertura * 3600 + InpMinutoApertura * 60));
  }

string HoraNy(datetime servidor)
  {
   return TimeToString(UtcANy(ServidorAUtc(servidor)), TIME_DATE | TIME_MINUTES);
  }

// "SEP 26" (mes y año) o "07 OCT 26" con el día, a partir de una fecha de Nueva York.
string EtiquetaFecha(datetime ny, bool conDia)
  {
   string meses[12] = {"ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"};
   MqlDateTime t;
   TimeToStruct(ny, t);
   string texto = meses[t.mon - 1] + StringFormat(" %02d", t.year % 100);
   return conDia ? StringFormat("%02d ", t.day) + texto : texto;
  }

// Hora de apertura de la vela en curso del gráfico.
datetime VelaEnCurso()
  {
   return iTime(_Symbol, PERIOD_CURRENT, 0);
  }

ENUM_TIMEFRAMES TFVela()
  {
   return InpTFVela == PERIOD_CURRENT ? (ENUM_TIMEFRAMES)_Period : InpTFVela;
  }

//+------------------------------------------------------------------+
//| Velas                                                            |
//+------------------------------------------------------------------+
// Vela de la temporalidad elegida que contiene `inicio`.
bool DatosVela(datetime inicio, MqlRates &vela)
  {
   ENUM_TIMEFRAMES tf = TFVela();
   int shift = iBarShift(_Symbol, tf, inicio, false);
   if(shift < 0)
      return false;
   MqlRates r[];
   if(CopyRates(_Symbol, tf, shift, 1, r) != 1)
      return false;
   if(r[0].time == 0 || r[0].time > inicio || inicio - r[0].time >= PeriodSeconds(tf))
      return false; // sin vela a esa hora (festivo o historial aún sin cargar)
   vela = r[0];
   return true;
  }

string Precio(double valor)
  {
   return DoubleToString(valor, _Digits);
  }

string Direccion(const MqlRates &vela)
  {
   if(vela.close > vela.open)
      return "alcista";
   if(vela.close < vela.open)
      return "bajista";
   return "sin cambio";
  }

string DescribirVela(datetime inicio)
  {
   MqlRates vela;
   if(!DatosVela(inicio, vela))
      return "sin datos (falta historial)";
   return StringFormat("A %s  Max %s  Min %s  C %s  ·  rango %s  ·  %s",
                       Precio(vela.open), Precio(vela.high), Precio(vela.low), Precio(vela.close),
                       Precio(vela.high - vela.low), Direccion(vela));
  }

//+------------------------------------------------------------------+
//| Dibujo                                                           |
//+------------------------------------------------------------------+
// Dibuja (o actualiza) un rectángulo con el máximo y el mínimo de la vela que contiene `inicio`.
// La etiqueta va en el extremo derecho, como en TradingView.
bool DibujarZonaVela(const string nombre, datetime inicio, datetime fin, color clr,
                     const string etiqueta, color clrEtiqueta, const string tooltip)
  {
   MqlRates vela;
   if(!DatosVela(inicio, vela))
      return false;

   if(ObjectFind(0, nombre) < 0)
      ObjectCreate(0, nombre, OBJ_RECTANGLE, 0, vela.time, vela.high, fin, vela.low);
   else
     {
      ObjectMove(0, nombre, 0, vela.time, vela.high);
      ObjectMove(0, nombre, 1, fin, vela.low);
     }
   ObjectSetInteger(0, nombre, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, nombre, OBJPROP_FILL, InpRellenoZona);
   ObjectSetInteger(0, nombre, OBJPROP_WIDTH, InpGrosorBorde);
   ObjectSetInteger(0, nombre, OBJPROP_STYLE, InpEstiloBorde);
   ObjectSetInteger(0, nombre, OBJPROP_BACK, true);
   ObjectSetInteger(0, nombre, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, nombre, OBJPROP_HIDDEN, true);
   ObjectSetString(0, nombre, OBJPROP_TOOLTIP, tooltip + "\nMáximo: " + Precio(vela.high) +
                   "   Mínimo: " + Precio(vela.low));

   string nombreTexto = nombre + "_T";
   if(ObjectFind(0, nombreTexto) < 0)
      ObjectCreate(0, nombreTexto, OBJ_TEXT, 0, fin, vela.high);
   else
      ObjectMove(0, nombreTexto, 0, fin, vela.high);
   ObjectSetString(0, nombreTexto, OBJPROP_TEXT, etiqueta);
   ObjectSetString(0, nombreTexto, OBJPROP_TOOLTIP, tooltip);
   ObjectSetInteger(0, nombreTexto, OBJPROP_COLOR, clrEtiqueta);
   ObjectSetInteger(0, nombreTexto, OBJPROP_FONTSIZE, 8);
   ObjectSetInteger(0, nombreTexto, OBJPROP_ANCHOR, ANCHOR_RIGHT_LOWER);
   ObjectSetInteger(0, nombreTexto, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, nombreTexto, OBJPROP_HIDDEN, true);
   return true;
  }

// `noticias` = nombres de las noticias del día; vacío en un día sin noticia ("Apertura NY").
bool DibujarApertura(datetime diaNy, bool ultima, const string noticias)
  {
   datetime inicio = AperturaServidor(diaNy);
   if(inicio > TimeTradeServer())
      return false;
   datetime velaActual = VelaEnCurso();
   datetime fin = UtcAServidor(NyAUtc(diaNy + InpHoraFinZona * 3600));
   if(ultima || InpExtenderTodas || fin > velaActual)
      fin = velaActual;
   string fecha = TimeToString(diaNy, TIME_DATE);
   string etiqueta = noticias == "" ? "Apertura NY " + EtiquetaFecha(diaNy, true)
                                    : noticias + " " + EtiquetaFecha(diaNy, false);
   string tooltip = StringFormat("Apertura de Nueva York %s %02d:%02d (hora NY)", fecha, InpHoraApertura, InpMinutoApertura);
   if(noticias != "")
      tooltip += "\nNoticias del día: " + noticias;
   return DibujarZonaVela(PREFIJO + "AP_" + fecha, inicio, fin, InpColorApertura, etiqueta, InpColorTexto, tooltip);
  }

void DibujarAperturas()
  {
   bool ultima = true; // la apertura más reciente siempre llega hasta la vela en curso
   if(InpModoEstudio || InpAperturaSoloNoticias)
     {
      // Solo los días con noticia: la estudiada o, en modo normal, las de importancia para zona.
      // La apertura de hoy se marca aunque la noticia salga más tarde.
      datetime diaAnterior = 0;
      for(int k = ArraySize(g_noticias) - 1; k >= 0; k--)
        {
         datetime dia = DiaNy(g_noticias[k].hora);
         if(dia == diaAnterior || !MarcaApertura(k))
            continue;
         diaAnterior = dia;
         if(DibujarApertura(dia, ultima, NoticiasDelDia(dia)))
            ultima = false;
        }
      return;
     }

   datetime hoyNy = UtcANy(TimeGMT());
   hoyNy -= (datetime)((long)hoyNy % 86400);
   for(int i = 0; i <= InpDiasHistorial; i++)
     {
      datetime dia = hoyNy - i * 86400;
      MqlDateTime t;
      TimeToStruct(dia, t);
      if(t.day_of_week == 0 || t.day_of_week == 6)
         continue;
      if(DibujarApertura(dia, ultima, NoticiasDelDia(dia))) // vacío en días sin noticia
         ultima = false;
     }
  }

bool MarcaApertura(int k)
  {
   return EligePorNombre() || g_noticias[k].importancia >= (int)InpImportanciaAlta;
  }

// Nombres de las noticias de ese día (en orden de hora y sin repetir), para la etiqueta de la apertura.
string NoticiasDelDia(datetime diaNy)
  {
   string nombres = "";
   for(int k = 0; k < ArraySize(g_noticias); k++)
     {
      if(DiaNy(g_noticias[k].hora) != diaNy || !MarcaApertura(k))
         continue;
      string nombre = g_noticias[k].principal;
      if(StringFind(" / " + nombres + " / ", " / " + nombre + " / ") < 0)
         nombres += (nombres == "" ? "" : " / ") + nombre;
     }
   return nombres;
  }

//+------------------------------------------------------------------+
//| Calendario económico                                             |
//+------------------------------------------------------------------+
bool PasaFiltro(const MqlCalendarEvent &ev, ENUM_CALENDAR_EVENT_IMPORTANCE minima, const string filtro)
  {
   if((int)ev.importance < (int)minima)
      return false;
   if(filtro == "")
      return true;
   string nombre = ev.name;
   StringToLower(nombre);
   string partes[];
   int n = StringSplit(filtro, ';', partes);
   for(int i = 0; i < n; i++)
     {
      string parte = partes[i];
      StringTrimLeft(parte);
      StringTrimRight(parte);
      StringToLower(parte);
      if(parte != "" && StringFind(nombre, parte) >= 0)
         return true;
     }
   return false;
  }

// Texto que buscan las casillas de la lista en el nombre de la noticia (en minúsculas, como lo da MT5).
string FiltroLista()
  {
   string filtro = "";
   if(InpNotCPI)       filtro += "cpi;";
   if(InpNotPPI)       filtro += "ppi;";
   if(InpNotNFP)       filtro += "nonfarm payrolls;unemployment rate;average hourly earnings;";
   if(InpNotADP)       filtro += "adp;";
   if(InpNotClaims)    filtro += "jobless claims;";
   if(InpNotJOLTS)     filtro += "jolts;";
   if(InpNotFedTasa)   filtro += "interest rate decision;fomc statement;";
   if(InpNotFOMCActas) filtro += "fomc minutes;";
   if(InpNotPowell)    filtro += "powell;fed chair;fomc press conference;";
   if(InpNotPIB)       filtro += "gdp;";
   if(InpNotPCE)       filtro += "pce;";
   if(InpNotVentas)    filtro += "retail sales;";
   if(InpNotISM)       filtro += "ism manufacturing;ism non-manufacturing;ism services;";
   if(InpNotConfianza) filtro += "michigan;consumer confidence;";
   if(InpNotDuraderos) filtro += "durable goods;";
   filtro += InpFiltroNombre;
   return filtro == "" ? "#ninguna#" : filtro; // sin casillas activadas no se muestra ninguna
  }

string FiltroActivo()
  {
   if(InpModoEstudio)
      return InpEstudioNoticia;
   return InpUsarLista ? FiltroLista() : InpFiltroNombre;
  }

// Con la lista o en el modo estudio la noticia se elige por nombre, sin importar su importancia.
bool EligePorNombre()
  {
   return InpModoEstudio || InpUsarLista;
  }

ENUM_CALENDAR_EVENT_IMPORTANCE ImportanciaActiva()
  {
   return EligePorNombre() ? CALENDAR_IMPORTANCE_NONE : InpImportanciaMinima;
  }

// Noticias que generan alertas: las de la lista o, sin lista, las de importancia para zona.
bool SeAvisa(const MqlCalendarEvent &ev)
  {
   if(InpUsarLista)
      return PasaFiltro(ev, CALENDAR_IMPORTANCE_NONE, FiltroLista());
   return PasaFiltro(ev, InpImportanciaAlta, InpFiltroNombre);
  }

void ListarNombres()
  {
   MqlCalendarEvent eventos[];
   int n = CalendarEventByCurrency(InpMoneda == "" ? "USD" : InpMoneda, eventos);
   string filtro = FiltroActivo();
   PrintFormat("Noticias de %s en el calendario de MT5 (%d). [X] = se muestra con los parámetros actuales:",
               InpMoneda == "" ? "USD" : InpMoneda, n);
   for(int i = 0; i < n; i++)
      PrintFormat("%s %s (importancia %d)", PasaFiltro(eventos[i], ImportanciaActiva(), filtro) ? "[X]" : "[ ]",
                  eventos[i].name, (int)eventos[i].importance);
  }

// Los valores del calendario vienen multiplicados por 1 000 000; LONG_MIN significa "sin dato".
string Valor(long valor, const MqlCalendarEvent &ev)
  {
   if(valor == LONG_MIN)
      return "n/d";
   string texto = DoubleToString(valor / 1000000.0, (int)ev.digits);
   if(ev.unit == CALENDAR_UNIT_PERCENT)
      texto += "%";
   switch(ev.multiplier)
     {
      case CALENDAR_MULTIPLIER_THOUSANDS: texto += "K"; break;
      case CALENDAR_MULTIPLIER_MILLIONS:  texto += "M"; break;
      case CALENDAR_MULTIPLIER_BILLIONS:  texto += "B"; break;
      case CALENDAR_MULTIPLIER_TRILLIONS: texto += "T"; break;
      default: break;
     }
   return texto;
  }

string Sorpresa(const MqlCalendarValue &v)
  {
   if(v.actual_value == LONG_MIN || v.forecast_value == LONG_MIN)
      return "";
   if(v.actual_value > v.forecast_value)
      return " (por encima de la previsión)";
   if(v.actual_value < v.forecast_value)
      return " (por debajo de la previsión)";
   return " (en línea con la previsión)";
  }

string ResumenValor(const MqlCalendarValue &v, const MqlCalendarEvent &ev)
  {
   return StringFormat("%s: previsión %s · anterior %s · actual %s%s", ev.name,
                       Valor(v.forecast_value, ev), Valor(v.prev_value, ev), Valor(v.actual_value, ev), Sorpresa(v));
  }

string DescribirValor(const MqlCalendarValue &v, const MqlCalendarEvent &ev)
  {
   MqlCalendarCountry pais;
   string moneda = CalendarCountryById(ev.country_id, pais) ? pais.currency : "";
   string texto = StringFormat("%s %s · %s NY\nPrevisión: %s · Anterior: %s · Actual: %s%s",
                               moneda, ev.name, HoraNy(v.time),
                               Valor(v.forecast_value, ev), Valor(v.prev_value, ev), Valor(v.actual_value, ev), Sorpresa(v));
   if(v.impact_type == CALENDAR_IMPACT_POSITIVE)
      texto += "\nImpacto en " + moneda + ": positivo";
   else if(v.impact_type == CALENDAR_IMPACT_NEGATIVE)
      texto += "\nImpacto en " + moneda + ": negativo";
   return texto;
  }

void AgregarValor(Ocurrencia &lista[], const MqlCalendarValue &v, const MqlCalendarEvent &ev)
  {
   int n = ArraySize(lista);
   int k = 0;
   while(k < n && lista[k].hora != v.time)
      k++;
   if(k == n)
     {
      ArrayResize(lista, n + 1);
      lista[k].hora        = v.time;
      lista[k].importancia = 0;
      lista[k].titulo      = "";
      lista[k].principal   = ev.name;
      lista[k].detalle     = "";
      lista[k].tooltip     = "";
     }
   lista[k].titulo  += (lista[k].titulo == "" ? "" : " / ") + ev.name;
   lista[k].detalle += (lista[k].detalle == "" ? "" : "\n") + ResumenValor(v, ev);
   lista[k].tooltip += (lista[k].tooltip == "" ? "" : "\n\n") + DescribirValor(v, ev);
   if((int)ev.importance > lista[k].importancia)
     {
      lista[k].importancia = (int)ev.importance;
      lista[k].principal   = ev.name;
     }
  }

void MoverOcurrencia(Ocurrencia &lista[], int de, int a)
  {
   lista[a].hora        = lista[de].hora;
   lista[a].importancia = lista[de].importancia;
   lista[a].titulo      = lista[de].titulo;
   lista[a].principal   = lista[de].principal;
   lista[a].detalle     = lista[de].detalle;
   lista[a].tooltip     = lista[de].tooltip;
  }

void OrdenarPorHora(Ocurrencia &lista[])
  {
   for(int i = 1; i < ArraySize(lista); i++)
     {
      datetime hora        = lista[i].hora;
      int      importancia = lista[i].importancia;
      string   titulo      = lista[i].titulo;
      string   principal   = lista[i].principal;
      string   detalle     = lista[i].detalle;
      string   tooltip     = lista[i].tooltip;
      int j = i - 1;
      while(j >= 0 && lista[j].hora > hora)
        {
         MoverOcurrencia(lista, j, j + 1);
         j--;
        }
      lista[j + 1].hora        = hora;
      lista[j + 1].importancia = importancia;
      lista[j + 1].titulo      = titulo;
      lista[j + 1].principal   = principal;
      lista[j + 1].detalle     = detalle;
      lista[j + 1].tooltip     = tooltip;
     }
  }

bool CargarNoticias(Ocurrencia &lista[], datetime desde, datetime hasta)
  {
   ArrayResize(lista, 0);
   string filtro = FiltroActivo();
   ENUM_CALENDAR_EVENT_IMPORTANCE minima = ImportanciaActiva();
   ResetLastError();
   if(InpMoneda != "")
     {
      // Se buscan primero las noticias de la moneda y luego el historial de cada una: es mucho
      // más rápido que leer todo el calendario cuando se piden varios años.
      MqlCalendarEvent eventos[];
      if(CalendarEventByCurrency(InpMoneda, eventos) <= 0)
         return false;
      for(int e = 0; e < ArraySize(eventos); e++)
        {
         if(!PasaFiltro(eventos[e], minima, filtro))
            continue;
         MqlCalendarValue valores[];
         if(!CalendarValueHistoryByEvent(eventos[e].id, valores, desde, hasta))
            continue;
         for(int i = 0; i < ArraySize(valores); i++)
            AgregarValor(lista, valores[i], eventos[e]);
        }
     }
   else
     {
      MqlCalendarValue valores[];
      if(!CalendarValueHistory(valores, desde, hasta))
         return false;
      for(int i = 0; i < ArraySize(valores); i++)
        {
         MqlCalendarEvent ev;
         if(CalendarEventById(valores[i].event_id, ev) && PasaFiltro(ev, minima, filtro))
            AgregarValor(lista, valores[i], ev);
        }
     }
   OrdenarPorHora(lista);
   return true;
  }

bool LlevaZona(int k, datetime ahora)
  {
   if(g_noticias[k].hora > ahora)
      return false;
   if(InpModoEstudio)
      return true;
   return InpZonaNoticia && (InpUsarLista || g_noticias[k].importancia >= (int)InpImportanciaAlta);
  }

string NombreLinea(int k)
  {
   return PREFIJO + "N_" + IntegerToString((long)g_noticias[k].hora);
  }

bool CargarNoticiasDelPeriodo()
  {
   datetime ahora = TimeTradeServer();
   int diasAtras = InpModoEstudio ? InpEstudioAnios * 365 : InpDiasHistorial;
   if(!CargarNoticias(g_noticias, ahora - diasAtras * 86400, ahora + InpDiasFuturo * 86400))
     {
      if(g_calendarioOk)
         PrintFormat("No se pudo leer el calendario económico (error %d). Revise que el terminal esté conectado.", GetLastError());
      g_calendarioOk = false;
      return false;
     }
   g_calendarioOk = true;
   return true;
  }

void DibujarNoticias()
  {
   datetime ahora = TimeTradeServer();

   // La zona de la noticia más reciente siempre llega hasta la vela en curso.
   datetime velaActual = VelaEnCurso();
   datetime ultimaZona = 0;
   for(int k = 0; k < ArraySize(g_noticias); k++)
      if(LlevaZona(k, ahora))
         ultimaZona = g_noticias[k].hora;

   for(int k = 0; k < ArraySize(g_noticias); k++)
     {
      int importancia = g_noticias[k].importancia;
      color clr = importancia >= (int)CALENDAR_IMPORTANCE_HIGH ? InpColorAlta :
                  importancia == (int)CALENDAR_IMPORTANCE_MODERATE ? InpColorMedia : InpColorBaja;
      bool pasada = g_noticias[k].hora <= ahora;
      string nombre = NombreLinea(k);
      if(pasada ? InpLineasPasadas : InpLineasFuturas)
        {
         if(ObjectFind(0, nombre) < 0)
            ObjectCreate(0, nombre, OBJ_VLINE, 0, g_noticias[k].hora, 0);
         ObjectSetInteger(0, nombre, OBJPROP_COLOR, clr);
         ObjectSetInteger(0, nombre, OBJPROP_STYLE, pasada ? STYLE_SOLID : STYLE_DOT); // punteada = aún no sale
         ObjectSetInteger(0, nombre, OBJPROP_BACK, true);
         ObjectSetInteger(0, nombre, OBJPROP_SELECTABLE, false);
         ObjectSetInteger(0, nombre, OBJPROP_HIDDEN, true);
         ObjectSetString(0, nombre, OBJPROP_TEXT, g_noticias[k].titulo);
         ObjectSetString(0, nombre, OBJPROP_TOOLTIP, g_noticias[k].tooltip);
        }
      else
         ObjectDelete(0, nombre); // la noticia ya salió: queda solo la zona

      if(LlevaZona(k, ahora))
        {
         datetime fin = g_noticias[k].hora + InpMinutosZonaNoticia * 60;
         if(g_noticias[k].hora == ultimaZona || InpExtenderTodas || fin > velaActual)
            fin = velaActual;
         DibujarZonaVela(PREFIJO + "NZ_" + IntegerToString((long)g_noticias[k].hora), g_noticias[k].hora, fin,
                         InpColorZonaNoticia,
                         g_noticias[k].principal + " " + EtiquetaFecha(UtcANy(ServidorAUtc(g_noticias[k].hora)), false),
                         clr, g_noticias[k].tooltip);
        }
     }
  }

//+------------------------------------------------------------------+
//| Panel del modo estudio                                           |
//+------------------------------------------------------------------+
// Cantidad de noticias que ya salieron (las primeras del arreglo, que está ordenado por hora).
int NoticiasPasadas()
  {
   datetime ahora = TimeTradeServer();
   int n = 0;
   while(n < ArraySize(g_noticias) && g_noticias[n].hora <= ahora)
      n++;
   return n;
  }

void CrearBoton(const string nombre, const string texto, int x, int ancho)
  {
   ObjectCreate(0, nombre, OBJ_BUTTON, 0, 0, 0);
   ObjectSetInteger(0, nombre, OBJPROP_CORNER, CORNER_LEFT_LOWER);
   ObjectSetInteger(0, nombre, OBJPROP_XDISTANCE, x);
   ObjectSetInteger(0, nombre, OBJPROP_YDISTANCE, 32);
   ObjectSetInteger(0, nombre, OBJPROP_XSIZE, ancho);
   ObjectSetInteger(0, nombre, OBJPROP_YSIZE, 22);
   ObjectSetString(0, nombre, OBJPROP_TEXT, texto);
   ObjectSetInteger(0, nombre, OBJPROP_FONTSIZE, 9);
   ObjectSetInteger(0, nombre, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, nombre, OBJPROP_HIDDEN, true);
  }

void CrearPanel()
  {
   string fondo = PREFIJO + "P_FONDO";
   ObjectCreate(0, fondo, OBJ_RECTANGLE_LABEL, 0, 0, 0);
   ObjectSetInteger(0, fondo, OBJPROP_CORNER, CORNER_LEFT_LOWER);
   ObjectSetInteger(0, fondo, OBJPROP_XDISTANCE, 4);
   ObjectSetInteger(0, fondo, OBJPROP_XSIZE, 720);
   ObjectSetInteger(0, fondo, OBJPROP_BGCOLOR, InpColorPanel);
   ObjectSetInteger(0, fondo, OBJPROP_BORDER_TYPE, BORDER_FLAT);
   ObjectSetInteger(0, fondo, OBJPROP_COLOR, InpColorApertura);
   ObjectSetInteger(0, fondo, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, fondo, OBJPROP_HIDDEN, true);

   for(int i = 0; i < LINEAS_PANEL; i++)
     {
      string nombre = PREFIJO + "P_L" + IntegerToString(i);
      ObjectCreate(0, nombre, OBJ_LABEL, 0, 0, 0);
      ObjectSetInteger(0, nombre, OBJPROP_CORNER, CORNER_LEFT_LOWER);
      ObjectSetInteger(0, nombre, OBJPROP_ANCHOR, ANCHOR_LEFT_LOWER);
      ObjectSetInteger(0, nombre, OBJPROP_XDISTANCE, 12);
      ObjectSetString(0, nombre, OBJPROP_FONT, "Consolas");
      ObjectSetInteger(0, nombre, OBJPROP_FONTSIZE, 9);
      ObjectSetInteger(0, nombre, OBJPROP_COLOR, InpColorTexto);
      ObjectSetInteger(0, nombre, OBJPROP_SELECTABLE, false);
      ObjectSetInteger(0, nombre, OBJPROP_HIDDEN, true);
     }

   CrearBoton(PREFIJO + "P_ANT", "◄ Anterior", 12, 90);
   CrearBoton(PREFIJO + "P_SIG", "Siguiente ►", 106, 90);
   CrearBoton(PREFIJO + "P_CSV", "Exportar CSV", 200, 100);
  }

void MostrarLineas(const string &lineas[])
  {
   int n = ArraySize(lineas) < LINEAS_PANEL ? ArraySize(lineas) : LINEAS_PANEL;
   for(int i = 0; i < LINEAS_PANEL; i++)
     {
      string nombre = PREFIJO + "P_L" + IntegerToString(i);
      ObjectSetString(0, nombre, OBJPROP_TEXT, i < n ? lineas[i] : " ");
      ObjectSetInteger(0, nombre, OBJPROP_YDISTANCE, 40 + (n - 1 - i) * ALTO_LINEA);
     }
   string fondo = PREFIJO + "P_FONDO";
   ObjectSetInteger(0, fondo, OBJPROP_YDISTANCE, 40 + n * ALTO_LINEA + 6);
   ObjectSetInteger(0, fondo, OBJPROP_YSIZE, 40 + n * ALTO_LINEA + 2);
  }

void AgregarLinea(string &lineas[], const string texto)
  {
   int n = ArraySize(lineas);
   ArrayResize(lineas, n + 1);
   lineas[n] = texto;
  }

// Promedios de la vela de la noticia y de la apertura en todas las publicaciones cargadas.
string Promedios(int pasadas)
  {
   double rangoNoticia = 0, rangoApertura = 0;
   int velasNoticia = 0, velasApertura = 0, alcistasNoticia = 0, alcistasApertura = 0;
   for(int k = 0; k < pasadas; k++)
     {
      MqlRates vela;
      if(DatosVela(g_noticias[k].hora, vela))
        {
         rangoNoticia += vela.high - vela.low;
         velasNoticia++;
         if(vela.close > vela.open)
            alcistasNoticia++;
        }
      if(DatosVela(AperturaServidor(DiaNy(g_noticias[k].hora)), vela))
        {
         rangoApertura += vela.high - vela.low;
         velasApertura++;
         if(vela.close > vela.open)
            alcistasApertura++;
        }
     }
   if(velasNoticia == 0 && velasApertura == 0)
      return "Promedios: sin historial de velas para esas fechas";
   return StringFormat("Promedio (%d de %d con velas): noticia rango %s, %d%% alcistas · apertura rango %s, %d%% alcistas",
                       velasNoticia, pasadas,
                       Precio(velasNoticia > 0 ? rangoNoticia / velasNoticia : 0),
                       velasNoticia > 0 ? alcistasNoticia * 100 / velasNoticia : 0,
                       Precio(velasApertura > 0 ? rangoApertura / velasApertura : 0),
                       velasApertura > 0 ? alcistasApertura * 100 / velasApertura : 0);
  }

// Hasta dónde llega el historial de velas que usan las zonas (depende del bróker y de "Máx. barras").
string HistorialDisponible()
  {
   ENUM_TIMEFRAMES tf = TFVela();
   datetime primera = (datetime)SeriesInfoInteger(_Symbol, tf, SERIES_FIRSTDATE);
   string nombreTf = StringSubstr(EnumToString(tf), 7);
   if(primera == 0)
      return "Historial " + nombreTf + ": cargando...";
   return StringFormat("Historial %s disponible desde %s (Máx. barras: %d)", nombreTf,
                       TimeToString(primera, TIME_DATE), TerminalInfoInteger(TERMINAL_MAXBARS));
  }

void ActualizarPanel()
  {
   string lineas[];
   int pasadas = NoticiasPasadas();
   string tf = StringSubstr(EnumToString(TFVela()), 7);
   if(pasadas == 0)
     {
      AgregarLinea(lineas, "Estudio: \"" + InpEstudioNoticia + "\" · no se encontraron publicaciones");
      AgregarLinea(lineas, "Revise el nombre de la noticia (en inglés, por ejemplo CPI, Nonfarm, FOMC) y la moneda.");
      MostrarLineas(lineas);
      return;
     }
   if(g_indice < 0 || g_indice >= pasadas)
      g_indice = pasadas - 1;

   int k = g_indice;
   AgregarLinea(lineas, StringFormat("Estudio: \"%s\" · %d de %d publicaciones (%d años)",
                                     InpEstudioNoticia, k + 1, pasadas, InpEstudioAnios));
   AgregarLinea(lineas, HoraNy(g_noticias[k].hora) + " NY");
   string detalle[];
   int n = StringSplit(g_noticias[k].detalle, '\n', detalle);
   for(int i = 0; i < n; i++)
      AgregarLinea(lineas, "  " + detalle[i]);
   AgregarLinea(lineas, "Vela de la noticia (" + tf + "): " + DescribirVela(g_noticias[k].hora));
   AgregarLinea(lineas, "Vela de apertura NY (" + tf + "): " + DescribirVela(AperturaServidor(DiaNy(g_noticias[k].hora))));
   AgregarLinea(lineas, Promedios(pasadas));
   AgregarLinea(lineas, HistorialDisponible());
   MostrarLineas(lineas);

   // Marca con una línea punteada la noticia que se está viendo.
   string marca = PREFIJO + "P_SEL";
   if(ObjectFind(0, marca) < 0)
      ObjectCreate(0, marca, OBJ_VLINE, 0, g_noticias[k].hora, 0);
   else
      ObjectMove(0, marca, 0, g_noticias[k].hora, 0);
   ObjectSetInteger(0, marca, OBJPROP_COLOR, InpColorTexto);
   ObjectSetInteger(0, marca, OBJPROP_STYLE, STYLE_DOT);
   ObjectSetInteger(0, marca, OBJPROP_BACK, true);
   ObjectSetInteger(0, marca, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, marca, OBJPROP_HIDDEN, true);
  }

void IrA(int indice)
  {
   int pasadas = NoticiasPasadas();
   if(pasadas == 0)
      return;
   g_indice = indice < 0 ? 0 : (indice >= pasadas ? pasadas - 1 : indice);
   ActualizarPanel();

   // Centra el gráfico en la vela de la noticia.
   int shift = iBarShift(_Symbol, PERIOD_CURRENT, g_noticias[g_indice].hora, false);
   if(shift >= 0)
     {
      ChartSetInteger(0, CHART_AUTOSCROLL, false);
      int visibles = (int)ChartGetInteger(0, CHART_VISIBLE_BARS);
      int derecha = shift - visibles / 2; // vela que queda en el borde derecho
      ChartNavigate(0, CHART_END, derecha > 0 ? -derecha : 0);
     }
   ChartRedraw();
  }

void ExportarCsv()
  {
   string nombre = InpEstudioNoticia;
   StringReplace(nombre, ";", "_");
   StringReplace(nombre, "/", "_");
   StringReplace(nombre, " ", "_");
   nombre = "ZonasEventosNY_" + _Symbol + "_" + nombre + ".csv";

   int archivo = FileOpen(nombre, FILE_WRITE | FILE_CSV | FILE_ANSI, ';');
   if(archivo == INVALID_HANDLE)
     {
      PrintFormat("No se pudo crear %s (error %d)", nombre, GetLastError());
      return;
     }
   FileWrite(archivo, "Fecha y hora NY", "Noticias", "Datos",
             "Noticia apertura", "Noticia máximo", "Noticia mínimo", "Noticia cierre", "Noticia rango", "Noticia dirección",
             "Apertura NY apertura", "Apertura NY máximo", "Apertura NY mínimo", "Apertura NY cierre", "Apertura NY rango", "Apertura NY dirección");
   int pasadas = NoticiasPasadas();
   for(int k = 0; k < pasadas; k++)
     {
      string datos = g_noticias[k].detalle;
      StringReplace(datos, "\n", " | ");
      MqlRates noticia, apertura;
      bool hayNoticia  = DatosVela(g_noticias[k].hora, noticia);
      bool hayApertura = DatosVela(AperturaServidor(DiaNy(g_noticias[k].hora)), apertura);
      FileWrite(archivo, HoraNy(g_noticias[k].hora), g_noticias[k].titulo, datos,
                hayNoticia ? Precio(noticia.open) : "", hayNoticia ? Precio(noticia.high) : "",
                hayNoticia ? Precio(noticia.low) : "", hayNoticia ? Precio(noticia.close) : "",
                hayNoticia ? Precio(noticia.high - noticia.low) : "", hayNoticia ? Direccion(noticia) : "",
                hayApertura ? Precio(apertura.open) : "", hayApertura ? Precio(apertura.high) : "",
                hayApertura ? Precio(apertura.low) : "", hayApertura ? Precio(apertura.close) : "",
                hayApertura ? Precio(apertura.high - apertura.low) : "", hayApertura ? Direccion(apertura) : "");
     }
   FileClose(archivo);
   Alert("CSV guardado en ", TerminalInfoString(TERMINAL_DATA_PATH), "\\MQL5\\Files\\", nombre);
  }

void DibujarTodo()
  {
   CalcularDesfase();
   bool mostrarNoticias = InpMostrarNoticias || InpModoEstudio;
   if(mostrarNoticias || (InpMostrarApertura && InpAperturaSoloNoticias))
     {
      if(CargarNoticiasDelPeriodo() && mostrarNoticias)
         DibujarNoticias();
     }
   if(InpMostrarApertura)
      DibujarAperturas(); // con "solo días con noticia" usa las noticias recién cargadas
   if(InpModoEstudio)
      ActualizarPanel();
   g_ultimoDibujo = TimeLocal();
   ChartRedraw();
  }

//+------------------------------------------------------------------+
//| Avisos                                                           |
//+------------------------------------------------------------------+
bool LeerCalendario(MqlCalendarValue &valores[], datetime desde, datetime hasta)
  {
   if(InpMoneda == "")
      return CalendarValueHistory(valores, desde, hasta) > 0;
   return CalendarValueHistory(valores, desde, hasta, NULL, InpMoneda) > 0;
  }

int LeerCambios(MqlCalendarValue &cambios[])
  {
   if(InpMoneda == "")
      return CalendarValueLast(g_cambioCalendario, cambios);
   return CalendarValueLast(g_cambioCalendario, cambios, NULL, InpMoneda);
  }

bool YaEsta(const ulong &lista[], ulong id)
  {
   for(int i = 0; i < ArraySize(lista); i++)
      if(lista[i] == id)
         return true;
   return false;
  }

void Agregar(ulong &lista[], ulong id)
  {
   int n = ArraySize(lista);
   ArrayResize(lista, n + 1);
   lista[n] = id;
  }

void Avisar(string texto)
  {
   StringReplace(texto, "\n", " | ");
   Alert(_Symbol, " ", texto);
   if(InpNotificacionMovil)
      SendNotification(StringSubstr(texto, 0, 255));
  }

void AvisarPublicaciones(const MqlCalendarValue &cambios[])
  {
   if(!InpAvisoPublicacion)
      return;
   datetime ahora = TimeTradeServer();
   for(int i = 0; i < ArraySize(cambios); i++)
     {
      // Solo datos recién publicados, no revisiones de noticias antiguas.
      if(cambios[i].actual_value == LONG_MIN || ahora - cambios[i].time > 3600 || YaEsta(g_avisados, cambios[i].id))
         continue;
      MqlCalendarEvent ev;
      if(!CalendarEventById(cambios[i].event_id, ev) || !SeAvisa(ev))
         continue;
      Agregar(g_avisados, cambios[i].id);
      Avisar("Publicado: " + DescribirValor(cambios[i], ev));
     }
  }

void AvisarProximas()
  {
   if(InpMinutosPreaviso <= 0)
      return;
   datetime ahora = TimeTradeServer();
   MqlCalendarValue proximas[];
   if(!LeerCalendario(proximas, ahora, ahora + InpMinutosPreaviso * 60))
      return;
   for(int i = 0; i < ArraySize(proximas); i++)
     {
      if(YaEsta(g_preavisados, proximas[i].id))
         continue;
      MqlCalendarEvent ev;
      if(!CalendarEventById(proximas[i].event_id, ev) || !SeAvisa(ev))
         continue;
      Agregar(g_preavisados, proximas[i].id);
      int minutos = (int)((proximas[i].time - ahora) / 60);
      Avisar(StringFormat("En %d min: %s", minutos, DescribirValor(proximas[i], ev)));
     }
  }

//+------------------------------------------------------------------+
//| Eventos del indicador                                            |
//+------------------------------------------------------------------+
int OnInit()
  {
   CalcularDesfase();
   if(InpMostrarNoticias)
     {
      MqlCalendarValue inicial[];
      LeerCambios(inicial); // la primera llamada solo guarda el punto de partida
     }
   if(InpListarNombres)
      ListarNombres();
   if(InpModoEstudio)
     {
      CrearPanel();
      // Varios años de velas pueden superar el límite de barras del terminal.
      long necesarias = (long)InpEstudioAnios * 365 * 86400 / PeriodSeconds(TFVela());
      if(TerminalInfoInteger(TERMINAL_MAXBARS) < necesarias)
         PrintFormat("Aviso: para %d años en %s hacen falta unas %I64d barras y el terminal permite %d. "
                     "Suba 'Máx. barras en el gráfico' en Herramientas > Opciones > Gráficos.",
                     InpEstudioAnios, StringSubstr(EnumToString(TFVela()), 7), necesarias,
                     TerminalInfoInteger(TERMINAL_MAXBARS));
     }
   EventSetTimer(InpSegundosRevision > 0 ? InpSegundosRevision : 10);

   datetime hoyNy = UtcANy(TimeGMT());
   hoyNy -= (datetime)((long)hoyNy % 86400);
   int desfase = (int)(UtcAServidor(TimeGMT()) - TimeGMT()) / 3600;
   PrintFormat("Servidor en UTC%s%d. Apertura de Nueva York de hoy en hora del servidor: %s",
               desfase >= 0 ? "+" : "", desfase, TimeToString(AperturaServidor(hoyNy), TIME_MINUTES));
   return INIT_SUCCEEDED;
  }

void OnDeinit(const int reason)
  {
   EventKillTimer();
   ObjectsDeleteAll(0, PREFIJO);
   ChartRedraw();
  }

void OnTimer()
  {
   bool redibujar = TimeLocal() - g_ultimoDibujo >= 60;
   if(InpMostrarNoticias)
     {
      MqlCalendarValue cambios[];
      if(LeerCambios(cambios) > 0)
        {
         AvisarPublicaciones(cambios);
         redibujar = true;
        }
      AvisarProximas();
     }
   if(redibujar)
      DibujarTodo();
  }

void OnChartEvent(const int id, const long &lparam, const double &dparam, const string &sparam)
  {
   if(id != CHARTEVENT_OBJECT_CLICK || !InpModoEstudio)
      return;
   if(sparam == PREFIJO + "P_ANT")
      IrA(g_indice - 1);
   else if(sparam == PREFIJO + "P_SIG")
      IrA(g_indice + 1);
   else if(sparam == PREFIJO + "P_CSV")
      ExportarCsv();
   else
      return;
   ObjectSetInteger(0, sparam, OBJPROP_STATE, false);
   ChartRedraw();
  }

int OnCalculate(const int rates_total,
                const int prev_calculated,
                const datetime &time[],
                const double &open[],
                const double &high[],
                const double &low[],
                const double &close[],
                const long &tick_volume[],
                const long &volume[],
                const int &spread[])
  {
   if(rates_total > 0 && (prev_calculated == 0 || time[rates_total - 1] != g_ultimaBarra))
     {
      g_ultimaBarra = time[rates_total - 1];
      DibujarTodo();
     }
   return rates_total;
  }
//+------------------------------------------------------------------+
