all: thread

clean:
	rm -f bin/thread
bin:
	mkdir bin

thread: thread.go bin
	go build --o bin thread.go