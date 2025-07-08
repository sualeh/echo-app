# Echo App MCP Server

A simple MCP (Model Context Protocol) server that provides tools for accessing command-line arguments and environment variables.

## Tools

- `get_command_line_args()` - Returns command-line arguments passed to the server
- `get_environment_variables()` - Returns environment variables with `ECHO_` prefix

## Usage

```bash
python -m echo_app.main [args...]
```

Set environment variables with `ECHO_` prefix to make them available through the server.

## Docker

```bash
docker run sualehfatehi/echo-app
