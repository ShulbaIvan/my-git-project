import pytest
from my_project.api_client import APIClient

def test_fetch_data():
    """Tests API response."""
    data = APIClient.fetch_data()
    assert isinstance(data, dict), "Expected a dictionary response"
    assert "title" in data, "Response should contain 'title'"
    assert "body" in data, "Response should contain 'body'"
