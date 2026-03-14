import os
from dotenv import load_dotenv

load_dotenv()

def get_gemini_key():
    return os.getenv("GEMINI_API_KEY")

def get_elevenlabs_key():
    # This is your main API Secret Key
    return os.getenv("ELEVENLABS_KEY")

def get_agent_id():
    # This is the specific ID for the transcription agent
    return os.getenv("AGENT_ID")