import os
import pytest
from my_project.file_manager import FileManager

TEST_FILE = "test_data.txt"

@pytest.fixture
def file_manager():
    """Fixture to create and clean up a test file."""
    fm = FileManager(TEST_FILE)
    yield fm
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_write_and_read(file_manager):
    """Tests writing and reading from a file."""
    file_manager.write_data("Hello\nWorld")
    assert file_manager.read_lines() == ["Hello\n", "World"]

def test_count_lines(file_manager):
    """Tests line counting functionality."""
    file_manager.write_data("Line 1\nLine 2\nLine 3")
    assert file_manager.count_lines() == 3
