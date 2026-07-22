from asyncio import coroutines
import os
import re
from dotenv import load_dotenv
from groq import Groq
import time

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API_KEY)

MODEL="llama-3.3-70b-versatile"

# Tool
def get_product_price(product):
    product_clean = product.lower().strip()
    if product_clean == "iphone 17":
        return 120000
    elif product_clean == "iphone 15":
        return 50000
    else:
        return 0

def calculator(expression):
  try:
    return eval(expression)
  except:
    return "calc error!"


tools = {
  "get_product_price": get_product_price,
  "calculator": calculator
}


system_prompt = f"""
	# ROLE:
		You are a shopping assistant.
	# TASK:
		Your Job is to answer the user's query.
	You have access to these tools:
	get_product_price(product) -> returns the price of the product
	calculator(expression) -> returns the result of the expression

	IMPORTANT RULES:
		- Call tools exactly like these examples:
    Action: get_product_price('iphone 17')
    Action: calculator('1+1')
    
    - Never call tools like this:
    get_product_price(product = 'iphone 17')
    calculator(expression = '2 + 2')
		
  FOLLOW THESE RULES:
  1. Decide what you need to do next.
  2. Call only one tool at a time.
  3. After writing an action, STOP immediately.
  4. Never guess or invent a tool result.
  5. Wait until you receive an observation.
  6. Then decide your next action.
  7. When the task is complete, then give the final answer.

  FORMAT:
  Thought: What you need to do
  Action: tool_name(argument)
  
  When finished:
  Final answer: your final answer

  """

def run_agent(user_query):
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_query
        }
    ]

    for step in range(5):
      print("\n -------------------")
      print("STEP", step + 1)
      print("-----------------------")

      response = client.chat.completions.create(
          model=MODEL,
          messages=messages,
          temperature=0
      )
      response_content = response.choices[0].message.content
      print("Response:", response_content)
      
      # Agent has finished
      if "Final answer:" in response_content:
        break

      # Find the next action
      match = re.search(
        r"Action:\s*(\w+)\((.*?)\)",
        response_content
      )

      if match:

        tool_name = match.group(1)

        tool_input = match.group(2)

        tool_input = tool_input.strip()

        tool_input = tool_input.strip('"\'')

        # run the tool
        if tool_name in tools:
          tool = tools[tool_name]

          observation = tool(tool_input)
        
        else:
          # tool not found
          observation = f"Tool '{tool_name}' not found."

        print(f"Observation: {observation}")

        # Append observation to history (Add LLM response to memory)
        messages.append({
          "role": "assistant",
          "content": response_content
        })

        # Give tool result back to LLM (make tool result as memory)
        messages.append({
          "role": "user",
          "content": f"Observation: {str(observation)}"
        })

        time.sleep(5)
      
    # return response.choices[0].message.content

user_prompt = f"""
I have 150000 rupees. What is the price of Iphone 17? and how much money i have left?
"""
print(run_agent(user_prompt))