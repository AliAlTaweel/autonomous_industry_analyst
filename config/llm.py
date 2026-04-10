"""
config/llm.py — LLM Factory

Single source of truth for which LLM the agents use.
Controlled by LLM_PROVIDER in .env.
Uses the crewai.LLM class for native compatibility with CrewAI 1.x.
"""

import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()


def get_llm():
    """
    Returns a crewai.LLM instance based on LLM_PROVIDER env var.
    Defaults to Ollama (local) for development.
    """
    provider = os.getenv("LLM_PROVIDER", "ollama").lower()

    if provider == "ollama":
        model = os.getenv("OLLAMA_MODEL", "llama3.2")
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

        print(f"[LLM] Configured CrewAI LLM for Ollama → model: {model} @ {base_url}")

        # CrewAI LLM uses "ollama/model" format for Ollama
        return LLM(
            model=f"ollama/{model}",
            base_url=base_url,
            temperature=0.7,
        )

    elif provider == "openai":
        model = os.getenv("OPENAI_MODEL", "gpt-4o")
        print(f"[LLM] Configured CrewAI LLM for OpenAI → model: {model}")

        return LLM(
            model=model,  # OpenAI is the default provider
            temperature=0.7,
        )

    elif provider == "anthropic":
        model = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")
        print(f"[LLM] Configured CrewAI LLM for Anthropic → model: {model}")

        # For Anthropic, prefix with "anthropic/" if needed, 
        # but CrewAI LLM usually handles it.
        return LLM(
            model=f"anthropic/{model}",
            temperature=0.7,
        )

    else:
        raise ValueError(
            f"Unknown LLM_PROVIDER: '{provider}'. "
            "Valid options: ollama | openai | anthropic"
        )
