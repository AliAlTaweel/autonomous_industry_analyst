# Phase 2 — Intelligence Layer

**Duration:** 4–5 days  
**Status:** 🔴 Not started  
**Prerequisite:** Phase 1 complete + Serper API key available

---

## Goal

Replace every stub with a real LangChain tool. Add the critique loop with dynamic confidence scoring. Make the output actually useful and interesting to read.

---

## What to Build

### 2a — Real LangChain Tools (build and test in isolation first)

Build each tool as a standalone testable unit before wiring into an agent:

| Order | Tool | Input | External Dependency |
|---|---|---|---|
| 1st | `SerperSearchTool` | query string | Serper.dev API key |
| 2nd | `RSSFeedTool` | topic keywords | Public RSS feeds (no key) |
| 3rd | `WebScraperTool` | URL | `playwright` (headless) |
| 4th | `FinancialParserTool` | company name / ticker | `yfinance` (no key) |
| 5th | `TrendCorrelatorTool` | events list | Internal logic only |
| 6th | `RiskScorerTool` | topic dict | LLM call |
| 7th | `S3UploaderTool` | file path | **Stub as local save for now** (Phase 3) |

### Tool Test Pattern
Each tool gets a standalone test before agent wiring:
```bash
python tools/test_serper.py "Nordic EV infrastructure"
# → prints top 10 results cleanly
```

### 2b — Structured Output Contracts

Replace free-form agent text with typed Pydantic models:

```python
# models/researcher_output.py
class ResearchOutput(BaseModel):
    sources: list[str]
    key_facts: list[str]
    data_points: list[dict]
    gaps: list[str]

# models/analyst_output.py
class AnalysisOutput(BaseModel):
    implications: list[str]
    risks: list[dict]
    opportunities: list[dict]
    confidence_score: float    # 0.0 – 10.0
```

### 2c — Real Critique Loop

```
Analyst produces AnalysisOutput with confidence_score
    │
    ├─ confidence_score ≥ 7.0
    │       └─ Manager approves → Writer drafts
    │
    └─ confidence_score < 7.0
            └─ Manager sends critique note back to Researcher
                    └─ Researcher revises with more targeted search
                            └─ Analyst re-analyzes
                                    └─ Max 2 loops, then force-approve
```

**Log the critique verbosely:**
```
[MANAGER]    Confidence score: 5.8 — below threshold.
[MANAGER]    Critique: "Insufficient primary sources on EU regulatory timeline.
             Researcher should specifically search CBAM implementation dates."
[RESEARCHER] Received critique. Revising research focus...
[RESEARCHER] → New targeted query: "EU CBAM implementation schedule 2026"
[ANALYST]    Re-analyzing revised research...
[ANALYST]    → New confidence score: 8.1. Approved.
```

---

## Folder Changes from Phase 1

```
autonomous-industry-analyst/
├── agents/           ← same, but now tools are real
├── tasks/            ← same
├── tools/
│   ├── stubs.py            ← keep for fallback testing
│   ├── serper_tool.py      ← NEW
│   ├── rss_tool.py         ← NEW
│   ├── web_scraper_tool.py ← NEW
│   ├── financial_tool.py   ← NEW
│   ├── trend_tool.py       ← NEW
│   ├── risk_tool.py        ← NEW
│   └── s3_tool.py          ← saves locally for now
├── models/
│   ├── researcher_output.py ← NEW
│   └── analyst_output.py    ← NEW
├── tests/
│   ├── test_serper.py       ← NEW
│   ├── test_rss.py          ← NEW
│   └── test_scraper.py      ← NEW
└── reports/                 ← real reports land here
```

---

## What to Skip

| Item | Reason |
|---|---|
| Real S3 upload | Phase 3 — use local `./reports/` save |
| Docker | Phase 3 |
| FastAPI | Phase 3 |

---

## Done When

```bash
python main.py "Impact of EU CBAM on Nordic steel manufacturers"
```

- Real articles are scraped from industrial news sources
- Critique loop fires (or logs clearly why it didn't)
- A real `.md` report is saved to `./reports/`
- The process log is verbose and tells a story

---

## Recruiter Signal

> **The critique loop logs are the most important thing in this entire project.** Print them verbosely. This is the line that separates "ChatGPT wrapper" from "AI systems engineer."

---

*Previous: [Phase 1](./phase-1-local-skeleton.md) | Next: [Phase 3 — Cloud Deployment](./phase-3-cloud-deployment.md)*
