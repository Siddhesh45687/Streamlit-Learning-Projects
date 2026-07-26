import streamlit as st
from datetime import date

st.title("Age Calculator")
dob = st.date_input("Select Your Date By Age",min_value=date(1999,1,1),max_value=date.today())




today = date.today()

age = today.year - dob.year

if (today.month , today.day) < (dob.month , dob.day):
    age -=1

st.success(f"Your Current Age is {age}")

st.write("### Details")
st.write(f"Date of Birth: **{dob.strftime('%d %B %Y')}**")
st.write(f"Your Age: **{today.strftime('%d %B %Y')}**")

