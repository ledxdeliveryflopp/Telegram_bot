from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from src.settings.settings import settings


dispatcher = Dispatcher(storage=MemoryStorage())

bot = Bot(token=settings.bot_settings.bot_token,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))
