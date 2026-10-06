//+------------------------------------------------------------------+
//|                                           OpenCloseExtremos.mq4  |
//| Marca las velas cuya apertura o cierre coincide con el máximo    |
//| o el mínimo de la vela (velas sin mecha en uno de sus extremos). |
//|                                                                  |
//|  ▼ rojo/naranja sobre la vela : Apertura/Cierre = Máximo         |
//|  ▲ verde/azul bajo la vela    : Apertura/Cierre = Mínimo         |
//+------------------------------------------------------------------+
#property copyright "OpenCloseExtremos"
#property version   "1.30"
#property strict
#property indicator_chart_window
#property indicator_buffers 4
#property indicator_color1  clrRed
#property indicator_color2  clrOrange
#property indicator_color3  clrLime
#property indicator_color4  clrDodgerBlue
#property indicator_width1  2
#property indicator_width2  2
#property indicator_width3  2
#property indicator_width4  2

//--- entradas
enum ENUM_DIR_NIVELES
  {
   DIR_AMBAS  = 0,   // Ambas
   DIR_VERDES = 1,   // Solo verdes (niveles en mínimos)
   DIR_ROJAS  = 2    // Solo rojas (niveles en máximos)
  };

input int    InpToleranciaPuntos = 0;     // Tolerancia en puntos (0 = exacto)
input bool   InpMarcarApertura   = true;  // Marcar Apertura = Máx/Mín
input bool   InpMarcarCierre     = true;  // Marcar Cierre = Máx/Mín
input bool   InpVelaActual       = false; // Marcar también la vela en formación
input double InpSeparacionATR    = 0.3;   // Separación de la flecha (x ATR14)
input bool   InpAlertaPopup      = false; // Alerta emergente al cerrar la vela
input bool   InpAlertaPush       = false; // Notificación push al móvil
input bool   InpAlertaSonido     = false; // Sonido
input string InpArchivoSonido    = "alert.wav";
input bool   InpMostrarEstadistica = true;  // Mostrar panel de porcentajes
input int    InpBarrasEstadistica  = 1000;  // Velas cerradas a analizar (0 = todas)
input bool   InpNiveles          = true;            // Dibujar niveles sin mecha (desequilibrios)
input bool   InpNivelesCierre    = false;           // Incluir también niveles de cierre
input bool   InpMostrarTesteados = true;            // Mantener los niveles ya testeados
input int    InpVelasNiveles     = 500;             // Velas cerradas a revisar para niveles
input color  InpColorNivelMin    = C'46,125,80';    // Color nivel en mínimo (pendiente)
input color  InpColorNivelMax    = C'150,60,60';    // Color nivel en máximo (pendiente)
input color  InpColorTesteado    = C'75,75,75';     // Color nivel ya testeado
input ENUM_TIMEFRAMES  InpTFNiveles = PERIOD_CURRENT;  // Temporalidad de los niveles
input ENUM_DIR_NIVELES InpDireccion = DIR_AMBAS;       // Dirección de los niveles
input bool   InpSesAsia          = true;            // Niveles nacidos en Asia (01–10 h servidor)
input bool   InpSesLondres       = true;            // Niveles nacidos en Londres (10–15 h)
input bool   InpSesLondresNY     = true;            // Niveles nacidos en Londres+NY (15–19 h)
input bool   InpSesNYTarde       = true;            // Niveles nacidos en NY tarde (19–24 h)
input int    InpVelasTesteadoVisible = 0;           // Ocultar testeados tras N velas (0 = nunca)
input bool   InpPermitirOcultar  = true;            // Permitir ocultar líneas a mano (Supr)
input bool   InpBotonRestaurar   = true;            // Botón para restaurar niveles ocultos

//--- buffers
double BufOpenHigh[];
double BufCloseHigh[];
double BufOpenLow[];
double BufCloseLow[];

double   g_tol;
datetime g_ultimaAlerta = 0;
datetime g_ultimaEstadistica = 0;
datetime g_ultimosNiveles = 0;

#define RAY_PROP OBJPROP_RAY
#define NV_PREFIX "OCE_Nivel_"
struct Nivel
  {
   string            nombre;
   double            precio;
   bool              abajo;     // true = nivel en un mínimo (el precio quedó por encima)
  };
