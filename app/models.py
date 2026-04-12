from pydantic import BaseModel
from typing import Optional

class AnalyzeRequest(BaseModel):
    query: str
    depth: Optional[str] = "standard"

class AnalyzeResponse(BaseModel):
    run_id: str
    status: str
    estimated_minutes: int

class StatusResponse(BaseModel):
    status: str
    report_url: Optional[str] = None
    report_path: Optional[str] = None
