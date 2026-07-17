# Class for Job Description

from pydantic import BaseModel

class JobDescription(BaseModel):
    role: str | None
    required_skills: list[str] | None
    preferred_skills: list[str] | None
    minimum_experience: float | None
    education_qualification: str | None
    responsibilities: list[str] | None

job_description_schema = JobDescription.model_json_schema()