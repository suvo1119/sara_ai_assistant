import logging
from duckduckgo_search import DDGS
from langchain.tools import tool

logger = logging.getLogger(__name__)

@tool
async def duckduckgo_search(query: str) -> str:
    """
    Searches DuckDuckGo and returns the top 3 results with heading and summary.
    No raw links are included to make speech output sound natural.
    
    Use this tool when the user asks a question that requires realtime information from the internet.
    """
    logger.info(f"DuckDuckGo Query received: {query}")
    
    try:
        results = DDGS().text(query, max_results=3)
        if not results:
            return "No results found on DuckDuckGo."
            
        formatted = "Here are the top results from DuckDuckGo:\n"
        for i, res in enumerate(results, start=1):
            title = res.get("title", "No title")
            body = res.get("body", "").strip()
            formatted += f"{i}. {title}. {body}\n\n"
            
        return formatted.strip()
        
    except Exception as e:
        logger.error(f"DuckDuckGo Search failed: {e}")
        return f"Search failed: {e}"
