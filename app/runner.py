import time
from pathlib import Path
from config.logger import logger

# In-memory dictionary to store the run status
# Format: { "run_id": {"status": "running" | "complete" | "failed", "report_path": "...", "error": "..."} }
RUNS = {}

def execute_run(run_id: str, query: str):
    """
    Executes the crew kickoff process synchronously but is called via a background task.
    """
    logger.info(f"[API] Starting background execution for {run_id} | Query: {query}")
    RUNS[run_id] = {"status": "running"}
    
    start_time = time.time()
    
    try:
        # Import inside the function to ensure any environment configurations load first
        from crew import build_crew
        crew = build_crew(query)
        logger.info(f"[API] Kicking off crew for run {run_id}...")
        
        # This is a long-running, blocking call
        crew.kickoff()
        
        elapsed = round(time.time() - start_time, 1)
        
        # Calculate expected output report path based on tasks/writing_task.py
        slug = query[:50].lower().replace(" ", "-").replace("/", "-")
        report_path = f"reports/{slug}.md"
        
        RUNS[run_id] = {
            "status": "complete",
            "report_path": report_path
        }
        
        logger.info(f"[API] Run {run_id} complete in {elapsed}s. Report saved to {report_path}")

    except Exception as e:
        logger.error(f"[API] Run {run_id} failed with error: {e}")
        RUNS[run_id] = {
            "status": "failed",
            "error": str(e)
        }
