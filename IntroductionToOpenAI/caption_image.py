from openai import OpenAI

client = OpenAI()

image_url = "https://hips.hearstapps.com/ghk.h-cdn.co/assets/17/30/dachshund.jpg"


def generate_captions(image_url):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What is this image?"},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            }
        ],
    )

    return response.choices[0].message.content


print(generate_captions(image_url))
