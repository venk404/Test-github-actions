FROM python:3.13-alpine

WORKDIR /app

# Install required packages
RUN apk add --no-cache postgresql-dev gcc musl-dev

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the schema creation script
COPY Create_Student.py .

CMD ["python", "Create_Student.py"]
