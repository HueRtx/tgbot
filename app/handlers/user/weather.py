from aiogram import Bot
from aiogram.types import Message
import requests
from app import dp
from app.common import FMT
from aiogram.dispatcher.filters import Command, CommandObject


@dp.message(commands=['weather','wttr'])
async def weather(message: Message, f: FMT, bot: Bot, command: CommandObject):
    weather1 = requests.get(f"https://wttr.in/{command.args}?format=3")
    weather_reply = weather1.text
    await bot.send_message(text=f"{weather_reply}", chat_id=message.from_user.id)