Nivel g_pendientes[];
string   g_dibujados[];            // líneas dibujadas en la última reconstrucción
datetime g_ultimaVelaTF = 0;
#define GV_PREFIX     "OCE_O_"
#define BTN_RESTAURAR "OCE_BtnRestaurar"
double   g_tablaTeorica[201];

//+------------------------------------------------------------------+
int OnInit()
  {
   SetIndexBuffer(0, BufOpenHigh);
   SetIndexBuffer(1, BufCloseHigh);
   SetIndexBuffer(2, BufOpenLow);
   SetIndexBuffer(3, BufCloseLow);

   for(int p = 0; p < 4; p++)
     {
      SetIndexStyle(p, DRAW_ARROW);
      SetIndexEmptyValue(p, EMPTY_VALUE);
     }
   SetIndexArrow(0, 234); SetIndexLabel(0, "Apertura = Máximo");
   SetIndexArrow(1, 234); SetIndexLabel(1, "Cierre = Máximo");
   SetIndexArrow(2, 233); SetIndexLabel(2, "Apertura = Mínimo");
   SetIndexArrow(3, 233); SetIndexLabel(3, "Cierre = Mínimo");

   // medio punto de margen para evitar errores de redondeo en doubles
   g_tol = (InpToleranciaPuntos + 0.5) * _Point;

   IndicatorShortName("OpenCloseExtremos");
   IndicatorDigits(_Digits);
   PrepararTablaTeorica();
   return(INIT_SUCCEEDED);
  }

//+------------------------------------------------------------------+
bool Igual(const double a, const double b)
  {
   return(MathAbs(a - b) <= g_tol);
  }

//+------------------------------------------------------------------+
//| Referencia teórica (teorema de Sparre Andersen): en un camino    |
//| aleatorio simétrico de m pasos, la probabilidad de que ningún    |
//| paso supere al punto inicial es C(2m,m)/4^m ~ 1/sqrt(pi*m).      |
//| Con n ticks en la vela hay m = n-1 pasos.                         |
//+------------------------------------------------------------------+
void PrepararTablaTeorica()
  {
   g_tablaTeorica[0] = 1.0;
   for(int k = 1; k <= 200; k++)
      g_tablaTeorica[k] = g_tablaTeorica[k - 1] * (2.0 * k - 1.0) / (2.0 * k);
  }

double ProbTeorica(const long ticks)
  {
   long m = ticks - 1;
   if(m <= 0)   return(1.0);
   if(m <= 200) return(g_tablaTeorica[(int)m]);
   return(1.0 / MathSqrt(M_PI * (double)m));
  }

//+------------------------------------------------------------------+
//| Acumuladores del panel de estadística                            |
//+------------------------------------------------------------------+
int    st_n, st_oh, st_ch, st_ol, st_cl, st_alguna;
double st_ticks, st_ticksMarc, st_ticksNo, st_teo;

void EstadisticaReset()
  {
   st_n = st_oh = st_ch = st_ol = st_cl = st_alguna = 0;
   st_ticks = st_ticksMarc = st_ticksNo = st_teo = 0.0;
  }

void EstadisticaSumar(const double o, const double h, const double l,
                      const double c, const long tv)
  {
   if(Igual(h, l))   // vela sin rango: no cuenta
      return;
   bool oh = Igual(o, h), ch = Igual(c, h), ol = Igual(o, l), cl = Igual(c, l);
   st_n++;
   if(oh) st_oh++;
   if(ch) st_ch++;
   if(ol) st_ol++;
   if(cl) st_cl++;
   st_ticks += (double)tv;
   st_teo   += ProbTeorica(tv);
   if(oh || ch || ol || cl) { st_alguna++; st_ticksMarc += (double)tv; }
   else                       st_ticksNo += (double)tv;
  }

string Pct(const int x)
  {
   return(StringFormat("%5.1f%%  (%d)", 100.0 * x / MathMax(st_n, 1), x));
  }

