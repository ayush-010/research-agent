import sys
from search import web_search
from summarize import summarize_results

def run_agent(query: str):
    print(f"\n🔍 Searching for: {query}\n")
    results = web_search(query, max_results=5)

    if not results:
        print("No results found. Try rephrasing your question.")
        return

    print(f"Found {len(results)} sources. Summarizing...\n")
    answer = summarize_results(query, results)

    print("=" * 60)
    print(answer)
    print("=" * 60)

    print("\nSources:")
    for i, r in enumerate(results, start=1):
        print(f"[{i}] {r['title']} — {r['url']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python agent.py "your question here"')
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    run_agent(query)