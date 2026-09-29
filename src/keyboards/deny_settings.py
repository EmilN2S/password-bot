from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def deny_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Cancel", callback_data="cancel")],
        ],
    )
    return keyboard