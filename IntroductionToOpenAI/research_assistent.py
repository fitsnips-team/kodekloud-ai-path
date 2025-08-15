from openai import OpenAI
import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("mdsultanulislamovi/student-stress-monitoring-datasets")

print("Path to dataset files:", path)

client = OpenAI()

# read cvs file
df = pd.read_csv(f"{path}/StressLevelDataset.csv")

# create a function that reads a file and outputs
def analyze_data(df):
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [{"role":"user","content":f"You are a research assistant. Provide key insights only from demographics {df} in point form"}],
        max_tokens = 500,
        temperature = 0.2
    )

    return response.choices[0].message.content

print(analyze_data(df))