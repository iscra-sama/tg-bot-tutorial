import asyncio
from os import getenv

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

load_dotenv(dotenv_path=".env")
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("I am born.")

@dp.message(Command("iscroecho"))
async def echo(message: Message):
    entries = (message.text).split(maxsplit=1)
    if len(entries) == 0:
        return await message.answer(f"I'm a bot that echos: you sent nothing.")
    await message.answer(f"I'm a bot that echos: «{entries[1]}».")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print(e)
        exit(0)