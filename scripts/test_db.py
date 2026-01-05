#!/usr/bin/env python3
"""
interactive test script for db.py crud operations

run this after setup_db.sh to verify all database operations work.
also serves as examples of how to use each function.

usage: python scripts/test_db.py
"""

import sys
import os

# add src/ to path so we can import db module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from db import (
    get_cursor,
    insert_company,
    get_company_by_name,
    get_or_create_company,
    insert_skill,
    get_skill_by_name,
    get_or_create_skill,
    get_all_skills,
    insert_job,
    get_job_by_id,
    search_jobs,
    link_job_to_skill,
    link_job_to_skills,
    get_skills_for_job,
    get_top_skills,
    insert_raw_posting,
    get_unprocessed_postings,
    mark_posting_processed,
)


def print_header(text: str) -> None:
    """print a section header"""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print('='*60)


def print_success(text: str) -> None:
    """print green success message"""
    print(f"\033[1;32m✓\033[0m {text}")


def print_info(text: str) -> None:
    """print blue info message"""
    print(f"\033[1;34m→\033[0m {text}")


def cleanup_test_data() -> None:
    """remove test data from all tables"""
    print_info("cleaning up test data...")
    
    with get_cursor() as cursor:
        # delete in reverse dependency order
        # job_skills auto-deleted by cascade when jobs deleted
        cursor.execute("DELETE FROM raw_postings WHERE source = 'test'")
        cursor.execute("DELETE FROM jobs WHERE location = 'Test City'")
        cursor.execute("DELETE FROM skills WHERE name LIKE 'Test%'")
        cursor.execute("DELETE FROM companies WHERE name LIKE 'Test%'")
    
    print_success("test data cleaned up")


def test_company_operations() -> int:
    """demonstrate company crud operations"""
    print_header("COMPANY OPERATIONS")
    
    # insert a new company
    print_info("inserting new company...")
    company_id = insert_company(
        name="Test Startup Inc",
        website="https://teststartup.com"
    )
    print_success(f"created company with id={company_id}")
    
    # fetch it back
    print_info("fetching company by name...")
    company = get_company_by_name("Test Startup Inc")
    print_success(f"found: {company}")
    
    # get_or_create with existing company (should return same id)
    print_info("testing get_or_create with existing company...")
    same_id = get_or_create_company("Test Startup Inc")
    assert same_id == company_id, "should return same id for existing company"
    print_success(f"correctly returned existing id={same_id}")
    
    # get_or_create with new company
    print_info("testing get_or_create with new company...")
    new_id = get_or_create_company("Test Agency Ltd")
    assert new_id != company_id, "should create new company"
    print_success(f"created new company with id={new_id}")
    
    return company_id


def test_skill_operations() -> list[int]:
    """demonstrate skill crud operations"""
    print_header("SKILL OPERATIONS")
    
    # insert some skills
    print_info("inserting test skills...")
    skill_ids = []
    
    for skill_name in ["TestPython", "TestJavaScript", "TestSQL"]:
        skill_id = insert_skill(skill_name)
        skill_ids.append(skill_id)
        print_success(f"created skill '{skill_name}' with id={skill_id}")
    
    # fetch one back
    print_info("fetching skill by name...")
    skill = get_skill_by_name("TestPython")
    print_success(f"found: {skill}")
    
    # get all skills
    print_info("fetching all skills...")
    all_skills = get_all_skills()
    test_skills = [s for s in all_skills if s["name"].startswith("Test")]
    print_success(f"found {len(test_skills)} test skills")
    
    return skill_ids


def test_job_operations(company_id: int, skill_ids: list[int]) -> int:
    """demonstrate job crud operations"""
    print_header("JOB OPERATIONS")
    
    # insert a job
    print_info("inserting new job...")
    job_id = insert_job(
        company_id=company_id,
        title="Senior Test Engineer",
        description="We're looking for someone to write tests all day.",
        salary_min=80000,
        salary_max=120000,
        location="Test City",
        posted_date="2024-01-15",
        source_url="https://ca.indeed.com/viewjob?jk=5409096974d153f4&from=shareddesktop_copy"
    )
    print_success(f"created job with id={job_id}")
    
    # fetch with company name joined
    print_info("fetching job with company name...")
    job = get_job_by_id(job_id)
    print_success(f"found job at '{job['company_name']}': {job['title']}")
    print(f"         salary: ${job['salary_min']:,} - ${job['salary_max']:,}")
    
    # search jobs
    print_info("searching jobs by location...")
    results = search_jobs(location="Test")
    print_success(f"found {len(results)} jobs in 'Test' locations")
    
    print_info("searching jobs by title...")
    results = search_jobs(title_contains="Engineer")
    print_success(f"found {len(results)} jobs with 'Engineer' in title")
    
    return job_id


