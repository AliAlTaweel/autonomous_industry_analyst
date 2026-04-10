"""
tasks/writing_task.py — Report Writing Task Definition

Assigned to: Writer Agent
Input: Research + Analysis task outputs (via context=[...])
Output: Formatted Markdown report saved to ./reports/

Report Schema:
  1. Executive Summary
  2. Key Findings (table)
  3. Financial Implications
  4. Risk Matrix
  5. Strategic Opportunities
  6. Sources & Citations
  7. Agent Process Log (appended by main.py)
"""

import os
from datetime import datetime
from crewai import Task
from crewai.agent import Agent


def create_writing_task(query: str, writer: Agent, research_task: Task, analysis_task: Task) -> Task:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
    slug = query[:50].lower().replace(" ", "-").replace("/", "-")

    return Task(
        description=(
            f"Write a professional industry analysis report on the following topic:\n\n"
            f"TOPIC: {query}\n\n"
            f"Use ALL the research and analysis provided to you via context.\n\n"
            f"Follow this EXACT report structure:\n"
            f"---\n"
            f"# [TOPIC] — Autonomous Industry Analysis\n"
            f"**Generated:** {timestamp} | **Confidence:** [X.X]/10 | **Run ID:** [uuid]\n\n"
            f"## Executive Summary\n"
            f"[2-3 paragraphs. No jargon. Action-oriented. Written for a C-suite reader.]\n\n"
            f"## Key Findings\n"
            f"[Markdown table: # | Finding | Source | Confidence]\n\n"
            f"## Financial Implications\n"
            f"[From Analyst output: revenue impact, capex, valuation effects]\n\n"
            f"## Risk Matrix\n"
            f"[Markdown table: Risk | Severity | Likelihood | Mitigation]\n\n"
            f"## Strategic Opportunities\n"
            f"[Bulleted list. Each tagged: SHORT / MID / LONG term]\n\n"
            f"## Sources & Citations\n"
            f"[Numbered list with URLs and access dates from Researcher output]\n"
            f"---\n\n"
            f"The report will be saved to ./reports/{slug}.md"
        ),
        expected_output=(
            "A complete, well-structured Markdown report following the exact schema above. "
            "All sections must be present. All claims must cite a source. "
            "The confidence score from the Analyst must appear in the header. "
            "Minimum length: 600 words."
        ),
        agent=writer,
        context=[research_task, analysis_task],  # Writer reads both outputs
        output_file=f"reports/{slug}.md",        # CrewAI saves output to this file
    )
