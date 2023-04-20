import requests

# Send an HTTP GET request to the '/' endpoint in the Go code
response = requests.get('http://localhost:8200/')
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")

# Send an HTTP GET request to the '/contact' endpoint in the Go code
response = requests.get('http://localhost:8200/contact')
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")

# Send an HTTP POST request to the '/submit' endpoint in the Go code
data = {'name': 'John Doe', 'email': 'johndoe@example.com'}
response = requests.post('http://localhost:8200/submit', data=data)
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error: {response.status_code}")
