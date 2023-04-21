package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

type Config struct {
	Port    string `json:"port"`
	Website string `json:"website"`
}

func home(w http.ResponseWriter, r *http.Request) {
	// Write the response to the HTTP response writer
	fmt.Fprintf(w, "Welcome to Bill's Go server! 🚀")
}

func contact(w http.ResponseWriter, r *http.Request) {
	// Write the response to the HTTP response writer
	fmt.Fprintf(w, "Email: ochieng@allegheny.com")
}

func submit(w http.ResponseWriter, r *http.Request) {
	// Parse the JSON data from the request body
	decoder := json.NewDecoder(r.Body)
	var data map[string]string
	err := decoder.Decode(&data)
	if err != nil {
		http.Error(w, "Failed to parse JSON data", http.StatusBadRequest)
		return
	}

	// Get the name and email values from the JSON data
	name, ok := data["name"]
	if !ok {
		http.Error(w, "Name field is missing", http.StatusBadRequest)
		return
	}
	email, ok := data["email"]
	if !ok {
		http.Error(w, "Email field is missing", http.StatusBadRequest)
		return
	}

	// Create a JSON response object
	response := map[string]string{
		"message": fmt.Sprintf("Thanks for submitting the form, %s! We'll contact you at %s.", name, email),
	}
	jsonResponse, err := json.Marshal(response)
	if err != nil {
		http.Error(w, "Failed to create JSON response", http.StatusInternalServerError)
		return
	}

	// Write the JSON response to the HTTP response writer
	w.Header().Set("Content-Type", "application/json")
	w.Write(jsonResponse)
}

func main() {
	// Read the config file
	configFile, err := ioutil.ReadFile("config.json")
	if err != nil {
		log.Fatal("Failed to read config file")
	}
	var config Config
	err = json.Unmarshal(configFile, &config)
	if err != nil {
		log.Fatal("Failed to parse config file")
	}

	// Define the HTTP endpoints and handlers
	http.HandleFunc("/", home)
	http.HandleFunc("/contact", contact)
	http.HandleFunc("/submit", submit)

	// Start the HTTP server on the configured port
	log.Printf("Starting server on port %s\n", config.Port)
	log.Fatal(http.ListenAndServe(":"+config.Port, nil))
}
