//+------------------------------------------------------------------+
//|                                           OpenCloseExtremos.mq4  |
//| Marca las velas cuya apertura o cierre coincide con el máximo    |
//| o el mínimo de la vela (velas sin mecha en uno de sus extremos). |
//|                                                                  |
//|  ▼ rojo/naranja sobre la vela : Apertura/Cierre = Máximo         |
//|  ▲ verde/azul bajo la vela    : Apertura/Cierre = Mínimo         |
//+------------------------------------------------------------------+
#property copyright "OpenCloseExtremos"
#property version   "1.20"
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
//+------------------------------------------------------------------+
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
   ObjectSetInteger(0, nombre, OBJPROP_SELECTABLE, false);
   ObjectSetInteger(0, nombre, OBJPROP_HIDDEN, true);
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
      if(!InpMostrarTesteados)
         ObjectDelete(0, n);
      else
        {
         ObjectMove(0, n, 1, t, g_pendientes[k].precio);
         ObjectSetInteger(0, n, RAY_PROP, false);
         ObjectSetInteger(0, n, OBJPROP_COLOR, InpColorTesteado);
         ObjectSetString(0, n, OBJPROP_TOOLTIP, ObjectGetString(0, n, OBJPROP_TOOLTIP) + " → testeado");
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

void NivelDesde(const int i, const double p, const bool abajo, const string cod, const string texto,
                const datetime &time[], const double &high[], const double &low[])
  {
   int jt = -1;
   for(int j = i - 1; j >= 0; j--)                     // series: j menor = más reciente
      if(abajo ? (low[j] <= p + g_tol) : (high[j] >= p - g_tol)) { jt = j; break; }
   if(jt >= 0 && !InpMostrarTesteados)
      return;
   string nombre = NV_PREFIX + cod + "_" + IntegerToString((long)time[i]);
   string tip = StringFormat("%s %s  %s", texto, DoubleToString(p, _Digits), TimeToString(time[i], TIME_DATE | TIME_MINUTES));
   CrearLineaNivel(nombre, time[i], (jt >= 0) ? time[jt] : time[0], p, jt >= 0, abajo, tip);
   if(jt < 0)
      AgregarPendiente(nombre, p, abajo);
  }

void ConstruirNiveles(const int rates_total, const datetime &time[], const double &open[],
                      const double &high[], const double &low[], const double &close[])
  {
   ObjectsDeleteAll(0, NV_PREFIX);
   ArrayResize(g_pendientes, 0);
   if(!InpNiveles)
      return;
   int desde = MathMin(InpVelasNiveles, rates_total - 1);
   for(int i = desde; i >= 1; i--)                     // índice 1 = última vela cerrada
     {
      if(Igual(high[i], low[i]))
         continue;
      bool oh = Igual(open[i], high[i]),  ol = Igual(open[i], low[i]);
      bool ch = Igual(close[i], high[i]), cl = Igual(close[i], low[i]);
      if(oh) NivelDesde(i, high[i], false, "AMax", "Apertura = Máximo", time, high, low);
      if(ol) NivelDesde(i, low[i],  true,  "AMin", "Apertura = Mínimo", time, high, low);
      if(InpNivelesCierre)
        {
         if(ch && !oh) NivelDesde(i, high[i], false, "CMax", "Cierre = Máximo", time, high, low);
         if(cl && !ol) NivelDesde(i, low[i],  true,  "CMin", "Cierre = Mínimo", time, high, low);
        }
     }
  }

//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
   ObjectsDeleteAll(0, NV_PREFIX);
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
   if(prev_calculated == 0 || time[0] != g_ultimosNiveles)
     {
      ConstruirNiveles(rates_total, time, open, high, low, close);
      g_ultimosNiveles = time[0];
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
