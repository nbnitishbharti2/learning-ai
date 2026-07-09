import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API_KEY)

prompts = [
    # Prompt one
    {
        "role": "user",
        "content": "Hi"
    },
    # Promot two
    {
        "role": "user",
        "content": "Explain time travel in simple terms"
    },
    # Promot three
    {
        "role": "user",
        "content": "Write a 1000 words essay on Machine Learning"
    }
]

for prompt in prompts:
    print(prompt)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[prompt],
        # Set the temperature to 0.7 for more creative responses
        temperature=2,
        # Limit the token usage to 100 tokens
        max_tokens=100
    )

    # Print the response from the model
    print(response.choices[0].message.content)
    usage = response.usage
    print(f"Prompt Tokens: {usage.prompt_tokens}, Completion Tokens: {usage.completion_tokens}, Total Tokens: {usage.total_tokens}")
    print(f"Finish reason: {response.choices[0].finish_reason}")