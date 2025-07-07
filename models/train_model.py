""" 
train_model.py

Train a RandomForestClassifier to predict asset failure in utility operations.
Includes logging, flexible arguments, model evaluation and export.

Author: Mohamed Elmansy
Updated: 2025
"""

import argparse
import logging
import pandas as pd
import numpy as np
import os
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# === Logging Config ===
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')

# === Train Functionality ===
def load_data(path):
    logging.info(f"Loading data from {path}")
    return pd.read_csv(path)

def preprocess(df):
    df_encoded = pd.get_dummies(df.drop("Asset_ID", axis=1), drop_first=True)
    X = df_encoded.drop("Failure", axis=1)
    y = df_encoded["Failure"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, scaler, X.columns

def evaluate_model(y_test, y_pred, output_dir):
    logging.info("Evaluating model...")
    report = classification_report(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    with open(os.path.join(output_dir, "classification_report.txt"), "w") as f:
        f.write(report)

    plt.figure(figsize=(6, 4))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "confusion_matrix.png"))
    plt.close()

def save_objects(model, scaler, output_model, output_scaler):
    dump(model, output_model)
    dump(scaler, output_scaler)
    logging.info(f"Model saved to {output_model}")
    logging.info(f"Scaler saved to {output_scaler}")

def train_model(data_path, model_path, scaler_path, report_dir):
    df = load_data(data_path)
    X_scaled, y, scaler, _ = preprocess(df)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, stratify=y, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    evaluate_model(y_test, y_pred, report_dir)
    save_objects(model, scaler, model_path, scaler_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train AI model for predictive maintenance")
    parser.add_argument("--data", default="../data/sample_asset_data_full.csv", help="Path to training CSV")
    parser.add_argument("--model", default="../models/rf_model.pkl", help="Output model path")
    parser.add_argument("--scaler", default="../models/scaler.pkl", help="Output scaler path")
    parser.add_argument("--report", default="../reports", help="Output reports directory")
    args = parser.parse_args()

    os.makedirs(args.report, exist_ok=True)
    train_model(args.data, args.model, args.scaler, args.report)
