from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import  Text
from loader import dp
from states.calculate import *
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from utils import slp_take_price, get_user_info

# Функция получения клавиатуры
def keyboards_menu(id):
    menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    average_earnings = KeyboardButton(text='❔ Средний заработок в день')
    slp_to_rub = KeyboardButton(text=f'💲 {get_user_info(id)[0][5]}% SLP в {get_user_info(id)[0][4]}')
    back = KeyboardButton(text='В меню ')
    menu.add(slp_to_rub)
    menu.add(average_earnings)
    menu.add(back)
    return menu

# Меню калькулятора
@dp.message_handler(Text(startswith=f'Калькулятор'), state=None)
async def take_number(message: Message):

    await message.answer('''Что будем вычислять?''', reply_markup=keyboards_menu(message.from_user.id))

# Расчитать SLP в рублях
@dp.message_handler(Text(startswith=f'💲'), state=None)
async def slp_to_rub_take_number(message: Message):
    await message.answer(f'''Расчитать {get_user_info(message.from_user.id)[0][5]}% SLP в {get_user_info(message.from_user.id)[0][4]}
    
Введите общее кол-во SLP:''')
    await state_slp_45_to_rub.Q1.set()

@dp.message_handler(state=state_slp_45_to_rub.Q1)
async def slp_to_rub_result(message: Message, state: FSMContext):
    answer = message.text
    if answer.isdigit(): # Проверка на число
        user_info = get_user_info(message.from_user.id)
        answer = int(answer) / 100 * int(user_info[0][5])
        slp_price = slp_take_price(f'{user_info[0][4]}')
        result = float(slp_price) * answer
        await message.answer(f'{int(answer)} SLP составит {int(result)} {get_user_info(message.from_user.id)[0][4]}')
        print(f'{message.from_user.full_name} считает {get_user_info(message.from_user.id)[0][5]}% SLP')
        await state.reset_state()
    else:
        await state_slp_45_to_rub.first()
        await message.answer(f'''Расчитать {get_user_info(message.from_user.id)[0][5]}% SLP в {get_user_info(message.from_user.id)[0][4]}
        
❗️ Ошибка:  Напишите кол-во SLP''')

# Средний заработок в день:

@dp.message_handler(Text(startswith='❔'), state=None)
async def take_number(message: Message):
    await message.answer('''Средний заработок в день

Введите кол-во SLP:''')
    await state_average_earnings.Q1.set()

@dp.message_handler(state=state_average_earnings.Q1)
async def show_result(message: Message, state: FSMContext):
    slp = message.text
    if slp.isdigit():
        await state.update_data(slp=slp)
        await state_average_earnings.next()
        await message.answer(f'''Введите кол-во дней:''')
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
        if int(answer2) > 0:
            average = int(slp) / int(day)
            await state.reset_state()
            await message.answer(f'В среднем по {int(average)} SLP в день')
            print(f'{message.from_user.full_name} считает средний заработок')
        else:
            await message.answer(f'''❗️ Ошибка: Неверное кол-во дней''')
    else:
        await message.answer('''Средний заработок в день

❗️ Ошибка: Напишите кол-во дней''')