from openai import OpenAI
import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("uom190346a/sleep-health-and-lifestyle-dataset")

print("Path to dataset files:", path)

client = OpenAI()

# bring in fitness data
df = pd.read_csv(f"{path}/Sleep_health_and_lifestyle_dataset.csv")

goals = []

while True:
    goal = input("What are your health goals, enter done when complete: ")
    if goal.lower() == "done":
        break

    goals.append(goal)

def trainer(goals, df):
    messages = []
    for goal in goals:
        messages.append({"role": "user", "content": goal})

    messages.extend([
       {"role": "system", "content": "Direct. Point form"},
       {"role": "assistant", "content": f"You are a health expert. The person you are responding to is a accountant. Be specific to the role. Be technical and specific and reference this data {df} in your response and provide solutions to the {goals}"} 
    ])

    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = messages,
        temperature = 0.9)

    return response.choices[0].message.content


print(trainer(goals,df))