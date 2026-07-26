import streamlit as st

st.title('Programming with Siddhesh')
st.subheader('Acknowledge your Coding')
st.text('Welcome to Coding Field')
st.write('Choose your favourite programming language')

language = st.selectbox("Your Programming Languages:",["Python","Java","C++","C","Django"])

st.write(f"{language} is my favourite programming language")
st.success(f"{language} is booming field language")