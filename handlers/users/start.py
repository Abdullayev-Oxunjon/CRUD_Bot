from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.user_button import user_rkm
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=f"Salom, {message.from_user.full_name}!",
                         reply_markup=user_rkm())
