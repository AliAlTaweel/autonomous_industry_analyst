# 📋 Product Requirements Document (PRD)
### Autonomous Industry Analyst

**Version:** 1.0  
**Status:** Draft  
**Author:** Ali Al-Taweel  
**Date:** April 2026  
**Target Audience:** Recruiters · Engineering Teams · Reaktor Hiring Committee

---

## 1. Executive Summary

**Autonomous Industry Analyst** is a multi-agent AI system that simulates a professional research team. Given a company name, industry vertical, or a free-form research question, the system autonomously dispatches specialized agents to gather intelligence, critically analyze findings, and synthesize a structured, publishable-grade report — saved to S3 for retrieval and sharing.

> **The elevator pitch:** "Give it a topic. Walk away. Come back to a board-room-ready report."

---

## 2. Problem Statement

Professionals in industrial, public, and enterprise sectors spend enormous time on manual research:

- Scanning 10+ news sources to track sector developments
- Manually correlating technical news with financial signals
- Formatting raw findings into digestible reports for stakeholders

This is exactly the kind of repetitive, high-cognitive-load work that a well-designed multi-agent system can automate — while demonstrating a recruiter-facing signal: **I can build systems that think, not just respond.**

---

## 3. Goals & Non-Goals

### ✅ Goals
- Build a working end-to-end pipeline from query → agents → report → S3
- Demonstrate meaningful agent collaboration (not just sequential LLM calls)
- Show inter-agent **critique and revision loops**
- Deploy on AWS in a containerized, reproducible way
- Generate recruiter-facing artifacts: process logs, sample reports, architecture diagrams

### ❌ Non-Goals
- Real-time streaming UI (v1 is CLI/API-first)
- Financial trading signals or investment advice
- Multi-tenant SaaS (single-user developer tooling for now)
- Fine-tuned domain models (uses general LLMs + specialized tools)

---

## 4. System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER / API CALL                          │
│              { "query": "EV battery supply chain 2025" }        │
└─────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MANAGER AGENT (CrewAI)                       │
│  • Parses research intent                                       │
│  • Delegates tasks to worker agents                             │
│  • Collects outputs and triggers critique loop                  │
│  • Final approval gate before report generation                 │
└────────────┬───────────────────────────┬────────────────────────┘
             │                           │
             ▼                           ▼
┌────────────────────┐       ┌───────────────────────┐
│  RESEARCHER AGENT  │       │   ANALYST AGENT        │
│  Tools:            │──────▶│  Tools:                │
│  • Web Scraper     │       │  • Financial parser    │
│  • RSS Feed reader │       │  • Trend correlator    │
│  • Serper API      │       │  • Risk scorer         │
└────────────────────┘       └──────────┬────────────┘
                                        │
                                        ▼
                          ┌─────────────────────────┐
                          │   WRITER AGENT           │
                          │  Tools:                  │
                          │  • Markdown formatter    │
                          │  • S3 uploader           │
                          └──────────────────────────┘
```

### Critique Loop
```
Analyst → critiques Researcher output → Researcher revises → Writer drafts
Writer → Manager reviews draft → triggers re-analysis if confidence < 7.0
Manager → approves or loops (max 2 iterations)
```

---

## 5. Agent Definitions

### Manager Agent
| Property | Value |
|---|---|
| **Role** | Research Director |
| **Goal** | Ensure the final report is accurate, well-sourced, and actionable |
| **LLM** | GPT-4o / Claude 3.5 Sonnet |
| **Process** | Hierarchical (`Process.hierarchical`) |

### Researcher Agent
| Property | Value |
|---|---|
| **Role** | Senior Industry Researcher |
| **Goal** | Gather current, relevant, and credible raw intelligence |
| **Tools** | `WebScraperTool`, `SerperSearchTool`, `RSSFeedTool` |
| **Output** | `{ sources[], key_facts[], data_points[], gaps[] }` |

### Analyst Agent
| Property | Value |
|---|---|
| **Role** | Technical & Financial Analyst |
| **Goal** | Interpret raw data and surface strategic implications |
| **Tools** | `FinancialParserTool`, `TrendCorrelatorTool`, `RiskScorerTool` |
| **Output** | `{ implications[], risks[], opportunities[], confidence_score }` |

### Writer Agent
| Property | Value |
|---|---|
| **Role** | Research Communications Lead |
| **Goal** | Transform analysis into a board-room-ready report |
| **Tools** | `MarkdownFormatterTool`, `S3UploaderTool` |
| **Output** | `.md` report uploaded to S3 |

---

## 6. Report Output Schema

```markdown
# [TOPIC] — Autonomous Industry Analysis
**Generated:** {timestamp} | **Confidence:** {score}/10 | **Run ID:** {uuid}

## Executive Summary
## Key Findings        ← table with source + confidence
## Financial Implications
## Risk Matrix         ← severity × likelihood
## Strategic Opportunities ← time-horizon tagged
## Sources & Citations
## Agent Process Log   ← the recruiter gold
```

---

## 7. AWS Infrastructure

| Service | Purpose |
|---|---|
| **ECR** | Container image registry |
| **App Runner / ECS** | Serverless container execution |
| **S3** | Report storage + presigned URLs (7-day expiry) |
| **IAM** | Role-based access (no hardcoded keys) |
| **CloudWatch** | Agent execution logs |
| **Secrets Manager** | API keys (OpenAI, Serper) |

---

## 8. Success Metrics

| Metric | Target |
|---|---|
| End-to-end generation time | < 5 minutes |
| Minimum confidence score | ≥ 7.0 / 10 |
| Source diversity per report | ≥ 5 unique domains |
| Critique loop trigger rate | ~30% of runs |
| Docker image size | < 1.2 GB |

---

## 9. Open Questions

1. **LLM Provider:** GPT-4o vs Claude 3.5 Sonnet?
2. **Deployment target:** App Runner vs ECS Fargate?
3. **Demo queries:** 3 Reaktor-relevant topics to pre-generate?
4. **Process logs:** Inline in report or separate S3 file?

---

*See [`docs/README.md`](./README.md) for phase execution plan.*
