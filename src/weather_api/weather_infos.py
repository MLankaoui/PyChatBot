import requests
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
api_key = os.getenv('API_KEY_WEATHER')

def display_weather_infos(city_name):
    print(f'So you chose to display the weather infos of {city_name} city.')

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name},ma&appid={api_key}")

    if response.status_code == 404:
        print(f"The city '{city_name}' is not available for the moment!")
        return

    weather = response.json()

    print(f"id: {weather['weather'][0]['id']}")
    print(f"main: {weather['weather'][0]['main']}")
    print(f"description: {weather['weather'][0]['description']}")