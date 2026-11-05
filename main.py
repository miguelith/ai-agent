import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key == None:
        raise RuntimeError("No api key supplied.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    generate_content(client, messages)


def generate_content(client: OpenAI, messages: list[dict[str, str]]) -> None:

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    print("User prompt: " + messages[0]["content"])
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print("Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
