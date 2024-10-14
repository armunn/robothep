import streamlit as st
from generate import generate_mediation

# Set page config with title and blue circle emoji
st.set_page_config(page_title="Blue Dot 🔵", page_icon="🔵", layout="wide")

# Custom CSS to style the background, sidebar, and text colors
st.markdown(
    """
    <style>
    /* Dark midnight blue background for the main page */
    .stApp {
        background-color: #191970;
    }
    /* Pale blue sidebar */
    .css-1d391kg {
        background-color: #add8e6;
    }
    /* White text for the main page */
    .stApp {
        color: white;
    }
    /* Dark gray text for the sidebar */
    .css-1d391kg, .css-1lcbmhc {
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add title to the page
st.title("Blue Dot 🔵")

st.text("Welcome to Blue Dot, please make your selections below")


text_input = st.text_area("Please describe what you'd like to get out of the session today?")

option1 = st.selectbox("Which techniques would you like for relaxation?", ["Breath", "Body", "Mind"])

option2 = st.selectbox("What imagery would you like to use?", ["A forest", "The beach", "A mountain"])

option3 = st.selectbox("How would you like it to end?", ["Sunrise", "Tide", "Dawn chorus"])

if st.button("Generate"):
    progress = st.progress(0, "")
    mediation = generate_mediation(text_input, option1, option2, option3, progress)
    progress.progress(100, "Done!")
    audio_file = open(mediation, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mpeg")