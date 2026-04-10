# Phase 1 — Local Skeleton

**Duration:** 3–4 days  
**Status:** 🔴 Not started  
**LLM (dev):** Ollama + Llama (local) — swap to GPT-4o / Claude via `.env` for prod  
**Prerequisite:** Ollama installed + a Llama model pulled (`ollama pull llama3.2`)

---

## Goal

Get all 4 agents talking to each other in a working pipeline — **no real tools, no cloud, no distractions.** Prove the agent graph before touching a single external API.

---

## What to Build

### 1. Project Scaffold
```
autonomous-industry-analyst/
├── agents/
│   ├── __init__.py
│   ├── manager.py
│   ├── researcher.py
│   ├── analyst.py
│   └── writer.py
├── tasks/
│   ├── __init__.py
│   ├── research_task.py
│   ├── analysis_task.py
│   ├── critique_task.py
│   └── writing_task.py
├── tools/
│   ├── __init__.py
│   └── stubs.py          ← ALL tools return hardcoded fake data here
├── config/
│   └── llm.py            ← LLM factory (Ollama dev / OpenAI prod)
├── crew.py               ← Wires agents + tasks into CrewAI
├── main.py               ← Entry: python main.py "your query"
├── .env.example          ← Template: OLLAMA_MODEL, OLLAMA_BASE_URL, LLM_PROVIDER
├── requirements.txt
└── docs/                 ← (this folder)
```

### LLM Config Pattern (`config/llm.py`)
```python
# Reads LLM_PROVIDER from .env
# "ollama" (default for dev) → talks to local Ollama
# "openai" or "anthropic"   → uses API key from .env (prod)
#
# Agents never import the LLM directly — always go through get_llm()
```

### `.env.example`
```bash
# LLM config
LLM_PROVIDER=ollama              # ollama | openai | anthropic
OLLAMA_MODEL=llama3.2            # or llama3.1, mistral, etc.
OLLAMA_BASE_URL=http://localhost:11434

# Production (leave empty in dev)
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
```

### 2. Agent Definitions (agents/)
- Define all 4 agents with roles, goals, and backstories
- Attach stub tools (not real tools)
- Use `Process.hierarchical` for Manager orchestration

### 3. Tasks (tasks/)
- `ResearchTask` → assigned to Researcher
- `AnalysisTask` → assigned to Analyst, reads Researcher output
- `CritiqueTask` → assigned to Manager (decision gate)
- `WritingTask` → assigned to Writer

### 4. Critique Logic (simplified for Phase 1)
- Hardcode `confidence_score = 8.5` in stub output
- Manager always approves (loop doesn't fire yet)
- Just verify the flow reaches the Writer

### 5. Logging
- Print each agent handoff to stdout with a clear prefix:
```
[MANAGER]    Delegating research task...
[RESEARCHER] Starting intelligence gathering...
[RESEARCHER] → Returning stub data (Phase 1)
[ANALYST]    Analyzing research output...
[ANALYST]    → Confidence score: 8.5
[MANAGER]    Score ≥ 7.0. Approving for writing.
[WRITER]     Drafting report...
[WRITER]     → Report saved to ./reports/draft.md
```

---

## What to Skip

| Item | Reason |
|---|---|
| Real web scraping | Too much noise while wiring agents |
| S3 / AWS | Phase 3 concern |
| FastAPI server | Phase 3 concern |
| Actual critique loop | Phase 2 concern |
| Docker | Phase 3 concern |

---

## Done When

```bash
python main.py "EV battery supply chain"
```
Prints the full agent log above and saves a stub report to `./reports/`.

---

## Recruiter Signal

> You can show the **agent graph and reasoning flow** before any tool is wired up. This demonstrates top-down system design — you architect first, implement second.

---

*Next: [Phase 2 — Intelligence Layer](./phase-2-intelligence-layer.md)*
