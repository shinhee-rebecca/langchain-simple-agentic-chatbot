# SimpleChat Agent Demo

A simple AI chatbot agent demo project based on LangChain.

## Introduction

This project is an example of implementing a conversational AI agent that can utilize tools using LangChain. It includes a chatbot with a friendly persona called "Bubble" (버블이) by default.

## Key Features

- Interactive CLI interface
- Customizable AI persona
- Extensible tool system
  - Weather lookup
  - Calculator
  - Web search

## Installation

### Requirements

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Setup

```bash
# Clone the repository
git clone https://github.com/your-username/simplechat-agent-demo.git
cd simplechat-agent-demo

# Using uv
uv sync

# Using pip
pip install -e .
```

## Configuration

### .env File Setup

Create a `.env` file in the project root and configure it as follows:

```env
OPENAI_API_KEY=your-openai-api-key-here
OPENAI_MODEL=gpt-4o-mini
```

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key (required) | - |
| `OPENAI_MODEL` | Model to use | `gpt-4o-mini` |

> **Note**: The `.env` file is included in `.gitignore` and will not be committed to Git. Configure it according to your environment.

## Running

```bash
# Using uv
uv run python main.py

# After activating virtual environment
python main.py
```

When executed, the interactive interface starts:

```
==================================================
Welcome to Bubble Chatbot!
   (Exit: 'quit' or 'exit')
==================================================

You: What's the weather in Seoul?
Bubble: It's currently sunny in Seoul with a temperature of 15°C!
```

## Project Structure

```
simplechat-agent-demo/
├── main.py              # Main entry point
├── agent/
│   └── executor.py      # Agent creation logic
├── config/
│   └── settings.py      # Environment configuration
├── llm/
│   └── model.py         # LLM model initialization
├── prompts/
│   └── persona.py       # Persona and system prompts
├── tools/
│   ├── __init__.py      # Tool collection (ALL_TOOLS)
│   ├── weather.py       # Weather lookup tool
│   ├── calculator.py    # Calculator tool
│   └── search.py        # Web search tool
├── pyproject.toml       # Project dependencies
└── .env                 # Environment variables (create manually)
```

## Extension Guide

### Customizing Persona

You can freely modify the AI's personality and speech style in `prompts/persona.py`:

```python
# prompts/persona.py
MY_PERSONA = """
You are a professional assistant named 'My AI'.

## Personality
- Polite and professional
- Uses formal language

## Role
- Support user's work tasks
"""

def get_system_prompt(persona: str = MY_PERSONA) -> str:
    return persona
```

### Adding New Tools

You can add new tools in the `tools/` directory:

```python
# tools/my_tool.py
from langchain_core.tools import tool

@tool
def my_custom_tool(param: str) -> str:
    """
    Write a description of the tool.

    Args:
        param: Parameter description
    """
    # Implement tool logic
    return f"Result: {param}"
```

Register the new tool in `tools/__init__.py`:

```python
# tools/__init__.py
from tools.my_tool import my_custom_tool

ALL_TOOLS = [
    get_current_weather,
    calculate,
    search_web,
    my_custom_tool,  # Add new tool
]
```

### Use Cases

- **Customer Service Bot**: Modify persona and add FAQ search tool
- **Work Assistant**: Integrate calendar, email tools
- **Educational Bot**: Add quiz, learning material search tools

## Tool Details

### Weather Lookup (`get_current_weather`)

Uses the [wttr.in](https://wttr.in/) API to retrieve current weather for cities worldwide.

```
You: How's the weather in Seoul?
Bubble: Here's the current weather in Seoul!
        Weather: Clear
        Temperature: 15°C (Feels like 13°C)
        Humidity: 45%
        Wind: 12km/h
```

- **Supported Info**: Weather condition, temperature, feels-like temperature, humidity, wind speed
- **Multilingual Support**: Weather descriptions available in Korean
- **Input Examples**: `Seoul`, `Tokyo`, `New York`, `London`

### Web Search (`search_web`)

Uses [DuckDuckGo](https://duckduckgo.com/) to search for information on the web.

```
You: Search for Python async programming
Bubble: Here are the search results for 'Python async programming'!
        1. Python asyncio Official Documentation
           Python's asynchronous I/O framework...
           Link: https://docs.python.org/...
        ...
```

- **Search Results**: Returns up to 5 relevant results
- **Provided Info**: Title, summary, link

## Dependencies

- [LangChain](https://python.langchain.com/) - LLM application framework
- [langchain-openai](https://python.langchain.com/docs/integrations/llms/openai/) - OpenAI integration
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management
- [duckduckgo-search](https://github.com/deedy5/duckduckgo_search) - DuckDuckGo search API
- [requests](https://requests.readthedocs.io/) - HTTP client

## License

MIT License