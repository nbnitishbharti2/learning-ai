# Function to calculate final score

from core.dependencies import client
from base_classes.match_result import match_result_schema, MatchResult
from utils.utils import getJson

def final_score(jd_json, resume_json):
    # System prompt or instruction to fetch the final score from job description json and resume json
    final_score_system_prompt = f"""
    You are an expert Resume Matcher.
    Your job is to analyze the resume json and job description json and match them.

    Return only valid JSON matching this schema

    {match_result_schema}

    Rules:
    - Do not return the schema itself.
    - Do not return fields like "properties", "title" or "type".
    - Fill the schema with actual information extracted from the job description.

    If information for a list is empty, return an empty list.
    Match score should be between 0 and 100.
    Do not invent information.

    very field in the schema MUST be present.

    Never omit a field.

    If a string field is unavailable return "".

    If a numeric field is unavailable return null.

    If a list field is unavailable return [].

    Do not skip any keys.

    """

    final_score_prompts = [
        {
            "role": "system",
            "content": final_score_system_prompt
        },
        {
            "role": "user",
            "content": f"Job Description:\n{jd_json.model_dump_json()}"
        },
        {
            "role": "user",
            "content": f"Candidate Resume:\n{resume_json.model_dump_json()}"
        },
    ]

    final_score_response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=final_score_prompts,
        response_format={
            "type": "json_object"
        },
        temperature=0.2,
    )

    print(f" ========================         Final Score LLM Response:        ============================        ")
    final_score_res = final_score_response.choices[0].message.content
    # print(final_score_res) 


    # converts to JSON file and read JSON
    final_score_json = getJson(final_score_res, MatchResult)
    return final_score_json