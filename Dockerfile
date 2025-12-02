# Use Python 3.13 slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml README.md ./
COPY lab1 ./lab1
COPY templates ./templates

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install .           # installs your lab1 package
RUN pip install uvicorn[standard]  # ensure uvicorn is available

# Expose the port for FastAPI
EXPOSE 8000

# Command to run the API
CMD ["uvicorn", "lab1.api.api:app", "--host", "0.0.0.0", "--port", "8000"]
