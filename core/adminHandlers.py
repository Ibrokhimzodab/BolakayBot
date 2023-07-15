from app import dp, bot, types
from .model import User, Group
from db.state import RegisterState, FirstState
from .keyboards import lang_keyboard, contact_keyboard, menuKeyboard, subMenuKeyboard, subMenuKeyboard2, typeKeyboard, saleKeyboard, sendKeyboard
from .i18 import chooseLang, sendPhone, chooseName, registrationFinished, menuKb, subMenuKb, subMenuKb2, typeKb, saleKb, \
    sendKb, choose, fromLoc, whereLoc, mainMenu, sent, langKb, sendPhoto, sendDescription
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import Text


@dp.message_handler(commands=['admin'])
async def check_admin(message: types.Message):
    if User.isUserAdmin(message.from_user.id):
        await AdminState.menu.set()
        return await bot.send_message(message.chat.id, mainMenuAdmin, reply_markup=menuAdminKeyboard)


@dp.message_handler(Text(equals=menuAdminKb), state=AdminState.menu)
async def receiver_language(message: types.Message, state: FSMContext):
    if message.text == menuAdminKb[0]:
        #TODO: get and send users in list
        for user in User.getAllUsers():

        await state.finish()
    elif message.text == menuAdminKb[1]:
        #TODO: add group to database
    elif message.text == menuAdminKb[2]:
        #TODO: set user to admin
    elif message.text == menuAdminKb[3]:
        #TODO: send advertisement