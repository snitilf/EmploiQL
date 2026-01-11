#!/usr/bin/env python3
# streamlit dashboard for EmploiQL
# run with: streamlit run src/app.py

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from typing import Optional

from db import get_cursor, get_top_skills
from text_to_sql import ask, validate_sql, execute_sql

# page configuration; must be first streamlit command
st.set_page_config(
    page_title="EmploiQL - Montreal Tech Internships",
    page_icon="briefcase",
    layout="wide",
    initial_sidebar_state="expanded"
)

# custom css for better styling
st.markdown("""
<style>
    /* main title styling */
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #89B4FA;
        margin-bottom: 0.5rem;
    }
    
    /* subtitle styling */
    .subtitle {
        font-size: 1.1rem;
        color: #CDD6F4;
        margin-bottom: 2rem;
    }
    
    /* metric card styling */
    .metric-card {
        background-color: #313244;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
    
    /* section header styling */
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #CDD6F4;
        margin-top: 2rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #89B4FA;
    }
    
    /* general text styling */
    .stMarkdown, .stText, p, div {
        color: #CDD6F4;
    }
    
    /* subheader styling */
    h2, h3 {
        color: #CDD6F4 !important;
    }
    
    /* metric labels and values */
    [data-testid="stMetricLabel"], [data-testid="stMetricValue"] {
        color: #CDD6F4;
    }
    
    /* sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #313244;
    }
    
    /* button styling */
    .stButton > button {
        background-color: #89B4FA;
        color: #1E1E2E;
        border: none;
    }
    
    .stButton > button:hover {
        background-color: #A6C5FF;
    }
    
    /* input fields */
    .stTextInput > div > div > input {
        background-color: #313244;
        color: #CDD6F4;
    }
    
    .stSelectbox > div > div > select {
        background-color: #313244;
        color: #CDD6F4;
    }
    
    .stTextArea > div > div > textarea {
        background-color: #313244;
        color: #CDD6F4;
    }
    
    /* dataframe styling */
    .dataframe {
        background-color: #313244;
    }
    
    /* expander styling */
    [data-testid="stExpander"] {
        background-color: #313244;
    }
</style>
""", unsafe_allow_html=True)



# data loading functions (cached to avoid repeated database calls)


@st.cache_data(ttl=300)  # cache for 5 minutes
def load_dashboard_stats() -> dict:
    """
    load summary statistics for the dashboard.
    returns dict with counts for jobs, companies, skills, etc.
    """
    stats = {}
    
    with get_cursor(commit=False) as cursor:
        # count total jobs
        cursor.execute("SELECT COUNT(*) as count FROM jobs")
        stats["total_jobs"] = cursor.fetchone()["count"]
        
        # count companies
        cursor.execute("SELECT COUNT(*) as count FROM companies")
        stats["total_companies"] = cursor.fetchone()["count"]
        
        # count unique skills
        cursor.execute("SELECT COUNT(*) as count FROM skills")
        stats["total_skills"] = cursor.fetchone()["count"]
        
        # count jobs with salary data
        cursor.execute(
            "SELECT COUNT(*) as count FROM jobs WHERE salary_min IS NOT NULL"
        )
        stats["jobs_with_salary"] = cursor.fetchone()["count"]
        
        # count remote jobs
        cursor.execute(
            "SELECT COUNT(*) as count FROM jobs WHERE location ILIKE '%remote%'"
        )
        stats["remote_jobs"] = cursor.fetchone()["count"]
        
        # average salary (where available)
        cursor.execute("""
            SELECT 
                AVG(salary_min) as avg_min,
                AVG(salary_max) as avg_max
            FROM jobs 
            WHERE salary_min IS NOT NULL
        """)
        salary_result = cursor.fetchone()
        stats["avg_salary_min"] = salary_result["avg_min"]
        stats["avg_salary_max"] = salary_result["avg_max"]
    
    return stats


@st.cache_data(ttl=300)
def load_top_skills(limit: int = 15) -> list[dict]:
    """load top skills by job count."""
    return get_top_skills(limit)


