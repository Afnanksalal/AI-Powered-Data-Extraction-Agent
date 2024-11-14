from serpapi import GoogleSearch

class SerpAPIError(Exception):
    """Custom exception for SerpAPI errors."""
    pass

def search_and_extract(query, config):
    """Performs a web search using SerpAPI and returns the organic results.

    Args:
        query (str): The search query.
        config (dict): Configuration dictionary containing the SerpAPI key.

    Returns:
        list: A list of organic search results (dictionaries).
        Raises SerpAPIError if there's an issue with the SerpAPI call.
    """
    try:
        search = GoogleSearch({"q": query, "api_key": config["serpapi_api_key"]})
        results = search.get_json()
        return results.get("organic_results", [])
    except Exception as e:
        raise SerpAPIError(f"SerpAPI Search Error: {e}") from e
