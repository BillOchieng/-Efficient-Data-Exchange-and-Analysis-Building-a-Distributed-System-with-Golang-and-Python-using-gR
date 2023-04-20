package main

import (
    "fmt"
    "log"
    "net/http"
)

func home(w http.ResponseWriter, r *http.Request) {
    // Write the response to the HTTP response writer
    fmt.Fprintf(w, "Welcome to Bill's Go server! 🚀")
}

func contact(w http.ResponseWriter, r *http.Request) {
    // Write the response to the HTTP response writer
    fmt.Fprintf(w, "Email: ochieng@allegheny.com")
}

func submit(w http.ResponseWriter, r *http.Request) {
    // Parse the form data from the request body
    err := r.ParseForm()
    if err != nil {
        http.Error(w, "Failed to parse form data", http.StatusBadRequest)
        return
    }

    // Get the name and email values from the form data
    name := r.FormValue("name")
    email := r.FormValue("email")

    // Write the response to the HTTP response writer
    fmt.Fprintf(w, "Thanks for submitting the form, %s! We'll contact you at %s.", name, email)
}

func main() {
    // Define the HTTP endpoints and handlers
    http.HandleFunc("/", home)
    http.HandleFunc("/contact", contact)
    http.HandleFunc("/submit", submit)

    // Start the HTTP server on port 8200
    log.Fatal(http.ListenAndServe(":8200", nil))
}
