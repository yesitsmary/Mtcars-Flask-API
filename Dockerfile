# Use lightweight version of Python 3.12
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /server

# Copy the requirements.txt
COPY requirements.txt requirements.txt

# Install the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all remaining project files into the container
COPY . .

# Set the command to run the Flask app
CMD ["python", "server.py"]
