from fastapi import FastAPI
from random import randint, choice

app = FastAPI()

# Sample weather conditions for simulation
weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]

@app.get("/forecast/{city_name}")
async def get_weather_forecast(city_name: str):
    """Get a 3-day weather forecast for a specific city."""
    forecast_data = []
    days = ["Day 1", "Day 2", "Day 3"]

    for day in days:
        # Generate random weather data
        forecast = {
            "day": day,
            "temperature_c": randint(-5, 35),
            "condition": choice(weather_conditions)
        }
        forecast_data.append(forecast)

    return {"city": city_name, "forecasts": forecast_data}

