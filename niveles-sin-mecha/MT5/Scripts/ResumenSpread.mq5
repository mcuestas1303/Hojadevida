//+------------------------------------------------------------------+
//|                                                ResumenSpread.mq5 |
//| Lee los ticks del símbolo del gráfico entre dos fechas y guarda  |
//| un resumen del spread (Ask − Bid) por día y por hora del         |
//| servidor. Meses de ticks quedan en un CSV de pocos cientos de KB.|
//|                                                                  |
//| Columnas (spread en puntos; en XAUUSD 1 punto = 0,01):           |
//|   Ticks, Media, P50, P75, P90, P99, Max  → por tick              |
//|   MediaTiempo, P50Tiempo, P90Tiempo       → ponderado por el     |
//|     tiempo que duró cada spread (lo que encontraría una orden    |
//|     enviada en un momento cualquiera de esa hora)                |
//|                                                                  |
//| Uso: arrastrar a un gráfico del activo. El archivo se guarda en  |
//| MQL5\Files\OCE_Spread_<activo>.csv                               |
//+------------------------------------------------------------------+
#property copyright "OpenCloseExtremos"
#property version   "1.00"
#property description "Resumen del spread por día y hora a partir de los ticks"
#property script_show_inputs

input datetime InpDesde = D'2026.01.01 00:00';   // Desde (hora del servidor)
input datetime InpHasta = D'2026.10.06 00:00';   // Hasta (hora del servidor)

#define NB       2001       // histograma de 0 a 2000 puntos; el último recoge lo mayor
#define DUR_MAX  60000      // un spread cuenta como máximo 60 s (huecos y cierres)

int    g_hist[24][NB];
double g_thist[24][NB];

//--- valor (en puntos) bajo el que queda la fracción q del total
int PercentilInt(const int h, const double q, const double total)
  {
   double acc = 0, obj = q * total;
   for(int b = 0; b < NB; b++)
     {
      acc += g_hist[h][b];
      if(acc >= obj) return(b);
     }
   return(NB - 1);
  }

int PercentilTiempo(const int h, const double q, const double total)
  {
   double acc = 0, obj = q * total;
   for(int b = 0; b < NB; b++)
     {
      acc += g_thist[h][b];
      if(acc >= obj) return(b);
     }
   return(NB - 1);
  }

//+------------------------------------------------------------------+
void OnStart()
  {
   if(InpHasta <= InpDesde) { Alert("La fecha «Hasta» debe ser posterior a «Desde»."); return; }

   string fn = "OCE_Spread_" + _Symbol + ".csv";
   int fh = FileOpen(fn, FILE_WRITE | FILE_CSV | FILE_ANSI, ';', CP_UTF8);
   if(fh == INVALID_HANDLE) { Alert("No se pudo crear ", fn); return; }
   FileWrite(fh, "Fecha", "DiaSemana", "Hora", "Ticks", "Media", "P50", "P75", "P90", "P99", "Max",
             "MediaTiempo", "P50Tiempo", "P90Tiempo", "SegundosCubiertos", "Punto");

   int    dias = 0, diasSinDatos = 0;
   long   ticksTotal = 0;
   string punto = DoubleToString(_Point, _Digits);

   for(datetime d = InpDesde; d < InpHasta && !IsStopped(); d += 86400)
     {
      MqlDateTime st;
      TimeToStruct(d, st);
      if(st.day_of_week == 0 || st.day_of_week == 6)   // sin sesión los fines de semana
         continue;

      Comment(StringFormat("ResumenSpread %s: leyendo %s (%d días, %I64d ticks)",
                           _Symbol, TimeToString(d, TIME_DATE), dias, ticksTotal));

      MqlTick t[];
      int n = -1;
      for(int intento = 0; intento < 5 && n <= 0; intento++)
        {
         n = CopyTicksRange(_Symbol, t, COPY_TICKS_INFO, (ulong)d * 1000, (ulong)(d + 86400) * 1000 - 1);
         if(n <= 0) Sleep(1000);       // da tiempo a que el servidor envíe el historial
        }
      if(n <= 0) { diasSinDatos++; continue; }

      ZeroMemory(g_hist);
      ZeroMemory(g_thist);
      double cnt[24], sum[24], mx[24], tsum[24], tdur[24];
      ArrayInitialize(cnt, 0); ArrayInitialize(sum, 0); ArrayInitialize(mx, 0);
      ArrayInitialize(tsum, 0); ArrayInitialize(tdur, 0);

      for(int i = 0; i < n; i++)
        {
         if(t[i].bid <= 0 || t[i].ask <= 0) continue;
         int sp = (int)MathRound((t[i].ask - t[i].bid) / _Point);
         if(sp < 0) continue;
         int b = MathMin(sp, NB - 1);
         int h = (int)((t[i].time % 86400) / 3600);
         cnt[h]++;
         sum[h] += sp;
         if(sp > mx[h]) mx[h] = sp;
         g_hist[h][b]++;
         double dur = (i < n - 1) ? (double)MathMin(t[i + 1].time_msc - t[i].time_msc, (long)DUR_MAX) : 0.0;
         if(dur < 0) dur = 0;
         g_thist[h][b] += dur;
         tsum[h] += sp * dur;
         tdur[h] += dur;
        }

      for(int h = 0; h < 24; h++)
        {
         if(cnt[h] == 0) continue;
         string mt = "", p50t = "", p90t = "";
         if(tdur[h] > 0)
           {
            mt   = DoubleToString(tsum[h] / tdur[h], 2);
            p50t = IntegerToString(PercentilTiempo(h, 0.50, tdur[h]));
            p90t = IntegerToString(PercentilTiempo(h, 0.90, tdur[h]));
           }
         FileWrite(fh, TimeToString(d, TIME_DATE), st.day_of_week, h, (long)cnt[h],
                   DoubleToString(sum[h] / cnt[h], 2),
                   PercentilInt(h, 0.50, cnt[h]), PercentilInt(h, 0.75, cnt[h]),
                   PercentilInt(h, 0.90, cnt[h]), PercentilInt(h, 0.99, cnt[h]),
                   (int)mx[h], mt, p50t, p90t, DoubleToString(tdur[h] / 1000.0, 0), punto);
        }
      dias++;
      ticksTotal += n;
     }

   FileClose(fh);
   Comment("");
   Alert(StringFormat("ResumenSpread listo: %d días con datos, %d sin datos, %I64d ticks. Archivo: MQL5\\Files\\%s",
                      dias, diasSinDatos, ticksTotal, fn));
  }
//+------------------------------------------------------------------+
