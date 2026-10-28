//@version=5
strategy("Fabio Valentino Scalping Bot", overlay=true, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

// --- 1. ان پٹس اور سیٹنگز (Inputs & Settings) ---
i_useVolFilter   = input.bool(true, title="والیوم سپائک فلٹر استعمال کریں؟", group="Risk & Filters")
i_volumeMultiplier = input.float(1.5, title="والیوم ملٹی پلائر (اوسط سے کتگنا زیادہ)", group="Risk & Filters")
i_stopLossPips   = input.int(20, title="سٹاپ لاس (پوائنٹس/ٹیکس میں)", group="Risk & Filters")
i_takeProfitPips = input.int(35, title="टेक پرافٹ (ٹارگٹس)", group="Risk & Filters")

// --- 2. مارکیٹ پروفाइल اور ویلیو ایریا کا تخمینہ (Session / Volume Proxy) ---
// سکیلپنگ کے لیے ہم روزانہ کے ہائی/لو اور VWAP یا موونگ ایوریج بیسڈ بیلنس زون استعمال کریں گے
lookbackPeriod = input.int(20, title="بیلنس زون لوک بیک پیریڈ", group="Market Structure")
basis = ta.vwap(close)
dev = ta.stdev(close, lookbackPeriod)

// Value Area High (VAH) اور Value Area Low (VAL) کا تخمینہ
valAreaHigh = basis + (dev * 0.75)
valAreaLow  = basis - (dev * 0.75)

// --- 3. انیفیشینسی اور آؤٹ آف بیلنس سگنلز (Out of Balance / Inefficiency) ---
// جب قیمت ویلیو ایریا سے باہر نکلے (Out of Balance)
isBullishBreakout = close > valAreaHigh and close[1] <= valAreaHigh[1]
isBearishBreakout = close < valAreaLow and close[1] >= valAreaLow[1]

// والیوم کا فلٹر (فیبیو کا ایگریسووم سگنل)
volumeCondition = i_useVolFilter ? (volume > ta.sma(volume, 20) * i_volumeMultiplier) : true

// --- 4. انٹری کنڈیشنز (Entry Triggers) ---
longCondition  = isBullishBreakout and volumeCondition and strategy.position_size == 0
shortCondition = isBearishBreakout and volumeCondition and strategy.position_size == 0

// --- 5. ٹریڈ ایگزیکیوشن اور رسک مینجمنٹ (Execution & SL/TP) ---
var float longStopPrice = na
var float longTpPrice = na
var float shortStopPrice = na
var float shortTpPrice = na

if (longCondition)
    strategy.entry("Long Scalp", strategy.long)
    longStopPrice := close - (i_stopLossPips * symm_pip_value())
    longTpPrice   := close + (i_takeProfitPips * symm_pip_value())

if (shortCondition)
    strategy.entry("Short Scalp", strategy.short)
    shortStopPrice := close + (i_stopLossPips * symm_pip_value())
    shortTpPrice   := close - (i_takeProfitPips * symm_pip_value())

// سٹاپ لاس اور ٹیک پرافٹ لاگو کرنا
if (strategy.position_size > 0)
    strategy.exit("Exit Long", "Long Scalp", stop=longStopPrice, limit=longTpPrice)

if (strategy.position_size < 0)
    strategy.exit("Exit Short", "Short Scalp", stop=shortStopPrice, limit=shortTpPrice)

// کموڈیٹی یا فیوچرز کے حساب سے ٹک سائز ایڈجस्ट کرنے کا فنکشن
symm_pip_value() =>
    syminfo.mintick * 10

// --- 6. چارٹ پر لیولز کی پلاٹنگ (Plotting) ---
plot(valAreaHigh, title="Value Area High", color=color.blue, linewidth=2)
plot(valAreaLow, title="Value Area Low", color=color.orange, linewidth=2)
plot(basis, title="Fair Value / VWAP", color=color.gray, style=plot.style_line)
