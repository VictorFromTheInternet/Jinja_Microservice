"""
Hello World Controller
Contains the business logic for hello world operations
"""
from typing import Dict, Any


class HelloController:
    """Controller for handling hello world operations"""
    
    @staticmethod
    async def get_hello_world() -> Dict[str, Any]:
        """
        Returns a simple hello world message
        
        Returns:
            Dict containing hello world message and metadata
        """
        return {
            "message": "Hello, World!",
            "service": "Hello World Microservice",
            "status": "success",
            "data": {
                "greeting": "Welcome to FastAPI with routers and controllers!",
                "version": "1.0.0"
            }
        }
    
    @staticmethod
    async def get_hello_with_name(name: str) -> Dict[str, Any]:
        """
        Returns a personalized hello message
        
        Args:
            name: The name to include in the greeting
            
        Returns:
            Dict containing personalized hello message
        """
        return {
            "message": f"Hello, {name}!",
            "service": "Hello World Microservice",
            "status": "success",
            "data": {
                "greeting": f"Welcome {name} to FastAPI with routers and controllers!",
                "personalized": True
            }
        }
    
    @staticmethod
    async def get_health_check() -> Dict[str, Any]:
        """
        Returns health check information
        
        Returns:
            Dict containing health status
        """
        return {
            "status": "healthy",
            "service": "Hello World Microservice",
            "message": "Service is running properly"
        }
