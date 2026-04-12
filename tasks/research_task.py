"""
tasks/research_task.py — Research Task Definition

Assigned to: Researcher Agent
Output: Structured intelligence document with sources, facts, data points, and gaps
"""

from crewai import Task
from crewai.agent import Agent
from models import ResearchOutput


def create_research_task(query: str, researcher: Agent) -> Task:
    return Task(
        description=(
            f"Research the following topic thoroughly:\n\n"
            f"TOPIC: {query}\n\n"
            f"Your job is to gather raw intelligence. Use all available tools:\n"
            f"1. Use duckduckgo_search_tool to find recent news (last 90 days)\n"
            f"2. Use rss_feed_tool to pull from curated industrial RSS feeds\n"
            f"3. Use web_scraper_tool on the 2-3 most relevant URLs from your search results\n\n"
            f"Structure your output clearly:\n"
            f"- SOURCES: List every URL/source you consulted\n"
            f"- KEY FACTS: Top 5-7 concrete, data-backed findings\n"
            f"- DATA POINTS: Numbers, percentages, dates, company names\n"
            f"- GAPS: What you could NOT find that would improve the analysis"
        ),
        expected_output=(
            "A RAW JSON object matching the ResearchOutput schema. "
            "Do NOT include markdown markers, do NOT include conversational text. "
            "Focus on high-density data and specific sources."
        ),
        agent=researcher,
        output_pydantic=ResearchOutput,
    )
