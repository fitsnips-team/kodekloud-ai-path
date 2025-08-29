from openai import OpenAI

client = OpenAI()

prompt = "A blue alien with six fingers on each hand, wearing a purple suit, playing a really alien instrument based on a guitar. Photo realistic, modern.  The room should have a subtle mushroom theme. Soft lighting."


def main() -> None:
    response = client.images.generate(
        prompt=prompt,
        model="dall-e-3",
        size="1024x1024",  # Supported values are: '1024x1024', '1024x1792', and '1792x1024'
    )

    print(response.data[0].url)


if __name__ == "__main__":
    main()
