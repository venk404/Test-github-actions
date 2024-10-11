.ONESHELL:

# Variables
VENV := venv
DB_SERVICE := postgres
MIGRATION_DIR := ./DB/Schemas
MIGRATION_IMAGE := migrations_img
MIGRATION_CONTAINER := migrations_container
NETWORK_NAME := dem
API_IMAGE := restapi
API_CONTAINER := restapi
API_PORT := 8000

# Determine OS-specific command prefix
ifeq ($(OS),Windows_NT)
    CMD_PREFIX :=
else
    CMD_PREFIX := 
endif

all: Run_all_containers

Run_all_containers:
	$(CMD_PREFIX) docker-compose up

Start_DB:
	$(CMD_PREFIX) docker-compose up $(DB_SERVICE)

run-migrations:
	$(CMD_PREFIX) docker build -t $(MIGRATION_IMAGE) $(MIGRATION_DIR)
	$(CMD_PREFIX) docker run --rm --name $(MIGRATION_CONTAINER) --network $(NETWORK_NAME) $(MIGRATION_IMAGE)

build-api:
	$(CMD_PREFIX) docker build -t $(API_IMAGE) .

run-api:
	$(CMD_PREFIX) docker run -d \
		--name $(API_CONTAINER) \
		--network $(NETWORK_NAME) \
		-p $(API_PORT):$(API_PORT) \
		$(API_IMAGE)


# Define a clean step
clean:
ifeq ($(OS),Windows_NT)
	@powershell -Command "Get-ChildItem -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force"
	@powershell -Command "Get-ChildItem -Recurse -Directory -Filter 'data' | Remove-Item -Recurse -Force"
else
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "data" -exec rm -rf {} +
endif

test:
ifeq ($(OS),Windows_NT)
	python test.py
else
	python test.py
endif

.PHONY: all Run_all_containers Start_DB run-migrations build-api run-api