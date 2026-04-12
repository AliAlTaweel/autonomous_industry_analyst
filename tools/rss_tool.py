import feedparser
import json
from crewai.tools import tool

@tool
def rss_feed_tool(topic: str) -> str:
    """
    Fetches and parses industrial RSS feeds for a given topic.
    Returns a JSON string with the most relevant news items.
    """
    feeds = [
        "https://www.ft.com/manufacturing?format=rss",
        "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml",
        "https://feeds.reuters.com/reuters/businessNews"
    ]
    
    results = []
    
    for url in feeds:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]: # Limit to top 5 per feed
                if topic.lower() in entry.title.lower() or topic.lower() in entry.summary.lower():
                    results.append({
                        "title": entry.title,
                        "link": entry.link,
                        "published": getattr(entry, 'published', 'Unknown Date'),
                        "source": feed.feed.title if hasattr(feed, 'feed', 'title') else "Unknown Source"
                    })
        except Exception as e:
            continue
            
    if not results:
        return f"No recent RSS items found for topic: {topic}"
        
    return json.dumps(results, indent=2)
