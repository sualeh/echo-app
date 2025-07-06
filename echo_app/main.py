#!/usr/bin/env python3
"""Main module for echo-app MCP server that provides tools for command-line arguments and environment variables."""

import logging
import os
import sys
import fastmcp

# Create the MCP server
app = fastmcp.FastMCP("Echo App MCP Server")

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
    
    # Log the command-line arguments
    logger.info(f"Command-line arguments requested: {args}")
    
    if len(args) == 0:
        return {
            "message": "No command-line arguments provided.",
            "args": []
        }
    else:
        return {
            "message": "Command-line arguments:",
            "args": [{"index": i+1, "value": arg} for i, arg in enumerate(args)]
        }


@app.tool()
def get_environment_variables() -> dict:
    """Get all environment variables."""
    env_vars = dict(os.environ)
    sorted_vars = sorted(env_vars.items())
    
    # Log environment variables count (avoid logging sensitive values)
    logger.info(f"Environment variables requested: {len(env_vars)} variables")
    
    if not sorted_vars:
        return {
            "message": "No environment variables found.",
            "variables": []
        }
    else:
        return {
            "message": "Environment variables:",
            "variables": [{"name": key, "value": value} for key, value in sorted_vars]
        }


def print_command_line_args(args: list[str]) -> None:
    """Print command-line arguments (legacy function for backward compatibility)."""
    print("Command-line arguments:")
    
    if len(args) == 0:
        print("  No command-line arguments provided.")
    else:
        for i, arg in enumerate(args):
            print(f"  [{i+1}]: {arg}")
    
    print()


def print_environment_variables(env_vars: dict[str, str]) -> None:
    """Print environment variables (legacy function for backward compatibility)."""
    print("Environment variables:")
    
    # Sort environment variables for consistent output
    sorted_vars = sorted(env_vars.items())
    if not sorted_vars:
        print("  No environment variables found.")
    else:
        for key, value in sorted_vars:
            print(f"  {key}={value}")
    
    print()


def main() -> None:
    """Main entry point that runs the MCP server."""
    # Log startup information
    args = sys.argv[1:]  # Exclude the script name
    env_vars = dict(os.environ)
    
    logger.info("Starting Echo App MCP Server")
    logger.info(f"Command-line arguments: {args}")
    logger.info(f"Environment variables count: {len(env_vars)}")
    
    print("Starting Echo App MCP Server...")
    print("Available tools:")
    print("  - hello_world: Returns 'Hello, world!'")
    print("  - get_command_line_args: Returns command-line arguments")
    print("  - get_environment_variables: Returns environment variables")
    print()
    
    # Run the MCP server
    app.run()


if __name__ == "__main__":
    main()
