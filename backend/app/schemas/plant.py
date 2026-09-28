from pydantic import BaseModel, Field

class PlantBase(BaseModel):
    name: str
    species: str
    growth_stage: str = "seedling"


    health: int = Field(default=100, ge = 0, le = 100)
    water_level: int = Field(default=100, ge = 0, le = 100)
    soil_strength: int = Field(default=100, ge = 0, le = 100)
    #sunlight: bool = True 

#plant base describe what a plant look like in my application

