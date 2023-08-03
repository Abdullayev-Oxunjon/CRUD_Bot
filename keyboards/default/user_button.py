from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def user_rkm() -> ReplyKeyboardMarkup:
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton(text="user")
    rkm.add(button)
    return rkm



def cancel() :
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton(text="cancel")
    rkm.add(button)
    return rkm



