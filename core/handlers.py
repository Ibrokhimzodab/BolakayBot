from app import dp, bot, types
from .model import User, Group
from db.state import RegisterState, FirstState, AdminState
from .keyboards import lang_keyboard, contact_keyboard, menuKeyboard, subMenuKeyboard, subMenuKeyboard2, typeKeyboard, \
    saleKeyboard, sendKeyboard, menuAdminKeyboard
from .i18 import chooseLang, sendPhone, chooseName, registrationFinished, menuKb, subMenuKb, subMenuKb2, typeKb, saleKb, \
    sendKb, choose, fromLoc, whereLoc, mainMenu, sent, langKb, sendPhoto, sendDescription, menuAdminKb, mainMenuAdmin
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import Text


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if User.isRegistered(message.chat.id):
        user = User.getUser(message.chat.id)
        return await bot.send_message(message.chat.id, mainMenu[user.language], reply_markup=menuKeyboard[user.language])

    await RegisterState.language.set()

    await message.answer(chooseLang[0], reply_markup=lang_keyboard)


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


@dp.message_handler(lambda message: message.text, state=RegisterState.language)
async def receiver_language(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        lang = 0 if message.text == "uz" else 1
        data['language'] = lang

    await RegisterState.next()
    await message.answer(chooseName[lang], reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text, state=RegisterState.name)
async def receiver_language(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        lang = data["language"]

    await RegisterState.next()
    await bot.send_message(message.chat.id, sendPhone[lang], reply_markup=contact_keyboard[lang])


@dp.message_handler(lambda message: message.contact, content_types=['contact'], state=RegisterState.phone)
async def receiver_phone(message: types.contact, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.contact.phone_number
        lang = data["language"]
        name = data["name"]

        user = User(message.contact.user_id, message.chat.id, name, message.contact.phone_number, lang)
        user.save()

        await bot.send_message(message.chat.id, registrationFinished[lang])
        await bot.send_message(message.chat.id, mainMenu[lang], reply_markup=menuKeyboard[lang])
        await state.finish()


@dp.message_handler(Text(equals=[menuKb[0][0], menuKb[0][1], menuKb[0][2], menuKb[1][0], menuKb[1][1], menuKb[1][2]]))
async def menu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["menu"] = message.text
        user = User.getUser(message.chat.id)

        if message.text == menuKb[0][0] or message.text == menuKb[1][0]:
            await FirstState.subMenu.set()
            await bot.send_message(message.chat.id, choose[user.language], reply_markup=subMenuKeyboard[user.language])
        elif message.text == menuKb[0][2] or message.text == menuKb[1][2]:
            await bot.send_message(message.chat.id, chooseLang[0], reply_markup=lang_keyboard)
        else:
            await FirstState.subMenu.set()
            await bot.send_message(message.chat.id, choose[user.language], reply_markup=subMenuKeyboard2[user.language])


@dp.message_handler(Text(equals=[langKb[0], langKb[1]]))
async def change_lang(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        lang = 0 if message.text == "uz" else 1
        user = User.getUser(message.chat.id)
        User.changeLang(user.userId, lang)
        await bot.send_message(message.chat.id, mainMenu[lang], reply_markup=menuKeyboard[lang])


@dp.message_handler(Text(equals=[subMenuKb[0][0], subMenuKb[0][1], subMenuKb[0][2], subMenuKb[1][0], subMenuKb[1][1], subMenuKb[1][2],
                                 subMenuKb2[0][0], subMenuKb2[0][1], subMenuKb2[0][2], subMenuKb2[1][0], subMenuKb2[1][1], subMenuKb2[1][2]]),
                    state=FirstState.subMenu)
async def subMenu(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["subMenu"] = message.text
        menuData = data["menu"]
        user = User.getUser(message.chat.id)

        if menuData == menuKb[0][0] or menuData == menuKb[1][0]:

            await FirstState.next()

            await bot.send_message(message.chat.id, choose[user.language], reply_markup=typeKeyboard[user.language])
        else:
            data["type"] = None
            await FirstState.sale.set()

            await bot.send_message(message.chat.id, choose[user.language], reply_markup=saleKeyboard[user.language])


@dp.message_handler(Text(equals=[typeKb[0][0], typeKb[0][1], typeKb[0][2], typeKb[1][0], typeKb[1][1], typeKb[1][2]]),
                    state=FirstState.type)
async def MenuType(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["type"] = message.text
        user = User.getUser(message.chat.id)

        await FirstState.next()

        await bot.send_message(message.chat.id, choose[user.language], reply_markup=saleKeyboard[user.language])


@dp.message_handler(Text(equals=[saleKb[0][0], saleKb[0][1], saleKb[1][0], saleKb[1][1]]),
                    state=FirstState.sale)
async def sale(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["sale"] = message.text
        user = User.getUser(message.chat.id)

        if message.text == saleKb[0][1] or message.text == saleKb[1][1]:
            await FirstState.description.set()
            data["photo"] = None
            await bot.send_message(message.chat.id, sendDescription[user.language], reply_markup=types.ReplyKeyboardRemove())
        else:
            await FirstState.next()
            await bot.send_message(message.chat.id, sendPhoto[user.language], reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: types.ContentType.PHOTO, content_types=['photo'], state=FirstState.photo)
async def photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[-1].file_id
        user = User.getUser(message.chat.id)

        await FirstState.next()

        await bot.send_message(message.chat.id, sendDescription[user.language], reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text, state=FirstState.description)
async def description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["description"] = message.text
        user = User.getUser(message.chat.id)

        await FirstState.next()

        await bot.send_message(message.chat.id, fromLoc[user.language], reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text, state=FirstState.fromLoc)
async def fromLocFunc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["fromLoc"] = message.text
        user = User.getUser(message.chat.id)

        await FirstState.next()

        await bot.send_message(message.chat.id, whereLoc[user.language], reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text, state=FirstState.whereLoc)
async def whereLocFunc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["whereLoc"] = message.text
        user = User.getUser(message.chat.id)
        menuData = data["menu"]
        subMenuData = data["subMenu"]
        typeData = data["type"]
        saleData = data["sale"]
        desc = data["description"]
        fromLocData = data["fromLoc"]
        username = message.from_user.username
        if typeData is None:
            data["text"] = f"{subMenuData} {saleData}\n" \
                           f"{desc}\n" \
                           f"{fromLocData} --> {message.text}\n" \
                           f"Тел. {user.phone}, {user.name}, @{username}"
        else:
            data["text"] = f"{subMenuData} {typeData} {saleData}\n" \
                           f"{desc}\n" \
                           f"{fromLocData} --> {message.text}\n" \
                           f"Тел. {user.phone}, {user.name}, @{username}"
        await FirstState.next()
        if data["photo"] is None:
            await bot.send_message(message.chat.id, data["text"], reply_markup=sendKeyboard[user.language])
        else:
            await bot.send_photo(message.chat.id, data["photo"], caption=data["text"], reply_markup=sendKeyboard[user.language])


@dp.message_handler(Text(equals=[sendKb[0][0], sendKb[0][1], sendKb[1][0], sendKb[1][1]]), state=FirstState.send)
async def send(message: types.Message, state: FSMContext):
    async with state.proxy() as data:

        user = User.getUser(message.chat.id)
        if message.text == sendKb[0][0] or message.text == sendKb[1][0]:
            for i in Group.getAll():
                if data["photo"] is None:
                    await bot.send_message(i.groupId, data["text"])
                else:
                    await bot.send_photo(i.groupId, data["photo"], caption=data["text"])

            await bot.send_message(message.chat.id, sent[user.language])

        await bot.send_message(message.chat.id, mainMenu[user.language], reply_markup=menuKeyboard[user.language])

        await state.finish()
