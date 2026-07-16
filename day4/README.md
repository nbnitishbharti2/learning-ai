# Day 4 Learnings

In this day, I learned how to ask an LLM for structured output using a Pydantic model and a JSON schema.

## Why structured output matters
Structured output is useful when you want the model to return data in a predictable format.
This is helpful for:
- Extracting information from emails or documents
- Filling form-like objects in code
- Building APIs and automation workflows
- Reducing manual parsing of free-form responses

## Using Pydantic
Pydantic helps define the shape of the data you want.

Example:
```python
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    email: str
    phone: str
    issue: str
```

This model defines the expected fields for the extracted information.

## Generating a schema
You can generate a JSON schema from the model using:
```python
schema = Ticket.model_json_schema()
```

That schema tells the model what fields should appear in the response.

## Sending the schema to the model
The system prompt can instruct the model to return a JSON object that matches the schema.

Example idea:
```python
system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema {schema}.
Return ONLY a valid JSON object that matches this schema.
"""
```

## Why this is useful
- It makes outputs easier to parse
- It helps avoid extra explanation text
- It keeps the result consistent for downstream code

## Summary
Day 4 introduced structured data extraction using Pydantic and JSON schemas. This is a strong pattern for building reliable LLM-powered applications.

## Example files
- [json_pydantic.py](json_pydantic.py)
- [main.py](main.py)
