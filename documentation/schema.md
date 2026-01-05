# schema documentation

## overview

the database has 5 tables designed to store job postings without duplicating data. the main idea is normalization — each piece of information lives in one place only.

```
companies ──────────────┐
                        ▼
raw_postings ────────► jobs ◄────── job_skills ────► skills
```

## tables

### companies
stores each company once. jobs reference this via `company_id`.

| column | type | notes |
|--------|------|-------|
| id | serial | auto-increment primary key |
| name | text | unique, required |
| website | text | optional |

### jobs
the core table. each row is one unique job posting.

| column | type | notes |
|--------|------|-------|
| id | serial | primary key |
| company_id | integer | foreign key → companies.id |
| title | text | required |
| description | text | full posting text |
| salary_min/max | integer | nullable, annual CAD |
| location | text | "montreal", "remote", etc |
| posted_date | date | when job was posted |
| source_url | text | link to original posting |
| created_at | timestamp | auto-set on insert |

### skills
master list of normalized skill names. "python3" and "Python" both become "Python" during extraction.

| column | type | notes |
|--------|------|-------|
| id | serial | primary key |
| name | text | unique, required |

### job_skills (junction table)
solves the many-to-many problem: one job needs many skills, one skill appears in many jobs. each row = "this job requires this skill".

| column | type | notes |
|--------|------|-------|
| job_id | integer | foreign key → jobs.id, cascades on delete |
| skill_id | integer | foreign key → skills.id, cascades on delete |

primary key is the combo of (job_id, skill_id) so you can't have duplicates.

### raw_postings
archives everything scraped before processing. multiple raw_postings can point to the same job — this handles deduplication when indeed and linkedin post the same job.

| column | type | notes |
|--------|------|-------|
| id | serial | primary key |
| source | text | "indeed", "linkedin", etc |
| url | text | unique |
| raw_content | text | original html/text |
| scraped_at | timestamp | auto-set |
| processed | boolean | default false, flipped after extraction |
| job_id | integer | nullable fk → jobs.id, set after deduplication |

## indexes

indexes speed up queries by creating lookup structures. without them, postgres scans every row.

- `idx_jobs_company_id` — fast joins between jobs and companies
- `idx_jobs_location` — fast filtering by location
- `idx_job_skills_job_id` — "what skills does this job need?"
- `idx_job_skills_skill_id` — "what jobs need this skill?"
- `idx_raw_postings_processed` — find unprocessed postings quickly
- `idx_raw_postings_job_id` — link raw postings to jobs

## key relationships

- `jobs.company_id` → `companies.id` (many jobs belong to one company)
- `job_skills.job_id` → `jobs.id` (many-to-many bridge)
- `job_skills.skill_id` → `skills.id` (many-to-many bridge)
- `raw_postings.job_id` → `jobs.id` (many raw postings can map to one deduplicated job)

## cascade behavior

- deleting a job removes its job_skills rows automatically (`on delete cascade`)
- deleting a job sets raw_postings.job_id to null (`on delete set null`) — keeps the archive