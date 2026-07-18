# Day 6 - Prompt Engineering and Structuring Prompts

Today we learned how to design structured prompts to make the model perform specific tasks (like classification) reliably and accurately.

## What is Prompt Engineering?
Prompt Engineering is the practice of structuring text inputs (prompts) for an LLM so that it understands the context and behaves exactly as expected. Instead of asking a simple question, we can provide specific components to guide the model.

## Core Parts of a Structured Prompt
A professional prompt template often contains:
- **ROLE**: Who the AI is pretending to be (e.g., support assistant).
- **TASK**: What the AI needs to do (e.g., classify an issue).
- **CONSTRAINTS**: Specific rules or limits (e.g., only output specific words, no extra text).
- **OUTPUT FORMAT**: The exact structure of the response (e.g., one word only).
- **EXAMPLES (Few-shot learning)**: Showing the model examples of correct output.
- **FALLBACK**: What to do if the input doesn't fit any categories.

## Example Code
Here is how we implement structured prompt template in Python:

```python
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Define our structured prompt template
customer_email = """
# ROLE:
    You are a support assistant for a laptop company.
# TASK:
    Your job is to classify the customer issue into a category.
# CONSTRAINTS:
    You must classify the issue into one of the three categories: billing, technical, and return.
# OUTPUT FORMAT:
    Your answer must be one word only (the category).
# EXAMPLE:
    If customer says: "I want a refund", output: return
# FALLBACK:
    If the issue doesn't match any category, output: OTHER

This is the customer issue:
    "My Laptop is not working"

Classify this:
"""

# Call the model
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": customer_email}]
)

print(response.choices[0].message.content) # Output: technical
```

## Running the Example
1. Make sure dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the python script:
   ```bash
   python prompt_eng.py
   ```
