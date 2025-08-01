"""
Jinja Template Router
Defines the API endpoints for Jinja template rendering operations
"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional
from app.controllers.jinja_controller import JinjaController


# Pydantic models for request/response
class TemplateRenderRequest(BaseModel):
    template: str
    context: Dict[str, Any]


class TemplateValidateRequest(BaseModel):
    template: str


# Create router instance
router = APIRouter(
    prefix="/template",
    tags=["Jinja Templates"],
    responses={404: {"description": "Not found"}},
)

# Initialize controller
jinja_controller = JinjaController()


@router.post("/render")
async def render_template(request: TemplateRenderRequest):
    """
    Render a Jinja template with provided context data
    
    Args:
        request: TemplateRenderRequest containing template string and context data
        
    Returns:
        JSON response with rendered HTML
    """
    result = await jinja_controller.render_template(
        template_string=request.template,
        context_data=request.context
    )
    
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    
    return result


@router.post("/render-html", response_class=HTMLResponse)
async def render_template_as_html(request: TemplateRenderRequest):
    """
    Render a Jinja template and return raw HTML
    
    Args:
        request: TemplateRenderRequest containing template string and context data
        
    Returns:
        Raw HTML response
    """
    result = await jinja_controller.render_template(
        template_string=request.template,
        context_data=request.context
    )
    
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    
    return result["data"]["rendered_html"]


@router.get("/sample")
async def get_sample_template():
    """
    Get a sample Hello World HTML template with context data
    
    Returns:
        JSON response with sample template and context
    """
    return await jinja_controller.get_sample_template()


@router.get("/sample/render", response_class=HTMLResponse)
async def render_sample_template():
    """
    Render the sample Hello World template and return as HTML
    
    Returns:
        Raw HTML response of rendered sample template
    """
    # Get sample template and context
    sample_data = await jinja_controller.get_sample_template()
    
    # Render the sample template
    result = await jinja_controller.render_template(
        template_string=sample_data["data"]["template"],
        context_data=sample_data["data"]["sample_context"]
    )
    
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail="Failed to render sample template")
    
    return result["data"]["rendered_html"]


@router.post("/validate")
async def validate_template(request: TemplateValidateRequest):
    """
    Validate a Jinja template without rendering it
    
    Args:
        request: TemplateValidateRequest containing template string
        
    Returns:
        JSON response with validation results
    """
    result = await jinja_controller.validate_template(request.template)
    
    if result["status"] == "error" and result["data"]["error_type"] == "template_error":
        raise HTTPException(status_code=400, detail=result["message"])
    
    return result


@router.get("/health")
async def template_health_check():
    """
    Health check endpoint for template service
    
    Returns:
        JSON response with health status
    """
    return {
        "status": "healthy",
        "service": "Jinja Template Service",
        "message": "Template rendering service is operational",
        "features": [
            "Template rendering",
            "Template validation", 
            "Sample templates",
            "HTML response support"
        ]
    }
