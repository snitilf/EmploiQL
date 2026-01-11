# extraction.py - LLM-powered job posting extraction
# uses GPT-4o-mini to convert raw job text into structured data matching our schema
import config
import json
import os
from typing import Optional

from openai import OpenAI

# initialize client - reads OPENAI_API_KEY from environment automatically
client = OpenAI()

# the extraction schema - defines exactly what structure we want back
# this maps directly to our database tables for easy insertion
EXTRACTION_SCHEMA = """
{
  "company_name": "string or null - the hiring company's name",
  "title": "string, required - job title exactly as posted",
  "description": "string or null - job responsibilities and requirements summary",
  "salary_min": "integer or null - minimum annual salary in CAD (convert hourly rates: hourly * 2080)",
  "salary_max": "integer or null - maximum annual salary in CAD",
  "location": "string or null - normalize to: 'Montreal', 'Remote', 'Hybrid - Montreal', or specific city",
  "posted_date": "string or null - format as YYYY-MM-DD if mentioned",
  "skills": ["array of strings - technical skills, languages, frameworks, tools mentioned"]
}
"""

# skill normalization mapping - consolidates variations into canonical names
# this prevents "python3", "Python 3", "python" from becoming separate skills
SKILL_NORMALIZATIONS = {
    # python variations
    "python3": "Python",
    "python 3": "Python",
    "py": "Python",
    
    # javascript variations
    "js": "JavaScript",
    "javascript": "JavaScript",
    "es6": "JavaScript",
    "ecmascript": "JavaScript",
    "node": "Node.js",
    "nodejs": "Node.js",
    "node.js": "Node.js",
    
    # typescript
    "ts": "TypeScript",
    "typescript": "TypeScript",
    
    # databases
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "psql": "PostgreSQL",
    "mongo": "MongoDB",
    "mongodb": "MongoDB",
    "mysql": "MySQL",
    "sql server": "SQL Server",
    "mssql": "SQL Server",
    
    # cloud
    "aws": "AWS",
    "amazon web services": "AWS",
    "gcp": "Google Cloud",
    "google cloud platform": "Google Cloud",
    "azure": "Azure",
    "microsoft azure": "Azure",
    
    # containers
    "docker": "Docker",
    "k8s": "Kubernetes",
    "kubernetes": "Kubernetes",
    
    # frameworks
    "react": "React",
    "reactjs": "React",
    "react.js": "React",
    "vue": "Vue.js",
    "vuejs": "Vue.js",
    "angular": "Angular",
    "angularjs": "Angular",
    "django": "Django",
    "flask": "Flask",
    "fastapi": "FastAPI",
    "express": "Express.js",
    "expressjs": "Express.js",
    
    # ML/AI
    "ml": "Machine Learning",
    "machine learning": "Machine Learning",
    "ai": "Artificial Intelligence",
    "artificial intelligence": "Artificial Intelligence",
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "scikit-learn": "Scikit-learn",
    "sklearn": "Scikit-learn",
    
    # other common
    "git": "Git",
    "github": "GitHub",
    "gitlab": "GitLab",
    "ci/cd": "CI/CD",
    "cicd": "CI/CD",
    "agile": "Agile",
    "scrum": "Scrum",
    "rest": "REST APIs",
    "restful": "REST APIs",
    "graphql": "GraphQL",
}


def normalize_skill(skill: str) -> str:
    """
    convert skill variations to canonical names.
    
    why: job postings use inconsistent casing and abbreviations.
    without normalization, "Python" and "python3" would be separate
    skills in the database, making frequency analysis useless.
    
    examples:
        "python3" -> "Python"
        "k8s" -> "Kubernetes"
        "Some Unknown Skill" -> "Some Unknown Skill" (unchanged)
    """
    # lowercase for lookup, preserve original if no match
    lookup_key = skill.lower().strip()
    return SKILL_NORMALIZATIONS.get(lookup_key, skill.strip())


def normalize_skills(skills: list[str]) -> list[str]:
    """
    normalize a list of skills and remove duplicates.
    
    after normalization, "python" and "Python3" both become "Python",
    so we deduplicate to avoid inserting the same skill twice.
    """
    normalized = [normalize_skill(s) for s in skills]
    
    # remove duplicates while preserving order
    # dict.fromkeys() keeps first occurrence of each key
    return list(dict.fromkeys(normalized))


def build_extraction_prompt(raw_content: str, source: str) -> list[dict]:
    """
    construct the message list for the extraction API call.
    
    prompt engineering choices:
    1. system message sets the role and output format
    2. schema is explicit - model knows exact structure expected
    3. rules handle edge cases (missing data, salary conversion)
    4. source context helps model interpret site-specific formatting
    """
    system_message = f"""You are a job posting data extractor. Your task is to extract 
structured information from raw job postings and return valid JSON.

Extract data into this exact schema:
{EXTRACTION_SCHEMA}

CRITICAL RULES:
1. Return ONLY valid JSON matching the schema above - no markdown, no explanation
2. Use null for missing/unknown fields, never invent data
3. Convert hourly rates to annual: hourly_rate * 2080 (40 hrs/week * 52 weeks)
4. Convert USD salaries to CAD: multiply by 1.36 (approximate exchange rate)
5. Skills should be specific technologies (Python, React, AWS), not soft skills
6. Normalize location to Montreal area when applicable
7. If salary is a single number, use it for both min and max
8. Extract 5-15 relevant technical skills maximum

The posting is from: {source}"""

    user_message = f"""Extract structured data from this job posting:

---
{raw_content}
---

Return the JSON object only."""

    return [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]


