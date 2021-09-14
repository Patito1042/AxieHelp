from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from loader import dp
from utils import *
from keyboards.default import *

@dp.message_handler(CommandStart())
@dp.message_handler(Text(equals='В меню'))
async def bot_start(message: Message):
    user_check(message.from_user.id, message.from_user.full_name)
    await message.answer(f"""Привет, {message.from_user.full_name}!""", reply_markup=menu)

@dp.message_handler(Text(equals=slp_price.text))
async def slp_price(message: Message):
    await message.answer(f'Текущий курс SLP: {slp_take_price()} рубля')

@dp.message_handler(Text(equals=axs_price.text))
async def axs_price(message: Message):
    await message.answer(f'Текущий курс AXS: {axs_take_price()} рубля')

    @dp.message_handler(Text(equals=useful_links.text))
    async def axs_price(message: Message):
        await message.answer(f'Раздел в разработке')