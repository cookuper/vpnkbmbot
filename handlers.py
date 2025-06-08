from aiogram.types import Message
from aiogram import Bot
from keyboards import join_kb, user_kb, admin_kb
from db import add_user, user_exists, get_masked_users, get_all_users
from config import ADMIN_ID

async def start_handler(message: Message, bot: Bot):
   await message.answer(
    "Привет! Этот бот создан для участников предварительной акции перед запуском VPN-сервиса KBM VPN.\n\n"
    "Нажми кнопку ниже, чтобы принять участие и получить шанс:\n"
    "• Бесплатную подписку на 1 месяц\n"
    "• Промокод со скидкой 50% на годовой тариф\n"
    "• Или другие бонусы при старте продаж\n\n"
    "Чем раньше зарегистрируешься — тем больше шансов. Удачи!",
    reply_markup=join_kb
)

async def join_handler(message: Message, bot: Bot):
    user_id = message.from_user.id
    username = message.from_user.username
    if not user_exists(user_id):
        add_user(user_id, username)
        await message.answer("Вы зарегистрированы.", reply_markup=user_kb)
    else:
        await message.answer("Вы уже участвуете.", reply_markup=user_kb)

async def list_handler(message: Message, bot: Bot):
    masked_users = get_masked_users()
    if not masked_users:
        await message.answer("Пока что нет участников.")
    else:
        response = "Список участников:\n\n" + "\n".join(masked_users)
        await message.answer(response)

async def admin_handler(message: Message, bot: Bot):
    if message.from_user.id != ADMIN_ID:
        await message.answer("Доступ запрещён.")
        return

    all_users = get_all_users()
    if not all_users:
        await message.answer("Нет зарегистрированных участников.")
    else:
        response = "Регистрация завершена.\n\nСписок ID участников:\n" + "\n".join(all_users)
        await message.answer(response, reply_markup=admin_kb)
