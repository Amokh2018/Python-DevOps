# Variables
include .env
export

.PHONY: build run stop clean test help

# Show help
help:
	@echo "Available commands:"
	@echo "  make build    - Build the Docker image"
	@echo "  make run      - Run the Flask app in a Docker container"
	@echo "  make stop     - Stop the running container"
	@echo "  make clean    - Remove stopped containers"
	@echo "  make test     - Run the unit tests"

# initialization:
init:
	@echo "initialization...";
	@echo "Creation d'un environment virtuelle";\
	python3 -m venv .venv;\
	source .venv/bin/activate;\
	@echo " installer les librairies";\
	pip3 install -r requirements.txt

test-env:
	@echo "port = $(PORT)"
# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Flask app
run:
	docker run -d -p $(PORT):5000 $(IMAGE_NAME)

# Stop the running container
stop:
	docker stop $$(docker ps -q --filter ancestor=$(IMAGE_NAME))

# Clean up stopped containers
clean:
	docker rm $$(docker ps -a -q)

# Run the tests
test:
	python3 test.py
