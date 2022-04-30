from aiogram import Bot
from aiogram.types import Message

from app import dp
from app.common import FMT

@dp.message(commands=['roadmap'])
async def cmd_roadmap(message: Message, f: FMT, bot: Bot):
    await bot.send_message(text='Roadmap 2022\n Добавить больше интересных команд\n Сделать инлайн погоду.\n Свои '
                                'идеи в https://github.com/HueRtx/tgbot/issues', chat_id=message.from_user.id)
