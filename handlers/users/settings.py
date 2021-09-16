from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import Text
from loader import dp
from utils import *
from states.settings import set_slp_percent
from keyboards.inline import *
from keyboards.default import *
from aiogram.dispatcher import FSMContext
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


@dp.message_handler(Text(equals=user_settings.text))
async def show_settings(message: Message):
    user_check(message.from_user.id, message.from_user.full_name)
    await message.answer(f"""Выберите настройку""", reply_markup=settings_menu)

@dp.message_handler(Text(equals=currencies_btn.text))
async def show_settings(message: Message):
    await message.answer(f"""Изменить валюту

Текущая валюта: {get_user_info(message.from_user.id)[0][4]}""", reply_markup=currencies_menu)

@dp.message_handler(Text(equals=currencies_usd.text))
async def show_settings(message: Message):
    sql_select_query = """UPDATE users set currencies = "USD" where userid = ?"""
    cursor.execute(sql_select_query, (message.from_user.id,))
    conn.commit()
    print(f'{message.from_user.full_name} поменял валюту на {get_user_info(message.from_user.id)[0][4]}')
    await message.answer(f"""Валюта изменена на {get_user_info(message.from_user.id)[0][4]}""")

@dp.message_handler(Text(equals=currencies_rub.text))
async def show_settings(message: Message):
    sql_select_query = """UPDATE users set currencies = "RUB" where userid = ?"""
    cursor.execute(sql_select_query, (message.from_user.id,))
    conn.commit()
    print(f'{message.from_user.full_name} поменял валюту на {get_user_info(message.from_user.id)[0][4]}')
    await message.answer(f"""Валюта изменена на {get_user_info(message.from_user.id)[0][4]}""")



@dp.message_handler(Text(startswith=f'{calculator_btn.text}'), state=None)
async def take_number(message: Message):
    await message.answer('''Изменить % вычисления калькулятора
    
Вы вводите общую сумму SLP, а калькулятор посчитает вам вашу долю в %

Бот принимает цифру от 1 до 100

Напишите какой процент нужно вычислять:''', reply_markup=calculator_menu)
    await set_slp_percent.Q1.set()

@dp.message_handler(state=set_slp_percent.Q1)
async def show_result(message: Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        if int(text) > 0 and int(text) <= 100:
            sql_select_query = f"""UPDATE users set fraction = ? where userid = ?"""
            cursor.execute(sql_select_query, (text, message.from_user.id))
            conn.commit()
            await state.reset_state()
            await message.answer(f'Успешно изменен на {text}%', reply_markup=settings_menu)
            print(f'{message.from_user.full_name} поменял % на {text}%')
        else:
            await message.answer(f'''❗️ Ошибка: Введите число в промежутке от 1 до 100''')
    elif text == 'Отменить':
        await state.reset_state()
        await message.answer('Действие отменено', reply_markup=settings_menu)
    else:
        await message.answer('❗️ Ошибка: Введите число в промежутке от 1 до 100 или нажмите "Отменить"')

