# EV_Load_Predictor


# 🔋 EV Charging Load Predictor

This is a machine learning-powered web app that predicts the **EV Charging Station Load (in kWh)** based on input factors like time, weather, traffic, and more.

Built using **Streamlit**, it allows easy, real-time predictions through a simple web interface.

---

## 🚀 Features

- Predict EV load using a trained Linear Regression model
- Clean and responsive Streamlit interface
- Real-time input of parameters like hour, weather, temperature, etc.

---

## 🧪 Input Features

| Feature              | Description                            |
|----------------------|----------------------------------------|
| Day_of_Week          | Day index (0=Monday, 6=Sunday)         |
| Hour                 | Hour of the day (0–23)                 |
| Weather              | Encoded weather condition              |
| Temperature_C        | Temperature in Celsius                 |
| Traffic_Density      | Encoded traffic status                 |
| Location_Type        | Encoded type of station location       |
| Month                | Month index (1–12)                     |
| Is_Weekend           | 0 = Weekday, 1 = Weekend               |
| Perfect_Time_Load    | Historical ideal load                  |
| Temp_Traffic         | Feature interaction: Temp × Traffic    |
| Hour_Traffic         | Feature interaction: Hour × Traffic    |
| Temp_Weather         | Feature interaction: Temp × Weather    |
| Hour_Weekend         | Feature interaction: Hour × Weekend    |

---


pip install -r requirements.txt
streamlit run app.py
