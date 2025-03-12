# Use the official Python image as base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn python-jose

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "security_toolkit:app", "--host", "0.0.0.0", "--port", "8000"]
