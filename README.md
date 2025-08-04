# Echo App MCP Server

A simple MCP (Model Context Protocol) server that provides tools for accessing command-line arguments and environment variables.

Use this app to test registration with the Docker MCP Registry.

## Usage

```bash
python -m echo_app.main [args...]
```

## Docker

### Build Docker Image

```bash
docker build -t sualehfatehi/echo-app:latest .
```

### Start Docker Container in `stdio` Mode

```bash
docker run -it -d sualehfatehi/echo-app
```
