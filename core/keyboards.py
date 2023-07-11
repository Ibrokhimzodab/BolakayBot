from aiogram import types
from .i18 import menuKb, saleKb, contact, langKb, subMenuKb, subMenuKb2, typeKb, sendKb

lang_keyboard = types.ReplyKeyboardMarkup([
    [
        types.KeyboardButton(text=langKb[0]),
        types.KeyboardButton(text=langKb[1])
    ]
], resize_keyboard=True)

menuKeyboard = [
    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=menuKb[0][0]),
            types.KeyboardButton(text=menuKb[0][1])
        ]
    ], resize_keyboard=True),

    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=menuKb[1][0]),
            types.KeyboardButton(text=menuKb[1][1])
        ]
    ], resize_keyboard=True)
]

subMenuKeyboard = [
    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=subMenuKb[0][0]),
            types.KeyboardButton(text=subMenuKb[0][1]),
            types.KeyboardButton(text=subMenuKb[0][2])
        ]
    ], resize_keyboard=True),

    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=subMenuKb[1][0]),
            types.KeyboardButton(text=subMenuKb[1][1]),
            types.KeyboardButton(text=subMenuKb[1][2])
        ]
    ], resize_keyboard=True)
]

subMenuKeyboard2 = [
    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=subMenuKb2[0][0]),
            types.KeyboardButton(text=subMenuKb2[0][1]),
            types.KeyboardButton(text=subMenuKb2[0][2])
        ]
    ], resize_keyboard=True),

    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=subMenuKb2[1][0]),
            types.KeyboardButton(text=subMenuKb2[1][1]),
            types.KeyboardButton(text=subMenuKb2[1][2])
        ]
    ], resize_keyboard=True)
]

typeKeyboard = [
    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=typeKb[0][0]),
            types.KeyboardButton(text=typeKb[0][1]),
            types.KeyboardButton(text=typeKb[0][2])
        ]
    ], resize_keyboard=True),

    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=typeKb[1][0]),
            types.KeyboardButton(text=typeKb[1][1]),
            types.KeyboardButton(text=typeKb[1][2])
        ]
    ], resize_keyboard=True)
]

saleKeyboard = [
    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=saleKb[0][0]),
            types.KeyboardButton(text=saleKb[0][1]),
        ]
    ], resize_keyboard=True),

    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=saleKb[1][0]),
            types.KeyboardButton(text=saleKb[1][1]),
        ]
    ], resize_keyboard=True),
]

contact_keyboard = [
    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=contact[0], request_contact=True)
        ]
    ], resize_keyboard=True, one_time_keyboard=True),

    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=contact[1], request_contact=True)
        ]
    ], resize_keyboard=True, one_time_keyboard=True)
]

sendKeyboard = [
    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=sendKb[0])
        ]
    ], resize_keyboard=True),

    types.ReplyKeyboardMarkup([
        [
            types.KeyboardButton(text=sendKb[1])
        ]
    ], resize_keyboard=True)
]
