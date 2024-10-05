import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from routers import router as main_router

async def main():
    dp = Dispatcher()
    dp.include_router(main_router)

    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(
        #Токен бота
        token=os.getenv('TOKEN'),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML,
    ))

    await dp.start_polling(bot)

#Запуск бота
if __name__ == "__main__":
    asyncio.run(main())