from aiogram import types, Dispatcher
from database.orm.user import check_user_by_telegram_id, get_user_film_history
from keyboards.inline.create_pagination_kb import create_pagination_kb


PER_PAGE = 1
dp = Dispatcher()


@dp.callback_query(lambda c: c.data and c.data.startswith('page_'))
async def change_page_callback_handler(callback_query: types.CallbackQuery):
    await callback_query.answer()

    page = int(callback_query.data.split('_')[1])
    telegram_id = callback_query.from_user.id
    user_id = await check_user_by_telegram_id(int(telegram_id))

    # Логирование для отладки
    print(f"Received callback for page: {page}, user_id: {user_id}")

    if user_id:
        history, total_count = await get_user_film_history(user_id, page, PER_PAGE)
        if history:
            film = history[0].film
            keyboards = create_pagination_kb(page, total_count)
            await callback_query.message.edit_media(
                media=types.InputMediaPhoto(
                    media=film.picture,
                    caption=f"{film.name}\n"
                            f"Жанры: {film.janr}\n"
                            f"Рейтинг: {film.rating}\n"
                            f"Год: {film.year}\n"
                            f"Продолжительность фильма: {film.movie_length}\n"
                            f"Страна: {film.country}\n"
                            f"Возрастной рейтинг: {film.age_rating}\n"
                            f"Описание: {film.description}",
                ),
                reply_markup=keyboards
            )
        else:
            await callback_query.message.edit_caption(
                caption="История поиска пуста.",
                reply_markup=None
            )
    else:
        await callback_query.message.edit_caption(
            caption="Пользователь не найден.",
            reply_markup=None
        )