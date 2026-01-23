from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards import main_keyboard, help_kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Choose your gender", reply_markup=main_keyboard)


@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Start bot - /start \nshow this menu - /help", reply_markup=help_kb)


@router.message()
async def echo(message: Message):
    await message.answer(message.text)