from pydantic_settings import BaseSettings  # ⬅️ instead of pydantic

class Settings(BaseSettings):
    database_url: str
    jwt_secret: str
    jwt_algorithm: str
    jwt_expiration: int

    class Config:
        env_file = ".env"

settings = Settings()
