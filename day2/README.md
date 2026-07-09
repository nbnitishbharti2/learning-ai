# Day 2 Learnings

In this day, I learned about message roles and temperature while interacting with the LLM.

## Why roles are needed
Roles help the model understand who is saying what in a conversation. They make the chat feel more structured, just like a human conversation with different speakers.

Without roles, the model may not know whether the input is an instruction, a question, or a previous reply. Roles help the model respond in the correct way.

## The three message roles

### 1. System role
The `system` role gives the model instructions about its behavior.

Example:
```python
{
    "role": "system",
    "content": "You are a helpful and strict coding tutor."
}
```

Usage:
- Set personality
- Give rules
- Define tone or style
- Guide the model before user questions

### 2. User role
The `user` role contains the actual request or question from the person chatting with the model.

Example:
```python
{
    "role": "user",
    "content": "Explain Python loops in simple words."
}
```

Usage:
- Ask questions
- Give instructions
- Provide input for the model to answer

### 3. Assistant role
The `assistant` role represents the previous reply from the model.

Example:
```python
{
    "role": "assistant",
    "content": "Python loops repeat a block of code multiple times."
}
```

Usage:
- Keep conversation history
- Help the model remember what was already said
- Make multi-turn chats more natural

## Example of all three roles together
```python
messages = [
    {
        "role": "system",
        "content": "You are a friendly teacher."
    },
    {
        "role": "user",
        "content": "What is a loop?"
    },
    {
        "role": "assistant",
        "content": "A loop repeats actions multiple times."
    },
    {
        "role": "user",
        "content": "Give me one example."
    }
]
```

## What is temperature?
Temperature controls how creative or random the model’s response should be.

- Low temperature = more focused and predictable
- High temperature = more creative and diverse

### Simple idea
- `temperature = 0.2` → safe, clear, factual
- `temperature = 2` → more imaginative, less predictable

## Creativity example
Prompt:
```python
"Write a short line about rain"
```

### With temperature 0.2
The model will likely give a simple and clear answer like:
```text
Rain falls softly from the sky.
```

### With temperature 2
The model may give a more creative and unusual answer like:
```text
The sky opens its silver curtain and whispers music to the earth.
```

## Difference between temperature 0.2 and 2

### Temperature 0.2
- Very focused
- More likely to repeat common patterns
- Better for factual answers
- Good for coding, summaries, and instructions

Example:
```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Explain recursion in one sentence."}],
    temperature=0.2
)
```

Likely output:
```text
Recursion is when a function calls itself to solve a smaller part of the same problem.
```

### Temperature 2
- Much more creative
- More variety in wording
- Can be less precise
- Good for storytelling, poems, brainstorming, and creative writing

Example:
```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Explain recursion in one sentence."}],
    temperature=2
)
```

Likely output:
```text
Recursion is like a tiny mirror that keeps reflecting a smaller version of itself until the problem becomes simple enough to solve.
```

## Summary
- Roles help the model understand the structure of the conversation.
- `system` sets behavior, `user` asks, and `assistant` remembers previous replies.
- Temperature controls creativity.
- Lower temperature is better for accurate answers.
- Higher temperature is better for creative answers.

## Example files
- [system_temp.py](system_temp.py)
