# Project Documentation: Go Server with Python Client

## Introduction

The project is a simple web application written in the Go programming language that provides a basic RESTful API to retrieve and manipulate user data. The application makes use of a configuration file (config.json), a JSON data file for storing user data (users.json), and a client-side Python script (client.py) to interact with the API.

## Files

*config.json:* This file contains the configuration settings for the web application, such as the server port and website URL.

*users.json:* This file is used to store user data in JSON format. The User struct in main.go maps to the JSON data structure in this file.

*client.py:* This is a simple client script written in Python that demonstrates how to interact with the RESTful API provided by the web application. The script allows users to create, read, update, and delete user data.

*main.go:* This is the main source code file for the web application. It contains the handlers for each of the API endpoints, as well as the main function that initializes the HTTP server.

## Working together

- When the web application is launched, the main function in 'main.go' reads the configuration settings from "config.json", initializes a user store by reading the user data from "users.json", and then starts an HTTP server on the *specified port*. The HTTP server listens for *incoming requests* and *routes them to the appropriate handler function based on the URL path*.

## The API endpoints provided by the web application are

/: This endpoint returns a simple welcome message.

/contact: This endpoint returns the contact email address for the website.

/submit: This endpoint is used to submit a form with name and email fields. It returns a JSON response thanking the user for submitting the form and indicating that they will be contacted at the provided email address.

/users: This endpoint returns a list of all users in JSON format. It also supports creating new users, updating existing users, and deleting users.

## Real world application

- This project can be used as a starting point for building more complex RESTful API services. It demonstrates how to handle HTTP requests, parse JSON data, and interact with a file-based data store. With additional development, this web application could be extended to support additional API endpoints, more complex data models, and integration with external services or databases.

- A real-world application is a customer relationship management (CRM) system. The basic user data model provided in this project could be expanded to include additional fields such as customer addresses, phone numbers, and order histories. Additional API endpoints could be added to support features such as searching for customers by name, creating and updating orders, and generating reports on customer activity.
