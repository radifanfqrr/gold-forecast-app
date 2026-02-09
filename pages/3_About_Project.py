import streamlit as st

st.set_page_config(page_title="About Project", page_icon="📘")

st.title("About This Project")

st.markdown("""
This application demonstrates a machine learning approach to forecasting short-term movements in gold prices.

The model predicts the **7-day future return** of the GLD Gold ETF using a combination of:

• Technical indicators (momentum, volatility, moving averages)  
• Macroeconomic variables (USD Index, bond yields, volatility index, oil prices)

The goal is not to produce trading signals, but to explore how market data and macro conditions can be used to build an explainable financial forecasting model.
""")

st.markdown("---")

st.subheader("Data Sources")

st.markdown("""
- **Gold Price:** GLD ETF historical data (Yahoo Finance)  
- **USD Index:** DX-Y.NYB  
- **US 10Y Yield:** ^TNX  
- **Volatility Index:** ^VIX  
- **Oil Prices:** CL=F Futures  
""")

st.markdown("---")

st.subheader("Model Overview")

st.markdown("""
- Algorithm: **XGBoost Regressor**  
- Target: **7-Day Forward Return**  
- Features: Technical + Macroeconomic  
- Training approach: Time-series split  
""")

st.markdown("---")

st.caption("Built as a portfolio project demonstrating applied machine learning in financial markets.")
