from aiogram import types, executor
from dotenv import load_dotenv
import os
from aiogram.dispatcher.dispatcher import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage


config = load_dotenv('.venv')

storage = MemoryStorage()

bot = Bot(token=os.environ.get('BOT_TOKEN'), parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)


if __name__ == "__main__":
    from core.handlers import dp
    from core.adminHandlers import dp
    executor.start_polling(dp)
