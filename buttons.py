from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup
from main import *
from tiktok import tk

natija = tk(message.text)
qoshiq = natija['music']
btn = InlineKeyboardMarkup(
inline_keyboard=[
	    [

	    InlineKeyboardButton(text = "Musiqani yuklash",url = "🎵{}".format(qoshiq)),

		],
            
	],

)