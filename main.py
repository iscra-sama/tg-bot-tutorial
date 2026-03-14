from os import getenv
from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher

from iscrohandlers.routes import router

load_dotenv()
BOT_TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()
dp.include_router(router)

async def main():
    bot = Bot(token=BOT_TOKEN)
    print("Bot started")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())