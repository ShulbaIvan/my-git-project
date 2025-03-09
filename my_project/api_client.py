import requests

class APIClient:
    """Handles API requests to fetch data."""

    API_URL = "https://jsonplaceholder.typicode.com/posts/1"

    @staticmethod
    def fetch_data():
        """Fetches data from the API."""
        try:
            response = requests.get(APIClient.API_URL)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
