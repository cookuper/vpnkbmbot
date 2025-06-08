from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

join_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Участвую")]
    ],
    resize_keyboard=True
)

user_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Список участников")]
    ],
    resize_keyboard=True
)

admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Завершить регистрацию")]
    ],
    resize_keyboard=True
)
