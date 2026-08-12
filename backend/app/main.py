from fastapi import FastAPI

app = FastAPI(
    title="Plant Simulator API",
    description="Backend API for the AI-powered weather-aware plant simulator.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Plant Simulator API is running",
        "status": "healthy",
    }
