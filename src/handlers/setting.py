from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import CallbackQuery

from database.db import get_setting, set_setting

from keyboards.main import main_keyboard
from keyboards.deny_settings import deny_keyboard

from states.pass_length import SettingStates

router = Router()

@router.message(Command("settings"))
@router.message(F.text.lower() == "settings")
async def settings_handler(message: Message, state: FSMContext):
    current = await get_setting(message.from_user.id)
    await message.answer(
        f"Current password length: <b>{current}</b>\n\nSend a new length (8–128):",
        parse_mode="HTML", reply_markup=deny_keyboard()
    )
    await state.set_state(SettingStates.waiting_for_length)


@router.message(SettingStates.waiting_for_length, F.text)
async def receive_length(message: Message, state: FSMContext):
    text = message.text.strip()
    if not text.isdigit() or not (8 <= int(text) <= 128):
        await message.answer("❌ Please send a whole number between 8 and 128.")
        return

    length = int(text)
    await set_setting(message.from_user.id, length)
    await state.clear()
    await message.answer(f"✅ Password length set to <b>{length}</b>.", parse_mode="HTML", reply_markup=main_keyboard())

@router.callback_query(F.data == "cancel")
async def process_task_priority(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer()
    await callback.message.answer("Changed denied")