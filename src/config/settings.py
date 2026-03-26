from pydantic import computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    # GraphDB
    GRAPHDB_HOST: str
    GRAPHDB_PORT: int
    GRAPHDB_REPO_NAME: str
    GRAPHDB_REPO_URL: str

    # GRIP DB
    GRIP_DB_HOST: str
    GRIP_DB_PORT: int
    GRIP_DB_NAME: str
    GRIP_DB_USER: str
    GRIP_DB_PASSWORD: str

    # VCMS DB
    VCMS_DB_HOST: str
    VCMS_DB_PORT: int
    VCMS_DB_NAME: str
    VCMS_DB_USER: str
    VCMS_DB_PASSWORD: str
    VCMS_DB_SSL: bool = False

    @computed_field
    @property
    def GRIP_DB_URL(self) -> str:
        return (
            f"postgresql+psycopg://{self.GRIP_DB_USER}:{self.GRIP_DB_PASSWORD}"
            f"@{self.GRIP_DB_HOST}:{self.GRIP_DB_PORT}/{self.GRIP_DB_NAME}"
        )

    @computed_field
    @property
    def VCMS_DB_URL(self) -> str:
        return (
            f"postgresql+psycopg://{self.VCMS_DB_USER}:{self.VCMS_DB_PASSWORD}"
            f"@{self.VCMS_DB_HOST}:{self.VCMS_DB_PORT}/{self.VCMS_DB_NAME}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
