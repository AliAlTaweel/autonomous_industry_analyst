import os
import asyncio
from typing import Optional
from crewai.tools import tool
from .cache import tool_cache
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

@tool
@tool_cache() # Uses TOOL_CACHE_EXPIRE from .env
def web_scraper_tool(url: str) -> str:
    """
    Scrapes the content of a website using Playwright for high-fidelity extraction.
    Useful for sites that block traditional scrapers or require JavaScript.
    """
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            # Set a user-agent to avoid simple bot detection
            page.set_extra_http_headers({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            })
            
            # Navigate with a longer 60s timeout and a more reliable load condition
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=60000)
                # Wait briefly for dynamic content that might skip domcontentloaded
                page.wait_for_timeout(2000) 
            except Exception as timeout_error:
                # If it's a timeout, try to scrape whatever loaded anyway
                if "timeout" in str(timeout_error).lower():
                    pass # Continue to extract whatever is in the page buffer
                else:
                    raise timeout_error
            
            # Get content and clean it with BeautifulSoup
            html = page.content()
            browser.close()
            
            soup = BeautifulSoup(html, "html.parser")
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
                
            # Get text and clean up whitespace
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            clean_text = "\n".join(chunk for chunk in chunks if chunk)
            
            # Limit to ~6k characters to keep the prompt manageable for local LLMs
            return clean_text[:6000] 
            
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"
