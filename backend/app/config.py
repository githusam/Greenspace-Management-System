from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class TortoiseSettings(BaseSettings):
    #db_connection: str = os.environ['DATABASE_URL']
    db_connection: str = "sqlite://db.sqlite3"


class APISettings(BaseSettings):
    key: str = "667e86da72414219889ed347f37c8d89"


# Create settings instance
tortoise_settings = TortoiseSettings()

