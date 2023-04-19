package main

import (
	"fmt"
	"sync"
	"time"
	"net/http"
	"io/ioutil"
)

var counter int // shared counter
var mutex sync.Mutex // mutex for synchronizing access to counter

func increment() {
	for i := 0; i < 1000; i++ {
		mutex.Lock() // acquire lock
		counter++
		mutex.Unlock() // release lock
	}
}

func decrement() {
	for i := 0; i < 1000; i++ {
		mutex.Lock() // acquire lock
		counter--
		mutex.Unlock() // release lock
	}
}

func fetchWebData() {
	resp, err := http.Get("https://example.com/data") // Fetch data from a web page
	if err != nil {
		fmt.Println("Error fetching web data:", err)
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error reading web data:", err)
		return
	}

	fmt.Println("Fetched web data:", string(body))
}

func main() {
	// Initialize counter
	counter = 0

	// Launch 10 additional goroutines to increment, decrement, and fetch web data concurrently
	for i := 0; i < 5; i++ {
		go increment()
		go decrement()
		go fetchWebData()
	}

	// Sleep for a while to allow goroutines to complete
	time.Sleep(2 * time.Second)

	// Print final value of counter
	fmt.Println("Counter:", counter)
}
