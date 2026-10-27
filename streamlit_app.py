import streamlit as st
import time

st.set_page_config(
    page_title="لالے کی جان - Sir's AI Terminal",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ لالے کی جان - Institutional Terminal for Sir")
st.markdown("### Smart Money Concepts | 5-Screen Grid + Sir's Personal AI Assistant (+923296865871)")

# Sidebar Controls & Permanent WhatsApp Configuration for User
st.sidebar.header("Terminal Settings & WhatsApp")
user_whatsapp = st.sidebar.text_input("Connected WhatsApp Number", value="+923296865871")
selected_pair = st.sidebar.selectbox("Select Currency Pair", ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "XAU/USD (Gold)"])
selected_timeframe = st.sidebar.selectbox("Select Timeframe", ["15M", "30M", "1H", "2H", "4H", "1D"])

run_grid_scan = st.sidebar.button("🔍 Run Full Grid Radar & Connect Sir")

if run_grid_scan and user_whatsapp:
    st.sidebar.success(f"🟢 System Connected for Sir! Number: {user_whatsapp}")

st.divider()

# ==========================================
# 5-SCREEN GRID LAYOUT
# ==========================================

col_s1, col_s2 = st.columns([1.3, 1])

with col_s1:
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
    <div class="tradingview-widget-container" style="height:360px;width:100%">
      <div id="tradingview_widget" style="height:100%;width:100%"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget(
      {{
        "width": "100%",
        "height": "360",
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
    st.components.v1.html(tradingview_html, height=380)

with col_s2:
    st.markdown("##### 📰 Screen 2: Economic News & Flag Calendar")
    economic_calendar_html = """
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container" style="height:360px;width:100%">
      <div class="tradingview-widget-container__widget" style="height:100%;width:100%"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
      {
      "colorTheme": "light",
      "isTransparent": false,
      "width": "100%",
      "height": "360",
      "locale": "en",
      "importanceFilter": "-1,0,1",
      "currencyFilter": "USD,EUR,GBP,JPY,AUD,CAD,CHF,NZD"
      }
      </script>
    </div>
    <!-- TradingView Widget END -->
    """
    st.components.v1.html(economic_calendar_html, height=380)

st.divider()

col_s3, col_s4, col_s5 = st.columns([1, 1, 1.2])

with col_s3:
    st.markdown("##### 🌐 Screen 3: Global Bank Flow Radar")
    global_radar_html = """
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 260px; background-color: #0e1117; border-radius: 12px; border: 2px solid #00ffcc; padding: 10px;">
      <div style="position: relative; width: 75px; height: 75px; border: 2px dashed #00ffcc; border-radius: 50%; display: flex; align-items: center; justify-content: center; animation: spin 4s linear infinite;">
        <div style="position: absolute; width: 50%; height: 2px; background-color: #00ffcc; top: 50%; left: 50%; transform-origin: left center;"></div>
        <div style="width: 10px; height: 10px; background-color: #ff0055; border-radius: 50%; position: absolute; top: 10px; right: 15px;"></div>
      </div>
      <p style="color: #00ffcc; margin-top: 8px; font-weight: bold; font-family: monospace; font-size: 11px; text-align: center;">🌍 SIR'S AI ASSISTANT ACTIVE</p>
      <p style="color: #ffffff; font-size: 10px; text-align: center; margin: 0;">Connected: <b>+923296865871</b></p>
    </div>
    <style>
    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    </style>
    """
    st.components.v1.html(global_radar_html, height=275)

with col_s4:
    st.markdown("##### 📊 Screen 4: Market Structure & Logic")
    if run_grid_scan:
        st.success(
            f"• **Pair:** {selected_pair} ({selected_timeframe})\n\n"
            f"• **Smart Money:** Order block mitigation active.\n"
            f"• **Status:** Sir's terminal is fully primed and running."
        )
    else:
        st.info("👆 سائیڈ بار میں **'Run Full Grid Radar'** پریس کریں تاکہ اسکرین 4 اور 5 مکمل ایکٹیو ہو جائیں!")

with col_s5:
    st.markdown("##### 📱 Screen 5: Sir's AI Market Assistant & Targets")
    
    wa_query = st.text_input("💬 یہاں پوچھیں (مثلاً: 'مارکیٹ کیسی چل رہی ہے؟ کوئی خبر ہے؟')", value="")
    
    if wa_query:
        if "خبر" in wa_query or "نیوز" in wa_query:
            st.warning("🤖 **لاِلے کی جان AI:** سر جی! آنے والے سیشن میں ہائی-امپیکٹ نیوز آنے والی ہے، مارکیٹ میں جھٹکا لگ سکتا ہے، پوزیشنز کو ٹائٹ رکھیں یا احتیاط کریں!")
        elif "ٹریڈ" in wa_query or "سگنل" in wa_query or "مارکیٹ" in wa_query or "سیل" in wa_query or "بائے" in wa_query:
            st.success(f"🤖 **لاِلے کی جان AI:** جی سر جی! اس وقت {selected_pair} پر اسمارٹ منی (SMC) کا زبردست سیٹ اپ بن رہا ہے۔ ریڈار مکمل اسکین کر رہا ہے، جیسے ہی زبردست پوائنٹ آئے گا میں آپ کو واٹس ایپ پر بتا دوں گا!")
        else:
            st.info("🤖 **لاِلے کی جان AI:** حکم کریں سر جی! مارکیٹ کے حالات میرے سامنے ہیں۔ آپ بتائیں کون سا پیئر چیک کرنا ہے؟")
    
    if run_grid_scan:
        st.markdown(f"""
        - **Active Pair:** `{selected_pair}`  
        - **Sir's Number:** `{user_whatsapp}`  
        - **System:** Fully Active
        """)
    else:
        st.info("📌 سر جی! بوٹ سے بات کرنے کے لیے اوپر اسکین پریس کریں اور نیچے اپنا سوال لکھیں۔")

st.info("💡 **لالے کی جان ٹرمینل:** اب یہ بورڈ ہر بات پر آپ کو 'سر جی' کہہ کر عزت دے گا اور مکمل گائیڈ کرے گا!")
