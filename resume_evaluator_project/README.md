# Resume Evaluator Project Learnings

In this project, I learned how to build a complete end-to-end application that combines document text parsing, structured schemas, and multiple LLM calls to match resumes against a job description.

## Workflow Overview
Our evaluator operates in three distinct stages:
1. **Parse the Job Description (JD)** from unstructured text into a structured Pydantic model.
2. **Read and Parse Resumes** from formats like PDF or DOCX using helper libraries into a structured model.
3. **Compute a Match Score & Verdict** by prompting the LLM with both structured models side-by-side.

## Parsing PDF and Word Documents
We use `pypdf` for extracting text from PDF structures, and `python-docx` for `.docx` and `.doc` word documents.

Example details:
```python
from pathlib import Path
from pypdf import PdfReader
from docx import Document

# Reading a PDF file
reader = PdfReader("resume.pdf")
text = "".join([page.extract_text() for page in reader.pages])
```

## Structured Pydantic Schemas
We leverage Pydantic models to guarantee that JSON replies returned by the LLM adhere to strict fields (e.g. name, experiences, skills). These models are passed to the Groq API as JSON schemas.

Example schema definition:
```python
from pydantic import BaseModel, Field

class MatchResult(BaseModel):
    name: str = Field("", description="Name of the candidate")
    score: float = Field(0.0, description="Match score (0 to 100)")
    details: dict = Field({}, description="Match details")
    final_verdict: str = Field("", description="Final verdict")
```

## Summary
The Resume Evaluator Project represents a practical culmination of:
- Structured text generation
- Prompt engineering with multiple system roles
- Local document parsing
- Pydantic schema validation

## Example Files
- [resume_evaluator.py](resume_evaluator.py) — Main entry point to orchestrate evaluation.
- [utils/utils.py](utils/utils.py) — Text cleaners, file readers, and JSON parsing helpers.
- [services/jd_parser.py](services/jd_parser.py) — Service to extract structured JD details.
- [services/resume_parser.py](services/resume_parser.py) — Service to extract structured Resume details.
- [services/final_score.py](services/final_score.py) — Service to calculate the final match scoring.
