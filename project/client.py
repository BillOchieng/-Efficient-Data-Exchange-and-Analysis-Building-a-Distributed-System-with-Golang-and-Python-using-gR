import requests
import json

# Send an HTTP GET request to the '/' endpoint in the Go code
try:
    response = requests.get('http://localhost:8200/')
    response.raise_for_status() # Raise an exception if the response has an HTTP error status code
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP error: {err}")
except requests.exceptions.RequestException as err:
    print(f"Error: {err}")

# Send an HTTP GET request to the '/contact' endpoint in the Go code
try:
    response = requests.get('http://localhost:8200/contact')
    response.raise_for_status() # Raise an exception if the response has an HTTP error status code
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP error: {err}")
except requests.exceptions.RequestException as err:
    print(f"Error: {err}")

# Send an HTTP POST request to the '/submit' endpoint in the Go code
data = {'name': 'John Doe', 'email': 'johndoe@example.com'}
try:
    response = requests.post('http://localhost:8200/submit', json=data)
    response.raise_for_status() # Raise an exception if the response has an HTTP error status code
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP error: {err}")
except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
