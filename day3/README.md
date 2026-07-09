# Day 3 Learnings

In this day, I learned about token usage, finish reasons, and how to limit output length.

## Why tokens are needed
Tokens are the basic units of text that the model reads and generates. A token can be a whole word, part of a word, or even punctuation.

The model does not process raw text directly. It first breaks the input into tokens, and then it uses those tokens to understand the request and generate a response.

This is why token usage matters:
- The model needs tokens to understand your prompt.
- The model also uses tokens to generate its answer.
- More tokens usually mean more cost and longer response time.

## What is the requirement of tokens?
Every API request uses tokens in two main parts:

1. Input tokens
   - These are the tokens used by your prompt and conversation history.
   - A longer question or more previous messages means more input tokens.

2. Completion tokens
   - These are the tokens used by the model to generate the answer.
   - A longer response means more completion tokens.

3. Total tokens
   - This is the sum of input tokens and completion tokens.

Example:
```python
usage = response.usage
print(usage.prompt_tokens)       # input tokens
print(usage.completion_tokens)   # output tokens
print(usage.total_tokens)        # total used
```

## Why we need to limit tokens
Limiting tokens is important because:
- It controls cost
- It keeps responses shorter
- It avoids generating too much text
- It helps fit within API limits

## How to limit tokens
You can limit the response length by using `max_tokens`.

Example:
```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Explain time travel in simple terms"}],
    max_tokens=50
)
```

In this example, the model is asked to generate at most 50 tokens.

### Example with a short answer
If the prompt is small and the limit is low, the model will respond briefly.

### Example with a long prompt
If the prompt is long, the model may use more input tokens, and the output may be shorter because of the limit.

## What is finish reason?
`finish_reason` tells us why the model stopped generating text.

It is usually one of these values:
- `stop` → the model finished normally because it reached a natural stopping point
- `length` → the response stopped because the `max_tokens` limit was reached
- `content_filter` → the response was blocked by safety filters
- `tool_calls` → the model used a tool and stopped generating text

## When should finish reason appear?
It appears in the response object after the model generates text.

Example:
```python
print(response.choices[0].finish_reason)
```

## How to handle finish reason
You should check it so that you know why the model stopped.

Example:
```python
finish_reason = response.choices[0].finish_reason

if finish_reason == "stop":
    print("The response finished normally.")
elif finish_reason == "length":
    print("The response was cut off because max_tokens was reached.")
elif finish_reason == "content_filter":
    print("The response was blocked by a safety filter.")
else:
    print(f"Other finish reason: {finish_reason}")
```

## Practical example
```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Write a short poem"}],
    max_tokens=30
)

print(response.choices[0].message.content)
print(response.choices[0].finish_reason)
```

If the model reaches the 30-token limit, you may see:
```text
length
```

That means the answer was cut off before completion because the token limit was reached.

## Summary
- Tokens are needed to read input and generate output.
- `prompt_tokens` measure the input size.
- `completion_tokens` measure the output size.
- `total_tokens` is the combined total.
- `max_tokens` helps control response length.
- `finish_reason` tells you why the model stopped.

## Example files
- [tokens.py](tokens.py)
