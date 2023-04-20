package main

import (
	"fmt"
	"log"
	"net/http"
)

func home(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Bill is cool 😎 !")
}

func contact(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Email: support@educative.io")
}

func handleRequests() {
	http.HandleFunc("/", home)
	http.HandleFunc("/contact", contact)
	log.Fatal(http.ListenAndServe(":8200", nil))
}

func main() {
	handleRequests()
}
