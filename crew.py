"""
crew.py — Crew Assembly

Wires all agents and tasks into a CrewAI Crew.
Uses Process.hierarchical so the Manager agent automatically
orchestrates delegation, reviews outputs, and manages flow.

Phase 1: Critique loop is passive (stubs always pass confidence >= 7.0)
Phase 2: Real confidence scores drive actual loop-back behavior
"""

from crewai import Crew, Process

from config.logger import logger
from config.llm import get_llm
from agents.manager import create_manager
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
    logger.info("\n" + "═" * 60)
    logger.info("  🧠  AUTONOMOUS INDUSTRY ANALYST")
    logger.info("═" * 60)
    logger.info(f"  Query: {query}")
    logger.info("═" * 60 + "\n")

    logger.debug(f"Building crew for query: {query}")

    logger.debug("Initializing agents...")
    manager = create_manager()
    researcher = create_researcher()
    analyst = create_analyst()
    writer = create_writer()
    logger.debug(f"Agents initialized: {len([manager, researcher, analyst, writer])}")

    # ── Tasks (order matters for context chaining) ─────────────────
    research_task = create_research_task(query, researcher)
    analysis_task = create_analysis_task(analyst, research_task)
    writing_task = create_writing_task(query, writer, research_task, analysis_task)

    # ── Crew ──────────────────────────────────────────────────────
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, writing_task],
        
        # Enable Memory: stores short-term, long-term, and entity memory
        memory=True,
        embedder={
            "provider": "ollama",
            "config": {
                "model": "nomic-embed-text",
            }
        },

        # Hierarchical: custom Manager agent orchestrates delegation and review
        process=Process.hierarchical,
        manager_agent=manager,

        verbose=True,       # Show all agent reasoning and tool calls
        planning=False,     # Disabled: local LLMs struggle with the strict Planner schema
        planning_llm=get_llm(),
        max_execution_time=1800, # 30-minute cap allowed for slower local 26B model reasoning
    )

    return crew
