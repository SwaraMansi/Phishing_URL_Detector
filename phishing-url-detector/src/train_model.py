import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import sys

# allow import from src
sys.path.append(os.path.dirname(__file__))
from extract_features import extract_features

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "urls.csv")
MODEL_DIR = os.path.join(BASE_DIR, "..", "model")

os.makedirs(MODEL_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

features = df["url"].apply(lambda u: extract_features(u))
X = pd.DataFrame(list(features))
y = df["label"]  # 1 = phishing, 0 = legitimate

with open(os.path.join(MODEL_DIR, "feature_columns.pkl"), "wb") as f:
    pickle.dump(X.columns.tolist(), f)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

print("Training Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))

with open(os.path.join(MODEL_DIR, "phishing_model.pkl"), "wb") as f:
    pickle.dump(model, f)

print("Model and feature columns saved successfully.")

