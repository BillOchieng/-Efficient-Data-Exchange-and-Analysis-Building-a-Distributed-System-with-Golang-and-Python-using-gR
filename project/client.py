import requests
import json

# Read the users from the JSON file
with open("users.json") as f:
    users = json.load(f)["users"]

# Loop through the users and send a POST request to the Go server
for user in users:
    url = "http://localhost:8080/users"
    data = {
        "name": user["name"],
        "email": user["email"],
        "phone": user["phone"]
    }
    response = requests.post(url, json=data)
    print(response.json())
