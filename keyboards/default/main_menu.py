from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

directory = KeyboardButton(text='Справочник 📚')
useful_links = KeyboardButton(text='Полезные ссылки 🔗')
calculator = KeyboardButton(text='Калькулятор 📟')
slp_price = KeyboardButton(text='Курс SLP 📈')
axs_price = KeyboardButton(text='Курс AXS 📈')
settings = KeyboardButton(text='Настройки ⚙️')

menu.add(directory)
menu.add(calculator)
menu.row(slp_price, axs_price)
menu.add(settings)
