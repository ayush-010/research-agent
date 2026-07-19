from search import web_search
from summarize import summarize_results


def format_history_for_prompt(history: list, max_turns: int = 3) -> str:
    """Turn the last few exchanges into text the LLM can use for context."""
    if not history:
        return ""
    recent = history[-max_turns:]
    lines = ["Previous conversation:"]
    for turn in recent:
        lines.append(f"Q: {turn['query']}")
        lines.append(f"A: {turn['answer']}\n")
    return "\n".join(lines)


def run_agent(query: str, history: list):
    print(f"\n🔍 Searching for: {query}\n")
    results = web_search(query, max_results=5)

    if not results:
        print("No results found. Try rephrasing your question.")
        return None

    print(f"Found {len(results)} sources. Summarizing...\n")
    history_context = format_history_for_prompt(history)
    answer = summarize_results(query, results, history_context)

    print("=" * 60)
    print(answer)
    print("=" * 60)

    print("\nSources:")
    for i, r in enumerate(results, start=1):
        print(f"[{i}] {r['title']} — {r['url']}")

    return answer


if __name__ == "__main__":
    print("Research Agent — type your question, or 'exit' to quit.")
    print("(Memory lasts for this session only — nothing is saved to disk.)\n")

    history = []  # plain in-memory list, wiped when you close the terminal

    while True:
        query = input("\n> ").strip()
        if query.lower() in ("exit", "quit"):
            print("Goodbye! (History cleared — nothing was saved.)")
            break
        if not query:
            continue

        answer = run_agent(query, history)
        if answer:
            history.append({"query": query, "answer": answer})