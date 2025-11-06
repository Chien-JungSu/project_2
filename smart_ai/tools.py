# tools.py
import requests
import json
from config import GOOGLE_API_KEY, SEARCH_ENGINE_ID

def search_the_web(query: str) -> str:
    """
    Searches the web for a given query using the Google Custom Search API
    and returns a summarized list of results. Use this for questions about
    recent events, specific facts, or topics outside of common knowledge.
    """
    print(f"⚡ Performing web search for: '{query}'")
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': GOOGLE_API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': query,
        'num': 5 # Requesting top 5 results
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        search_results = response.json()

        if "items" not in search_results:
            return "No relevant search results found."

        # Process and simplify the results for the LLM
        summary_snippets = []
        for item in search_results.get("items", []):
            title = item.get("title", "No Title")
            snippet = item.get("snippet", "No Snippet").replace("\n", "")
            summary_snippets.append(f"Title: {title}\nSnippet: {snippet}")

        return "\n---\n".join(summary_snippets)

    except requests.exceptions.RequestException as e:
        return f"Error during web search: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
