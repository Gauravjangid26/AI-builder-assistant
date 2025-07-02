from backend.models.gemini_wrapper import gemini_generate

def summarize_logs(state):
    log_text = state.get("query", "")
    prompt = f"""
You are a construction site assistant AI.
Summarize the following construction log in clear, concise bullet points.
Focus on progress, delays, issues, and pending work.

Log:
{log_text}
"""
    summary = gemini_generate(prompt)
    return {"response": summary}
