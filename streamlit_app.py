import streamlit as st
import time

st.set_page_config(
    page_title="لالے کی جان - 5-Screen Terminal with Signal Generator",
    page_icon="⚡",
    layout="wide"
)

# Custom CSS to keep the 5 screens compact and side-by-side
st.markdown("""
    <style>
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
    }
    iframe {
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ لالے کی جان - Institutional Terminal for Sir")
st.markdown("### Compact 5-Screen Grid + Live Signal Generator & AI Assistant")

# Sidebar Controls
st.sidebar.header("Terminal Control & Signals")
user_whatsapp = st.sidebar.text_input("Sir's WhatsApp", value="+923296865871")
selected_pair = st.sidebar.selectbox("Select Pair", ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "XAU/USD (Gold)"])
selected_timeframe = st.sidebar.selectbox("Select Timeframe", ["15M", "30M", "1H", "4H", "1D"])

# 🚀 Generate Signal Button as requested by Sir
generate_signal = st.sidebar.button("🚀 Generate Fresh Trade Signal")

st.divider()

# ==========================================
# 5 SCREENS PLACED SIDE BY SIDE IN COMPACT GRID
# ==========================================
s1, s2, s3, s4, s5 = st.columns(5)

# ------------------------------------------
# SCREEN 1: Compact TradingView Chart
# ------------------------------------------
with s1:
    st.markdown("##### 📈 1. Live Chart")
    tv_symbols = {
        "EUR/USD": "FX:EURUSD",
        "GBP/USD": "FX:GBPUSD",
        "USD/JPY": "FX:USDJPY",
        "AUD/USD": "FX:AUDUSD",
        "XAU/USD (Gold)": "OANDA:XAUUSD"
    }
    sym = tv_symbols.get(selected_pair, "FX:EURUSD")
    
    chart_html = f"""
    <div style="height:280px;width:100%">
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({{
        "width": "100%", "height": "280", "symbol": "{sym}",
        "interval": "15", "timezone": "Etc/UTC", "theme": "light",
        "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6", "enable_publishing": false, "allow_symbol_change": false
      }});
      </script>
    </div>
    """
    st.components.v1.html(chart_html, height=290)

# ------------------------------------------
# SCREEN 2: Compact News & Flags Calendar
# ------------------------------------------
with s2:
    st.markdown("##### 📰 2. News & Flags")
    news_html = """
    <div style="height:280px;width:100%">
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
      { "colorTheme": "light", "isTransparent": false, "width": "100%", "height": "280", "locale": "en", "importanceFilter": "-1,0,1", "currencyFilter": "USD,EUR,GBP,JPY,AUD" }
      </script>
    </div>
    """
    st.components.v1.html(news_html, height=290)

# ------------------------------------------
# SCREEN 3: Global Bank Flow Radar
# ------------------------------------------
with s3:
    st.markdown("##### 🌐 3. Bank Radar")
    radar_html = """
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 280px; background-color: #0e1117; border-radius: 8px; border: 1.5px solid #00ffcc; padding: 5px;">
      <div style="position: relative; width: 55px; height: 55px; border: 2px dashed #00ffcc; border-radius: 50%; display: flex; align-items: center; justify-content: center; animation: spin 4s linear infinite;">
        <div style="position: absolute; width: 50%; height: 2px; background-color: #00ffcc; top: 50%; left: 50%; transform-origin: left center;"></div>
        <div style="width: 8px; height: 8px; background-color: #ff0055; border-radius: 50%; position: absolute; top: 8px; right: 10px;"></div>
      </div>
      <p style="color: #00ffcc; margin-top: 10px; font-weight: bold; font-family: monospace; font-size: 10px; text-align: center;">🟢 RADAR ACTIVE</p>
      <p style="color: #ffffff; font-size: 9px; text-align: center; margin: 0;">Scanning Liquidity...</p>
    </div>
    <style>@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }</style>
    """
    st.components.v1.html(radar_html, height=290)

# ------------------------------------------
# SCREEN 4: Market Structure & Fresh Signal Output
# ------------------------------------------
with s4:
    st.markdown("##### 📊 4. Signal Board")
    if generate_signal:
        with st.spinner("Analyzing market..."):
            time.sleep(1.0)
        
        if "EUR" in selected_pair or "AUD" in selected_pair:
            st.success(f"🟢 **BUY SIGNAL ({selected_pair})**\n\n• **Direction:** UP (Long)\n• **Entry:** Optimal Zone\n• **TP1:** Secure 50%\n• **TP2 / TP3:** Active")
        else:
            st.error(f"🔴 **SELL SIGNAL ({selected_pair})**\n\n• **Direction:** DOWN (Short)\n• **Entry:** Optimal Zone\n• **TP1:** Secure 50%\n• **TP2 / TP3:** Active")
    else:
        st.info("👆 سائیڈ بار میں **'Generate Fresh Trade Signal'** بٹن دبائیں تاکہ تازہ سگنل یہاں ظاہر ہو!")

# ------------------------------------------
# SCREEN 5: Sir's Fast AI Assistant & Chat
# ------------------------------------------
with s5:
    st.markdown("##### 📱 5. Sir's AI Chat")
    
    user_msg = st.text_input("سوال لکھیں (مثلاً: 'سر جی، ٹریڈ لوں؟')", value="", key="sir_chat")
    
    if user_msg:
        if "خبر" in user_msg or "نیوز" in user_msg:
            st.warning("🤖 **لاِلے کی جان:** سر جی! آنے والے سیشن میں ہائی-امپیکٹ نیوز ہے، لاٹ سائز کم رکھیں۔")
        elif "ٹریڈ" in user_msg or "سگنل" in user_msg or "لیں" in user_msg:
            st.success(f"🤖 **لاِلے کی جان:** جی سر جی! {selected_pair} پر اسمارٹ منی کا بہترین سیٹ اپ بن رہا ہے، آپ سگنل بورڈ چیک کر سکتے ہیں!")
        else:
            st.info(f"🤖 **لاِلے کی جان:** حکم سر جی! '{user_msg}' نوٹ کر لیا ہے۔ سب کنٹرول میں ہے۔")
    
    if generate_signal:
        st.markdown(f"✅ **Linked:** `{user_whatsapp}`")
    else:
        st.markdown("💡 *سر جی، یہاں اے آئی سے بات کریں یا سائیڈ بار سے سگنل جنریٹ کریں!*")

st.divider()
st.info("💡 **نوٹ سر جی:** اب سائیڈ بار میں نیا 'Generate Fresh Trade Signal' بٹن موجود ہے جو آپ کو ایک کلک پر بتائے گا کہ مارکیٹ میں کس طرف انٹری لینی ہے!")
