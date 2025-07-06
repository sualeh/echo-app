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

### Using Poetry

Run the application using Poetry:

```bash
# Run without arguments
poetry run echo-app

# Run with arguments
poetry run echo-app arg1 arg2 "argument with spaces" --flag

# Run directly with Python
python -m echo_app.main [arguments...]
```

### Using Docker

The application is also available as a Docker image:

```bash
# Run without arguments
docker run --rm sualeh/echo-app

# Run with arguments
docker run --rm sualeh/echo-app arg1 arg2 "argument with spaces" --flag

# Run with environment variables
docker run --rm -e MY_VAR=test sualeh/echo-app
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

## Docker Distribution

This application is distributed as a Docker image that supports both x86 and ARM architectures.

### Docker Hub

The image is automatically built and published to Docker Hub via GitHub Actions:
- **Repository**: `sualeh/echo-app`
- **Platforms**: `linux/amd64`, `linux/arm64`
- **Tags**: `latest`, version tags (e.g., `v1.0.0`), and branch tags

### Building Locally

To build the Docker image locally:

```bash
# Build for current platform
docker build -t echo-app .

# Build for specific platform
docker build -t echo-app --platform linux/amd64 .
```

### GitHub Actions Workflow

The Docker image is automatically built and pushed to Docker Hub when:
- Code is pushed to the `main` branch
- A version tag is created (e.g., `v1.0.0`)
- Pull requests are opened (build only, no push)

Required secrets for Docker Hub publishing:
- `DOCKER_USERNAME`: Docker Hub username
- `DOCKER_PASSWORD`: Docker Hub password or access token

## Development

The project structure:
- `echo_app/` - Main package directory
- `echo_app/__init__.py` - Package initialization
- `echo_app/main.py` - Main application logic
- `pyproject.toml` - Poetry configuration and dependencies
- `Dockerfile` - Docker image configuration
- `.github/workflows/docker.yml` - GitHub Actions workflow for Docker builds