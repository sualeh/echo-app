#!/usr/bin/env python3
"""
Main module for echo-app MCP server that provides tools for
   command-line arguments and environment variables.
"""

import logging
import os
import sys
import fastmcp

# Create the MCP server
app = fastmcp.FastMCP("Echo App MCP Server", banner=False)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@app.tool()
def hello_world() -> str:
    """A simple tool that returns 'Hello, world!'"""
    return "Hello, world!"


@app.tool()
def get_command_line_args() -> dict:
    """Get command-line arguments that were passed to the server."""
    args = sys.argv[1:]  # Exclude the script name

    logger.info("Command-line arguments requested: %s", args)

    if len(args) == 0:
        return []

    return [{"index": i+1, "value": arg} for i, arg in enumerate(args)]


@app.tool()
def get_environment_variables() -> dict:
    """Get environment variables with ECHO_ prefix."""
    env_vars = dict(os.environ)
    # Filter to only include variables with ECHO_ prefix
    filtered_vars = {
        k: v for k, v in env_vars.items() if k.startswith('ECHO_')
    }
    sorted_vars = sorted(filtered_vars.items())

    logger.info("ECHO_ environment variables: %d variables",
                len(filtered_vars))

    if not sorted_vars:
        return []

    return [{"name": key, "value": value} for key, value in sorted_vars]


def main() -> None:
    """Main entry point that runs the MCP server."""

    logger.info("Starting Echo App MCP Server")
    logger.info("%s", get_command_line_args())
    logger.info("%s", get_environment_variables())

    print("Starting Echo App MCP Server...")

    # Run the MCP server
    app.run()


if __name__ == "__main__":
    main()
