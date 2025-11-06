# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- IMPORTANT: SET THESE VALUES in your .env file ---
# Create a file named .env in the same directory and add these lines:
# GOOGLE_API_KEY="your_gemini_api_key"
# SEARCH_ENGINE_ID="your_programmable_search_engine_id"
# GOOGLE_PROJECT_ID="your_google_cloud_project_id"
# GOOGLE_LOCATION="us-central1" # Or your preferred location

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
PROJECT_ID = os.getenv("GOOGLE_PROJECT_ID")
LOCATION = os.getenv("GOOGLE_LOCATION")
