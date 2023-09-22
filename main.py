"""
Bu echo bot.
Bu har qanday kiruvchi matnli xabarlarni aks ettiradi.
"""
import os
import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import BoundFilter


class Kanal(BoundFilter):
    async def check(self, message: types.Message):
        return message.chat.type == types.ChatType.CHANNEL

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

@dp.channel_post_handler(Kanal(),content_types=['voice'])
async def post_in_channel(post: types.Message):
    chanel_caption = post.caption
    if chanel_caption == None: chanel_caption = ''
    await post.edit_caption(caption=f"""{chanel_caption}
    
    🔊  ▁ ▂ ▃ ▄ ▅ ▆ ▇ █

  ⇆ㅤㅤ◁ㅤ❚❚ㅤ▷ㅤㅤ↻

𝐓𝐎𝐋𝐈𝐐 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 𝐏𝐀𝐒𝐓𝐃𝐀 👇🎶""")


@dp.channel_post_handler(Kanal(),content_types=['audio'])
async def post_in_channel(post: types.Message):
    chanel_caption = post.caption
    if chanel_caption == None: chanel_caption = ''
    await post.edit_caption(caption=f"{chanel_caption}\n\n"
                                    f"𝐌𝐮𝐳𝐢𝐤𝐚 𝐭𝐨𝐩𝐮𝐯𝐜𝐡𝐢 𝐛𝐨𝐭👇\n"
                                    f"<a href='https://t.me/KuyniTopBot'>🖤🎧  @𝐊𝐮𝐲𝐧𝐢𝐓𝐨𝐩𝐁𝐨𝐭</a>\n\n"
                                    f"<a href='https://t.me/KuyMuzon'>👉𝐊𝐚𝐧𝐚𝐥𝐠𝐚 𝐨𝐛𝐮𝐧𝐚 𝐛𝐨𝐥𝐢𝐧𝐠</a>",reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Ulashish ♻️", url=f"https://t.me/share/url?url=https://t.me/{post.chat.username}/{post.message_id}")))

TEXT=os.environ.get("TASDIQLANGAN_XABARI", "Yangi Obunachi {mention}\n\n{title} kanaliga qo'shildi\n\n")

@dp.chat_join_request_handler(Kanal())
async def Tasdiqlash (message: ChatJoinRequest):
    chat=message.chat
    user=message.from_user
    print(f"{user.first_name} Obuna Boldi")
    await bot.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    await bot.send_message(chat_id=user.id, text="Xush Kelibsiz")
    await bot.send_message(chat_id=ADMINS, text=TEXT.format(mention=user.mention, title=chat.title))

class Guruh(BoundFilter):
    async def check(self,message: types.Message):
        return message.chat.type == types.ChatType.SUPERGROUP

@dp.chat_join_request_handler(Guruh())
async def Tasdiqlash (message: ChatJoinRequest):
    chat=message.chat
    user=message.from_user
    print(f"{user.first_name} Obuna Boldi")
    await bot.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    await bot.send_message(chat_id=user.id, text="Xush Kelibsiz")

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
