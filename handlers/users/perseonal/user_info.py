from operator import ge

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.default.user_button import cancel
from keyboards.inline.user_inline_button import inline_user_button
from loader import dp, db, bot
from states.user_state import AddUserState, EditUserState, DeleteUserState, GetUserState


@dp.message_handler(Text(equals="cancel"),  state="*")
async def get_cancel(message: types.Message, state: FSMContext):
    await message.answer(text="Bekor qilindi",
                         reply_markup=inline_user_button())
    await state.finish()


@dp.message_handler(Text(equals="user"))
async def get_info(message: types.Message):
    await message.answer(text="Foydalanuvchilarni tahrirlash",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text="Qaysi amalni tanlaysiz",
                         reply_markup=inline_user_button())


@dp.callback_query_handler()
async def user_callback(callback: types.CallbackQuery):
    if callback.data == "add_user":
        await callback.message.answer(text="Foydalanuvchilar ro'yxatiga qo'shish",
                                      reply_markup=ReplyKeyboardRemove())
        await callback.message.answer(text="Foydalanuchining ismini kiriting ",
                                      reply_markup=cancel())
        await AddUserState.name.set()

    elif callback.data == "update_user":
        await callback.message.answer(text="Foydalanuvchi tahrirlash",
                                      reply_markup=ReplyKeyboardRemove())
        await EditUserState.id.set()
        await callback.message.answer(text="Qaysi id tegishli foydalanuvchini tahrirlamoqchisiz",
                                      reply_markup=cancel())

    elif callback.data == "delete_user":
        await callback.message.answer(text="Foydalanuvchini o'chirish",
                                 reply_markup=ReplyKeyboardRemove())

        await callback.message.answer("Qaysi id ga tegishli "
                                      "foydalanuvchini o'chirmoqchisiz !",
                                      reply_markup=cancel())
        await DeleteUserState.id.set()

    elif callback.data == "all_user":
        users = db.all_user()
        for user in users:
            await callback.message.answer_photo(photo=user[5],
                                                caption=f"Foydalanuvchini ismi {user[1]},\n"
                                                        f"yoshi {user[2]},\n"
                                                        f"Telefon raqami {user[3]},"
                                                        f"Emaili {user[4]}")

    elif callback.data == "get_user":
        await callback.message.answer(text="Kiritilgan id ga tegishli foydalanuvchini olish",
                                      reply_markup=ReplyKeyboardRemove())

        await callback.message.answer("Qaysi id ga tegishli fuqaro kerak ",
                                      reply_markup=cancel())
        await GetUserState.id.set()






