import requests
import json

# Endpoint URLs
base_url = "http://localhost:8080"
welcome_url = f"{base_url}/"
contact_url = f"{base_url}/contact"
submit_url = f"{base_url}/submit"
users_url = f"{base_url}/users"

# Simple welcome message
response = requests.get(welcome_url)
print(response.text)

# Contact email address
response = requests.get(contact_url)
print(response.text)

# Read the users from the JSON file
with open("users.json") as f:
    users = json.load(f)["users"]

# Command-line interface
while True:
    query = input("Enter a user's name to display their information, or type 'quit' to exit: ")
    if query == "quit":
        break
    found = False
    for user in users:
        if user["name"].lower() == query.lower():
            found = True
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Phone: {user['phone']}")
            break
    if not found:
        print(f"No user found with name '{query}'.")

# Submit a form with name and email fields
form_data = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}
headers = {"Content-Type": "application/json"}
response = requests.post(submit_url, data=json.dumps(form_data), headers=headers)
print(response.text)
