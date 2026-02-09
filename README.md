# Gold Price Forecast Dashboard

This project explores how machine learning can be used to model short-term movements in gold prices.

The application predicts the **7-day forward return** of the GLD Gold ETF using a combination of technical indicators and macroeconomic market data. The goal is not to create trading signals, but to demonstrate how financial data can be used in an explainable forecasting framework.

## Live Application
You can view the interactive dashboard here:  
**(Add your Streamlit link once deployed)**

## What the App Does

The dashboard provides:

- Latest gold price (GLD ETF)
- Predicted 7-day return and projected price
- Historical gold price chart
- Current macroeconomic conditions (USD index, bond yields, VIX, oil)
- Explanation of model features and design

The focus is on combining **market context** with model output, rather than presenting raw predictions in isolation.

## Model Overview

- Model type: XGBoost Regressor  
- Prediction target: 7-day forward return  
- Feature groups:
  - Price momentum and trend indicators
  - Volatility measures
  - Macroeconomic variables (USD, yields, VIX, oil)

The model is trained using a time-series split to respect chronological order and avoid look-ahead bias.

## Data Sources

All data is sourced from Yahoo Finance using the `yfinance` Python library:

- GLD ETF (gold proxy)
- USD Index (DX-Y.NYB)
- US 10Y Yield (^TNX)
- VIX (^VIX)
- Crude Oil Futures (CL=F)

## Project Purpose

This project was built as a portfolio piece to demonstrate:

- Applied time-series machine learning
- Financial feature engineering
- Model explainability concepts
- Turning a model into an interactive web application

## Disclaimer

This project is for educational and research purposes only. It is not intended to provide financial or investment advice.
