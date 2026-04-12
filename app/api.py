import uuid
from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import ValidationError
from .models import AnalyzeRequest, AnalyzeResponse, StatusResponse
from .runner import execute_run, RUNS

app = FastAPI(
    title="Autonomous Industry Analyst API",
    description="REST API wrapper for the autonomous multi-agent research pipeline.",
    version="1.0.0"
)

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest, background_tasks: BackgroundTasks):
    """
    Start a background research run given a user query.
    Returns the run_id that can be used to query execution status.
    """
    # Using hex format for a more concise run_id string
    run_id = f"run-{uuid.uuid4().hex[:8]}"
    
    # Offload the blocking execution call to background task
    background_tasks.add_task(execute_run, run_id, request.query)
    
    return AnalyzeResponse(
        run_id=run_id,
        status="running",
        estimated_minutes=5 # Rough estimate based on LLMs speeds
    )

@app.get("/analyze/{run_id}", response_model=StatusResponse)
def get_status(run_id: str):
    """
    Get the status of an ongoing or completed research run.
    """
    if run_id not in RUNS:
        raise HTTPException(status_code=404, detail="Run ID not found")
        
    run_data = RUNS[run_id]
    
    # Later passing the S3 url to report_url field can be added here
    return StatusResponse(
        status=run_data.get("status"),
        report_url=run_data.get("report_url"),
        report_path=run_data.get("report_path")
    )

@app.get("/health")
def health():
    """
    Liveness probe for AWS App Runner or ALB.
    """
    return {"status": "healthy"}
