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
from tools import fetch_financials, analyze_trends, assess_risks


def create_analyst() -> Agent:
    return Agent(
        role="Technical & Financial Analyst",
        goal=(
            "Interpret raw research data and surface the strategic implications with precision. "
            "Assign a confidence_score (0.0–10.0) to your analysis. "
            "CRITICAL: Use the tools EXACTLY as named: fetch_financials, analyze_trends, and assess_risks."
        ),
        backstory=(
            "You are a former sell-side equity analyst from Goldman Sachs who now leads AI-powered "
            "research at a European industrial consultancy. You are trained to separate signal from noise. "
            "You are obsessive about precision and only use your official toolkit: fetch_financials, "
            "analyze_trends, and assess_risks. You never invent tool names."
        ),
        tools=[fetch_financials, analyze_trends, assess_risks],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=3,
    )
