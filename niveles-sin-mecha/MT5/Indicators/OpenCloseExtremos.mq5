//+------------------------------------------------------------------+
//|                                           OpenCloseExtremos.mq5  |
//| Marca las velas cuya apertura o cierre coincide con el máximo    |
//| o el mínimo de la vela (velas sin mecha en uno de sus extremos). |
//|                                                                  |
//|  ▼ rojo/naranja sobre la vela : Apertura/Cierre = Máximo         |
//|  ▲ verde/azul bajo la vela    : Apertura/Cierre = Mínimo         |
//+------------------------------------------------------------------+
#property copyright "OpenCloseExtremos"
#property version   "1.40"
#property indicator_chart_window
#property indicator_buffers 4
#property indicator_plots   4

#property indicator_label1  "Apertura = Máximo"
#property indicator_type1   DRAW_ARROW
#property indicator_color1  clrRed
#property indicator_width1  2

#property indicator_label2  "Cierre = Máximo"
#property indicator_type2   DRAW_ARROW
#property indicator_color2  clrOrange
#property indicator_width2  2

#property indicator_label3  "Apertura = Mínimo"
#property indicator_type3   DRAW_ARROW
#property indicator_color3  clrLime
#property indicator_width3  2

#property indicator_label4  "Cierre = Mínimo"
#property indicator_type4   DRAW_ARROW
#property indicator_color4  clrDodgerBlue
#property indicator_width4  2

//--- entradas
input group "General"
input int    InpToleranciaPuntos = 0;     // Tolerancia en puntos (0 = exacto)
input bool   InpVelaActual       = false; // Marcar también la vela en formación
input int    InpDesplazamientoPx = 12;    // Separación de la flecha (píxeles)

input group "Flecha roja · Apertura = Máximo"
input bool   InpOHMostrar    = true;       // Mostrar flecha
input color  InpOHColor      = clrRed;    // Color de la flecha
input int    InpOHTamano     = 2;          // Tamaño de la flecha (1–5)
input int    InpOHSimbolo    = 234;        // Símbolo (código Wingdings)
input bool   InpOHAlerta     = true;       // Incluir en las alertas al cerrar la vela
input bool   InpOHNivel      = true;       // Dibujar su línea de nivel
input color  InpOHColorNivel = C'150,60,60'; // Color de su línea pendiente

input group "Flecha naranja · Cierre = Máximo"
input bool   InpCHMostrar    = true;       // Mostrar flecha
input color  InpCHColor      = clrOrange; // Color de la flecha
input int    InpCHTamano     = 2;          // Tamaño de la flecha (1–5)
input int    InpCHSimbolo    = 234;        // Símbolo (código Wingdings)
input bool   InpCHAlerta     = true;       // Incluir en las alertas al cerrar la vela
input bool   InpCHNivel      = false;      // Dibujar su línea de nivel
input color  InpCHColorNivel = C'150,100,40'; // Color de su línea pendiente

input group "Flecha verde · Apertura = Mínimo"
input bool   InpOLMostrar    = true;       // Mostrar flecha
input color  InpOLColor      = clrLime;   // Color de la flecha
input int    InpOLTamano     = 2;          // Tamaño de la flecha (1–5)
input int    InpOLSimbolo    = 233;        // Símbolo (código Wingdings)
input bool   InpOLAlerta     = true;       // Incluir en las alertas al cerrar la vela
input bool   InpOLNivel      = true;       // Dibujar su línea de nivel
input color  InpOLColorNivel = C'46,125,80'; // Color de su línea pendiente

input group "Flecha azul · Cierre = Mínimo"
input bool   InpCLMostrar    = true;       // Mostrar flecha
input color  InpCLColor      = clrDodgerBlue; // Color de la flecha
input int    InpCLTamano     = 2;          // Tamaño de la flecha (1–5)
input int    InpCLSimbolo    = 233;        // Símbolo (código Wingdings)
input bool   InpCLAlerta     = true;       // Incluir en las alertas al cerrar la vela
input bool   InpCLNivel      = false;      // Dibujar su línea de nivel
input color  InpCLColorNivel = C'40,90,150'; // Color de su línea pendiente

input group "Canales de alerta"
input bool   InpAlertaPopup      = false; // Alerta emergente
input bool   InpAlertaPush       = false; // Notificación push al móvil
input bool   InpAlertaSonido     = false; // Sonido
input string InpArchivoSonido    = "alert.wav"; // Archivo de sonido

input group "Panel de porcentajes"
input bool   InpMostrarEstadistica = true;  // Mostrar panel de porcentajes
input int    InpBarrasEstadistica  = 1000;  // Velas cerradas a analizar (0 = todas)

