from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Generate Password")],
            [KeyboardButton(text="Settings")],
            [KeyboardButton(text="Help")],
        ],
        resize_keyboard=True,
    )
    return keyboard