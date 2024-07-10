from dataclasses import dataclass
from typing import Coroutine
from src.bot.models import SubscriberModel
from src.user.repository import UserRepository


@dataclass
class UserService(UserRepository):
    """Сервис пользователей"""

    async def get_users(self) -> Coroutine:
        """Получение всех пользователей"""
        return await self.get_all_users()

    async def get_user_telegram(self, telegram_id: int) -> Coroutine:
        """Получение пользователя по id чата"""
        return await self.get_user_by_telegram(telegram_id)

    async def add_subscriber(self, user: SubscriberModel) -> Coroutine:
        """Добавление подписчика"""
        return await self.add_user(user)
