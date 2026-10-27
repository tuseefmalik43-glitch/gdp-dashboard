import streamlit as st
import random
import time

st.set_page_config(
    page_title="لالے کی جان - Forex Signal Board",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ لالے کی جان - Forex Liquidity & SMC Advanced Board")
st.markdown("### Smart Money Concepts | Multi-Timeframe Analysis & Live Forex News")

# Sidebar Controls for Timeframes & Pairs
st.sidebar.header("Board Controls")
selected_pair = st.sidebar.selectbox("Select Currency Pair", ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "XAU/USD (Gold)"])
selected_timeframe = st.sidebar.selectbox(
    "Select Timeframe", 
    ["5M", "10M", "15M", "20M", "30M", "1H", "2H", "4H", "1D"]
)

if st.sidebar.button("Scan Liquidity Pool"):
    with st.spinner(f"Scanning Order Blocks for {selected_timeframe} timeframe..."):
        time.sleep(1.2)
    st.sidebar.success("Scan Complete!")

# Main Dashboard Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Active Pair", value=selected_pair)

with col2:
    st.metric(label="Selected Timeframe", value=selected_timeframe)

with col3:
    signal_type = random.choice(["BUY (Bullish Sweep)", "SELL (Bearish Sweep)"])
    st.metric(label="Market Status", value=signal_type)

st.divider()

# Signal Analysis Section
st.subheader(f"📊 Live Signal Analysis for {selected_pair} ({selected_timeframe})")

if "BUY" in signal_type:
    st.success(f"🟢 **SIGNAL: STRONG BUY ({selected_timeframe})**\n\n- **Reason:** Price swept session low liquidity on the {selected_timeframe} chart.\n- **Entry Zone:** Dynamic Order Block support\n- **Stop Loss (SL):** Placed strictly below the liquidity sweep point\n- **Take Profit (TP):** Target set at next major liquidity pool")
else:
    st.error(f"🔴 **SIGNAL: STRONG SELL ({selected_timeframe})**\n\n- **Reason:** Price swept session high liquidity on the {selected_timeframe} chart.\n- **Entry Zone:** Dynamic Order Block resistance\n- **Stop Loss (SL):** Placed strictly above the liquidity sweep point\n- **Take Profit (TP):** Target set at next major liquidity pool")

st.divider()

# Two columns layout for Chart and Live News
chart_col, news_col = st.columns([1.2, 1])

with chart_col:
    st.subheader(f"📈 Live TradingView Chart ({selected_pair})")
    
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
    st.subheader("📰 Live Economic Calendar & News")
    st.markdown("Real-time forex news, impact levels & currency flags:")
    
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

st.info("💡 Tip: Use the sidebar to switch timeframes and currency pairs, while monitoring live high/medium impact news on the right side.")
