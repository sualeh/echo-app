#!/usr/bin/env python3
"""Main module for echo-app that prints command-line arguments and environment variables."""

import os
import sys
from typing import Dict, List


# Define module-level constant for separator width
SEPARATOR_WIDTH = 50

def print_command_line_args(args: List[str]) -> None:
    """Print command-line arguments."""
    print("=" * SEPARATOR_WIDTH)
    print("COMMAND-LINE ARGUMENTS")
    print("=" * SEPARATOR_WIDTH)
    
    if len(args) == 0:
        print("No command-line arguments provided.")
    else:
        for i, arg in enumerate(args):
            print(f"  [{i}]: {arg}")
    
    print()


def print_environment_variables(env_vars: Dict[str, str]) -> None:
    """Print environment variables."""
    print("=" * 50)
    print("ENVIRONMENT VARIABLES")
    print("=" * 50)
    
    if not env_vars:
        print("No environment variables found.")
    else:
        # Sort environment variables for consistent output
        sorted_vars = sorted(env_vars.items())
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