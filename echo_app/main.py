#!/usr/bin/env python3
"""Main module for echo-app that prints command-line arguments and environment variables."""

import os
import sys


def print_command_line_args(args: list[str]) -> None:
    """Print command-line arguments."""
    print("Command-line arguments:")
    
    if len(args) == 0:
        print("  No command-line arguments provided.")
    else:
        for i, arg in enumerate(args):
            print(f"  [{i+1}]: {arg}")
    
    print()


def print_environment_variables(env_vars: dict[str, str]) -> None:
    """Print environment variables."""
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
    """Main entry point for the echo application."""
    print("Echo App - Command-line Arguments and Environment Variables")
    print()
    
    # Print command-line arguments (excluding the script name)
    args = sys.argv[1:]
    print_command_line_args(args)
    
    # Print environment variables
    env_vars = dict(os.environ)
    print_environment_variables(env_vars)


if __name__ == "__main__":
    main()
