from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNELS

btnProfile = KeyboardButton(text='ПРОФИЛЬ')
keyboard_buttons = [[btnProfile]]
profileKeyboard = ReplyKeyboardMarkup(keyboard=keyboard_buttons, resize_keyboard=True)

def showChannels():
    buttons = []
    for channel in CHANNELS:
        btn = InlineKeyboardButton(text=channel[0], url=channel[2])
        buttons.append(btn)
    btnDoneSub = InlineKeyboardButton(text='Я ПОДПИСАЛСЯ', callback_data='subchanneldone')
    buttons.append(btnDoneSub)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[btn] for btn in buttons])
    return keyboard

def subchannel_done_message():
    return "Спасибо, что подписались на наших спонсоров. Теперь вы можете использовать полный функционал бота, у вас на балансе 100.000 условных рублей"
