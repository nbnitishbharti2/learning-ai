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

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are my strict senior colleague"
        },
        {
            "role": "user",
            "content": "I love you"
        }
    ],
    # Set the temperature to 0.7 for more creative responses
    temperature=2
)

# Print the response from the model
print(response.choices[0].message.content)