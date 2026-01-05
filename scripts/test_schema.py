#!/usr/bin/env python3
"""
validates schema.sql is properly configured

tests:
1. all 5 tables exist and are accessible
2. insert operations work (respecting foreign key order)
3. foreign key relationships are enforced
4. unique constraints prevent duplicates
5. cascade deletes work correctly
6. indexes exist and are usable

run after setup_db.sh to verify everything is wired up correctly
"""

import sys
import os

# add src directory to python's module search path
# allows import from src/db.py regardless of where script is ran
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import psycopg2
from db import get_connection


def print_status(message: str) -> None:
    """print a blue status message"""
    # \033[1;34m = bold blue, \033[0m = reset to default
    print(f"\033[1;34m==>\033[0m {message}")


def print_success(message: str) -> None:
    """print a green success message"""
    print(f"\033[1;32m✓\033[0m {message}")


def print_error(message: str) -> None:
    """print a red error message"""
    print(f"\033[1;31m✗\033[0m {message}")


def test_tables_exist(cursor) -> bool:
    """verify all 5 expected tables are present in the database"""
    print_status("checking all tables exist...")
    
    # information_schema is a built-in postgresql schema containing metadata
    # about all database objects. table_name column lists all table names.
    # table_schema = 'public' filters to only user-created tables
    # (excludes system tables in pg_catalog, etc.)
    cursor.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
        ORDER BY table_name
    """)
    
    # fetchall() returns list of tuples, each tuple is one row
    # [(companies,), (jobs,), ...] -> extract first element of each
    found_tables = [row[0] for row in cursor.fetchall()]
    
    expected_tables = ["companies", "job_skills", "jobs", "raw_postings", "skills"]
    
    if found_tables == expected_tables:
        print_success(f"all 5 tables found: {', '.join(found_tables)}")
        return True
    else:
        print_error(f"expected {expected_tables}, found {found_tables}")
        return False


def test_insert_operations(cursor) -> bool:
    """test that we can insert data respecting foreign key order"""
    print_status("testing insert operations...")
    
    try:
        # step 1: insert into parent tables first (no foreign key dependencies)
        # RETURNING id gives us back the auto-generated serial id
        cursor.execute("""
            INSERT INTO companies (name, website) 
            VALUES ('Test Corp', 'https://testcorp.com')
            RETURNING id
        """)
        # fetchone() returns single row as tuple, [0] extracts id value
        company_id = cursor.fetchone()[0]
        print_success(f"inserted company with id={company_id}")
        
        cursor.execute("""
            INSERT INTO skills (name) 
            VALUES ('Python')
            RETURNING id
        """)
        skill_id = cursor.fetchone()[0]
        print_success(f"inserted skill with id={skill_id}")
        
        # step 2: insert into jobs (depends on companies existing first)
        cursor.execute("""
            INSERT INTO jobs (company_id, title, description, location) 
            VALUES (%s, 'Software Engineer', 'Build cool stuff', 'Montreal')
            RETURNING id
        """, (company_id,))  # %s placeholder, tuple provides the value
        job_id = cursor.fetchone()[0]
        print_success(f"inserted job with id={job_id}")
        
        # step 3: insert into junction table (depends on both jobs and skills)
        cursor.execute("""
            INSERT INTO job_skills (job_id, skill_id) 
            VALUES (%s, %s)
        """, (job_id, skill_id))
        print_success("inserted job_skills relationship")
        
        # step 4: insert raw_posting (can reference job_id)
        cursor.execute("""
            INSERT INTO raw_postings (source, url, raw_content, job_id) 
            VALUES ('indeed', 'https://indeed.com/job/123', '<html>...</html>', %s)
            RETURNING id
        """, (job_id,))
        raw_posting_id = cursor.fetchone()[0]
        print_success(f"inserted raw_posting with id={raw_posting_id}")
        
        return True
        
    except psycopg2.Error as error:
        print_error(f"insert failed: {error}")
        return False


def test_foreign_key_enforcement(cursor) -> bool:
    """verify that foreign keys reject invalid references"""
    print_status("testing foreign key constraints...")
    
    try:
        # try inserting a job with a company_id that doesn't exist
        # should fail
        cursor.execute("""
            INSERT INTO jobs (company_id, title) 
            VALUES (99999, 'Ghost Job')
        """)
        # if we reach here, constraint didn't work
        print_error("foreign key constraint NOT enforced - insert should have failed")
        return False
        
    except psycopg2.errors.ForeignKeyViolation:
        # this is the expected behavior - constraint caught the bad insert
        print_success("foreign key constraint enforced correctly")
        # clear the error state so we can continue using the cursor
        # when an error occurs in postgresql, the transaction is aborted
        # we need to rollback to reset it
        cursor.connection.rollback()
        return True
        
    except psycopg2.Error as error:
        print_error(f"unexpected error: {error}")
        return False


def test_unique_constraints(cursor) -> bool:
    """verify that unique constraints prevent duplicate entries"""
    print_status("testing unique constraints...")
    
    try:
        # first insert should work
        cursor.execute("""
            INSERT INTO companies (name, website) 
            VALUES ('Unique Test Corp', 'https://unique.com')
        """)
        
        # second insert with same name SHOULD fail
        cursor.execute("""
            INSERT INTO companies (name, website) 
            VALUES ('Unique Test Corp', 'https://different.com')
        """)
        
        print_error("unique constraint NOT enforced - duplicate insert should have failed")
        return False
        
    except psycopg2.errors.UniqueViolation:
        print_success("unique constraint enforced correctly")
        cursor.connection.rollback()
        return True
        
    except psycopg2.Error as error:
        print_error(f"unexpected error: {error}")
        return False


def test_cascade_delete(cursor) -> bool:
    """verify that deleting a job also deletes its job_skills entries"""
    print_status("testing cascade delete on job_skills...")
    
    try:
        # set up test data
        cursor.execute("""
            INSERT INTO companies (name) VALUES ('Cascade Test Corp')
            RETURNING id
        """)
        company_id = cursor.fetchone()[0]
        
        cursor.execute("""
            INSERT INTO skills (name) VALUES ('TestSkill')
            RETURNING id
        """)
        skill_id = cursor.fetchone()[0]
        
        cursor.execute("""
            INSERT INTO jobs (company_id, title) VALUES (%s, 'Cascade Test Job')
            RETURNING id
        """, (company_id,))
        job_id = cursor.fetchone()[0]
        
        cursor.execute("""
            INSERT INTO job_skills (job_id, skill_id) VALUES (%s, %s)
        """, (job_id, skill_id))
        
        # verify the job_skills row exists
        cursor.execute("""
            SELECT COUNT(*) FROM job_skills WHERE job_id = %s
        """, (job_id,))
        count_before = cursor.fetchone()[0]
        
        # now delete the job
        cursor.execute("DELETE FROM jobs WHERE id = %s", (job_id,))
        
        # check if job_skills row was automatically deleted
        cursor.execute("""
            SELECT COUNT(*) FROM job_skills WHERE job_id = %s
        """, (job_id,))
        count_after = cursor.fetchone()[0]
        
        if count_before == 1 and count_after == 0:
            print_success("cascade delete worked - job_skills row automatically removed")
            return True
        else:
            print_error(f"cascade delete failed: before={count_before}, after={count_after}")
            return False
            
    except psycopg2.Error as error:
        print_error(f"cascade delete test failed: {error}")
        return False


def test_indexes_exist(cursor) -> bool:
    """verify all expected indexes were created"""
    print_status("checking indexes exist...")
    
    # pg_indexes is a postgresql system view that lists all indexes
    # indexname column contains the name we gave each index in schema.sql
    cursor.execute("""
        SELECT indexname 
        FROM pg_indexes 
        WHERE schemaname = 'public'
        AND indexname LIKE 'idx_%'
        ORDER BY indexname
    """)
    
    found_indexes = [row[0] for row in cursor.fetchall()]
    
    expected_indexes = [
        "idx_job_skills_job_id",
        "idx_job_skills_skill_id", 
        "idx_jobs_company_id",
        "idx_jobs_location",
        "idx_raw_postings_job_id",
        "idx_raw_postings_processed"
    ]
    
    if found_indexes == expected_indexes:
        print_success(f"all {len(found_indexes)} indexes found")
        return True
    else:
        missing = set(expected_indexes) - set(found_indexes)
        extra = set(found_indexes) - set(expected_indexes)
        if missing:
            print_error(f"missing indexes: {missing}")
        if extra:
            print_error(f"unexpected indexes: {extra}")
        return False


def cleanup_test_data(cursor) -> None:
    """remove all test data to leave database clean"""
    print_status("cleaning up test data...")
    
    # delete in reverse order of dependencies
    # job_skills deleted automatically via cascade when jobs deleted
    cursor.execute("DELETE FROM raw_postings")
    cursor.execute("DELETE FROM jobs")
    cursor.execute("DELETE FROM skills")
    cursor.execute("DELETE FROM companies")
    
    print_success("test data cleaned up")


def main():
    """run all schema tests"""
    print("\n" + "=" * 50)
    print("EmploiQL Schema Validation")
    print("=" * 50 + "\n")
    
    try:
        connection = get_connection()
        # cursor is like a pointer that lets us execute sql and fetch results
        cursor = connection.cursor()
        
        # track test results
        all_passed = True
        tests_run = 0
        tests_passed = 0
        
        # run each test
        test_functions = [
            test_tables_exist,
            test_insert_operations,
            test_foreign_key_enforcement,
            test_unique_constraints,
            test_cascade_delete,
            test_indexes_exist,
        ]
        
        for test_function in test_functions:
            tests_run += 1
            # each test returns True if passed, False if failed
            if test_function(cursor):
                tests_passed += 1
                # commit successful test data so next test can use it
                connection.commit()
            else:
                all_passed = False
                # rollback failed transaction to reset state
                connection.rollback()
        
        # clean up after all tests
        print()
        cleanup_test_data(cursor)
        connection.commit()
        
        # final summary
        print("\n" + "=" * 50)
        if all_passed:
            print_success(f"all {tests_passed}/{tests_run} tests passed")
            print("schema is correctly configured")
        else:
            print_error(f"only {tests_passed}/{tests_run} tests passed")
            print("review the errors above and check schema.sql")
        print("=" * 50 + "\n")
        
        cursor.close()
        connection.close()
        
        # exit with appropriate code for scripts/CI
        # 0 = success, 1 = failure 
        sys.exit(0 if all_passed else 1)
        
    except psycopg2.OperationalError as error:
        print_error(f"could not connect to database: {error}")
        print("\nmake sure you've run: ./scripts/setup_db.sh")
        sys.exit(1)


if __name__ == "__main__":
    main()  