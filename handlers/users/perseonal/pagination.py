# from aiogram import types
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto, InlineQuery
# import math
# from loader import db, bot, dp

#
# def get_users(offset=0, limit=5):
#     users = db.all_user(offset, limit)
#     user_list = []
#     for user in users:
#         user_list.append({
#             'id': user[0],
#             'name': user[1],
#             'age': user[2],
#             'phone_number': user[3],
#             'photo': user[4]
#         })
#     return user_list
