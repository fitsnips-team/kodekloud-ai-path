from openai import OpenAI
import os

RobotBestFriend = OpenAI()

prompt = "You are a nba basket ball expert. Who is better MJ or Lebron?"

def prompt_engine(prompt):
    response = RobotBestFriend.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        max_tokens = 250,
    )
    
    return response.choices[0].message.content

print(prompt_engine(prompt))