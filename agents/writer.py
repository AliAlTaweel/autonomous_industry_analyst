"""
agents/writer.py — Research Communications Lead Agent

Responsibilities:
  - Transform approved analysis into a structured, formatted report
  - Follow the standard report schema (Executive Summary → Findings → Implications → Risk → Opportunities → Sources)
  - Save the report to ./reports/ (Phase 1) or upload to S3 (Phase 3+)

Phase 1: Saves report to local ./reports/ folder
Phase 3: S3UploaderTool replaces local save
"""

from crewai import Agent
from config.llm import get_llm


def create_writer() -> Agent:
    return Agent(
        role="Research Communications Lead",
        goal=(
            "Transform the approved analysis into a crisp, professional, board-room-ready report. "
            "Follow the standard report schema precisely. "
            "Every claim must be tied to a source. Every recommendation must have a time horizon."
        ),
        backstory=(
            "You are a former Economist journalist who now writes AI-generated research briefs "
            "for enterprise clients in the industrial and public sectors. "
            "You have an obsessive attachment to structure: if a section is missing, "
            "you add it. If a claim has no citation, you flag it. "
            "You write for a C-suite audience that has 4 minutes to read your output — "
            "every word must earn its place."
        ),
        tools=[],  # Phase 3: add S3UploaderTool here
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )
