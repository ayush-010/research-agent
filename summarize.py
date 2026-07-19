import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def summarize_results(query: str, results: list) -> str:
    """
    Takes the original query and a list of search result dicts
    ({title, url, content}) and returns a cited, synthesized answer.
    """
    context_blocks = []
    for i, r in enumerate(results, start=1):
        context_blocks.append(
            f"[{i}] {r['title']}\nURL: {r['url']}\nContent: {r['content']}\n"
        )
    context = "\n".join(context_blocks)

    prompt = f"""You are a research assistant. Answer the user's question using ONLY the sources below.
Cite sources inline using [1], [2], etc. matching the source numbers.
If sources conflict or are insufficient, say so clearly.

Question: {query}

Sources:
{context}

Write a clear, well-organized answer with inline citations."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    from search import web_search
    query = "latest developments in fusion energy"
    results = web_search(query)
    answer = summarize_results(query, results)
    print(answer)