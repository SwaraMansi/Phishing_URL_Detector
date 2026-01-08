## 🚀 Live Demo

🔗 **Deployed App:**  
https://phishingurldetector-nscpewvo5wobtcywj6dd8j.streamlit.app/

# Phishing URL Detection System (ML Project)
[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-red?logo=streamlit)](https://phishingurldetector-nscpewvo5wobtcywj6dd8j.streamlit.app/)


A machine learning system that classifies URLs as **phishing** or **legitimate** using lexical and statistical features.  
Trained using **Random Forest classifier** with 90%+ accuracy.

## Features

- Detects phishing URLs using ML
- Extracts URL-based lexical features
- Easy to train, test, and predict
- Beginner-friendly project
- Industry-level project for internships

## 📦 Deployment

This project is deployed using **Streamlit Cloud**.

- The trained machine learning model is loaded at runtime
- Feature extraction is performed on user-provided URLs
- The app predicts whether a URL is **Phishing** or **Legitimate**
- Deployed directly from GitHub with CI-based auto redeployment

🔗 Live URL: https://phishingurldetector-nscpewvo5wobtcywj6dd8j.streamlit.app/
### 1. Install requirements
pip install -r requirements.txt

### 2. Train model
python src/train_model.py

### 3. Predict URL
python src/predict.py

## Dataset
Used the Kaggle Phishing URL Dataset.

## Tech Stack
- Python
- Scikit-learn
- Pandas
- Feature Engineering
- Random Forest


