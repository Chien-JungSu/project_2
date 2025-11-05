import os
import google.generativeai as genai
from googleapiclient.discovery import build



# --- Configuration ---
# IMPORTANT: Set these environment variables in your terminal before running the script.
# For example:
# export GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
# export SEARCH_API_KEY="YOUR_CUSTOM_SEARCH_API_KEY"
# export SEARCH_ENGINE_ID="YOUR_SEARCH_ENGINE_ID"

# Configure the Gemini API
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# --- Tool Definition: Web Search ---
def google_search(query: str) -> list[dict]:
    """
    Performs a Google search using the Custom Search JSON API and returns formatted results.

    Args:
        query: The search query string.

    Returns:
        A list of dictionaries, each containing the 'title', 'link', and 'snippet'
        of a search result. Returns an empty list if an error occurs.
    """
    print(f"⚡ Performing search for: '{query}'")
    try:
        search_api_key = os.environ.get("SEARCH_API_KEY")
        search_engine_id = os.environ.get("SEARCH_ENGINE_ID")

        # Build the search service
        service = build("customsearch", "v1", developerKey=search_api_key)
        
        # Execute the search
        res = service.cse().list(q=query, cx=search_engine_id, num=5).execute() # Get top 5 results

        # Format the results
        if 'items' in res:
            print("💡 Raw search results found:")
            formatted_results = [
                {
                    "title": item.get("title"),
                    "link": item.get("link"),
                    "snippet": item.get("snippet"),
                }
                for item in res["items"]
            ]
            print("💡 Raw search results found:")
            print(formatted_results)
            return formatted_results
        else:
            return []
            
    except Exception as e:
        print(f"⚠️ An error occurred during search: {e}")
        return []


# --- Agent Setup ---
# 1. Create the generative model
model = genai.GenerativeModel(
    model_name='gemini-2.0-flash-lite',
    tools=[google_search] # Register the search function as a tool
)

# 2. Start a chat session with the model
chat = model.start_chat(enable_automatic_function_calling=True)
print("🚀 Your Smart Research Bot is online. Ask me anything!")

# --- Main Interaction Loop ---
while True:
    user_question = input("\n> You: ")
    if user_question.lower() in ['exit', 'quit']:
        print("👋 Bot shutting down. Goodbye!")
        break

    # Send the user's question to the agent
    response = chat.send_message(user_question)

    # The agent will automatically call the google_search tool if needed.
    # The framework handles the tool call and response.

    # Print the final, summarized answer from the agent
    print(f"\n🤖 Bot: {response.text}")