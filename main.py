import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from insta import instadownload
from funk import *
import datetime
from aiogram.types import Message,CallbackQuery
from config import *
from tiktok import tk
from aiogram.dispatcher.filters.builtin import CallbackQuery
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
from pytube import YouTube
from io import BytesIO
import os
import re
import urllib.request

logging.basicConfig(level=logging.INFO)

Admin = 708006401
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


##### register
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    conn = sqlite3.connect('tiktik.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        id integer,
        username varchar(60),
        first_name varchar(60),
        voxt varchar(50) 
       
        )""")
    conn.commit()

    user_id = message.chat.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    c.execute(f"SELECT id FROM users WHERE id = {user_id}")
    data = c.fetchone()
    datatime = datetime.datetime.now()

    if data is None:
        c.execute("INSERT INTO users  VALUES ({},'{}','{}','{}')".format(user_id,username,first_name,datatime))
        conn.commit()
        await message.reply(f"*Assalomu aleykum Botimizga Xush kelibsz 😊*\n*{username}*\n*Yuklamoxchi bo\'lgan videoyingizni silkasini yuboring✅*👇🏻",parse_mode='markdown')
        await bot.send_message(Admin,"ID: #{}\nUsername: @{}\nF.I.O: {}\nTashrif vaqti: {}".format(user_id,username,first_name,datatime))
    else:
        await message.answer('*Siz ro\'yxatdan o\'tkansz✅\nYuklamoxchi bo\'lgan videoyingizni silkasini yuboring ✅*',parse_mode='markdown')



############# instagram
@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_welcome(message: types.Message):
    await message.answer('*Loading...🔍*',parse_mode='markdown')
    link = message.text
    print(link,'lllllllllllllllllllllllllllllllllllllllll')
    data = instadownload(link=link)
    try:
        if data == 'Bad':
                await message.answer('*sorry not found*',parse_mode='markdown')
        else:
            if data['type'] == 'image':
                await message.answer_photo(photo=data['media'])
            elif data['type'] == 'video':
                await message.answer_video(video=data['media'])
            elif data['type'] == 'carousel':
                for i in data['media']:
                    await message.answer_document(document=i)
    except:
            await message.answer('*sorry not found*',parse_mode='markdown')





############# tiktok
@dp.message_handler(Text(startswith='https://www.tiktok.com/'))
async def test(message: types.Message):
    await message.answer('*Loading...🔍*',parse_mode='markdown')
    natija = tk(message.text)
    qoshiq = natija['music']
    print(qoshiq)
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text = "Musiqani yuklash",
            url = "{}".format(qoshiq))]
            ]
        )
    try:
        await message.answer_audio(natija['video'],reply_markup=btn)
    except:
        await message.answer("*sorry not found*",parse_mode='markdown')


####### youtube
@dp.message_handler()
async def text_message(message: types.Message):
    await message.answer('*Music download...🔍*',parse_mode='markdown')
    link = message.text
    url = YouTube(link)
    try:
        if url.check_availability() is None:
            buffer = BytesIO()
            audio = url.streams.get_audio_only()
            audio.stream_to_buffer(buffer=buffer)
            buffer.seek(0)
            filename = url.title
            await message.answer_audio(audio=buffer,caption=filename)
    except:
        await message.answer("*sorry*",parse_mode='markdown')
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    try:
        if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/':
            await bot.send_message(chat_id,f"*beginning download*: *{yt.title}*\n"
                                f"*chanel*: [{yt.author}]({yt.channel_url})",parse_mode='markdown')
            await message.answer('*Loading...🔍\nPlase wait few minutes*',parse_mode='markdown')
            await dowload_youtube_videos(url,message,bot)
    except:
        await message.answer("*Sorry video not found*",parse_mode='markdown')



async def dowload_youtube_videos(url,message,bot):
    chat_id = message.chat.id
    yt = YouTube(url)
    print(yt.title)
    stream = yt.streams.filter(progressive=True,file_extension="mp4")
    stream.get_highest_resolution().download(f'{message.chat.id}',f'{message.chat.id}_{yt.title}')
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", 'rb') as video:
        await bot.send_video(message.chat.id,video,caption="*your video*",parse_mode='markdown')
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")




############### youtube audio
###### youtube 
@dp.message_handler(Text(startswith="http"))
async def get_audio(message:types.Message):
     await message.answer('Loading...🔍')
     link = message.text
     url = YouTube(link)
     if url.check_availability() is None:
         buffer = BytesIO()
         audio = url.streams.get_audio_only()
         audio.stream_to_buffer(buffer=buffer)
         buffer.seek(0)
         filename = url.title
         await message.answer_audio(audio=buffer,caption=filename)
        
     else:
         await message.answer("xatolik")

################################## facebook

# @dp.message_handler()
# async def text_message(message: types.Message):
#     chat_id = message.chat.id
#     try:
#         if message.text.startswith == 'https://fb/' or 'https://www.facebook.com/':
#             html = requests.get(link)
#             url = re.search('hd_src:"(.+?)"',html.message.text)[1]
#             await message.answer("hd")
#             a = urllib.request.urlretrieve(url)
#             await bot.send_message(a)
#     except:
#         url = re.search('sd_src:"(.+?)"',html.message.text)[1]
#         await message.answer("hd")





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)