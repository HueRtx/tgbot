from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault

import app

users_commands = {
    "help": "Показать список команд",
    "wttr": "Показать погоду в городе. Подробнее в /help",
    "bio": "О создателе",
    "roadmap": "Планы на бота",
}

owner_commands = {
    "ping": "Check bot ping",
    "stats": "Show bot stats",
    "user": "Show user info",
}


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(command=command, description=description)
            for command, description in owner_commands.items()
        ],
        scope=BotCommandScopeChat(chat_id=app.owner_id),
    )

    await bot.set_my_commands(
        [
            BotCommand(command=command, description=description)
            for command, description in users_commands.items()
        ],
        scope=BotCommandScopeDefault(),
    )


async def remove_bot_commands(bot: Bot):
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
    await bot.delete_my_commands(scope=BotCommandScopeChat(chat_id=app.owner_id))
