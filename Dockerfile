FROM python:3.11-slim

# Set the working directory directly in the container
WORKDIR /app

# Install basic system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install the browser binaries needed for the Research Agent's scraper tool
# Playwright resolves missing system dependencies dynamically
RUN playwright install --with-deps chromium

# Copy the entire workspace into the image
COPY . .

# Expose the API port standard for App Runner deployments
EXPOSE 8080

# Command to execute when the container triggers
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8080"]
