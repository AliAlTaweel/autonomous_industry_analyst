import json
import warnings
import time
import random
from crewai.tools import tool

# Suppress the duckduckgo_search renaming warning to keep logs clean
warnings.filterwarnings("ignore", category=RuntimeWarning, module="duckduckgo_search")

from ddgs import DDGS
from config.logger import logger

@tool
def duckduckgo_search_tool(query: str) -> str:
    """
    Search the web using DuckDuckGo to get the most recent and relevant news.
    Returns a JSON string containing the title, link, and snippet of the top results.
    """
    logger.info(f"Searching DuckDuckGo for: {query}")
    
    max_retries = 3
    retry_delay = 2  # base delay in seconds
    
    for attempt in range(max_retries):
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                with DDGS() as ddgs:
                    # Use news() for more relevant, timely results on industry topics
                    # Some versions of DDGS might return a generator, some return a list.
                    results_gen = ddgs.news(query, max_results=5)
                    results = list(results_gen)
                    
                    # If news is empty, fallback to regular text search
                    if not results:
                        results = list(ddgs.text(query, max_results=5))
                    
                    search_results = []
                    for r in results:
                        search_results.append({
                            "title": r.get("title"),
                            "url": r.get("href") or r.get("url"),
                            "snippet": r.get("body") or r.get("snippet")
                        })
                    
                    if not search_results:
                        logger.warning(f"No results found for query: {query}")
                        return "Search tool called but no results were found. Try a broader search query."
                    
                    logger.debug(f"Found {len(search_results)} results for query: {query} (Attempt {attempt + 1})")
                    return json.dumps(search_results, indent=2)

        except Exception as e:
            error_msg = str(e)
            if "403" in error_msg or "Ratelimit" in error_msg:
                if attempt < max_retries - 1:
                    # Exponential backoff with jitter
                    sleep_time = (retry_delay ** (attempt + 1)) + random.uniform(0, 1)
                    logger.warning(f"DuckDuckGo rate limited (403). Retrying in {sleep_time:.2f}s... (Attempt {attempt + 1}/{max_retries})")
                    time.sleep(sleep_time)
                    continue
                else:
                    logger.error(f"DuckDuckGo search failed after {max_retries} attempts: {error_msg}")
                    return f"Error: DuckDuckGo is currently rate-limiting searches. Try again later or use the Serper tool if available. Details: {error_msg}"
            else:
                logger.error(f"DuckDuckGo search failed: {error_msg}")
                return f"Error performing DuckDuckGo search: {error_msg}"
