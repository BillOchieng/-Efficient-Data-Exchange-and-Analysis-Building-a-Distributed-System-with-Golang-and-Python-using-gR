package main

import (
	"fmt"
	"log"
	"net/http"
)

func Home(w http.ResponseWriter, r *http.Request) {
	// This is what the function will print.
	fmt.Fprintf(w, "Welcome to Educative Home!")
}

func returnContact(w http.ResponseWriter, r *http.Request) {
	// This is what the function will print.
	fmt.Fprintf(w, "Email: support@educative.io")
}

func handleReq() {
	// will call Home function by default.
	http.HandleFunc("/", Home)
	http.HandleFunc("/contact", returnContact)

	log.Fatal(http.ListenAndServe(":8200", nil))
}

func main() {
	// starting the API
	handleReq()
}
