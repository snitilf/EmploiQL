# import this at the top of any module that needs API keys
import os
from pathlib import Path

# python-dotenv reads .env file and sets environment variables
# install with: pip install python-dotenv 
from dotenv import load_dotenv

# find the project root (where .env lives)
# this file is in src/, so parent is project root
PROJECT_ROOT = Path(__file__).parent.parent

# load .env file into environment variables
# this makes os.getenv("OPENAI_API_KEY") work
env_path = PROJECT_ROOT / ".env"
load_dotenv(env_path)

# convenience access to common keys
# these will be None if not set, which triggers helpful errors later
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


def check_api_keys() -> dict:
    """
    check which API keys are configured.
    useful for debugging setup issues.
    
    returns dict with key names and whether they're set
    """
    return {
        "OPENAI_API_KEY": bool(OPENAI_API_KEY),
        "RAPIDAPI_KEY": bool(RAPIDAPI_KEY),
    }


if __name__ == "__main__":
    # quick check when running directly
    print("EmploiQL Configuration Check")
    print("-" * 40)
    print(f".env path: {env_path}")
    print(f".env exists: {env_path.exists()}")
    print()
    
    status = check_api_keys()
    for key, is_set in status.items():
        icon = "[OK]" if is_set else "[MISSING]"
        print(f"  {icon} {key}")
    
    if not all(status.values()):
        print()
        print("To fix missing keys:")
        print("  1. Copy .env.example to .env")
        print("  2. Edit .env and add your keys")