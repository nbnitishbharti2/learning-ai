# Function to parse resume from text to JSON

from core.dependencies import client
from base_classes.resume import resume_schema, Resume
from utils.utils import getJson

def resume_parser(resume_text):

    # System prompt or instruction to fetch the resume json from resume data
    resume_system_prompt = f"""
    You are an expert Resume Parser.
    Your job is to analyze the resume and extract the structured information from them.

    Return only valid JSON matching this schema

    {resume_schema}

    Rules:
    - Do not return the schema itself.
    - Do not return fields like "properties", "title" or "type".
    - Fill the schema with actual information extracted from the job description.

    If total_exp_years is not mentioned return null.
    If information for a list is empty, return an empty list.
    Do not invent information.

    very field in the schema MUST be present.

    Never omit a field.

    If a string field is unavailable return "".

    If a numeric field is unavailable return null.

    If a list field is unavailable return [].

    Do not skip any keys.

    """

    resume_prompts = [
        {
            "role": "system",
            "content": resume_system_prompt
        },
        {
            "role": "user",
            "content": resume_text
        },
    ]

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=resume_prompts,
        response_format={
            "type": "json_object"
        },
        temperature=0.2,
    )

    print(f" ========================         Resume LLM Response:        ============================        ")
    resume_res = response.choices[0].message.content
    # print(resume_res) 


    # converts to JSON file and read JSON
    resume_json = getJson(resume_res, Resume)
    return resume_json