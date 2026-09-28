from fastapi import FastAPI

# now adding more imports to make more endpoints
from app.services.weather import get_current_weather
#adding imports for both simulation service and simulation pydantic schema 
from app.services.simulation import simulate_day
from app.schemas.simulation import SimulationRequest


app = FastAPI(
    title="Plant Simulator API",
    description="Backend API for the AI-powered weather-aware plant simulator.",
    version="0.1.0",
)
#this creates backend application 

@app.get("/") #when somebody sends a get request to /, run the function below
def root():
    return {
        "message": "Plant Simulator API is running",
        "status": "healthy",
    }
#FastAPI automatically converts that into JSON for the frontend

#now adding the endpoint for weather service

@app.get("/weather")
def get_weather(latitude: float, longitude: float):
    weather = get_current_weather(latitude, longitude)
    return weather

#now creating a get request endpoint for simulation
#but i have already ctreated a pydantic schema
@app.post("/simulate")
def simulate_plant(request: SimulationRequest):
    #whatever sent to /simulate must to follow SimulationRequest schema
    weather = get_current_weather(
        request.latitude,
        request.longitude
    )
    updated_plant = simulate_day(
        request.plant,
        weather
    )

    return updated_plant
#I used POST instead of GET, because this time 
#the client is sending a structured body of data to the backend for processing

