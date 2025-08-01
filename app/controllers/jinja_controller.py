"""
Jinja Template Controller
Contains the business logic for Jinja template rendering operations
"""
from typing import Dict, Any
from jinja2 import Template, TemplateError
import json


class JinjaController:
    """Controller for handling Jinja template rendering operations"""
    
    @staticmethod
    async def render_template(template_string: str, context_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Renders a Jinja template with provided context data
        
        Args:
            template_string: The Jinja template as a string
            context_data: Dictionary containing variables for template rendering
            
        Returns:
            Dict containing rendered HTML and metadata
        """
        try:
            # Create Jinja template
            template = Template(template_string)
            
            # Render template with context data
            rendered_html = template.render(context_data)
            
            return {
                "status": "success",
                "message": "Template rendered successfully",
                "data": {
                    "rendered_html": rendered_html,
                    "template_variables": list(context_data.keys()),
                    "template_length": len(template_string),
                    "output_length": len(rendered_html)
                }
            }
            
        except TemplateError as e:
            return {
                "status": "error",
                "message": f"Template rendering error: {str(e)}",
                "data": {
                    "error_type": "template_error",
                    "template_string": template_string,
                    "context_data": context_data
                }
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Unexpected error: {str(e)}",
                "data": {
                    "error_type": "general_error"
                }
            }
    
    @staticmethod
    async def get_sample_template() -> Dict[str, Any]:
        """
        Returns a sample HTML template with Hello World content
        
        Returns:
            Dict containing sample template and context data
        """
        sample_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title | default('Hello World') }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .message {
            font-size: 18px;
            text-align: center;
            margin: 20px 0;
        }
        .info {
            background-color: #e7f3ff;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ heading | default('Hello, World!') }}</h1>
        <div class="message">
            <p>Welcome {{ name | default('Guest') }}!</p>
            <p>{{ message | default('This is a Jinja template rendered by FastAPI.') }}</p>
        </div>
        {% if show_info %}
        <div class="info">
            <h3>Template Information:</h3>
            <ul>
                <li>Service: {{ service_name | default('Jinja Microservice') }}</li>
                <li>Version: {{ version | default('1.0.0') }}</li>
                <li>Rendered at: {{ timestamp | default('N/A') }}</li>
            </ul>
        </div>
        {% endif %}
        {% if items %}
        <div class="info">
            <h3>Items:</h3>
            <ul>
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
            </ul>
        </div>
        {% endif %}
    </div>
</body>
</html>"""

        sample_context = {
            "title": "Jinja Template Demo",
            "heading": "Hello from Jinja!",
            "name": "FastAPI User",
            "message": "This HTML was generated using Jinja2 templating engine.",
            "show_info": True,
            "service_name": "Jinja Microservice",
            "version": "1.0.0",
            "timestamp": "2025-08-01",
            "items": ["FastAPI", "Jinja2", "Python", "Templates"]
        }
        
        return {
            "status": "success",
            "message": "Sample template retrieved successfully",
            "data": {
                "template": sample_template,
                "sample_context": sample_context,
                "description": "A complete HTML document with Jinja template variables"
            }
        }
    
    @staticmethod
    async def validate_template(template_string: str) -> Dict[str, Any]:
        """
        Validates a Jinja template without rendering it
        
        Args:
            template_string: The Jinja template string to validate
            
        Returns:
            Dict containing validation results
        """
        try:
            # Try to parse the template
            template = Template(template_string)
            
            # Extract variables from template
            from jinja2.meta import find_undeclared_variables
            parsed_content = template.environment.parse(template_string)
            variables = find_undeclared_variables(parsed_content)
            
            return {
                "status": "success",
                "message": "Template is valid",
                "data": {
                    "is_valid": True,
                    "variables_found": list(variables),
                    "variable_count": len(variables),
                    "template_length": len(template_string)
                }
            }
            
        except TemplateError as e:
            return {
                "status": "error",
                "message": f"Template validation failed: {str(e)}",
                "data": {
                    "is_valid": False,
                    "error_type": "template_error",
                    "error_details": str(e)
                }
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Validation error: {str(e)}",
                "data": {
                    "is_valid": False,
                    "error_type": "general_error"
                }
            }
