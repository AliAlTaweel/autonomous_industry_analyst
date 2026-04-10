"""
agents/researcher.py — Senior Industry Researcher Agent

Responsibilities:
  - Gather raw intelligence from news sources, search APIs, and RSS feeds
  - Return structured data: sources, key facts, data points, gaps
  - Does NOT analyse or interpret — only gathers

Phase 1: Uses stub tools (tools/stubs.py)
Phase 2: Tools are replaced with real implementations
"""

from crewai import Agent
from config.llm import get_llm
from tools.stubs import web_scraper_tool, serper_search_tool, rss_feed_tool


def create_researcher() -> Agent:
    return Agent(
        role="Senior Industry Researcher",
        goal=(
            "Gather current, relevant, and credible raw intelligence on the given topic. "
            "Prioritize primary sources and quantified data points over opinion. "
            "Always surface gaps in the data — what you couldn't find is as important as what you did."
        ),
        backstory=(
            "You are a Bloomberg Intelligence analyst with 15 years covering Nordic industrial markets. "
            "You are obsessive about primary sources and allergic to speculation. "
            "You have broken major stories on EU industrial policy by reading Commission documents "
            "before the press release hit. Your colleagues call you 'the bloodhound' — "
            "if the data exists, you will find it."
        ),
        tools=[web_scraper_tool, serper_search_tool, rss_feed_tool],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )
