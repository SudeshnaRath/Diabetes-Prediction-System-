import streamlit as st
import numpy as np
import pickle 

# Load the model
@st.cache_resource  # Cache to avoid reloading the model repeatedly
def load_model():
    with open('model.sav', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# Function to make predictions
def predict(age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level, model):
    input_data = np.array([[age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level]])
    prediction = model.predict(input_data)
    return prediction

# Streamlit app starts here
def main():
    st.title("Health Prediction App")
    st.write("Provide the required details to get a prediction:")

    # Input fields
    age = st.number_input("Age (in years)", min_value=0, step=1, value=30)
    hypertension = st.selectbox("Do you have hypertension?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    heart_disease = st.selectbox("Do you have heart disease?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, step=0.1, value=25.0)
    hba1c_level = st.number_input("HbA1c Level", min_value=0.0, step=0.1, value=5.5)
    blood_glucose_level = st.number_input("Blood Glucose Level (mg/dL)", min_value=0.0, step=1.0, value=100.0)

    # Load model
    model = load_model()

    # Prediction button
    if st.button("Get Prediction"):
        result = predict(age, hypertension, heart_disease, bmi, hba1c_level, blood_glucose_level, model)
        st.success(f"The predicted outcome is: {result[0]}")

if __name__ == "__main__":
    main()
