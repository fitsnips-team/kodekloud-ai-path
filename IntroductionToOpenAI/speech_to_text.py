from openai import OpenAI
import os

client = OpenAI()

AUDIO_FILE = open("./tts_example.mp3", "rb")

transcribe = client.audio.transcriptions.create(model="whisper-1", file=AUDIO_FILE)

print(transcribe.text)
