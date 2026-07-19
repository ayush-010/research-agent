# Research Agent

A personal research assistant that takes a question, searches the web, and returns a clear, cited summary — so you don't have to open 10 tabs.

## How it works

1. Takes your question as a command-line argument
2. Searches the web using [Tavily](https://tavily.com)
3. Sends the top results to [Groq](https://groq.com) (Llama 3.3 70B) to synthesize a cited answer
4. Prints the answer plus a numbered source list

## Setup

\`\`\`bash
git clone https://github.com/YOUR_USERNAME/research-agent.git
cd research-agent
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

Create a `.env` file in the project root:

\`\`\`
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
\`\`\`

Get free keys at [console.groq.com](https://console.groq.com) and [tavily.com](https://tavily.com).

## Usage

\`\`\`bash
python agent.py "what are the latest breakthroughs in solid-state batteries"
\`\`\`

## Project structure

- `search.py` — Tavily web search wrapper
- `summarize.py` — Groq LLM summarization with inline citations
- `agent.py` — CLI entry point tying it together

## Roadmap

- [ ] Save results to a file (markdown/PDF export)
- [ ] Conversation memory for follow-up questions
- [ ] Web UI (Streamlit or Flask)

## Usage

### CLI (interactive)
\`\`\`bash
python agent.py
\`\`\`

### Web GUI
\`\`\`bash
streamlit run app.py
\`\`\`
Opens a chat interface in your browser at `http://localhost:8501`.