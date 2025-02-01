from pydantic_settings import BaseSettings
from pydantic import BaseModel
from functools import lru_cache

class Settings(BaseSettings):
    ALGORITHM: str = "RS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./test.db"
    
    # Path to RSA keys
    PRIVATE_KEY_PATH: str = "private_key.pem"
    PUBLIC_KEY_PATH: str = "public_key.pem"

    @property
    def PRIVATE_KEY(self) -> str:
        with open(self.PRIVATE_KEY_PATH, 'r') as f:
            return f.read()

    @property
    def PUBLIC_KEY(self) -> str:
        with open(self.PUBLIC_KEY_PATH, 'r') as f:
            return f.read()

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
