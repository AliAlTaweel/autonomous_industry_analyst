# 🧠 Autonomous Industry Analyst

> A multi-agent AI system that simulates a professional research team — give it a topic, walk away, come back to a board-room-ready report.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/python-3.11-blue)
![CrewAI](https://img.shields.io/badge/orchestration-CrewAI-purple)
![LangChain](https://img.shields.io/badge/tools-LangChain-green)
![AWS](https://img.shields.io/badge/cloud-AWS-orange)
![Docker](https://img.shields.io/badge/container-Docker-2496ED)

---

## What It Does

Most AI tools are chatbots. This is a **research team**.

You submit a query like:

```
"Impact of EU Carbon Border Adjustment Mechanism on Finnish manufacturers"
```

And a crew of specialized agents gets to work:

| Agent | Role | What it does |
|---|---|---|
| 🎯 **Manager** | Research Director | Orchestrates the team, reviews quality, triggers critique loops |
| 🔍 **Researcher** | Senior Analyst | Scrapes news, queries APIs, gathers primary sources |
| 📊 **Analyst** | Technical & Financial | Interprets data, scores confidence, surfaces implications |
| ✍️ **Writer** | Communications Lead | Produces a structured, formatted, publishable report |

The defining feature: **agents critique each other's work.** If the Analyst's confidence score is too low, the Manager sends a specific critique back to the Researcher, who revises — and the cycle repeats until the output meets the quality threshold.

---

## Architecture

```
User Query
    │
    ▼
Manager Agent (CrewAI Hierarchical Process)
    │
    ├──▶ Researcher Agent
    │         Tools: Serper Search · RSS Feed Reader · Web Scraper
    │         Output: { sources, key_facts, data_points, gaps }
    │
    ├──▶ Analyst Agent
    │         Tools: Financial Parser · Trend Correlator · Risk Scorer
    │         Output: { implications, risks, opportunities, confidence_score }
    │
    ├──▶ [Critique Loop] ── confidence < 7.0 → loop back to Researcher
    │
    └──▶ Writer Agent
              Tools: Markdown Formatter · S3 Uploader
              Output: Structured .md report → S3 presigned URL
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Agent Orchestration | [CrewAI](https://www.crewai.com/) |
| Tool Framework | [LangChain](https://python.langchain.com/) |
| Web Scraping | Playwright (headless) |
| Financial Data | yfinance |
| Search | Serper.dev API |
| API Layer | FastAPI |
| Container | Docker |
| Registry | AWS ECR |
| Runtime | AWS App Runner |
| Storage | AWS S3 (presigned URLs) |
| Secrets | AWS Secrets Manager |
| Observability | AWS CloudWatch |

---

## Sample Reports

Pre-generated on real queries using the deployed system:

| Topic | Report |
|---|---|
| EU CBAM impact on Finnish manufacturers | 🔗 *Coming in Phase 4* |
| Nordic EV charging infrastructure gaps | 🔗 *Coming in Phase 4* |
| Autonomous port logistics in the Baltic Sea | 🔗 *Coming in Phase 4* |

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/alial-taweel/autonomous-industry-analyst.git
cd autonomous-industry-analyst

# 2. Install dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# → Fill in: OPENAI_API_KEY, SERPER_API_KEY

# 4. Run
python main.py "Impact of EU CBAM on Nordic steel manufacturers"
```

---

## API Usage (Phase 3+)

```bash
# Submit a research query
curl -X POST https://<live-url>/analyze \
  -H "Content-Type: application/json" \
  -d '{"query": "Nordic EV infrastructure gaps", "depth": "standard"}'

# Check status
curl https://<live-url>/analyze/{run_id}
```

---

## Project Structure

```
autonomous-industry-analyst/
├── agents/         ← Manager, Researcher, Analyst, Writer definitions
├── tasks/          ← CrewAI task definitions
├── tools/          ← LangChain custom tools (scraper, search, S3, etc.)
├── models/         ← Pydantic output contracts
├── app/            ← FastAPI REST API
├── tests/          ← Tool and agent unit tests
├── sample-reports/ ← Pre-generated reports for demo
├── docs/           ← PRD and phased execution plans
├── Dockerfile
├── docker-compose.yml
└── main.py
```

---

## Development Phases

| Phase | Description | Status |
|---|---|---|
| [Phase 1](./docs/phase-1-local-skeleton.md) | Local agent scaffold with mocked tools | 🔴 Not started |
| [Phase 2](./docs/phase-2-intelligence-layer.md) | Real tools + critique loop | 🔴 Not started |
| [Phase 3](./docs/phase-3-cloud-deployment.md) | Docker + AWS deployment | 🔴 Not started |
| [Phase 4](./docs/phase-4-portfolio-polish.md) | Sample reports + CI/CD + README polish | 🔴 Not started |

See [`docs/README.md`](./docs/README.md) for the full planning index.

---

## Why This Project

This system is designed to demonstrate production-grade AI engineering for industrial and public sector applications:

- **Agent orchestration** — not just prompt chaining, real hierarchical delegation
- **Tool-calling** — custom LangChain tools hitting real external APIs
- **Quality control loops** — agents critique each other before output is accepted
- **Cloud-native deployment** — containerized, IAM-secured, observable
- **State management** — structured Pydantic contracts between every agent handoff

---

## License

MIT

---

*Built by [Ali Al-Taweel](https://github.com/alial-taweel)*