def extract_job_data(
    raw_content: str,
    source: str = "unknown",
    model: str = "gpt-4o-mini"
) -> dict:
    """
    extract structured job data from raw posting text.
    
    args:
        raw_content: the raw job posting text/html
        source: where it came from ("indeed", "linkedin")
        model: which model to use (gpt-4o-mini is cheap + fast)
    
    returns:
        dict with extracted fields matching EXTRACTION_SCHEMA
        
    raises:
        json.JSONDecodeError: if response isn't valid JSON (shouldn't happen with json mode)
        openai.APIError: if API call fails
    
    cost estimate (gpt-4o-mini pricing as of 2024):
        ~500 tokens input + ~200 tokens output per posting
        ~$0.0001 per posting = $1 per 10,000 postings
    """
    messages = build_extraction_prompt(raw_content, source)
    
    response = client.chat.completions.create(
        model=model,
        # json_object mode guarantees parseable JSON output
        # the model will never add markdown formatting or explanatory text
        # REQUIREMENT: prompt must mention "JSON" somewhere or API errors
        response_format={"type": "json_object"},
        messages=messages,
        # temperature 0 = deterministic, same input -> same output
        # good for extraction where we want consistency
        temperature=0,
        # cap tokens to control costs and prevent runaway responses
        max_tokens=1000
    )
    
    # extract the response text
    raw_response = response.choices[0].message.content
    
    # parse JSON (should never fail with json_object mode, but be safe)
    extracted = json.loads(raw_response)
    
    # normalize skills if present
    if extracted.get("skills"):
        extracted["skills"] = normalize_skills(extracted["skills"])
    
    return extracted


def extract_job_data_safe(
    raw_content: str,
    source: str = "unknown",
    model: str = "gpt-4o-mini"
) -> Optional[dict]:
    """
    safe wrapper around extract_job_data that catches errors.
    
    use this in batch processing where you don't want one bad
    posting to crash the entire pipeline.
    
    returns:
        extracted dict on success, None on any error
    """
    try:
        return extract_job_data(raw_content, source, model)
    except json.JSONDecodeError as error:
        print(f"JSON parse error: {error}")
        return None
    except Exception as error:
        print(f"extraction error: {error}")
        return None


def validate_extracted_data(data: dict) -> tuple[bool, list[str]]:
    """
    validate extracted data before database insertion.
    
    returns:
        (is_valid, list_of_errors)
        
    checks:
        - required fields present
        - types are correct
        - salary range is logical (min <= max)
    """
    errors = []
    
    # title is required
    if not data.get("title"):
        errors.append("missing required field: title")
    
    # salary sanity check
    salary_min = data.get("salary_min")
    salary_max = data.get("salary_max")
    
    if salary_min is not None and salary_max is not None:
        if salary_min > salary_max:
            errors.append(f"salary_min ({salary_min}) > salary_max ({salary_max})")
        if salary_min < 20000:
            errors.append(f"salary_min suspiciously low: {salary_min}")
        if salary_max > 500000:
            errors.append(f"salary_max suspiciously high: {salary_max}")
    
    # skills should be a list
    if data.get("skills") and not isinstance(data["skills"], list):
        errors.append("skills should be a list")
    
    return (len(errors) == 0, errors)


# testing/demo code
if __name__ == "__main__":
    # example job posting for testing
    test_posting = """
    Senior Backend Developer - Montreal
    
    TechStartup Inc is hiring!
    
    We're looking for a senior backend developer to join our team.
    You'll be building scalable APIs and working with our data pipeline.
    
    Requirements:
    - 5+ years Python experience
    - Strong PostgreSQL skills
    - Experience with Django or FastAPI
    - Familiarity with Docker and Kubernetes
    - AWS experience preferred
    
    Nice to have:
    - Machine learning background
    - GraphQL experience
    
    Salary: $95,000 - $130,000 CAD
    Location: Hybrid - Montreal office 2 days/week
    
    Apply at careers@techstartup.io
    """
    
    print("=" * 60)
    print("EmploiQL Extraction Test")
    print("=" * 60)
    
    # check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("\  OPENAI_API_KEY not set")
        print("Set it with: export OPENAI_API_KEY='your-key-here'")
        print("\nShowing what the prompt would look like:\n")
        
        messages = build_extraction_prompt(test_posting, "test")
        print("SYSTEM MESSAGE:")
        print("-" * 40)
        print(messages[0]["content"])
        print("\nUSER MESSAGE:")
        print("-" * 40)
        print(messages[1]["content"])
    else:
        print("\nExtracting data from test posting...")
        result = extract_job_data(test_posting, source="test")
        
        print("\nExtracted data:")
        print("-" * 40)
        print(json.dumps(result, indent=2))
        
        # validate
        is_valid, errors = validate_extracted_data(result)
        print(f"\nValidation: {'passed' if is_valid else 'failed'}")
        if errors:
            for e in errors:
                print(f"  - {e}")