# database connection and utility functions for EmploiQL
# this module handles all communication between python and postgresql

import os
from typing import Optional
from contextlib import contextmanager

import psycopg2
# RealDictCursor returns rows as dictionaries instead of tuples
from psycopg2.extras import RealDictCursor

# CONNECTION MANAGEMENT
def get_connection():
    """
    create and return a raw database connection.
    
    use this when you need fine-grained control over commits/rollbacks
    for most cases, prefer get_cursor() context manager instead
    
    caller is responsible for closing the connection
    """
    # psycopg2.connect() establishes a TCP connection to the postgresql server
    # and authenticates. returns a connection object for running queries.
    # host="localhost" postgresql runs on your machine
    # port=5432 is postgresql's default port
    connection = psycopg2.connect(
        dbname="EmploiQL",
        user=os.getenv("USER"),
        host="localhost",
        port="5432"
    )
    return connection


@contextmanager
def get_cursor(commit: bool = True):
    """
    context manager that handles connection lifecycle automatically.
    
    - automatically closes cursor and connection when done
    - automatically commits on success (if commit=True)
    - automatically rolls back on exception
    - returns dict rows for easier data access
    
    usage:
        with get_cursor() as cursor:
            cursor.execute("SELECT * FROM companies")
            rows = cursor.fetchall()
        # connection automatically closed here, changes committed
    
    args:
        commit: if true, commit transaction on successful exit.
                set to false for read-only queries 
    """
    # @contextmanager decorator turns this function into a context manager
    # code before 'yield' runs on __enter__ (the 'with' line)
    # code after 'yield' runs on __exit__ (leaving the 'with' block)
    
    connection = None
    cursor = None
    
    try:
        connection = get_connection()
        
        # cursor_factory=RealDictCursor makes all results return as dicts
        # instead of creating a cursor then setting its type, we pass it here
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        
        # yield pauses here and gives cursor to with block
        # when the block finishes, execution continues 
        yield cursor
        
        # if we reach here, no exception was raised
        if commit:
            # commit() saves all changes made during this session to the database
            # without commit, changes exist only in memory and disappear on close
            connection.commit()
            
    except Exception:
        # if any error occurred in the with block, undo all changes
        # rollback() discards all uncommitted changes from this session
        if connection:
            connection.rollback()
        # re-raise the exception so caller knows something went wrong
        raise
        
    finally:
        # finally block ALWAYS runs, even if there was an exception
        # this guarantees we don't leak database connections
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# COMPANY CRUD OPERATIONS
def insert_company(name: str, website: Optional[str] = None) -> int:
    """
    insert a new company and return its id.
    
    args:
        name: company name (must be unique)
        website: optional company website url
    
    returns:
        the auto-generated id of the new company
    
    raises:
        psycopg2.errors.UniqueViolation: if company name already exists
    """
    with get_cursor() as cursor:
        # %s is placeholder - psycopg2 safely substitutes the values
        # RETURNING id tells postgresql to send back the new row's id
        # better than doing a separate SELECT to find it
        cursor.execute(
            """
            INSERT INTO companies (name, website)
            VALUES (%s, %s)
            RETURNING id
            """,
            (name, website)  # values as tuple, order matches %s placeholders
        )
        
        # fetchone() gets one row, returns dict because of RealDictCursor
        result = cursor.fetchone()
        return result["id"]


def get_company_by_name(name: str) -> Optional[dict]:
    """
    find a company by exact name match.
    
    returns:
        dict with company data, or None if not found
    """
    # commit=False because only reading, not modifying data
    # skips the commit step 
    with get_cursor(commit=False) as cursor:
        cursor.execute(
            "SELECT id, name, website FROM companies WHERE name = %s",
            (name,)  # single-element tuple needs trailing comma
        )
        # fetchone() returns none if no rows match
        return cursor.fetchone()


def get_or_create_company(name: str, website: Optional[str] = None) -> int:
    """
    get existing company id or create new one if it doesn't exist.
    
    don't know if the company already exists, don't want duplicates.
    
    returns:
        company id (existing or newly created)
    """
    existing_company = get_company_by_name(name)
    
    if existing_company:
        return existing_company["id"]
    
    return insert_company(name, website)


