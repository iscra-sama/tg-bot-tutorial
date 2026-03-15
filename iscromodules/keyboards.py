from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1")],
        [KeyboardButton(text="2"), KeyboardButton(text="3")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Напишите что-нибудь (^^)"
)
settings_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="1", url="https://youtube.com/@iscra-chan")],
    [InlineKeyboardButton(text="2", url="https://youtube.com/@iscra-chan"), InlineKeyboardButton(text="3", url="https://youtube.com/@iscra-chan")],
])

arr = "i s c r a".split()
def get_arr_keyboard():
    keyboard = InlineKeyboardBuilder()
    for e in arr:
        keyboard.add(InlineKeyboardButton(text=e, url="https://youtube.com/@iscra-chan"))
    return keyboard.adjust(2).as_markup()