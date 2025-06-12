# ⚡ EV Load Predictor

An end-to-end machine learning project that predicts the electric vehicle (EV) charging load based on multiple environmental and time-based factors. Built using Python, trained using Linear Regression, and deployed via Streamlit for interactive use.

🔗 **GitHub Repo**: [maheshwarikalaskar/EV_Load_Predictor](https://github.com/maheshwarikalaskar/EV_Load_Predictor)

---

## 🚀 Live Demo

👉 [Try it on Streamlit](https://your-streamlit-app-link) *(Add your deployed link here)*

---

## 🎯 Objective

To predict the electricity load demand for EV charging stations using historical and contextual features such as time of day, temperature, traffic, and weather — helping optimize load distribution and resource planning.

---

## 📂 Project Structure

```plaintext
EV_Load_Predictor/
├── app.py                          # Streamlit web app
├── ML_training_project.ipynb      # Model training notebook
├── linear_regression_ev_model.pkl # Trained Linear Regression model
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation


##🧠 Model Overview
Model: Linear Regression

Built using scikit-learn

Trained on a dataset with both original and engineered features

Saved using Python's pickle module for deployment

##🧪 Features Used for Prediction
Day of Week (0 = Monday, ..., 6 = Sunday)

Hour of Day

Weather Condition (Encoded)

Temperature (°C)

Traffic Density (Encoded)

Location Type (Encoded)

Month

Is Weekend (0 or 1)

Perfect Time Load

Temperature × Traffic

Hour × Traffic

Temperature × Weather

Hour × Weekend

These features are collected via numeric input fields in the Streamlit UI and passed as a DataFrame for prediction.

##📈 Model Performance
Metric	Score
R² Score	0.87
RMSE	~2.53 kWh

The model performs well for EV load forecasting under standard conditions using simple regression techniques.

##📊 Streamlit App Features
📥 User inputs 13 numeric features related to date/time, weather, and traffic

⚡ “Predict” button triggers the trained model to estimate EV load

📋 Clean, real-time output in kWh

🧠 Backend: Trained .pkl model loaded via pickle

▶️ Run This Project Locally
bash
Copy
Edit
# 1. Clone the repository
git clone https://github.com/maheshwarikalaskar/EV_Load_Predictor.git
cd EV_Load_Predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
🖼️ Screenshots
(Place images in a screenshots/ folder and link them here)

🔹 Home Page

🔹 Input Form

🔹 Prediction Output

🔮 Future Enhancements
Use advanced models like XGBoost or LSTM

Fetch real-time traffic/weather data from APIs

Visualize prediction intervals and error metrics

Include feature importance with SHAP

Dockerize for robust deployment

👤 Author
Maheshwari Kalaskar
🎓 B.Tech in Artificial Intelligence, Final Year
📍 Nagpur, India
📧 maheshwarikalaskar@gmail.com
🔗 GitHub • LinkedIn • Portfolio



