from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    """Настройки бота"""
    token: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class DatabaseSettings(BaseSettings):
    """Настройки бота"""

    user: str
    password: str
    host: str
    port: str
    name: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def get_full_db(self):
        return f'postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'


class Settings(BaseSettings):

    bot_settings: BotSettings
    database_settings: DatabaseSettings


@lru_cache
def init_settings():
    """Инициализация настроек"""
    return Settings(bot_settings=BotSettings(), database_settings=DatabaseSettings())


settings = init_settings()