input group "Niveles (comunes a todas las flechas)"
input bool   InpNiveles          = true;            // Dibujar niveles sin mecha (desequilibrios)
input bool   InpMostrarTesteados = true;            // Mantener los niveles ya testeados
input int    InpVelasNiveles     = 500;             // Velas a revisar para niveles
input color  InpColorTesteado    = C'75,75,75';     // Color nivel ya testeado
input ENUM_TIMEFRAMES  InpTFNiveles = PERIOD_CURRENT;  // Temporalidad de los niveles
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

#define RAY_PROP OBJPROP_RAY_RIGHT
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
void EstiloFlecha(const int p, const int simbolo, const color col, const int tam)
  {
   PlotIndexSetInteger(p, PLOT_ARROW, simbolo);
   PlotIndexSetInteger(p, PLOT_LINE_COLOR, col);
   PlotIndexSetInteger(p, PLOT_LINE_WIDTH, MathMax(1, MathMin(5, tam)));
  }

//+------------------------------------------------------------------+
int OnInit()
  {
   SetIndexBuffer(0, BufOpenHigh,  INDICATOR_DATA);
   SetIndexBuffer(1, BufCloseHigh, INDICATOR_DATA);
   SetIndexBuffer(2, BufOpenLow,   INDICATOR_DATA);
   SetIndexBuffer(3, BufCloseLow,  INDICATOR_DATA);

   EstiloFlecha(0, InpOHSimbolo, InpOHColor, InpOHTamano);
   EstiloFlecha(1, InpCHSimbolo, InpCHColor, InpCHTamano);
   EstiloFlecha(2, InpOLSimbolo, InpOLColor, InpOLTamano);
   EstiloFlecha(3, InpCLSimbolo, InpCLColor, InpCLTamano);

   // desplazamiento vertical en píxeles (negativo = hacia arriba)
   PlotIndexSetInteger(0, PLOT_ARROW_SHIFT, -InpDesplazamientoPx);
   PlotIndexSetInteger(1, PLOT_ARROW_SHIFT, -InpDesplazamientoPx * 2 - 4);
   PlotIndexSetInteger(2, PLOT_ARROW_SHIFT,  InpDesplazamientoPx);
   PlotIndexSetInteger(3, PLOT_ARROW_SHIFT,  InpDesplazamientoPx * 2 + 4);

   for(int p = 0; p < 4; p++)
      PlotIndexSetDouble(p, PLOT_EMPTY_VALUE, EMPTY_VALUE);

   // medio punto de margen para evitar errores de redondeo en doubles
   g_tol = (InpToleranciaPuntos + 0.5) * _Point;

   IndicatorSetString(INDICATOR_SHORTNAME, "OpenCloseExtremos");
   IndicatorSetInteger(INDICATOR_DIGITS, _Digits);
   PrepararTablaTeorica();
   return(INIT_SUCCEEDED);
  }

//+------------------------------------------------------------------+
bool Igual(const double a, const double b)
  {
   return(MathAbs(a - b) <= g_tol);
  }

