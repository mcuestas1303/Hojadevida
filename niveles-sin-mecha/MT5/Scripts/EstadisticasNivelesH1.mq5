//+------------------------------------------------------------------+
//|                                        EstadisticasNivelesH1.mq5 |
//| Igual que EstadisticasNiveles, pero mide la reacción tras el     |
//| test con velas H1 en lugar de M1. El historial H1 es mucho más   |
//| largo, así que H4, D1 y W1 tienen muchos más casos medidos.      |
//|   flecha verde = Apertura = Mínimo (nivel en el mínimo)          |
//|   flecha roja  = Apertura = Máximo (nivel en el máximo)          |
//| Compara con un grupo de control: aperturas CON mecha.            |
//|                                                                  |
//| Uso: arrastrar el script a un gráfico del activo (cualquier      |
//| temporalidad). El informe se guarda en MQL5\Files.               |
//+------------------------------------------------------------------+
#property copyright "OpenCloseExtremos"
#property version   "1.00"
#property description "Estadísticas de niveles sin mecha con la reacción medida en H1"
#property script_show_inputs

input string InpTemporalidades  = "H1,H4,D1,W1";            // Temporalidades a analizar (H1 o mayores)
input int    InpBarrasTF        = 50000;   // Velas máximas por temporalidad
input int    InpBarrasBase      = 100000;  // Velas H1 para medir la reacción
input int    InpToleranciaPts   = 0;       // Tolerancia en puntos (0 = exacto)
input int    InpVelasReaccion   = 4;       // Velas H1 tras el test para medir la reacción
input bool   InpGrupoControl    = true;    // Comparar con aperturas con mecha
input bool   InpExportarCSV     = true;    // Exportar cada nivel a un CSV

//--- tipos de nivel
#define T_AMIN 0   // Apertura = Mínimo (flecha verde)
#define T_AMAX 1   // Apertura = Máximo (flecha roja)
#define T_CMIN 2   // control: vela alcista con mecha inferior, nivel = apertura
#define T_CMAX 3   // control: vela bajista con mecha superior, nivel = apertura
#define N_TIPOS 4

string NOMBRE_TIPO[N_TIPOS] =
  {
   "Apertura = Mínimo (flecha verde)",
   "Apertura = Máximo (flecha roja)",
   "Control: apertura con mecha (alcista)",
   "Control: apertura con mecha (bajista)"
  };

struct Grupo
  {
   int               n, test, w1, w5, w20, w100;
   int               nReac, resp, nAtr;
   double            sumReb, sumPen, sumRebAtr, sumPenAtr;
   int               velas[];
   void              Grupo(void)
     {
      n = test = w1 = w5 = w20 = w100 = 0;
      nReac = resp = nAtr = 0;
      sumReb = sumPen = sumRebAtr = sumPenAtr = 0.0;
     }
  };

Grupo            g_gr[];
ENUM_TIMEFRAMES  g_tf[];
string           g_tfNombre[];
MqlRates         g_base[];
int              g_nbase = 0;
double           g_tol = 0;
int              g_csv = INVALID_HANDLE;
string           g_rep[];
string           g_pend[];

//+------------------------------------------------------------------+
void Linea(const string s)
  {
   int n = ArraySize(g_rep);
   ArrayResize(g_rep, n + 1, 200);
   g_rep[n] = s;
   Print(s);
  }

bool TfDesdeTexto(string s, ENUM_TIMEFRAMES &tf)
  {
   StringTrimLeft(s);
   StringTrimRight(s);
   StringToUpper(s);
   if(s == "M1")       tf = PERIOD_M1;
   else if(s == "M2")  tf = PERIOD_M2;
   else if(s == "M3")  tf = PERIOD_M3;
   else if(s == "M5")  tf = PERIOD_M5;
   else if(s == "M10") tf = PERIOD_M10;
   else if(s == "M15") tf = PERIOD_M15;
   else if(s == "M30") tf = PERIOD_M30;
   else if(s == "H1")  tf = PERIOD_H1;
   else if(s == "H2")  tf = PERIOD_H2;
   else if(s == "H4")  tf = PERIOD_H4;
   else if(s == "H8")  tf = PERIOD_H8;
   else if(s == "D1")  tf = PERIOD_D1;
   else if(s == "W1")  tf = PERIOD_W1;
   else return(false);
   return(true);
  }

