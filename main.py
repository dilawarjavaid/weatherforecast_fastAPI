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

@app.get("/forecast/{city_name}/{day}")
async def get_specific_day_forecast(city_name: str, day: int):
    """Get the forecast for a specific day in the 3-day range."""
    if day < 1 or day > 3:
        return {"error": "Invalid day. Please choose between 1 and 3."}

    forecast = {
        "day": f"Day {day}",
        "temperature_c": randint(-5, 35),
        "condition": choice(weather_conditions)
    }

    return {"city": city_name, "forecast": forecast}

