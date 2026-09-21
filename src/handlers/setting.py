from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from database.db import get_setting, set_setting

router = Router()


class SettingStates(StatesGroup):
    waiting_for_length = State()


@router.message(Command("settings"))
async def settings_handler(message: Message, state: FSMContext):
    current = await get_setting(message.from_user.id)
    await message.answer(
        f"Current password length: <b>{current}</b>\n\nSend a new length (1–128):",
        parse_mode="HTML",
    )
    await state.set_state(SettingStates.waiting_for_length)


@router.message(SettingStates.waiting_for_length, F.text)
async def receive_length(message: Message, state: FSMContext):
    await state.clear()

    text = message.text.strip()
    if not text.isdigit() or not (1 <= int(text) <= 128):
        await message.answer("❌ Please send a whole number between 1 and 128.")
        return

    length = int(text)
    await set_setting(message.from_user.id, length)
    await message.answer(f"✅ Password length set to <b>{length}</b>.", parse_mode="HTML")
