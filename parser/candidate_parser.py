import json
import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def parse_resume(text):

    prompt = f"""
You are an expert ATS resume parser.

Extract ALL information available in the resume.

IMPORTANT:

1. Extract skills from:
   - Skills section
   - Experience section
   - Project descriptions
   - Certifications
   - Summary/Profile

2. Infer technical skills from work experience.

Example:
- "Electrical Engineer" -> electrical systems
- "Troubleshooting electrical glitches" -> troubleshooting
- "Designed circuit boards" -> circuit design
- "Power systems" -> power systems
- "AutoCAD renderings" -> autocad
- "Testing devices" -> testing
- "Diagnostics team" -> diagnostics

3. Remove duplicates from skills.

4. Return ONLY valid JSON.

Schema:

{{
    "personal_info": {{
        "name": "",
        "email": "",
        "phone": "",
        "location": "",
        "linkedin": "",
        "github": "",
        "portfolio": ""
    }},
    "summary": "",
    "skills": [],
    "education": [],
    "experience": [],
    "projects": [],
    "certifications": [],
    "positions_of_responsibility": [],
    "achievements": [],
    "activities": [],
    "languages": [],
    "experience_years": 0
}}

Resume:

{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content
    import re

    match = re.search(
        r'\{.*\}',
        content,
        re.DOTALL
    )

    if not match:
        raise Exception(
            "No JSON found in LLM response"
        )

    content = match.group(0)
    profile=json.loads(content)

    skills = set(
    str(s).strip()
    for s in profile.get("skills", [])
)

    # experience text se keywords add karo
    for exp in profile.get("experience", []):

        exp_text = str(exp).lower()

        if "electrical" in exp_text:
            skills.add("Electrical Systems")

        if "troubleshooting" in exp_text:
            skills.add("Troubleshooting")

        if "autocad" in exp_text:
            skills.add("AutoCAD")

        if "circuit" in exp_text:
            skills.add("Circuit Design")

        if "power system" in exp_text:
            skills.add("Power Systems")

        if "testing" in exp_text:
            skills.add("Testing")

        if "diagnostic" in exp_text:
            skills.add("Diagnostics")

    profile["skills"] = sorted(list(skills))

   
    print(profile["skills"])
    return profile
    # return json.loads(content)