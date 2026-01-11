# natural language to SQL conversion
# uses GPT-4o to generate SQL from plain english/french questions
import config
import json
import os
import re
from typing import Optional

from openai import OpenAI

from db import get_cursor

# lazy client initialization: only created when needed
# allows dashboard to load without OPENAI_API_KEY set
_client = None


def _get_client() -> OpenAI:
    """
    get or create the OpenAI client.
    lazy initialization so app can load without API key.
    raises clear error if key not set when actually needed.
    """
    global _client
    
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY environment variable not set. "
                "Set it with: export OPENAI_API_KEY='your-key-here'"
            )
        _client = OpenAI(api_key=api_key)
    
    return _client


# schema context for the LLM - needs to know exact table/column names
SCHEMA_DESCRIPTION = """
DATABASE SCHEMA:

TABLE companies (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    website TEXT
)

TABLE skills (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
)

TABLE jobs (
    id SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES companies(id),
    title TEXT NOT NULL,
    description TEXT,
    salary_min INTEGER,  -- annual CAD, nullable
    salary_max INTEGER,  -- annual CAD, nullable
    location TEXT,       -- 'Montreal', 'Remote', 'Hybrid - Montreal', etc.
    posted_date DATE,
    source_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
)

TABLE job_skills (
    job_id INTEGER REFERENCES jobs(id),
    skill_id INTEGER REFERENCES skills(id),
    PRIMARY KEY (job_id, skill_id)
)
-- junction table: each row = "this job requires this skill"

TABLE raw_postings (
    id SERIAL PRIMARY KEY,
    source TEXT NOT NULL,      -- 'indeed', 'linkedin'
    url TEXT UNIQUE NOT NULL,
    raw_content TEXT,
    scraped_at TIMESTAMP DEFAULT NOW(),
    processed BOOLEAN DEFAULT FALSE,
    job_id INTEGER REFERENCES jobs(id)
)

RELATIONSHIPS:
- jobs.company_id -> companies.id (many jobs per company)
- job_skills links jobs <-> skills (many-to-many)
- raw_postings.job_id -> jobs.id (multiple raw postings can map to one job)

COMMON QUERY PATTERNS:
- skill frequency: COUNT(*) on job_skills grouped by skill
- jobs by company: JOIN jobs with companies
- salary ranges: use salary_min and salary_max (often NULL)
- location filtering: use ILIKE for fuzzy match
"""

# few-shot examples help the model understand expected output format
FEW_SHOT_EXAMPLES = """
EXAMPLE QUERIES:

Q: What are the top 10 most requested skills?
SQL:
SELECT s.name, COUNT(*) AS job_count
FROM skills s
JOIN job_skills js ON s.id = js.skill_id
GROUP BY s.id, s.name
ORDER BY job_count DESC
LIMIT 10;

Q: Which companies have the most job postings?
SQL:
SELECT c.name, COUNT(*) AS job_count
FROM companies c
JOIN jobs j ON c.id = j.company_id
GROUP BY c.id, c.name
ORDER BY job_count DESC
LIMIT 10;

Q: Show me remote Python jobs
SQL:
SELECT j.title, c.name AS company, j.salary_min, j.salary_max
FROM jobs j
JOIN companies c ON j.company_id = c.id
JOIN job_skills js ON j.id = js.job_id
JOIN skills s ON js.skill_id = s.id
WHERE j.location ILIKE '%remote%'
AND s.name = 'Python'
ORDER BY j.created_at DESC;

Q: What's the average salary for jobs requiring PostgreSQL?
SQL:
SELECT 
    AVG(j.salary_min) AS avg_min_salary,
    AVG(j.salary_max) AS avg_max_salary,
    COUNT(*) AS job_count
FROM jobs j
JOIN job_skills js ON j.id = js.job_id
JOIN skills s ON js.skill_id = s.id
WHERE s.name = 'PostgreSQL'
AND j.salary_min IS NOT NULL;

Q: List all skills for Ubisoft jobs
SQL:
SELECT DISTINCT s.name
FROM skills s
JOIN job_skills js ON s.id = js.skill_id
JOIN jobs j ON js.job_id = j.id
JOIN companies c ON j.company_id = c.id
WHERE c.name ILIKE '%ubisoft%'
ORDER BY s.name;
"""


