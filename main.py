import asyncio
import logging
from src.bot.service import init_bot

if __name__ == "__main__":
    logging.basicConfig(filename='bot.log', level=logging.INFO)
    asyncio.run(init_bot())
