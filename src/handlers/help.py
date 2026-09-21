from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.main import main_keyboard

router = Router()

HELP_TEXT = (
    "🤖 <b>Password Bot — Help</b>\n"
    "\n"
    "Here's everything you can do:\n"
    "\n"
    "🔑 <b>/pass</b> — Generate a secure password\n"
    "   <i>Also: tap the «Generate Password» button</i>\n"
    "\n"
    "⚙️ <b>/settings</b> — Change your password length (8–128 chars)\n"
    "   <i>Also: tap the «Settings» button</i>\n"
    "\n"
    "🏠 <b>/start</b> — Go back to the main menu\n"
    "\n"
    "❓ <b>/help</b> — Show this message\n"
    "\n"
    "━━━━━━━━━━━━━━━━━━\n"
    "💡 <b>Tip:</b> By default your passwords are generated with the "
    "length you set in <b>/settings</b>. The characters pool includes "
    "uppercase &amp; lowercase letters, digits, and special symbols."
)


@router.message(Command("help"))
@router.message(F.text.lower() == "help")
async def help_handler(message: Message):
    await message.answer(HELP_TEXT, parse_mode="HTML", reply_markup=main_keyboard())