@st.cache_data(ttl=300)
def load_companies_by_job_count(limit: int = 10) -> list[dict]:
    """load companies ranked by number of job postings."""
    with get_cursor(commit=False) as cursor:
        cursor.execute("""
            SELECT 
                c.name as company_name,
                COUNT(*) as job_count
            FROM companies c
            JOIN jobs j ON c.id = j.company_id
            GROUP BY c.id, c.name
            ORDER BY job_count DESC
            LIMIT %s
        """, (limit,))
        return cursor.fetchall()


@st.cache_data(ttl=300)
def load_jobs_by_location() -> list[dict]:
    """load job counts grouped by location."""
    with get_cursor(commit=False) as cursor:
        cursor.execute("""
            SELECT 
                COALESCE(location, 'Not Specified') as location,
                COUNT(*) as job_count
            FROM jobs
            GROUP BY location
            ORDER BY job_count DESC
            LIMIT 10
        """)
        return cursor.fetchall()


@st.cache_data(ttl=300)
def load_salary_by_skill(min_jobs: int = 3) -> list[dict]:
    """
    load average salary for each skill.
    only includes skills with at least min_jobs postings that have salary data.
    """
    with get_cursor(commit=False) as cursor:
        cursor.execute("""
            SELECT 
                s.name as skill_name,
                AVG(j.salary_min) as avg_salary_min,
                AVG(j.salary_max) as avg_salary_max,
                COUNT(*) as job_count
            FROM skills s
            JOIN job_skills js ON s.id = js.skill_id
            JOIN jobs j ON js.job_id = j.id
            WHERE j.salary_min IS NOT NULL
            GROUP BY s.id, s.name
            HAVING COUNT(*) >= %s
            ORDER BY avg_salary_max DESC
            LIMIT 15
        """, (min_jobs,))
        return cursor.fetchall()


@st.cache_data(ttl=300)
def load_all_jobs(
    skill_filter: Optional[str] = None,
    company_filter: Optional[str] = None,
    location_filter: Optional[str] = None,
    limit: int = 100
) -> list[dict]:
    """
    load jobs with optional filters.
    returns list of job dicts with company name included.
    """
    # build dynamic query based on filters
    query = """
        SELECT 
            j.id,
            j.title,
            c.name as company_name,
            j.location,
            j.salary_min,
            j.salary_max,
            j.source_url,
            j.created_at
        FROM jobs j
        JOIN companies c ON j.company_id = c.id
        WHERE 1=1
    """
    
    parameters = []
    
    # add skill filter via subquery
    if skill_filter and skill_filter != "All":
        query += """
            AND j.id IN (
                SELECT js.job_id 
                FROM job_skills js 
                JOIN skills s ON js.skill_id = s.id 
                WHERE s.name = %s
            )
        """
        parameters.append(skill_filter)
    
    # add company filter
    if company_filter and company_filter != "All":
        query += " AND c.name ILIKE %s"
        parameters.append(f"%{company_filter}%")
    
    # add location filter
    if location_filter and location_filter != "All":
        query += " AND j.location ILIKE %s"
        parameters.append(f"%{location_filter}%")
    
    query += " ORDER BY j.created_at DESC LIMIT %s"
    parameters.append(limit)
    
    with get_cursor(commit=False) as cursor:
        cursor.execute(query, tuple(parameters))
        return cursor.fetchall()


@st.cache_data(ttl=300)
def load_filter_options() -> dict:
    """load unique values for filter dropdowns."""
    options = {}
    
    with get_cursor(commit=False) as cursor:
        # get all skill names
        cursor.execute("SELECT name FROM skills ORDER BY name")
        options["skills"] = ["All"] + [row["name"] for row in cursor.fetchall()]
        
        # get all company names
        cursor.execute("SELECT name FROM companies ORDER BY name")
        options["companies"] = ["All"] + [row["name"] for row in cursor.fetchall()]
        
        # get unique locations
        cursor.execute("""
            SELECT DISTINCT location 
            FROM jobs 
            WHERE location IS NOT NULL 
            ORDER BY location
        """)
        options["locations"] = ["All"] + [row["location"] for row in cursor.fetchall()]
    
    return options


