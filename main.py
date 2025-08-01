from fastapi import FastAPI
from app.routers import hello_router, jinja_router

# Create FastAPI instance
app = FastAPI(
    title="Hello World Microservice",
    description="A simple FastAPI microservice with routers and controllers",
    version="1.0.0"
)

# Include routers
app.include_router(hello_router.router, prefix="/api/v1")
app.include_router(jinja_router.router, prefix="/api/v1")

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World Microservice is running!", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)