string Duracion(const double segundos)
  {
   if(segundos < 3600)  return(StringFormat("%.0f min", segundos / 60.0));
   if(segundos < 86400) return(StringFormat("%.1f h", segundos / 3600.0));
   return(StringFormat("%.1f días", segundos / 86400.0));
  }

int CopiarVelas(const ENUM_TIMEFRAMES tf, const int cuantas, MqlRates &r[])
  {
   ArraySetAsSeries(r, false);              // r[0] = la más antigua
   int n = -1;
   for(int intento = 0; intento < 10 && n <= 0; intento++)
     {
      n = CopyRates(_Symbol, tf, 1, cuantas, r);   // desde 1: sin la vela en formación
      if(n <= 0)
         Sleep(500);
     }
   return(n);
  }

//--- primera vela H1 con time >= t
int IndiceBase(const datetime t)
  {
   int lo = 0, hi = g_nbase;
   while(lo < hi)
     {
      int mid = (lo + hi) / 2;
      if(g_base[mid].time < t) lo = mid + 1;
      else                   hi = mid;
     }
   return(lo);
  }

double Percentil(int &v[], const double q)
  {
   int n = ArraySize(v);
   if(n == 0) return(0);
   int c[];
   ArrayCopy(c, v);
   ArraySort(c);
   int k = (int)MathFloor(q * (n - 1));
   return(c[k]);
  }

//+------------------------------------------------------------------+
//| Analiza un nivel: busca su primer test y mide la reacción en H1  |
//+------------------------------------------------------------------+
void Analizar(const int tfi, const int tipo, const MqlRates &r[], const int n,
              const int i, const double p, const bool abajo)
  {
   int g = tfi * N_TIPOS + tipo;
   g_gr[g].n++;
   int psec = PeriodSeconds(g_tf[tfi]);

   int jt = -1;
   for(int j = i + 1; j < n; j++)
      if(abajo ? (r[j].low <= p + g_tol) : (r[j].high >= p - g_tol)) { jt = j; break; }

   string sTest = "0", sVelas = "", sMin = "", sReb = "", sPen = "", sResp = "", sRebAtr = "", sPenAtr = "";

   if(jt < 0)
     {
      if(tipo == T_AMIN || tipo == T_AMAX)
        {
         int k = ArraySize(g_pend);
         ArrayResize(g_pend, k + 1, 100);
         g_pend[k] = StringFormat("   %s %s · %s · formado %s", g_tfNombre[tfi],
                                  tipo == T_AMIN ? "verde (mínimo)" : "roja (máximo)",
                                  DoubleToString(p, _Digits), TimeToString(r[i].time, TIME_DATE | TIME_MINUTES));
        }
     }
   else
     {
      int v = jt - i;
      g_gr[g].test++;
      int sz = ArraySize(g_gr[g].velas);
      ArrayResize(g_gr[g].velas, sz + 1, 5000);
      g_gr[g].velas[sz] = v;
      if(v <= 1)   g_gr[g].w1++;
      if(v <= 5)   g_gr[g].w5++;
      if(v <= 20)  g_gr[g].w20++;
      if(v <= 100) g_gr[g].w100++;
      sTest  = "1";
      sVelas = IntegerToString(v);
      sMin   = DoubleToString((double)(r[jt].time - (r[i].time + psec)) / 60.0, 0);   // desde el cierre de la vela

      //--- reacción medida en H1 a partir de la hora del test
      datetime t0 = r[jt].time, t1 = t0 + psec;
      int k = IndiceBase(t0);
      if(k < g_nbase && g_base[k].time < t1)
        {
         int kk = k;
         while(kk < g_nbase && g_base[kk].time < t1 &&
               !(abajo ? (g_base[kk].low <= p + g_tol) : (g_base[kk].high >= p - g_tol)))
            kk++;
         if(kk < g_nbase && g_base[kk].time < t1)
            k = kk;                                  // hora del toque
         int fin = k + InpVelasReaccion;
         if(fin < g_nbase)
           {
            double mx = g_base[k].high, mn = g_base[k].low;
            for(int q = k + 1; q <= fin; q++)
              {
               mx = MathMax(mx, g_base[q].high);
               mn = MathMin(mn, g_base[q].low);
              }
            double reb  = abajo ? mx - p : p - mn;              // a favor del rebote
            double pen  = MathMax(0.0, abajo ? p - mn : mx - p); // en contra (atraviesa el nivel)
            double dist = abajo ? g_base[fin].close - p : p - g_base[fin].close;
            g_gr[g].nReac++;
            g_gr[g].sumReb += reb;
            g_gr[g].sumPen += pen;
            if(dist > 0) g_gr[g].resp++;
            sReb  = DoubleToString(reb, _Digits);
            sPen  = DoubleToString(pen, _Digits);
            sResp = dist > 0 ? "1" : "0";
            if(k >= 24)
              {
               double s = 0;
               for(int q = k - 24; q < k; q++) s += g_base[q].high - g_base[q].low;
               double atr = s / 24.0;
               if(atr > 0)
                 {
                  g_gr[g].nAtr++;
                  g_gr[g].sumRebAtr += reb / atr;
                  g_gr[g].sumPenAtr += pen / atr;
                  sRebAtr = DoubleToString(reb / atr, 2);
                  sPenAtr = DoubleToString(pen / atr, 2);
                 }
              }
           }
        }
     }

   if(g_csv != INVALID_HANDLE)
      FileWrite(g_csv, g_tfNombre[tfi], NOMBRE_TIPO[tipo], TimeToString(r[i].time, TIME_DATE | TIME_MINUTES),
                DoubleToString(p, _Digits), sTest, sVelas, sMin, sReb, sPen, sResp, sRebAtr, sPenAtr);
  }

