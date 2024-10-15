from openai import OpenAI
import io
from pydub import AudioSegment
import tempfile
import streamlit as st
from concurrent.futures import ThreadPoolExecutor
from scripts import get_prompts

client = OpenAI()

def generate_mediation(challenge: str, impact: str, summary: str, progress: st._DeltaGenerator):
    progress.progress(0, "Generating script...")
    script = generate_script(challenge, impact, summary, progress)
    progress.progress(25, "Generating speech...")
    audio_segment = generate_speech(script, progress)
    progress.progress(75, "Merging with background...")
    return merge_with_background(audio_segment, "background.mp3")

def generate_section(prompt: str):
    response = client.chat.completions.create(
    model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an accomplished hypnotherapist. You are preparing a guided meditation for a client. Please provide a script for the following section:"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def generate_script(challenge: str, impact: str, summary: str, progress: st._DeltaGenerator):
    prompts = get_prompts(challenge, impact, summary)
    full_script = []

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(generate_section, prompt) for prompt in prompts]
        for future in futures:
            full_script.append(future.result() + "\nPAUSE\n")
            completed = ((len(full_script) / len(prompts)) / 4)
            progress.progress(completed, f"Generating script {len(full_script)}/{len(prompts)}...")

    return "".join(full_script)

def generate_speech(script: str, progress: st._DeltaGenerator):
    paragraphs = script.split("PAUSE")  # Split script into paragraphs

    responses = []
    def generate_audio(paragraph):
        response = client.audio.speech.create(
            model="tts-1",
            speed=0.65,
            voice="nova",
            input=paragraph,
        )
        return response.content

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(generate_audio, paragraph) for paragraph in paragraphs]
        for future in futures:
            responses.append(future.result())
            completed = ((len(responses) / len(paragraphs)) / 2) + 0.25
            progress.progress(completed, f"Generating speech {len(responses)}/{len(paragraphs)}...")


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

    