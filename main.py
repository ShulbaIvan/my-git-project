import argparse
import os
import sys
import datetime
import requests

# Define the API endpoint
API_URL = "https://jsonplaceholder.typicode.com/posts/1"  # Placeholder API

# Define the file path for data storage
DATA_FILE = os.path.join(os.getcwd(), "data.txt")

# Function to fetch data from API and write to file
def fetch_and_store_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        with open(DATA_FILE, "w") as file:
            file.write(f"Title: {data['title']}\n")
            file.write(f"Body: {data['body']}\n")

        print(f"Data successfully fetched and stored in {DATA_FILE}")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

# Function to count lines in the text file
def count_lines():
    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()
            print(f"Total number of lines in {DATA_FILE}: {len(lines)}")
    except FileNotFoundError:
        print("Error: Data file not found. Run the script with '--fetch' first.")

# Function to display the current timestamp
def log_timestamp():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Script executed at: {timestamp}")

# Set up argument parser
parser = argparse.ArgumentParser(description="A CLI tool for handling text file operations.")
parser.add_argument("--fetch", action="store_true", help="Fetch data from API and save to file")
parser.add_argument("--count", action="store_true", help="Count lines in the text file")
parser.add_argument("--log-time", action="store_true", help="Log the current timestamp")

# Parse the command-line arguments
args = parser.parse_args()

# Execute functions based on arguments
if args.fetch:
    fetch_and_store_data()
if args.count:
    count_lines()
if args.log_time:
    log_timestamp()

# If no arguments are provided, show help
if not any(vars(args).values()):
    parser.print_help()

