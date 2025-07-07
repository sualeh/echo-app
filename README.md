# echo-app

# echo-app

A Model Context Protocol (MCP) server built with FastMCP that provides tools for accessing command-line arguments and environment variables, along with a simple hello world tool.

## Features

- **MCP Server**: Provides tools accessible via Model Context Protocol
- **hello_world tool**: Returns a simple "Hello, world!" message
- **get_command_line_args tool**: Returns command-line arguments with their indices
- **get_environment_variables tool**: Returns environment variables with ECHO_ prefix in alphabetical order
- **Clean structured output**: All tools return well-formatted JSON data
- **Poetry managed**: Uses Poetry for dependency management and building

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

### Running the MCP Server

Run the MCP server using Poetry:

```bash
# Start the MCP server
poetry run echo-app

# Start with arguments (accessible via get_command_line_args tool)
poetry run echo-app arg1 arg2 "argument with spaces" --flag

# Run directly with Python
python -m echo_app.main [arguments...]
```

### Available MCP Tools

The server provides these tools:

1. **hello_world**: Returns "Hello, world!" message
2. **get_command_line_args**: Returns command-line arguments passed to the server
3. **get_environment_variables**: Returns environment variables with ECHO_ prefix

### MCP Client Usage

Connect to the server using any MCP-compatible client. The server uses stdio transport by default.

Example tool calls:
- `hello_world` - No parameters needed
- `get_command_line_args` - No parameters needed  
- `get_environment_variables` - No parameters needed

## Example Output

Starting the MCP server:

```bash
$ poetry run echo-app hello world --verbose
Starting Echo App MCP Server...
Available tools:
  - hello_world: Returns 'Hello, world!'
  - get_command_line_args: Returns command-line arguments
  - get_environment_variables: Returns ECHO_ environment variables

# Server will then wait for MCP client connections
```

Example MCP tool responses:

**hello_world tool:**
```json
"Hello, world!"
```

**get_command_line_args tool:**
```json
{
  "message": "Command-line arguments:",
  "args": [
    {"index": 1, "value": "hello"},
    {"index": 2, "value": "world"},
    {"index": 3, "value": "--verbose"}
  ]
}
```

**get_environment_variables tool:**
```json
{
  "message": "ECHO_ environment variables:",
  "variables": [
    {"name": "ECHO_HOME", "value": "/home/user"},
    {"name": "ECHO_DEBUG", "value": "true"},
    {"name": "ECHO_VERSION", "value": "1.0.0"}
  ]
}
```

## Docker Distribution

This application is distributed as a Docker image that supports both x86 and ARM architectures.

### Docker Hub

The image is automatically built and published to Docker Hub via GitHub Actions:
- **Repository**: `sualeh/echo-app`
- **Platforms**: `linux/amd64`, `linux/arm64`
- **Tags**: `latest`, version tags (e.g., `v1.0.0`), and branch tags

### Using Docker

The MCP server is also available as a Docker image:

```bash
# Run MCP server without arguments
docker run --rm sualeh/echo-app

# Run MCP server with arguments  
docker run --rm sualeh/echo-app arg1 arg2 "argument with spaces" --flag

# Run with environment variables
docker run --rm -e MY_VAR=test sualeh/echo-app
```

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