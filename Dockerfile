# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the Docker image
WORKDIR /app

# Copy the requirements file into the Docker image
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Copy the entire Flask app into the Docker image
COPY . .

# Expose port 5000
EXPOSE 5000

# Command to run the Flask application
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]