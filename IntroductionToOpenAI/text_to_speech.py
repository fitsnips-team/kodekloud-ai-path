"""Text to speech using OpenAI's GPT model."""

import os
from openai import OpenAI
from gtts import gTTS

client = OpenAI()

PROMPT = "Tell me a story about super dog named Lexi"
OUTPUT_FILE = "tts_example.mp3"


def text_to_speech(text, lang="en"):
    """Convert text to speech and play the audio."""
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(OUTPUT_FILE)
    os.system(f"afplay {OUTPUT_FILE}")


def gen_text(user_prompt):
    """Generate text using OpenAI's GPT model."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_prompt}],
        max_tokens=100,
        temperature=0.5,
    )

    return response.choices[0].message.content


def gen_and_speak(prompt):
    """Generate text and convert it to speech."""
    text = gen_text(prompt)
    print("Generated Text: \n", text)
    text_to_speech(text)


print(gen_and_speak(PROMPT))
