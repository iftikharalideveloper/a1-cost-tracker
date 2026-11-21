import os
import sys
import json
import time

from dotenv import load_dotenv
from google import genai
from groq import Groq








# Load environment variables
load_dotenv()

# Get API keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Check if API keys are available
if not GEMINI_API_KEY:
    sys.exit("Error: GEMINI_API_KEY is missing from .env")

        if not GROQ_API_KEY:
            print("Error: GROQ_API_KEY is missing from .env")
                sys.exit(1)
                # Get model names from environment variables
                GEMINI_MODEL = os.getenv("GEMINI_MODEL")
                GROQ_MODEL = os.getenv("GROQ_MODEL")

                # Check model configuration
                if not GEMINI_MODEL:
                    print("Error: GEMINI_MODEL is missing from .env")
                        sys.exit(1)

                        if not GROQ_MODEL:
                            print("Error: GROQ_MODEL is missing from .env")
                                sys.exit(1)
                                