//+------------------------------------------------------------------+
//|                                               ZonasEventosNY.mq5 |
//| Marca la vela de apertura de Nueva York (NYSE / Nasdaq, 9:30 NY) |
//| y las noticias del calendario económico de MT5, pasadas y nuevas.|
//| Las noticias nuevas se detectan solas cada pocos segundos.       |
//+------------------------------------------------------------------+
#property copyright   "Marvin Cuestas"
#property version     "1.00"
#property description "Zonas de la vela de apertura de Nueva York y de las noticias del calendario económico."
#property indicator_chart_window
#property indicator_buffers 0
#property indicator_plots   0

#define PREFIJO "ZENY_"

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
input int             InpHoraFinZona     = 16;            // Extender la zona hasta (hora de Nueva York)
input ENUM_TIMEFRAMES InpTFVela          = PERIOD_M15;    // Temporalidad de la vela (apertura y noticias)
input int             InpDiasHistorial   = 30;            // Días hacia atrás
input color           InpColorApertura   = C'35,70,120';  // Color de la zona de apertura
input color           InpColorTexto      = clrSilver;     // Color de las etiquetas

input group "Noticias (calendario económico de MT5)"
input bool   InpMostrarNoticias = true;                                          // Marcar noticias
input string InpMoneda          = "USD";                                         // Moneda (vacío = todas)
input ENUM_CALENDAR_EVENT_IMPORTANCE InpImportanciaMinima = CALENDAR_IMPORTANCE_MODERATE; // Importancia mínima para la línea
input ENUM_CALENDAR_EVENT_IMPORTANCE InpImportanciaAlta   = CALENDAR_IMPORTANCE_HIGH;     // Importancia mínima para zona y avisos
input string InpFiltroNombre    = "";                                            // Solo noticias que contengan (separar con ;)
input int    InpDiasFuturo      = 7;                                             // Días hacia adelante
input bool   InpZonaNoticia     = true;                                          // Marcar la vela de la noticia
input int    InpMinutosZonaNoticia = 120;                                        // Extender la zona de la noticia (minutos)
input color  InpColorAlta       = clrRed;                                        // Color importancia alta
input color  InpColorMedia      = clrOrange;                                     // Color importancia media
input color  InpColorBaja       = clrGold;                                       // Color importancia baja
input color  InpColorZonaNoticia = C'110,35,35';                                 // Color de la zona de la noticia

input group "Avisos"
input int    InpSegundosRevision  = 10;    // Revisar el calendario cada (segundos)
input bool   InpAvisoPublicacion  = true;  // Avisar cuando se publica el dato
input int    InpMinutosPreaviso   = 5;     // Avisar antes de la noticia (minutos, 0 = no)
input bool   InpNotificacionMovil = false; // Enviar también al móvil (MetaQuotes ID)

int      g_desfaseBase      = 0;  // desfase del servidor respecto a UTC en invierno, en segundos
ulong    g_cambioCalendario = 0;  // último cambio conocido del calendario
datetime g_ultimoDibujo     = 0;
datetime g_ultimaBarra      = 0;
bool     g_calendarioOk     = true;
ulong    g_avisados[];            // valores ya avisados al publicarse
ulong    g_preavisados[];         // valores ya avisados antes de publicarse

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

ENUM_TIMEFRAMES TFVela()
  {
   return InpTFVela == PERIOD_CURRENT ? (ENUM_TIMEFRAMES)_Period : InpTFVela;
  }

