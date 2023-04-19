import requests
import json
import cProfile
import pandas as pd
import matplotlib.pyplot as plt

# I use try and except blocks to handle the JSONDecodeError exception that could occur if the response from the server is not a valid JSON string.
# If the exception is raised, I print an error message and set the data variable to an empty dictionary.
# This way, the rest of the code can still run without errors, even if there was a problem with the data received from the server.
try:
    response = requests.get("https://example.com/data")
    data = json.loads(response.text)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    data = {}

# Perform data analysis on data

# I use the `get` method from the `requests` library to send a GET request to the Golang server running on `localhost:8080`.
# We then use the `json` method to decode the JSON data received from the server.

# Once I have received the data in Python, I can use libraries like NumPy, Pandas, and Matplotlib to perform data analysis and visualization.

counter = 0
counter_data = []


def increment():
    global counter
    for i in range(1000000):
        counter += 1
    counter_data.append(counter)


def decrement():
    global counter
    for i in range(1000000):
        counter -= 1
    counter_data.append(counter)


cProfile.run("increment(); decrement()")

df = pd.DataFrame(counter_data, columns=["counter"])
df.to_csv("counter_data.csv", index=False)

mean = df.mean()["counter"]
std = df.std()["counter"]
max_val = df.max()["counter"]

print(f"Mean value of counter: {mean}")
print(f"Standard deviation of counter: {std}")
print(f"Maximum value of counter: {max_val}")

plt.plot(counter_data)
plt.xlabel("Time")
plt.ylabel("Counter Value")
plt.title("Counter Value over Time")
plt.show()
