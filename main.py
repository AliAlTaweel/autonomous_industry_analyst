"""
main.py — Entry Point

Usage:
    python main.py "your research query"

Example:
    python main.py "Impact of EU CBAM on Nordic steel manufacturers"

Output:
    - Agent process log printed to stdout
    - Report saved to ./reports/<slug>.md
"""

import sys
import os
import time
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Ensure reports directory exists
Path("reports").mkdir(exist_ok=True)


def main():
    # ── Input validation ──────────────────────────────────────────
    if len(sys.argv) < 2:
        print("\n❌  Usage: python main.py \"your research query\"")
        print("   Example: python main.py \"Impact of EU CBAM on Nordic steel\"")
        sys.exit(1)

    query = " ".join(sys.argv[1:]).strip()

    if len(query) < 10:
        print("\n❌  Query too short. Please provide a meaningful research topic.")
        sys.exit(1)

    # ── Run ───────────────────────────────────────────────────────
    start_time = time.time()
    run_id = datetime.now().strftime("%Y%m%d-%H%M%S")

    print(f"\n[SYSTEM] Run ID: {run_id}")
    print(f"[SYSTEM] LLM Provider: {os.getenv('LLM_PROVIDER', 'ollama')}")
    print(f"[SYSTEM] Phase: 1 (Local Skeleton — Stub Tools)")

    # Import here to allow env vars to load first
    from crew import build_crew

    crew = build_crew(query)

    print("\n[SYSTEM] Kicking off crew...\n")

    result = crew.kickoff()

    # ── Summary ───────────────────────────────────────────────────
    elapsed = round(time.time() - start_time, 1)
    slug = query[:50].lower().replace(" ", "-").replace("/", "-")
    report_path = Path(f"reports/{slug}.md")

    print("\n" + "═" * 60)
    print("  ✅  RUN COMPLETE")
    print("═" * 60)
    print(f"  Run ID    : {run_id}")
    print(f"  Duration  : {elapsed}s")
    print(f"  Report    : {report_path}")
    print("═" * 60 + "\n")

    return result


if __name__ == "__main__":
    main()
