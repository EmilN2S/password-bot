from os import getenv
from dotenv import load_dotenv
import asyncio
from passwd import passwd

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Hi, your password: {passwd(15)}")


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())