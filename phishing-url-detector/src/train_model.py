import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
from extract_features import extract_features

# Load dataset
df = pd.read_csv("../data/urls.csv")

# Feature extraction
features = df["url"].apply(lambda u: extract_features(u))
X = pd.DataFrame(list(features))
y = df["label"]   # label = 1 (phishing), 0 (legitimate)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate
print("Training Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))

# Save model
pickle.dump(model, open("../model/phishing_model.pkl", "wb"))
print("Model saved to model/phishing_model.pkl")
