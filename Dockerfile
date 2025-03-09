# Use the official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Set the default command to run your CLI app
CMD ["python", "my_project/main.py"]

