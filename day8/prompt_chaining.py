import os
import sys
from dotenv import load_dotenv
from groq import Groq
import time

# Reconfigure stdout to use UTF-8 encoding (prevents UnicodeEncodeError on Windows)
sys.stdout.reconfigure(encoding='utf-8')

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API_KEY)

MODEL="llama-3.3-70b-versatile"

# Job description
JD = """
We are hiring a python backend developer.
Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Redis
- Docker
- AWS
- Git
- Linux

Experience: Minimum 2 years
"""

# Resume
RESUME = """
Name: Rahul Sharma

Education

- Bachelor of Technology in Computer Science, 2018–2022
- Indian Institute of Information Technology, Allahabad
- GPA: 3.8/4.0

Relevant Coursework

- Advanced Algorithms
- Django
- FastAPI
- Docker
- Linux
- Distributed Systems
- Machine Learning
- Database Management Systems

Professional Experience

- Software Engineer, Google, Zurich, Switzerland
- June 2022 – Present
- Developed and maintained scalable backend systems using Python and gRPC
- Collaborated in cross-functional teams to deliver high-quality software
- Contributed to system design and architecture discussions
- Implemented CI/CD pipelines and automated testing workflows

Achievements

- Received Google Peer Bonus for exceptional teamwork and technical contribution
- Presented technical talk at internal engineering conference
- Mentored junior engineers and interns

"""

# Function to ask LLM
def ask_llm(system_prompt, user_prompt):
	messages=[
		{
			"role": "system",
			"content": system_prompt
		},
		{
			"role": "user",
			"content": user_prompt
		}
	]
	response = client.chat.completions.create(
		model=MODEL,
		messages=messages,
		temperature=0.7
	)
	answer = response.choices[0].message.content

	return answer

def step1_resume_skills():
	# Extract skill from resume
	system_prompt = """
	You are a professional HR assistant. Extract the skills from the resume provided.
	Return only skills, not any other details. Do not invent any skills by yourself.
	"""

	user_prompt = f"""
	{RESUME}
	"""
	
	return ask_llm(system_prompt, user_prompt)
	
def step2_jd_skills():
	# Extract skills from JD
	system_prompt = """
	You are a professional HR assistant. Extract the skills from the job description provided.
	Return only skills, not any other details. Do not invent any skills by yourself.
	"""

	user_prompt = f"""
	{JD}
	"""
	
	return ask_llm(system_prompt, user_prompt)


def step3_match_skills(candidate_skills,jd_skills):
	# Match skills from resume and JD
	system_prompt = """
	You are an expert in matching skills from a resume with the skills required in a job description.
	Compare the skills of the candidate and JD skills and produce a final score between 1 to 100 percent. Also produce a short verdict wheather a candidate is a good fit or not and why.
	"""

	user_prompt = f"""
	Candidate Skills:
	{candidate_skills}
	
	Job Skills:
	{jd_skills}
	"""
	
	return ask_llm(system_prompt, user_prompt)

# Extract resume skills
candidate_skills = step1_resume_skills()
print(candidate_skills)
print("\n")
time.sleep(3)

# Extract JD skills
jd_skills = step2_jd_skills()
print(jd_skills)
print("\n")
time.sleep(3)

# Match skills from resume and JD
final_result = step3_match_skills(candidate_skills, jd_skills)
print(final_result)