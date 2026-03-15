import asyncio
from os import getenv

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from iscromodules.routes import router

load_dotenv(dotenv_path=".env")
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print(e)
        exit(0)