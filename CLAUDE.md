## KodeKloud Coding Projects

### Overview
Sample Python scripts demonstrating the OpenAI SDK. Below are concise setup and run instructions using uv (recommended) and a plain venv alternative.

### Prerequisites
- **Python**: 3.10+
- **uv**: installed (`pip install uv` or see uv docs)
- **OpenAI API key**: set `OPENAI_API_KEY`

### Quick start (uv)
```bash

# Initialize a project (creates pyproject.toml)
uv init --bare

# Add runtime dependency and lock/install it
uv add openai

# Provide your API key (zsh)
export OPENAI_API_KEY="sk-..."

# Run the examples
uv run python IntroductionToOpenAI/prompt_ex.py
uv run python IntroductionToOpenAI/prompt_ex_v2.py
```

### Alternative: virtualenv + pip
```bash
cd /Users/jmiller/Development/KodeKloud
python3 -m venv kodekloud_venv
source ./kodekloud_venv/bin/activate
pip install --upgrade pip
pip install openai
export OPENAI_API_KEY="sk-..."
python IntroductionToOpenAI/prompt_ex.py
python IntroductionToOpenAI/prompt_ex_v2.py
```

### Useful uv commands
```bash
# Export pinned requirements for legacy tools
uv export --frozen --no-hashes > requirements.txt

# Upgrade a single package (lock + install)
uv sync --upgrade-package openai

# Remove a dependency
uv remove <package>
```

### Troubleshooting
- **ModuleNotFoundError: openai**: Ensure you installed in the same environment you run from (activate venv or use `uv run`).
- **Authentication errors**: Verify `OPENAI_API_KEY` is set in your shell (and not expired/incorrect). Add it to `~/.zshrc` to persist.
