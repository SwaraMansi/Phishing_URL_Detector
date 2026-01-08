import streamlit as st
import pickle
import pandas as pd
import os
import sys

# ---------------------------------
# Path setup
# ---------------------------------
BASE_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(BASE_DIR, "src"))

from extract_features import extract_features

# ---------------------------------
# Load model
# ---------------------------------
MODEL_PATH = os.path.join(BASE_DIR, "model", "phishing_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ---------------------------------
# Streamlit UI
# ---------------------------------
st.set_page_config(page_title="Phishing URL Detector", layout="centered")
st.title("🔐 Phishing URL Detector")

url = st.text_input("Enter a URL")

# ---------------------------------
# Prediction
# ---------------------------------
if st.button("Check URL"):
    if url.strip() == "":
        st.warning("Please enter a URL")
    else:
        # extract features (dict)
        feature_dict = extract_features(url)

        # convert dict → DataFrame (THIS FIXES ERROR)
        features_df = pd.DataFrame([feature_dict])

        # predict
        prediction = model.predict(features_df)[0]

        if prediction == 1:
            st.error("⚠️ Phishing URL Detected")
        else:
            st.success("✅ Legitimate URL")

