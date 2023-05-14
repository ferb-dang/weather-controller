from typing import Optional
from pydantic import BaseSettings

class settings(BaseSettings):
    

    class Config:
        case_sensitive = True
        env = ".env"