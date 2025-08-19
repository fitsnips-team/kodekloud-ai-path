"""Simple text translator using OpenAI's GPT model."""

from openai import OpenAI


client = OpenAI()

TEXT = (
    "Pues...En realidad, no es mucho difícil, no es como mis amigos dicen; "
    "dicen que español es taaaaaaaan difícil, son (o están?) equivocado. "
    "Si sigue en las clases (que no ellos hacen), la aprendizaje no es un problema."
)

# PROMPT
PROMPT = f"Translate the following: {TEXT}"


# function to translate
def article_translator(user_prompt):
    """Translate text using OpenAI's GPT model."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_prompt},
            {
                "role": "assistant",
                "content": "You are profession translator. You translate news articles into English",
            },
            {"role": "system", "content": "Direct english translator"},
        ],
        temperature=0.1,
    )
    return response.choices[0].message.content


print(article_translator(PROMPT))
