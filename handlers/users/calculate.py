from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from loader import dp, bot
from states.calculate import *
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from utils import slp_take_price, slp_price
from utils.calculator import *

menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

slp_to_rub = KeyboardButton(text='💲 SLP в рублях')
slp45_to_rub = KeyboardButton(text='💲 45% SLP в рублях')
average_earnings = KeyboardButton(text='❔ Средний заработок в день')
back = KeyboardButton(text='В меню ')

menu.add(slp_to_rub, slp45_to_rub)
menu.add(average_earnings)
menu.add(back)

#
@dp.message_handler(Text(startswith=f'Калькулятор'), state=None)
async def take_number(message: Message):
    await message.answer('''Что будем вычислять?''', reply_markup=menu)

@dp.message_handler(Text(startswith=f'{slp45_to_rub.text}'), state=None)
async def take_number(message: Message):
    await message.answer('''Расчитать 45% SLP в рублях

Введите кол-во SLP:''', reply_markup=menu)
    await state_slp_45_to_rub.Q1.set()


@dp.message_handler(state=state_slp_45_to_rub.Q1)
async def show_result(message: Message, state: FSMContext):
    answer = message.text
    if answer.isdigit():
        answer = int(answer) / 100 * 45
        slp_price = slp_take_price()
        result = float(slp_price) * answer
        await message.answer(f'{int(answer)} SLP составит {int(result)} рублей')
        print(f'{message.from_user.full_name} считает 45% SLP')
        await state.reset_state()
    else:
        await state_slp_45_to_rub.first()
        await message.answer('''Расчитать 45% SLP в рублях
        
❗️ Ошибка:  Напишите кол-во SLP''')

# Расчитать 100% SLP в рублях

@dp.message_handler(Text(startswith=f'{slp_to_rub.text}'), state=None)
async def take_number(message: Message):
    await message.answer('''Расчитать SLP в рублях

Введите кол-во SLP:''', reply_markup=menu)
    await state_slp_to_rub.Q1.set()


@dp.message_handler(state=state_slp_to_rub.Q1)
async def show_result(message: Message, state: FSMContext):
    answer = message.text
    if answer.isdigit():
        slp_price = slp_take_price()
        result = float(slp_price) * float(answer)
        await message.answer(f'{int(answer)} SLP составит {int(result)} рублей')
        print(f'{message.from_user.full_name} считает SLP')
        await state.reset_state()
    else:
        await state_slp_to_rub.first()
        await message.answer('''Расчитать SLP в рублях

❗️ Ошибка: Напишите кол-во SLP''')

# Средний заработок в день:

@dp.message_handler(Text(startswith=f'{average_earnings.text}'), state=None)
async def take_number(message: Message):
    await message.answer('''Средний заработок в день

Введите кол-во SLP:''', reply_markup=menu)
    await state_average_earnings.Q1.set()


@dp.message_handler(state=state_average_earnings.Q1)
async def show_result(message: Message, state: FSMContext):
    slp = message.text
    if slp.isdigit():
        await state.update_data(slp=slp)
        await state_average_earnings.next()
        await message.answer(f'''Введите кол-во дней:''', reply_markup=menu)
    else:
        await state_average_earnings.first()
        await message.answer('''Средний заработок в день

❗️ Ошибка: Напишите кол-во SLP''')

@dp.message_handler(state=state_average_earnings.Q2)
async def show_result(message: Message, state: FSMContext):
    data = await state.get_data()
    slp = data['slp']
    day = message.text
    answer2 = message.text
    if answer2.isdigit():
        average = int(slp) / int(day)
        await state.reset_state()
        await message.answer(f'В среднем по {int(average)} SLP в день')
        print(f'{message.from_user.full_name} считает средний заработок')
    else:
        await state_average_earnings.previous()
        await message.answer('''Средний заработок в день

❗️ Ошибка: Напишите кол-во дней''')
