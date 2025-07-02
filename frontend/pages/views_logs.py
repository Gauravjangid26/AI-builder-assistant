import streamlit as st
from backend.services.db import get_all_logs

st.title("📊 Assistant Log History")

logs = get_all_logs()

if not logs:
    st.info("No logs found yet.")
else:
    for log in logs:
        st.markdown("----")
        st.markdown(f"🗓️ **Time:** `{log[4]}`")
        st.markdown(f"🛠️ **Tool:** `{log[3]}`")
        st.markdown(f"🔍 **Query:** {log[1]}")
        st.markdown(f"🧠 **Response:** {log[2]}")
