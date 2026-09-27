from aiogram.fsm.state import State, StatesGroup

class SettingStates(StatesGroup):
    waiting_for_length = State()

