from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def inline_user_button():
    ikm = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="Add User", callback_data="add_user")
    button2 = InlineKeyboardButton(text="All User", callback_data="all_user")
    button3 = InlineKeyboardButton(text="Get User", callback_data="get_user")
    button4 = InlineKeyboardButton(text="Update User", callback_data="update_user")
    button5 = InlineKeyboardButton(text="Delete User", callback_data="delete_user")
    ikm.add(button, button2, button3, button4, button5)
    return ikm


def update_inline_check():
    ikm = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Name",callback_data="edit_name")
    button1 = InlineKeyboardButton("Age",callback_data="edit_age")
    button2 = InlineKeyboardButton("Phone Number",callback_data="edit_phone_number")
    button3 = InlineKeyboardButton("Email",callback_data="edit_email")
    button4 = InlineKeyboardButton("Photo",callback_data="edit_photo")
    button5 = InlineKeyboardButton("Back to home",callback_data="back_to_start")
    ikm.add(button,button1,button2,button3,button4,button5)

    return ikm