//+------------------------------------------------------------------+
void InformeGrupo(const int tfi, const int tipo)
  {
   int g = tfi * N_TIPOS + tipo;
   if(g_gr[g].n == 0)
     {
      Linea(StringFormat("  %s: sin casos", NOMBRE_TIPO[tipo]));
      return;
     }
   double n = g_gr[g].n, t = MathMax(g_gr[g].test, 1);
   int psec = PeriodSeconds(g_tf[tfi]);
   Linea(StringFormat("  %s: %d niveles · testeados %.1f%% · pendientes %d",
                      NOMBRE_TIPO[tipo], g_gr[g].n, 100.0 * g_gr[g].test / n, g_gr[g].n - g_gr[g].test));
   if(g_gr[g].test > 0)
     {
      double med = Percentil(g_gr[g].velas, 0.5), p25 = Percentil(g_gr[g].velas, 0.25), p75 = Percentil(g_gr[g].velas, 0.75);
      Linea(StringFormat("     Tiempo hasta el test: mediana %.0f velas (%s) · 25%%–75%%: %.0f–%.0f velas",
                         med, Duracion(med * psec), p25, p75));
      Linea(StringFormat("     De los testeados: en 1 vela %.1f%% · ≤5 %.1f%% · ≤20 %.1f%% · ≤100 %.1f%%",
                         100.0 * g_gr[g].w1 / t, 100.0 * g_gr[g].w5 / t, 100.0 * g_gr[g].w20 / t, 100.0 * g_gr[g].w100 / t));
     }
   if(g_gr[g].nReac > 0)
     {
      double nr = g_gr[g].nReac;
      string aviso = g_gr[g].nReac < 30 ? "  (pocos casos, poco fiable)" : "";
      string atr = g_gr[g].nAtr > 0 ? StringFormat(" · en ATR H1: rebote %.2f / penetración %.2f",
                                                   g_gr[g].sumRebAtr / g_gr[g].nAtr, g_gr[g].sumPenAtr / g_gr[g].nAtr) : "";
      Linea(StringFormat("     Reacción %d velas H1 tras el test (%d casos): respetado %.1f%% · rebote medio %s · penetración media %s%s%s",
                         InpVelasReaccion, g_gr[g].nReac, 100.0 * g_gr[g].resp / nr,
                         DoubleToString(g_gr[g].sumReb / nr, 2), DoubleToString(g_gr[g].sumPen / nr, 2), atr, aviso));
     }
   else if(g_gr[g].test > 0)
      Linea("     Reacción: sin datos H1 que cubran estos tests (aumenta «Velas H1»).");
  }

//--- combina dos grupos (verde+roja o control alcista+bajista) para la tabla de jerarquía
void Combinar(const int tfi, const int a, const int b, int &n, int &test, int &nr, int &resp,
              double &reb, double &pen, int &nAtr, double &rebAtr, double &penAtr, int &velas[])
  {
   int ga = tfi * N_TIPOS + a, gb = tfi * N_TIPOS + b;
   n    = g_gr[ga].n + g_gr[gb].n;
   test = g_gr[ga].test + g_gr[gb].test;
   nr   = g_gr[ga].nReac + g_gr[gb].nReac;
   resp = g_gr[ga].resp + g_gr[gb].resp;
   reb  = g_gr[ga].sumReb + g_gr[gb].sumReb;
   pen  = g_gr[ga].sumPen + g_gr[gb].sumPen;
   nAtr = g_gr[ga].nAtr + g_gr[gb].nAtr;
   rebAtr = g_gr[ga].sumRebAtr + g_gr[gb].sumRebAtr;
   penAtr = g_gr[ga].sumPenAtr + g_gr[gb].sumPenAtr;
   ArrayResize(velas, 0);
   ArrayCopy(velas, g_gr[ga].velas);
   ArrayCopy(velas, g_gr[gb].velas, ArraySize(velas));
  }

