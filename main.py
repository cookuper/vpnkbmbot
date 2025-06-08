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

from aiohttp import web  # ← добавим фейковый сервер для Render

async def main():
    init_db()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.message.register(start_handler, Command("start"))
    dp.message.register(join_handler, lambda m: m.text and m.text.strip().lower() == "участвую")
    dp.message.register(list_handler, lambda m: m.text and m.text.strip().lower() == "список участников")
    dp.message.register(admin_handler, lambda m: m.text and m.text.strip().lower() == "завершить регистрацию")

    # ← запускаем aiogram + aiohttp одновременно
    await asyncio.gather(
        dp.start_polling(bot),
        start_web_server()
    )

# ← фейковый сервер, чтобы Render не останавливал процесс
async def start_web_server():
    async def handler(request):
        return web.Response(text="Bot is running")

    app = web.Application()
    app.router.add_get("/", handler)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", 10000)  # порт 10000
    await site.start()

if __name__ == "__main__":
    asyncio.run(main())
