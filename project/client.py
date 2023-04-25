import requests
import json

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

# Send an HTTP POST request to the '/submit' endpoint in the Go code with JSON data
data = {
    "name": "Bill Ochieng",
    "email": "ochieng01@allegheny.edu"
}
json_data = json.dumps(data)
headers = {'Content-type': 'application/json'}
response = requests.post('http://localhost:8200/submit', data=json_data, headers=headers)

if response.status_code == 200:
    response_data = json.loads(response.text)
    print(response_data['message'])
else:
    print(f"Error: {response.status_code}")
