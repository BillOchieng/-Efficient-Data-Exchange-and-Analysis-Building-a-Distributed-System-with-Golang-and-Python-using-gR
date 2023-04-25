# Makefile for the Go Server with Python Client project

# Variables
GO=go
PYTHON=python3
PKG=./...
BUILD_DIR=./bin
BUILD_NAME=webapp
CLIENT_SCRIPT=client.py

# Targets
all: build run
# all: Builds and runs the server.
build:
	@echo "Building server binary..."
	$(GO) build -o $(BUILD_DIR)/$(BUILD_NAME) $(PKG)
	@echo "Done."
# build: Builds the server binary and saves it to the bin directory.
run:
	@echo "Starting server..."
	$(BUILD_DIR)/$(BUILD_NAME)
	@echo "Server stopped."
# run: Starts the server.
test:
	@echo "Running tests..."
	$(GO) test -v $(PKG)
	@echo "Done."
# test: Runs the unit tests.
clean:
	@echo "Cleaning up..."
	rm -rf $(BUILD_DIR)
	@echo "Done."
# clean: Removes all build artifacts.
client:
	@echo "Starting client..."
	$(PYTHON) $(CLIENT_SCRIPT)
	@echo "Client stopped."
# client: Starts the Python client.