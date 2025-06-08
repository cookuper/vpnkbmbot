import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from config import TOKEN
from handlers import (
    start_handler,
    join_handler,
    list_handler,
    admin_handler
)
from db import init_db

async def main():
    init_db()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Обработка команды /start (правильно для aiogram 3.x)
    dp.message.register(start_handler, Command("start"))

    # Обработка текста кнопок (без стикеров, учтён trim и lower)
    dp.message.register(join_handler, lambda m: m.text and m.text.strip().lower() == "участвую")
    dp.message.register(list_handler, lambda m: m.text and m.text.strip().lower() == "список участников")
    dp.message.register(admin_handler, lambda m: m.text and m.text.strip().lower() == "завершить регистрацию")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
