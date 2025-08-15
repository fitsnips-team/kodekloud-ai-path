from openai import OpenAI


client = OpenAI()

text = "Pues...En realidad, no es mucho difícil, no es como mis amigos dicen; dicen que español es taaaaaaaan difícil, son (o están?) equivocado. Si sigue en las clases (que no ellos hacen), la aprendizaje no es un problema."

# prompt
prompt = f"Translate the following: {text}"

# function to translate
def article_translator(prompt):
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [{"role":"user", "content":prompt},
                    {"role":"assistant", "content":"You are profession translator. You translate news articles into English"},
                    {"role":"system","content":"Direct english translator"}],
        temperature=0.1          
    )
    return response.choices[0].message.content

print(article_translator(prompt))