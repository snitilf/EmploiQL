# fetch job postings from JSearch API (via RapidAPI)
# focused on montreal tech internships
# uses caching to preserve free API quota (200 requests/month)
import config
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

# internship search presets - saves API quota by having go-to queries
# each preset maps to a search query optimized for montreal internships
INTERNSHIP_PRESETS = {
    "software": {
        "query": "software engineer intern",
        "description": "Software engineering internships"
    },
    "developer": {
        "query": "software developer intern",
        "description": "Software developer internships"
    },
    "devops": {
        "query": "devops intern",
        "description": "DevOps and cloud infrastructure internships"
    },
    "data": {
        "query": "data science intern",
        "description": "Data science and analytics internships"
    },
    "cyber": {
        "query": "cybersecurity intern",
        "description": "Cybersecurity and security engineering internships"
    },
    "frontend": {
        "query": "frontend developer intern",
        "description": "Frontend/UI development internships"
    },
    "backend": {
        "query": "backend developer intern",
        "description": "Backend development internships"
    },
    "fullstack": {
        "query": "full stack developer intern",
        "description": "Full-stack development internships"
    },
    "ml": {
        "query": "machine learning intern",
        "description": "Machine learning and AI internships"
    },
    "qa": {
        "query": "QA engineer intern",
        "description": "Quality assurance and testing internships"
    },
    # canadian banks and financial institutions
    "rbc": {
        "query": "RBC intern technology",
        "description": "RBC tech internships"
    },
    "td": {
        "query": "TD Bank intern technology",
        "description": "TD Bank tech internships"
    },
    "bmo": {
        "query": "BMO intern technology",
        "description": "BMO tech internships"
    },
    "scotiabank": {
        "query": "Scotiabank intern technology",
        "description": "Scotiabank tech internships"
    },
    "cibc": {
        "query": "CIBC intern technology",
        "description": "CIBC tech internships"
    },
    "national": {
        "query": "National Bank Canada intern technology",
        "description": "National Bank tech internships"
    },
    "desjardins": {
        "query": "Desjardins intern technology",
        "description": "Desjardins tech internships"
    },
    "manulife": {
        "query": "Manulife intern technology",
        "description": "Manulife tech internships"
    },
    "sunlife": {
        "query": "Sun Life intern technology",
        "description": "Sun Life tech internships"
    }
}

# default location focused on montreal
DEFAULT_LOCATION = "Montreal, Canada"


def search_jobs(
    query: str = "software developer intern",
    location: str = DEFAULT_LOCATION,
    num_pages: int = 1,
    use_cache: bool = True
) -> list[dict]:
    """
    search for internships via JSearch API.
    
    args:
        query: job title or keywords (e.g., "software engineer intern")
        location: city/country to search (default: Montreal, Canada)
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
        print(f"Loading from cache: {cache_file.name}")
        with open(cache_file, "r") as f:
            cached = json.load(f)
        print(f"   Found {len(cached['jobs'])} jobs (cached {cached['fetched_at']})")
        return cached["jobs"]
    
    # no cache or use_cache=False — make live API call
    if not RAPIDAPI_KEY:
        print("Error: RAPIDAPI_KEY environment variable not set")
        print("Run: export RAPIDAPI_KEY='your-key-here'")
        print("get your free key at: https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch")
        return []
    
    print(f"   Fetching from JSearch API...")
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
    print(f"  Saved {len(all_jobs)} jobs to cache: {cache_file.name}")
    
    return all_jobs


def search_preset(
    preset: str,
    location: str = DEFAULT_LOCATION,
    num_pages: int = 1,
    use_cache: bool = True
) -> list[dict]:
    """
    search using a preset internship category.
    
    args:
        preset: one of the keys in INTERNSHIP_PRESETS (software, devops, cyber, etc.)
        location: city/country (default: Montreal)
        num_pages: pages to fetch
        use_cache: load from cache if available
    
    returns:
        list of job dictionaries
    """
    if preset not in INTERNSHIP_PRESETS:
        print(f"Unknown preset: {preset}")
        print(f"Available: {', '.join(INTERNSHIP_PRESETS.keys())}")
        return []
    
    config = INTERNSHIP_PRESETS[preset]
    print(f"Using preset: {config['description']}")
    
    return search_jobs(
        query=config["query"],
        location=location,
        num_pages=num_pages,
        use_cache=use_cache
    )


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
        "date_posted": "week",  # jobs from last month
        # employment_types filter for internships when available
        # some postings don't have this field properly set, so we rely on query terms
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
    this bridges JSearch -> extraction.py pipeline.
    
    jsearch gives us structured data already, but we'll still run it
    through extraction.py for consistency and skill normalization.
    """
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