//+------------------------------------------------------------------+
//| Dibujo                                                           |
//+------------------------------------------------------------------+
// Dibuja (o actualiza) un rectángulo con el máximo y el mínimo de la vela que contiene `inicio`.
bool DibujarZonaVela(const string nombre, datetime inicio, datetime fin, color clr,
                     const string etiqueta, const string tooltip)
  {
   ENUM_TIMEFRAMES tf = TFVela();
   int shift = iBarShift(_Symbol, tf, inicio, false);
   if(shift < 0)
      return false;
   datetime tVela = iTime(_Symbol, tf, shift);
   if(tVela == 0 || inicio - tVela >= PeriodSeconds(tf))
      return false; // sin vela a esa hora (festivo o historial aún sin cargar)
   double alto = iHigh(_Symbol, tf, shift);
   double bajo = iLow(_Symbol, tf, shift);

   if(ObjectFind(0, nombre) < 0)
      ObjectCreate(0, nombre, OBJ_RECTANGLE, 0, tVela, alto, fin, bajo);
   else
     {
      ObjectMove(0, nombre, 0, tVela, alto);
      ObjectMove(0, nombre, 1, fin, bajo);
     }
   ObjectSetInteger(0, nombre, OBJPROP_COLOR, clr);
   ObjectSetInteger(0, nombre, OBJPROP_FILL, true);
   ObjectSetInteger(0, nombre, OBJPROP_BACK, true);
   ObjectSetInteger(0, nombre, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, nombre, OBJPROP_HIDDEN, true);
   ObjectSetString(0, nombre, OBJPROP_TOOLTIP, tooltip + "\nMáximo: " + DoubleToString(alto, _Digits) +
                   "   Mínimo: " + DoubleToString(bajo, _Digits));

   string nombreTexto = nombre + "_T";
   if(ObjectFind(0, nombreTexto) < 0)
      ObjectCreate(0, nombreTexto, OBJ_TEXT, 0, tVela, alto);
   else
      ObjectMove(0, nombreTexto, 0, tVela, alto);
   ObjectSetString(0, nombreTexto, OBJPROP_TEXT, etiqueta);
   ObjectSetInteger(0, nombreTexto, OBJPROP_COLOR, InpColorTexto);
   ObjectSetInteger(0, nombreTexto, OBJPROP_FONTSIZE, 8);
   ObjectSetInteger(0, nombreTexto, OBJPROP_ANCHOR, ANCHOR_LEFT_LOWER);
   ObjectSetInteger(0, nombreTexto, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, nombreTexto, OBJPROP_HIDDEN, true);
   return true;
  }

void DibujarAperturas()
  {
   datetime ahora = TimeTradeServer();
   datetime hoyNy = UtcANy(TimeGMT());
   hoyNy -= (datetime)((long)hoyNy % 86400);
   for(int i = 0; i <= InpDiasHistorial; i++)
     {
      datetime dia = hoyNy - i * 86400;
      MqlDateTime t;
      TimeToStruct(dia, t);
      if(t.day_of_week == 0 || t.day_of_week == 6)
         continue;
      datetime inicio = UtcAServidor(NyAUtc(dia + InpHoraApertura * 3600 + InpMinutoApertura * 60));
      if(inicio > ahora)
         continue;
      datetime fin = UtcAServidor(NyAUtc(dia + InpHoraFinZona * 3600));
      string fecha = TimeToString(dia, TIME_DATE);
      DibujarZonaVela(PREFIJO + "AP_" + fecha, inicio, fin, InpColorApertura, "Apertura NY",
                      StringFormat("Apertura de Nueva York %s %02d:%02d (hora NY)", fecha, InpHoraApertura, InpMinutoApertura));
     }
  }

//+------------------------------------------------------------------+
//| Calendario económico                                             |
//+------------------------------------------------------------------+
bool LeerCalendario(MqlCalendarValue &valores[], datetime desde, datetime hasta)
  {
   if(InpMoneda == "")
      return CalendarValueHistory(valores, desde, hasta);
   return CalendarValueHistory(valores, desde, hasta, NULL, InpMoneda);
  }

int LeerCambios(MqlCalendarValue &cambios[])
  {
   if(InpMoneda == "")
      return CalendarValueLast(g_cambioCalendario, cambios);
   return CalendarValueLast(g_cambioCalendario, cambios, NULL, InpMoneda);
  }

