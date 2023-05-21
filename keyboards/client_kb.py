from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_music = KeyboardButton('Музика 🤟')
button_team = KeyboardButton('Команда 💪')
button_help = KeyboardButton('Довідка 🌚')


greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_help, button_team)