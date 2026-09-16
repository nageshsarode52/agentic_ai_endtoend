# Agentic AI Chatbot

A stateful chatbot built with Streamlit, LangGraph, LangChain, and Google Gemini. The application streams Gemini responses as they are generated and remembers earlier messages during the active Streamlit session.

## Features

- Streamlit chat interface
- Google Gemini integration through `langchain-google-genai`
- LangGraph workflow for the chatbot use case
- Streaming assistant responses
- Conversation history displayed in the chat
- Conversation context passed to Gemini on every turn
- Configurable provider, use case, and model options

## Requirements

- Python 3.14 or newer
- A Google AI Studio API key
- `uv` recommended for environment and dependency management

Create a free API key at [Google AI Studio](https://aistudio.google.com/app/apikey).

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd agentic_ai
```

Install the project dependencies with `uv`:

```bash
uv sync
```

You can also install the dependencies with pip:

```bash
pip install -r requirement.txt
```

## Run the Application

Start the Streamlit application:

```bash
uv run streamlit run app.py
```

Open the local URL shown by Streamlit, enter your Google AI Studio API key in the sidebar, and select the chatbot model.

## Configuration

The default UI and model settings are stored in:

`src/agentic_ai/langgraphagenticai/ui/uiconfigfile.ini`

Current defaults include:

```ini
LLM_OPTIONS = Google Gemini
USECASE_OPTIONS = Basic Chatbot
MODEL_OPTIONS = gemini-3.6-flash
```

The API key is entered through the Streamlit sidebar and is used only for the active application session. Do not commit API keys to the repository.

## How Conversation Memory Works

Messages are stored in `st.session_state["messages"]`. For each new prompt, the application sends the previous user and assistant messages together with the new prompt to Gemini. The complete assistant response is saved after streaming finishes so it is available on the next turn.

The history belongs to the current Streamlit browser session. Restarting the app or clearing the session resets the conversation.

## Project Structure

```text
.
├── app.py                                  # Streamlit entrypoint
├── pyproject.toml                           # Project metadata and dependencies
├── requirement.txt                          # pip dependency list
├── src/agentic_ai/langgraphagenticai/
│   ├── main.py                              # Application orchestration
│   ├── LLMS/geminillm.py                    # Gemini model adapter
│   ├── graph/graph_builder.py               # LangGraph construction
│   ├── nodes/basic_chatbot_node.py          # Chatbot graph node
│   ├── state/state.py                       # Graph state schema
│   └── ui/
│       ├── uiconfigfile.ini                 # UI and model configuration
│       ├── uiconfigfile.py                  # Configuration loader
│       └── streamlit/
│           ├── loadui.py                    # Sidebar and input controls
│           └── displayresult.py             # History and streaming output
```

## Troubleshooting

### API key error

Make sure the key is a valid Google AI Studio key and that it is entered in the sidebar before sending a message.

### Model not found

Check `MODEL_OPTIONS` in `uiconfigfile.ini`. Gemini model availability can vary by account and API version. Use a model currently listed as available for your Google AI Studio project.

### Dependencies are not found

Run the application through the project environment:

```bash
uv run streamlit run app.py
```

## Development Checks

Compile the main Python modules with:

```bash
uv run python -m py_compile app.py src/agentic_ai/langgraphagenticai/main.py
```