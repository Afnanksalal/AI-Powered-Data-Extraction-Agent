import re
from groq import Groq

class GroqError(Exception):
    """Custom exception for Groq LLM errors."""
    pass

def process_with_llm(query, search_results, config):
    """Processes a query with the Groq LLM, using provided search results.

    Args:
        query (str): The original search query.
        search_results (str):  The formatted string of search results.
        config (dict): Configuration dictionary containing the Groq API key.

    Returns:
        str: The plain text response from the LLM.
        Raises GroqError if there's an issue with the Groq API call.
    """
    try:
        client = Groq(api_key=config["groq_api_key"])

        refined_query = f"""
        Instructions: Extract the answer to the following question ONLY from the provided search results. Do not generate any text on your own.

        Question: {query}

        Search Results:
        {search_results}

        Output Format:
        * Give ONLY the specific information requested.  Do not provide introductory phrases.
        * No explanations, paragraphs, lists, or styling. Just plain text.
        * If you cannot find the information, output "Information not found in search results."
        """

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": refined_query}],
            model="llama3-8b-8192"
        )

        raw_text = response.choices[0].message.content.strip()
        plain_text = re.sub(r"[_*`~\[\]()]", "", raw_text)  # Remove Markdown styling
        return plain_text

    except Exception as e:
        raise GroqError(f"Groq LLM Error: {e}") from e
