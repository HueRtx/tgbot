from aiogram import Bot

from aiogram.types import Message

from app.keyboards.inline.author_keyboard import start1_kb,obo_mne,pc_xarak,serv_tex,botinfo
from app import dp
from app.common import FMT

@dp.message(commands=['bio'])
async def cmd_bio(message: Message, f: FMT, bot: Bot):
    await bot.send_message(text=f'Привет! Это кега или же FLoduat, простой человек из Беларуси(UTC+3 - Moscow '
                                       f'Time)!\n Я немного разбираюсь в python и JavaScript. Еще чуть-чуть в '
                                       f'компах.\n Мой талисман - хомяк.', chat_id=message.from_user.id, reply_markup=obo_mne())
@dp.callback_query_handler(text_contains='pc')
async def callback1(message: Message, f: FMT, bot: Bot):
    await bot.edit_message_text(text="Характеристики моего пк:\n Процессор: Ryzen 5 3600\n Материнская плата: B550 Aorus Pro\n Оперативная "
             "память: Geil evo spear 3000mhz, kit 2pcs 8gb\n Видеокарта: RTX 2060 palit (6gb VRAM)", message_id=message.message.message_id, chat_id=message.from_user.id,  reply_markup=pc_xarak())
@dp.callback_query_handler(text_contains='back')
async def backcall(message: Message, f: FMT, bot: Bot):
    await bot.edit_message_text(text=f'Привет! Это кега или же FLoduat, простой человек из Беларуси(UTC+3 - Moscow '
                            f'Time)!\n Я немного разбираюсь в python и JavaScript. Еще чуть-чуть в '
                            f'компах.\n Мой талисман - хомяк.', message_id=message.message.message_id,chat_id=message.from_user.id, reply_markup=obo_mne())
