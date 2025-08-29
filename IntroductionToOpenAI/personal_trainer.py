"""Personal Trainer Example with OpenAI"""

from openai import OpenAI
import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("uom190346a/sleep-health-and-lifestyle-dataset")

print("Path to dataset files:", path)

client = OpenAI()

# bring in fitness data
DATA_FILE = pd.read_csv(f"{path}/Sleep_health_and_lifestyle_dataset.csv")

goals = []

while True:
    goal = input("What are your health goals, enter done when complete: ")
    if goal.lower() == "done":
        break

    goals.append(goal)


def trainer(user_goals, data_file):
    "Have OpenAI analyze data and make suggestions"
    messages = []
    for user_goal in user_goals:
        messages.append({"role": "user", "content": user_goal})

    messages.extend(
        [
            {"role": "system", "content": "Direct. Point form"},
            {
                "role": "assistant",
                "content": f"You are a health expert. The person you are responding to is a accountant. "
                f"Be specific to the role. Be technical and specific and reference this data "
                f"{data_file} in your response and provide solutions to the {goals}",
            },
        ]
    )

    response = client.chat.completions.create(
        model="gpt-4o", messages=messages, temperature=0.9
    )

    return response.choices[0].message.content


print(trainer(goals, DATA_FILE))
