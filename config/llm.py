"""
config/llm.py — LLM Factory

Single source of truth for which LLM the agents use.
Controlled by LLM_PROVIDER in .env.
Uses the crewai.LLM class for native compatibility with CrewAI 1.x.
"""

import os
from dotenv import load_dotenv
from crewai import LLM
from langchain.globals import set_llm_cache
from langchain_community.cache import SQLiteCache

load_dotenv()

# Initialize a global LLM cache to persist local model results across runs
DEBUG_CACHE_PATH = os.path.join(os.getcwd(), ".cache", "llm_cache.db")
os.makedirs(os.path.dirname(DEBUG_CACHE_PATH), exist_ok=True)
set_llm_cache(SQLiteCache(database_path=DEBUG_CACHE_PATH))

def get_llm():
    """
    Returns the 'Worker' LLM (Gemma 26B) for Researcher and Analyst agents.
    """
    provider = os.getenv("LLM_PROVIDER", "ollama").lower()

    if provider == "ollama":
        model = os.getenv("OLLAMA_MODEL", "gemma4:26b")
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

        print(f"[LLM] Configured WORKER LLM for Ollama → {model}")

        return LLM(
            model=f"ollama/{model}",
            base_url=base_url,
            temperature=0.7,
            api_key="none",
            max_tokens=16384,
            timeout=600,
        ) 
    
    # ... other providers ...
    return _get_cloud_llm(provider)


def get_manager_llm():
    """
    Returns the 'Manager' LLM (Llama 3.1 8B) for high-speed coordination.
    """
    provider = os.getenv("MANAGER_LLM_PROVIDER", "ollama").lower()

    if provider == "ollama":
        model = os.getenv("MANAGER_OLLAMA_MODEL", "llama3.1:8b")
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

        print(f"[LLM] Configured MANAGER LLM for Ollama → {model}")

        return LLM(
            model=f"ollama/{model}",
            base_url=base_url,
            temperature=0.3, # Lower temperature for better coordination logic
            api_key="none",
            timeout=120,   # Faster decisions don't need 10 mins
        )

    return _get_cloud_llm(provider)


def _get_cloud_llm(provider):
    if provider == "openai":
        model = os.getenv("OPENAI_MODEL", "gpt-4o")
        return LLM(model=model, temperature=0.7, timeout=600)
    elif provider == "anthropic":
        model = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")
        return LLM(model=f"anthropic/{model}", temperature=0.7, timeout=600)
    
    raise ValueError(f"Unknown LLM_PROVIDER: '{provider}'")
