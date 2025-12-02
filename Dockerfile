# Build stage
FROM python:3.13-slim AS builder
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# Copy project metadata and source
COPY pyproject.toml README.md ./
COPY lab1 ./lab1

# Install Python dependencies in the builder stage
RUN pip install --upgrade pip
RUN pip install .  # installs your package
RUN pip install uvicorn[standard]  # ensure uvicorn is installed in the builder

# Final image
FROM python:3.13-slim
WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

# Copy the source code
COPY . .

# Expose port
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "lab1.api.api:app", "--host", "0.0.0.0", "--port", "8000"]
