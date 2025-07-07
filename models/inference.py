""" 
inference.py

Predict asset failure using a pre-trained model and input features.
Supports command-line input or embedded sample data.

Author: Mohamed Elmansy
Updated: 2025
"""

import argparse
import pandas as pd
import numpy as np
from joblib import load

def load_assets(model_path, scaler_path):
    model = load(model_path)
    scaler = load(scaler_path)
    return model, scaler

def prepare_input(sample_dict, feature_order):
    df = pd.DataFrame([sample_dict])
    df_encoded = pd.get_dummies(df)
    for col in feature_order:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[feature_order]
    return df_encoded.values

def predict(model, scaler, X):
    X_scaled = scaler.transform(X)
    result = model.predict(X_scaled)[0]
    probability = model.predict_proba(X_scaled)[0][1]
    return result, probability

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="../models/rf_model.pkl", help="Trained model path")
    parser.add_argument("--scaler", default="../models/scaler.pkl", help="Scaler object path")
    args = parser.parse_args()

    # Define aligned feature input
    sample_input = {
        "Zone": "East",
        "Asset_Type": "Pump",
        "Age_Years": 10,
        "Run_Hours": 12000,
        "Vibration": 3.5,
        "Temperature": 85,
        "Pressure": 6.2
    }

    expected_features = [
        'Age_Years', 'Run_Hours', 'Vibration', 'Temperature', 'Pressure',
        'Zone_East', 'Zone_North', 'Zone_South', 'Zone_West',
        'Asset_Type_Sensor', 'Asset_Type_Valve'
    ]

    model, scaler = load_assets(args.model, args.scaler)
    X_input = prepare_input(sample_input, expected_features)
    prediction, prob = predict(model, scaler, X_input)

    status = "FAILURE ⚠️" if prediction == 1 else "NO FAILURE ✅"
    print(f"Prediction: {status}")
    print(f"Probability of Failure: {prob:.2%}")