# SKILL CRUD OPERATIONS
def insert_skill(name: str) -> int:
    """insert a new skill and return its id."""
    with get_cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO skills (name)
            VALUES (%s)
            RETURNING id
            """,
            (name,)
        )
        return cursor.fetchone()["id"]


def get_skill_by_name(name: str) -> Optional[dict]:
    """find a skill by exact name match."""
    with get_cursor(commit=False) as cursor:
        cursor.execute(
            "SELECT id, name FROM skills WHERE name = %s",
            (name,)
        )
        return cursor.fetchone()


def get_or_create_skill(name: str) -> int:
    """get existing skill id or create new one."""
    existing_skill = get_skill_by_name(name)
    
    if existing_skill:
        return existing_skill["id"]
    
    return insert_skill(name)


def get_all_skills() -> list[dict]:
    """return all skills in alphabetical order."""
    with get_cursor(commit=False) as cursor:
        cursor.execute("SELECT id, name FROM skills ORDER BY name")
        # fetchall() returns list of all matching rows
        return cursor.fetchall()


# JOB CRUD OPERATIONS
def insert_job(
    company_id: int,
    title: str,
    description: Optional[str] = None,
    salary_min: Optional[int] = None,
    salary_max: Optional[int] = None,
    location: Optional[str] = None,
    posted_date: Optional[str] = None,
    source_url: Optional[str] = None
) -> int:
    """
    insert a new job posting and return its id.
    
    args:
        company_id: must reference existing company (foreign key)
        title: job title
        description: full job description text
        salary_min/max: salary range (often null in postings)
        location: job location
        posted_date: when job was posted (format: 'YYYY-MM-DD')
        source_url: original posting url
    
    returns:
        the auto-generated id of the new job
    """
    with get_cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO jobs (
                company_id, title, description, 
                salary_min, salary_max, location,
                posted_date, source_url
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (
                company_id, title, description,
                salary_min, salary_max, location,
                posted_date, source_url
            )
        )
        return cursor.fetchone()["id"]


def get_job_by_id(job_id: int) -> Optional[dict]:
    """
    get a job with its company name included.
    
    demonstrates JOIN - combining data from multiple tables.
    """
    with get_cursor(commit=False) as cursor:
        # JOIN connects jobs to companies via the foreign key
        # jobs.company_id must match companies.id
        # alias companies.name as company_name to avoid confusion
        cursor.execute(
            """
            SELECT 
                jobs.id,
                jobs.title,
                jobs.description,
                jobs.salary_min,
                jobs.salary_max,
                jobs.location,
                jobs.posted_date,
                jobs.source_url,
                jobs.created_at,
                companies.name AS company_name
            FROM jobs
            JOIN companies ON jobs.company_id = companies.id
            WHERE jobs.id = %s
            """,
            (job_id,)
        )
        return cursor.fetchone()


def search_jobs(
    location: Optional[str] = None,
    title_contains: Optional[str] = None,
    limit: int = 50
) -> list[dict]:
    """
    search jobs with optional filters.
    
    demonstrates dynamic query building with parameterized queries.
    """
    # start with base query
    query = """
        SELECT 
            jobs.id,
            jobs.title,
            jobs.location,
            jobs.salary_min,
            jobs.salary_max,
            companies.name AS company_name
        FROM jobs
        JOIN companies ON jobs.company_id = companies.id
        WHERE 1=1
    """
    # WHERE 1=1 trick: it's always true, but lets us add conditions
    # with AND without worrying if it's the first condition or not
    
    # collect parameters in a list since order matters
    parameters = []
    
    # dynamically add conditions based on what filters were provided
    if location:
        # ILIKE = case-insensitive pattern match
        # %% becomes a literal % after python formatting
        # so '%' || %s || '%' builds a pattern like '%montreal%'
        query += " AND jobs.location ILIKE %s"
        parameters.append(f"%{location}%")
    
    if title_contains:
        query += " AND jobs.title ILIKE %s"
        parameters.append(f"%{title_contains}%")
    
    query += " ORDER BY jobs.created_at DESC LIMIT %s"
    parameters.append(limit)
    
    with get_cursor(commit=False) as cursor:
        cursor.execute(query, tuple(parameters))
        return cursor.fetchall()


# JOB_SKILLS JUNCTION TABLE OPERATIONS
def link_job_to_skill(job_id: int, skill_id: int) -> None:
    """
    create a relationship between a job and a skill.
    
    the job_skills table has a composite primary key (job_id, skill_id),
    meaning each pair can only exist once - no duplicate links.
    """
    with get_cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO job_skills (job_id, skill_id)
            VALUES (%s, %s)
            """,
            (job_id, skill_id)
        )


