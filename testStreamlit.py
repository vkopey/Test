import streamlit as st

# App title
st.title("Simple Streamlit App")

# Text input
user_input = st.text_input("Enter some text:")

# Button
if st.button("Submit"):
    # Text output
    st.write(f"You entered: {user_input}")