void EstadisticaMostrar()
  {
   int sinMarca = st_n - st_alguna;
   string t = StringFormat("OpenCloseExtremos  |  %s  |  %d velas cerradas analizadas\n", _Symbol, st_n);
   t += "Apertura = Máximo :  " + Pct(st_oh) + "\n";
   t += "Cierre   = Máximo :  " + Pct(st_ch) + "\n";
   t += "Apertura = Mínimo :  " + Pct(st_ol) + "\n";
   t += "Cierre   = Mínimo :  " + Pct(st_cl) + "\n";
   t += "Al menos un caso  :  " + Pct(st_alguna) + "\n";
   t += StringFormat("Ticks promedio por vela: %.1f   (marcadas: %.1f  |  sin marca: %.1f)\n",
                     st_ticks / MathMax(st_n, 1),
                     st_ticksMarc / MathMax(st_alguna, 1),
                     st_ticksNo / MathMax(sinMarca, 1));
   t += StringFormat("Referencia modelo aleatorio, por caso: %.1f%%", 100.0 * st_teo / MathMax(st_n, 1));
   Comment(t);
  }

//+------------------------------------------------------------------+
//| Niveles sin mecha: línea punteada desde el extremo sin mecha de  |
//| la vela hasta que una vela posterior lo vuelve a tocar.          |
//| Las líneas se pueden ocultar a mano (seleccionar + Supr); el     |
//| indicador lo recuerda en variables globales del terminal.        |
//+------------------------------------------------------------------+
ENUM_TIMEFRAMES TFNiveles()
  {
   return(InpTFNiveles == PERIOD_CURRENT ? (ENUM_TIMEFRAMES)_Period : InpTFNiveles);
  }

string TFTexto(const ENUM_TIMEFRAMES tf)
  {
   string s = EnumToString(tf);
   StringReplace(s, "PERIOD_", "");
   return(s);
  }

string ClaveOculto(const string nombre)
  {
   return(GV_PREFIX + _Symbol + "_" + StringSubstr(nombre, StringLen(NV_PREFIX)));
  }

bool EstaOculto(const string nombre)
  {
   string k = ClaveOculto(nombre);
   if(!GlobalVariableCheck(k))
      return(false);
   GlobalVariableGet(k);            // renueva la fecha de acceso (MT borra las no usadas en 4 semanas)
   return(true);
  }

int ContarOcultos()
  {
   string pre = GV_PREFIX + _Symbol + "_";
   int n = 0;
   for(int i = GlobalVariablesTotal() - 1; i >= 0; i--)
      if(StringFind(GlobalVariableName(i), pre) == 0)
         n++;
   return(n);
  }

void AgregarDibujado(const string nombre)
  {
   int k = ArraySize(g_dibujados);
   ArrayResize(g_dibujados, k + 1, 200);
   g_dibujados[k] = nombre;
  }

void QuitarDibujado(const string nombre)
  {
   int last = ArraySize(g_dibujados) - 1;
   for(int k = last; k >= 0; k--)
      if(g_dibujados[k] == nombre)
        {
         g_dibujados[k] = g_dibujados[last];
         ArrayResize(g_dibujados, last);
         return;
        }
  }

//--- las líneas que dibujamos y ya no están en el gráfico las borró el usuario
void RegistrarOcultosManuales()
  {
   if(InpPermitirOcultar)
      for(int k = 0; k < ArraySize(g_dibujados); k++)
         if(ObjectFind(0, g_dibujados[k]) < 0)
            GlobalVariableSet(ClaveOculto(g_dibujados[k]), 1);
   ArrayResize(g_dibujados, 0);
  }

bool SesionPermitida(const datetime t)
  {
   MqlDateTime s;
   TimeToStruct(t, s);
   if(s.hour < 10) return(InpSesAsia);        // la hora 00 cuenta como Asia
   if(s.hour < 15) return(InpSesLondres);
   if(s.hour < 19) return(InpSesLondresNY);
   return(InpSesNYTarde);
  }

