import os
from dotenv import load_dotenv 
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    app_name: str = "Backend LLM API and DB"
    db_server: str = os.getenv("DB_SERVER")
    db_hostname: str = os.getenv("DB_HOSTNAME")
    db_database: str = os.getenv("DB_DATABASE")
    db_username: str = os.getenv("DB_USERNAME")
    db_password: str = os.getenv("DB_PASSWORD")
    db_port: int = int(os.getenv("DB_PORT", "3306"))
    db_sslmode: bool = os.getenv("DB_SSLMODE", "True").lower() == "true"

    HF_API_KEY: str = os.getenv("HF_API_KEY")
    HF_API_URI: str = "https://router.huggingface.co/v1/chat/completions"

    # validate
    def validate(self):
        if not self.HF_API_KEY:
            raise ValueError("HF_API_KEY environment variable is not set")

settings = Settings()
settings.validate()
