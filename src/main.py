from os import getenv
from dotenv import load_dotenv
import asyncio

from handlers.start import router as start_router
from handlers.passwd import router as passwd_router
from handlers.help import router as help_router
from handlers.setting import router as setting_router

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from database.db import init_db

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher(storage=MemoryStorage())
dp.include_router(start_router)
dp.include_router(passwd_router)
dp.include_router(help_router)
dp.include_router(setting_router)

async def main():
    await init_db()
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())