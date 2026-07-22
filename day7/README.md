# Day 7 - ReAct (Reasoning and Acting) Agents

On Day 7, we learn about the **ReAct** (Reasoning and Acting) pattern. ReAct allows an LLM to alternate between reasoning (generating thoughts) and taking actions (executing tools) to solve complex, multi-step queries.

---

## What is ReAct?
Traditionally, when you ask an LLM a question, it generates the whole response in one go. If it needs external information or calculation, it might hallucinate or fail.

With **ReAct**, the LLM follows a structured cycle:
1. **Thought**: Reason about what is needed next.
2. **Action**: Call an external tool (e.g., database lookup, calculator).
3. **Observation**: Read the result returned by the tool.
4. **Repeat**: Use the observation to generate the next thought.
5. **Final Answer**: Return the final answer once all information is gathered.

---

## Core Components of a ReAct Agent

### 1. System Prompt
The system prompt teaches the LLM the structure it must follow:
- Which tools are available.
- The formatting template (`Thought: ...`, `Action: tool(arg)`, `Final Answer: ...`).
- Strict guidelines (e.g., only call one tool at a time, stop after an Action).

### 2. Tools
Python functions representing capabilities the LLM doesn't have natively. In our example, we define:
- `get_product_price(product)`: Looks up product prices.
- `calculator(expression)`: Performs math equations.

### 3. Execution Loop
The execution loop coordinates between the LLM and the tools:
- It sends the message history to the LLM.
- If the LLM requests an `Action`, it parses the tool name and input using a regular expression (`re`).
- It executes the matching python function.
- It appends the result as an `Observation` to the conversation history and calls the LLM again.

---

## Code Example

Here is a simplified overview of how the ReAct loop is constructed:

```python
import re
import time

# 1. Define tools
def get_product_price(product):
    # Case-insensitive comparison
    product_clean = product.lower().strip()
    if product_clean == "iphone 17":
        return 120000
    return 0

# 2. ReAct parser and loop
for step in range(5):
    # Get response from LLM
    response_content = get_llm_response(messages)
    
    if "Final answer:" in response_content:
        print("Done:", response_content)
        break

    # Parse next action: Action: tool_name('input')
    match = re.search(r"Action:\s*(\w+)\((.*?)\)", response_content)
    if match:
        tool_name = match.group(1)
        tool_input = match.group(2).strip("'\"")

        # Run the tool
        observation = execute_tool(tool_name, tool_input)

        # Append assistant response and tool observation to messages memory
        messages.append({"role": "assistant", "content": response_content})
        messages.append({"role": "user", "content": f"Observation: {observation}"})
```

---

## Files in this Folder
- [react_chain.py](file:///d:/PHP8.2/htdocs/learning/python-learning/Padho%20with%20Pratyush/day7/react_chain.py): Full implementation of a ReAct agent using the Groq API.

---

## Running the Example
1. Make sure dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the python script:
   ```bash
   python react_chain.py
   ```
