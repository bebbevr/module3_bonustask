import streamlit as st
import joblib  # Används för att ladda pkl-filer

# Ladda modellen
model = joblib.load("sentiment_model.pkl")

# Funktion för att göra sentimentanalys
def predict_sentiment(text):
    sentiment = model.predict([text])
    return "POSITIVE" if sentiment[0] == 1 else "NEGATIVE"

# Streamlit UI
st.title("Sentiment Analysis App")
st.write("Skriv in en text och få dess sentiment!")

# Textinput från användaren
user_input = st.text_area("Skriv din text här:")

# Knapp för analys
if st.button("Analysera sentiment"):
    if user_input:
        sentiment = predict_sentiment(user_input)
        st.write(f"**Resultat:** {sentiment}")
    else:
        st.warning("Vänligen skriv in en text för att analysera!")
