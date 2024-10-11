FROM python:3.9-alpine AS builder

WORKDIR /app

# Install build dependencies
RUN apk add --no-cache postgresql-dev gcc musl-dev make

# Create a virtual environment
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.9-alpine

WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /app/venv /app/venv
COPY . .

# Set environment variables
ENV PATH="/app/venv/bin:$PATH"

# Install runtime dependencies
RUN apk add --no-cache libpq

# Expose port 8000

EXPOSE 8000

# Run the application
CMD ["sh", "-c", "venv/bin/python DB/Schemas/Create_Student.py && venv/bin/uvicorn Main:app --host 0.0.0.0 --port 8000"]

