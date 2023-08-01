from .settings import PostgresSettings, MySettings

postgres_settings = PostgresSettings()
my_settings = MySettings()

db_config: dict = dict(
    host=postgres_settings.DATABASE_HOST,
    port=postgres_settings.DATABASE_PORT,
    database=postgres_settings.DATABASE_NAME,
    user=postgres_settings.DATABASE_USER,
    password=postgres_settings.DATABASE_PASSWORD
)