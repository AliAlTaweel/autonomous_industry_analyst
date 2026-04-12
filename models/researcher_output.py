from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any

class ResearchOutput(BaseModel):
    """Structured output from the Researcher agent."""
    sources: List[str] = Field(..., description="List of URLs and primary sources consulted")
    key_facts: List[str] = Field(..., description="Top 5-7 concrete findings from the research")
    data_points: List[Dict[str, Any]] = Field(..., description="Quantified data (percentages, dates, revenue numbers)")
    gaps: List[str] = Field(..., description="Information that was sought but not found")