//+------------------------------------------------------------------+
void Evaluar(const int i, const double &open[], const double &high[],
             const double &low[], const double &close[])
  {
   BufOpenHigh[i]  = EMPTY_VALUE;
   BufCloseHigh[i] = EMPTY_VALUE;
   BufOpenLow[i]   = EMPTY_VALUE;
   BufCloseLow[i]  = EMPTY_VALUE;

   // ignorar velas sin rango (high == low)
   if(Igual(high[i], low[i]))
      return;

   if(InpOHMostrar && Igual(open[i],  high[i])) BufOpenHigh[i]  = high[i];
   if(InpCHMostrar && Igual(close[i], high[i])) BufCloseHigh[i] = high[i];
   if(InpOLMostrar && Igual(open[i],  low[i]))  BufOpenLow[i]   = low[i];
   if(InpCLMostrar && Igual(close[i], low[i]))  BufCloseLow[i]  = low[i];
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
                     const double p, const bool testeado, const bool abajo, const string texto,
                     const color col)
  {
   if(!ObjectCreate(0, nombre, OBJ_TREND, 0, t0, p, t1, p))
      return;
   ObjectSetInteger(0, nombre, OBJPROP_COLOR, testeado ? InpColorTesteado : col);
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
                const string tft, const string cod, const string texto, const datetime ahora,
                const color col)
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
   CrearLineaNivel(nombre, r[i].time, (jt >= 0) ? r[jt].time : r[n - 1].time, p, jt >= 0, abajo, tip, col);
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
   for(int i = 0; i <= n - 2; i++)
     {
      if(Igual(r[i].high, r[i].low) || !SesionPermitida(r[i].time))
         continue;
      bool oh = Igual(r[i].open, r[i].high),  ol = Igual(r[i].open, r[i].low);
      bool ch = Igual(r[i].close, r[i].high), cl = Igual(r[i].close, r[i].low);
      bool nOH = oh && InpOHNivel, nOL = ol && InpOLNivel;
      if(nOH) NivelDesde(r, n, i, r[i].high, false, tft, "AMax", "Apertura = Máximo", ahora, InpOHColorNivel);
      if(nOL) NivelDesde(r, n, i, r[i].low,  true,  tft, "AMin", "Apertura = Mínimo", ahora, InpOLColorNivel);
      // si apertura y cierre coinciden en el mismo extremo, el nivel solo se dibuja una vez
      if(ch && !nOH && InpCHNivel) NivelDesde(r, n, i, r[i].high, false, tft, "CMax", "Cierre = Máximo", ahora, InpCHColorNivel);
      if(cl && !nOL && InpCLNivel) NivelDesde(r, n, i, r[i].low,  true,  tft, "CMin", "Cierre = Mínimo", ahora, InpCLColorNivel);
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

   // índice 0 = vela más antigua, rates_total-1 = vela en formación
   int inicio = (prev_calculated > 1) ? prev_calculated - 2 : 0;

   for(int i = inicio; i < rates_total; i++)
     {
      if(i == rates_total - 1 && !InpVelaActual)
        {
         BufOpenHigh[i] = BufCloseHigh[i] = BufOpenLow[i] = BufCloseLow[i] = EMPTY_VALUE;
         continue;
        }
      Evaluar(i, open, high, low, close);
     }

   //--- alerta sobre la última vela cerrada
   int c = rates_total - 2;
   if(prev_calculated == 0)
      g_ultimaAlerta = time[c];   // no alertar velas históricas al cargar
   else if(time[c] != g_ultimaAlerta &&
           (InpAlertaPopup || InpAlertaPush || InpAlertaSonido))
     {
      string tipo = "";
      if(InpOHAlerta && BufOpenHigh[c] != EMPTY_VALUE) tipo += " Apertura=Máximo";
      if(InpCHAlerta && BufCloseHigh[c] != EMPTY_VALUE) tipo += " Cierre=Máximo";
      if(InpOLAlerta && BufOpenLow[c] != EMPTY_VALUE) tipo += " Apertura=Mínimo";
      if(InpCLAlerta && BufCloseLow[c] != EMPTY_VALUE) tipo += " Cierre=Mínimo";

      if(tipo != "")
        {
         string msg = StringFormat("%s %s vela %s:%s", _Symbol,
                                   EnumToString((ENUM_TIMEFRAMES)_Period),
                                   TimeToString(time[c], TIME_DATE | TIME_MINUTES), tipo);
         if(InpAlertaPopup)  Alert(msg);
         if(InpAlertaPush)   SendNotification(msg);
         if(InpAlertaSonido) PlaySound(InpArchivoSonido);
        }
      g_ultimaAlerta = time[c];
     }

   //--- niveles sin mecha: se reconstruyen en cada vela nueva y se revisan en cada tick
   datetime velaTF = iTime(_Symbol, TFNiveles(), 0);
   if(prev_calculated == 0 || time[rates_total - 1] != g_ultimosNiveles || velaTF != g_ultimaVelaTF)
     {
      if(ConstruirNiveles(time[rates_total - 1]))
        {
         g_ultimosNiveles = time[rates_total - 1];
         g_ultimaVelaTF   = velaTF;
        }
     }
   else
      RevisarPendientes(time[rates_total - 1], high[rates_total - 1], low[rates_total - 1]);

   //--- panel de estadística (se recalcula una vez por vela nueva)
   if(InpMostrarEstadistica && (prev_calculated == 0 || time[rates_total - 1] != g_ultimaEstadistica))
     {
      int hasta = rates_total - 2;   // última vela cerrada
      int desde = (InpBarrasEstadistica > 0) ? MathMax(0, hasta - InpBarrasEstadistica + 1) : 0;
      EstadisticaReset();
      for(int k = desde; k <= hasta; k++)
         EstadisticaSumar(open[k], high[k], low[k], close[k], tick_volume[k]);
      EstadisticaMostrar();
      g_ultimaEstadistica = time[rates_total - 1];
     }

   return(rates_total);
  }
//+------------------------------------------------------------------+
