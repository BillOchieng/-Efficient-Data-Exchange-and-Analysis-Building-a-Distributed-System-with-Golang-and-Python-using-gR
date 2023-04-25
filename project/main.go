package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

type Config struct {
	Port    string `json:"ServerPort"`
	Website string `json:"Website"`
}

type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
	Phone string `json:"phone"`
}

type Users struct {
	Users []User `json:"users"`
}

type UserStore struct {
	users []User
}

func NewUserStore(filename string) (*UserStore, error) {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}

	var users Users
	err = json.Unmarshal(data, &users)
	if err != nil {
		return nil, err
	}

	return &UserStore{users.Users}, nil
}

func (us *UserStore) UsersHandler(w http.ResponseWriter, r *http.Request) {
	jsonResponse, err := json.Marshal(us.users)
	if err != nil {
		http.Error(w, "Failed to create JSON response", http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(jsonResponse)
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome to Bill's Go server! 🚀")
}

func contactHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Email: ochieng@allegheny.com")
}

func submitHandler(w http.ResponseWriter, r *http.Request) {
	decoder := json.NewDecoder(r.Body)
	var data map[string]string
	err := decoder.Decode(&data)
	if err != nil {
		http.Error(w, "Failed to parse JSON data", http.StatusBadRequest)
		return
	}

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

	response := map[string]string{
		"message": fmt.Sprintf("Thanks for submitting the form, %s! We'll contact you at %s.", name, email),
	}
	jsonResponse, err := json.Marshal(response)
	if err != nil {
		http.Error(w, "Failed to create JSON response", http.StatusInternalServerError)
		return
	}

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

	// Initialize the users
	userStore, err := NewUserStore("users.json")
	if err != nil {
		log.Fatal("Failed to initialize user store")
	}

	// Define the HTTP endpoints and handlers
	http.HandleFunc("/", homeHandler)
	http.HandleFunc("/contact", contactHandler)
	http.HandleFunc("/submit", submitHandler)
	http.HandleFunc("/users", userStore.UsersHandler)

	// Start the HTTP server on the configured port
	// Start the HTTP server on the configured port
	log.Printf("Starting server on port %s\n", config.Port)
	log.Fatal(http.ListenAndServe(":"+config.Port, nil))
}