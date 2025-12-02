# Base image with Python 3.13
FROM python:3.13-slim AS base

# Recommended environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv and project dependencies
FROM base AS builder

# Install uv
RUN pip install --no-cache-dir uv

# Copy project dependency files
COPY pyproject.toml .
COPY uv.lock* .

# Install project dependencies in the system environment
RUN uv pip install --system --no-cache .

# Copy source code and prepare execution environment
FROM base AS runtime

# Copy installed dependencies from builder
COPY --from=builder /usr/local /usr/local

# Copy the source code of the API, logic, and templates
COPY lab1/api ./lab1/api
COPY lab1/logic ./lab1/logic
COPY lab1/preprocessing ./lab1/preprocessing
COPY templates ./templates

# Expose FastAPI port
EXPOSE 8000

# Default command to start the API
CMD ["uvicorn", "lab1.api.api:app", "--host", "0.0.0.0", "--port", "8000"]
