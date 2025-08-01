"""
Hello World Router
Defines the API endpoints and routes them to the appropriate controller
"""
from fastapi import APIRouter, Query
from app.controllers.hello_controller import HelloController

# Create router instance
router = APIRouter(
    prefix="/hello",
    tags=["Hello World"],
    responses={404: {"description": "Not found"}},
)

# Initialize controller
hello_controller = HelloController()


@router.get("/")
async def get_hello_world():
    """
    Get a simple hello world message
    
    Returns:
        JSON response with hello world message
    """
    return await hello_controller.get_hello_world()


@router.get("/greet/{name}")
async def get_hello_with_name(name: str):
    """
    Get a personalized hello message
    
    Args:
        name: The name to include in the greeting
        
    Returns:
        JSON response with personalized hello message
    """
    return await hello_controller.get_hello_with_name(name)


@router.get("/greet")
async def get_hello_with_query_name(
    name: str = Query(..., description="Name for personalized greeting")
):
    """
    Get a personalized hello message using query parameter
    
    Args:
        name: The name to include in the greeting (query parameter)
        
    Returns:
        JSON response with personalized hello message
    """
    return await hello_controller.get_hello_with_name(name)


@router.get("/health")
async def health_check():
    """
    Health check endpoint
    
    Returns:
        JSON response with health status
    """
    return await hello_controller.get_health_check()
