//+------------------------------------------------------------------+
//|                                          CostosCuenta_v1.0.mq5   |
//| Mide los costos reales de operar en la cuenta conectada:         |
//| spread (actual y promedio en velas M1), comisión (sacada del     |
//| historial de operaciones) y swap por noche, por cada símbolo.    |
//| Escribe el resultado en Expertos y en MQL5/Files (CSV).          |
//+------------------------------------------------------------------+
#property copyright   "Marvin Cuestas"
#property version     "1.00"
#property script_show_inputs

input string InpSimbolos      = "";   // Símbolos separados por ; (vacío = los de Observación del mercado)
input int    InpDiasSpread    = 5;    // Días de velas M1 para el spread promedio
input int    InpDiasHistorial = 180;  // Días de historial para medir la comisión
input double InpLotes         = 1.0;  // Lotes para calcular el costo de una operación

// Valor en la moneda de la cuenta de 1 punto de precio para 1 lote.
double DineroPorPunto(const string s)
  {
   double valorTick  = SymbolInfoDouble(s, SYMBOL_TRADE_TICK_VALUE);
   double tamanoTick = SymbolInfoDouble(s, SYMBOL_TRADE_TICK_SIZE);
   double punto      = SymbolInfoDouble(s, SYMBOL_POINT);
   return tamanoTick > 0 ? valorTick * punto / tamanoTick : 0;
  }

// Spread promedio y máximo (en puntos) de las velas M1 de los últimos días.
void SpreadHistorico(const string s, int dias, double &promedio, int &maximo, int &velas)
  {
   promedio = 0;
   maximo   = 0;
   velas    = 0;
   MqlRates r[];
   int n = CopyRates(s, PERIOD_M1, TimeCurrent() - dias * 86400, TimeCurrent(), r);
   if(n <= 0)
      return;
   double suma = 0;
   for(int i = 0; i < n; i++)
     {
      suma += r[i].spread;
      if(r[i].spread > maximo)
         maximo = r[i].spread;
     }
   velas    = n;
   promedio = suma / n;
  }

// Comisión por lote y por lado, a partir de las operaciones del historial (negativo = costo).
void ComisionHistorial(const string s, double &porLoteLado, double &volumen, int &operaciones)
  {
   porLoteLado = 0;
   volumen     = 0;
   operaciones = 0;
   double suma = 0;
   for(int i = 0; i < HistoryDealsTotal(); i++)
     {
      ulong ticket = HistoryDealGetTicket(i);
      if(ticket == 0 || HistoryDealGetString(ticket, DEAL_SYMBOL) != s)
         continue;
      long tipo = HistoryDealGetInteger(ticket, DEAL_TYPE);
      if(tipo != DEAL_TYPE_BUY && tipo != DEAL_TYPE_SELL)
         continue;
      suma    += HistoryDealGetDouble(ticket, DEAL_COMMISSION) + HistoryDealGetDouble(ticket, DEAL_FEE);
      volumen += HistoryDealGetDouble(ticket, DEAL_VOLUME);
      operaciones++;
     }
   if(volumen > 0)
      porLoteLado = suma / volumen;
  }

// Swap de una noche para 1 lote, en la moneda de la cuenta cuando se puede calcular.
double SwapDinero(const string s, double swap, string &nota)
  {
   ENUM_SYMBOL_SWAP_MODE modo = (ENUM_SYMBOL_SWAP_MODE)SymbolInfoInteger(s, SYMBOL_SWAP_MODE);
   nota = "";
   switch(modo)
     {
      case SYMBOL_SWAP_MODE_DISABLED:
         nota = "sin swap";
         return 0;
      case SYMBOL_SWAP_MODE_POINTS:
         return swap * DineroPorPunto(s);
      case SYMBOL_SWAP_MODE_CURRENCY_DEPOSIT:
         return swap;
      case SYMBOL_SWAP_MODE_CURRENCY_SYMBOL:
         nota = "en " + SymbolInfoString(s, SYMBOL_CURRENCY_BASE);
         return swap;
      case SYMBOL_SWAP_MODE_CURRENCY_MARGIN:
         nota = "en " + SymbolInfoString(s, SYMBOL_CURRENCY_MARGIN);
         return swap;
      case SYMBOL_SWAP_MODE_INTEREST_CURRENT:
      case SYMBOL_SWAP_MODE_INTEREST_OPEN:
        {
         // Porcentaje anual: costo por día = precio * % / 100 / 360, pasado a dinero por lote.
         double precio = SymbolInfoDouble(s, SYMBOL_BID);
         double valorTick  = SymbolInfoDouble(s, SYMBOL_TRADE_TICK_VALUE);
         double tamanoTick = SymbolInfoDouble(s, SYMBOL_TRADE_TICK_SIZE);
         nota = "aprox., % anual";
         return tamanoTick > 0 ? precio * swap / 100.0 / 360.0 * valorTick / tamanoTick : 0;
        }
      default:
         nota = "modo " + EnumToString(modo) + ", valor sin convertir";
         return swap;
     }
  }

string Dinero(double valor)
  {
   return DoubleToString(valor, 2) + " " + AccountInfoString(ACCOUNT_CURRENCY);
  }

