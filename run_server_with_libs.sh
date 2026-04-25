#!/bin/bash
# Wrapper script to run Google Ads MCP server

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PYTHON3="$(command -v python3)"
exec "$HOME/.local/bin/uv" run --python "$PYTHON3" python run_server.py "$@"
