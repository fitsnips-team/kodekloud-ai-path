from openai import OpenAI
import os

client = OpenAI()

prompt = "Who makes the best ice cream in the world?"

def prompt_engine(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        max_tokens = 100,
        temperature=.5,
        top_p=.5,
        stop=["\n"],
    )
    
    return response.choices[0].message.content

print(prompt_engine(prompt))