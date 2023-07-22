from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,InlineKeyboardMarkup, ReplyKeyboardRemove


remove_btn = ReplyKeyboardRemove()

async def get_user_phone_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(
        KeyboardButton("Telefon raqamim", request_contact=True)
    )
    return btn


async def get_all_info_btn():
    btn = InlineKeyboardMarkup()
    btn.add(
        InlineKeyboardButton("Barcha o`quvchilar", callback_data="all_students")
    )
    return btn