def generate_sql(question: str) -> str:
    """
    convert natural language question to SQL query.
    uses GPT-4o for better accuracy on complex queries.
    """
    # get client (will raise error if API key not set)
    client = _get_client()
    
    system_prompt = f"""You are a SQL expert. Convert natural language questions into PostgreSQL queries.

{SCHEMA_DESCRIPTION}

{FEW_SHOT_EXAMPLES}

RULES:
1. Return ONLY the SQL query, no explanation or markdown
2. Use table aliases (j for jobs, c for companies, s for skills, js for job_skills)
3. Always include appropriate JOINs when accessing related data
4. Use ILIKE for text searches (case-insensitive)
5. Handle NULL salary values appropriately
6. Add reasonable LIMITs to prevent huge result sets
7. End query with semicolon"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Q: {question}\nSQL:"}
        ],
        temperature=0,  # deterministic output
        max_tokens=500
    )
    
    sql = response.choices[0].message.content.strip()
    
    # clean up common formatting issues
    sql = clean_sql(sql)
    
    return sql


def clean_sql(sql: str) -> str:
    """remove markdown formatting and extra whitespace."""
    # strip markdown code blocks if present
    sql = re.sub(r'^```sql\s*', '', sql)
    sql = re.sub(r'^```\s*', '', sql)
    sql = re.sub(r'\s*```$', '', sql)
    
    # normalize whitespace
    sql = ' '.join(sql.split())
    
    return sql.strip()


def validate_sql(sql: str) -> tuple[bool, str]:
    """
    safety check: only allow SELECT statements.
    returns (is_safe, error_message).
    """
    sql_upper = sql.upper().strip()
    
    # must start with SELECT or WITH (for CTEs)
    if not (sql_upper.startswith('SELECT') or sql_upper.startswith('WITH')):
        return False, "only SELECT queries allowed"
    
    # block dangerous keywords
    dangerous = ['DROP', 'DELETE', 'INSERT', 'UPDATE', 'TRUNCATE', 'ALTER', 'CREATE', 'GRANT', 'REVOKE']
    for keyword in dangerous:
        # word boundary check to avoid false positives like "UPDATED_AT"
        pattern = rf'\b{keyword}\b'
        if re.search(pattern, sql_upper):
            return False, f"forbidden keyword: {keyword}"
    
    return True, ""


def execute_sql(sql: str) -> list[dict]:
    """
    execute a validated SQL query and return results.
    raises exception on invalid SQL or database errors.
    """
    # safety check before execution
    is_safe, error = validate_sql(sql)
    if not is_safe:
        raise ValueError(f"unsafe query blocked: {error}")
    
    with get_cursor(commit=False) as cursor:
        cursor.execute(sql)
        results = cursor.fetchall()
        # convert RealDictRow objects to plain dicts for cleaner output
        return [dict(row) for row in results]


def ask(question: str) -> dict:
    """
    main entry point: natural language question -> answer.
    
    returns dict with:
        - question: original question
        - sql: generated SQL query
        - results: query results (list of dicts)
        - error: error message if something failed
    """
    response = {
        "question": question,
        "sql": None,
        "results": None,
        "error": None
    }
    
    try:
        # generate SQL from question
        sql = generate_sql(question)
        response["sql"] = sql
        
        # validate and execute
        results = execute_sql(sql)
        response["results"] = results
        
    except ValueError as e:
        # validation error (unsafe query) or missing API key
        response["error"] = str(e)
    except Exception as e:
        # database error or API error
        response["error"] = f"query failed: {str(e)}"
    
    return response


def ask_interactive(question: str) -> None:
    """
    interactive version: prints formatted output.
    useful for testing in the terminal.
    """
    print(f"\nQuestion: {question}")
    print("-" * 50)
    
    result = ask(question)
    
    if result["sql"]:
        print(f"SQL: {result['sql']}")
        print("-" * 50)
    
    if result["error"]:
        print(f"Error: {result['error']}")
        return
    
    if not result["results"]:
        print("No results found.")
        return
    
    # print results as simple table
    results = result["results"]
    
    if results:
        # header
        columns = list(results[0].keys())
        print(" | ".join(columns))
        print("-" * 50)
        
        # rows
        for row in results[:20]:  # limit display to 20 rows
            values = [str(row[col])[:30] for col in columns]  # truncate long values
            print(" | ".join(values))
        
        if len(results) > 20:
            print(f"... and {len(results) - 20} more rows")


# testing
if __name__ == "__main__":
    print("=" * 60)
    print("EmploiQL Text-to-SQL Test")
    print("=" * 60)
    
    if not os.getenv("OPENAI_API_KEY"):
        print("\nOPENAI_API_KEY not set")
        print("Set it with: export OPENAI_API_KEY='your-key-here'")
        print("\nShowing schema context that would be sent:\n")
        print(SCHEMA_DESCRIPTION)
    else:
        # test queries
        test_questions = [
            "What are the top 5 most requested skills?",
            "Show me all companies in the database",
            "How many jobs are in Montreal?",
        ]
        
        for question in test_questions:
            ask_interactive(question)
            print("\n")