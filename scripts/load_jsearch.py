# load JSearch jobs into EmploiQL database
# bridges: JSearch cache -> extraction.py -> database
# focused on montreal tech internships

import sys
from pathlib import Path

# add src to path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rich.console import Console
from rich.table import Table

from jsearch import search_jobs, search_preset, jsearch_to_raw_posting, list_cache, INTERNSHIP_PRESETS
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
    query: str = "software developer intern",
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
    console.print("[bold blue]EmploiQL - Load Montreal Tech Internships")
    console.print("[bold blue]═" * 60)
    
    # step 1: get jobs from JSearch (cached or live)
    console.print("\n[yellow]Step 1:[/yellow] Fetching jobs from JSearch...")
    jobs = search_jobs(query=query, location=location, use_cache=use_cache)
    
    if not jobs:
        console.print("[red]No jobs found. Run jsearch.py --live first to fetch jobs.[/red]")
        return {"success": 0, "skipped": 0, "failed": 0}
    
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
    _print_summary(stats)
    
    return stats


def load_preset(
    preset: str,
    location: str = "Montreal, Canada",
    use_cache: bool = True,
    use_mock_extraction: bool = False,
    limit: int = None
):
    """
    load jobs from an internship preset category.
    
    args:
        preset: one of the INTERNSHIP_PRESETS keys (software, devops, cyber, etc.)
        location: location to search
        use_cache: load from cache (default True)
        use_mock_extraction: skip OpenAI, use JSearch metadata
        limit: only process first N jobs
    """
    if preset not in INTERNSHIP_PRESETS:
        console.print(f"[red]Unknown preset: {preset}[/red]")
        console.print(f"Available: {', '.join(INTERNSHIP_PRESETS.keys())}")
        return {"success": 0, "skipped": 0, "failed": 0}
    
    config = INTERNSHIP_PRESETS[preset]
    console.print(f"\n[bold cyan]Loading preset:[/bold cyan] {config['description']}")
    
    return load_jobs_to_database(
        query=config["query"],
        location=location,
        use_cache=use_cache,
        use_mock_extraction=use_mock_extraction,
        limit=limit
    )


def load_all_presets(
    location: str = "Montreal, Canada",
    use_cache: bool = True,
    use_mock_extraction: bool = True,
    limit_per_preset: int = None
):
    """
    load jobs from ALL internship preset categories.
    useful for building a comprehensive database quickly.
    
    warning: if use_cache=False, this will make many API calls!
    """
    console.print("\n[bold magenta]═" * 60)
    console.print("[bold magenta]EmploiQL - Batch Load All Internship Categories")
    console.print("[bold magenta]═" * 60)
    
    total_stats = {"success": 0, "skipped": 0, "failed": 0}
    
    for preset_name in INTERNSHIP_PRESETS:
        stats = load_preset(
            preset=preset_name,
            location=location,
            use_cache=use_cache,
            use_mock_extraction=use_mock_extraction,
            limit=limit_per_preset
        )
        
        # accumulate stats
        for key in total_stats:
            total_stats[key] += stats[key]
    
    # final summary
    console.print("\n[bold magenta]═" * 60)
    console.print("[bold magenta]BATCH LOAD COMPLETE")
    console.print("[bold magenta]═" * 60)
    _print_summary(total_stats)


def _print_summary(stats: dict) -> None:
    """print load summary with database statistics."""
    console.print("\n[yellow]Summary:[/yellow]")
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
        console.print(f"   Internships: {cur.fetchone()['count']}")
        cur.execute("SELECT COUNT(*) as count FROM companies")
        console.print(f"   Companies:   {cur.fetchone()['count']}")
        cur.execute("SELECT COUNT(*) as count FROM skills")
        console.print(f"   Skills:      {cur.fetchone()['count']}")
    
    console.print("\n[bold green]Done![/bold green] Query with: python src/cli.py")


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
        "Machine Learning", "Data Science", "DevOps", "CI/CD", "Agile",
        "Vue.js", "Angular", "Django", "Flask", "FastAPI", "Express",
        "Redis", "Elasticsearch", "GraphQL", "REST", "Terraform", "Ansible",
        "Jenkins", "GitHub Actions", "Azure", "Google Cloud", "Spark",
        "Hadoop", "Kafka", "RabbitMQ", "Nginx", "Apache", "Bash", "Shell"
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
        "skills": found_skills[:15]  # limit to 15 skills
    }


# CLI
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Load Montreal tech internships into EmploiQL database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --preset software --mock        # load software internships (no API cost)
  %(prog)s --preset devops                 # load devops with GPT extraction
  %(prog)s --all --mock                    # load ALL categories (fast, free)
  %(prog)s --query "python intern" --mock  # custom search
  %(prog)s --list-cache                    # show available cached searches
        """
    )
    
    parser.add_argument("--query", "-q", default=None,
                        help="Search query (must match a cached search)")
    parser.add_argument("--preset", "-p", choices=list(INTERNSHIP_PRESETS.keys()),
                        help="Load from an internship preset category")
    parser.add_argument("--all", "-a", action="store_true",
                        help="Load ALL internship preset categories")
    parser.add_argument("--location", "-l", default="Montreal, Canada",
                        help="Location (must match cached search)")
    parser.add_argument("--live", action="store_true",
                        help="Fetch fresh from JSearch API (costs quota)")
    parser.add_argument("--mock", action="store_true",
                        help="Skip OpenAI extraction, use JSearch metadata (free)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Only process first N jobs (for testing)")
    parser.add_argument("--list-cache", action="store_true",
                        help="Show available cached searches")
    parser.add_argument("--list-presets", action="store_true",
                        help="Show available internship presets")
    
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
            console.print("Run: python src/jsearch.py --preset software --live")
    
    elif args.list_presets:
        console.print("\n[bold]Internship Presets:[/bold]")
        for name, config in INTERNSHIP_PRESETS.items():
            console.print(f"   [cyan]{name:12}[/cyan] - {config['description']}")
        console.print("\n[dim]Usage: --preset <name> or --all for everything[/dim]")
    
    elif args.all:
        # load all preset categories
        load_all_presets(
            location=args.location,
            use_cache=not args.live,
            use_mock_extraction=args.mock,
            limit_per_preset=args.limit
        )
    
    elif args.preset:
        # load specific preset
        load_preset(
            preset=args.preset,
            location=args.location,
            use_cache=not args.live,
            use_mock_extraction=args.mock,
            limit=args.limit
        )
    
    elif args.query:
        # custom query
        load_jobs_to_database(
            query=args.query,
            location=args.location,
            use_cache=not args.live,
            use_mock_extraction=args.mock,
            limit=args.limit
        )
    
    else:
        # no arguments - show help
        console.print("\n[yellow] No search specified.[/yellow]")
        console.print("\nQuick start:")
        console.print("  1. Fetch data:  python3 src/jsearch.py --preset software --live")
        console.print("  2. Load to DB:  python3 scripts/load_jsearch.py --preset software --mock")
        console.print("  3. Query:       python3 src/cli.py")
        console.print("\nOr load everything: python3 scripts/load_jsearch.py --all --mock")
