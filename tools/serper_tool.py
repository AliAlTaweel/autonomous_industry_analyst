import os
from crewai_tools import SerperDevTool

def get_serper_tool():
    """Returns a configured SerperDevTool instance."""
    return SerperDevTool()