@st.cache_data(ttl=300)
def load_skills_for_job(job_id: int) -> list[str]:
    """load skill names for a specific job."""
    with get_cursor(commit=False) as cursor:
        cursor.execute("""
            SELECT s.name
            FROM skills s
            JOIN job_skills js ON s.id = js.skill_id
            WHERE js.job_id = %s
            ORDER BY s.name
        """, (job_id,))
        return [row["name"] for row in cursor.fetchall()]



# chart creation functions


def create_top_skills_chart(skills_data: list[dict]) -> go.Figure:
    """
    create horizontal bar chart of top skills.
    uses plotly for interactivity (hover, zoom, etc.)
    """
    if not skills_data:
        # return empty figure with message
        fig = go.Figure()
        fig.add_annotation(
            text="No skill data available",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="#CDD6F4")
        )
        return fig
    
    # extract data for chart
    skill_names = [row["name"] for row in skills_data]
    job_counts = [row["job_count"] for row in skills_data]
    
    # reverse for horizontal bar chart (highest at top)
    skill_names = skill_names[::-1]
    job_counts = job_counts[::-1]
    
    # create horizontal bar chart
    fig = px.bar(
        x=job_counts,
        y=skill_names,
        orientation="h",
        labels={"x": "Number of Jobs", "y": "Skill"},
        color=job_counts,
        color_continuous_scale=[[0, "#89B4FA"], [1, "#A6C5FF"]]
    )
    
    # customize layout
    fig.update_layout(
        showlegend=False,
        coloraxis_showscale=False,
        margin=dict(l=0, r=20, t=20, b=40),
        height=400,
        xaxis_title="Number of Job Postings",
        yaxis_title="",
        plot_bgcolor="#1E1E2E",
        paper_bgcolor="#1E1E2E",
        font=dict(color="#CDD6F4"),
        xaxis=dict(gridcolor="#313244"),
        yaxis=dict(gridcolor="#313244")
    )
    
    # add hover template
    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Jobs: %{x}<extra></extra>"
    )
    
    return fig


def create_companies_chart(companies_data: list[dict]) -> go.Figure:
    """create bar chart of top hiring companies."""
    if not companies_data:
        fig = go.Figure()
        fig.add_annotation(
            text="No company data available",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="#CDD6F4")
        )
        return fig
    
    company_names = [row["company_name"] for row in companies_data]
    job_counts = [row["job_count"] for row in companies_data]
    
    fig = px.bar(
        x=company_names,
        y=job_counts,
        labels={"x": "Company", "y": "Number of Jobs"},
        color=job_counts,
        color_continuous_scale=[[0, "#F5C2E7"], [1, "#F9E2AF"]]
    )
    
    fig.update_layout(
        showlegend=False,
        coloraxis_showscale=False,
        margin=dict(l=0, r=20, t=20, b=40),
        height=350,
        xaxis_title="",
        yaxis_title="Job Postings",
        xaxis_tickangle=-45,
        plot_bgcolor="#1E1E2E",
        paper_bgcolor="#1E1E2E",
        font=dict(color="#CDD6F4"),
        xaxis=dict(gridcolor="#313244"),
        yaxis=dict(gridcolor="#313244")
    )
    
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Jobs: %{y}<extra></extra>"
    )
    
    return fig


def create_location_pie_chart(location_data: list[dict]) -> go.Figure:
    """create pie chart of jobs by location."""
    if not location_data:
        fig = go.Figure()
        fig.add_annotation(
            text="No location data available",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="#CDD6F4")
        )
        return fig
    
    locations = [row["location"] for row in location_data]
    counts = [row["job_count"] for row in location_data]
    
    fig = px.pie(
        names=locations,
        values=counts,
        hole=0.4,  # donut chart style
        color_discrete_sequence=["#89B4FA", "#F5C2E7", "#F9E2AF", "#A6C5FF", "#F8BBD9", "#FCE5B4", "#B8D4FF", "#F9D0E8"]
    )
    
    fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=20),
        height=350,
        plot_bgcolor="#1E1E2E",
        paper_bgcolor="#1E1E2E",
        font=dict(color="#CDD6F4"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        )
    )
    
    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate="<b>%{label}</b><br>Jobs: %{value}<br>(%{percent})<extra></extra>"
    )
    
    return fig


