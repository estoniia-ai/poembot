import openai
import os
import json

def call_openai_api(text_to_alternate):
    #Setup API KEY as a global env variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "API key not found"

    openai.api_key = api_key
    query = f"Provide 3 alternatives to '{text_to_alternate}'"
    response = openai.Completion.create(engine="text-davinci-003", prompt=query, max_tokens=100)

    return json.dumps(response['choices'][0]['text'])

if __name__ == "__main__":
    text_input = "Hello, world!"  # Replace this with any text you'd like to get alternatives for
    print(call_openai_api(text_input))