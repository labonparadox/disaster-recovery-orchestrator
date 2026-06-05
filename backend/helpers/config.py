from pydantic_settings import BaseSettings
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent


class data(BaseSettings):

    Log_file_terraform: str
    Log_file_login: str
    Log_file_signup: str


    class Config:

        env_file = PROJECT_ROOT / ".env"

settings = data()