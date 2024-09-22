import logging
from pydantic_settings import BaseSettings, SettingsConfigDict


logger = logging.getLogger("Application Logs")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger.handlers[0].setFormatter(formatter)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, env_file_encoding="utf-8"
    )

    DATABASE_URI: str = "sqlite:///iot-app.db"
    JWT_SECRET: str


base_settings = Settings()
