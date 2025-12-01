#!/bin/bash
# Wrapper script to run Google Ads MCP server
# Bypasses devbox/nix to avoid GLIBC conflicts

# Clean environment - remove nix paths
unset LD_LIBRARY_PATH
export PATH="/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin"

cd "$(dirname "$0")"

# Use system uv with system Python
exec "$HOME/.local/bin/uv" run --python /usr/bin/python3 python run_server.py "$@"