void ActualizarBoton()
  {
   int n = InpBotonRestaurar ? ContarOcultos() : 0;
   if(n == 0)
     {
      ObjectDelete(0, BTN_RESTAURAR);
      return;
     }
   if(ObjectFind(0, BTN_RESTAURAR) < 0)
     {
      ObjectCreate(0, BTN_RESTAURAR, OBJ_BUTTON, 0, 0, 0);
      ObjectSetInteger(0, BTN_RESTAURAR, OBJPROP_CORNER, CORNER_LEFT_LOWER);
      ObjectSetInteger(0, BTN_RESTAURAR, OBJPROP_XDISTANCE, 10);
      ObjectSetInteger(0, BTN_RESTAURAR, OBJPROP_YDISTANCE, 45);
      ObjectSetInteger(0, BTN_RESTAURAR, OBJPROP_XSIZE, 230);
      ObjectSetInteger(0, BTN_RESTAURAR, OBJPROP_YSIZE, 22);
      ObjectSetInteger(0, BTN_RESTAURAR, OBJPROP_FONTSIZE, 8);
      ObjectSetInteger(0, BTN_RESTAURAR, OBJPROP_COLOR, clrWhite);
      ObjectSetInteger(0, BTN_RESTAURAR, OBJPROP_BGCOLOR, C'60,60,60');
      ObjectSetInteger(0, BTN_RESTAURAR, OBJPROP_SELECTABLE, false);
      ObjectSetInteger(0, BTN_RESTAURAR, OBJPROP_HIDDEN, true);
     }
   ObjectSetString(0, BTN_RESTAURAR, OBJPROP_TEXT, StringFormat("Restaurar niveles ocultos (%d)", n));
   ObjectSetInteger(0, BTN_RESTAURAR, OBJPROP_STATE, false);
  }

void CrearLineaNivel(const string nombre, const datetime t0, const datetime t1,
                     const double p, const bool testeado, const bool abajo, const string texto)
  {
   if(!ObjectCreate(0, nombre, OBJ_TREND, 0, t0, p, t1, p))
      return;
   ObjectSetInteger(0, nombre, OBJPROP_COLOR, testeado ? InpColorTesteado : (abajo ? InpColorNivelMin : InpColorNivelMax));
   ObjectSetInteger(0, nombre, OBJPROP_STYLE, STYLE_DOT);
   ObjectSetInteger(0, nombre, OBJPROP_WIDTH, 1);
   ObjectSetInteger(0, nombre, RAY_PROP, !testeado);
   ObjectSetInteger(0, nombre, OBJPROP_BACK, true);
   ObjectSetInteger(0, nombre, OBJPROP_SELECTABLE, InpPermitirOcultar);
   ObjectSetInteger(0, nombre, OBJPROP_HIDDEN, false);
   ObjectSetString(0, nombre, OBJPROP_TOOLTIP, texto + (testeado ? " (testeado)" : " (no testeado)"));
  }

void AgregarPendiente(const string nombre, const double p, const bool abajo)
  {
   int n = ArraySize(g_pendientes);
   ArrayResize(g_pendientes, n + 1);
   g_pendientes[n].nombre = nombre;
   g_pendientes[n].precio = p;
   g_pendientes[n].abajo  = abajo;
  }

//--- revisa en cada tick si la vela actual toca algún nivel pendiente
void RevisarPendientes(const datetime t, const double h, const double l)
  {
   for(int k = ArraySize(g_pendientes) - 1; k >= 0; k--)
     {
      bool toca = g_pendientes[k].abajo ? (l <= g_pendientes[k].precio + g_tol)
                                        : (h >= g_pendientes[k].precio - g_tol);
      if(!toca)
         continue;
      string n = g_pendientes[k].nombre;
      if(ObjectFind(0, n) >= 0)              // si el usuario la ocultó, no se toca
        {
         if(!InpMostrarTesteados)
           {
            ObjectDelete(0, n);
            QuitarDibujado(n);
           }
         else
           {
            ObjectMove(0, n, 1, t, g_pendientes[k].precio);
            ObjectSetInteger(0, n, RAY_PROP, false);
            ObjectSetInteger(0, n, OBJPROP_COLOR, InpColorTesteado);
            ObjectSetString(0, n, OBJPROP_TOOLTIP, ObjectGetString(0, n, OBJPROP_TOOLTIP) + " → testeado");
           }
        }
      int last = ArraySize(g_pendientes) - 1;
      if(k != last)
        {
         g_pendientes[k].nombre = g_pendientes[last].nombre;
         g_pendientes[k].precio = g_pendientes[last].precio;
         g_pendientes[k].abajo  = g_pendientes[last].abajo;
        }
      ArrayResize(g_pendientes, last);
     }
  }

