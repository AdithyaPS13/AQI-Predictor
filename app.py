import streamlit as st
import pandas as pd
import joblib

# Set Page Title
st.set_page_config(page_title="AQI Predictor", page_icon="🌬️")
st.title("🌬️ Air Quality AQI Prediction App")

# 1. Load trained model
@st.cache_resource
def load_model():
    return joblib.load('xgb_aqi_model.pkl')

model = load_model()

# 2. Correct Feature List (Must match your Notebook training exactly)
feature_cols = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'AQI']

# 3. UI Input Fields
st.write("### Enter Pollutant Levels")
input_data = {}
cols = st.columns(2)
for i, col in enumerate(feature_cols):
    with cols[i % 2]:
        input_data[col] = st.number_input(f"{col}", value=0.0, step=0.1)

# 4. Label Mapping
aqi_labels = {0: "Good", 1: "Moderate", 2: "Poor", 3: "Satisfactory", 4: "Severe", 5: "Very Poor"}

# 5. Prediction Logic
if st.button("Predict AQI Category"):
    input_df = pd.DataFrame([input_data])
    input_df = input_df[feature_cols] # Ensures correct column order
    
    prediction = model.predict(input_df)[0]
    result_text = aqi_labels.get(prediction, f"Category {prediction}")
    
    st.success(f"✅ Predicted AQI Category: **{result_text}**")
