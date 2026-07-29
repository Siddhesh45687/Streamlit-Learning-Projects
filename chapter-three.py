import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://spicestationsilverlake.com/wp-content/uploads/2023/03/An-Introduction-to-Masala-Chai-Indias-Spiced-Tea.jpg",width=200)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://tse4.mm.bing.net/th/id/OIP.4ShP-E7UnctfBazuj49PxQHaE7?r=0&pid=Api&h=220&P=0",width=200)
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting Masala Chai")

elif vote2:
    st.success("Thanks for voting adrak Chai")

name = st.sidebar.text_input("Enter Your Name")
tea = st.sidebar.selectbox("Choose your Chai", ["Masala","Kesar","Adrak"])

st.write(f"Welcome {name} and your Chai is {tea} getting ready")

with st.expander("Show Chai Making Instructions"):
    st.write("""
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Serve hot
""")

st.markdown('### Welcome to Chai App')
st.markdown('> Blockquote')