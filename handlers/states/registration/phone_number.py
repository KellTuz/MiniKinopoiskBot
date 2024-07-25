from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.reply.back_kb import back_kb
from keyboards.reply.main_kb import main_kb
from keyboards.reply.back_or_number_kb import back_or_number_kb
from states.registration import Registration
from utils.phonenumber_validation import phonenumber_validation
from database.orm.user import add_user, phone_number_exists


router = Router(name=__name__)


@router.message(Registration.phone_number, F.text == "Назад")
async def registration_phone_number_handler_back(message: Message, state: FSMContext):
    await state.set_state(Registration.email)
    await message.answer(
        text="Напишите пожалуйста вашу почту: ",
        reply_markup=back_kb(),
        )

TODO # Переделать вариацию вывода если пользователь авторизовывается или регистрируется
@router.message(Registration.phone_number, F.text.cast(phonenumber_validation).as_("phone_number"))
async def registration_phone_number_handler(message: Message, state: FSMContext):
    phone_number = message.text

    if await phone_number_exists(phone_number):
        await message.answer(
            text="Этот номер телефона уже зарегистрирован. Пожалуйста, используйте другой номер телефона.",
            reply_markup=back_or_number_kb(),
            parse_mode=None,
            )

    data = await state.update_data(phone_number=message.text)
    await add_user(
        name=data["name"],
        email=data["email"],
        phone_number=data["phone_number"],
        telegram_id=message.from_user.id,
    )

    await message.answer(
        text="Спасибо за регистрацию в боте. Теперь вы можете пользоваться всем функционалом бота.",
        reply_markup=main_kb(),
        parse_mode=None,
    )

    await state.clear()


@router.message(Registration.phone_number, F.contact)
async def registration_phone_number_handler(message: Message, state: FSMContext):
    if message.contact:
        phone_number = message.text

        if await phone_number_exists(phone_number):
            await message.answer(
                text="Этот номер телефона уже зарегистрирован. Пожалуйста, используйте другой номер телефона.",
                reply_markup=back_or_number_kb(),
                parse_mode=None,
                )

        data = await state.update_data(phone_number=message.contact.phone_number)
        await add_user(
            name=data["name"],
            email=data["email"],
            phone_number=data["phone_number"],
            telegram_id=message.from_user.id,
            )

        await message.answer(
            text="Спасибо за регистрацию в боте. Теперь вы можете пользоваться всем функционалом бота.",
            reply_markup=main_kb(),
            parse_mode=None,
            )

        await state.clear()


@router.message(Registration.phone_number)
async def registration_phone_number_handler_none(message: Message):
    await message.answer(
        text="Простите я не понимаю. Нажмите на кнопку <Поделиться номером> для отправки вашего номера телефона.",
        reply_markup=back_or_number_kb(),
        parse_mode=None,
    )

