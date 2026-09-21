import os, random, string
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from database.db import get_setting

router = Router()


def passwd(pass_length: int) -> str:
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed(os.urandom(1024))
    return ''.join(random.choice(chars) for _ in range(pass_length))


@router.message(Command("pass"))
async def pass_handler(message: Message):
    length = await get_setting(message.from_user.id)
    password = passwd(length)
    await message.answer(f"Your password: <code>{password}</code>", parse_mode="HTML")
