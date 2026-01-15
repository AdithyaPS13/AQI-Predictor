# AQI-Predictor
# 🌬️ Air Quality Index (AQI) Prediction App

This project uses Machine Learning to predict the **AQI Category** (e.g., Good, Moderate, Poor) based on atmospheric pollutant levels. It features a trained **XGBoost Classifier** and an interactive web interface built with **Streamlit**.

## 🚀 Live Demo
You can access the web application here: 
https://aqi-predictor-766qgtqvrdp6bw2tn6ghac.streamlit.app/

## 📊 Project Overview
Air pollution is a major concern for public health. This tool allows users to input specific pollutant measurements and instantly receive an AQI classification.

### Key Features:
- **Data Cleaning:** Handled missing values using median imputation.
- **EDA:** Visualized correlations between pollutants like PM2.5, PM10, and NOx.
- **Model:** Built and optimized an XGBoost Classifier for high-accuracy predictions.
- **Deployment:** User-friendly web app for real-time inference.

## 📂 File Structure
- `app.py`: The main script for the Streamlit web application.
- `xgb_aqi_model.pkl`: The saved XGBoost model file.
- `requirements.txt`: List of Python libraries required for the app.
- `AdithyaAQA Prediction.ipynb`: The full Jupyter Notebook containing EDA and model training.
- `README.md`: This project documentation.

## 🛠️ How to Run Locally
1. **Clone this repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   Navigate to the folder:

🧪 Pollutants Used for Prediction
The model accepts the following features:

Particulate Matter: PM2.5, PM10

Gases: NO, NO2, NOx, NH3, CO, SO2, O3

Chemicals: Benzene, Toluene, Xylene

👤 Author
Adithya    
