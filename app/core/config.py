import os
from pydantic_settings import BaseSettings,SettingsConfigDict
from typing import ClassVar

class Setting(BaseSettings):
    
    DATABASE_URL:str
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    
setting = Setting()