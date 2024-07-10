from aiogram.fsm.state import StatesGroup, State


class StateData(StatesGroup):
    """Данные о состояниях"""
    message_text = State()
