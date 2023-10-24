import os
import openai

# Get API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_poem(slogan):
    # Create a chat completion request
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a poetic assistant, skilled in explaining complex and novel concepts with creative flair."
            },
            {
                "role": "user",
                "content": f"Compose a three-versed poem titled '{slogan}' that explains the concept from the title."
            }
        ]
    )
    
    # Get the generated text
    poem_text = completion['choices'][0]['message']['content']
    
    # Combine the title and the generated text into a complete poem
    poem = f"{slogan}\n\n{poem_text}"
    
    return poem

# Get the slogan / title from the user
slogan = input("Enter the slogan: ")

# Generate and print the poem
poem = generate_poem(slogan)
print(poem)
