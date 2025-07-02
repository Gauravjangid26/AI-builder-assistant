import streamlit as st
import sys, os

# Add root path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from backend.agents.langgraph_bot import builder_bot

st.title("👷‍♂️ Builder AI Assistant - Daily Log Summarizer")

user_input = st.chat_input("Paste today's construction site log here...")

if user_input:
    with st.spinner("Summarizing with Gemini..."):
        result = builder_bot.invoke({"query": user_input})

        # ✅ Loop through tools to find the one that returned a response
        #response = None
        #for tool_key in ["summarizer", "budget_checker", "permit_parser"]:
         #   if tool_key in result and isinstance(result[tool_key], dict):
          #      response = result[tool_key].get("response")
           #     if response:
            #        break

        #if response:
        st.markdown("📋 **AI Response:**")
        st.write(result)
        #else:
         #   st.error("❌ No valid response returned by any tool.")
