# Learnings from the Python LLM Project

This project is a simple day wise learning journey for working with LLM APIs in Python using Groq.

## Project structure
- [day1](day1/) contains the first example for connecting to an LLM and getting a response.
- [day2](day2/) covers message roles and temperature.
- [day3](day3/) explains token usage, finish reasons, and token limits.

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
