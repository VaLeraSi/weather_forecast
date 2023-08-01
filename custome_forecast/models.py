from pydantic import BaseModel


class WeatherResponse(BaseModel):
    coord: dict
    weather: list
    base: str
    main: dict
    visibility: int
    wind: dict
    clouds: dict
    dt: int
    sys: dict
    timezone: int
    id: int
    name: str
    cod: int



