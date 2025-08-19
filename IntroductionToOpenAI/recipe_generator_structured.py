from openai import OpenAI
import os

client = OpenAI()

ingredients = []

while True:
    ingredient = input("Enter your ingredients. Type done once complete: ")
    if ingredient.lower() == "done":
        break

    ingredients.append(ingredient)


def recipe_gen(ingredients):
    messages = []

    for ingredient in ingredients:
        messages.append({"role": "user", "content": ingredient})

    messages.extend(
        [
            {"role": "system", "content": "JSON Format"},
            {
                "role": "assistant",
                "content": "You are a high end chef. Generate a recipe bases on the ingredients. Must be exported in JSON format",
            },
        ]
    )

    response = client.chat.completions.create(
        model="gpt-4o", messages=messages, max_tokens=300, temperature=0.9
    )
    return response.choices[0].message.content


print(recipe_gen(ingredients))
