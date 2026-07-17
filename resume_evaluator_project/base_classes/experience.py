# Class for Experience
from pydantic import BaseModel

class Experience(BaseModel):
    company: str
    role: str
    duration: str
    description: list[str]
    skills_used: list[str]

experience_schema = Experience.model_json_schema()