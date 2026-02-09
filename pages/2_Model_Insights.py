import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Model Insights", page_icon="🧠")

st.title("🧠 Model Insights & Explainability")

st.markdown("""
This page explains how the machine learning model makes predictions for gold price movements.
""")

# Load feature list
features = joblib.load("models/model_features.pkl")

st.subheader("📊 Features Used by the Model")

st.write(f"The model uses **{len(features)} features** combining technical indicators and macroeconomic data.")

st.dataframe(pd.DataFrame(features, columns=["Feature Name"]))

st.markdown("---")

st.subheader("🧠 Model Type")

st.markdown("""
**Algorithm:** XGBoost Regressor  
**Target:** 7-Day Future Return  
**Prediction Type:** Regression  
""")

st.markdown("---")

st.subheader("📈 How to Interpret Predictions")

st.markdown("""
- A **positive prediction** means gold price is expected to rise in 7 days  
- A **negative prediction** means gold price is expected to fall  
- The magnitude shows expected percentage return  
""")
