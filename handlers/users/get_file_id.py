from aiogram.types import *
from loader import dp, bot
from data.config import ADMINS

@dp.message_handler(content_types=['photo'])
async def registration(message: Message):
    if message.from_user.id == 469415168:
        document_id = message.photo[0].file_id
        file_info = await bot.get_file(document_id)
        print('ID изображения', file_info.file_id)
    else:
        await bot.delete_message(message.chat.id, message.message_id)
