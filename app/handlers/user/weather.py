from aiogram import Bot
from aiogram.types import Message
import requests
from app import dp
from app.common import FMT

@dp.message(commands=['weather','wttr'])
async def weather(message: Message, f: FMT, bot: Bot):
    commaarg = message.get_args()
    weather1 = requests.get(f"https://wttr.in/{commaarg}?format=3")
    weather_reply = weather1.text
    await bot.send_message(text=f"{weather_reply}", chat_id=message.from_user.id)