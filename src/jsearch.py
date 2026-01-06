# fetch job postings from JSearch API (via RapidAPI)
# uses caching to preserve free API quota (200 requests/month)

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

import requests

# load API key from environment variable (don't hardcode!)
# set with: export RAPIDAPI_KEY='your-key-here'
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = "jsearch.p.rapidapi.com"

# cache directory for storing API responses
CACHE_DIR = Path(__file__).parent.parent / "data" / "jsearch_cache"


def search_jobs(
    query: str = "software developer",
    location: str = "Montreal, Canada",
    num_pages: int = 1,
    use_cache: bool = True
) -> list[dict]:
    """
    search for jobs via JSearch API.
    
    args:
        query: job title or keywords (e.g., "python developer", "data scientist")
        location: city/country to search
        num_pages: pages to fetch (10 jobs per page). careful - each page = 1 API call!
        use_cache: if True, load from cache instead of making API call
    
    returns:
        list of job dictionaries from JSearch
    """
    # create cache filename from search params
    cache_key = f"{query}_{location}_{num_pages}".replace(" ", "_").replace(",", "").lower()
    cache_file = CACHE_DIR / f"{cache_key}.json"
    
    # try loading from cache first
    if use_cache and cache_file.exists():
        print(f"📁 Loading from cache: {cache_file.name}")
        with open(cache_file, "r") as f:
            cached = json.load(f)
        print(f"   Found {len(cached['jobs'])} jobs (cached {cached['fetched_at']})")
        return cached["jobs"]
    
    # no cache or use_cache=False — make live API call
    if not RAPIDAPI_KEY:
        print("Error: RAPIDAPI_KEY environment variable not set")
        print("Run: export RAPIDAPI_KEY='your-key-here'")
        return []
    
    print(f"Fetching from JSearch API...")
    print(f"   Query: '{query}' in '{location}'")
    print(f"   Pages: {num_pages} (≈{num_pages * 10} jobs, costs {num_pages} API calls)")
    
    all_jobs = []
    
    for page in range(1, num_pages + 1):
        jobs = _fetch_page(query, location, page)
        all_jobs.extend(jobs)
        print(f"   Page {page}: got {len(jobs)} jobs")
    
    # save to cache for future use
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_data = {
        "query": query,
        "location": location,
        "fetched_at": datetime.now().isoformat(),
        "jobs": all_jobs
    }
    with open(cache_file, "w") as f:
        json.dump(cache_data, f, indent=2)
    print(f"💾 Saved {len(all_jobs)} jobs to cache: {cache_file.name}")
    
    return all_jobs


def _fetch_page(query: str, location: str, page: int = 1) -> list[dict]:
    """
    fetch a single page of results from JSearch.
    internal function - use search_jobs() instead.
    """
    url = "https://jsearch.p.rapidapi.com/search"
    
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }
    
    params = {
        "query": f"{query} in {location}",
        "page": page,
        "num_pages": 1,
        "country": "ca",  # canada
        "date_posted": "month"  # jobs from last month
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print(f"API error: {response.status_code}")
        print(f"   {response.text[:200]}")
        return []
    
    data = response.json()
    return data.get("data", [])


def jsearch_to_raw_posting(job: dict) -> dict:
    """
    convert JSearch job format to our raw_posting format.
    this bridges JSearch → extraction.py pipeline.
    
    jsearch gives us structured data already, but we'll still run it
    through extraction.py for consistency and skill normalization.
    """
    # build a text blob similar to what we'd scrape from Indeed/LinkedIn
    # extraction.py expects raw text, not structured data
    
    description = job.get("job_description", "")
    
    # construct raw content like a scraped posting
    raw_content = f"""
Job Title: {job.get('job_title', 'Unknown')}
Company: {job.get('employer_name', 'Unknown')}
Location: {job.get('job_city', '')}, {job.get('job_state', '')} {job.get('job_country', '')}
Employment Type: {job.get('job_employment_type', '')}
Posted: {job.get('job_posted_at_datetime_utc', '')}

Salary: {_format_salary(job)}

Description:
{description}

Required Skills/Qualifications:
{job.get('job_highlights', {}).get('Qualifications', ['Not specified'])}
"""
    
    return {
        "source": "jsearch",
        "url": job.get("job_apply_link") or job.get("job_google_link", ""),
        "raw_content": raw_content.strip(),
        "employer_name": job.get("employer_name"),  # bonus: pre-extracted
        "job_title": job.get("job_title"),  # bonus: pre-extracted
    }


def _format_salary(job: dict) -> str:
    """format salary info from jsearch data."""
    min_sal = job.get("job_min_salary")
    max_sal = job.get("job_max_salary")
    currency = job.get("job_salary_currency", "CAD")
    period = job.get("job_salary_period", "")
    
    if min_sal and max_sal:
        return f"${min_sal:,.0f} - ${max_sal:,.0f} {currency} {period}"
    elif min_sal:
        return f"${min_sal:,.0f}+ {currency} {period}"
    elif max_sal:
        return f"Up to ${max_sal:,.0f} {currency} {period}"
    else:
        return "Not specified"


def list_cache() -> list[str]:
    """show all cached search results."""
    if not CACHE_DIR.exists():
        return []
    return [f.name for f in CACHE_DIR.glob("*.json")]


# CLI for testing 
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Fetch jobs from JSearch API")
    parser.add_argument("--live", action="store_true", 
                        help="Make live API call (default: use cache)")
    parser.add_argument("--query", "-q", default="software developer",
                        help="Job search query")
    parser.add_argument("--location", "-l", default="Montreal, Canada",
                        help="Location to search")
    parser.add_argument("--pages", "-p", type=int, default=1,
                        help="Number of pages (10 jobs each, 1 API call each)")
    parser.add_argument("--list-cache", action="store_true",
                        help="List cached searches")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("JSearch API Client")
    print("=" * 60)
    
    if args.list_cache:
        cached = list_cache()
        if cached:
            print(f"\n Cached searches ({len(cached)}):")
            for c in cached:
                print(f"   • {c}")
        else:
            print("\n No cached searches yet")
            print("   Run with --live to fetch jobs")
    else:
        # fetch jobs (from cache or live)
        jobs = search_jobs(
            query=args.query,
            location=args.location,
            num_pages=args.pages,
            use_cache=not args.live  # --live means don't use cache
        )
        
        if jobs:
            print(f"\n Sample job:")
            print("-" * 40)
            sample = jobs[0]
            print(f"Title:    {sample.get('job_title')}")
            print(f"Company:  {sample.get('employer_name')}")
            print(f"Location: {sample.get('job_city')}, {sample.get('job_state')}")
            print(f"Type:     {sample.get('job_employment_type')}")
            print(f"Salary:   {_format_salary(sample)}")
            print(f"URL:      {sample.get('job_apply_link', 'N/A')[:60]}...")
            
            print(f"\n Next steps:")
            print(f"   1. Run extraction: python scripts/load_jsearch.py")
            print(f"   2. Query with SQL: python src/cli.py")