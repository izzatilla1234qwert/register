from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStates(StatesGroup):
    fio = State()
    age = State()
    phone_number = State()
