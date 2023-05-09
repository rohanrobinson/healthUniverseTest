import streamlit as st
import pandas as pd

st.title("Welcome to BMI Calculator!")

st.write("Get your BMI Fast!")

height = st.text_input("Height in inches")

weight = st.text_input("Weight in pounds")

height_squared = int(height) * int(height)

constant_factor = 703


bmi =  int(weight)  / height_squared * constant_factor


st.write("Your BMI is ", bmi)




