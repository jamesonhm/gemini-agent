import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("gemini api key not found")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    generate_content(client, messages)

def generate_content(client: genai.Client, messages):
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages
    )
    if not response.usage_metadata:
        raise RuntimeError("no usage metadata returned")

    print("Prompt tokens: %d" % response.usage_metadata.prompt_token_count)
    print("Response tokens: %d" % response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
