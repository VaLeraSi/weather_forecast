from pydantic import Field, validators, BaseSettings


class MySettings(BaseSettings):
    app_id: str = Field("app_key", env="API_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
