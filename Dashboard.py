import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state="expanded")


import joblib
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

from utils.features import get_latest_features
from utils.predict import predict_return


st.set_page_config(layout="wide")

st.markdown("""
<style>
/* Background utama */
.stApp {
    background-color: #0e1117;
}

/* Judul utama */
h1 {
    font-weight: 600;
    letter-spacing: -0.5px;
}

/* Subjudul */
h2, h3 {
    color: #d1d5db;
    font-weight: 500;
}

/* Metric label */
[data-testid="stMetricLabel"] {
    font-size: 14px;
    color: #9ca3af;
}

/* Metric value */
[data-testid="stMetricValue"] {
    font-size: 28px;
    font-weight: 600;
}

/* Divider spacing */
hr {
    margin-top: 30px;
    margin-bottom: 30px;
    border: none;
    height: 1px;
    background-color: #1f2937;
}
</style>
""", unsafe_allow_html=True)


st.markdown("## Gold Price Forecast")
st.caption("Short-term gold return forecasting using technical and macroeconomic indicators")
st.markdown("### 7-Day Gold Return Prediction")

latest_df = get_latest_features()
pred_return = predict_return(latest_df)

last_price = latest_df["close"].values[0]
pred_price = last_price * (1 + pred_return)

with st.container():
    col1, col2, col3 = st.columns(3)

    col1.metric("Last Gold Price", f"${last_price:.2f}")
    col2.metric("Predicted 7-Day Return", f"{pred_return*100:.2f}%")
    col3.metric("Predicted Price (7d)", f"${pred_price:.2f}")

st.markdown("---")
st.markdown("### Gold Price Trend — Last 12 Months")
st.caption("Daily closing price of GLD ETF")

# Ambil data harga 1 tahun terakhir
price_data = yf.download("GLD", period="1y")

# Jika kolom MultiIndex, ratakan
if isinstance(price_data.columns, pd.MultiIndex):
    price_data.columns = [col[0] for col in price_data.columns]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=price_data.index,
    y=price_data["Close"],
    mode='lines',
    name='GLD Price'
))

fig.update_layout(
    title="GLD Gold ETF Price - Last 1 Year",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("### Market Conditions")
st.caption("Latest macro indicators influencing gold prices")

usd = yf.download("DX-Y.NYB", period="5d")
vix = yf.download("^VIX", period="5d")
yield_10y = yf.download("^TNX", period="5d")
oil = yf.download("CL=F", period="5d")

usd_last = float(usd["Close"].iloc[-1])
vix_last = float(vix["Close"].iloc[-1])
yield_last = float(yield_10y["Close"].iloc[-1])
oil_last = float(oil["Close"].iloc[-1])

m1, m2, m3, m4 = st.columns(4)

m1.metric("💵 USD Index", f"{usd_last:.2f}")
m2.metric("📉 VIX (Volatility)", f"{vix_last:.2f}")
m3.metric("🏦 US 10Y Yield", f"{yield_last:.2f}%")
m4.metric("🛢 Oil Price", f"${oil_last:.2f}")

st.markdown("---")
st.caption("Data sourced from Yahoo Finance. Model predictions are for educational and research purposes only.")