from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "JaliscoMunicipalFireRiskAgent"
    environment: str = "development"
    database_url: str = "postgresql://postgres:postgres@localhost:5432/jalisco_fire_db"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()