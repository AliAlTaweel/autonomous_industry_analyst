import os
from dotenv import load_dotenv
from tools import rss_feed_tool, financial_parser_tool, trend_correlator_tool, risk_scorer_tool, duckduckgo_search_tool

load_dotenv()

def test_rss():
    print("\n--- Testing RSS Tool ---")
    result = rss_feed_tool.run(topic="Steel Manufacturing")
    print(result[:500] + "...")

def test_finance():
    print("\n--- Testing Financial Tool ---")
    result = financial_parser_tool.run(company_name="SSAB-A.ST")
    print(result)

def test_logic_tools():
    print("\n--- Testing Trend & Risk Tools ---")
    trend = trend_correlator_tool.run(events="EU CBAM implementation")
    risk = risk_scorer_tool.run(topic="Hydrogen DRI transition")
    print(f"Trend: {trend}")
    print(f"Risk: {risk}")

if __name__ == "__main__":
    print("\n--- Testing DDG Search Tool ---")
    search_result = duckduckgo_search_tool.run(query="Python")
    print(search_result[:500] + "...")
    
    test_rss()
    test_finance()
    test_logic_tools()
