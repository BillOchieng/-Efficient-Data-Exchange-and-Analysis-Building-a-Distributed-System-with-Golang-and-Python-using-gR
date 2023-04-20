# GOLANG  REST API

- This Go code defines an HTTP server that listens for requests on port 8200. It has three endpoints: /,' /contact, and /submit.The home function handles requests to the / endpoint and simply writes a welcome message to the HTTP response writer.The contact function handles requests to the /contact endpoint and writes an email address to the HTTP response writer.

- The submit function handles requests to the /submit endpoint and processes form data sent in the request body. It parses the form data, gets the values for the name and email fields, and writes a thank-you message to the HTTP response writer. The main function defines the HTTP endpoints and handlers using the http.HandleFunc function, and starts the HTTP server using the http.ListenAndServe function.
