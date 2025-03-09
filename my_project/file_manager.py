import os

class FileManager:
    """Handles file reading and writing operations."""

    def __init__(self, file_path):
        self.file_path = file_path

    def write_data(self, data):
        """Writes data to the file."""
        with open(self.file_path, "w") as file:
            file.write(data)

    def read_lines(self):
        """Reads all lines from the file."""
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as file:
            return file.readlines()

    def count_lines(self):
        """Counts the number of lines in the file."""
        return len(self.read_lines())
