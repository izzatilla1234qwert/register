import logging

from aiogram import Bot, Dispatcher, executor, types
from bot_states import UserStates
from aiogram.dispatcher import FSMContext
from bot_database import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot_keyboards import *

logging.basicConfig(level=logging.INFO)


BOT_TOKEN = "6060324128:AAET5AvNCDHu0deiUS6-EI3b6mQfGYHVJLU"

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


async def on_start_my_bot(dp):
    await create_tables()


@dp.message_handler(commands=['start'])
async def start_bot_command(message: types.Message):
    await message.answer("Salom")


@dp.message_handler(commands=['register'])
async def register_bot_command(message: types.Message):
    await message.answer("F.I.O yuboring:")
    await UserStates.fio.set()


@dp.message_handler(state=UserStates.fio, content_types=['text'])
async def get_user_fio_state(message: types.Message, state: FSMContext):
    fio = message.text
    await state.update_data(fio=fio)
    await message.answer("Yoshingizni kiriting:")
    await UserStates.age.set()


@dp.message_handler(state=UserStates.age, content_types=['text'])
async def get_user_age_state(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=int(age))
    btn = await get_user_phone_btn()
    await message.answer("Telefon raqamizni kiriting:", reply_markup=btn)
    await UserStates.phone_number.set()


@dp.message_handler(state=UserStates.phone_number, content_types=['contact'])
async def get_user_phone_state(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    data = await state.get_data()
    await create_student(data['fio'], data['age'], phone_number)
    await state.finish()

    await message.answer("Malumotlar sqlandi", reply_markup=remove_btn)

    btn = await get_all_info_btn()
    await message.answer("Malumotlar", reply_markup=btn)



@dp.callback_query_handler(text='all_students')
async def get_info_callback(call: types.CallbackQuery):
    info = await get_all_students()
    context = ""
    for i in info:
        context += f"ism: {i[0]} \nYosh {i[0]}\n Tel: {i[0]}\n\n"

    await call.message.answer(context)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_start_my_bot)