def create_salary_by_skill_chart(salary_data: list[dict]) -> go.Figure:
    """create bar chart showing salary ranges by skill."""
    if not salary_data:
        fig = go.Figure()
        fig.add_annotation(
            text="Not enough salary data available",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="#CDD6F4")
        )
        return fig
    
    skill_names = [row["skill_name"] for row in salary_data]
    avg_min = [row["avg_salary_min"] or 0 for row in salary_data]
    avg_max = [row["avg_salary_max"] or 0 for row in salary_data]
    
    # create grouped bar chart with min and max salary
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name="Avg Min Salary",
        x=skill_names,
        y=avg_min,
        marker_color="#89B4FA"
    ))
    
    fig.add_trace(go.Bar(
        name="Avg Max Salary",
        x=skill_names,
        y=avg_max,
        marker_color="#F5C2E7"
    ))
    
    fig.update_layout(
        barmode="group",
        margin=dict(l=0, r=20, t=20, b=80),
        height=400,
        xaxis_title="",
        yaxis_title="Annual Salary (CAD)",
        xaxis_tickangle=-45,
        plot_bgcolor="#1E1E2E",
        paper_bgcolor="#1E1E2E",
        font=dict(color="#CDD6F4"),
        xaxis=dict(gridcolor="#313244"),
        yaxis=dict(gridcolor="#313244"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    # format y-axis as currency
    fig.update_yaxes(tickprefix="$", tickformat=",")
    
    return fig



# page sections


def render_header():
    """render the main page header."""
    st.markdown('<p class="main-title">EmploiQL</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Montreal Tech Internship Market Intelligence</p>',
        unsafe_allow_html=True
    )


def render_dashboard_section():
    """render the dashboard overview with stats and charts."""
    st.markdown(
        '<p class="section-header">Dashboard Overview</p>',
        unsafe_allow_html=True
    )
    
    # load stats
    stats = load_dashboard_stats()
    
    # display metrics in columns
    metric_col1, metric_col2, metric_col3, metric_col4, metric_col5 = st.columns(5)
    
    with metric_col1:
        st.metric(
            label="Total Postings",
            value=f"{stats['total_jobs']:,}"
        )
    
    with metric_col2:
        st.metric(
            label="Companies",
            value=f"{stats['total_companies']:,}"
        )
    
    with metric_col3:
        st.metric(
            label="Skills Tracked",
            value=f"{stats['total_skills']:,}"
        )
    
    with metric_col4:
        st.metric(
            label="Remote Positions",
            value=f"{stats['remote_jobs']:,}"
        )
    
    with metric_col5:
        # calculate average salary if data available
        if stats["avg_salary_max"]:
            avg_salary = int(stats["avg_salary_max"])
            st.metric(
                label="Avg Max Salary",
                value=f"${avg_salary:,}"
            )
        else:
            st.metric(
                label="Avg Max Salary",
                value="N/A"
            )
    
    # charts row
    st.markdown("---")
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.subheader("Top In-Demand Skills")
        skills_data = load_top_skills(15)
        skills_chart = create_top_skills_chart(skills_data)
        st.plotly_chart(skills_chart, use_container_width=True)
    
    with chart_col2:
        st.subheader("Top Hiring Companies")
        companies_data = load_companies_by_job_count(10)
        companies_chart = create_companies_chart(companies_data)
        st.plotly_chart(companies_chart, use_container_width=True)
    
    # second row of charts
    chart_col3, chart_col4 = st.columns(2)
    
    with chart_col3:
        st.subheader("Jobs by Location")
        location_data = load_jobs_by_location()
        location_chart = create_location_pie_chart(location_data)
        st.plotly_chart(location_chart, use_container_width=True)
    
    with chart_col4:
        st.subheader("Salary by Skill")
        salary_data = load_salary_by_skill(min_jobs=2)
        salary_chart = create_salary_by_skill_chart(salary_data)
        st.plotly_chart(salary_chart, use_container_width=True)


def render_query_section():
    """render the natural language query interface."""
    st.markdown(
        '<p class="section-header">Ask a Question</p>',
        unsafe_allow_html=True
    )
    
    st.write("Ask questions about the Montreal tech internship market in plain English or French.")
    
    # example questions
    with st.expander("Example questions"):
        st.markdown("""
        - What are the top 10 most requested skills?
        - Which companies have the most internship postings?
        - Show me remote jobs that require Python
        - What is the average salary for DevOps internships?
        - List all skills required at Ubisoft
        - How many jobs require both Python and SQL?
        """)
    
    # query input
    question = st.text_input(
        "Your question:",
        placeholder="e.g., What skills are most in demand for data science internships?"
    )
    
    # query button
    if st.button("Run Query", type="primary"):
        if question:
            with st.spinner("Generating SQL and querying database..."):
                result = ask(question)
            
            # show generated SQL
            if result["sql"]:
                st.subheader("Generated SQL")
                st.code(result["sql"], language="sql")
            
            # show error if any
            if result["error"]:
                st.error(f"Error: {result['error']}")
            
            # show results
            elif result["results"]:
                st.subheader(f"Results ({len(result['results'])} rows)")
                st.dataframe(
                    result["results"],
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("No results found for this query.")
        else:
            st.warning("Please enter a question.")
    
    # raw SQL option
    st.markdown("---")
    with st.expander("Advanced: Run Raw SQL"):
        raw_sql = st.text_area(
            "SQL Query (SELECT only):",
            placeholder="SELECT * FROM jobs LIMIT 10;",
            height=100
        )
        
        if st.button("Execute SQL"):
            if raw_sql:
                # validate first
                is_safe, error = validate_sql(raw_sql)
                if not is_safe:
                    st.error(f"Query blocked: {error}")
                else:
                    try:
                        with st.spinner("Executing query..."):
                            results = execute_sql(raw_sql)
                        
                        if results:
                            st.dataframe(
                                results,
                                use_container_width=True,
                                hide_index=True
                            )
                        else:
                            st.info("Query returned no results.")
                    except Exception as e:
                        st.error(f"SQL Error: {e}")
            else:
                st.warning("Please enter a SQL query.")


def render_explore_section():
    """render the job exploration interface with filters."""
    st.markdown(
        '<p class="section-header">Explore Jobs/Internships</p>',
        unsafe_allow_html=True
    )
    
    # load filter options
    filter_options = load_filter_options()
    
    # filter controls in columns
    filter_col1, filter_col2, filter_col3 = st.columns(3)
    
    with filter_col1:
        skill_filter = st.selectbox(
            "Filter by Skill:",
            options=filter_options["skills"],
            index=0
        )
    
    with filter_col2:
        company_filter = st.selectbox(
            "Filter by Company:",
            options=filter_options["companies"],
            index=0
        )
    
    with filter_col3:
        location_filter = st.selectbox(
            "Filter by Location:",
            options=filter_options["locations"],
            index=0
        )
    
    # load and display jobs
    jobs = load_all_jobs(
        skill_filter=skill_filter if skill_filter != "All" else None,
        company_filter=company_filter if company_filter != "All" else None,
        location_filter=location_filter if location_filter != "All" else None
    )
    
    st.write(f"Showing {len(jobs)} internships")
    
    # display jobs as cards/table
    if jobs:
        for job in jobs:
            with st.container():
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**{job['title']}**")
                    st.write(f"{job['company_name']} | {job['location'] or 'Location not specified'}")
                    
                    # load and display skills for this job
                    job_skills = load_skills_for_job(job["id"])
                    if job_skills:
                        skills_text = ", ".join(job_skills[:8])
                        if len(job_skills) > 8:
                            skills_text += f" +{len(job_skills) - 8} more"
                        st.caption(f"Skills: {skills_text}")
                
                with col2:
                    # display salary if available
                    if job["salary_min"] and job["salary_max"]:
                        st.write(f"${job['salary_min']:,} - ${job['salary_max']:,}")
                    elif job["salary_min"]:
                        st.write(f"${job['salary_min']:,}+")
                    elif job["salary_max"]:
                        st.write(f"Up to ${job['salary_max']:,}")
                    else:
                        st.write("Salary not listed")
                    
                    # link to original posting
                    if job["source_url"]:
                        st.link_button("View Posting", job["source_url"])
                
                st.markdown("---")
    else:
        st.info("No internships match your filters.")


def render_skills_analysis_section():
    """render detailed skills analysis."""
    st.markdown(
        '<p class="section-header">Skills Analysis</p>',
        unsafe_allow_html=True
    )
    
    st.write("Deep dive into skill demand and salary correlations.")
    
    # skills frequency table
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Complete Skills Ranking")
        
        # load all skills with counts
        with get_cursor(commit=False) as cursor:
            cursor.execute("""
                SELECT 
                    s.name as skill,
                    COUNT(*) as job_count,
                    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM jobs), 1) as percent_of_jobs
                FROM skills s
                JOIN job_skills js ON s.id = js.skill_id
                GROUP BY s.id, s.name
                ORDER BY job_count DESC
            """)
            all_skills = cursor.fetchall()
        
        if all_skills:
            st.dataframe(
                all_skills,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "skill": "Skill",
                    "job_count": st.column_config.NumberColumn("Jobs", format="%d"),
                    "percent_of_jobs": st.column_config.NumberColumn("% of Postings", format="%.1f%%")
                }
            )
        else:
            st.info("No skill data available.")
    
    with col2:
        st.subheader("Skill Co-occurrence")
        st.write("Skills that frequently appear together:")
        
        # find skill pairs that appear together
        with get_cursor(commit=False) as cursor:
            cursor.execute("""
                SELECT 
                    s1.name as skill_1,
                    s2.name as skill_2,
                    COUNT(*) as together_count
                FROM job_skills js1
                JOIN job_skills js2 ON js1.job_id = js2.job_id AND js1.skill_id < js2.skill_id
                JOIN skills s1 ON js1.skill_id = s1.id
                JOIN skills s2 ON js2.skill_id = s2.id
                GROUP BY s1.id, s1.name, s2.id, s2.name
                HAVING COUNT(*) >= 2
                ORDER BY together_count DESC
                LIMIT 15
            """)
            skill_pairs = cursor.fetchall()
        
        if skill_pairs:
            st.dataframe(
                skill_pairs,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "skill_1": "Skill A",
                    "skill_2": "Skill B",
                    "together_count": st.column_config.NumberColumn("Together In", format="%d jobs")
                }
            )
        else:
            st.info("Not enough data for skill co-occurrence analysis.")



# sidebar navigation


def render_sidebar():
    """render the sidebar with navigation and info."""
    with st.sidebar:
        st.title("Navigation")
        
        # section selection
        section = st.radio(
            "Go to:",
            options=[
                "Dashboard",
                "Ask a Question",
                "Explore Jobs/Internships",
                "Skills Analysis"
            ],
            index=0
        )
        
        st.markdown("---")
        
        # quick stats in sidebar
        st.subheader("Quick Stats")
        stats = load_dashboard_stats()
        st.write(f"Jobs: {stats['total_jobs']}")
        st.write(f"Companies: {stats['total_companies']}")
        st.write(f"Skills: {stats['total_skills']}")
        
        st.markdown("---")
        
        # about section
        st.subheader("About")
        st.write(
            "EmploiQL uses natural language to query Montreal's "
            "tech internship market data."
        )
        
        st.markdown("---")
        
        # cache clear button
        if st.button("Refresh Data"):
            st.cache_data.clear()
            st.rerun()
        
        return section



# main app


def main():
    """main app entry point."""
    # render header
    render_header()
    
    # render sidebar and get selected section
    selected_section = render_sidebar()
    
    # render selected section
    if selected_section == "Dashboard":
        render_dashboard_section()
    
    elif selected_section == "Ask a Question":
        render_query_section()
    
    elif selected_section == "Explore Jobs/Internships":
        render_explore_section()
    
    elif selected_section == "Skills Analysis":
        render_skills_analysis_section()


if __name__ == "__main__":
    main()