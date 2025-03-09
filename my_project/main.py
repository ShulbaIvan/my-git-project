import argparse
import os
import datetime
from file_manager import FileManager
from api_client import APIClient

# Define the file path
DATA_FILE = os.path.join(os.getcwd(), "data.txt")

# Initialize classes
file_manager = FileManager(DATA_FILE)
api_client = APIClient()

# Function to fetch and store data
def fetch_and_store_data():
    """Fetches data from API and saves it to the file."""
    data = api_client.fetch_data()
    if data:
        formatted_data = f"Title: {data['title']}\nBody: {data['body']}\n"
        file_manager.write_data(formatted_data)
        print(f"Data successfully stored in {DATA_FILE}")

# Function to count lines in file
def count_lines():
    """Counts lines in the stored file."""
    num_lines = file_manager.count_lines()
    print(f"Total number of lines: {num_lines}")

# Function to log execution timestamp
def log_timestamp():
    """Logs the script execution timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Script executed at: {timestamp}")

# CLI argument parsing
parser = argparse.ArgumentParser(description="CLI tool for file and API operations.")
parser.add_argument("--fetch", action="store_true", help="Fetch data from API and save to file")
parser.add_argument("--count", action="store_true", help="Count lines in the text file")
parser.add_argument("--log-time", action="store_true", help="Log execution time")

args = parser.parse_args()

# Execute functions based on arguments
if args.fetch:
    fetch_and_store_data()
if args.count:
    count_lines()
if args.log_time:
    log_timestamp()

# Show help if no arguments are passed
if not any(vars(args).values()):
    parser.print_help()
