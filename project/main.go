package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
)

// home handles HTTP requests to the '/' endpoint
func home(w http.ResponseWriter, r *http.Request) {
    // Write the response to the HTTP response writer
    fmt.Fprintf(w, "Welcome to Bill's Go server! 🚀")
}

// contact handles HTTP requests to the '/contact' endpoint
func contact(w http.ResponseWriter, r *http.Request) {
    // Write the response to the HTTP response writer
    fmt.Fprintf(w, "Email: ochieng@allegheny.com")
}

// FormData represents the expected structure of the form data in HTTP requests to the '/submit' endpoint
type FormData struct {
    Name  string `json:"name"`
    Email string `json:"email"`
}

// submit handles HTTP requests to the '/submit' endpoint
func submit(w http.ResponseWriter, r *http.Request) {
    // Parse the form data from the request body
    decoder := json.NewDecoder(r.Body)
    var formData FormData
    err := decoder.Decode(&formData)
    if err != nil {
        http.Error(w, "Failed to parse form data", http.StatusBadRequest)
        return
    }

    // Get the name and email values from the form data
    name := formData.Name
    email := formData.Email

    // Write the response to the HTTP response writer
    response := make(map[string]string)
    response["message"] = fmt.Sprintf("Thanks for submitting the form, %s! We'll contact you at %s.", name, email)
    jsonResponse, err := json.Marshal(response)
    if err != nil {
        http.Error(w, "Failed to encode response", http.StatusInternalServerError)
        return
    }
    w.Header().Set("Content-Type", "application/json")
    w.Write(jsonResponse)
}

func main() {
    // Define the HTTP endpoints and handlers
    http.HandleFunc("/", home)
    http.HandleFunc("/contact", contact)
    http.HandleFunc("/submit", submit)

    // Start the HTTP server on port 8200
    log.Fatal(http.ListenAndServe(":8200", nil))
}
