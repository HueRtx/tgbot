from aiogram.types import InlineQuery

from app import dp
from app.inline.articles.weather import weather


@dp.inline_query()
async def weather_query(inline_query: InlineQuery):
    await inline_query.answer(
        results=[weather(inline_query.from_user)],
        cache_time=0,
        is_personal=False,
    )