import pickle
from extract_features import extract_features

# Load trained model
model = pickle.load(open("../model/phishing_model.pkl", "rb"))

# User input
url = input("Enter a URL to check: ")

# Extract features
features = extract_features(url)
feature_list = list(features.values())

# Predict
output = model.predict([feature_list])[0]

print("\nResult:")
print("⚠️ Phishing URL" if output == 1 else "✅ Legitimate URL")
