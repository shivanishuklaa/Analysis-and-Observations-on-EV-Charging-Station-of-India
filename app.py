import streamlit as st
import pickle
import pandas as pd
import numpy as np

def load_model():
    with open("best_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

# Load the trained model
model = load_model()

# Streamlit App
st.title("EV Charging Energy Consumption Prediction")
st.write("Enter the details to predict energy consumption")

# Input fields
city = st.selectbox("City", ["Bangalore", "Delhi", "Pune"])
charger_type = st.selectbox("Charger Type", ["Fast", "Slow"])
daily_users = st.number_input("Daily Users", min_value=1, max_value=500, step=1)
charging_duration = st.number_input("Charging Duration (mins)", min_value=1, max_value=180, step=1)
charging_price = st.number_input("Charging Price (INR/kWh)", min_value=1, max_value=50, step=1)
usage_hour = st.number_input("Usage Hour (24-hour format)", min_value=0, max_value=23, step=1)

# Prepare input data
def preprocess_input(city, charger_type, daily_users, charging_duration, charging_price, usage_hour):
    df = pd.DataFrame({
        "City": [city],
        "Charger_Type": [charger_type],
        "Daily_Users": [daily_users],
        "Charging_Duration(mins)": [charging_duration],
        "Charging_Price(INR/kWh)": [charging_price],
        "Usage_Hour": [usage_hour]
    })
    return df

if st.button("Predict Energy Consumption"):
    input_data = preprocess_input(city, charger_type, daily_users, charging_duration, charging_price, usage_hour)
    prediction = model.predict(input_data)
    st.success(f"Predicted Energy Consumption: {prediction[0]:.2f} kWh")