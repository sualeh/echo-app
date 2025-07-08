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
echo_app = fastmcp.FastMCP("Echo App MCP Server")

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@echo_app.tool()
def get_command_line_args() -> list:
    """Get command-line arguments that were passed to the server."""
    args = sys.argv[1:]  # Exclude the script name

    logger.debug("Command-line arguments requested: %s", args)

    if len(args) == 0:
        return None

    return [{"index": i+1, "value": arg} for i, arg in enumerate(args)]


@echo_app.tool()
def get_environment_variables() -> list:
    """Get environment variables with ECHO_ prefix."""
    env_vars = dict(os.environ)
    # Filter to only include variables with ECHO_ prefix
    filtered_vars = {
        k: v for k, v in env_vars.items() if k.startswith('ECHO_')
    }
    sorted_vars = sorted(filtered_vars.items())

    logger.debug("Environment variables: %d variables", len(filtered_vars))

    if not sorted_vars:
        return None

    return [{"name": key, "value": value} for key, value in sorted_vars]


def main() -> None:
    """Main entry point that runs the MCP server."""

    logger.info("Starting Echo App MCP Server")

    # Run the MCP server
    echo_app.run()


if __name__ == "__main__":
    main()
