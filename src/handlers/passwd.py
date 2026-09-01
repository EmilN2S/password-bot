import os, random, string
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

def passwd(pass_length):
    length = pass_length
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))
    return ''.join(random.choice(chars) for i in range(length))


@router.message(Command("pass"))
async def pass_handler(message: Message):
    try:
        length = int(message.text.split()[1])

        password = passwd(length)

        await message.answer(f"Your password: {password}")

    except (IndexError, ValueError):
        await message.answer("Try: /pass 10")