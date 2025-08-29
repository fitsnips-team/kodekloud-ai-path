"Recipe from input ingredients"

from openai import OpenAI

client = OpenAI()

ingredients = []

while True:
    ingredient = input("Enter your ingredients. Type done once complete: ")
    if ingredient.lower() == "done":
        break

    ingredients.append(ingredient)


def recipe_gen(user_ingredients):
    "GPT generate recipe with ingredients mildly considered"
    messages = []

    for user_ingredient in user_ingredients:
        messages.append({"role": "user", "content": user_ingredient})

    messages.extend(
        [
            {"role": "system", "content": "direct, point"},
            {
                "role": "assistant",
                "content": "You are a high end chef."
                + "Generate a recipe based on the ingredients",
            },
        ]
    )

    response = client.chat.completions.create(
        model="gpt-4o", messages=messages, max_tokens=300, temperature=0.9
    )
    return response.choices[0].message.content


print(recipe_gen(ingredients))
