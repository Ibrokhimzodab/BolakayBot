from aiogram import types
from .adminI18 import menuAdminKb, cancel

menuAdminKeyboard = types.ReplyKeyboardMarkup([
    [
        types.KeyboardButton(text=menuAdminKb[0]),
        types.KeyboardButton(text=menuAdminKb[1])
    ],
    [
        types.KeyboardButton(text=menuAdminKb[2]),
        types.KeyboardButton(text=menuAdminKb[3])
    ],
    [
        types.KeyboardButton(text=menuAdminKb[4]),
        types.KeyboardButton(text=menuAdminKb[5])
    ],
    [
        types.KeyboardButton(text=menuAdminKb[6])
    ]
], resize_keyboard=True)

cancelKeyboard = types.ReplyKeyboardMarkup([
    [
        types.KeyboardButton(text=cancel)
    ]
], resize_keyboard=True)
