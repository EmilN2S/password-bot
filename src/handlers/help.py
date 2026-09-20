from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.main import main_keyboard

router = Router()

@router.message(Command("help"))
@router.message(F.text.lower() == "help")
async def help_handler(message: Message):
    await message.answer("Write /start to begin again\n",
                         "Write /pass *number* for password\n"
                         "Write /settings for settings\n"
                         "Write /help for help", 
                         parse_mode="Markdown", reply_markup=main_keyboard())