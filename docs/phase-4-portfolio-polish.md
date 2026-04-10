# Phase 4 — Portfolio Polish

**Duration:** 2–3 days  
**Status:** 🔴 Not started  
**Prerequisite:** Phase 3 complete + 3 demo topics confirmed

---

## Goal

Make it impossible to ignore on a CV or in a recruiter conversation. This phase is about **presentation**, not functionality.

---

## What to Build

### 4a — 3 Pre-Generated Sample Reports

Run the system on 3 Reaktor-relevant topics and save the outputs:

| # | Query | Why Reaktor Cares |
|---|---|---|
| 1 | EU Carbon Border Adjustment Mechanism impact on Finnish manufacturers | Public policy + industrial sector |
| 2 | Nordic EV charging infrastructure investment gaps 2025 | Industrial + sustainability |
| 3 | Autonomous port logistics in the Baltic Sea | Industrial operations + automation |

**Save outputs to:**
```
autonomous-industry-analyst/
└── sample-reports/
    ├── eu-cbam-finnish-manufacturing.md
    ├── nordic-ev-infrastructure.md
    └── baltic-port-logistics.md
```

Also upload to S3 with permanent (non-expiring) public read access for recruiter links.

### 4b — Process Log Showcase

From one of the 3 real runs, extract the most compelling critique loop log:

```
sample-reports/
└── process-log-example.txt    ← annotated with comments explaining each step
```

**What to highlight:**
- The moment the Manager rejected the Analyst's output
- The specific critique note sent back
- How the revised analysis differed (delta)
- Final approval and confidence score jump

> This is the file you keep open during an interview.

### 4c — GitHub README

Must include in this order:

- [ ] One-liner pitch ("Multi-agent research system that generates board-room-ready industry reports autonomously")
- [ ] Animated terminal GIF showing agent process log running live
- [ ] Architecture diagram (Mermaid or PNG)
- [ ] "Live Demo →" button linking to a sample report on S3
- [ ] Tech stack badges (CrewAI, LangChain, AWS, Docker, Python)
- [ ] Quick start: `git clone` + `.env` setup + `python main.py "your query"`
- [ ] Sample report preview (collapsed `<details>` block)
- [ ] Link to process log example

### 4d — GitHub Actions CI/CD

```yaml
# .github/workflows/deploy.yml
name: Build & Deploy

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.AWS_DEPLOY_ROLE_ARN }}
          aws-region: eu-north-1
      - name: Login to ECR
        uses: aws-actions/amazon-ecr-login@v2
      - name: Build and push image
        run: |
          docker build -t industry-analyst .
          docker tag industry-analyst $ECR_URI:$GITHUB_SHA
          docker push $ECR_URI:$GITHUB_SHA
      - name: Trigger App Runner redeploy
        run: aws apprunner start-deployment --service-arn ${{ secrets.APP_RUNNER_ARN }}
```

### 4e — CloudWatch Dashboard Screenshot

Take a screenshot of a real run's CloudWatch logs showing:
- Agent switching (Manager → Researcher → Analyst)
- The critique loop firing
- Total run duration

Save to `docs/assets/cloudwatch-demo.png` and embed in README.

---

## Final File Tree (end of Phase 4)

```
autonomous-industry-analyst/
├── agents/
├── app/
├── models/
├── tasks/
├── tools/
├── tests/
├── sample-reports/
│   ├── eu-cbam-finnish-manufacturing.md
│   ├── nordic-ev-infrastructure.md
│   ├── baltic-port-logistics.md
│   └── process-log-example.txt
├── docs/
│   ├── README.md
│   ├── PRD.md
│   ├── phase-1-local-skeleton.md
│   ├── phase-2-intelligence-layer.md
│   ├── phase-3-cloud-deployment.md
│   ├── phase-4-portfolio-polish.md
│   └── assets/
│       ├── architecture.png
│       └── cloudwatch-demo.png
├── .github/
│   └── workflows/
│       └── deploy.yml
├── Dockerfile
├── docker-compose.yml
├── crew.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Done When

- [ ] 3 sample reports in repo + live S3 links
- [ ] README has GIF, architecture diagram, and live demo link
- [ ] CI/CD deploys automatically on push to `main`
- [ ] Process log example is annotated and ready to discuss in interviews

---

## Recruiter Signal

> "Walk me through what happened here between the Manager and the Analyst."  
> That question, in an interview, is a win. This phase makes that question inevitable.

---

*Previous: [Phase 3](./phase-3-cloud-deployment.md) | Back to [docs/README.md](./README.md)*
