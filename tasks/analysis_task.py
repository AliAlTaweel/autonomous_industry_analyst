"""
tasks/analysis_task.py — Analysis Task Definition

Assigned to: Analyst Agent
Input: Research task output (via context=[research_task])
Output: Structured analysis with confidence_score

CRITICAL: The confidence_score drives the critique loop.
  >= 7.0 → Manager approves, passes to Writer
  <  7.0 → Manager flags for revision (Phase 2+)
"""

from crewai import Task
from crewai.agent import Agent
from models import AnalysisOutput


def create_analysis_task(analyst: Agent, research_task: Task) -> Task:
    return Task(
        description=(
            "Analyze the research data provided by the Researcher and produce a structured analysis.\n\n"
            "You must:\n"
            "1. Use fetch_financials on any companies mentioned in the research\n"
            "2. Use analyze_trends with the key events from the research\n"
            "3. Use assess_risks on the main research topic\n\n"
            "Then synthesize your findings into:\n"
            "- FINANCIAL IMPLICATIONS: Revenue impact, capex requirements, valuation effects\n"
            "- RISK MATRIX: Score each dimension (regulatory, market, execution, geopolitical)\n"
            "- STRATEGIC OPPORTUNITIES: Ranked by impact, tagged Short/Mid/Long term\n"
            "- CONFIDENCE SCORE: Your honest 0.0–10.0 rating of the analysis quality\n\n"
            "⚠️  IMPORTANT: If confidence_score < 7.0, explicitly state what additional "
            "research is needed and why. Do NOT inflate the score."
        ),
        expected_output=(
            "A structured analysis document containing:\n"
            "1. FINANCIAL IMPLICATIONS section\n"
            "2. RISK MATRIX section (scored 1-10 per dimension)\n"
            "3. STRATEGIC OPPORTUNITIES section (time-horizon tagged)\n"
            "4. CONFIDENCE SCORE: [X.X/10] with rationale\n\n"
            "If confidence < 7.0: REVISION REQUEST section explaining what's missing."
        ),
        agent=analyst,
        context=[research_task],  # Analyst reads Researcher's output
        output_pydantic=AnalysisOutput,
    )
