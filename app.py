import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("diabetes.pkl", "rb") as f:
    model = pickle.load(f)

# Title
st.title("🩺 Diabetes Prediction App")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose", min_value=0, step=1)
blood_pressure = st.number_input("Blood Pressure", min_value=0, step=1)
skin_thickness = st.number_input("Skin Thickness", min_value=0, step=1)
insulin = st.number_input("Insulin", min_value=0, step=1)
bmi = st.number_input("BMI", min_value=0.0, format="%.2f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
age = st.number_input("Age", min_value=1, step=1)

# Prediction button
if st.button("Predict"):
    # Combine inputs into a 2D array
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])

    # Predict
    prediction = model.predict(input_data)

    # Show result
    if prediction[0] == 1:
        st.error("Diabetes")
    else:
        st.success("No Diabetes")

