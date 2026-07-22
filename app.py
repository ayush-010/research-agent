import streamlit as st
from search import web_search
from summarize import summarize_results

st.set_page_config(page_title="Research Agent", page_icon="🔍", layout="centered")

st.title("🔍 Research Agent")
st.caption("Ask a question. It searches the web and gives you a cited answer.")
st.divider()

with st.sidebar:
    st.header("Settings")
    if st.button("🗑️ Clear conversation"):
        st.session_state.history = []
        st.rerun()

# Session-only memory — resets when the browser tab is closed/refreshed
if "history" not in st.session_state:
    st.session_state.history = []

def format_history_for_prompt(history: list, max_turns: int = 3) -> str:
    if not history:
        return ""
    recent = history[-max_turns:]
    lines = ["Previous conversation:"]
    for turn in recent:
        lines.append(f"Q: {turn['query']}")
        lines.append(f"A: {turn['answer']}\n")
    return "\n".join(lines)

# Render past conversation
for turn in st.session_state.history:
    with st.chat_message("user"):
        st.write(turn["query"])
    with st.chat_message("assistant"):
        st.write(turn["answer"])
        with st.expander("Sources"):
            for i, src in enumerate(turn["sources"], start=1):
                st.markdown(f"**[{i}]** [{src['title']}]({src['url']})")

# Input box at the bottom (Streamlit's built-in chat input)
query = st.chat_input("Ask a research question...")

if query:
    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        with st.spinner("Searching the web..."):
            results = web_search(query, max_results=5)

        if not results:
            st.write("No results found. Try rephrasing your question.")
        else:
            with st.spinner("Reading sources and writing answer..."):
                history_context = format_history_for_prompt(st.session_state.history)
                answer = summarize_results(query, results, history_context)

            st.write(answer)
            with st.expander("Sources"):
                for i, r in enumerate(results, start=1):
                    st.markdown(f"**[{i}]** [{r['title']}]({r['url']})")

            st.session_state.history.append({
                "query": query,
                "answer": answer,
                "sources": results
            })