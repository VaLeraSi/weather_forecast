import requests
from time import sleep
import json

from config import MySettings
from models import WeatherResponse


def retry(func):
    def wrapper(*args, **kwargs):
        count_retries = 3
        retry_delay = 2

        for i in range(count_retries):
            try:
                return func(*args, **kwargs)
            except Exception:
                print(f"Попытка № {i + 1} не удалась!")
                sleep(retry_delay)

    return wrapper


@retry
def get_weather_from_api(lon: float, lan: float, lang: str = "en",
                         app_id: str = MySettings().app_id) -> WeatherResponse:
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lan}&lon={lon}&appid={app_id}&lang={lang}"

    print(url)

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    weather_response = WeatherResponse(**data)
    return weather_response


def save_weather_data(weather_data: WeatherResponse, file_path: str):
    with open(file_path, "w") as file:
        json.dump(weather_data.dict(), file, indent=4)

