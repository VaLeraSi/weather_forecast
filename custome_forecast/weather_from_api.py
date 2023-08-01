import requests
import psycopg2
from time import sleep

from config import MySettings, db_config
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


class WeatherFromAPI:
    def __init__(self, app_id: str, db_settings: dict):
        self.app_id = app_id
        self.cursor = self.db_cursor(db_settings)
        self.conn = self.db_conn(db_settings)

    def db_conn(self, db_settings: dict):
        conn = psycopg2.connect(**db_settings)

        return conn

    def db_cursor(self, db_settings: dict):

        conn = psycopg2.connect(**db_settings)

        return conn.cursor()

    def _get_weather_from_db(self, city: str):
        sql = "SELECT temperature, description FROM weather WHERE city = %s"

        try:
            self.cursor.execute(sql, (city,))
            data = self.cursor.fetchone()

            if data is not None:
                return data

        except (Exception, psycopg2.Error) as error:
            print(error)

    @retry
    def _get_weather_from_api(self, city: str, lang: str = "en"):

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.app_id}&lang={lang}"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data

    def _save_weather_data(self, data) -> WeatherResponse:

        sql = "INSERT INTO weather (city, temperature, description) VALUES (%s, %s, %s)"

        try:
            self.city = data['name']
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            self.cursor.execute(sql, (city, temperature, description))
            self.conn.commit()

        except (Exception, psycopg2.Error) as error:
            print(error)

        weather_response = WeatherResponse(**data)
        return weather_response

    def main_weather_data(self, city: str):
        weather_data = self._get_weather_from_db(city)

        if weather_data is None:
            weather_data = self._get_weather_from_api(city)
            self._save_weather_data(weather_data)
            weather_data = self._get_weather_from_db(city)
        return weather_data


if __name__ == "__main__":
    city = str(input("Your city: "))
    weather_api = WeatherFromAPI(app_id=MySettings().app_id, db_settings=db_config)
    print(weather_api.main_weather_data(city=city))
