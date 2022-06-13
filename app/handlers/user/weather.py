from aiogram import Bot
from aiogram.types import Message
import requests
from app import dp
from app.common import FMT
from aiogram.dispatcher.filters import Command, CommandObject


@dp.message(commands=['weather','wttr'])
async def weather(message: Message, f: FMT, bot: Bot, command: CommandObject):
    if comamand.args == None:
        await bot.send_message(text="Укажите аргументы (город)")
    else: 
        weather1 = requests.get(f"https://wttr.in/{command.args}?format=3")
        weather_reply = weather1.text
        await bot.send_message(text=f"{weather_reply}", chat_id=message.from_user.id)
@dp.message(commands=['picweather'])
async def picweather(message: Message, f: FMT, bot: Bot, command: CommandObject):
    #weather1 = requests.get(f"https://wttr.in/{command.args}.png?format=3")
    #weather_reply = weather1.raw
    if command.args == None:
        await bot.send_message(text="Укажите аргументы (город)")
    else:
        await bot.send_message(text=f'Погода[ ](https://wttr.in/{command.args}.png)в {command.args}', parse_mode="MarkdownV2", chat_id=message.from_user.id)
