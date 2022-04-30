from aiogram import Bot
from aiogram.types import Message

from app import dp
from app.common import FMT

@dp.message(commands=['хелп','помощь','help'])
async def cmd_help(message: Message, f: FMT, bot: Bot):
    await bot.send_message(text='Привет! Как я вижу ты запросил помощи в командах. Обязательные аргументы {}, '
                                'не обязательные [].\n Погода /wttr,/weather {город}. Данная команда может работать '
                                'медленно/не работать вообще из за API\n О создателе /bio.\n Roadmap: '
                                '/roadmap\n Картинка погоды /picweather {город или место}', chat_id=message.from_user.id)