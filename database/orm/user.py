from datetime import datetime
from sqlalchemy import update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from database.databases import async_session_factory
from database.models import User, HistoryFilm, HistorySerial
from datetime import timedelta


async def get_users():
    async with async_session_factory() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users


async def check_user_by_telegram_id(telegram_id: int):
    async with async_session_factory() as session:
        query = select(User).where(User.telegram_id == telegram_id)
        result = await session.execute(query)
        user = result.scalars().first()
        return user


async def check_user_id_by_telegram_id(telegram_id: int):
    async with async_session_factory() as session:
        query = select(User).where(User.telegram_id == telegram_id)
        result = await session.execute(query)
        user = result.scalars().first()
        return int(user.id)


async def add_user(name: str,
                   email: str,
                   phone_number: str,
                   telegram_id: int
                   ):

    async with async_session_factory() as session:

        new_user = User(
            name=name,
            email=email,
            phone_number=phone_number,
            telegram_id=telegram_id,
            created_at=datetime.utcnow()
        )

        session.add(new_user)
        await session.commit()


async def update_user(user_id: int, **kwargs):
    async with async_session_factory() as session:
        await session.execute(
            update(User).where(User.id == user_id).values(**kwargs)
        )

        await session.commit()


async def delete_user(user_id: int):
    async with async_session_factory() as session:
        await session.execute(
            delete(User).where(User.id == user_id)
        )

        await session.commit()


async def email_exists(email: str) -> bool:
    async with async_session_factory() as session:
        result = await session.execute(
            select(User).where(User.email == email)
        )
        user = result.scalars().first()
        return user is not None


async def phone_number_exists(phone_number: str) -> bool:
    async with async_session_factory() as session:
        result = await session.execute(
            select(User).where(User.phone_number == phone_number)
        )
        user = result.scalars().first()
        return user is not None


async def get_user_film_serial_history(user_id: int, page: int, per_page: int):
    async with async_session_factory() as session:
        film_query = select(
            HistoryFilm
        ).options(
            joinedload(HistoryFilm.film)
        ).where(
            HistoryFilm.user_id == user_id
        ).order_by(
            HistoryFilm.created_at.desc()
        )

        film_result = await session.execute(film_query)
        film_history = film_result.scalars().all()

        serial_query = select(
            HistorySerial
        ).options(
            joinedload(HistorySerial.serial)
        ).where(
            HistorySerial.user_id == user_id
        ).order_by(
            HistorySerial.created_at.desc()
        )

        serial_result = await session.execute(serial_query)
        serial_history = serial_result.scalars().all()

        combined_history = sorted(
            film_history + serial_history,
            key=lambda x: x.created_at,
            reverse=True
        )

        start_index = page * per_page
        end_index = start_index + per_page
        paginated_history = combined_history[start_index:end_index]

        total_count = len(combined_history)

        return paginated_history, total_count


async def get_user_film_serial_history_per_date(user_id: int, page: int, per_page: int, start_date: str, end_date: str):
    async with async_session_factory() as session:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)

        film_query = select(
            HistoryFilm
        ).options(
            joinedload(HistoryFilm.film)
        ).where(
            HistoryFilm.user_id == user_id,
            HistoryFilm.created_at >= start_date_dt,
            HistoryFilm.created_at < end_date_dt
        ).order_by(
            HistoryFilm.created_at.desc()
        )

        film_result = await session.execute(film_query)
        film_history = film_result.scalars().all()

        serial_query = select(
            HistorySerial
        ).options(
            joinedload(HistorySerial.serial)
        ).where(
            HistorySerial.user_id == user_id,
            HistorySerial.created_at >= start_date_dt,
            HistorySerial.created_at < end_date_dt
        ).order_by(
            HistorySerial.created_at.desc()
        )

        serial_result = await session.execute(serial_query)
        serial_history = serial_result.scalars().all()

        combined_history = sorted(
            film_history + serial_history,
            key=lambda x: x.created_at,
            reverse=True
        )

        start_index = page * per_page
        end_index = start_index + per_page
        paginated_history = combined_history[start_index:end_index]

        total_count = len(combined_history)

        return paginated_history, total_count
