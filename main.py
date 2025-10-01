from fastapi import FastAPI
from app.routers import jinja_router

# Create FastAPI instance
app = FastAPI(
    title="Jinja Templating Microservice",
    description="FastAPI microservice for HTML templating and creating PDF documents",
    version="1.0.0"
)

# Include routers
app.include_router(jinja_router.router, prefix="/api/v1")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World Microservice is running!", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)