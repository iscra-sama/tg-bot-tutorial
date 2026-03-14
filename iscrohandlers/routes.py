from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer("Hello, Iscra-chan.")

@router.message(Command('iscroecho'))
async def iscroecho(message: Message):
    print(message.text)
    return await message.answer(f"Ви напейсали: «dbg».")