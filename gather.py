from typing import Generator, Union, Generator

from openai import OpenAI
import streamlit as st
import re

client = OpenAI()

def get_messages():
    if st.session_state.get("messages") is None:
        st.session_state["messages"] = [{"role": "system", "content": """You are an accomplished hypnotherapist, you are working to prepare a client for a session.
                                         Please ask short directed questions in order to determine what is the area of therapy a client would like.
                                         Please try to gather examples and details to help guide the session. Try and find the area of challenge and the impact they would like to have.
                                         When you think you have enough details, or if the user asks to start a session, please reply with ENDGATHERING."""},
                                        {"role": "assistant", "content": "Welcome to Blue Dot 🔵, I'm glad you're here. What do we want to do today?"}]
        
    return st.session_state.get("messages")

def get_transcript():
    messages = get_messages()

    def get_role(role:str):
        return "Therapist" if role == "assistant" else "Patient"

    transcript = "".join([get_role(message["role"]) + ": " + message["content"] + "\n" for message in messages])

    return transcript

def get_challenge():
    transcript = get_transcript().replace("ENDGATHERING", "")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an accomplished hypnotherapist, you have just completed information gathering with the client. You are about to prepare a script for a hypnotherapy session. Before then you need to get some information together"},
            {"role": "user", "content": f"""Based off the the attached transcript, please extract the main challenge the patient is trying to overcome
             Transcript:
             {transcript}
             """}
        ]
    )
    return response.choices[0].message.content

def get_impact():
    transcript = get_transcript().replace("ENDGATHERING", "")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an accomplished hypnotherapist, you have just completed information gathering with the client. You are about to prepare a script for a hypnotherapy session. Before then you need to get some information together"},
            {"role": "user", "content": f"""Based off the the attached transcript, please extract the main impact and state of mind the patient would like by the end of the session
             Transcript:
             {transcript}
             """}
        ]
    )
    return response.choices[0].message.content

def get_summary():
    transcript = get_transcript().replace("ENDGATHERING", "")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an accomplished hypnotherapist, you have just completed information gathering with the client. You are about to prepare a script for a hypnotherapy session. Before then you need to get some information together"},
            {"role": "user", "content": f"""Based off the the attached transcript, please provide a basic summary of what the interaction
             Transcript:
             {transcript}
             """}
        ]
    )
    return response.choices[0].message.content


def is_therapy_chat_complete():
    messages = get_messages()
    return "ENDGATHERING" in messages[-1]["content"]

def run_therapy_chat(new_message: str) -> Generator[str, None, None]:
    messages = get_messages()

    messages.append({"role": "user", "content": new_message})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        stream=True
    )

    response_text = ""
    response_cache = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            response_text += content
            response_cache += content

            if "ENDGATHERING" in response_cache:
                response_cache = response_cache.replace("ENDGATHERING", "")

            space_idx = response_cache.find(" ")
            if space_idx != -1:
                word = response_cache[:space_idx]
                response_cache = response_cache[space_idx:]

                yield word

    yield response_cache

    messages.append({"role": "assistant", "content": response_text})


def get_chat_display_list():
    if st.session_state.get("chat_widgets") is None:
        st.session_state["chat_widgets"] = list()

    return st.session_state.get("chat_widgets")


def add_chat_message(role: str, content: Union[str, Generator[str, None, None]]):
    chat_widgets = get_chat_display_list()

    icon = "🔵" if role == "assistant" else "🧘"
    name = "Blue Dot" if role == "assistant" else "You"
    m = st.chat_message(name, avatar=icon)
    if isinstance(content, str):
        m.markdown(content)
    else:
        m.write_stream(content)

    chat_widgets.append(m)