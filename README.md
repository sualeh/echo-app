# echo-app

A simple Python application managed by Poetry that prints command-line arguments and environment variables.

## Features

- Prints all command-line arguments with their indices
- Prints all environment variables in alphabetical order
- Clean, formatted output with clear section headers
- Handles arguments with spaces and special characters

## Installation

This project uses Poetry for dependency management. To install and run:

1. Install Poetry if you haven't already:
   ```bash
   pip install poetry
   ```

2. Install the project:
   ```bash
   poetry install
   ```

## Usage

Run the application using Poetry:

```bash
# Run without arguments
poetry run echo-app

# Run with arguments
poetry run echo-app arg1 arg2 "argument with spaces" --flag

# Run directly with Python
python -m echo_app.main [arguments...]
```

## Example Output

```
$ poetry run echo-app hello world --verbose
Echo App - Command-line Arguments and Environment Variables

==================================================
COMMAND-LINE ARGUMENTS
==================================================
  [0]: hello
  [1]: world
  [2]: --verbose

==================================================
ENVIRONMENT VARIABLES
==================================================
  HOME=/home/user
  PATH=/usr/local/bin:/usr/bin:/bin
  SHELL=/bin/bash
  USER=user
  ...
```

## Development

The project structure:
- `echo_app/` - Main package directory
- `echo_app/__init__.py` - Package initialization
- `echo_app/main.py` - Main application logic
- `pyproject.toml` - Poetry configuration and dependencies