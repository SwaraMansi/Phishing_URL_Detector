import streamlit as st
import pickle
import re
import pandas as pd

# Load trained model
with open("model/phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Phishing URL Detector", layout="centered")

st.title("🔐 Phishing URL Detection System")
st.write("Enter a URL to check whether it is **Phishing** or **Legitimate**")

url = st.text_input("Enter URL")

def extract_features(url):
    features = {}
    features["url_length"] = len(url)
    features["has_https"] = 1 if "https" in url else 0
    features["has_at"] = 1 if "@" in url else 0
    features["has_hyphen"] = 1 if "-" in url else 0
    features["num_dots"] = url.count(".")
    return pd.DataFrame([features])

if st.button("Check URL"):
    if url.strip() == "":
        st.warning("Please enter a URL")
    else:
        features = extract_features(url)
        prediction = model.predict(features)[0]

        if prediction == 1:
            st.error("⚠️ Phishing URL Detected")
        else:
            st.success("✅ Legitimate URL")
