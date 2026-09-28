import requests 
# this import gives python the ability to make an HTTP request to Open-Meteo

from app.schemas.weather import WeatherData
#this imports the weather model already created

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
#stores Open-Meteo's forecast API in one place

def get_current_weather(latitude: float, longitude: float) -> WeatherData:
    params = {"latitude": latitude, 
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m,precipitation",
    "temperature_unit": "fahrenheit",
    }

    response = requests.get(OPEN_METEO_URL, params = params)
    #this is my backend making the API GET request
    response.raise_for_status()
    #means if OPEN METEO responds with an HTTP error such as 400 or 500, we wont continue with bad data
    #consuming a restAPI, parsing its JSON response, and converting external data into my aplications own schema
    data = response.json()
    current = data["current"]

    return WeatherData(
        temperature=current["temperature_2m"],humidity=current["relative_humidity_2m"],precipitation=current["precipitation"],

    )