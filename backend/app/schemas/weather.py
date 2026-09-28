from pydantic import BaseModel, Field

class WeatherData(BaseModel):
    temperature: float
    humidity: int = Field(ge = 0, le= 100)
    precipitation: float = Field(ge = 0)

  #WeatherData describes what does weather look like in my application
    