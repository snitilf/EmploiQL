# schema testing

quick docs on how `scripts/test_schema.py` works and why each test matters.

## what it does

validates that schema.sql created everything correctly - tables, constraints, indexes. run it after `setup_db.sh` to catch issues before writing real code against the database.

```bash
python scripts/test_schema.py
```

## the tests

### 1. tables exist

queries `information_schema.tables` which is postgresql's built-in metadata. every database has this - it's how you ask "what tables do i have?" programmatically.

```sql
select table_name 
from information_schema.tables 
where table_schema = 'public'
```

`table_schema = 'public'` filters out system tables (pg_catalog stuff). we only care about our 5 tables.

### 2. insert operations

inserts test data in the correct order: companies → skills → jobs → job_skills → raw_postings. this order matters because of foreign keys - can't reference a company_id that doesn't exist yet.

uses `RETURNING id` to get back the auto-generated serial id immediately after insert, which we need for the next insert.

### 3. foreign key enforcement

tries to insert a job with `company_id = 99999` (doesn't exist). this *should* fail - that's the whole point of foreign keys. if it succeeds, something's wrong with the schema.

catches `psycopg2.errors.ForeignKeyViolation` specifically. after any postgres error, the transaction is aborted and you have to call `connection.rollback()` before doing anything else.

### 4. unique constraints

tries inserting two companies with the same name. second insert should fail with `UniqueViolation`. this validates that `name text not null unique` is actually enforced.

### 5. cascade delete

tests `on delete cascade` on job_skills. workflow:
1. insert a job + skill + job_skills row linking them
2. delete the job
3. check if job_skills row is gone automatically

if cascade works, count goes from 1 → 0 without explicitly deleting from job_skills.

### 6. indexes exist

queries `pg_indexes` (another system table) to verify all 6 indexes were created. indexes don't affect correctness but they're critical for query performance - worth verifying they exist.

## transaction handling

each test either commits (success) or rolls back (failure). this keeps the database in a clean state between tests. at the end, `cleanup_test_data()` deletes everything so the database is empty for actual use.

## error handling pattern

```python
try:
    cursor.execute("bad query that should fail")
    print("ERROR - should have failed")
    return False
except psycopg2.errors.SomeSpecificError:
    print("good - constraint worked")
    cursor.connection.rollback()  # required after any error
    return True
```

this pattern is useful anywhere you need to test that constraints are working.