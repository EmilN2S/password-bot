from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

length = 10

@router.message(Command("settings"))
@router.message(F.text.lower() == "settings")
async def settings_handler(message: Message):
    await message.answer(f"Write length for password, current is: {length}")

