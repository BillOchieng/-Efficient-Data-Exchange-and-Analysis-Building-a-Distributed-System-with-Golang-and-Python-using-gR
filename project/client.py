import requests
import json

# Endpoint URLs
base_url = "http://localhost:8080"
welcome_url = f"{base_url}/"
contact_url = f"{base_url}/contact"
submit_url = f"{base_url}/submit"

# Simple welcome message
response = requests.get(welcome_url)
print(response.text)

# Contact email address
response = requests.get(contact_url)
print(response.text)

# Read the users from the JSON file
with open("users.json") as f:
    users = json.load(f)["users"]

# Loop through the users and send a POST request to the Go server
for user in users:
    url = f"{base_url}/users"
    data = {
        "name": user["name"],
        "email": user["email"],
        "phone": user["phone"]
    }
    response = requests.post(url, json=data)
    print(response.json())

# Submit a form with name and email fields
form_data = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}
headers = {"Content-Type": "application/json"}
response = requests.post(submit_url, data=json.dumps(form_data), headers=headers)
print(response.text)
