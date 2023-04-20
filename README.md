# GOLANG  REST API

- This Go code defines an HTTP server that listens for requests on port 8200. It has three endpoints: /,' /contact, and /submit.The home function handles requests to the / endpoint and simply writes a welcome message to the HTTP response writer.The contact function handles requests to the /contact endpoint and writes an email address to the HTTP response writer.

- The submit function handles requests to the /submit endpoint and processes form data sent in the request body. It parses the form data, gets the values for the name and email fields, and writes a thank-you message to the HTTP response writer. The main function defines the HTTP endpoints and handlers using the http.HandleFunc function, and starts the HTTP server using the http.ListenAndServe function.

## PYTHON REQUESTS

- This Python code uses the requests library to send HTTP requests to the Go HTTP server running on port 8200.
The first request sends an HTTP GET request to the / endpoint and prints the response. The second request sends an HTTP GET request to the /contact endpoint and prints the response. The third request sends an HTTP POST request to the /submit endpoint with some data and prints the response.

**To run the Go code, you can save it to a file named "main.go" and run it using the "go run" command:**

```go
Copy code
$ go run main.go
```
