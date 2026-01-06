#!/usr/bin/env python3
# command line interface for EmploiQL
# natural language queries against montreal tech internship data

import argparse
import sys
from typing import Optional

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich import box

from text_to_sql import ask, generate_sql, validate_sql, execute_sql
from db import get_cursor, get_top_skills

console = Console()

# preset queries for common internship market questions
# saves typing and demonstrates what the system can do
PRESET_QUERIES = {
    "skills": {
        "description": "Top 10 most requested skills",
        "question": "What are the top 10 most requested skills?"
    },
    "companies": {
        "description": "Companies with most internship postings",
        "question": "Which companies have the most job postings?"
    },
    "remote": {
        "description": "Remote internship opportunities",
        "question": "Show me all remote jobs with their companies"
    },
    "python": {
        "description": "Internships requiring Python",
        "question": "Show me jobs that require Python skills"
    },
    "salaries": {
        "description": "Internships with salary info",
        "question": "Show jobs that have salary information, ordered by salary"
    },
    "recent": {
        "description": "Most recently added postings",
        "question": "Show the 10 most recent job postings"
    },
    "devops": {
        "description": "DevOps/Cloud internships",
        "question": "Show jobs requiring AWS, Docker, or Kubernetes"
    },
    "fullstack": {
        "description": "Full-stack development internships",
        "question": "Show jobs requiring both Python and JavaScript or React"
    }
}


def print_banner() -> None:
    """display the EmploiQL banner"""
    banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ███████╗███╗   ███╗██████╗ ██╗      ██████╗ ██╗ ██████╗ ██╗ ║
║   ██╔════╝████╗ ████║██╔══██╗██║     ██╔═══██╗██║██╔═══██╗██║ ║
║   █████╗  ██╔████╔██║██████╔╝██║     ██║   ██║██║██║   ██║██║ ║
║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██║   ██║██║██║▄▄ ██║██║ ║
║   ███████╗██║ ╚═╝ ██║██║     ███████╗╚██████╔╝██║╚██████╔╝███████╗
║   ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝ ╚══▀▀═╝ ╚══════╝
║                                                               ║
║         Montreal Tech Internship Market Intelligence          ║
║                     Natural Language → SQL                    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""
    console.print(banner, style="bold blue")


def print_help() -> None:
    """display help for interactive mode"""
    help_text = """
[bold]Commands:[/bold]
  [cyan]help[/cyan]          Show this help message
  [cyan]presets[/cyan]       List available preset queries
  [cyan]preset <name>[/cyan] Run a preset query (e.g., 'preset skills')
  [cyan]stats[/cyan]         Show database statistics
  [cyan]sql <query>[/cyan]   Execute raw SQL (SELECT only)
  [cyan]exit[/cyan], [cyan]quit[/cyan]   Exit the program

[bold]Example questions:[/bold]
  • What are the most in-demand skills?
  • Show me Python internships at Ubisoft
  • Which companies offer remote positions?
  • What's the average salary for DevOps roles?
  • List all cybersecurity internships

[dim]Just type your question in plain English or French![/dim]
"""
    console.print(Panel(help_text, title="EmploiQL Help", border_style="green"))


def print_presets() -> None:
    """display available preset queries"""
    table = Table(title="Preset Queries", box=box.ROUNDED)
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")
    
    for name, info in PRESET_QUERIES.items():
        table.add_row(name, info["description"])
    
    console.print(table)
    console.print("\n[dim]Usage: preset <name>  (e.g., 'preset skills')[/dim]")


def print_stats() -> None:
    """display database statistics"""
    console.print("\n[bold]Database Statistics[/bold]")
    console.print("-" * 40)
    
    with get_cursor(commit=False) as cur:
        # count jobs
        cur.execute("SELECT COUNT(*) as count FROM jobs")
        job_count = cur.fetchone()["count"]
        
        # count companies
        cur.execute("SELECT COUNT(*) as count FROM companies")
        company_count = cur.fetchone()["count"]
        
        # count skills
        cur.execute("SELECT COUNT(*) as count FROM skills")
        skill_count = cur.fetchone()["count"]
        
        # count raw postings
        cur.execute("SELECT COUNT(*) as count FROM raw_postings")
        raw_count = cur.fetchone()["count"]
        
        # jobs with salary info
        cur.execute("SELECT COUNT(*) as count FROM jobs WHERE salary_min IS NOT NULL")
        salary_count = cur.fetchone()["count"]
    
    table = Table(show_header=False, box=None)
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green", justify="right")
    
    table.add_row("Total internships", str(job_count))
    table.add_row("Companies", str(company_count))
    table.add_row("Unique skills tracked", str(skill_count))
    table.add_row("Raw postings archived", str(raw_count))
    table.add_row("Postings with salary data", str(salary_count))
    
    console.print(table)
    
    # show top 5 skills
    console.print("\n[bold]Top 5 Skills:[/bold]")
    top_skills = get_top_skills(5)
    if top_skills:
        for i, skill in enumerate(top_skills, 1):
            console.print(f"  {i}. {skill['name']} ({skill['job_count']} jobs)")
    else:
        console.print("  [dim](no skill data yet)[/dim]")


