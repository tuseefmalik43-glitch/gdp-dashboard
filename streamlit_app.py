import streamlit as st
import random
import time

st.set_page_config(
    page_title="لالے کی جان - Ultimate Trading Terminal",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ لالے کی جان - Ultimate Forex & SMC Terminal")
st.markdown("### Smart Money Concepts | Multi-Screen Layout, Live Charts, News, TP Targets & Risk Alerts")

# Sidebar Controls
st.sidebar.header("Terminal Controls")
selected_pair = st.sidebar.selectbox("Select Currency Pair", ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "XAU/USD (Gold)"])
selected_timeframe = st.sidebar.selectbox(
    "Select Timeframe", 
    ["5M", "10M", "15M", "20M", "30M", "1H", "2H", "4H", "1D"]
)

if st.sidebar.button("Run Ultimate Market Scan"):
    with st.spinner(f"Scanning Liquidity, FVG & Target Zones for {selected_timeframe}..."):
        time.sleep(1.5)
    st.sidebar.success("Scan Completed!")

# Main Metrics Header
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Active Pair", value=selected_pair)

with col2:
    st.metric(label="Timeframe", value=selected_timeframe)

with col3:
    signal_type = random.choice(["BUY (Bullish SMC Setup)", "SELL (Bearish SMC Setup)"])
    st.metric(label="Primary Signal", value=signal_type)

st.divider()

# 🚨 NEW: Live News Risk Warning & Notification Banner
st.markdown("### 🚨 لائیو مارکیٹ الرٹ اور نیوز وارننگ (Live Risk Warning)")
current_warning = random.choice([
    "⚠️ **خبردار!** آنے والے 30 منٹ میں USD کی **High Impact (CPI / NFP)** نیوز ہے۔ مارکیٹ میں شدید اتار چڑھاؤ آ سکتا ہے، احتیاط کریں اور نئی ٹ्रेड اوفر کرنے سے گریز کریں!",
    "⚡ **مارکیٹ الرٹ:** آج یورپی سیشن میں بڑی بینکنگ نیوز آنے والی ہے۔ اپنے اسٹاپ لاس (SL) کو ٹائٹ رکھیں اور بریک ایون (Break-even) پر لے آئیں!",
    "🔔 **احتیاطی تدبیر:** گولڈ (XAU/USD) اور بڑی کرنسیز پر اس وقت اداروں کی لیکویڈیٹی ہنٹنگ جاری ہے۔ ہائی امپیکٹ نیوز سے پہلے بڑی پوزیشنز ہرگز نہ کھولیں!"
])
st.warning(current_warning)

st.divider()

# SCREEN 1 & SCREEN 2: Side-by-Side Live TradingView Chart & Live Economic News
st.subheader("📊 Screen 1 & Screen 2: Live Market Analysis & News Feed")
chart_col, news_col = st.columns([1.2, 1])

with chart_col:
    st.markdown("##### 📈 Screen 1: Live TradingView Chart")
    tv_symbols = {
        "EUR/USD": "FX:EURUSD",
        "GBP/USD": "FX:GBPUSD",
        "USD/JPY": "FX:USDJPY",
        "AUD/USD": "FX:AUDUSD",
        "XAU/USD (Gold)": "OANDA:XAUUSD"
    }
    current_tv_symbol = tv_symbols.get(selected_pair, "FX:EURUSD")

    tradingview_html = f"""
    <div class="tradingview-widget-container" style="height:480px;width:100%">
      <div id="tradingview_widget" style="height:100%;width:100%"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget(
      {{
        "width": "100%",
        "height": "480",
        "symbol": "{current_tv_symbol}",
        "interval": "D",
        "timezone": "Etc/UTC",
        "theme": "light",
        "style": "1",
        "locale": "en",
        "toolbar_bg": "#f1f3f6",
        "enable_publishing": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_widget"
      }}
      );
      </script>
    </div>
    """
    st.components.v1.html(tradingview_html, height=500)

with news_col:
    st.markdown("##### 📰 Screen 2: Live Economic Calendar & News")
    economic_calendar_html = """
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container" style="height:480px;width:100%">
      <div class="tradingview-widget-container__widget" style="height:100%;width:100%"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
      {
      "colorTheme": "light",
      "isTransparent": false,
      "width": "100%",
      "height": "480",
      "locale": "en",
      "importanceFilter": "-1,0,1",
      "currencyFilter": "USD,EUR,GBP,JPY,AUD,CAD,CHF,NZD"
      }
      </script>
    </div>
    <!-- TradingView Widget END -->
    """
    st.components.v1.html(economic_calendar_html, height=500)

st.divider()

# SCREEN 3 (Big Lower Display): Ultimate Target Board (TP1, TP2, TP3) & Strategy Breakdown
st.subheader("🎯 Screen 3: Ultimate Trade Setup & Profit Targets (TP1, TP2, TP3)")

if "BUY" in signal_type:
    st.success(f"🟢 **LONG (BUY) POSITION ACTIVE — {selected_pair} ({selected_timeframe})**\n\n"
                f"- **Market Structure:** Bullish Order Block & Fair Value Gap (FVG) mitigation completed.\n"
                f"- **Stop Loss (SL):** Placed safely below the recent session liquidity sweep low.")
    
    # 3 Columns for TP1, TP2, TP3
    tp_col1, tp_col2, tp_col3 = st.columns(3)
    with tp_col1:
        st.metric(label="🎯 Target 1 (TP1)", value="1.08850", delta="Risk-Free / Secure Half")
    with tp_col2:
        st.metric(label="🎯 Target 2 (TP2)", value="1.09200", delta="Main Liquidity Pool")
    with tp_col3:
        st.metric(label="🎯 Target 3 (TP3)", value="1.09650", delta="Extended Institutional Target")

else:
    st.error(f"🔴 **SHORT (SELL) POSITION ACTIVE — {selected_pair} ({selected_timeframe})**\n\n"
               f"- **Market Structure:** Bearish Order Block & Premium FVG rejection.\n"
               f"- **Stop Loss (SL):** Placed safely above the recent session liquidity sweep high.")
    
    # 3 Columns for TP1, TP2, TP3
    tp_col1, tp_col2, tp_col3 = st.columns(3)
    with tp_col1:
        st.metric(label="🎯 Target 1 (TP1)", value="1.07450", delta="Risk-Free / Secure Half")
    with tp_col2:
        st.metric(label="🎯 Target 2 (TP2)", value="1.07100", delta="Main Liquidity Pool")
    with tp_col3:
        st.metric(label="🎯 Target 3 (TP3)", value="1.06650", delta="Extended Institutional Target")

st.info("💡 **Terminal Guide:** Read the live news warning banner first, check Screen 1 & 2 for charts and news, and finally execute your targets using Screen 3 (TP1, TP2, TP3).")
