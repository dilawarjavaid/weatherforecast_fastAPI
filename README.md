A simple RESTful API that predicts the weather—with 100% made-up accuracy!
 
Features
3-Day Forecasts: Get fictional weather predictions for any city.

Daily Breakdown: Query specific days (because sometimes you just need to know if it's a "stay in bed" kind of day).

Fast & Lightweight: Built with FastAPI for speedy responses (unlike real weather forecasts).

Setup
Install dependencies:

sh
pip install fastapi uvicorn

Run the API:
uvicorn weather_api:app --reload
(The --reload flag is for auto-updates—because even fake weather deserves fresh data.)

Test it out:

Full forecast:

http
GET /forecast/London  
Specific day (1-3):

http
GET /forecast/London/2  
Expected Responses
3-Day Forecast:

json
{
  "city": "London",
  "forecasts": [
    {"day": 1, "condition": "Rainy", "temperature": 12},
    {"day": 2, "condition": "Cloudy", "temperature": 14},
    {"day": 3, "condition": "Sunny", "temperature": 18}
  ]
}
☀️ Single-Day Forecast:

json
{
  "city": "London",
  "forecast": {"day": 2, "condition": "Cloudy", "temperature": 14}
}
(Disclaimer: Temperatures may be optimistic. Stormy days may or may not involve dragons.)

Why This Exists

Learn FastAPI in a fun way.


Want to Improve It?
PRs welcome! Ideas:

Add more "realistic" fake data (hurricanes? heatwaves?).

Extend to 5-day forecasts (living on the edge).

Integrate memes for certain weather conditions.

Powered by FastAPI, randomness, and a disregard for actual weather patterns.
License: MIT (because even fake weather should be free).
