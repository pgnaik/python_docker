# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Copy the rest of the application code into the container
COPY . .

# Specify the command to run the application
CMD ["python", "test.py"]
