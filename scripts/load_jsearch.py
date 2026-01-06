# load JSearch jobs into EmploiQL database
# bridges: JSearch cache → extraction.py → database

import sys
from pathlib import Path

# add src to path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rich.console import Console
from rich.table import Table

from jsearch import search_jobs, jsearch_to_raw_posting, list_cache
from extraction import extract_job_data
from db import (
    get_cursor,
    insert_raw_posting,
    get_or_create_company,
    insert_job,
    link_job_to_skills,
    mark_posting_processed
)

console = Console()


def load_jobs_to_database(
    query: str = "software developer",
    location: str = "Montreal, Canada",
    use_cache: bool = True,
    use_mock_extraction: bool = False,
    limit: int = None
):
    """
    full pipeline: JSearch → extraction → database.
    
    args:
        query: search query (must match a cached search if use_cache=True)
        location: location (must match cached search)
        use_cache: load from JSearch cache (default True to save API quota)
        use_mock_extraction: skip OpenAI API, use JSearch's pre-extracted data
        limit: only process first N jobs (for testing)
    """
    console.print("\n[bold blue]═" * 60)
    console.print("[bold blue]EmploiQL - Load JSearch Jobs")
    console.print("[bold blue]═" * 60)
    
    # step 1: get jobs from JSearch (cached or live)
    console.print("\n[yellow]Step 1:[/yellow] Fetching jobs from JSearch...")
    jobs = search_jobs(query=query, location=location, use_cache=use_cache)
    
    if not jobs:
        console.print("[red]No jobs found. Run jsearch.py --live first to fetch jobs.[/red]")
        return
    
    if limit:
        jobs = jobs[:limit]
        console.print(f"   [dim](limited to {limit} jobs for testing)[/dim]")
    
    console.print(f"   Found [green]{len(jobs)}[/green] jobs to process")
    
    # step 2: process each job through the pipeline
    console.print("\n[yellow]Step 2:[/yellow] Processing jobs...")
    
    stats = {"success": 0, "skipped": 0, "failed": 0}
    
    for i, job in enumerate(jobs, 1):
        title = job.get("job_title", "Unknown")[:40]
        company = job.get("employer_name", "Unknown")[:20]
        
        console.print(f"\n[dim]({i}/{len(jobs)})[/dim] {title} @ {company}")
        
        try:
            # convert to raw posting format
            raw = jsearch_to_raw_posting(job)
            
            # check if we already have this URL
            with get_cursor() as cur:
                cur.execute("SELECT id FROM raw_postings WHERE url = %s", (raw["url"],))
                if cur.fetchone():
                    console.print("   [yellow]⏭ Skipped (already in database)[/yellow]")
                    stats["skipped"] += 1
                    continue
            
            # insert raw posting
            raw_id = insert_raw_posting(
                source=raw["source"],
                url=raw["url"],
                raw_content=raw["raw_content"]
            )
            console.print(f"   [dim]raw_posting id: {raw_id}[/dim]")
            
            # extract structured data
            if use_mock_extraction:
                # use JSearch's pre-extracted data (no OpenAI cost)
                extracted = _mock_extract_from_jsearch(job)
                console.print("   [dim]Using JSearch metadata (mock extraction)[/dim]")
            else:
                # run through GPT-4o-mini for full extraction + skill normalization
                extracted = extract_job_data(raw["raw_content"], source="jsearch")
                console.print("   [dim]Extracted via GPT-4o-mini[/dim]")
            
            # insert company
            company_id = get_or_create_company(
                name=extracted.get("company_name") or job.get("employer_name", "Unknown"),
                website=job.get("employer_website")
            )
            
            # insert job
            job_id = insert_job(
                company_id=company_id,
                title=extracted.get("title") or job.get("job_title"),
                description=job.get("job_description", "")[:1000],  # truncate long descriptions
                salary_min=extracted.get("salary_min"),
                salary_max=extracted.get("salary_max"),
                location=extracted.get("location") or f"{job.get('job_city', '')}, {job.get('job_state', '')}",
                source_url=raw["url"]
            )
            console.print(f"   [dim]job id: {job_id}[/dim]")
            
            # link skills
            skills = extracted.get("skills", [])
            if skills:
                link_job_to_skills(job_id, skills)
                console.print(f"   [dim]skills: {', '.join(skills[:5])}{'...' if len(skills) > 5 else ''}[/dim]")
            
            # mark raw posting as processed
            mark_posting_processed(raw_id, job_id)
            
            console.print("   [green]✓ Success[/green]")
            stats["success"] += 1
            
        except Exception as e:
            console.print(f"   [red]✗ Error: {e}[/red]")
            stats["failed"] += 1
    
    # step 3: summary
    console.print("\n[yellow]Step 3:[/yellow] Summary")
    console.print("-" * 40)
    
    table = Table(show_header=False, box=None)
    table.add_row("✓ Loaded:", f"[green]{stats['success']}[/green]")
    table.add_row("⏭ Skipped:", f"[yellow]{stats['skipped']}[/yellow]")
    table.add_row("✗ Failed:", f"[red]{stats['failed']}[/red]")
    console.print(table)
    
    # show database stats
    console.print("\n[bold]Database now contains:[/bold]")
    with get_cursor() as cur:
        cur.execute("SELECT COUNT(*) as count FROM jobs")
        console.print(f"   Jobs:      {cur.fetchone()['count']}")
        cur.execute("SELECT COUNT(*) as count FROM companies")
        console.print(f"   Companies: {cur.fetchone()['count']}")
        cur.execute("SELECT COUNT(*) as count FROM skills")
        console.print(f"   Skills:    {cur.fetchone()['count']}")
    
    console.print("\n[bold green]Done![/bold green] Now test with: python src/text_to_sql.py")


