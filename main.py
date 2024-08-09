import logging
import asyncio

from config_data.config import settings
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from handlers import router as main_router


async def main():
    dp = Dispatcher()
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode="HTML"),
    )
    logging.basicConfig(level=logging.INFO)

    # Регистрация основного маршрутизатора
    dp.include_router(main_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
