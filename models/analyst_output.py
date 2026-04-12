from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any

class AnalysisOutput(BaseModel):
    """Structured output from the Analyst agent."""
    implications: List[str] = Field(..., description="Financial and strategic implications of the research")
    risks: List[Dict[str, Any]] = Field(..., description="Risk matrix items (Risk, Severity, Likelihood)")
    opportunities: List[Dict[str, Any]] = Field(..., description="Strategic opportunities (Opportunity, Term, Impact)")
    confidence_score: float = Field(..., description="0.0 - 10.0 rating of the analysis quality", ge=0.0, le=10.0)
    revision_notes: Optional[str] = Field(None, description="Detailed notes on what is missing if confidence < 7.0")