void NivelDesde(const MqlRates &r[], const int n, const int i, const double p, const bool abajo,
                const string tft, const string cod, const string texto, const datetime ahora)
  {
   string nombre = NV_PREFIX + tft + "_" + cod + "_" + IntegerToString((long)r[i].time);
   if(InpPermitirOcultar && EstaOculto(nombre))
      return;
   int jt = -1;
   for(int j = i + 1; j < n; j++)
      if(abajo ? (r[j].low <= p + g_tol) : (r[j].high >= p - g_tol)) { jt = j; break; }
   if(jt >= 0)
     {
      if(!InpMostrarTesteados)
         return;
      if(InpVelasTesteadoVisible > 0 &&
         (long)(ahora - r[jt].time) > (long)InpVelasTesteadoVisible * PeriodSeconds((ENUM_TIMEFRAMES)_Period))
         return;
     }
   string tip = StringFormat("%s %s %s  %s", tft, texto, DoubleToString(p, _Digits),
                             TimeToString(r[i].time, TIME_DATE | TIME_MINUTES));
   CrearLineaNivel(nombre, r[i].time, (jt >= 0) ? r[jt].time : r[n - 1].time, p, jt >= 0, abajo, tip);
   AgregarDibujado(nombre);
   if(jt < 0)
      AgregarPendiente(nombre, p, abajo);
  }

//--- devuelve false si el historial de la temporalidad de niveles aún no está disponible
bool ConstruirNiveles(const datetime ahora)
  {
   RegistrarOcultosManuales();
   ObjectsDeleteAll(0, NV_PREFIX);
   ArrayResize(g_pendientes, 0);
   if(!InpNiveles)
     {
      ActualizarBoton();
      return(true);
     }
   ENUM_TIMEFRAMES tf = TFNiveles();
   MqlRates r[];
   ArraySetAsSeries(r, false);                // r[0] = la más antigua, r[n-1] = en formación
   int n = CopyRates(_Symbol, tf, 0, InpVelasNiveles + 1, r);
   if(n < 2)
      return(false);
   string tft    = TFTexto(tf);
   bool   verdes = (InpDireccion != DIR_ROJAS);
   bool   rojas  = (InpDireccion != DIR_VERDES);
   for(int i = 0; i <= n - 2; i++)
     {
      if(Igual(r[i].high, r[i].low) || !SesionPermitida(r[i].time))
         continue;
      bool oh = Igual(r[i].open, r[i].high),  ol = Igual(r[i].open, r[i].low);
      bool ch = Igual(r[i].close, r[i].high), cl = Igual(r[i].close, r[i].low);
      if(oh && rojas)  NivelDesde(r, n, i, r[i].high, false, tft, "AMax", "Apertura = Máximo", ahora);
      if(ol && verdes) NivelDesde(r, n, i, r[i].low,  true,  tft, "AMin", "Apertura = Mínimo", ahora);
      if(InpNivelesCierre)
        {
         if(ch && !oh && rojas)  NivelDesde(r, n, i, r[i].high, false, tft, "CMax", "Cierre = Máximo", ahora);
         if(cl && !ol && verdes) NivelDesde(r, n, i, r[i].low,  true,  tft, "CMin", "Cierre = Mínimo", ahora);
        }
     }
   ActualizarBoton();
   return(true);
  }

//+------------------------------------------------------------------+
void OnChartEvent(const int id, const long &lparam, const double &dparam, const string &sparam)
  {
   if(id == CHARTEVENT_OBJECT_CLICK && sparam == BTN_RESTAURAR)
     {
      GlobalVariablesDeleteAll(GV_PREFIX + _Symbol + "_");
      ArrayResize(g_dibujados, 0);
      ObjectDelete(0, BTN_RESTAURAR);
      g_ultimosNiveles = 0;
      g_ultimaVelaTF   = 0;
      ChartSetSymbolPeriod(0, _Symbol, (ENUM_TIMEFRAMES)_Period);   // fuerza el recálculo
     }
  }

