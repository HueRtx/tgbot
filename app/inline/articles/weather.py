from aiogram.types import InlineQueryResultArticle, InputTextMessageContent, User
import requests
def weather(user: User):
    weather1 = requests.get(f"https://wttr.in/{InputTextMessageContent}?format=3")
    weather_reply = weather1.text
    return InlineQueryResultArticle(
        id="weather-inline",
        title="Погода в определенном городе",
        description=f"Укажите город",
        input_message_content=InputTextMessageContent(
            message_text=f"{weather_reply}"
        ),
    )
