# 📚 Autonomous Industry Analyst — Documentation

This folder contains all planning, architecture, and execution documents for the project.

## Index

| File | Description |
|---|---|
| [`PRD.md`](./PRD.md) | Full Product Requirements Document |
| [`phase-1-local-skeleton.md`](./phase-1-local-skeleton.md) | Agent scaffold, mocked tools, local pipeline |
| [`phase-2-intelligence-layer.md`](./phase-2-intelligence-layer.md) | Real tools, critique loop, structured outputs |
| [`phase-3-cloud-deployment.md`](./phase-3-cloud-deployment.md) | Docker, AWS (ECR + App Runner + S3), live API |
| [`phase-4-portfolio-polish.md`](./phase-4-portfolio-polish.md) | Sample reports, README, CI/CD, recruiter artifacts |

## Decision Gates

Before starting each phase, the following must be resolved:

| Gate | Question | Decision |
|---|---|---|
| 0 → 1 | LLM provider? | ✅ **Ollama + Llama** (dev) → GPT-4o / Claude (prod) |
| 0 → 1 | Serper API key available? | ⏳ Pending (Phase 2) |
| 2 → 3 | Deployment target: App Runner or ECS Fargate? | ⏳ Pending |
| 3 → 4 | 3 demo query topics confirmed? | ⏳ Pending |

## Phase Status

| Phase | Status |
|---|---|
| Phase 1 — Local Skeleton | 🔴 Not started |
| Phase 2 — Intelligence Layer | 🔴 Not started |
| Phase 3 — Cloud Deployment | 🔴 Not started |
| Phase 4 — Portfolio Polish | 🔴 Not started |
