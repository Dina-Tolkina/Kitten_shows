from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    MODELS: list = ["models.permission_model", "models.user_model", "models.breed_model", "models.kitten_model", "models.rating_model", "aerich.models"]
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()