void OnStart()
  {
   // Lista de símbolos.
   string simbolos[];
   if(InpSimbolos == "")
     {
      int n = SymbolsTotal(true);
      ArrayResize(simbolos, n);
      for(int i = 0; i < n; i++)
         simbolos[i] = SymbolName(i, true);
     }
   else
     {
      StringSplit(InpSimbolos, ';', simbolos);
      for(int i = 0; i < ArraySize(simbolos); i++)
        {
         StringTrimLeft(simbolos[i]);
         StringTrimRight(simbolos[i]);
         SymbolSelect(simbolos[i], true);
        }
     }

   HistorySelect(TimeCurrent() - InpDiasHistorial * 86400, TimeCurrent());

   string archivo = "CostosCuenta_" + IntegerToString(AccountInfoInteger(ACCOUNT_LOGIN)) + ".csv";
   int csv = FileOpen(archivo, FILE_WRITE | FILE_CSV | FILE_ANSI, ';');
   if(csv != INVALID_HANDLE)
      FileWrite(csv, "Símbolo", "Spread ahora (pts)", "Spread prom. (pts)", "Spread máx. (pts)", "Spread prom. por lote",
                "Comisión ida y vuelta por lote", "Operaciones medidas", "Swap compra por noche", "Swap venta por noche",
                "Día del swap triple", "Costo de " + DoubleToString(InpLotes, 2) + " lotes (spread prom. + comisión)");

   PrintFormat("=== Costos de la cuenta %I64d (%s, %s) — spread de %d días, comisión de %d días ===",
               AccountInfoInteger(ACCOUNT_LOGIN), AccountInfoString(ACCOUNT_SERVER), AccountInfoString(ACCOUNT_COMPANY),
               InpDiasSpread, InpDiasHistorial);

   for(int i = 0; i < ArraySize(simbolos); i++)
     {
      string s = simbolos[i];
      if(s == "" || !SymbolInfoInteger(s, SYMBOL_SELECT))
        {
         PrintFormat("%s: no existe en este servidor", s);
         continue;
        }
      double porPunto = DineroPorPunto(s);
      long   spreadAhora = SymbolInfoInteger(s, SYMBOL_SPREAD);

      double spreadProm;
      int    spreadMax, velas;
      SpreadHistorico(s, InpDiasSpread, spreadProm, spreadMax, velas);

      double comLado, volumen;
      int    operaciones;
      ComisionHistorial(s, comLado, volumen, operaciones);
      double comIdaVuelta = comLado * 2; // negativo = costo

      string notaCompra, notaVenta;
      double swapCompra = SwapDinero(s, SymbolInfoDouble(s, SYMBOL_SWAP_LONG), notaCompra);
      double swapVenta  = SwapDinero(s, SymbolInfoDouble(s, SYMBOL_SWAP_SHORT), notaVenta);
      string diaTriple  = EnumToString((ENUM_DAY_OF_WEEK)SymbolInfoInteger(s, SYMBOL_SWAP_ROLLOVER3DAYS));

      double costoSpread = spreadProm * porPunto * InpLotes;
      double costoTotal  = costoSpread - comIdaVuelta * InpLotes;

      string textoCom = operaciones > 0
                        ? Dinero(-comIdaVuelta) + " por lote (" + IntegerToString(operaciones) + " operaciones)"
                        : "sin operaciones en el historial (abre y cierra 0.01 lotes para medirla)";
      PrintFormat("%s | spread ahora %I64d pts = %s/lote | prom. %d días %.1f pts = %s/lote, máx. %d pts | comisión ida y vuelta %s | swap compra %s%s, venta %s%s por noche/lote (triple: %s) | costo de %.2f lotes: %s",
                  s, spreadAhora, Dinero(spreadAhora * porPunto), InpDiasSpread, spreadProm, Dinero(spreadProm * porPunto), spreadMax,
                  textoCom, Dinero(swapCompra), notaCompra == "" ? "" : " (" + notaCompra + ")",
                  Dinero(swapVenta), notaVenta == "" ? "" : " (" + notaVenta + ")", diaTriple, InpLotes,
                  operaciones > 0 ? Dinero(costoTotal) : Dinero(costoSpread) + " + comisión sin medir");

      if(csv != INVALID_HANDLE)
         FileWrite(csv, s, spreadAhora, DoubleToString(spreadProm, 1), spreadMax, DoubleToString(spreadProm * porPunto, 2),
                   operaciones > 0 ? DoubleToString(-comIdaVuelta, 2) : "sin medir", operaciones,
                   DoubleToString(swapCompra, 2), DoubleToString(swapVenta, 2), diaTriple,
                   operaciones > 0 ? DoubleToString(costoTotal, 2) : DoubleToString(costoSpread, 2) + " + comisión");
     }

   if(csv != INVALID_HANDLE)
     {
      FileClose(csv);
      PrintFormat("CSV guardado en %s\\MQL5\\Files\\%s", TerminalInfoString(TERMINAL_DATA_PATH), archivo);
     }
  }
//+------------------------------------------------------------------+
