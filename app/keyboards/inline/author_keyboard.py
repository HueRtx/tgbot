from aiogram.utils.keyboard import InlineKeyboardBuilder

from app import owner_id


def get_author_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Автор", url=f"tg://user?id={owner_id}")
    return keyboard.as_markup()
def start1_kb():
    keyboard= InlineKeyboardBuilder()
    keyboard.button(text="Обо мне", callback_data="bio")
    keyboard.button(text="Сайт владельца", url="https://floduat.org/")
    keyboard.button(text="Блог владельца", url="tg://resolve?domain=kegablog")
    return keyboard.as_markup()
def obo_mne():
    keyboard=InlineKeyboardBuilder()
    keyboard.button(text="Мой пк", callback_data="pc")
    keyboard.button(text="Сайт владельца",url="https://floduat.org/")
    keyboard.button(text="Блог владельца", url="tg://resolve?domain=kegablog")
    return keyboard.as_markup()
def pc_xarak():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="⬅Назад", callback_data="back"),
    return keyboard.as_markup()
def serv_tex():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="⬅Назад", callback_data="server")
    keyboard.button(text="⬅В начало", callback_data="back1")
    return keyboard.as_markup()
def botinfo():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="⬅Назад", callback_data="pc")
    keyboard.button(text="Техническия характеристики на сервере бота", callback_data="servertex")
    return keyboard.as_markup()
