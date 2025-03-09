# main.py - Reads a file and counts the number of lines

def count_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    file_name = "data.txt"
    print(f"Total lines in {file_name}: {count_lines(file_name)}")

