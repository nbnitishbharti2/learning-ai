import os
from dotenv import load_dotenv
from groq import Groq
import json

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API_KEY)

MODEL="llama-3.3-70b-versatile"

def llm_response(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

customer_email = f"""
	# ROLE:
		You are a support assistant as a mobile/laptop company.
	# TASK:
		Your Job is to only classify the customer issue in a category.
	#CONSTRAINT:
		You have the classify the issue in of the three categories namely billing, technical, and return.
	#OUTPUT FORMAT:
		Your answer should be one word only. The one word should be one of the categories given in constraint.
	#EXAMPLE:
		For instance if a user complain says he wants a refund then the category is return.
	#FALLBACK:
		If the issue is unrelated to any of the categories mentioned in the constraints , then the answer should be OTHER.
	This is a user complaint:
		My Laptop is not working
	Classify this.
"""

print(llm_response(customer_email))