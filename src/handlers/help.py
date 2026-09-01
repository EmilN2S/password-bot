from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(f"Write /start to begin\nWrite /pass *number* for password, as example: /pass 10\nWrite /help for help", parse_mode="Markdown")