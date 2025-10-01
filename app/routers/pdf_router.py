"""
PDF Template Router
API endpoints for PDF templates
"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional
from app.controllers.pdf_controller import PDFController