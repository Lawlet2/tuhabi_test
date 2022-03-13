from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Class to set the app settings
    """
    app_name: str = "tuhabiAPI"
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    allowed_statuses: str

    class Config:
        """
        Class to set the env file
        """
        env_file = ".env"


settings = Settings()
