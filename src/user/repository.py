from dataclasses import dataclass
from sqlalchemy import select
from src.bot.models import SubscriberModel
from src.settings.database import async_session


@dataclass
class UserRepository:
    """Репозиторий пользователей"""

    @staticmethod
    async def get_all_users() -> SubscriberModel:
        """Получение всех пользователей"""
        async with async_session() as session:
            users = await session.execute(select(SubscriberModel))
        return users.scalars().all()

    @staticmethod
    async def get_user_by_telegram(telegram_id: int) -> SubscriberModel:
        """Поиск пользователя по id чата"""
        async with async_session() as session:
            user = await session.execute(select(SubscriberModel).where(SubscriberModel.telegram == telegram_id))
        return user.scalar()

    @staticmethod
    async def add_user(user: SubscriberModel) -> str:
        """Добавление пользователя"""
        async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return "success"
