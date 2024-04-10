from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    sqlalchemy_database_url: str
    sqlalchemy_database_test: str = "sqlite://"
    app_name: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
