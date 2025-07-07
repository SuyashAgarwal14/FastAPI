# FastAPI Backend

A simple FastAPI backend application that allows users to log in, submit text prompts, and receive dummy AI responses. The application stores and returns a history of submitted prompts and responses for each user.

## Features

- **Authentication System**: Token-based authentication with hardcoded users
- **Prompt Submission**: Submit text prompts and receive dummy AI responses
- **History Tracking**: Store and retrieve prompt/response history per user
- **Persistent Storage**: Save history to JSON file (bonus feature)
- **Error Handling**: Proper HTTP status codes and error messages

## Project Structure

```
fastapi/
├── main.py - FastAPI app entrypoint
├── routes.py - All API endpoints
├── models.py- Pydantic request/response models
├── auth.py - Authentication logic
├── history.py - Prompt history saving/loading
├── prompt_history.json - Stores user prompt/response history
├── requirements.txt
└── README.md
```

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/SuyashAgarwal14/FastAPI.git
   cd FastAPI
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```
   
   Alternative using uvicorn directly:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the application**
   - API Base URL: `http://localhost:8000`
   - Interactive API Documentation: `http://localhost:8000/docs`
   - Alternative API Documentation: `http://localhost:8000/redoc`

## API Endpoints

### 1. Login
**POST** `/login/`

Authenticate a user and receive a token.

**Request:**
```json
{
  "username": "alice",
  "password": "password123"
}
```

**Response:**
```json
{
  "token": "abc123..."
}
```

### 2. Submit Prompt
**POST** `/prompt/`

Submit a text prompt and receive a dummy AI response.

**Headers:**
```
Authorization: Bearer <your-token>
Content-Type: application/json
```

**Request:**
```json
{
  "prompt": "Tell me your name."
}
```

**Response:**
```json
{
  "response": "I'm not sure, but let's find out together."
}
```

### 3. Get History
**GET** `/history/`

Retrieve your prompt/response history.

**Headers:**
```
Authorization: Bearer <your-token>
```

**Response:**
```json
 "alice": [
   {
     "timestamp": "2025-07-07T12:16:13",
     "prompt": "Tell me your name.",
     "response": "I'm not sure, but let's find out together."
   }
]
```


## Example Usage

### Using curl

1. **Login**
   ```bash
   curl -X POST "http://localhost:8000/login/" \
        -H "Content-Type: application/json" \
        -d '{"username": "alice", "password": "password123"}'
   ```

2. **Submit Prompt** (replace TOKEN with actual token from login)
   ```bash
   curl -X POST "http://localhost:8000/prompt/" \
        -H "Authorization: Bearer TOKEN" \
        -H "Content-Type: application/json" \
        -d '{"prompt": "Tell me your name."}'
   ```

3. **Get History**
   ```bash
   curl -X GET "http://localhost:8000/history/" \
        -H "Authorization: Bearer TOKEN"
   ```

4. **Logout**
   ```bash
   curl -X POST "http://localhost:8000/logout/" \
        -H "Authorization: Bearer TOKEN"
   ```

### Using Python requests

```python
import requests

# Login
response = requests.post(
    "http://localhost:8000/login/",
    json={"username": "alice", "password": "password123"}
)
token = response.json()["token"]

# Submit prompt
response = requests.post(
    "http://localhost:8000/prompt/",
    headers={"Authorization": f"Bearer {token}"},
    json={"prompt": "Tell me a joke"}
)
print(response.json())

# Get history
response = requests.get(
    "http://localhost:8000/history/",
    headers={"Authorization": f"Bearer {token}"}
)
print(response.json())
```

## Hardcoded Users

The application comes with three test users:
- **Username:** `alice`, **Password:** `password123`
- **Username:** `bob`, **Password:** `secret`
- **Username:** `suyash`, **Password:** `Gennovation@123`

## Application Architecture

The application is structured as follows:

- **Authentication**: Token-based authentication using FastAPI's HTTPBearer
- **Data Storage**: In-memory storage with optional JSON file persistence
- **Request Validation**: Pydantic models for request/response validation
- **Error Handling**: Proper HTTP status codes and error messages
- **Security**: Bearer token authentication for protected endpoints

## Bonus Features Implemented

✅ **Persistent Storage**: History is saved to `prompt_history.json` file  
✅ **Logout Endpoint**: Invalidate tokens when logging out  
✅ **Comprehensive Error Handling**: Proper HTTP status codes and messages  
✅ **Interactive Documentation**: Auto-generated API documentation  

## Known Limitations

- **In-Memory Authentication**: Tokens are stored in memory and will be lost on server restart
- **No User Registration**: Users are hardcoded in the application
- **No Rate Limiting**: No built-in rate limiting (mentioned as optional bonus)
- **No Real AI Integration**: Uses dummy responses instead of real AI API
- **No Password Hashing**: Passwords are stored in plain text (not production-ready)

## Development Notes

- The application uses FastAPI's automatic OpenAPI schema generation
- Token generation uses Python's `secrets` module for cryptographically secure tokens
- History is stored both in memory and persistently in JSON format
- The application includes proper type hints and Pydantic models for validation

## License

This project is for educational purposes and demonstration of FastAPI concepts.
