# tools package
from .ddg_tool import duckduckgo_search_tool
from .rss_tool import rss_feed_tool
from .web_scraper_tool import web_scraper_tool
from .financial_tool import fetch_financials
from .trend_tool import analyze_trends
from .risk_tool import assess_risks

# Map duckduckgo to serper_search_tool name if we want to avoid agent changes,
# but it's cleaner to use the actual name.
# Here we'll export both or just the new one.

__all__ = [
    "web_scraper_tool",
    "duckduckgo_search_tool",
    "rss_feed_tool",
    "fetch_financials",
    "analyze_trends",
    "assess_risks",
]
