# Mazzu AI - Personal Dev Assistant

A powerful, local-first AI assistant inspired by Claude Code. It features both a **Command Line Interface (CLI)** and a **Streamlit Web UI**.

## Features
* **Dual Interface**: Seamlessly switch between a **CLI (Terminal)** for quick tasks and a **Streamlit Web UI** for longer coding sessions.
* **Local-First Design**: Optimized for local development and code analysis.
* **Model Flexibility**: Easy to swap between the latest high-performance models.
* **Security Built-in**: Configuration and API keys are stored locally and kept out of version control.

## Setup
1. Clone the repo.
2. Create a folder named `config`.
3. Inside `config/`, create `api_key.txt` (paste your Groq key, get it at https://console.groq.com/) and `system_prompt.txt` (paste your AI instructions).
4. Install dependencies: `pip install -r requirements.txt`
5. Run Web UI: `streamlit run app.py`
6. Run CLI: `python chat.py`

*Note: The `config/` folder is gitignored to keep your credentials safe.*
