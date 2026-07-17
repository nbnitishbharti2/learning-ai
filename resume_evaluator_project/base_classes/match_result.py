# Class for Match Result Based on JD & Resume Data

from pydantic import BaseModel, Field

class MatchResult(BaseModel):
    name: str = Field("", description="Name of the candidate")
    score: float = Field(0.0, description="Match score between resume and job description")
    details: dict = Field({}, description="Details of the match")
    final_verdict: str = Field("", description="Final verdict based on the match score")

match_result_schema = MatchResult.model_json_schema()