def _mock_extract_from_jsearch(job: dict) -> dict:
    """
    create extracted data from JSearch's pre-parsed fields.
    skips OpenAI API call entirely — useful for testing pipeline.
    downside: no skill normalization, skills come from job_highlights.
    """
    # try to get skills from qualifications
    qualifications = job.get("job_highlights", {}).get("Qualifications", [])
    
    # basic skill extraction from qualifications text
    # this is crude compared to GPT extraction but costs nothing
    common_skills = [
        "Python", "JavaScript", "Java", "SQL", "React", "Node.js", "AWS",
        "Docker", "Kubernetes", "PostgreSQL", "MongoDB", "Git", "Linux",
        "TypeScript", "C++", "C#", "Go", "Ruby", "PHP", "Swift", "Kotlin",
        "Machine Learning", "Data Science", "DevOps", "CI/CD", "Agile"
    ]
    
    found_skills = []
    qual_text = " ".join(qualifications).lower() if qualifications else ""
    desc_text = job.get("job_description", "").lower()
    full_text = qual_text + " " + desc_text
    
    for skill in common_skills:
        if skill.lower() in full_text:
            found_skills.append(skill)
    
    return {
        "company_name": job.get("employer_name"),
        "title": job.get("job_title"),
        "salary_min": job.get("job_min_salary"),
        "salary_max": job.get("job_max_salary"),
        "location": f"{job.get('job_city', '')}, {job.get('job_state', '')}".strip(", "),
        "skills": found_skills[:10]  # limit to 10 skills
    }


# CLI
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Load JSearch jobs into EmploiQL database")
    parser.add_argument("--query", "-q", default="software developer",
                        help="Search query (must match cached search)")
    parser.add_argument("--location", "-l", default="Montreal, Canada",
                        help="Location (must match cached search)")
    parser.add_argument("--live", action="store_true",
                        help="Fetch fresh from JSearch API (costs quota)")
    parser.add_argument("--mock", action="store_true",
                        help="Skip OpenAI extraction, use JSearch metadata")
    parser.add_argument("--limit", type=int, default=None,
                        help="Only process first N jobs (for testing)")
    parser.add_argument("--list-cache", action="store_true",
                        help="Show available cached searches")
    
    args = parser.parse_args()
    
    if args.list_cache:
        cached = list_cache()
        if cached:
            console.print(f"\n[bold]Cached searches ({len(cached)}):[/bold]")
            for c in cached:
                console.print(f"   • {c}")
            console.print(f"\n[dim]Use --query and --location matching a cache file[/dim]")
        else:
            console.print("\n[yellow]No cached searches.[/yellow]")
            console.print("Run: python src/jsearch.py --live --query 'python developer'")
    else:
        load_jobs_to_database(
            query=args.query,
            location=args.location,
            use_cache=not args.live,
            use_mock_extraction=args.mock,
            limit=args.limit
        )