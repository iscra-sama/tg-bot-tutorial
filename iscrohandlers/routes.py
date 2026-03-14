from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()
@router.message(Command('start'))
async def hello(message: Message):
    await message.answer("Hello, Iscra-chan.")
@router.message(Command('iscroecho'))
async def hello(message: Message):
    entry = (message.text).find("")
    print(entry)
    await message.answer(f"Ви напейсали: «{entry}».")