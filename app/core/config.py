from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str = (
        "postgresql://shopsphere_admin:"
        "shopsphere_password@localhost:5432/shopsphere"
    )

    class Config:
        env_file = ".env"


settings = Settings()