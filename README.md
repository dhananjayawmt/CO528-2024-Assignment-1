# FastAPI JSON CRUD Application

This is a simple REST API built with FastAPI that performs CRUD (Create, Read, Update, Delete) operations on items stored in a JSON file. The application is dockerized and can be easily deployed as a Docker container.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete items using HTTP requests.
- **JSON File Storage**: Data is persisted in a JSON file (`items.json`), making it easy to manage and inspect.
- **FastAPI**: Leverages FastAPI for high performance and automatic generation of interactive API documentation.
- **Dockerized**: Easily deploy the application using Docker.

## Getting Started

### Prerequisites

- [Python 3.10](https://www.python.org/downloads/) or higher
- [Docker](https://www.docker.com/products/docker-desktop)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/dhananjayawmt/CO528-2024-Assignment-1.git
   cd fastapi-json-crud
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application locally**:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be accessible at `http://127.0.0.1:8000`.

5. **Access API Documentation**:

   - Open your browser and go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive Swagger UI.

### Docker Deployment

1. **Build the Docker image**:

   ```bash
   docker build -t fastapi-json-crud .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -d --name fastapi-json-crud -p 8000:8000 fastapi-json-crud
   ```

   The API will be accessible at `http://localhost:8000`.

## API Endpoints

### 1. Create an Item

- **Endpoint**: `POST /items/`
- **Parameters**:
  - **Body**: JSON object with the following fields:
    - `id` (integer, required): Unique identifier for the item.
    - `name` (string, required): Name of the item.
    - `description` (string, optional): Description of the item.
    - `price` (float, required): Price of the item.
- **Response**:
  - **200 OK**: Returns the created item.
  - **400 Bad Request**: If an item with the same ID already exists.

  ```json
  {
    "id": 1,
    "name": "Item1",
    "description": "A test item",
    "price": 10.0
  }
  ```

### 2. Get All Items

- **Endpoint**: `GET /items/`
- **Parameters**: None
- **Response**:
  - **200 OK**: Returns a list of all items.

  ```json
  [
    {
      "id": 1,
      "name": "Item1",
      "description": "A test item",
      "price": 10.0
    },
    {
      "id": 2,
      "name": "Item2",
      "description": "Another item",
      "price": 15.0
    }
  ]
  ```

### 3. Get a Single Item by ID

- **Endpoint**: `GET /items/{item_id}`
- **Parameters**:
  - **Path**: `item_id` (integer, required): The ID of the item to retrieve.
- **Response**:
  - **200 OK**: Returns the item with the specified ID.
  - **404 Not Found**: If the item does not exist.

  ```json
  {
    "id": 1,
    "name": "Item1",
    "description": "A test item",
    "price": 10.0
  }
  ```

### 4. Update an Item

- **Endpoint**: `PUT /items/{item_id}`
- **Parameters**:
  - **Path**: `item_id` (integer, required): The ID of the item to update.
  - **Body**: JSON object with the updated fields:
    - `id` (integer, required): Unique identifier for the item.
    - `name` (string, required): Name of the item.
    - `description` (string, optional): Description of the item.
    - `price` (float, required): Price of the item.
- **Response**:
  - **200 OK**: Returns the updated item.
  - **404 Not Found**: If the item does not exist.

  ```json
  {
    "id": 1,
    "name": "Updated Item",
    "description": "An updated test item",
    "price": 20.0
  }
  ```

### 5. Delete an Item

- **Endpoint**: `DELETE /items/{item_id}`
- **Parameters**:
  - **Path**: `item_id` (integer, required): The ID of the item to delete.
- **Response**:
  - **200 OK**: Returns a message confirming the deletion.
  - **404 Not Found**: If the item does not exist.

  ```json
  {
    "message": "Item deleted"
  }
  ```

### Testing

You can test the API using tools like [Postman](https://www.postman.com/) or `curl`. Below are some sample `curl` commands:

- **Create an Item**:

  ```bash
  curl -X POST "http://localhost:8000/items/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Item1", "description": "A test item", "price": 10.0}'
  ```

- **Get All Items**:

  ```bash
  curl -X GET "http://localhost:8000/items/"
  ```

- **Get a Specific Item**:

  ```bash
  curl -X GET "http://localhost:8000/items/1"
  ```

- **Update an Item**:

  ```bash
  curl -X PUT "http://localhost:8000/items/1" -H "Content-Type: application/json" -d '{"id": 1, "name": "Updated Item", "description": "An updated test item", "price": 20.0}'
  ```

- **Delete an Item**:

  ```bash
  curl -X DELETE "http://localhost:8000/items/1"
  ```

### Repository Structure

```plaintext
fastapi-json-crud/
│
├── main.py                # Main application file with FastAPI endpoints
├── items.json             # JSON file for data storage
├── Dockerfile             # Dockerfile to build the application image
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```
