# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port (not strictly necessary for Cloud Run, 
# but helpful if running locally)
EXPOSE 8080

# Comment: The command to start the Flask app
CMD ["python", "app.py"]
