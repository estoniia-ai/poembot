import os
import openai

# Get API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a chat completion request
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming."
        }
    ]
)

# Print the generated text
print(completion['choices'][0]['message']['content'])
