from aiogram import Bot
from aiogram.types import Message

from app import dp
from app.common import FMT

@dp.message(commands=['хелп','помощь','help'])
async def cmd_help(message: Message, f: FMT, bot: Bot):
    await bot.send_message(text='Привет! Как я вижу ты запросил помощи в командах. Обязательные аргументы {}, '
                                'не обязательные [].\n Погода /wttr,/weather {}.\n О создателе /bio.\n Roadmap: '
                                '/roadmap', chat_id=message.from_user.id)