# On the Python side, you could use the `requests` library to send a request to the Golang server and receive the JSON data:

import requests

import cProfile
import pandas as pd
import matplotlib.pyplot as plt


response = requests.get("http://localhost:8080/")
data = response.json()

# Perform data analysis on data

# In this example, we use the `get` method from the `requests` library to send a GET request to the Golang server running on `localhost:8080`. We then use the `json` method to decode the JSON data received from the server.

# Once you have received the data in Python, you can use libraries like NumPy, Pandas, and Matplotlib to perform data analysis and visualization.

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
