def decide_next_tool(state):
    query = state["query"].lower()

    if "budget" in query:
        return {"next": "budget_checker"}  # ✅ Must match graph.add_node name
    elif "permit" in query or "pdf" in query:
        return {"next": "permit_parser"}   # ✅ Already good
    else:
        return {"next": "summarizer"}      # ✅ Must match graph.add_node name
