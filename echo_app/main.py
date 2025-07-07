#!/usr/bin/env python3
"""Main module for echo-app MCP server that provides tools for command-line arguments and environment variables."""

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


def print_command_line_args(args: list[str]) -> str:
    """Return command-line arguments as a string (legacy function for backward compatibility)."""
    lines = ["Command-line arguments:"]
    
    if len(args) == 0:
        lines.append("  No command-line arguments provided.")
    else:
        for i, arg in enumerate(args):
            lines.append(f"  [{i+1}]: {arg}")
    
    lines.append("")
    return "\n".join(lines)


def print_environment_variables(env_vars: dict[str, str]) -> str:
    """Return environment variables as a string (legacy function for backward compatibility)."""
    lines = ["Environment variables:"]
    
    # Sort environment variables for consistent output
    sorted_vars = sorted(env_vars.items())
    if not sorted_vars:
        lines.append("  No environment variables found.")
    else:
        for key, value in sorted_vars:
            lines.append(f"  {key}={value}")
    
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """Main entry point that runs the MCP server."""
    # Log startup information
    args = sys.argv[1:]  # Exclude the script name
    env_vars = dict(os.environ)
    
    logger.info("Starting Echo App MCP Server")
    logger.info(f"Command-line arguments: {args}")
    logger.info(f"Environment variables count: {len(env_vars)}")
    
    # Log detailed command-line arguments and environment variables
    args_details = print_command_line_args(args)
    env_details = print_environment_variables(env_vars)
    logger.info(f"Command-line arguments details:\n{args_details}")
    logger.info(f"Environment variables details:\n{env_details}")
    
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
