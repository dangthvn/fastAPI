
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str  # -> DATABASE_HOST
    database_port: str      # -> DATABASE_PORT
    database_name: str      # -> DATABASE_NAME
    database_username: str  # -> DATABASE_USER
    database_password: str  # -> DATABASE_PASSWORD
    secret_key: str         # -> SECRET_KEY
    algorithm: str          # -> ALGORITHM
    access_token_expire_minutes: int  # -> ACCESS_TOKEN_EXPIRE_MINUTES

    class Config:
        env_file = ".env"
        env_prefix = ""  # Không thêm tiền tố nào vào biến môi trường

settings = Settings()
