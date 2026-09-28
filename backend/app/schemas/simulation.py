from pydantic import BaseModel

from app.schemas.plant import PlantBase

class SimulationRequest(BaseModel):
    plant: PlantBase    #I am putting one pydantic model inside another pydantic model
    latitude: float
    longitude: float

#SimulationRequest describes what info must someone give to my APi
#if they want to simulate a plant
#this is why we create schemas
