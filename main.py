"""
Bu echo bot.
Bu har qanday kiruvchi matnli xabarlarni aks ettiradi.
"""

import config
import logging
from aiogram import Bot, Dispatcher, executor, types

# loggingni sozlaymiz
logging.basicConfig(level=logging.INFO)

# Bot va dispetcherni ishga tushiring
bot = Bot(token=config.BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def welcome(m: types.Message):

    """
    Ushbu ishlov beruvchi foydalanuvchi `/start` buyrug'ini yuborganda chaqiriladi
    """

    await m.answer(
        text=f'Salom botga xush kelibsiz!\n{m.from_user.full_name}'
    )

@dp.message_handler(state=None)
async def echo(m: types.Message):
    # eski uslub:
    # kutmoqda bot. send_message(message.chat.id, xabar.matn)

    # yangi uslub:
    await m.answer(
        text=m.text
    )

# botni ishga tushiradigan kodni yozamiz
if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)