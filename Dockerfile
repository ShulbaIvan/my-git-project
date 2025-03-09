# Use an official Python image as a base
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run the CLI script
CMD ["python", "my_project/main.py"]

