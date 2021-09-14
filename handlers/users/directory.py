from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp, bot
from keyboards.default import *
from data.img_id import *
import sqlite3

@dp.message_handler(Text(equals=directory.text))
async def slp_price(message: types.Message):
    await bot.send_photo(message.from_user.id, balance_circle, 'Раздел в разработке ;)')
