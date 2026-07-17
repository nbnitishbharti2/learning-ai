# Class for Resume
from pydantic import BaseModel, Field
from base_classes.experience import Experience, experience_schema

class Resume(BaseModel):
    name: str = ""
    email: str = ""
    phone: str = ""

    total_exp_years: str | None = None

    skills: list[str] = Field(default_factory=list)

    experiences: list[Experience] = Field(default_factory=list)

    projects: list[str] = Field(default_factory=list)

    certifications: list[str] = Field(default_factory=list)

resume_schema = Resume.model_json_schema()