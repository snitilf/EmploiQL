-- database blueprint for EmploiQL
-- this file defines all tables, columns, relationships, and constraints
-- run this once to set up an empty database structure, then populate with data
-- ============================================================================
-- tables must be created in a specific order
-- if table B references table A (via foreign key), table A must exist first
-- companies -> skills -> jobs -> job_skills -> raw_postings
-- ============================================================================
-- ============================================================================
-- TABLE 1: companies
-- stores each company exactly once (normalization)
-- jobs table will reference this via foreign key
-- ============================================================================
-- "create table" tells postgresql to make a new table with the given name
-- everything inside the parentheses defines the columns

create table companies (

    -- "id" is the primary key - a unique identifier for each row
    -- "serial" is a postgresql shortcut that means:
    --   1. integer type
    --   2. auto-increment (first row gets 1, second gets 2, etc.)
    --   3. never null
    -- "primary key" means this column uniquely identifies each row
    -- no two rows can have the same id
    id serial primary key,

    -- "text" type stores strings of any length
    -- "not null" means this column cannot be empty - every company must have a name
    -- "unique" means no two companies can have the same name
    -- this prevents accidentally creating duplicate company entries
    name text not null unique,
    website text
);

-- ============================================================================
-- TABLE 2: skills
-- master list of all unique skills we've encountered
-- acts as a controlled vocabulary - "Python", "python", "Python3" all become "Python"
-- the junction table (job_skills) will connect these to jobs
-- ============================================================================

create table skills (

    id serial primary key,
    -- skill names must be unique and required
    -- normalize skill names during extraction (e.g., lowercase, standardize spelling)
    -- "PostgreSQL", "Postgres", and "psql" all become one canonical entry
    name text not null unique
);

-- ============================================================================
-- TABLE 3: jobs
-- core table storing each unique job posting
-- references companies table (many jobs belong to one company)
-- ============================================================================

create table jobs (

    id serial primary key,
    -- foreign key linking to companies table
    -- "references companies(id)" tells postgresql:
    --   1. this value must exist in companies.id (enforces data integrity)
    --   2. you cannot insert a job with company_id=99 if no company has id=99
    -- every job must belong to a company
    company_id integer not null references companies(id),

    -- job title as posted, e.g., "Senior Backend Developer"
    title text not null,

    -- full job description text
    -- for potential re-processing or full-text search later
    description text,

    -- salary range - stored as integers (annual salary in CAD)
    -- nullable because many postings don't include salary
    -- having min and max lets us handle ranges like "$80,000 - $100,000"
    salary_min integer,
    salary_max integer,

    -- job location, e.g., "Montreal", "Remote", "Hybrid - Toronto"
    location text,

    -- when the job was originally posted (not when we scraped it)
    -- "date" type stores just the date without time
    -- nullable because not all postings show their post date
    posted_date date,

    -- direct link to the job posting
    -- useful for verification or if user wants to apply
    source_url text,

    -- "timestamp" stores both date and time
    -- "default now()" automatically sets this to the current moment
    -- when a new row is inserted, so we don't have to specify it manually
    created_at timestamp default now()
);

-- ============================================================================
-- TABLE 4: job_skills (junction table)
-- solves the many-to-many relationship problem:
--   - one job requires many skills
--   - one skill is required by many jobs
-- each row represents one connection: this job requires this skill
-- ============================================================================

create table job_skills (

    -- foreign key to jobs table
    -- "on delete cascade" means: if a job is deleted, automatically delete
    -- all job_skills rows that reference it (cleanup orphaned connections)
    -- without this, deleting a job would fail if it has skills attached
    job_id integer not null references jobs(id) on delete cascade,

    -- foreign key to skills table
    -- cascade here too: if a skill is deleted, remove all its job connections
    skill_id integer not null references skills(id) on delete cascade,

    -- composite primary key: the combination of (job_id, skill_id) must be unique
    -- this prevents duplicate entries like "job 1 requires Python" appearing twice
    -- also makes lookups by this pair very fast
    primary key (job_id, skill_id)

);

-- ============================================================================
-- TABLE 5: raw_postings
-- archives everything we scrape before processing
-- multiple raw_postings can point to the same job (indeed + linkedin post same job)
-- ============================================================================

create table raw_postings (

    id serial primary key,
    -- which website we scraped this from
    -- e.g., "indeed", "linkedin", "glassdoor"
    source text not null,

    -- original url scraped
    url text not null unique,

    -- the complete html or text content as scraped
    -- storing this lets us re-extract data if our llm prompts improve
    raw_content text,

    -- when we scraped this page
    scraped_at timestamp default now(),

    -- has the llm extracted structured data from this posting yet?
    -- "default false" means new rows start as unprocessed
    -- our pipeline will flip this to true after extraction
    processed boolean default false,

    -- link to the deduplicated job this posting represents
    -- nullable because we set this AFTER processing, not during initial scrape
    -- multiple raw_postings can have the same job_id 
    -- on delete set null: if the job is deleted, don't delete this
    -- raw_posting, just clear its job_id (keep the archive)
    job_id integer references jobs(id) on delete set null

);

-- ============================================================================
-- INDEXES
-- indexes make queries faster by creating a lookup structure 
-- it jumps directly to matching rows 
-- trade-off: indexes use disk space and slow down inserts slightly
-- ============================================================================
-- speeds up queries that filter or join on company_id
-- "show all jobs from company X" or joining jobs to companies
create index idx_jobs_company_id on jobs(company_id);

-- speeds up finding jobs by location
-- "show all Montreal jobs"
create index idx_jobs_location on jobs(location);

-- speeds up the junction table lookups from both directions:
-- "what skills does this job need?" (lookup by job_id)
-- "what jobs need this skill?" (lookup by skill_id)
create index idx_job_skills_job_id on job_skills(job_id);
create index idx_job_skills_skill_id on job_skills(skill_id);

-- speeds up finding unprocessed postings
-- "get all raw_postings where processed = false"
create index idx_raw_postings_processed on raw_postings(processed);

-- speeds up finding which raw_postings belong to which job
create index idx_raw_postings_job_id on raw_postings(job_id);