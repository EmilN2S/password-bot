import os, random, string
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from handlers.setting import length

router = Router()

def passwd(pass_length):
    length = pass_length
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))
    return ''.join(random.choice(chars) for i in range(length))


@router.message(Command("pass"))
@router.message(F.text.lower() == "generate password")
async def pass_handler(message: Message):
    
    password = passwd(length)

    await message.answer(f"Your password: {password}")
