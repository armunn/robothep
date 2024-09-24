import streamlit as st
from generate import generate_mediation

st.title("Auto Therapy")
st.text("Welcome to Auto Therapy, please make your selections below")


text_input = st.text_area("Please describe what you'd like to get out of the session today?")

option1 = st.selectbox("Which techniques would you like for relaxation?", ["Breath", "Body", "Mind"])

option2 = st.selectbox("What imagery would you like to use?", ["A forest", "The beach", "A mountain"])

option3 = st.selectbox("How would you like it to end?", ["Sunrise", "Tide", "Dawn chorus"])

progress = st.text("")

script = st.text("")

if st.button("Generate"):
    mediation = generate_mediation(text_input, option1, option2, option3, progress, script)
    audio_file = open(mediation, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")