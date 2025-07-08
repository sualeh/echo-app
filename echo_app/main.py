#!/usr/bin/env python3
"""
Main module for echo-app MCP server that provides tools for
   command-line arguments and environment variables.
"""

import os
import sys
import fastmcp

# Create the MCP server
echo_app = fastmcp.FastMCP("Echo App MCP Server")


@echo_app.tool()
def get_command_line_args() -> list | str:
    """Get command-line arguments that were passed to the server."""
    args = sys.argv[1:]  # Exclude the script name

    if len(args) == 0:
        return "No results found"

    return [{"index": i+1, "value": arg} for i, arg in enumerate(args)]


@echo_app.tool()
def get_environment_variables() -> list | str:
    """Get environment variables with 'ECHO_' prefix."""
    env_vars = dict(os.environ)
    # Filter to only include variables with ECHO_ prefix
    filtered_vars = {
        k: v for k, v in env_vars.items() if k.startswith('ECHO_')
    }
    sorted_vars = sorted(filtered_vars.items())

    if not sorted_vars:
        return "No results found"

    return [{"name": key, "value": value} for key, value in sorted_vars]


def main() -> None:
    """Main entry point that runs the Echo App MCP server."""
    echo_app.run()


if __name__ == "__main__":
    main()
