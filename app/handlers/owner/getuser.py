from aiogram import Bot
from aiogram.types import Message
import requests
from app import dp
from app.common import FMT
from aiogram.dispatcher.filters import Command, CommandObject
from aiogram.methods.get_chat import GetChat

@dp.message(commands=['юзер','user','userinfo'])
async def cmd_help(message: Message, f: FMT, bot: Bot,command: CommandObject):
    id = command.args
    firstname = await bot.get_chat(chat_id=id)
    await bot.send_message(text=f'{firstname}', chat_id=message.from_user.id)