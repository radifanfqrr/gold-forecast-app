import yfinance as yf
import pandas as pd
import ta

def get_latest_features():
    # =====================
    # DATA EMAS
    # =====================
    gold = yf.download("GLD", period="6mo")
    df = gold.copy()

    # Ratakan kolom jika MultiIndex
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0].lower() for col in df.columns]
    else:
        df.columns = [col.lower() for col in df.columns]

    # =====================
    # FITUR TEKNIKAL
    # =====================
    df["close_lag_1"] = df["close"].shift(1)
    df["close_lag_7"] = df["close"].shift(7)
    df["close_lag_14"] = df["close"].shift(14)

    df["return_1d"] = df["close"].pct_change(1)
    df["return_7d"] = df["close"].pct_change(7)

    df["ma_7"] = df["close"].rolling(7).mean()
    df["ma_14"] = df["close"].rolling(14).mean()
    df["ma_30"] = df["close"].rolling(30).mean()

    df["volatility_7"] = df["close"].rolling(7).std()
    df["volatility_30"] = df["close"].rolling(30).std()

    df["rsi_14"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()

    # =====================
    # DATA MAKRO
    # =====================
    usd = yf.download("DX-Y.NYB", period="6mo")["Close"]
    yield_10y = yf.download("^TNX", period="6mo")["Close"]
    vix = yf.download("^VIX", period="6mo")["Close"]
    oil = yf.download("CL=F", period="6mo")["Close"]

    macro = pd.concat([usd, yield_10y, vix, oil], axis=1)
    macro.columns = ["usd_index", "yield_10y", "vix", "oil_price"]

    df = df.join(macro, how="left")
    df = df.fillna(method="ffill")

    df = df.dropna()

    # Ambil baris terakhir saja (untuk prediksi hari ini)
    return df.iloc[-1:]