def link_job_to_skills(job_id: int, skill_names: list[str]) -> None:
    """
    link a job to multiple skills by name, creating skills if needed.
    
    this is the pattern you'll use when processing extracted job data:
    the LLM gives you skill names, you need to normalize them in the db.
    """
    for skill_name in skill_names:
        # get_or_create ensures skill exists and gives us its id
        skill_id = get_or_create_skill(skill_name)
        
        # try to create the link, ignore if it already exists
        try:
            link_job_to_skill(job_id, skill_id)
        except psycopg2.errors.UniqueViolation:
            # link already exists, that's fine - continue to next skill
            # need to rollback the failed transaction before continuing
            pass


def get_skills_for_job(job_id: int) -> list[dict]:
    """get all skills required for a specific job."""
    with get_cursor(commit=False) as cursor:
        # JOIN through junction table to get skill names
        cursor.execute(
            """
            SELECT skills.id, skills.name
            FROM skills
            JOIN job_skills ON skills.id = job_skills.skill_id
            WHERE job_skills.job_id = %s
            ORDER BY skills.name
            """,
            (job_id,)
        )
        return cursor.fetchall()


def get_top_skills(limit: int = 10) -> list[dict]:
    """
    get the most frequently requested skills across all jobs
    
    this is a key query
    """
    with get_cursor(commit=False) as cursor:
        # COUNT(*) counts rows, GROUP BY collects rows by skill
        # so we count how many jobs list each skill
        cursor.execute(
            """
            SELECT 
                skills.name,
                COUNT(*) AS job_count
            FROM skills
            JOIN job_skills ON skills.id = job_skills.skill_id
            GROUP BY skills.id, skills.name
            ORDER BY job_count DESC
            LIMIT %s
            """,
            (limit,)
        )
        return cursor.fetchall()


# RAW_POSTINGS CRUD OPERATIONS
def insert_raw_posting(
    source: str,
    url: str,
    raw_content: Optional[str] = None
) -> int:
    """
    store a scraped job posting for later processing.
    
    args:
        source: where it came from ("indeed", "linkedin", etc.)
        url: original posting url (must be unique)
        raw_content: the raw html/text that was scraped
    
    returns:
        id of the new raw_posting
    """
    with get_cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO raw_postings (source, url, raw_content)
            VALUES (%s, %s, %s)
            RETURNING id
            """,
            (source, url, raw_content)
        )
        return cursor.fetchone()["id"]


def get_unprocessed_postings(limit: int = 100) -> list[dict]:
    """
    get raw postings that haven't been processed by the LLM yet.
    
    uses the idx_raw_postings_processed index for fast lookup.
    """
    with get_cursor(commit=False) as cursor:
        cursor.execute(
            """
            SELECT id, source, url, raw_content, scraped_at
            FROM raw_postings
            WHERE processed = FALSE
            ORDER BY scraped_at ASC
            LIMIT %s
            """,
            (limit,)
        )
        return cursor.fetchall()


def mark_posting_processed(raw_posting_id: int, job_id: int) -> None:
    """
    mark a raw posting as processed and link it to the created job.
    
    called after LLM successfully extracts data and job is inserted.
    """
    with get_cursor() as cursor:
        cursor.execute(
            """
            UPDATE raw_postings
            SET processed = TRUE, job_id = %s
            WHERE id = %s
            """,
            (job_id, raw_posting_id)
        )


# CONNECTION TEST
if __name__ == "__main__":
    # quick test that connection and basic operations work
    print("testing database connection...")
    
    with get_cursor(commit=False) as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        # result is a dict because of RealDictCursor
        # the column is auto-named "?column?" for literal SELECT
        if result:
            print("connected successfully to EmploiQL database")
        else:
            print("connection test failed")
    
    print("\ntesting get_top_skills (will be empty if no data)...")
    top_skills = get_top_skills(5)
    if top_skills:
        for skill in top_skills:
            print(f"  {skill['name']}: {skill['job_count']} jobs")
    else:
        print("  (no skills in database yet)")