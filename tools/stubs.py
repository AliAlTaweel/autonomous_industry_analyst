"""
tools/stubs.py — Phase 1 Stub Tools

All tools return realistic but hardcoded fake data.
Goal: prove the agent pipeline works before wiring real APIs.

PHASE 2: each function here gets replaced with a real implementation
in a separate file (e.g., tools/serper_tool.py). Stubs are preserved
as a fallback for offline testing.
"""

import json
from crewai.tools import tool


@tool
def web_scraper_tool(url: str) -> str:
    """
    Scrapes a given URL and returns structured article content.
    STUB: returns realistic fake data for pipeline testing.
    """
    return json.dumps({
        "url": url,
        "title": "EU Announces Stricter Emission Targets for Heavy Industry",
        "date": "2025-03-15",
        "author": "Reuters Manufacturing Desk",
        "content": (
            "The European Commission unveiled binding emission targets for heavy industry, "
            "mandating a 45% reduction in carbon output by 2030. Nordic steel producers face "
            "immediate pressure to upgrade Blast Furnace (BF) technology or transition to "
            "Electric Arc Furnace (EAF) systems. Capital expenditure requirements are estimated "
            "at €2.3B across the sector. SSAB and Outokumpu are positioned as early movers, "
            "having already invested in hydrogen-based direct reduced iron (H-DRI) pilots."
        ),
        "reliability": "high",
        "_stub": True
    }, indent=2)


@tool
def serper_search_tool(query: str) -> str:
    """
    Searches the web for recent news and returns top results.
    STUB: returns realistic fake search results.
    """
    return json.dumps({
        "query": query,
        "results": [
            {
                "title": "Nordic Steel Giants Accelerate Hydrogen DRI Transition",
                "url": "https://ft.com/content/stub-001",
                "snippet": (
                    "SSAB and Outokumpu are accelerating hydrogen-based steelmaking pilots "
                    "after the EU confirmed CBAM Phase 2 enforcement dates."
                ),
                "date": "2025-03-10",
                "source": "Financial Times"
            },
            {
                "title": "EU CBAM Phase 2 Creates Immediate Supply Chain Pressure",
                "url": "https://bloomberg.com/content/stub-002",
                "snippet": (
                    "Carbon Border Adjustment Mechanism enters enforcement phase for steel "
                    "imports, raising costs for non-compliant EU trading partners by 18-24%."
                ),
                "date": "2025-03-08",
                "source": "Bloomberg"
            },
            {
                "title": "Finnish Government Commits €400M to Industrial Decarbonization",
                "url": "https://hs.fi/content/stub-003",
                "snippet": (
                    "Business Finland allocates €400M for green steel and clean energy "
                    "industrial programs. SSAB's Raahe plant first in line."
                ),
                "date": "2025-03-05",
                "source": "Helsingin Sanomat"
            },
            {
                "title": "Outokumpu Q1 Guidance: CBAM Compliance Cost Absorbed",
                "url": "https://reuters.com/content/stub-004",
                "snippet": (
                    "Outokumpu raised full-year guidance, citing early CBAM compliance as a "
                    "competitive differentiator vs. Asian steel imports."
                ),
                "date": "2025-03-02",
                "source": "Reuters"
            }
        ],
        "_stub": True
    }, indent=2)


@tool
def rss_feed_tool(topic: str) -> str:
    """
    Fetches recent RSS feed items for a given topic from curated industrial sources.
    STUB: returns realistic fake feed items.
    """
    return json.dumps({
        "topic": topic,
        "feeds_polled": [
            "FT Manufacturing",
            "Industrial Automation World",
            "EU Policy Watch",
            "Bloomberg Industries"
        ],
        "items": [
            {
                "title": "Wärtsilä Partners with Port of Helsinki on Autonomous Cargo Logistics",
                "source": "Industrial Automation World",
                "date": "2025-03-12",
                "url": "https://industrialautomationworld.com/stub-001",
                "summary": (
                    "Wärtsilä's autonomous vessel navigation system will be deployed at the "
                    "Port of Helsinki for a 12-month pilot starting Q3 2025."
                )
            },
            {
                "title": "EU Industrial Policy: New State Aid Rules for Green Tech",
                "source": "EU Policy Watch",
                "date": "2025-03-11",
                "url": "https://eupolicywatch.eu/stub-002",
                "summary": (
                    "Updated State Aid framework allows member states to front-load subsidies "
                    "for industrial decarbonization projects up to €500M without prior approval."
                )
            }
        ],
        "_stub": True
    }, indent=2)


@tool
def financial_parser_tool(company_name: str) -> str:
    """
    Returns a financial snapshot for a given company name or stock ticker.
    STUB: returns realistic fake financial data.
    """
    return json.dumps({
        "company": company_name,
        "ticker": "SSAB-A.ST",
        "market_cap": "€4.8B",
        "revenue_trend": "+12.3% YoY",
        "ebitda_margin": "18.4%",
        "pe_ratio": 11.2,
        "debt_to_equity": 0.43,
        "recent_filing_summary": (
            "Q4 2024 results: Revenue €2.1B (+11% YoY). Green steel premium pricing "
            "added €180M to top line. Fossil-free steel production reached 8% of total output."
        ),
        "analyst_consensus": "Overweight",
        "price_target": "€8.40 (vs. current €7.10)",
        "_stub": True
    }, indent=2)


@tool
def trend_correlator_tool(events: str) -> str:
    """
    Correlates a list of events with historical market and sector movement data.
    STUB: returns realistic fake correlation analysis.
    """
    return json.dumps({
        "input_events": events,
        "correlation_score": 0.74,
        "confidence": "medium-high",
        "narrative": (
            "Regulatory announcements around CBAM have historically preceded 12-18 month "
            "capital expenditure cycles in Nordic industrial companies. Analysis of the past "
            "3 EU environmental policy cycles shows a consistent pattern: early-mover companies "
            "capture 15-22% stock appreciation vs. sector laggards within 24 months of "
            "compliance milestone announcements."
        ),
        "comparable_events": [
            "EU ETS Phase 3 announcement (2012) → SSAB +18% in 18 months",
            "Paris Agreement ratification (2016) → Nordic industrials outperformed EU index by 9%"
        ],
        "_stub": True
    }, indent=2)


@tool
def risk_scorer_tool(topic: str) -> str:
    """
    Scores a research topic across key risk dimensions: regulatory, market, execution, geopolitical.
    STUB: returns realistic fake risk matrix.
    """
    return json.dumps({
        "topic": topic,
        "risk_matrix": [
            {
                "dimension": "regulatory",
                "score": 7.5,
                "severity": "High",
                "rationale": "CBAM enforcement timelines are aggressive; non-compliance fines escalate quarterly."
            },
            {
                "dimension": "market_timing",
                "score": 6.0,
                "severity": "Medium",
                "rationale": "Green steel demand is established but premium pricing remains fragile in downturns."
            },
            {
                "dimension": "execution",
                "score": 5.5,
                "severity": "Medium",
                "rationale": "H-DRI technology is proven at pilot scale but industrial rollout carries capex risk."
            },
            {
                "dimension": "geopolitical",
                "score": 3.5,
                "severity": "Low",
                "rationale": "Nordic region operates in a stable, predictable policy environment."
            }
        ],
        "overall_risk": "Moderate (5.6/10)",
        "recommendation": "Proceed with analysis — risk levels are manageable with proper hedging.",
        "_stub": True
    }, indent=2)
