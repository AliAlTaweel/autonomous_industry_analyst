"""
crew.py — Crew Assembly

Wires all agents and tasks into a CrewAI Crew.
Uses Process.hierarchical so the Manager agent automatically
orchestrates delegation, reviews outputs, and manages flow.

Phase 1: Critique loop is passive (stubs always pass confidence >= 7.0)
Phase 2: Real confidence scores drive actual loop-back behavior
"""

from crewai import Crew, Process

from config.llm import get_llm
from agents.researcher import create_researcher
from agents.analyst import create_analyst
from agents.writer import create_writer
from tasks.research_task import create_research_task
from tasks.analysis_task import create_analysis_task
from tasks.writing_task import create_writing_task


def build_crew(query: str) -> Crew:
    """
    Assembles and returns a configured CrewAI Crew for a given research query.

    Args:
        query: The research topic or question to investigate

    Returns:
        A configured Crew ready to run
    """
    print("\n" + "═" * 60)
    print("  🧠  AUTONOMOUS INDUSTRY ANALYST")
    print("═" * 60)
    print(f"  Query: {query}")
    print("═" * 60 + "\n")

    # ── Agents ────────────────────────────────────────────────────
    researcher = create_researcher()
    analyst = create_analyst()
    writer = create_writer()

    # ── Tasks (order matters for context chaining) ─────────────────
    research_task = create_research_task(query, researcher)
    analysis_task = create_analysis_task(analyst, research_task)
    writing_task = create_writing_task(query, writer, research_task, analysis_task)

    # ── Crew ──────────────────────────────────────────────────────
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, writing_task],

        # Hierarchical: auto-created Manager agent orchestrates delegation
        # manager_llm drives the Manager's reasoning and critique decisions
        process=Process.hierarchical,
        manager_llm=get_llm(),

        verbose=True,       # Show all agent reasoning and tool calls
        planning=False,     # Phase 1: no upfront task planning (added in CrewAI 1.x)
        # memory=False      # Default is False — omit to avoid deprecation warnings
    )

    return crew
