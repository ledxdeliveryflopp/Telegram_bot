from sqlalchemy import Column, Integer
from src.settings.database import base


class SubscriberModel(base):
    __tablename__ = "subscriber"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True, index=True)
    telegram = Column(Integer, nullable=True, unique=True, index=True)