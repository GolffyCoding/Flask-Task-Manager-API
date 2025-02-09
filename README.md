
# Flask Task Manager API

## Overview
This is a simple Flask-based RESTful API for managing tasks. It allows users to create, retrieve, update, and delete tasks.

## Features
- Retrieve all tasks
- Create a new task
- Retrieve a specific task by ID
- Update a task
- Delete a task

## Installation
### Prerequisites
- Python 3.x
- `pip` package manager

### Setup
1. Clone this repository:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the API
To start the Flask application, run:
```sh
python app.py
```
The API will be available at `http://127.0.0.1:5000/`

## API Endpoints

### Get all tasks
```http
GET /tasks
```
Response:
```json
{
  "tasks": []
}
```

### Create a new task
```http
POST /tasks
```
Request Body:
```json
{
  "title": "New Task",
  "description": "Task description"
}
```
Response:
```json
{
  "task": {
    "id": 1,
    "title": "New Task",
    "description": "Task description",
    "done": false
  }
}
```

### Get a specific task
```http
GET /tasks/{task_id}
```
Response:
```json
{
  "task": {
    "id": 1,
    "title": "New Task",
    "description": "Task description",
    "done": false
  }
}
```

### Update a task
```http
PUT /tasks/{task_id}
```
Request Body:
```json
{
  "title": "Updated Task",
  "done": true
}
```
Response:
```json
{
  "task": {
    "id": 1,
    "title": "Updated Task",
    "description": "Task description",
    "done": true
  }
}
```

### Delete a task
```http
DELETE /tasks/{task_id}
```
Response:
```json
{
  "result": true
}
```

## Running Tests
To run unit tests, use:
```sh
pytest test_app.py
```

## Dependencies
- Flask==2.0.1
- pytest==7.0.1

## License
This project is licensed under the MIT License.


![Screenshot 2025-02-09 234256](https://github.com/user-attachments/assets/747e51da-d72a-41b5-a5f6-385480f7367d)
