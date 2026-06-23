from pydantic_settings import BaseSettings
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).parent.parent


class data(BaseSettings):

    Log_file_terraform: Optional[str] = None
    Log_file_login: Optional[str] = None
    Log_file_signup: Optional[str] = None
    Log_file_deploy: Optional[str] = None
    Log_file_filler: Optional[str] = None
    Endpoint: Optional[str] = None
    db_user: Optional[str] = None
    db_password: Optional[str] = None
    database: Optional[str] = None
    port: Optional[int] = None


    class Config:

        env_file = PROJECT_ROOT / ".env"

settings = data()