def format_results(results: list[dict], max_rows: int = 25) -> None:
    """display query results as a formatted table"""
    if not results:
        console.print("[yellow]No results found.[/yellow]")
        return
    
    # create table with column headers from result keys
    columns = list(results[0].keys())
    
    table = Table(box=box.ROUNDED, show_lines=False)
    
    for col in columns:
        # right-align numeric columns
        justify = "right" if col in ("count", "job_count", "salary_min", "salary_max", "avg_salary") else "left"
        table.add_column(col, justify=justify, overflow="fold")
    
    # add rows (limit to max_rows)
    for row in results[:max_rows]:
        values = []
        for col in columns:
            val = row[col]
            # format None values
            if val is None:
                values.append("[dim]—[/dim]")
            # format salary values
            elif col in ("salary_min", "salary_max", "avg_salary") and isinstance(val, (int, float)):
                values.append(f"${val:,.0f}")
            # truncate long strings
            elif isinstance(val, str) and len(val) > 50:
                values.append(val[:47] + "...")
            else:
                values.append(str(val))
        table.add_row(*values)
    
    console.print(table)
    
    # show truncation notice
    if len(results) > max_rows:
        console.print(f"\n[dim]Showing {max_rows} of {len(results)} results[/dim]")


def process_query(question: str) -> None:
    """process a natural language question and display results"""
    with console.status("[bold blue]Generating SQL...", spinner="dots"):
        result = ask(question)
    
    # show the generated SQL
    if result["sql"]:
        console.print("\n[bold]Generated SQL:[/bold]")
        syntax = Syntax(result["sql"], "sql", theme="monokai", line_numbers=False)
        console.print(syntax)
    
    # show error if any
    if result["error"]:
        console.print(f"\n[red]Error:[/red] {result['error']}")
        return
    
    # show results
    console.print("\n[bold]Results:[/bold]")
    format_results(result["results"])


def process_raw_sql(sql: str) -> None:
    """execute raw SQL (with safety validation)"""
    # validate first
    is_safe, error = validate_sql(sql)
    if not is_safe:
        console.print(f"[red]Blocked:[/red] {error}")
        console.print("[dim]Only SELECT queries are allowed for safety.[/dim]")
        return
    
    try:
        with console.status("[bold blue]Executing query...", spinner="dots"):
            results = execute_sql(sql)
        
        console.print("\n[bold]Results:[/bold]")
        format_results(results)
        
    except Exception as e:
        console.print(f"[red]SQL Error:[/red] {e}")


def run_interactive() -> None:
    """run the interactive REPL mode"""
    print_banner()
    console.print("[dim]Type 'help' for commands, or just ask a question![/dim]\n")
    
    while True:
        try:
            # prompt for input
            user_input = Prompt.ask("[bold green]EmploiQL[/bold green]").strip()
            
            if not user_input:
                continue
            
            # check for commands
            lower_input = user_input.lower()
            
            if lower_input in ("exit", "quit", "q"):
                console.print("[dim]Goodbye![/dim]")
                break
            
            elif lower_input == "help":
                print_help()
            
            elif lower_input == "presets":
                print_presets()
            
            elif lower_input == "stats":
                print_stats()
            
            elif lower_input.startswith("preset "):
                preset_name = lower_input[7:].strip()
                if preset_name in PRESET_QUERIES:
                    question = PRESET_QUERIES[preset_name]["question"]
                    console.print(f"[dim]Running: {question}[/dim]")
                    process_query(question)
                else:
                    console.print(f"[yellow]Unknown preset: {preset_name}[/yellow]")
                    console.print("[dim]Type 'presets' to see available options.[/dim]")
            
            elif lower_input.startswith("sql "):
                raw_sql = user_input[4:].strip()
                process_raw_sql(raw_sql)
            
            else:
                # treat as natural language question
                process_query(user_input)
            
            print()  # blank line between queries
            
        except KeyboardInterrupt:
            console.print("\n[dim]Use 'exit' to quit.[/dim]")
        
        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")


def run_single_query(question: str, show_sql: bool = True) -> None:
    """run a single query and exit"""
    result = ask(question)
    
    if show_sql and result["sql"]:
        console.print(f"[dim]SQL: {result['sql']}[/dim]\n")
    
    if result["error"]:
        console.print(f"[red]Error:[/red] {result['error']}")
        sys.exit(1)
    
    format_results(result["results"])


def main():
    """entry point - parse args and run appropriate mode"""
    parser = argparse.ArgumentParser(
        description="EmploiQL - Query Montreal tech internship data with natural language",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                              # start interactive mode
  %(prog)s "what skills are most needed"  # single query
  %(prog)s --preset skills              # run a preset query
  %(prog)s --stats                      # show database statistics
        """
    )
    
    parser.add_argument(
        "question",
        nargs="?",
        help="Natural language question to ask (starts interactive mode if omitted)"
    )
    
    parser.add_argument(
        "--preset", "-p",
        choices=list(PRESET_QUERIES.keys()),
        help="Run a preset query"
    )
    
    parser.add_argument(
        "--stats", "-s",
        action="store_true",
        help="Show database statistics"
    )
    
    parser.add_argument(
        "--sql",
        help="Execute raw SQL query (SELECT only)"
    )
    
    parser.add_argument(
        "--no-sql",
        action="store_true",
        help="Don't show generated SQL in output"
    )
    
    parser.add_argument(
        "--list-presets",
        action="store_true",
        help="List available preset queries"
    )
    
    args = parser.parse_args()
    
    # handle special flags
    if args.list_presets:
        print_presets()
        return
    
    if args.stats:
        print_stats()
        return
    
    if args.sql:
        process_raw_sql(args.sql)
        return
    
    if args.preset:
        question = PRESET_QUERIES[args.preset]["question"]
        console.print(f"[dim]Preset: {PRESET_QUERIES[args.preset]['description']}[/dim]\n")
        run_single_query(question, show_sql=not args.no_sql)
        return
    
    if args.question:
        run_single_query(args.question, show_sql=not args.no_sql)
        return
    
    # no arguments = interactive mode
    run_interactive()


if __name__ == "__main__":
    main()