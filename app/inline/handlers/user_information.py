from aiogram.types import InlineQuery

from app import dp
from app.inline.articles.user_information import get_user_information_article


@dp.inline_query()
async def user_information_query(inline_query: InlineQuery):
    await inline_query.answer(
        results=[get_user_information_article(inline_query.from_user)],
        cache_time=0,
        is_personal=True,
    )