def list_presets() -> None:
    """print all available internship presets."""
    print("\nAvailable Internship Presets:")
    print("-" * 50)
    for name, config in INTERNSHIP_PRESETS.items():
        print(f"  {name:12} - {config['description']}")
    print()
    print("Usage: python src/jsearch.py --preset software --live")


# CLI for fetching internship data
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Fetch Montreal tech internships from JSearch API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --preset software --live     # fetch software engineering internships
  %(prog)s --preset devops --live       # fetch devops internships
  %(prog)s --query "python intern"      # custom search (from cache)
  %(prog)s --list-presets               # show all preset categories
  %(prog)s --list-cache                 # show cached searches
        """
    )
    
    parser.add_argument("--live", action="store_true", 
                        help="Make live API call (default: use cache)")
    parser.add_argument("--query", "-q", default=None,
                        help="Custom job search query")
    parser.add_argument("--preset", "-p", choices=list(INTERNSHIP_PRESETS.keys()),
                        help="Use a preset internship category")
    parser.add_argument("--location", "-l", default=DEFAULT_LOCATION,
                        help=f"Location to search (default: {DEFAULT_LOCATION})")
    parser.add_argument("--pages", type=int, default=1,
                        help="Number of pages (10 jobs each, 1 API call each)")
    parser.add_argument("--list-cache", action="store_true",
                        help="List cached searches")
    parser.add_argument("--list-presets", action="store_true",
                        help="List available internship presets")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("EmploiQL - JSearch Internship Fetcher")
    print("=" * 60)
    
    if args.list_presets:
        list_presets()
    
    elif args.list_cache:
        cached = list_cache()
        if cached:
            print(f"\nCached searches ({len(cached)}):")
            for c in cached:
                print(f"   • {c}")
            print(f"\Load with: python3 scripts/load_jsearch.py --query '...'")
        else:
            print("\nNo cached searches yet")
            print("   Run with --live to fetch jobs")
            print("   Example: python3 src/jsearch.py --preset software --live")
    
    elif args.preset:
        # use preset category
        jobs = search_preset(
            preset=args.preset,
            location=args.location,
            num_pages=args.pages,
            use_cache=not args.live
        )
    
    elif args.query:
        # custom search
        jobs = search_jobs(
            query=args.query,
            location=args.location,
            num_pages=args.pages,
            use_cache=not args.live
        )
    
    else:
        # no query specified - show help
        print("\nNo search specified. Use --preset or --query")
        print()
        list_presets()
        print("Or try: python3 src/jsearch.py --preset software --live")


def _print_sample(jobs: list[dict]) -> None:
    """print a sample job and next steps."""
    if not jobs:
        return
    
    print(f"\nFound {len(jobs)} jobs")
    print("\nSample job:")
    print("-" * 40)
    sample = jobs[0]
    print(f"Title:    {sample.get('job_title')}")
    print(f"Company:  {sample.get('employer_name')}")
    print(f"Location: {sample.get('job_city')}, {sample.get('job_state')}")
    print(f"Type:     {sample.get('job_employment_type')}")
    print(f"Salary:   {_format_salary(sample)}")
    url = sample.get('job_apply_link', 'N/A')
    print(f"URL:      {url[:60]}..." if len(url) > 60 else f"URL:      {url}")
    
    print(f"\nNext steps:")
    print(f"   Load into database: python3 scripts/load_jsearch.py")
    print(f"   Query with CLI:     python3 src/cli.py")
