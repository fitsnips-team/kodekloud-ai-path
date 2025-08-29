"""Simple batch processing using OpenAI's GPT model."""

from openai import OpenAI

client = OpenAI()

prompts = [
    "Tell me story about Texas",
    "Why are the starts so bright in Texas",
    "What is the average summer temperature in Austin Texas",
    "Is California cooler then Texas?",
]


def process_prompt(user_prompt):
    """Process the prompt with OpenAI"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_prompt}],
        max_tokens=100,
        temperature=0.8,
    )

    return response.choices[0].message.content


results = []

for prompt in prompts:
    result = process_prompt(prompt)
    results.append(result)

for i, result in enumerate(results):
    print(f"Prompt {i+1}: {prompt}")
    print(f"Result {i+1}: {result}")
