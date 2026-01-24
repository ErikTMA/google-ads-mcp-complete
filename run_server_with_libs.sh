#!/bin/bash
# Wrapper script to run Google Ads MCP server
# Bypasses devbox/nix to avoid GLIBC conflicts

# Clean ALL nix/devbox environment variables
unset LD_LIBRARY_PATH
unset PYTHONPATH
unset PYTHONHOME
unset VIRTUAL_ENV
unset NIX_PATH
unset NIX_PROFILES
unset NIX_SSL_CERT_FILE

# Set clean PATH - remove any nix store paths
export PATH=$(echo "/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin" | tr ':' '\n' | grep -v '/nix/store' | tr '\n' ':' | sed 's/:$//')

cd "$(dirname "$0")"

# Use system uv with system Python
exec "$HOME/.local/bin/uv" run --python /usr/bin/python3 python run_server.py "$@"
