import asyncio
from os import getenv
from pprint import pprint

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
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
    entry_maybe = (message.text).split(maxsplit=1)
    if len(entry_maybe) == 0:
        return await message.answer(f"I'm a bot that echos: you sent nothing.")
    await message.answer(f"I'm a bot that echos: «{entry_maybe[1]}».")

@dp.message(F.text == "ping")
async def ping(message: Message):
    await message.answer("pong!")

@dp.message(F.photo)
async def get_photo(message: Message):
    orig_photo = message.photo[-1]
    pprint(orig_photo, indent=4)
    async def _():
        await message.answer_photo(photo=orig_photo.file_id, caption="Photo.")
    async def __():
        await message.answer("Photo.")
    await asyncio.gather(_(), __())

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        print(e)
        exit(0)