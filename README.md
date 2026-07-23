# Learnings from the Python LLM Project

This project is a simple day-wise learning journey for working with LLM APIs in Python using Groq.

## Project structure
- [Introduction](Introduction/) contains the overview of the 9-week learning path and style.
- [day1](day1/) contains the first example for connecting to an LLM and getting a response.
- [day2](day2/) covers message roles and temperature.
- [day3](day3/) explains token usage, finish reasons, and token limits.
- [day4](day4/) focuses on structured outputs using Pydantic and JSON schemas.
- [day5 - resume_evaluator_project](resume_evaluator_project/) contains a mini resume evaluation project using PDFs, Word documents, and LLMs
- [day6](day6/) covers structured prompt engineering and classification tasks.
- [day7](day7/) implements the ReAct (Reasoning and Acting) agent pattern with a tool-execution loop.
- [day8](day8/) demonstrates prompt chaining by executing sequential tasks where output flows from step to step.

## Day-wise learnings

### Day 1 - Connecting to an LLM
- Learned how to load the API key from a `.env` file using `python-dotenv`.
- Learned how to initialize the Groq client.
- Sent a simple user prompt to the model and printed the returned response.
- See [day1/README.md](day1/README.md) for the detailed notes.

### Day 2 - Roles and temperature
- Learned about message roles such as `system`, `user`, and `assistant`.
- Understood that the `system` role can shape the assistant's behavior.
- Learned that `temperature` controls how creative or random the response can be.
- See [day2/README.md](day2/README.md) for the detailed notes.

### Day 3 - Tokens and finish reasons
- Learned about `prompt_tokens`, `completion_tokens`, and `total_tokens`.
- Understood that `max_tokens` can be used to limit the output length.
- Observed `finish_reason` to understand why the model stopped generating text.
- See [day3/README.md](day3/README.md) for the detailed notes.

### Day 4 - Structured outputs with Pydantic
- Learned how to define a Pydantic model for structured data.
- Used `model_json_schema()` to generate a JSON schema from the model.
- Sent the schema to the LLM and asked for a JSON object matching the required fields.
- See [day4/README.md](day4/README.md) for the detailed notes.

### Day 5 - Resume Evaluator Project 
- Integrated document parsers (`pypdf` for PDFs, `python-docx` for `.docx` / `.doc` files).
- Orchestrated multiple sequential LLM tasks (parsing job description, parsing resume, and matching).
- Implemented robust key-value extraction and match scoring utilizing Pydantic models.
- See [resume_evaluator_project/README.md](resume_evaluator_project/README.md) for the detailed notes.

### Day 6 - Prompt Engineering
- Learned how to structure prompt elements including ROLE, TASK, CONSTRAINTS, OUTPUT FORMAT, EXAMPLES, and FALLBACK.
- Applied structured templates to classify customer emails into single-word categories (billing, technical, return, or OTHER).
- See [day6/README.md](day6/README.md) for the detailed notes.

### Day 7 - ReAct (Reasoning and Acting) Agents
- Learned about the ReAct pattern where the LLM alternates between reasoning (Thought) and action (calling tools).
- Implemented a parser to extract tool calls and executed the tools using Python.
- Fed observations back to the LLM's conversation history to maintain context.
- See [day7/README.md](day7/README.md) for the detailed notes.

### Day 8 - Prompt Chaining
- Learned how to decompose complex tasks into multiple sequential, focused prompts.
- Connected the output of resume and JD skill extraction steps into a final candidate-matching step.
- Observed how chaining reduces complexity and increases reliability of LLM completions.
- See [day8/README.md](day8/README.md) for the detailed notes.
