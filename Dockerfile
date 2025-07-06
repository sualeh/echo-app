# Use Python 3.12 slim image for smaller size
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY echo_app/ ./echo_app/

# Set the entry point to run the application directly
ENTRYPOINT ["python", "-m", "echo_app.main"]