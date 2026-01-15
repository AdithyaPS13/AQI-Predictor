import streamlit as st
import pandas as pd
import joblib

# Set Page Configuration
st.set_page_config(page_title="AQI Prediction App", page_icon="🌬️")
st.title("🌬️ Air Quality AQI Prediction App")
st.write("Enter pollutant levels to predict the AQI Category.")

# --- Load the Model ---
@st.cache_resource
def load_model():
    # Ensure 'xgb_aqi_model.pkl' is in the same folder on GitHub
    return joblib.load('xgb_aqi_model.pkl')

model = load_model()

# --- 1. THE FIXED FEATURE LIST ---
# Based on your notebook: Datetime, StationId, Xylene, and AQI were dropped.
# These 11 features must be in this EXACT order.
feature_cols = [
    'PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 
    'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene'
]

# --- 2. THE FIXED LABEL MAPPING ---
# This maps the numbers (0-6) back to the categories from your notebook
aqi_labels = {
    0: "Good",
    1: "Moderate",
    2: "Poor",
    3: "Satisfactory",
    4: "Severe",
    5: "Very Poor",
    6: "Unknown (nan)"
}

# --- UI Input Fields ---
st.write("### Input Pollutant Concentrations")
input_data = {}
cols = st.columns(2) # Two-column layout for better looks

for i, col in enumerate(feature_cols):
    with cols[i % 2]:
        # Defaults to the median-like values from your dataset
        input_data[col] = st.number_input(f"Enter {col}", value=0.0, step=0.1)

# --- Prediction Logic ---
if st.button("Predict AQI Category"):
    # Convert input to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Force the column order to match the training set exactly
    input_df = input_df[feature_cols]
    
    # Generate prediction
    prediction_num = model.predict(input_df)[0]
    result_text = aqi_labels.get(prediction_num, "Unknown")
    
    # Display Result
    st.divider()
    st.success(f"### Predicted AQI Category: **{result_text}**")
    st.info(f"Model Class Code: {prediction_num}")
