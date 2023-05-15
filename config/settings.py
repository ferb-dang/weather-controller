from typing import Optional
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    LATITUDE : float
    LONGITUDE : float
    OPENWEATHER_API_KEY : str

    class Config:
        case_sensitive = True
        env = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()