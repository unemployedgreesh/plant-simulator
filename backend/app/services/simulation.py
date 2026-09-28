from app.schemas.plant import PlantBase
from app.schemas.weather import WeatherData


def simulate_day(plant: PlantBase, weather: WeatherData) -> PlantBase:
    water_loss = 10 
    if weather.temperature >= 90:
        water_loss += 10
    if weather.humidity < 40: 
        water_loss += 5
    if weather.precipitation > 0:
        water_loss -= 5
    new_water_level = max(
        0, min(100, plant.water_level - water_loss)
    )
    plant.water_level = new_water_level
    return plant