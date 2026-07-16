import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
import json

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API_KEY)

class Ticket(BaseModel):
    name:str
    email:str
    phone:str
    issue:str

schema = Ticket.model_json_schema()


response_format = {
    "type": "json_object"
}

system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema {schema}.
Return ONLY a valid JSON object that matches this schema.
Do not include any explanation, markdown, or extra text.
"""

system_message = {
    "role": "system",
    "content": system_prompt
}

customer_email = "Hello my name is John. I bought and Iphone from your store last month and it stopped working. My address is Delhi, India. My email is abc@gmail.com and my contact no is 82988"

prompts = [
    system_message,
    {
        "role": "user",
        "content": f"""
            This is a customer email. Please extract the personal information of the customer from this. {customer_email}
        """
    },
]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=prompts,
    response_format=response_format,
    temperature=0.1,
)

# Print the response from the model
print(f"          LLM Response:                ")
answer = response.choices[0].message.content
print(answer)

# converts to JSON file and read JSON
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
