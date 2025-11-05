#!/bin/bash
# Wrapper script to run Google Ads MCP server with correct venv

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Use the venv Python
exec "$SCRIPT_DIR/venv/bin/python3" "$SCRIPT_DIR/run_server.py" "$@"
