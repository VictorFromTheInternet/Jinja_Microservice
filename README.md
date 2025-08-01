# Hello World FastAPI Microservice

A simple FastAPI microservice demonstrating the use of routers and controllers.

## Project Structure

```
Jinja Microservice/
├── app/
│   ├── __init__.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── hello_controller.py
│   └── routers/
│       ├── __init__.py
│       └── hello_router.py
├── server.py
├── run.py
├── requirements.txt
└── README.md
```

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

You can run the application in several ways:

### Option 1: Using the run script
```bash
python run.py
```

### Option 2: Using uvicorn directly
```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

### Option 3: Running the server file directly
```bash
python server.py
```

## API Endpoints

The application will be available at `http://localhost:8000`

### Available Endpoints:

- **GET /** - Root endpoint with basic info
- **GET /api/v1/hello/** - Simple hello world message
- **GET /api/v1/hello/greet/{name}** - Personalized greeting with path parameter
- **GET /api/v1/hello/greet?name=YourName** - Personalized greeting with query parameter
- **GET /api/v1/hello/health** - Health check endpoint

### Interactive API Documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Example Usage

```bash
# Basic hello world
curl http://localhost:8000/api/v1/hello/

# Personalized greeting with path parameter
curl http://localhost:8000/api/v1/hello/greet/John

# Personalized greeting with query parameter
curl "http://localhost:8000/api/v1/hello/greet?name=John"

# Health check
curl http://localhost:8000/api/v1/hello/health
```

## Architecture

This project follows a clean architecture pattern:

- **server.py**: Main application entry point and FastAPI app configuration
- **routers/**: Contains API route definitions and request/response handling
- **controllers/**: Contains business logic and data processing
- **run.py**: Development server startup script
