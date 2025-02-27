import streamlit as st
import requests # HTTP requests

st.title("Sentiment Analysis App")
st.write("Write text and get sentiment analysis!!")

user_input = st.text_area("Write text:")

if st.button("Analyze sentiment"):
    if user_input:
        response = requests.post(
            "https://module3-assignment-part2-api.onrender.com/predict",
            json={"text": user_input},
        )
        if response.status_code == 200:
            sentiment = response.json().get("sentiment")
            st.write(f"**Result:** {sentiment}")