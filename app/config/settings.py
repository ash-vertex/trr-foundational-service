from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GRAPHDB_REPO_URL: str = "http://localhost:7200/repositories/grip-vcms-poc"

settings = Settings()