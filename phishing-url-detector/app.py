import streamlit as st
import pickle
import pandas as pd
import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from extract_features import extract_features

# Load model safely
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "model",
    "phishing_model.pkl"
)

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Phishing URL Detector")

st.title("🔐 Phishing URL Detector")

url = st.text_input("Enter a URL")

if st.button("Check"):
    if url.strip() == "":
        st.warning("Please enter a URL")
    else:
        features = extract_features(url)
        prediction = model.predict(features)[0]

        if prediction == 1:
            st.error("⚠️ Phishing URL")
        else:
            st.success("✅ Legitimate URL")
