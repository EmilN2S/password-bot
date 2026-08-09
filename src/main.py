from os import getenv
from dotenv import load_dotenv
import asyncio
from passwd import passwd

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
router = Router()
dp.include_router(router)

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(f"Hi, {message.from_user.first_name}.\nWrite /pass *number* for password", parse_mode="Markdown")

@dp.message(Command("pass"))
async def pass_handler(message: Message):
    try:
        length = int(message.text.split()[1])

        password = passwd(length)

        await message.answer(f"Your password: {password}")

    except (IndexError, ValueError):
        await message.answer("Try: /pass 10")

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())