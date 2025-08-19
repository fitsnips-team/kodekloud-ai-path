from openai import OpenAI
import os
from gtts import gTTS

client = OpenAI()

prompt = ("Tell me a story about super dog named Lexi")
OUTPUT_FILE="tts_example.mp3"


def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(OUTPUT_FILE)
    os.system(f"afplay {OUTPUT_FILE}")

def gen_text(prompt):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [{"role": "user","content":prompt}],
        max_tokens=100,
        temperature=0.5
    )

    return response.choices[0].message.content

def gen_and_spaeak(prompt):
    text=gen_text(prompt)
    print("Generated Text: \n",text)
    text_to_speech(text)


print(gen_and_spaeak(prompt))