bool PasaFiltro(const MqlCalendarEvent &ev, ENUM_CALENDAR_EVENT_IMPORTANCE minima)
  {
   if((int)ev.importance < (int)minima)
      return false;
   if(InpFiltroNombre == "")
      return true;
   string nombre = ev.name;
   StringToLower(nombre);
   string partes[];
   int n = StringSplit(InpFiltroNombre, ';', partes);
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

string DescribirValor(const MqlCalendarValue &v, const MqlCalendarEvent &ev)
  {
   MqlCalendarCountry pais;
   string moneda = CalendarCountryById(ev.country_id, pais) ? pais.currency : "";
   datetime ny = UtcANy(ServidorAUtc(v.time));
   string texto = StringFormat("%s %s · %s NY\nPrevisión: %s · Anterior: %s · Actual: %s",
                               moneda, ev.name, TimeToString(ny, TIME_DATE | TIME_MINUTES),
                               Valor(v.forecast_value, ev), Valor(v.prev_value, ev), Valor(v.actual_value, ev));
   if(v.actual_value != LONG_MIN && v.forecast_value != LONG_MIN)
     {
      if(v.actual_value > v.forecast_value)
         texto += " (por encima de la previsión)";
      else if(v.actual_value < v.forecast_value)
         texto += " (por debajo de la previsión)";
      else
         texto += " (en línea con la previsión)";
     }
   if(v.impact_type == CALENDAR_IMPACT_POSITIVE)
      texto += "\nImpacto en " + moneda + ": positivo";
   else if(v.impact_type == CALENDAR_IMPACT_NEGATIVE)
      texto += "\nImpacto en " + moneda + ": negativo";
   return texto;
  }

void DibujarNoticias()
  {
   datetime ahora = TimeTradeServer();
   MqlCalendarValue valores[];
   ResetLastError();
   if(!LeerCalendario(valores, ahora - InpDiasHistorial * 86400, ahora + InpDiasFuturo * 86400))
     {
      if(g_calendarioOk)
         PrintFormat("No se pudo leer el calendario económico (error %d). Revise que el terminal esté conectado.", GetLastError());
      g_calendarioOk = false;
      return;
     }
   g_calendarioOk = true;

   // Agrupa las noticias que salen a la misma hora en una sola línea.
   datetime horas[];
   string   titulos[];
   string   textos[];
   int      importancias[];
   for(int i = 0; i < ArraySize(valores); i++)
     {
      MqlCalendarEvent ev;
      if(!CalendarEventById(valores[i].event_id, ev) || !PasaFiltro(ev, InpImportanciaMinima))
         continue;
      int n = ArraySize(horas);
      int k = 0;
      while(k < n && horas[k] != valores[i].time)
         k++;
      if(k == n)
        {
         ArrayResize(horas, n + 1);
         ArrayResize(titulos, n + 1);
         ArrayResize(textos, n + 1);
         ArrayResize(importancias, n + 1);
         horas[k] = valores[i].time;
         titulos[k] = "";
         textos[k] = "";
         importancias[k] = 0;
        }
      titulos[k] += (titulos[k] == "" ? "" : " / ") + ev.name;
      textos[k]  += (textos[k] == "" ? "" : "\n\n") + DescribirValor(valores[i], ev);
      if((int)ev.importance > importancias[k])
         importancias[k] = (int)ev.importance;
     }

   for(int k = 0; k < ArraySize(horas); k++)
     {
      color clr = importancias[k] >= (int)CALENDAR_IMPORTANCE_HIGH ? InpColorAlta :
                  importancias[k] == (int)CALENDAR_IMPORTANCE_MODERATE ? InpColorMedia : InpColorBaja;
      string nombre = PREFIJO + "N_" + IntegerToString((long)horas[k]);
      if(ObjectFind(0, nombre) < 0)
         ObjectCreate(0, nombre, OBJ_VLINE, 0, horas[k], 0);
      ObjectSetInteger(0, nombre, OBJPROP_COLOR, clr);
      ObjectSetInteger(0, nombre, OBJPROP_STYLE, horas[k] <= ahora ? STYLE_SOLID : STYLE_DOT); // punteada = aún no sale
      ObjectSetInteger(0, nombre, OBJPROP_BACK, true);
      ObjectSetInteger(0, nombre, OBJPROP_SELECTABLE, false);
      ObjectSetInteger(0, nombre, OBJPROP_HIDDEN, true);
      ObjectSetString(0, nombre, OBJPROP_TEXT, titulos[k]);
      ObjectSetString(0, nombre, OBJPROP_TOOLTIP, textos[k]);

      if(InpZonaNoticia && importancias[k] >= (int)InpImportanciaAlta && horas[k] <= ahora)
         DibujarZonaVela(PREFIJO + "NZ_" + IntegerToString((long)horas[k]), horas[k],
                         horas[k] + InpMinutosZonaNoticia * 60, InpColorZonaNoticia, "Noticia", textos[k]);
     }
  }

void DibujarTodo()
  {
   CalcularDesfase();
   if(InpMostrarApertura)
      DibujarAperturas();
   if(InpMostrarNoticias)
      DibujarNoticias();
   g_ultimoDibujo = TimeLocal();
   ChartRedraw();
  }

//+------------------------------------------------------------------+
//| Avisos                                                           |
//+------------------------------------------------------------------+
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
      if(!CalendarEventById(cambios[i].event_id, ev) || !PasaFiltro(ev, InpImportanciaAlta))
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
      if(!CalendarEventById(proximas[i].event_id, ev) || !PasaFiltro(ev, InpImportanciaAlta))
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
   EventSetTimer(InpSegundosRevision > 0 ? InpSegundosRevision : 10);

   datetime hoyNy = UtcANy(TimeGMT());
   hoyNy -= (datetime)((long)hoyNy % 86400);
   datetime aperturaHoy = UtcAServidor(NyAUtc(hoyNy + InpHoraApertura * 3600 + InpMinutoApertura * 60));
   int desfase = (int)(UtcAServidor(TimeGMT()) - TimeGMT()) / 3600;
   PrintFormat("Servidor en UTC%s%d. Apertura de Nueva York de hoy en hora del servidor: %s",
               desfase >= 0 ? "+" : "", desfase, TimeToString(aperturaHoy, TIME_MINUTES));
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
