import yfinance as yf
import json
from crewai.tools import tool
from .cache import tool_cache

@tool
@tool_cache() # Uses TOOL_CACHE_EXPIRE from .env
def fetch_financials(company_name: str) -> str:
    """
    Fetches financial data for a given company name or stock ticker using Yahoo Finance.
    Returns market cap, revenue trend, and recent performance summary.
    """
    try:
        # Attempt to find ticker if company name is provided
        ticker_obj = yf.Ticker(company_name)
        info = ticker_obj.info
        
        # If the direct lookup didn't work, maybe we need a search (though yfinance is better for tickers)
        # For professional use, one might use a search to resolve company -> ticker first.
        
        data = {
            "symbol": info.get("symbol"),
            "longName": info.get("longName"),
            "marketCap": info.get("marketCap"),
            "trailingPE": info.get("trailingPE"),
            "forwardPE": info.get("forwardPE"),
            "revenueGrowth": info.get("revenueGrowth"),
            "operatingMargins": info.get("operatingMargins"),
            "businessSummary": info.get("longBusinessSummary", "No summary available")[:500]
        }
        
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error fetching financial data for {company_name}: {str(e)}"
