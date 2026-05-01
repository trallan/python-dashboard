
## UV Commands
`curl -Ls https://astral.sh/uv/install.sh | sh
uv init myproject
cd myproject
uv venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
uv pip install requests
uv run python main.py
uv add requests
uv sync
uv remove requests
uv run python script.py     # Quick script run
`