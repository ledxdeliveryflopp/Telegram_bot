from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from src.settings.settings import settings


engine = create_async_engine(url=settings.database_settings.get_full_db, echo=False)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

base = declarative_base()

