from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
    InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

settings_menu = ReplyKeyboardMarkup()
currencies_btn = KeyboardButton('Валюта 💵')
calculator_btn = KeyboardButton('% Калькулятора 📟')
back = KeyboardButton('В меню')
cancel = KeyboardButton('Отменить')

settings_menu.row(currencies_btn, calculator_btn)
settings_menu.add(back)

currencies_menu = ReplyKeyboardMarkup()
currencies_usd = KeyboardButton('USD 🇺🇸')
currencies_rub = KeyboardButton('RUB 🇷🇺')
currencies_menu.row(currencies_rub, currencies_usd)
currencies_menu.add(back)

calculator_menu = ReplyKeyboardMarkup()
calculator_menu.add(cancel)

