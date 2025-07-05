# etl/extract.py
import requests
import pandas as pd
from config import CITIES_CSV_PATH

def fetch_weather():
    cities_df = pd.read_csv(CITIES_CSV_PATH)
    weather_data = []

    for _, row in cities_df.iterrows():
        city = row['city']
        lat = row['latitude']
        lon = row['longitude']
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current_weather=true"
        )
        response = requests.get(url)
        json_data = response.json()
        current = json_data["current_weather"]
        current["city"] = city
        weather_data.append(current)

    return weather_data
