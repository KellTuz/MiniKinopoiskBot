import logging
import asyncio

from config_data.config import settings
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from handlers import router as main_router


async def main():
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode="HTML"),
    )

    dp = Dispatcher()

    logging.basicConfig(level=logging.INFO)

    dp.include_routers(main_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
