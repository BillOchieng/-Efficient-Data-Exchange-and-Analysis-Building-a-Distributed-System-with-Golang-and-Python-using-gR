import requests
import json

# Define the base URL for the Go code
BASE_URL = 'http://localhost:8200'

def get_request(endpoint):
    """
    Send an HTTP GET request to the specified endpoint and return the response data as a JSON object.
    If an error occurs, raise an exception with a descriptive message.
    """
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}")
        response.raise_for_status() # Raise an exception if the response has an HTTP error status code
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"HTTP error: {err}")
    except requests.exceptions.RequestException as err:
        raise Exception(f"Error: {err}")

def post_request(endpoint, data):
    """
    Send an HTTP POST request to the specified endpoint with the given data and return the response data as a JSON object.
    If an error occurs, raise an exception with a descriptive message.
    """
    try:
        response = requests.post(f"{BASE_URL}/{endpoint}", json=data)
        response.raise_for_status() # Raise an exception if the response has an HTTP error status code
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"HTTP error: {err}")
    except requests.exceptions.RequestException as err:
        raise Exception(f"Error: {err}")

# Example usage:

# Send an HTTP GET request to the '/' endpoint in the Go code
try:
    data = get_request('')
    print(data)
except Exception as err:
    print(f"Error: {err}")

# Send an HTTP GET request to the '/contact' endpoint in the Go code
try:
    data = get_request('contact')
    print(data)
except Exception as err:
    print(f"Error: {err}")

# Send an HTTP POST request to the '/submit' endpoint in the Go code
data = {'name': 'John Doe', 'email': 'johndoe@example.com'}
try:
    data = post_request('submit', data)
    print(data)
except Exception as err:
    print(f"Error: {err}")
