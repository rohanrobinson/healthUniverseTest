import streamlit as st

st.title('Vascular Vigil CVD Risk Assessment')
st.header('Cardiovascular disease is bad. We help you not get.')

st.write('Please enter your blood panel information:')

total_cholesterol = st.number_input('Total Cholesterol (mg/dL)', min_value=100, max_value=400, value=200)
hdl_cholesterol = st.number_input('HDL Cholesterol (mg/dL)', min_value=20, max_value=100, value=50)
ldl_cholesterol = st.number_input('LDL Cholesterol (mg/dL)', min_value=50, max_value=200, value=100)
triglycerides = st.number_input('Triglycerides (mg/dL)', min_value=50, max_value=500, value=150)
blood_pressure = st.number_input('Blood Pressure (mm Hg)', min_value=80, max_value=200, value=120)

if st.button('Calculate Risk Score'):
    # This is a dummy risk score calculation and does not represent a real algorithm
    risk_score = (total_cholesterol / 200) + (hdl_cholesterol / 50) + (ldl_cholesterol / 100) + (triglycerides / 150) + (blood_pressure / 120)
    st.write('Your CVD Risk Score is:', risk_score)
