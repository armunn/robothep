import streamlit as st
from gather import get_messages, run_therapy_chat, add_chat_message, is_therapy_chat_complete, get_challenge, get_impact, get_summary
from generate_two import generate_mediation

# Set page config with title and blue circle emoji
st.set_page_config(page_title="Blue Dot 🔵", page_icon="🔵")

# Custom CSS to style the background, sidebar, and text colors
st.markdown(
    """
    <style>
    /* Dark midnight blue background for the main page */
    .stApp {
        background-color: #191970;
    }

    [data-testid="stHeader"] {
        background-color: #191970;
    }

    /* Pale blue sidebar */
    .css-1d391kg, button {
        background-color: #add8e6;
    }
    /* White text for the main page */
    .stApp {
        color: white;
    }

    h1, p {
        color: white;
    }

    [data-testid="stBaseButton-secondary"] {
        background-color: #add8e6;
    }
    
    /* Dark gray text for the sidebar */
    .css-1d391kg, .css-1lcbmhc, button {
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)
if "mode" not in st.session_state:
    st.session_state.mode = "chat"

# Add title to the page
st.title("Blue Dot 🔵")

if st.session_state.mode == "chat":
    messages = get_messages()[-1:]

    chat_widgets = list()

    for message in messages:
        if message["role"] != "system" and "ENDGATHERING" not in message["content"]:
            add_chat_message(message["role"], message["content"])
                
    if is_therapy_chat_complete():
        st.session_state.mode = "ready"
    elif prompt := st.chat_input("What do we want to do today?"):
        add_chat_message("user", prompt)
        add_chat_message("assistant", run_therapy_chat(prompt))

        if is_therapy_chat_complete():
            st.session_state.mode = "ready"
            st.rerun()

if st.session_state.mode == "ready":
    messages = get_messages()[-3:]

    chat_widgets = list()

    for message in messages:
        if message["role"] != "system":
            content = message["content"].replace("ENDGATHERING", "")
            add_chat_message(message["role"], content)

    if st.button("Create audio session"):
        st.session_state.mode = "generate"

if st.session_state.mode == "generate":
        progress = st.progress(0, "Starting to put together your session...")
        mediation = generate_mediation(get_challenge(), get_impact(), get_summary(), progress)
        progress.progress(100, "Done!")
        audio_file = open(mediation, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mpeg")


