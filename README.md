# Project Documentation: Go Server with Python Client

## Introduction

This project is a demonstration of a simple client-server application that communicates via HTTP protocol. The server-side of the application is written in Go programming language while the client-side is implemented using Python programming language. The project provides endpoints for a homepage, a contact page, and a form submission page. The server receives JSON data from the client and sends back a JSON response.

## Server-Side Implementation

The server-side implementation of the application is written in Go programming language. It consists of four main components; the main function, endpoints, request handlers, and configuration file. The main function is the entry point of the application. It reads the configuration file that specifies the port and website details, defines the HTTP endpoints and request handlers, and starts the server on the specified port.

** The application provides three endpoints:

'/' - The homepage endpoint that returns a welcome message.
'/contact' - The contact page endpoint that returns an email address.
'/submit' - The form submission endpoint that receives a JSON object from the client containing name and email values, and sends back a JSON response.
The request handlers for the endpoints are implemented as separate functions. They receive HTTP requests, process them, and send back HTTP responses. For example, the request handler for the '/submit' endpoint parses the JSON data from the request body, extracts the name and email values, generates a response JSON object, and sends it back to the client.

## Client-Side Implementation

The client-side implementation of the application is written in Python programming language. It consists of a single file that sends HTTP requests to the server and receives HTTP responses. The requests are sent using the requests library, and the data is sent and received in JSON format.

** The client sends three HTTP requests to the server:

GET request to the '/' endpoint to retrieve the homepage message.
GET request to the '/contact' endpoint to retrieve the contact email address.
POST request to the '/submit' endpoint to submit a form containing name and email values.
The client handles the HTTP responses by checking the status codes and reading the response data. For example, the client checks the status code of the HTTP response to the '/submit' endpoint to verify that the data was successfully submitted. It then reads the JSON response object sent by the server and prints the message to the console.

## Summary

This project is a simple demonstration of a client-server application using HTTP protocol. The server-side is implemented in Go programming language while the client-side is implemented in Python programming language. The server provides three endpoints; a homepage, a contact page, and a form submission page, while the client sends HTTP requests to these endpoints to retrieve and submit data. The project can be extended by adding more endpoints and implementing additional features such as authentication and database integration.
