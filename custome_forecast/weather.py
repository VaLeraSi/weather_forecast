import argparse

from weather_from_api import WeatherFromAPI
from config import MySettings, db_config


def main():
    parser = argparse.ArgumentParser(description='Get weather information for a city')
    parser.add_argument('city', type=str, help='Name of the city')
    args = parser.parse_args()

    city = args.city
    weather_from_api = WeatherFromAPI(app_id=MySettings().app_id, db_settings=db_config)
    weather_data = weather_from_api.main_weather_data(city)

    return weather_data


if __name__ == "__main__":
    new_data = main()
    print(*new_data)

