import asyncio
from pprint import pprint

from aiogram import F, Router
from aiogram.filters import and_f, Command, CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("I am born.")

@router.message(Command("iscroecho"))
async def echo(message: Message):
    entry_maybe = (message.text).split(maxsplit=1)
    if len(entry_maybe) == 0:
        return await message.answer(f"I'm a bot that echos: you sent nothing.")
    await message.answer(f"I'm a bot that echos: «{entry_maybe[1]}».")

@router.message(F.text == "ping")
async def ping(message: Message):
    await message.answer("pong!")

@router.message(and_f(F.photo, Command("photo")))
async def get_photo(message: Message):
    orig_photo = message.photo[-1]
    pprint(orig_photo, indent=4)
    async def _():
        await message.answer_photo(photo=orig_photo.file_id, caption="Photo.")
    async def __():
        await message.answer("Photo.")
    await asyncio.gather(_(), __())