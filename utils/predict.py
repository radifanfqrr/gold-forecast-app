import joblib

def load_model():
    model = joblib.load("models/xgb_return_model.pkl")
    features = joblib.load("models/model_features.pkl")
    return model, features

def predict_return(input_df):
    model, features = load_model()
    X = input_df[features]
    return model.predict(X)[0]
