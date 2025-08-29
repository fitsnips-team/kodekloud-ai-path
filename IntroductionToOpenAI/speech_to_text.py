"""Speech to text using OpenAI's GPT model."""

from openai import OpenAI

client = OpenAI()

AUDIO_FILE = "./tts_example.mp3"

with open(AUDIO_FILE, "rb") as audio_file:
    transcribe = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    print(transcribe.text)
