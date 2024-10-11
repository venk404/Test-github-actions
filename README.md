
# Student Management API

This project is a simple Student Management API built using FastAPI. It allows for basic CRUD operations on student data. The API supports creating, reading, updating, and deleting student information.



## Features

- Create Student: Add a new student.
- Get All Students: Retrieve a list of all students.
- Get Student by ID: Retrieve a specific student by their ID.
- Update Student: Update a student's information.
- Delete Student: Delete a student by their ID.


## Requirments
- Python 3.11+
- PIP
- Docker & Docker Compose(For database)
- Make
## Installation
1) Clone the repository:

```bash
  git clone https://github.com/venk404/SRE--RestAPI.git
```
2) Execute the makeFile command (assuming make is installed on your system).

```bash
  cd .\Assignment 3
```
3) ## "Rename the .env file from the Schema folder and, in the root directory, the variable dev is used for versioning the image."


4) The following command will start the DB container, run the DB DML migrations, build the REST API, and run the REST API Docker container.
```bash
  make all
```
## If you want to perform each target individually, use the following commands
4) To start the DB container
```bash
  make Start_DB
```
5) Run the DB DML migrations

```bash
  make run-migrations
```
6) Build the REST API

```bash
  make build-api
```

7) Run the REST API Docker container

```bash
  make run-api
```



## To run Test
```bash
  make test
```

## Documentation(API Documentation)

- Refer to the API documentation for the endpoints listed below
```bash
  http://127.0.0.1:8000/docs
```

