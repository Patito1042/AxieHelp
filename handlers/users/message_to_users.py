from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from loader import dp, bot
from data.config import ADMINS
from states.send_to_user import *
from utils.db_api.db_view import *
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from keyboards.default import *

cancel = ReplyKeyboardMarkup()
cancel_btn = KeyboardButton(text='Отменить')
cancel.add(cancel_btn)

@dp.message_handler(Text(startswith=f'Отправить всем'), state=None)
async def msg_to_user_check(message: Message):
    if message.from_user.id == ADMINS:
        await message.answer('Все норм. Пиши сообщение:', reply_markup=cancel)
        await send_msg_to_user.Q1.set()
    else:
        print('Чужак')

@dp.message_handler(state=send_msg_to_user.Q1)
async def msg_to_user_send(message: Message, state: FSMContext):
    if message.text == 'Отменить':
        await message.answer('Отменено', reply_markup=menu)
        await state.reset_state()
    else:
        text = message.text
        users = get_all_users()
        for id in users[0:]:
            await bot.send_message(id[0], text)
        await message.answer('Успех', reply_markup=menu)
    await state.reset_state()