from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from function import functions

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Приветствую я бот погоды.')


@router.message(Command('/help'))
async def process_help_command(message: Message):
    await message.answer(text='Вам всеголищь необходимо ввести город')


@router.message()
async def process_start_weather(message: Message):
    city: str = message.text
    weather_life = functions.weather(city)

    await message.answer(weather_life)