def test_job_skills_operations(job_id: int, skill_ids: list[int]) -> None:
    """demonstrate junction table operations"""
    print_header("JOB_SKILLS OPERATIONS")
    
    # link job to skills individually
    print_info("linking job to skills one by one...")
    for skill_id in skill_ids[:2]:  # link first two
        link_job_to_skill(job_id, skill_id)
    print_success(f"linked job to {len(skill_ids[:2])} skills")
    
    # get skills for job
    print_info("fetching skills for job...")
    job_skills = get_skills_for_job(job_id)
    print_success(f"job requires: {[s['name'] for s in job_skills]}")
    
    # link multiple skills by name (including one that already exists)
    print_info("linking job to skills by name (batch)...")
    link_job_to_skills(job_id, ["TestSQL", "TestDocker", "TestKubernetes"])
    
    # verify new skills were created and linked
    job_skills = get_skills_for_job(job_id)
    print_success(f"job now requires: {[s['name'] for s in job_skills]}")
    
    # get top skills
    print_info("getting top skills across all jobs...")
    top = get_top_skills(5)
    if top:
        for skill in top:
            print(f"         {skill['name']}: {skill['job_count']} job(s)")
    else:
        print("(no skills linked to jobs yet)")


def test_raw_posting_operations(job_id: int) -> None:
    """demonstrate raw_postings workflow"""
    print_header("RAW_POSTINGS OPERATIONS")
    
    # simulate scraping: insert raw posting
    print_info("inserting raw posting (simulating scrape)...")
    raw_id = insert_raw_posting(
        source="test",
        url="https://emplois.ca.indeed.com/viewjob?jk=7104d67493856063&from=shareddesktop_copy",
        raw_content="<html><body>Senior Test Engineer wanted...</body></html>"
    )
    print_success(f"created raw_posting with id={raw_id}")
    
    # check unprocessed queue
    print_info("checking unprocessed postings queue...")
    unprocessed = get_unprocessed_postings(limit=10)
    test_postings = [p for p in unprocessed if p["source"] == "test"]
    print_success(f"found {len(test_postings)} unprocessed test posting(s)")
    
    # mark as processed (simulating LLM extraction completed)
    print_info("marking posting as processed...")
    mark_posting_processed(raw_id, job_id)
    print_success(f"linked raw_posting {raw_id} to job {job_id}")
    
    # verify it's no longer in unprocessed queue
    unprocessed = get_unprocessed_postings(limit=10)
    test_postings = [p for p in unprocessed if p["source"] == "test"]
    print_success(f"unprocessed queue now has {len(test_postings)} test posting(s)")


def test_parameterized_query_safety() -> None:
    """demonstrate why parameterized queries matter"""
    print_header("PARAMETERIZED QUERY SAFETY")
    
    # this is what a sql injection attack looks like
    malicious_input = "'; DROP TABLE companies; --"
    
    print_info(f"testing with malicious input: {malicious_input}")
    
    # safe: parameterized query treats input as data, not code
    result = get_company_by_name(malicious_input)
    
    if result is None:
        print_success("parameterized query safely returned None (no match)")
        print("         the malicious input was treated as a literal string")
        print("         NOT executed as sql code - your tables are safe!")
    else:
        print_success(f"found company: {result}")


def main():
    """run all tests"""
    print("\n" + "=" * 60)
    print("EmploiQL Database Operations Test")
    print("=" * 60)
    
    try:
        # run tests in dependency order
        company_id = test_company_operations()
        skill_ids = test_skill_operations()
        job_id = test_job_operations(company_id, skill_ids)
        test_job_skills_operations(job_id, skill_ids)
        test_raw_posting_operations(job_id)
        test_parameterized_query_safety()
        
        # clean up
        print_header("CLEANUP")
        cleanup_test_data()
        
        print("\n" + "=" * 60)
        print_success("all database operations working correctly!")
        print("=" * 60 + "\n")
        
    except Exception as error:
        print(f"\n\033[1;31mERROR:\033[0m {error}")
        print("\nmake sure you've run:")
        print("  1. ./scripts/setup_db.sh")
        print("  2. python scripts/test_schema.py")
        sys.exit(1)


if __name__ == "__main__":
    main()