//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
   ArrayResize(g_dibujados, 0);          // lo que borra el propio indicador no cuenta como ocultado
   ObjectsDeleteAll(0, NV_PREFIX);
   ObjectDelete(0, BTN_RESTAURAR);
   Comment("");
  }

//+------------------------------------------------------------------+
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
   if(rates_total < 2)
      return(0);

   // en MQL4 los arrays son serie: índice 0 = vela en formación
   int limite = (prev_calculated > 1) ? rates_total - prev_calculated + 1 : rates_total - 1;

   for(int i = limite; i >= 0; i--)
     {
      BufOpenHigh[i] = BufCloseHigh[i] = BufOpenLow[i] = BufCloseLow[i] = EMPTY_VALUE;

      if(i == 0 && !InpVelaActual)
         continue;
      if(Igual(high[i], low[i]))           // vela sin rango
         continue;

      double sep = iATR(NULL, 0, 14, i) * InpSeparacionATR;
      if(sep <= 0) sep = 10 * _Point;

      if(InpMarcarApertura && Igual(open[i],  high[i])) BufOpenHigh[i]  = high[i] + sep;
      if(InpMarcarCierre   && Igual(close[i], high[i])) BufCloseHigh[i] = high[i] + sep * 2.2;
      if(InpMarcarApertura && Igual(open[i],  low[i]))  BufOpenLow[i]   = low[i]  - sep;
      if(InpMarcarCierre   && Igual(close[i], low[i]))  BufCloseLow[i]  = low[i]  - sep * 2.2;
     }

   //--- alerta sobre la última vela cerrada (índice 1)
   if(prev_calculated == 0)
      g_ultimaAlerta = time[1];   // no alertar velas históricas al cargar
   else if(time[1] != g_ultimaAlerta &&
           (InpAlertaPopup || InpAlertaPush || InpAlertaSonido))
     {
      string tipo = "";
      if(BufOpenHigh[1]  != EMPTY_VALUE) tipo += " Apertura=Máximo";
      if(BufCloseHigh[1] != EMPTY_VALUE) tipo += " Cierre=Máximo";
      if(BufOpenLow[1]   != EMPTY_VALUE) tipo += " Apertura=Mínimo";
      if(BufCloseLow[1]  != EMPTY_VALUE) tipo += " Cierre=Mínimo";

      if(tipo != "")
        {
         string msg = StringFormat("%s M%d vela %s:%s", _Symbol, _Period,
                                   TimeToString(time[1], TIME_DATE | TIME_MINUTES), tipo);
         if(InpAlertaPopup)  Alert(msg);
         if(InpAlertaPush)   SendNotification(msg);
         if(InpAlertaSonido) PlaySound(InpArchivoSonido);
        }
      g_ultimaAlerta = time[1];
     }

   //--- niveles sin mecha: se reconstruyen en cada vela nueva y se revisan en cada tick
   datetime velaTF = iTime(_Symbol, TFNiveles(), 0);
   if(prev_calculated == 0 || time[0] != g_ultimosNiveles || velaTF != g_ultimaVelaTF)
     {
      if(ConstruirNiveles(time[0]))
        {
         g_ultimosNiveles = time[0];
         g_ultimaVelaTF   = velaTF;
        }
     }
   else
      RevisarPendientes(time[0], high[0], low[0]);

   //--- panel de estadística (se recalcula una vez por vela nueva)
   if(InpMostrarEstadistica && (prev_calculated == 0 || time[0] != g_ultimaEstadistica))
     {
      int hasta = (InpBarrasEstadistica > 0) ? MathMin(InpBarrasEstadistica, rates_total - 1) : rates_total - 1;
      EstadisticaReset();
      for(int k = 1; k <= hasta; k++)   // índice 1 = última vela cerrada
         EstadisticaSumar(open[k], high[k], low[k], close[k], tick_volume[k]);
      EstadisticaMostrar();
      g_ultimaEstadistica = time[0];
     }

   return(rates_total);
  }
//+------------------------------------------------------------------+
