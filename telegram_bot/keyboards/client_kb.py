from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_keyboard_1 = KeyboardButton('/Добавить_задачу')
button_keyboard_2 = KeyboardButton('/Просмотр_списка')

keyboard_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_client.add(button_keyboard_1).insert(button_keyboard_2)