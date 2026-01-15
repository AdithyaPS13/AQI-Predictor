import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Set Page Configuration
st.set_page_config(page_title="AQI Prediction", layout="centered")

# --- Load the Model ---
@st.cache_resource
def load_model():
    # Ensure this matches the filename you used in joblib.dump()
    return joblib.load('xgb_aqi_model.pkl')

model = load_model()

# --- Mapping Dictionary ---
# Based on the LabelEncoder logic in your notebook
aqi_mapping = {
    0: "Good",
    1: "Moderate",
    2: "Poor",
    3: "Satisfactory",
    4: "Severe",
    5: "Very Poor",
    6: "Unknown"
}

# --- App UI ---
st.title("🌬️ Air Quality Index (AQI) Prediction")
st.write("Enter the pollutant values to predict the AQI category.")

# Features used in your notebook training
feature_cols = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'AQI']

# Create input fields for each feature
input_dict = {}
cols = st.columns(2) 

for i, col_name in enumerate(feature_cols):
    with cols[i % 2]:
        # Default value 0.0, similar to your median imputation logic
        input_dict[col_name] = st.number_input(f"Enter {col_name}", min_value=0.0, step=0.1)

# --- Prediction Logic ---
if st.button("Predict AQI Bucket"):
    # Convert input into the same format as your training data
    input_df = pd.DataFrame([input_dict])
    
    # Perform prediction
    prediction_code = model.predict(input_df)[0]
    prediction_label = aqi_mapping.get(prediction_code, "Unknown")
    
    # Display Result
    st.divider()
    st.subheader(f"Prediction Result:")
    st.success(f"The predicted AQI Category is: **{prediction_label}**")