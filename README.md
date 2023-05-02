# Introduction 

* My project is about the implementation of a small-scale web application that allows users to submit a contact form, stores the submitted data in a JSON file, and provides an interface to query the stored data. The project also includes unit tests for the server's endpoints to ensure they are functioning correctly.


## Design of my project

```sql
+----------+         +------------+
|          |         |            |
|   User   |  <----  |   System   |
|          |         |            |
+----------+         +------------+
     |                      |
     |                      |
     v                      v
+----------+         +------------+
|          |         |            |
| Database |  <----  |   Program  |
|          |         |            |
+----------+         +------------+

```

## Implementation of my project

* The Python client application communicates with the web application through HTTP requests, and retrieves user information from the database using SQL queries. The database is implemented using SQLite and stores user information in a table with columns for id, name, email, and phone. The client application uses the SQLAlchemy ORM to interact with the database. The user data is also stored in a separate JSON file, which is read by the Go web application and used to populate the initial state of the database. The configuration files specify settings for the web application and database, such as the database file path and server port number.
Evaluation and Testing of your Program


Since there are multiple files involved in the project, I will provide instructions for running and testing each of them separately.


### For the Go web application:

Open a terminal and navigate to the project directory.
Run the following command to start the web application: "go run main.go."
Open a web browser and go to http://localhost:8080 to see the welcome page.
To test the web application:

```py
Open a terminal and navigate to the project directory.
Run the following command to start the test server: go run main.go test.
rawlings@Bills-MacBook-Pro project % go run main.go test.
2023/05/02 00:02:36 Starting server on port 8080
2023/05/02 00:02:36 listen tcp :8080: bind: address already in use
```

```py
Open another terminal and navigate to the project directory.
Run the following command to execute the test script: python3 test_client.py
The output should indicate whether all test cases passed or not.


rawlings@Bills-MacBook-Pro project % python test_client.py  
FFE./Users/rawlings/.pyenv/versions/3.9.7/lib/python3.9/unittest/suite.py:84: ResourceWarning: unclosed file <_io.BufferedReader name=10>
  return self.run(*args, **kwds)
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/Users/rawlings/.pyenv/versions/3.9.7/lib/python3.9/unittest/suite.py:84: ResourceWarning: unclosed file <_io.BufferedReader name=14>
  return self.run(*args, **kwds)
ResourceWarning: Enable tracemalloc to get the object allocation traceback

======================================================================
ERROR: test_users (__main__.TestClient)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/rawlings/Desktop/CMPSC-PL/-Efficient-Data-Exchange-and-Analysis-Building-a-Distributed-System-with-Golang-and-Python-using-gR/project/test_client.py", line 61, in test_users
    p.stdin.write(b"quit\n")
ValueError: write to closed file

======================================================================
FAIL: test_contact (__main__.TestClient)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/rawlings/Desktop/CMPSC-PL/-Efficient-Data-Exchange-and-Analysis-Building-a-Distributed-System-with-Golang-and-Python-using-gR/project/test_client.py", line 35, in test_contact
    self.assertIn("Contact", response.text)
AssertionError: 'Contact' not found in 'Email: ochieng@allegheny.com'

======================================================================
FAIL: test_submit (__main__.TestClient)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/rawlings/Desktop/CMPSC-PL/-Efficient-Data-Exchange-and-Analysis-Building-a-Distributed-System-with-Golang-and-Python-using-gR/project/test_client.py", line 46, in test_submit
    self.assertEqual(response.status_code, 200)
AssertionError: 400 != 200

----------------------------------------------------------------------
Ran 4 tests in 4.344s

FAILED (failures=2, errors=1)
```

### For the Python client:

Open a terminal and navigate to the project directory.
Run the following command to execute the client script: python3 client.py.
Follow the prompts to query user data by name.
Example program input and output:

```py
Enter a user's name to display their information, or type 'quit' to exit: Bill
2023-05-01 23:41:21,776 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, users.phone AS users_phone 
FROM users 
WHERE users.name = ?
 LIMIT ? OFFSET ?
2023-05-01 23:41:21,776 INFO sqlalchemy.engine.Engine [cached since 10.71s ago] ('Bill', 1, 0)
No user found with name 'Bill'.
Enter a user's name to display their information, or type 'quit' to exit: Shereen
2023-05-01 23:41:27,010 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, users.phone AS users_phone 
FROM users 
WHERE users.name = ?
 LIMIT ? OFFSET ?
2023-05-01 23:41:27,011 INFO sqlalchemy.engine.Engine [cached since 15.95s ago] ('Shereen', 1, 0)
Name: Shereen
Email: shereen@example.com
Phone: 555-555-2222
Enter a user's name to display their information, or type 'quit' to exit: 

```




*CAN BE CONTINUED TO A BIGGER PROJECT 🚀😃

- The type of concept demonstrated in the code is a basic client-server architecture used for communication between a client application and a server application over the internet. This type of architecture is commonly used in many real-time applications, such as online gaming, chat applications, and video streaming services.

- For example, in online gaming, the client-server architecture is used to facilitate real-time communication between players and the game server. The client sends input from the player to the server, which then processes the input and sends the game state back to the client. This process happens rapidly and repeatedly, allowing for seamless real-time gameplay.

- Similarly, chat applications use this architecture to allow users to send and receive messages in real-time. When a user sends a message, it is sent to the server and then broadcasted to all other connected clients in real-time, allowing for a seamless conversation experience.

- Video streaming services also use this architecture to deliver video content to users in real-time. The client requests video data from the server, which then streams the data back to the client in real-time, allowing for uninterrupted video playback.

- Anyway all i'm saying is the client-server architecture is an essential component of many real-time applications, enabling real-time communication and data transfer between clients and servers over the internet.





