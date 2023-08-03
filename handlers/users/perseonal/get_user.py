from aiogram import types
from aiogram.dispatcher.filters import state

from loader import dp, db
from states.user_state import GetUserState


@dp.message_handler(state=GetUserState.id)
async def get_user(message:types.Message):
        try:
                user_id= int(message.text)
                user = db.get_user(user_id)
                if user:
                        await message.answer_photo(photo=user[5],
                                                   caption=f"Foydalanuvchining ismi : {user[1]}\n"
                                                           f"Foydalanuvchining yoshi : {user[2]}\n"
                                                           f"Foydalanuvchining telefon raqami : {user[3]}\n"
                                                           f"Foydalanuvchining emaili : {user[4]}\n"
                                                           f"\n")

                else:
                        await message.answer("Bu id ga tegishli fuqaro topilmadi ")
        except:
                await message.answer("Id raqam bo'lsin")

