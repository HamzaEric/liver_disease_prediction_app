import streamlit as st
import numpy as np
import pickle

st.title("🩺 Liver Disease Prediction App")
st.markdown('---')
col1, col2 = st.columns(2)
with col1:
    st.image('AI.jpeg')
with col2:
    st.image('Machine Learning.jpeg')
st.markdown('---')
st.markdown("Fill in the details below to predict liver disease.")
# Load your trained model
model = pickle.load(open('rf_model.pkl', 'rb'))
# Input form
age = st.number_input("Age", min_value=1, max_value=100, value=45)
gender = st.selectbox("Gender", options=["Male", "Female"])
total_bilirubin = st.number_input("Total Bilirubin", value=1.0)
direct_bilirubin = st.number_input("Direct Bilirubin", value=0.5)
alk_phosphate = st.number_input("Alkaline Phosphotase", value=200.0)
alamine_aminotransferase = st.number_input("Alamine Aminotransferase", value=30.0)
aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", value=40.0)
total_proteins = st.number_input("Total Proteins", value=6.5)
albumin = st.number_input("Albumin", value=3.2)
ag_ratio = st.number_input("Albumin and Globulin Ratio", value=1.0)

# Transform gender to numeric
gender_val = 1 if gender == "Male" else 0

# Create feature array
features = np.array([[age, gender_val, total_bilirubin, direct_bilirubin,
                      alk_phosphate, alamine_aminotransferase,
                      aspartate_aminotransferase, total_proteins,
                      albumin, ag_ratio]])

# Predict
if st.button("Predict"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error("⚠️ The patient is likely to have liver disease.")
    else:
        st.success("✅ The patient is unlikely to have liver disease.")