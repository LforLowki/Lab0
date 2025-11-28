# Build stage
FROM python:3.13-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml README.md ./
COPY lab1 ./lab1
RUN pip install --upgrade pip && pip install .

# Final image
FROM python:3.13-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY . .
EXPOSE 8000
CMD ["uvicorn", "lab1.api.api:app", "--host", "0.0.0.0", "--port", "8000"]
