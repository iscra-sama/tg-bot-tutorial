from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer("Hello, Iscra-chan.")

@router.message(Command('iscroecho'))
async def iscroecho(message: Message):
    entry = (message.text).split(maxsplit=1)[1:]
    if len(entry) == 0:
        return await message.answer(f"Ви напейсали: пустоту.")
    return await message.answer(f"Ви напейсали: «{entry[0]}».")