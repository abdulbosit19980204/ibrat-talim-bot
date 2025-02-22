from aiogram.filters.state import State, StatesGroup


class Feedback(StatesGroup):
    body = State()
