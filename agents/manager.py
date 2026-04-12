from crewai import Agent
from config.llm import get_llm
from config.logger import logger

def create_manager() -> Agent:
    logger.debug("Creating Research Operations Manager agent")
    return Agent(
        role="Research Operations Manager",
        goal="Ensure all research analysis meets a confidence threshold of 7.0/10.",
        backstory=(
            "You are a meticulous operations manager at a global strategy firm. "
            "Your reputation depends on the accuracy of your team's reports. "
            "If an analyst's confidence score is below 7.0, you must identify what is missing "
            "and delegate specific follow-up research tasks back to the Researcher. "
            "You only approve work for final writing when the analysis is robust and well-supported."
        ),
        llm=get_llm(),
        verbose=True,
        allow_delegation=True,
    )
