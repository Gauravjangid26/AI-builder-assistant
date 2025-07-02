from langgraph.graph import StateGraph
from typing import TypedDict

from backend.tools.log_summarizer import summarize_logs
from backend.tools.budget_analyzer import check_budget
from backend.tools.permit_parser import parse_permit
from backend.agents.tool_planner import decide_next_tool

# Define shared state
class BuilderState(TypedDict):
    query: str
    response: str

# Build the LangGraph
graph = StateGraph(BuilderState)

# Add nodes
graph.add_node("summarizer", summarize_logs)
graph.add_node("budget_checker", check_budget)
graph.add_node("permit_parser", parse_permit)
graph.add_node("planner", decide_next_tool)

# ❗ FIX THIS LINE: Use function references as values, not strings
graph.add_conditional_edges(
    "planner",
    {
        "summarizer": summarize_logs,
        "budget_checker": check_budget,
        "permit_parser": parse_permit
    },
    "next"
)

graph.set_entry_point("planner")
builder_bot = graph.compile()
