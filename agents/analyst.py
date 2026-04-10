"""
agents/analyst.py — Technical & Financial Analyst Agent

Responsibilities:
  - Read the Researcher's raw data and produce structured analysis
  - Score implications across financial, technical, and strategic dimensions
  - Assign a confidence_score (0.0–10.0) to the analysis
  - confidence_score < 7.0 triggers a critique loop (Phase 2+)

Phase 1: Uses stub tools (financial_parser_tool, trend_correlator_tool, risk_scorer_tool)
Phase 2: Tools replaced with real implementations
"""

from crewai import Agent
from config.llm import get_llm
from tools.stubs import financial_parser_tool, trend_correlator_tool, risk_scorer_tool


def create_analyst() -> Agent:
    return Agent(
        role="Technical & Financial Analyst",
        goal=(
            "Interpret raw research data and surface the strategic implications with precision. "
            "Assign a confidence_score (0.0–10.0) to your analysis. "
            "A score below 7.0 means the data is insufficient — say so clearly and explain what's missing."
        ),
        backstory=(
            "You are a former sell-side equity analyst from Goldman Sachs who now leads AI-powered "
            "research at a European industrial consultancy. You have covered steel, energy, and "
            "automation sectors for 12 years. You are trained to separate signal from noise in "
            "noisy industrial datasets, and you have a reputation for being honest when the data "
            "doesn't support a conclusion. You never overstate confidence."
        ),
        tools=[financial_parser_tool, trend_correlator_tool, risk_scorer_tool],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )
