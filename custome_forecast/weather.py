import argparse

from weather_from_api import WeatherFromAPI


def main():
    parser = argparse.ArgumentParser(description='Get weather information for a city')
    parser.add_argument('city', type=str, help='Name of the city')
    args = parser.parse_args()

    city = args.city
    weather_api = WeatherFromAPI(city)
    weather_data = weather_api.get_weather_from_db()

    return weather_data


if __name__ == "__main__":
    print(*main())

