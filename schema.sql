-- run once to create empty tables, then populate with data
-- creation order matters: parent tables before children (foreign key dependencies)

-- companies: stores each company once (jobs reference this via foreign key)
create table companies (
    -- serial = auto-incrementing integer, primary key = unique row identifier
    id serial primary key,
    -- unique prevents duplicate company entries
    name text not null unique,
    website text
);

-- skills: master list of normalized skill names ("Python", not "python3")
-- junction table (job_skills) connects these to jobs
create table skills (
    id serial primary key,
    name text not null unique
);

-- jobs: each unique job posting, linked to one company
create table jobs (
    id serial primary key,
    -- references = foreign key, value must exist in companies.id
    company_id integer not null references companies(id),
    title text not null,
    description text,
    -- salary nullable because many postings don't include it
    salary_min integer,
    salary_max integer,
    location text,
    -- date = just date, no time component
    posted_date date,
    source_url text,
    -- default now() = auto-set to current timestamp on insert
    created_at timestamp default now()
);

-- job_skills: junction table for many-to-many (job <-> skill) relationship
-- each row = "this job requires this skill"
create table job_skills (
    -- on delete cascade = if parent row deleted, delete this row too
    job_id integer not null references jobs(id) on delete cascade,
    skill_id integer not null references skills(id) on delete cascade,
    -- composite primary key = (job_id, skill_id) pair must be unique
    primary key (job_id, skill_id)
);

-- raw_postings: archive of scraped content before LLM processing
-- multiple raw_postings can point to same job (indeed + linkedin same posting)
create table raw_postings (
    id serial primary key,
    -- which site: "indeed", "linkedin", etc.
    source text not null,
    url text not null unique,
    -- keep raw html/text for re-extraction if prompts improve
    raw_content text,
    scraped_at timestamp default now(),
    -- pipeline flips to true after LLM extraction
    processed boolean default false,
    -- set after processing, nullable until then
    -- on delete set null = keep archive even if job deleted
    job_id integer references jobs(id) on delete set null
);

-- indexes: speed up queries by creating lookup structures
-- trade-off: faster reads, slightly slower writes, more disk space

-- filter/join on company_id
create index idx_jobs_company_id on jobs(company_id);
-- filter by location ("show montreal jobs")
create index idx_jobs_location on jobs(location);
-- junction table lookups from both directions
create index idx_job_skills_job_id on job_skills(job_id);
create index idx_job_skills_skill_id on job_skills(skill_id);
-- find unprocessed postings quickly
create index idx_raw_postings_processed on raw_postings(processed);
-- find which raw_postings belong to which job
create index idx_raw_postings_job_id on raw_postings(job_id);