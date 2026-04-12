import json
from crewai.tools import tool

@tool
def assess_risks(topic: str) -> str:
    """
    Evaluates regulatory, market, execution, and geopolitical risks for a given topic.
    Provides a structured risk matrix for analysis.
    """
    # This tool prompts the agent to look for specific risk indicators.
    return json.dumps({
        "topic": topic,
        "instructions": (
            "Evaluate the primary risks for this topic across these dimensions:\n"
            "1. Regulatory (Policy shifts, compliance costs)\n"
            "2. Market (Demand fragility, pricing power)\n"
            "3. Execution (Capex risk, technology readiness)\n"
            "4. Geopolitical (Supply chain stability, regional conflict)\n"
        )
    })
