from aiogram import types
from aiogram.dispatcher import FSMContext
import re
from keyboards.inline.user_inline_button import update_inline_check, inline_user_button
from loader import dp, db
from states.user_state import EditUserState




@dp.message_handler(state=EditUserState.id)
async def edit_user(message: types.Message, state: FSMContext):
    try:
        user_id = int(message.text)
        user = db.get_user(id=user_id)

        if user:
            async with state.proxy() as data:
                data['id'] = message.text
            # await EditUserState.next()
            # await message.answer("Foydalanuvchining ismini yangilang ")
            await message.answer_photo(photo=user[5],
                                       caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                               f"Foydalanuvchining yoshi : {user[2]}\n"
                                               f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                               f"Foydalanuvchining emaili : {user[4]}\n"
                                               f"\n",
                                       reply_markup=update_inline_check())
        else:
            await message.answer("Bu id raqamga tegishli fuqaro topilmadi . ")


    except:
        await message.answer("Id raqam bo'lsin")


# @dp.
        # await state.finish()



@dp.callback_query_handler(state=EditUserState)
async def call_back(callback: types.CallbackQuery, state: FSMContext):

    if callback.data == "edit_name":
        await callback.message.answer("Ismni yangilang ")
        await EditUserState.name.set()

    elif callback.data == "edit_age":

        await callback.message.answer("Yoshni yangilang ")
        await EditUserState.age.set()

    elif callback.data == "edit_phone_number":

        await callback.message.answer("Telefon nomerni yangilang ")
        await EditUserState.phone_number.set()

    elif callback.data == "edit_email":

        await callback.message.answer("Emailini  yangilang ")
        await EditUserState.email.set()

    elif callback.data == "edit_photo":

        await callback.message.answer("Rasmni yuklang ")
        await EditUserState.photo.set()

    elif callback.data == 'back_to_start':
        await callback.message.answer('Tanlang', reply_markup=inline_user_button())
        await state.finish()

@dp.message_handler(state=EditUserState.name)
async def edit_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        update_id = data["id"]

        db.update_user_name(id=update_id,name=data['name'])
    user_id = int(data['id'])
    user = db.get_user(id=user_id)
    await message.answer_photo(photo=user[5],
                               caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                       f"Foydalanuvchining yoshi : {user[2]}\n"
                                       f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                       f"Foydalanuvchining emaili : {user[4]}\n"
                                       f"\n",
                               reply_markup=update_inline_check())

#



@dp.message_handler(state=EditUserState.age)
async def edit_age(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        try:
            data['age'] = int(message.text)
            db.update_user_age(id=data['id'],
                               age=data['age'])
            user = db.get_user(data['id'])
            await message.answer_photo(photo=user[5],
                                   caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                           f"Foydalanuvchining yoshi : {user[2]}\n"
                                           f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                           f"Foydalanuvchining emaili : {user[4]}\n"
                                           f"\n",
                                   reply_markup=update_inline_check())
        except :
            await message.answer("Yosh butun sonda kiritimadi !")







@dp.message_handler(state=EditUserState.phone_number)
async def edit_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        PHONE_REGEX = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        phone = re.match(PHONE_REGEX, message.text)
        if phone:

            data['phone_number'] = message.text
            db.update_user_phone(id=data['id'],
                                 phone_number=data['phone_number'])
            user = db.get_user(data['id'])
            await message.answer_photo(photo=user[5],
                                       caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                               f"Foydalanuvchining yoshi : {user[2]}\n"
                                               f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                               f"Foydalanuvchining emaili : {user[4]}\n"
                                               f"\n",
                                       reply_markup=update_inline_check())

        else:
            await message.answer("Telefon nomer xato kiritildi !")
#











@dp.message_handler(state=EditUserState.email)
async def edit_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
        EMAIL_REGEX=r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
        email = re.match(EMAIL_REGEX, message.text)
        if email:
            db.update_user_email(id=data['id'],
                                 email=data['email'])
            user = db.get_user(data['id'])
            await message.answer_photo(photo=user[5],
                                       caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                               f"Foydalanuvchining yoshi : {user[2]}\n"
                                               f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                               f"Foydalanuvchining emaili : {user[4]}\n"
                                               f"\n",
                                       reply_markup=update_inline_check())

        else:
            await message.answer("Emailingizda xatolik bor!")



@dp.message_handler(lambda message: not message.photo, state=EditUserState.photo)
async def check_photo(message: types.Message):
    await message.answer("Bu rasm formatida emas")


@dp.message_handler(state=EditUserState.photo, content_types=['photo'])
async def add_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

        db.update_user_photo(id=data['id'],
                             photo=data['photo'])
        user = db.get_user(data['id'])
        await message.answer_photo(photo=user[5],
                                   caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                           f"Foydalanuvchining yoshi : {user[2]}\n"
                                           f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                           f"Foydalanuvchining emaili : {user[4]}\n"
                                           f"\n",
                                   reply_markup=update_inline_check())

    # db.add_user(name=data['name'],
    #                   age=data['age'],
    #                   phone_number=data['phone_number'],
    #                   email=data['email'],
    #                   photo=data['photo'])
    # await message.answer_photo(photo=data['photo'],
    #                            caption=f"Foydalanuvchini ismi {data['name']},\n"
    #                      f"uning yoshi {data['age']},\n"
    #                      f"uning raqami {data['phone_number']},\n"
    #                      f"emaili {data['email']}")








# @dp.message_handler(state=EditUserState.photo, content_types=['photo'])
# async def edit_photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['photo'] = message.photo[0].file_id
#
#     await state.finish()
#
#     db.update_user(id=data['id'],
#                    name=data['name'],
#                    age=data['age'],
#                    phone_number=data['phone_number'],
#                    email=data['email'],
#                    photo=data['photo'])
#     await message.answer("Foydalanuvchi ma'lumotlari o'zgartirildi")




# @dp.message_handler(state=EditUserState.photo, content_types=['photo'])
# async def add_photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['photo'] = message.photo[0].file_id

    # db.add_user(name=data['name'],
    #                   age=data['age'],
    #                   phone_number=data['phone_number'],
    #                   email=data['email'],
    #                   photo=data['photo'])
    # await message.answer_photo(photo=data['photo'],
    #                            caption=f"Foydalanuvchini ismi {data['name']},\n"
    #                      f"uning yoshi {data['age']},\n"
    #                      f"uning raqami {data['phone_number']},\n"
    #                      f"emaili {data['email']}")

