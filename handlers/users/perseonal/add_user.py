from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot, db
from states.user_state import AddUserState
import re


@dp.message_handler(state=AddUserState.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer("Foydalanuvchini yoshini kiriting")
    # await AddUserState.age.set()
    await AddUserState.next()


@dp.message_handler(state=AddUserState.age)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await AddUserState.next()
    await message.answer("Foydalanuvchini raqamini kiriting")


@dp.message_handler(state=AddUserState.phone_number)
async def add_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        PHONE_REGEX = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        phone_number = re.match(PHONE_REGEX, message.text)
        if phone_number:
            data['phone_number'] = message.text

            await AddUserState.next()
            await message.answer("Foydalanuvchini emailini kiriting")
        else:
            await message.answer("Telefon raqam xato kiritildi")


@dp.message_handler(state=AddUserState.email)
async def add_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
        EMAIL_REGEX=r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
        email = re.match(EMAIL_REGEX, message.text)
        if email:
            data['email'] = message.text
            await AddUserState.next()
            await message.answer("Foydalanuvchini rasmini kiriting")
        else:
            await message.answer("Emailingizda xatolik bor!")







@dp.message_handler(lambda message: not message.photo, state=AddUserState.photo)
async def check_photo(message: types.Message):
    await message.answer("Bu rasm formatida emas")


@dp.message_handler(state=AddUserState.photo, content_types=['photo'])
async def add_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await state.finish()
    await message.answer("Ma'lumotingiz saqlandi")
    db.add_user(name=data['name'],
                      age=data['age'],
                      phone_number=data['phone_number'],
                      email=data['email'],
                      photo=data['photo'])
    await message.answer_photo(photo=data['photo'],
                               caption=f"Foydalanuvchini ismi {data['name']},\n"
                         f"uning yoshi {data['age']},\n"
                         f"uning raqami {data['phone_number']},\n"
                         f"emaili {data['email']}")



