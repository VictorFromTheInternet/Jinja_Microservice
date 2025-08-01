# Hello World FastAPI Microservice

A simple FastAPI microservice demonstrating the use of routers and controllers.

## Project Structure

```
Jinja Microservice/
├── app/
│   ├── __init__.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── hello_controller.py
│   │   └── jinja_controller.py
│   └── routers/
│       ├── __init__.py
│       ├── hello_router.py
│       └── jinja_router.py
├── main.py
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

### Hello World Endpoints:

- **GET /** - Root endpoint with basic info
- **GET /api/v1/hello/** - Simple hello world message
- **GET /api/v1/hello/greet/{name}** - Personalized greeting with path parameter
- **GET /api/v1/hello/greet?name=YourName** - Personalized greeting with query parameter
- **GET /api/v1/hello/health** - Health check endpoint

### Jinja Template Endpoints:

- **POST /api/v1/template/render** - Render a Jinja template with JSON context
- **POST /api/v1/template/render-html** - Render template and return raw HTML
- **GET /api/v1/template/sample** - Get sample Hello World template and context
- **GET /api/v1/template/sample/render** - Render sample template as HTML
- **POST /api/v1/template/validate** - Validate Jinja template syntax
- **GET /api/v1/template/health** - Template service health check

### Interactive API Documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Example Usage

### Hello World Endpoints:
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

### Jinja Template Endpoints:
```bash
# Get sample template
curl http://localhost:8000/api/v1/template/sample

# Render sample template as HTML
curl http://localhost:8000/api/v1/template/sample/render

# Render custom template (POST with JSON)
curl -X POST "http://localhost:8000/api/v1/template/render" \
  -H "Content-Type: application/json" \
  -d '{
    "template": "<h1>Hello {{ name }}!</h1><p>Welcome to {{ place }}.</p>",
    "context": {"name": "World", "place": "FastAPI"}
  }'

# Render template and get raw HTML
curl -X POST "http://localhost:8000/api/v1/template/render-html" \
  -H "Content-Type: application/json" \
  -d '{
    "template": "<!DOCTYPE html><html><body><h1>{{ title }}</h1></body></html>",
    "context": {"title": "My Page"}
  }'

# Validate template syntax
curl -X POST "http://localhost:8000/api/v1/template/validate" \
  -H "Content-Type: application/json" \
  -d '{
    "template": "<h1>{{ title }}</h1>{% if show_content %}<p>{{ content }}</p>{% endif %}"
  }'
```

## Architecture

This project follows a clean architecture pattern:

- **main.py**: Main application entry point and FastAPI app configuration
- **routers/**: Contains API route definitions and request/response handling
  - `hello_router.py`: Hello world endpoints
  - `jinja_router.py`: Jinja template rendering endpoints
- **controllers/**: Contains business logic and data processing
  - `hello_controller.py`: Hello world business logic
  - `jinja_controller.py`: Template rendering and validation logic
- **run.py**: Development server startup script

## Features

### Hello World Service
- Simple greeting endpoints
- Personalized greetings with path/query parameters
- Health check endpoint

### Jinja Template Service
- Render Jinja2 templates with JSON context data
- Return rendered HTML as JSON or raw HTML response
- Template validation without rendering
- Sample Hello World template included
- Template variable extraction and analysis
