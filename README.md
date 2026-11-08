# AI Agent

A simple AI coding agent built with Python as part of Boot.dev's **Build an AI Agent** course.

The agent uses OpenRouter to interact with an LLM that can inspect, modify, and run Python files in the included `calculator/` project.

## Requirements

- Python 3.15+
- [uv](https://docs.astral.sh/uv/)
- An [OpenRouter API key](https://openrouter.ai/)

## Setup

```bash
git clone https://github.com/miguelith/ai-agent.git
cd ai-agent
uv sync
```

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key
```

## Usage

```bash
uv run main.py "Your prompt here"
```

Add `--verbose` to see the agent's execution details.
