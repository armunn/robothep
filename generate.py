from openai import OpenAI
import io
from pydub import AudioSegment
import tempfile
import streamlit as st

RELAX_MAP = {
    "Breath": "a breathing exercise, focusing on an area of breath",
    "Body": "a body scan, focusing on each muscle group and encouraging to relax",
    "Mind": "a basic mindfulness exercise",
}

IMAGERY_MAP = {
    "A forest": "a forest, with trees and a river",
    "The beach": "a beach, with waves and wind",
    "A mountain": "a mountain, with snow and a view",
}

ENDING_MAP = {
    "Sunrise": "a sunrise, with the sun rising over the horizon",
    "Tide": "the tide, with the water coming in ready to start a new cycle",
    "Dawn chorus": "a dawn chorus, with birds singing with uplifting eneragy",
}

client = OpenAI()

def generate_mediation(outcome: str, relaxation: str, imagery: str, ending: str, progress: st._DeltaGenerator, script_display: st._DeltaGenerator):
    progress.text("Generating script...")
    script = generate_script(outcome, relaxation, imagery, ending)
    script_display.text(f"Received script:\n\n {script}")
    progress.text("Generating speech...")
    audio_segment = generate_speech(script)
    progress.text("Merging with background...")
    return merge_with_background(audio_segment, "background.mp3")

def generate_script(outcome: str, relaxation: str, imagery: str, ending: str):
    relaxation = RELAX_MAP[relaxation]
    imagery = IMAGERY_MAP[imagery]
    ending = ENDING_MAP[ending]

    response = client.chat.completions.create(
    model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an accomplished hypnotherapist. You are preparing a guided meditation for a client."},
            {"role": "user", "content": f"""Please could you produce me a script for a guided meditation used for hypnotherapy.

The script should start with {relaxation} to establish relaxation.

Once that is achieved, guided imagery should be used. Imagery should include {imagery}.

This should support an outcome (in the clients own words) of "{outcome}."

The ending should be focused around {ending} and a suggestion to smile.

Please do not include title or section headings.
"""}
        ]
    )
    return response.choices[0].message.content

def generate_speech(script: str):
    paragraphs = script.split("\n\n")  # Split script into paragraphs

    responses = []
    for paragraph in paragraphs:
        response = client.audio.speech.create(
            model="tts-1",
            speed=0.65,
            voice="nova",
            input=paragraph,
        )
        responses.append(response.content)

    # Concatenate the responses with 5 seconds of silence between each
    final_audio = AudioSegment.silent(duration=5000)
    for response in responses:
        audio_segment = AudioSegment.from_file(io.BytesIO(response), format="mp3") + 5
        final_audio += audio_segment + AudioSegment.silent(duration=5000)

    final_audio += AudioSegment.silent(duration=10000)

    return final_audio

def merge_with_background(audio_segment, background: str):
    background_segment = AudioSegment.from_file(background) - 10
    merged_segment = background_segment.overlay(audio_segment)
    merged_segment = merged_segment[:len(audio_segment)]

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_file:
        tmp_filename = tmp_file.name

    merged_segment.export(f"{tmp_filename}", format="mp3")
    return tmp_filename

    