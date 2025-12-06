from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd

app = FastAPI()

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.get("/")
def home():
    return {"message": "Churn Prediction API is live"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])

    # scale / preprocess if needed
    df_scaled = scaler.transform(df)

    pred = model.predict(df_scaled)[0]
    prob = model.predict_proba(df_scaled)[0,1]

    return {
        "churn_prediction": int(pred),
        "churn_probability": float(prob)
    }
