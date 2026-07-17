
from pathlib import Path
from base_classes.match_result import match_result_schema, MatchResult
from utils.utils import read_resume
from services.jd_parser import jd_parser
from services.resume_parser import resume_parser
from services.final_score import final_score
import time

# Get Job description JOSN Data

jd_json = jd_parser()

if jd_json is None:
    print("Error parsing job description")
    exit()


# Read resumes
resume_folder = Path("resumes")
match_results = []
try:

    for file_path in resume_folder.iterdir():
        if file_path.suffix.lower() not in [".pdf", ".docx", ".doc"]:
            print(f"File format not supported: {file_path}")
            continue

        print(f"\nProcessing: {file_path.name}...")
        resume_text = read_resume(file_path)

        if resume_text is None:
            print(f"Error reading resume: {file_path.name}")
            continue
        print(f"\nParsing resume: {file_path.name}...")
        parsed_resume = resume_parser(resume_text)

        if parsed_resume is None:
            print(f"Error parsing resume: {file_path.name}")
            continue
        time.sleep(5)
        print(f"\nMatching JD and resume: {file_path.name}...")
        result = final_score(jd_json, parsed_resume)

        if result is None:
            print(f"Error matching resume: {file_path.name}")
            continue
        time.sleep(5)
        print(result.score)
        match_results.append({
            "name": parsed_resume.name,
            "score": result.score,
            "details": result.details,
            "final_verdict": result.final_verdict
        })

        print(f"Processed {file_path.name} successfully")
    
except Exception as e:
    print(f"Error: {e}")
    exit()

print(f"All resume matching finished.")
print(match_results)