//+------------------------------------------------------------------+
void OnStart()
  {
   g_tol = (InpToleranciaPts + 0.5) * _Point;

   //--- temporalidades
   string partes[];
   int np = StringSplit(InpTemporalidades, ',', partes);
   for(int k = 0; k < np; k++)
     {
      ENUM_TIMEFRAMES tf;
      if(!TfDesdeTexto(partes[k], tf)) { Print("Temporalidad no reconocida: ", partes[k]); continue; }
      int m = ArraySize(g_tf);
      ArrayResize(g_tf, m + 1);
      ArrayResize(g_tfNombre, m + 1);
      g_tf[m] = tf;
      string nm = partes[k];
      StringTrimLeft(nm); StringTrimRight(nm); StringToUpper(nm);
      g_tfNombre[m] = nm;
     }
   int ntf = ArraySize(g_tf);
   if(ntf == 0) { Alert("No hay temporalidades válidas."); return; }
   ArrayResize(g_gr, ntf * N_TIPOS);

   //--- velas H1 para medir reacciones
   g_nbase = CopiarVelas(PERIOD_H1, InpBarrasBase, g_base);
   if(g_nbase <= 0) { Alert("No se pudo cargar el historial H1 de ", _Symbol); return; }

   string base = "OCE_EstadisticasH1_" + _Symbol;
   if(InpExportarCSV)
     {
      g_csv = FileOpen(base + ".csv", FILE_WRITE | FILE_CSV | FILE_ANSI, ';', CP_UTF8);
      if(g_csv != INVALID_HANDLE)
         FileWrite(g_csv, "TF", "Tipo", "Hora", "Nivel", "Testeado", "Velas hasta test", "Minutos hasta test",
                   "Rebote", "Penetracion", "Respetado", "Rebote ATR H1", "Penetracion ATR H1");
     }

   Linea(StringFormat("Estadísticas de niveles sin mecha (reacción en H1) · %s · %s", _Symbol, AccountInfoString(ACCOUNT_COMPANY)));
   Linea(StringFormat("Generado %s · tolerancia %d puntos · reacción medida en H1 durante %d velas (%d h)",
                      TimeToString(TimeCurrent(), TIME_DATE | TIME_MINUTES), InpToleranciaPts, InpVelasReaccion, InpVelasReaccion));
   Linea(StringFormat("Historial H1 disponible: %s → %s (%d velas)",
                      TimeToString(g_base[0].time, TIME_DATE), TimeToString(g_base[g_nbase - 1].time, TIME_DATE), g_nbase));
   Linea("Testeado = una vela posterior vuelve a tocar el nivel. Respetado = el cierre H1 al final de la ventana queda del lado del rebote.");
   Linea("Rebote = máximo recorrido a favor tras el test; penetración = cuánto atravesó el nivel (en precio y en ATR H1 de 24 velas).");
   Linea("");

   for(int tfi = 0; tfi < ntf && !IsStopped(); tfi++)
     {
      MqlRates r[];
      if(PeriodSeconds(g_tf[tfi]) < PeriodSeconds(PERIOD_H1))
        {
         Linea(StringFormat("=== %s: se omite (este script mide la reacción en H1; usa H1 o mayores) ===", g_tfNombre[tfi]));
         continue;
        }
      int n = (g_tf[tfi] == PERIOD_H1) ? 0 : CopiarVelas(g_tf[tfi], InpBarrasTF, r);
      if(g_tf[tfi] == PERIOD_H1)
        {
         int desde = MathMax(0, g_nbase - InpBarrasTF);
         n = ArrayCopy(r, g_base, 0, desde);
        }
      if(n <= 0) { Linea(StringFormat("=== %s: sin datos ===", g_tfNombre[tfi])); continue; }
      int pendDesde = ArraySize(g_pend);

      for(int i = 0; i < n && !IsStopped(); i++)
        {
         if(r[i].high - r[i].low <= g_tol)
            continue;
         bool aMin = MathAbs(r[i].open - r[i].low)  <= g_tol;
         bool aMax = MathAbs(r[i].open - r[i].high) <= g_tol;
         if(aMin) Analizar(tfi, T_AMIN, r, n, i, r[i].low,  true);
         if(aMax) Analizar(tfi, T_AMAX, r, n, i, r[i].high, false);
         if(InpGrupoControl && !aMin && !aMax)
           {
            if(r[i].close > r[i].open)      Analizar(tfi, T_CMIN, r, n, i, r[i].open, true);
            else if(r[i].close < r[i].open) Analizar(tfi, T_CMAX, r, n, i, r[i].open, false);
           }
        }

      Linea(StringFormat("=== %s · %d velas · %s → %s ===", g_tfNombre[tfi], n,
                         TimeToString(r[0].time, TIME_DATE), TimeToString(r[n - 1].time, TIME_DATE)));
      for(int tipo = 0; tipo < N_TIPOS; tipo++)
         if(tipo < 2 || InpGrupoControl)
            InformeGrupo(tfi, tipo);
      int np2 = ArraySize(g_pend) - pendDesde;
      if(np2 > 0)
        {
         Linea(StringFormat("  Niveles pendientes más recientes (%d en total):", np2));
         for(int k = MathMax(pendDesde, ArraySize(g_pend) - 5); k < ArraySize(g_pend); k++)
            Linea(g_pend[k]);
        }
      Linea("");
     }

   //--- tabla de jerarquía
   Linea("=== Jerarquía por temporalidad: niveles sin mecha (verde+roja) frente a control ===");
   Linea("TF    | Niveles | Testeados | Mediana test | Respetado | Rebote/Penetr. | Reb. ATR H1 || Control: Respetado | Rebote/Penetr.");
   for(int tfi = 0; tfi < ntf; tfi++)
     {
      int n, test, nr, resp, nAtr, cn, ctest, cnr, cresp, cnAtr;
      double reb, pen, rebAtr, penAtr, creb, cpen, crebAtr, cpenAtr;
      int velas[], cvelas[];
      Combinar(tfi, T_AMIN, T_AMAX, n, test, nr, resp, reb, pen, nAtr, rebAtr, penAtr, velas);
      Combinar(tfi, T_CMIN, T_CMAX, cn, ctest, cnr, cresp, creb, cpen, cnAtr, crebAtr, cpenAtr, cvelas);
      double med = Percentil(velas, 0.5);
      string sResp  = nr  > 0 ? StringFormat("%.1f%%", 100.0 * resp / nr) : "–";
      string sRat   = pen > 0 ? StringFormat("%.2f", reb / pen) : "–";
      string sAtr   = nAtr > 0 ? StringFormat("%.2f", rebAtr / nAtr) : "–";
      string scResp = cnr > 0 ? StringFormat("%.1f%%", 100.0 * cresp / cnr) : "–";
      string scRat  = cpen > 0 ? StringFormat("%.2f", creb / cpen) : "–";
      Linea(StringFormat("%-5s | %7d | %8.1f%% | %12s | %9s | %14s | %11s || %18s | %s",
                         g_tfNombre[tfi], n, n > 0 ? 100.0 * test / n : 0.0,
                         test > 0 ? Duracion(med * PeriodSeconds(g_tf[tfi])) : "–",
                         sResp, sRat, sAtr, InpGrupoControl ? scResp : "–", InpGrupoControl ? scRat : "–"));
     }
   Linea("Cómo leerla: si los niveles sin mecha de una temporalidad tienen un «Respetado» y un «Rebote/Penetr.»");
   Linea("claramente mayores que su control, y esa ventaja crece con la temporalidad, hay jerarquía.");
   Linea("Si las cifras son parecidas al control, el regreso al nivel es el comportamiento normal del precio.");

   if(g_csv != INVALID_HANDLE)
      FileClose(g_csv);
   int h = FileOpen(base + ".txt", FILE_WRITE | FILE_TXT | FILE_ANSI, 0, CP_UTF8);
   if(h != INVALID_HANDLE)
     {
      for(int k = 0; k < ArraySize(g_rep); k++)
         FileWriteString(h, g_rep[k] + "\r\n");
      FileClose(h);
     }
   Alert(StringFormat("Estadísticas listas. Archivos en MQL5\\Files: %s.txt%s", base, InpExportarCSV ? " y " + base + ".csv" : ""));
  }
//+------------------------------------------------------------------+
