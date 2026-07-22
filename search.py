import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])



def web_search(query: str, max_results: int = 5):
    """
    Search the web and return a list of dicts:
    [{title, url, content}, ...]
    """
    
    response = client.search(
        query=query,
        max_results=max_results,
        search_depth="advanced"
    )
    results = []
    for r in response.get("results", []):
        results.append({
            "title": r.get("title", ""),
            "url": r.get("url", ""),
            "content": r.get("content", "")
        })
    return results


if __name__ == "__main__":
    # quick manual test
    import json
    results = web_search("latest developments in fusion energy")
    print(json.dumps(results, indent=2))