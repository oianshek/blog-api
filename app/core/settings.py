from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = ""
    PROJECT_DESCRIPTION: str = ""
    PROJECT_VERSION: str = ""

    DATABASE_PORT: int = 0
    POSTGRES_PASSWORD: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_DB: str = ""
    POSTGRES_HOST: str = ""

    JWT_SECRET_KEY: str = "8dfe3e18b7237f7cf9b8ba9bf6853a96722ec8dbe6f763159e4dc9c0b4801fae"
    JWT_ENCODE_ALGORITHM: str = "HS256"
    REFRESH_TOKEN_EXPIRES_IN: int = 0
    ACCESS_TOKEN_EXPIRES_IN: int = 0

    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_SECRET_KEY: str = ""
    GOOGLE_REDIRECT_URI: str = ""
    GOOGLE_TOKEN_URL: str = ""

    @property
    def db_url(self):
        return (f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.DATABASE_PORT}/{self.POSTGRES_DB}")


settings = Settings()
