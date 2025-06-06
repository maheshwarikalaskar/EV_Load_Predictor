import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open('linear_regression_ev_model.pkl', 'rb'))

st.set_page_config(page_title="EV Load Predictor", page_icon="🔋")
st.title("🔋 EV Charging Station Load Prediction")

st.markdown("Enter the input values below. All fields accept numeric input only, as per your model training.")

# Input features (all numeric)
day_of_week = st.number_input('Day of Week (0=Mon, 6=Sun)', min_value=0, max_value=6, value=0)
hour = st.number_input('Hour of Day (0–23)', min_value=0, max_value=23, value=12)
weather = st.number_input('Weather Condition (Encoded)', min_value=0, max_value=3, value=0)
temperature_c = st.number_input('Temperature (°C)', value=30.0)
traffic_density = st.number_input('Traffic Density (Encoded)', min_value=0, max_value=2, value=1)
location_type = st.number_input('Location Type (Encoded)', min_value=0, max_value=2, value=0)
month = st.number_input('Month (1–12)', min_value=1, max_value=12, value=6)
is_weekend = st.number_input('Is Weekend (0 = No, 1 = Yes)', min_value=0, max_value=1, value=0)
perfect_time_load = st.number_input('Perfect Time Load', value=20.0)
temp_traffic = st.number_input('Temperature × Traffic', value=60.0)
hour_traffic = st.number_input('Hour × Traffic', value=24.0)
temp_weather = st.number_input('Temperature × Weather', value=30.0)
hour_weekend = st.number_input('Hour × Weekend', value=0.0)

# Create input DataFrame
input_data = pd.DataFrame([{
    'Day_of_Week': day_of_week,
    'Hour': hour,
    'Weather': weather,
    'Temperature_C': temperature_c,
    'Traffic_Density': traffic_density,
    'Location_Type': location_type,
    'Month': month,
    'Is_Weekend': is_weekend,
    'Perfect_Time_Load': perfect_time_load,
    'Temp_Traffic': temp_traffic,
    'Hour_Traffic': hour_traffic,
    'Temp_Weather': temp_weather,
    'Hour_Weekend': hour_weekend
}])

# Prediction
if st.button("⚡ Predict EV Load"):
    prediction = model.predict(input_data)
    st.success(f"🔋 Predicted EV Load: **{prediction[0]:.2f} kWh**")
