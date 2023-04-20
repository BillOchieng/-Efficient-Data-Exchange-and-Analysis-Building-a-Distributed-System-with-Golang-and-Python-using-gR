all: main

clean:
	rm -f bin/main
bin:
	mkdir bin

thread: main.go bin
	go build --o bin main.go

