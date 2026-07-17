# Function to parse JD from text to JSON

from core.dependencies import client
from base_classes.job_description import job_description_schema, JobDescription
from utils.utils import getJson

def jd_parser():
    # Job Description against which LLM needs to evaluate the resume
    job_description = f"""
    Job description

    Key Responsibilities:

    - Design and implement advanced Generative AI models to solve complex problems.
    - Collaborate with cross-functional teams to integrate AI solutions into existing systems.
    - Conduct research and stay updated with the latest advancements in NLP and AI technologies.
    - Develop scalable and efficient AI algorithms to enhance product offerings.
    - Mentor junior team members and share knowledge to foster a culture of learning.

    Good to have skills: Machine Learning, Data Analysis, Deep Learning, Python Programming, Cloud Computing
    """

    # System prompt or instruction to fetch the job description json from job description data
    system_prompt = f"""
    You are an expert HR assistant.
    Your job is to analyze the job description and extract the structured information from them.

    Return only valid JSON matching this schema

    {job_description_schema}

    Rules:
    - Do not return the schema itself.
    - Do not return fields like "properties", "title" or "type".
    - Fill the schema with actual information extracted from the job description.

    If minimum experince is not mentioned return null.
    If information for a list is empty, return an empty list.
    Do not invent information.

    very field in the schema MUST be present.

    Never omit a field.

    If a string field is unavailable return "".

    If a numeric field is unavailable return null.

    If a list field is unavailable return [].

    Do not skip any keys.

    """

    try:
        prompts = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": job_description
            },
        ]

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=prompts,
            response_format={
                "type": "json_object"
            },
            temperature=0.2,
        )

        print(f" ========================         JD LLM Response:        ============================        ")
        job_desc = response.choices[0].message.content
        # print(job_desc) 


        # converts to JSON file and read JSON
        jd_json = getJson(job_desc, JobDescription)
        return jd_json
    except Exception as e:
        print(f"Error parsing job description: {e}")
        return None
    